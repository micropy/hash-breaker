# hashes/dehash_sha256.py
from hashlib import sha256
from threading import Event
import time
from rich.console import Console

console = Console()
found_event = Event()

def dehash_sha256(hash_str: str, salt_str: str, chunk):
    start = time.time()
    # iterate over each password in the chunk
    for password in chunk:
        # stop if password found by another thread
        if found_event.is_set():
            return

        password_encoded = password.encode()
        salt_encoded = salt_str.encode()

        # try three different combinations of password and salt for sha256 hash
        combined1 = sha256(password_encoded + salt_encoded).hexdigest()
        combined2 = sha256(salt_encoded + password_encoded).hexdigest()
        combined3 = sha256(sha256(password_encoded).hexdigest().encode() + salt_encoded).hexdigest()

        # check if any of the hashes match the given hash
        if combined1 == hash_str or combined2 == hash_str or combined3 == hash_str:
            end = time.time()
            duration = round(end - start, 4)
            # print success message with password, hash, salt and duration
            console.print(f"[bold green]✔ password found:[/] [cyan]{password}[/] [dim](in {duration} seconds)[/]")
            console.print(f"[yellow]hash:[/] {hash_str}  [yellow]salt:[/] {salt_str}")
            # notify other threads to stop
            found_event.set()
            break
