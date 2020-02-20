from pathlib import Path

home_path = str(Path().home())
source_command = "source ~/.gut/aliases"


def add_alias_sourcing_to_file(name):
    path = Path("%s/%s" % (home_path, name))
    if path.exists():
        if source_command not in path.read_text():
            with open(path, 'a+') as file:
                file.write("\n%s" % source_command)
            file.close()


for file_name in [".zshrc"]: #".bash_profile", ".bashrc",
    add_alias_sourcing_to_file(file_name)
