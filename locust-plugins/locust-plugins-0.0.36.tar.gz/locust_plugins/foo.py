import subprocess

print(subprocess.check_output("git remote show origin -n | grep h.URL | sed 's/.*://;s/.git$//'", shell=True))

