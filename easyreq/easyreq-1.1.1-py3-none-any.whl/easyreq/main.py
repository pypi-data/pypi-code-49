from argparse import ArgumentParser
import os, re


def main():
    parser = ArgumentParser(prog='easyreq', description='Tool for easy requirements generating')

    parser.add_argument('path', nargs='?', help='path to project directory or requirements.txt', default=False)

    args = parser.parse_args()

    currentdir = os.getcwd()

    reqpath = False
    dirpath = False

    if args.path:
        if os.path.isfile(args.path):
            reqpath = args.path
        elif os.path.isdir(args.path):
            dirpath = args.path

    if not reqpath and not dirpath:
        dirpath = currentdir

    if reqpath:
        # If path to requirements file was given - just modufy the file
        # Step 1: get all packages and versions form requirements file
        reqlist = getRequirements(reqpath)

        # Step 2: get packages form pip freeze and add minimum version to packages without one
        reqlist = getFreeze(reqlist)

        # Step 3: generate requirements file with packages and versions
        with open(reqpath, 'w') as file:
            for package in reqlist:
                version = reqlist[package]
                line = package
                if version:
                    line += version
                file.write(line + "\n")
        endProgram("File '" + reqpath + "' modified properly")
    else:
        # If no path given or path to directory given
        # If requirements file found ask if it should be overwritten
        reqpath = os.path.join(dirpath, 'requirements.txt')
        if os.path.isfile(reqpath):
            message = "I found existing requirements file in directory " + dirpath
            message += "\nIf you continue the file will be overwritten"
            message += "\nDo you want to continue?"
            message += "\n(y|n) [y]: "

            decision = input(message)

            while decision != "y":
                if decision == "n":
                    endProgram("File '" + reqpath + "' left unchanged")
                elif decision != "y" and decision != "":
                    decision = input(message)
                else:
                    decision = "y"
            print("yes")

        # Step 1: search for all imports in files
        packages = []
        for filePath in scanDir(dirpath):
            with open(filePath, 'r') as file:
                content = file.read()

                # search for 'from' in code
                froms = [m.start() for m in re.finditer('from ', content)]
                for start in froms:
                    start += 5
                    end = start + (content[start:]).find('import') - 1
                    add = content[start:end].strip()
                    if add not in packages and add != "" and not add.startswith("."):
                        if "." in add:
                            add = add.split(".")[0]
                        packages.append(add)

                # search for 'import' in code but only if it starts with that (not 'from ... import ...')
                imports = [m.start() for m in re.finditer('(^|\n)import ', content)]
                for start in imports:
                    start += 7
                    end = start + (content[start:]).find('\n')
                    imString = content[start:end]
                    if "," in imString:
                        for string in imString.split(","):
                            add = string.strip()
                            if "as" in add:
                                add = add.split(" as")[0]
                            if "." in add:
                                add = add.split(".")[0]
                            if add not in packages and add != "" and not add.startswith("."):
                                packages.append(add)
                    else:
                        add = imString.strip()
                        if "as" in add:
                            add = add.split(" as")[0]
                        if "." in add:
                            add = add.split(".")[0]
                        if add not in packages and add != "" and not add.startswith("."):
                            packages.append(add)

        # Step 2: get all packages form requirements file if it exists and merge it with imports found in files
        reqlist = getRequirements(reqpath)
        for package in packages:
            if package not in reqlist:
                reqlist[package] = False

        # Step 3: get packages form pip freeze and add minimum version to packages without one
        reqlist = getFreeze(reqlist)

        # Step 4: generate requirements file with packages and versions
        reqpath = os.path.join(dirpath, 'requirements.txt')
        with open(reqpath, 'w') as file:
            for package in reqlist:
                version = reqlist[package]
                line = package
                if not version:
                    continue
                line += version
                file.write(line + "\n")
        endProgram("File '" + reqpath + "' was successfully created/updated")


def scanDir(dir):
    filesToOmmit = ['.', '__pycache__', 'dist', 'build', 'setup', 'requirements', 'LICENSE', 'MANIFEST', 'README']
    foundFiles = []
    for name in os.listdir(dir):
        cont = False
        for ommit in filesToOmmit:
            if name.startswith(ommit):
                cont = True
        if cont:
            continue

        name = os.path.join(dir, name)
        if os.path.isfile(name):
            foundFiles.append(name);
        if os.path.isdir(name):
            foundFiles += scanDir(name);
    return foundFiles;


def getRequirements(reqpath):
    existingReqs = []
    requirements = {}

    if os.path.isfile(reqpath):
        with open(reqpath, 'r') as file:
            existingReqs = file.read().splitlines()

    if len(existingReqs) > 0:
        for req in existingReqs:
            foundArr = [m.start() for m in re.finditer('[<=>]', req)]
            if len(foundArr) > 0:
                package = req[0:foundArr[0]]
            else:
                package = req

            findEquals = req.find('==')
            equals = ""
            if findEquals > -1:
                equals = re.findall(r'([\d.]+)', req[findEquals:])[0]

            findMore = req.find('>')
            more = ""
            if findMore > -1:
                more = ">" + re.findall(r'(=?[\d.]+)', req[findMore:])[0]

            findLess = req.find('<')
            less = ""
            if findLess > -1:
                less = "<" + re.findall(r'(=?[\d.]+)', req[findLess:])[0]

            if more == "" and equals != "":
                more = ">=" + equals
                if less == "":
                    versionNum = int(re.findall(r'\d', more)[0]) + 1
                    less = "<" + str(versionNum)

            version = False
            if more != "":
                version = more
            if less != "":
                if version:
                    version += "," + less
                else:
                    version = less

            requirements[package] = version
    return requirements


def getFreeze(reqlist={}):
    try:
        from pip._internal.operations import freeze
    except ImportError:  # pip < 10.0
        from pip.operations import freeze

    installed_packages = freeze.freeze()
    for inst_pack in installed_packages:
        inst_pack = inst_pack.split('==')
        try:
            if not reqlist[inst_pack[0]]:
                versionNum = int(re.findall(r'\d', inst_pack[1])[0]) + 1
                reqlist[inst_pack[0]] = ">=" + inst_pack[1] + ",<" + str(versionNum)
        except KeyError:
            continue
    return reqlist


def endProgram(message=""):
    if message != "":
        print(message)
    exit()


main()
