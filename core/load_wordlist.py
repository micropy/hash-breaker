def load_wordlist():
    try:
        with open("wordlist//800k.txt", "r") as file:
            wordlist = file.read().splitlines()
        print("Wordlist loaded successfully.")
    except FileNotFoundError:
        print("Wordlist file not found. Please ensure 'wordlist.txt' exists in the current directory.")