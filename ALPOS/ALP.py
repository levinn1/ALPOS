import os
import shutil

def ls():
    for item in os.listdir():
        print(item)

def pwd():
    print(os.getcwd())

def cd(path):
    try:
        os.chdir(path)
    except FileNotFoundError:
        print(f"Directory '{path}' not found.")

def mkdir(directory):
    try:
        os.mkdir(directory)
    except FileExistsError:
        print(f"Directory '{directory}' already exists.")

def rmdir(directory):
    try:
        os.rmdir(directory)
    except FileNotFoundError:
        print(f"Directory '{directory}' not found.")
    except OSError:
        print(f"Directory '{directory}' is not empty.")

def touch(filename):
    with open(filename, 'w'):
        pass

def rm(filename):
    try:
        os.remove(filename)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

def cp(source, destination):
    try:
        shutil.copy(source, destination)
    except FileNotFoundError:
        print(f"Source file '{source}' not found.")

def mv(source, destination):
    try:
        shutil.move(source, destination)
    except FileNotFoundError:
        print(f"Source '{source}' not found.")

def help_command():
    commands = {
        'ls': '    List files and directories in the current directory.',
        'pwd': '   Display the current working directory.',
        'cd': '    Change the current working directory.',
        'mkdir': ' Create a new directory.',
        'rmdir': ' Remove an empty directory.',
        'touch': ' Create an empty file.',
        'rm': '    Remove a file.',
        'cp': '    Copy a file.',
        'mv': '    Move or rename a file or directory.',
        'help': '  Display this help message.',
        'clear': ' Clear the terminal screen.',
        'exit': '  Exit the CLI.',
        'tree': '  Display the directory structure in a tree format.',
        'search': 'Search for a file or directory by name.',
        'log': '   Save command history to a log file.',
        'ascii': ' Display an ASCII art banner.'
    }
    for cmd, desc in commands.items():
        print(f"{cmd}: {desc}")

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def exit_cli():
    print("Exiting. Goodbye!")
    exit()

def tree(path=".", indent=""):
    items = os.listdir(path)
    for i, item in enumerate(items):
        if i == len(items) - 1:
            print(indent + "\u2514\u2500 " + item)
            new_indent = indent + "   "
        else:
            print(indent + "\u251c\u2500 " + item)
            new_indent = indent + "\u2502  "
        if os.path.isdir(os.path.join(path, item)):
            tree(os.path.join(path, item), new_indent)

def search(pattern, path="."):
    for root, dirs, files in os.walk(path):
        for name in dirs + files:
            if pattern in name:
                print(os.path.join(root, name))

def log(command):
    with open("command_log.txt", "a") as log_file:
        log_file.write(command + "\n")

