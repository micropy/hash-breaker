
<h1 align="center">Hash Breaker</h1>

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

**Hash Breaker** is a fast, multithreaded command-line tool to crack hashes (MD5, SHA1, SHA256, SHA512, bcrypt) with optional salt support and a beautiful `rich`-powered UI.

---

## 🚀 Features

- 🔍 Auto-detects hash types (MD5, SHA1, SHA256, SHA512, bcrypt)  
- 🧂 Supports salted hashes (`$SHA512$salt$hash`)  
- ⚡ Multithreaded cracking using `concurrent.futures`  
- 📁 Input via single hash or `.txt` file  
- 🎨 Stylish terminal with `rich` for colored outputs  
- 🧩 Modular — easy to extend with new hash functions

---
## 🛠 Installation

```bash
git clone https://github.com/micropy/hash-breaker.git
cd hash-breaker
pip install -r requirements.txt
```

Optionally, run the setup:

```bash
python setup.py
```

*(Installs dependencies, deletes `setup.py`, then runs the tool)*

---

## 🔐 Supported formats

* `$SHA...$salt$hash`
* `$2a$...` (bcrypt)

---

## 📁 Project Structure

```
hash-breaker/
├── core/
│   ├── engine.py
│   ├── load_wordlist.py
│   └── load_txt.py
├── hashes/
│   ├── dehash_md5.py
│   ├── dehash_sha1.py
│   ├── dehash_sha256.py
│   ├── dehash_sha512.py
│   └── dehash_bcrypt.py
├── wordlist/
│   └── rockyou.txt         # example (not included)
├── main.py                 # entry point
├── setup.py                # optional installer script
├── requirements.txt
└── README.md
```

---

## 📚 Dependencies

* [rich](https://github.com/Textualize/rich)
* [bcrypt](https://pypi.org/project/bcrypt/)

Install via:

```bash
pip install -r requirements.txt
```

---

## ⚙ Requirements

* Python 3.10 or newer
* A wordlist file (e.g. `rockyou.txt`) placed in `wordlist/`

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

## 👤 Author

Made with ❤️ by [@micropy](https://github.com/micropy)

⭐ If you find this project useful, please give it a star!
