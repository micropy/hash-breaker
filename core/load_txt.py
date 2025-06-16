# core/load_txt.py

def load_txt(file_path):
    try:
        with open(file_path, "r", encoding='utf-8') as file:
            file_content = file.read().splitlines()
            print("TXT loaded successfully.")
            return file_content
    except FileNotFoundError:
        print(f"TXT file not found: {file_path}. Please ensure the file exists.")
        return