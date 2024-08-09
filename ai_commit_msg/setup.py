import subprocess

def setup_dev():
    commands = [
        "pip3 install .",
        "pre-commit install",
        "pre-commit autoupdate"
    ]
    for cmd in commands:
        subprocess.run(cmd, shell=True, check=True)

if __name__ == "__main__":
    setup_dev()