def ascii_art():
    banner = """
    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    +++++++++++++++++++++++++++++++++++++++++++++*******##**++++++++++++++++++++++++++++++++++++++++++++
    ++++++++++++++++++++++++++++++++++++++++**##%%%%##%%%%%%%%##*+++++++++++++++++++++++++++++++++++++++
    +++++++++++++++++++++++++++++++++++++*#%%%@@@@@@@@@@@@@@@@%@%%%#*+++++++++++++++++++++++++++++++++++
    +++++++++++++++++++++++++++++++++++#%@@@@@@@@@@@@@@@@@@@@@@@@@@%%%*+++++++++++++++++++++++++++++++++
    ++++++++++++++++++++++++++++++++*#%@@@@@@@@@@@@@@@%%%%%%@%@@@@@@@@%%*+++++++++++++++++++++++++++++++
    +++++++++++++++++++++++++++++++#%@@@@@@@@%%%%%%%%%%%%%#%%%%%%%%%@@@@@%*+++++++++++++++++++++++++++++
    ++++++++++++++++++++++++++++++#@@@@@@@@%%%%%########**########%%%%%%@@%*++++++++++++++++++++++++++++
    +++++++++++++++++++++++++++++#@@@@@@@%%%%%%########********####%%%%%%@@@*+++++++++++++++++++++++++++
    ++++++++++++++++++++++++++++*@@@@@@@@%%%%##########*****+***###%%%%%%%@@%+++++++++++++++++++++++++++
    ++++++++++++++++++++++++++++%@@@@@@@%%%%#######*******+++****###%%%%%%%@@#++++++++++++++++++++++++++
    +++++++++++++++++++++++++++*@@@@@@@@%%%%%########*#***+++++***###%%%%%%%@%++++++++++++++++++++++++++
    +++++++++++++++++++++++++++#@@@@@@@%%%%%########**************####%%%%%%@@*+++++++++++++++++++++++++
    +++++++++++++++++++++++++++#@@@@@@@%%#####***************+++++**###%%%%%%%*+++++++++++++++++++++++++
    +++++++++++++++++++++++++++#@@@@@@%%%%%%%#***+++*++++++++====+*#####%%%%@%*+++++++++++++++++++++++++
    +++++++++++++++++++++++++++#@@@@@@@@@@@@@@%%#*++++++++++##%%%%%%%%%@%%%%@@*+++++++++++++++++++++++++
    +++++++++++++++++++++++++++*@@@@@@%%###%%@@@%%#********##%%#########%%%%@@*+++++++++++++++++++++++++
    ++++++++++++++++++++++++++++@@@@@%#########%%@%%##*+**######*****####%%%%@#*++++++++++++++++++++++++
    +++++++++++++++++++++++++++%@@@@%%@@@%%%%#++*#%@@%*=**###%#%%%%*#%%####%%%#%++++++++++++++++++++++++
    +++++++++++++++++++++++++++#@@@%%%@@%++%@#==*#%@@%*=**#*#*++%%*-=#%#**#%%%##++++++++++++++++++++++++
    +++++++++++++++++++++++++++*%@@%%%%@@%%###***#%%%#*++**#*+*******#****##%##*++++++++++++++++++++++++
    +++++++++++++++++++++++++++*%@@%%######*****#%%@%#*++****+==+===++++*##%%##+++++++++++++++++++++++++
    ++++++++++++++++++++++++++++@@@%%##*********#%@@%#*++**##*=========+*##%%%*+++++++++++++++++++++++++
    ++++++++++++++++++++++++++++%@@%%##*********%@@@%#******#*+========+*#%%%%++++++++++++++++++++++++++
    ++++++++++++++++++++++++++++%@@%%%###******%@%#%%*++=+***#*+===++++*#%%%%%++++++++++++++++++++++++++
    ++++++++++++++++++++++++++++%@@@%%###****#%%%*+#%#*+++****#+++==++*##%%%%%++++++++++++++++++++++++++
    ++++++++++++++++++++++++++++#@@@%%%###**##%%%%%@@%%##+*%%#+==+==+**##%%%%#++++++++++++++++++++++++++
    ++++++++++++++++++++++++++++#@@@@%%%##***##%%@@@%#*%%#%#***++++++*###%%%%*++++++++++++++++++++++++++
    +++++++++++++++++++++++++++++%@@@%%%####%%%@@@@@%#%%%%%%%%%%##*+**##%%%%#+++++++++++++++++++++++++++
    +++++++++++++++++++++++++++++*@@@@%%%%%@@@@%%#*###*++++**#%%@%#**##%%%%%*+++++++++++++++++++++++++++
    ++++++++++++++++++++++++++++++*@@@%%%%@@@%##%%##%%%*#####**#%%%**####%%*++++++++++++++++++++++++++++
    +++++++++++++++++++++++++++++++#@@@%%%@@%%######***********#%%%####%%%*+++++++++++++++++++++++++++++
    ++++++++++++++++++++++++++**#%%@@@@@@%%%%%%%%%###+=++++*#***%%%###%%%*++++++++++++++++++++++++++++++
    ++++++++++++++++++++++*#%@@@@@%%@@@@@@@@%%%%%%%%%%%%%%%###**%%%%%%@@%%%#*+++++++++++++++++++++++++++
    ++++++++++++++++*##%@@@@@@@@@%%@@@@@@@@@@@%%@%@@@%%%%%%#%%%%@@@%@@%#%%@@@%%#*+++++++++++++++++++++++
    +++++++++++*#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%@%@@@@@@%%##%%#%@@@@@@%#*+++++++++++++++++++
    +++++++*#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%#%%%@@@@@@%####%%%%%%@@@@@@@@%#*+++++++++++++++
    ++++*#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@@%%%%@@@@@@@@#####%%####%@@@@@@@@@@@@%*+++++++++++
    *#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@######%%#####@@@@@@@@@@@@@@@%#*+++++++
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%############*%@@@@@@@@@@@@@@@@@@@%#++++
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%#################**@@@@@@@@@@@@@@@@@@@@@@@@#*
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@@@@@%%%%%%%%%%%##################*#**@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%@@%%%%%%%%####################***%@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%##%####################*#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%##################****#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%#########*********##%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

    """
    print(banner)

def main():
    print("Welcome to python CLI Application! Type 'help' for a list of commands.")
    while True:
        current_directory = os.getcwd()
        command = input(f"{current_directory}$ ").strip()
        log(command)  # Log every command

        if command.startswith("ls"):
            ls()
        elif command.startswith("pwd"):
            pwd()
        elif command.startswith("cd"):
            path = command[3:].strip()
            cd(path)
        elif command.startswith("mkdir"):
            directory = command[6:].strip()
            mkdir(directory)
        elif command.startswith("rmdir"):
            directory = command[6:].strip()
            rmdir(directory)
        elif command.startswith("touch"):
            filename = command[6:].strip()
            touch(filename)
        elif command.startswith("rm"):
            filename = command[3:].strip()
            rm(filename)
        elif command.startswith("cp"):
            parts = command[3:].strip().split()
            if len(parts) == 2:
                cp(parts[0], parts[1])
            else:
                print("Contoh: cp <source> <destination>")
        elif command.startswith("mv"):
            parts = command[3:].strip().split()
            if len(parts) == 2:
                mv(parts[0], parts[1])
            else:
                print("Contoh: mv <source> <destination>")
        elif command == "help":
            help_command()
        elif command == "clear":
            clear()
        elif command == "exit":
            exit_cli()
        elif command.startswith("tree"):
            path = command[5:].strip() or "."
            tree(path)
        elif command.startswith("search"):
            parts = command[7:].strip().split()
            if len(parts) == 1:
                search(parts[0])
            else:
                print("Usage: search <pattern>")
        elif command.startswith("log"):
            print("Command history saved to 'command_log.txt'.")
        elif command == "ascii":
            ascii_art()
        else:
            print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()
