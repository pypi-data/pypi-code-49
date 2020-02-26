#!/usr/bin/python3
import setuptools
import setuptools.command.build_py
import shutil
import sys
from pathlib import Path

LOCAL = str(Path(__file__).parent)
sys.path.append(LOCAL)
from __id__ import *


class ShortcutLinux(setuptools.command.build_py.build_py):
    def run(self):
        for s in SHORTCUTS:
            name, title = s
            filename = f"{ID}-{name}" if name else ID
            cmd = f"{ID} --{name}" if name else ID

            with open(Path(LOCAL) / f"{filename}.desktop", "w") as f:
                f.write("[Desktop Entry]\n")
                f.write(f"Name={title}")
                f.write("Type=Application\n")
                f.write("Categories=Utility;\n")
                f.write(f"Icon={filename}\n")
                f.write(f"Exec={cmd}\n")
        setuptools.command.build_py.build_py.run(self)


class ShortcutWindows(setuptools.command.build_py.build_py):
    def run(self):
        try:
            import sysconfig
            from win32com.client import Dispatch
            from win32com.shell import shell, shellcon

            desktop_dir = shell.SHGetFolderPath(0, shellcon.CSIDL_DESKTOP, None, 0)
            for s in SHORTCUTS:
                name, title = s
                filename = f"{ID}-{name}" if name else ID
                cmd = f"{ID}.exe --{name}" if name else f"{ID}.exe"

                shortcut = Path(desktop_dir) / f"{title}.lnk"
                icon = Path(sysconfig.get_path("data")) / "share" / "icons" / "win32-icons" / f"{filename}.ico"
                exe = Path(sysconfig.get_path("scripts")) / cmd

                sh = Dispatch("WScript.Shell")
                shortcut = sh.CreateShortCut(str(shortcut))
                shortcut.IconLocation = str(icon)
                shortcut.Targetpath = str(exe)
                shortcut.save()
        except ModuleNotFoundError:
            print("pywin32 import error: could not create a desktop shortcut")
        setuptools.command.build_py.build_py.run(self)


def copy_id():
    src = Path(LOCAL) / "__id__.py"
    dst = Path(LOCAL) / ID / "__id__.py"
    shutil.copyfile(src, dst)


def fetch_df():
    data_files = []
    win32_icons = []
    linux_icons = []
    linux_links = []

    for s in SHORTCUTS:
        name, title = s
        name = f"{ID}-{name}" if name else ID
        ico_path = Path() / ID / "frontend" / f"{name}.ico"
        svg_path = Path() / ID / "frontend" / f"{name}.svg"
        lnk_path = Path() / f"{name}.desktop"

        if ico_path.is_file():
            win32_icons.append(str(ico_path))

        if svg_path.is_file():
            linux_icons.append(str(svg_path))

        if lnk_path.is_file():
            linux_links.append(f"{name}.desktop")

    if win32_icons:
        win32_icons_dir = str(Path() / "share" / "icons" / "win32-icons")
        data_files += [(win32_icons_dir, win32_icons)]

    if linux_icons:
        data_files += [
            ("share/icons/hicolor/scalable/apps", linux_icons),
            ("share/applications", linux_links),
        ]
    return data_files


def setup():
    dependancies = set(DEPENDANCIES)
    try:
        from PyQt5 import uic
        uic.compileUiDir(Path(ID) / "frontend")
    except ImportError:
        dependancies.add("pyqt5")

    data_files = fetch_df()
    if sys.platform == "win32":
        cmdclass = {"build_py": ShortcutWindows}
    else:
        cmdclass = {"build_py": ShortcutLinux}

    setuptools.setup(
        name=ID,
        version=VERSION,
        description=DESCRIPTION,
        keywords=KEYWORDS,
        author=AUTHOR,
        url=URL,
        classifiers=CLASSIFIERS,
        install_requires=list(dependancies),
        cmdclass=cmdclass,
        data_files=data_files,
        package_data={'': ['frontend/*.svg']},  # ##
        packages=setuptools.find_packages(),
        entry_points={"gui_scripts": [f"{ID}={ID}:main"]},
    )


if __name__ == '__main__':
    copy_id()
    setup()
