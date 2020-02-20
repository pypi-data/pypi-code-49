from pathlib import Path

source_command = "source ~/.gut/aliases"
path = Path("~/.bash_profile")
path.touch()
if source_command not in path.read_text():
    with open(path, 'a+') as file:
        file.write("\n%s" % source_command)
    file.close()

