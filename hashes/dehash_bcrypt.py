# hashes/dehash_bcrypt.py
import bcrypt
from threading import Event
import time
from rich.console import Console

console = Console()
found_event = Event()

def dehash_bcrypt(hash_str: str, chunk):
    start = time.time()

    # iterate over each password in the chunk
    for password in chunk:
        # if password already found by another thread, stop this one
        if found_event.is_set():
            return

        # check if the password matches the bcrypt hash
        if bcrypt.checkpw(password.encode(), hash_str.encode()):
            duration = round(time.time() - start, 4)
            # print success message with the password and time taken
            console.print(f"[bold green]✔ password found:[/] [cyan]{password}[/] [dim](in {duration} seconds)[/]")
            console.print(f"[yellow]hash:[/] {hash_str}")
            # signal other threads to stop
            found_event.set()
            break
