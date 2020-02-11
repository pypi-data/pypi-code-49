
def install_requirements():
    import os
    os.system("pip3 install flask")
    os.system("pip3 install Flask-Cors")
    os.system("pip3 install fire")
    os.system("pip3 install gitpython")

if __name__ == '__main__':
    install_requirements()
