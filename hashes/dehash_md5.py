# hashes/dehash_md5.py
from hashlib import md5
from threading import Event
import time
from rich.console import Console

console = Console()
found_event = Event()

def dehash_md5(hash_str: str, salt_str: str, chunk):
    start = time.time()
    # iterate over each password in the chunk
    for password in chunk:
        # if password already found by another thread, stop this one
        if found_event.is_set():
            return
        
        password_encoded = password.encode()
        salt_encoded = salt_str.encode()

        # try three different combinations of password and salt for md5 hash
        combined1 = md5(password_encoded + salt_encoded).hexdigest()
        combined2 = md5(salt_encoded + password_encoded).hexdigest()
        combined3 = md5(md5(password_encoded).hexdigest().encode() + salt_encoded).hexdigest()

        # check if any of the combinations match the given hash
        if combined1 == hash_str or combined2 == hash_str or combined3 == hash_str:
            end = time.time()
            duration = round(end - start, 4)
            # print success message with password, hash, salt and duration
            console.print(f"[bold green]✔ password found:[/] [cyan]{password}[/] [dim](in {duration} seconds)[/]")
            console.print(f"[yellow]hash:[/] {hash_str}  [yellow]salt:[/] {salt_str}")
            # signal other threads to stop
            found_event.set()
            break
