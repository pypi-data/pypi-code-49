import json, os, re, sys
import subprocess, shutil
import uuid

verbose = False

def sep(char, times=10):
    print(" ".join(char for i in range(times)))

def generateOpenapi(spec, generator, outputDir):
    print("Generate {} from {} to {}".format(generator, spec, outputDir))
    if os.path.exists(outputDir):
        raise RuntimeError("tempDir {} exists already. Delete to continue.".format(cfg["tempDir"]))
    cmd = ["openapi-generator", "generate", "-i", spec, "-g", generator, "-o", outputDir]
    print("Execute command:", " ".join(cmd))
    if verbose:
        res = subprocess.run(cmd)
    else:
        res = subprocess.run(cmd, stdout=subprocess.DEVNULL)
    if res.returncode != 0:
        raise OSError("Generator exists with error code {}.".format(res.returncode))

def replaceInFiles(cfg):
    print("Replace in files")
    src = os.path.join(cfg["tempDir"], cfg["srcSubDir"])
    for dirname, dirnames, filenames in os.walk(src):
        for filename in filenames:
            srcFile = os.path.join(dirname, filename)
            subFile = os.path.relpath(srcFile, src)
            tempFile = srcFile + cfg["tempSuffix"]
            for pattern, replacements in cfg["replaceInFiles"].items():
                if re.match(pattern, subFile):
                    print("replace", pattern, "in", srcFile)
                    with open(srcFile, "rt") as fin:
                        with open(tempFile, "wt") as fout:
                            for line in fin:
                                for regex_search,regex_replace in replacements.items():
                                    if type(regex_replace) is list:
                                        regex_replace = "\n".join(regex_replace)
                                    if re.search(regex_search, line):
                                        print("       ", regex_search, "->", regex_replace)
                                    line = re.sub(regex_search, regex_replace, line)
                                fout.write(line)
                    shutil.move(tempFile, srcFile)

def overwrite(cfg):
    print("Mode: overwrite")
    if os.path.exists(cfg["outputDir"]):
        print("Delete output dir {}".format(cfg["outputDir"]))
        shutil.rmtree(cfg["outputDir"])
    src = os.path.join(cfg["tempDir"], cfg["srcSubDir"])
    dst = cfg["outputDir"]
    print("Move generated files from {} to {}".format(src, dst))
    shutil.move(src, dst)

def merge(cfg):
    print("Mode: merge")
    src = os.path.join(cfg["tempDir"], cfg["srcSubDir"])
    dst = cfg["outputDir"]
    if not os.path.exists(dst):
        print("Move generated files from {} to {}".format(src, dst))
        shutil.move(src, dst)
    for dirname, dirnames, filenames in os.walk(src):
        for currentDir in dirnames:
            srcDir = os.path.join(dirname, currentDir)
            relDir = os.path.relpath(srcDir, src)
            dstDir = os.path.join(dst, relDir)
            if re.match("|".join(cfg["dirsToKeep"] + [str(uuid.uuid4())]), relDir) and os.path.exists(dstDir):
                dstDir = os.path.join(dirname, currentDir + cfg["updatedDirSuffix"])
                print("keep     ", srcDir)
                print("          -> ", dstDir)
                shutil.move(srcDir, dstDir)
    for dirname, dirnames, filenames in os.walk(src):
        for filename in filenames:
            srcFile = os.path.join(dirname, filename)
            subFile = os.path.relpath(srcFile, src)
            dstFile = os.path.join(dst, subFile)
            if re.match("|".join(cfg["filesToKeep"] + [str(uuid.uuid4())]), subFile) and os.path.exists(dstFile):
                dstFile_orig = dstFile
                dstFile += cfg["updatedFileSuffix"]
                print("keep     ", dstFile_orig)
                print("         ", srcFile)
                print("          -> ", dstFile)
            else:
                print("overwrite", srcFile)
                print("          ->", dstFile)
                if not os.path.exists(os.path.split(dstFile)[0]):
                    os.makedirs(os.path.split(dstFile)[0])
            shutil.move(srcFile, dstFile)

def cleanup(cfg):
    if os.path.exists(cfg["tempDir"]):
        print("Delete tempDir {}".format(cfg["tempDir"]))
        shutil.rmtree(cfg["tempDir"])

def generate(cfg):
    sep(">")
    generateOpenapi(cfg["spec"], cfg["generator"], cfg["tempDir"])
    if "replaceInFiles" in cfg:
        replaceInFiles(cfg)
    if cfg["mode"] == "overwrite":
        overwrite(cfg)
    elif cfg["mode"] == "merge":
        merge(cfg)
    else:
        raise ValueError("Invalid mode: {}".format(cfg["mode"]))
    cleanup(cfg)
    sep("<")
    print()

def main(args):
    verbose_flags = ["-v", "--verbose"]
    verbose = len([arg for arg in args if arg in verbose_flags]) > 0
    configs = [arg for arg in args if arg not in verbose_flags]
    if len(configs) == 0:
        raise ValueError("No configuration file specified (must be JSON).")
    with open(config, "r") as f:
        cfg = json.load(f)
        for generator in cfg["generators"]:
            generate({**cfg["defaults"], **generator})

if __name__ == "__main__":
    main(sys.argv[1:])
