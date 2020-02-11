import subprocess

from pkg_scripts.misc_functions import check_if_exists, open_database, install, is_in_venv


def check_virtualenv_installation(conn, db):
    try:
        subprocess.run(["python3", "-m", "venv", "env"])
    except Exception as e:
        print(
            "We were not able to create your environment. The issue might be due to a missing 'python3-venv' package. "
            "To install the package, run the following command as root:\n\nsudo apt-get install python3-venv\n\nThen "
            "try again.")


def activate_env(db, engine):
    conn = open_database(engine)
    check_virtualenv_installation(conn, db)
    subprocess.run(["source", "env/bin/activate"])
    print("Environment Activated.")
    conn.close()


def deactivate_env(db, engine):
    status = is_in_venv()
    if status:
        print("Deactivating environment...")
        subprocess.run(["deactivate"])
        print("Environment Deactivated")
    else:
        print("No active environments")
        exit()
