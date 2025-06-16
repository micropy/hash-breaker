# dehasher/core/engine.py

from hashes.dehash_md5 import *
from hashes.dehash_sha1 import *
from hashes.dehash_sha256 import *
from hashes.dehash_sha512 import *
from hashes.dehash_bcrypt import *
from core.load_wordlist import *
from core.load_txt import *

import re
from concurrent.futures import ThreadPoolExecutor
from threading import Event

from rich import print
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel

console = Console()
found_event = Event()
wordlist_chunks = load_wordlist()

hash_length_to_function = {
    32: dehash_md5,
    40: dehash_sha1,
    64: dehash_sha256,
    128: dehash_sha512
}

def split_hash_format(input_str: str):
    match = re.match(r'^\$?SHA(?:256|512)?\$?(\w+)\$(\w+)$', input_str)
    if match:
        part1, part2 = match.groups()
        hash_candidate = part1 if len(part1) in [64, 128] else part2
        salt_candidate = part2 if hash_candidate == part1 else part1
        # No print aquí, para evitar impresión múltiple
        return hash_candidate, salt_candidate
    else:
        return input_str.strip(), None

def dispatch_dehash(hash_value, salt_value):
    hash_value = hash_value.strip()

    if len(hash_value) in hash_length_to_function:
        dehash_function = hash_length_to_function[len(hash_value)]
        console.print(f"[bold cyan]Hash type detected:[/] [magenta]{dehash_function.__name__.split('dehash_')[1]}[/]")
        start_threaded_dehash(dehash_function, hash_value, salt_value)
    elif hash_value.startswith(('$2a$', '$2b$', '$2y$')):
        console.print("[bold green]Hash type detected:[/] [yellow]bcrypt[/]")
        start_threaded_dehash(dehash_bcrypt, hash_value, None)

    else:
        console.print(f"[bold red]Unknown hash type:[/] {hash_value}")
        return

def start_threaded_dehash(dehash_function, hash_value, salt_value):
    with ThreadPoolExecutor(max_workers=20) as executor:
        for chunk_index in range(20):
            wordlist_chunk = wordlist_chunks[chunk_index]
            args = (hash_value, salt_value, wordlist_chunk) if salt_value else (hash_value, wordlist_chunk)
            executor.submit(dehash_function, *args)

def dehash_from_txt():
    txt_path = Prompt.ask("[bold blue]Enter the path to the .txt file[/]")
    hash_lines = load_txt(txt_path)
    for hash_str in hash_lines:
        hash_part, salt_part = split_hash_format(hash_str)
        dispatch_dehash(hash_part, salt_part)

def dehash_single_hash():
    user_input = Prompt.ask("[bold blue]Enter the hash to dehash[/]")
    hash_part, salt_part = split_hash_format(user_input)
    dispatch_dehash(hash_part, salt_part)

def engine(option: int):
    options = {
        1: dehash_single_hash,
        2: dehash_from_txt
    }
    if option in options:
        mode = 'Single Hash' if option == 1 else 'Text File'
        console.print(Panel.fit(f"Mode: [bold yellow]{mode}[/]", title="Hash Decrypter"))
        options[option]()
    else:
        console.print("[bold red]Invalid option.[/]")
