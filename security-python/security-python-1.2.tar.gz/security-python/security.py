from werkzeug import *
def genuser(user, password):
    return {user: generate_password_hash(password)}

def checkpaswd(hash_, password):
    return check_password_hash(hash_, password)

