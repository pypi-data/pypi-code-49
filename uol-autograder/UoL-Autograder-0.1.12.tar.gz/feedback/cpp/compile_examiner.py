import subprocess
import argparse
import os
from tempfile import TemporaryFile

from ..general.contants import COMPILER
from ..util import decoder

def compile_cpp_to_o(cpp_file, out_file, working_dir=os.getcwd()):
    if not out_file.endswith(".o"):
        extension = out_file.split(".")[-1]
        out_file = out_file.replace(f".{extension}", ".o")

    with TemporaryFile() as t:  # TODO: Use unified function
        run_params = [COMPILER, '-std=c++11', '-fnon-call-exceptions', '-c', cpp_file, '-o', out_file]
        # print(" ".join([param for param in run_params if param != ""]))
        subprocess.call([param for param in run_params if param != ""],
                        cwd=working_dir, stderr=t)              # Run compiler in the working directory and capture its contents to a file
        t.seek(0)           # Return to the start of the file, and read its contents
        output = decoder(t.read()).replace(working_dir, "").split("\n")
    assert os.path.isfile(out_file), f"Compilation failed with:\n{output}"
    return out_file

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compile file to .o file")
    parser.add_argument('cpp_file', type=str, help="file to be compiled")
    parser.add_argument('out_file', type=str, help="target compiled file")
    
    args = parser.parse_args()
    compile_cpp_to_o(args.cpp_file, args.out_file)
