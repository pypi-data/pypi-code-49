
import subprocess,os
import imp
def TTSnorm(text):
    A=imp.find_module('vinorm')[1]

    print(A)
    I=A+"/input.txt"
    with open(I,"w+") as fw:
        fw.write(text)

    myenv = os.environ.copy()
    myenv['LD_LIBRARY_PATH'] = A+'/lib'

    E=A+"/main"
    subprocess.check_call([E], env=myenv, cwd=A)
    
    O=A+"/output.txt"
    with open(O,"r") as fr:
        text=fr.read()

    TEXT=""
    A=text.split("#line#")
    for a in A:
        B=a.split("#@#")[2]
        text+=B + " . "


    return TEXT