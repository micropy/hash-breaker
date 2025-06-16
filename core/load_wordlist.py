def load_wordlist():
    try:
        with open("wordlist/800k.txt", "r", encoding='latin-1') as file:
            wordlist = [password.strip() for password in file]
            print("Wordlist loaded successfully.")
            return [wordlist[i::20] for i in range(20)]
    except FileNotFoundError:
        print("Wordlist file not found. Please ensure '800k.txt' exists in the 'wordlist' directory.")
        return