import subprocess
import os

def install_requirements():
    try:
        subprocess.run(["pip3", "install", "-r", "requirements.txt"], check=True)
        print("Requirements installed successfully.")
    except subprocess.CalledProcessError:
        print("Error installing requirements.")

def delete_python_file():
    os.remove("setup.py")
    subprocess.run(["python3", "main.py"])

install_requirements()
delete_python_file()
