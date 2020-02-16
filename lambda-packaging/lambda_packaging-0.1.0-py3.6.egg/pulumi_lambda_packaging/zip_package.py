import zipfile
import glob
import os
import pulumi


class ZipPackage(object):
    def __init__(self,
                 project_root,
                 zipfile_name,
                 target_install_path,
                 include=["**"],
                 exclude=[]
                 ):
        self.project_root = project_root
        self.zipfile_name = f'.plp/{zipfile_name}'
        self.include = include
        self.exclude = exclude
        self.exclude.append(".plp/**")
        self.target_path = f'{self.project_root}/.plp'
        self.target_install_path = target_install_path
        if not os.path.isdir(self.target_path):
            os.makedirs(self.target_path, exist_ok=True)

    def match_glob_files(self, patterns: list):
        return [f for pattern in patterns
                for f in glob.glob(os.path.join(self.project_root, pattern), recursive=True)
                ]

    def filter_package(self):
        self.exclude_files = self.match_glob_files(self.exclude)
        self.include_files = self.match_glob_files(self.include)

        filtered_package = []
        if "**" in self.exclude:
            filtered_package = set(self.include_files)
        else:
            filtered_package = set(self.include_files) - \
                set(self.exclude_files)
        return filtered_package

    def zip_package(self):
        self.add_files(self.filter_package(), 'w', self.project_root)
        self.inject_requirements()

    def add_files(self, files, mode='w', base_path=""):
        zip_file = zipfile.ZipFile(self.zipfile_name, mode)
        for file in files:
            pulumi.log.info(os.path.relpath(file, base_path))
            zip_file.write(file, os.path.relpath(file, base_path))
        zip_file.close()

    def inject_requirements(self):
        requirement_files = glob.glob(os.path.join(self.target_install_path, '**'), recursive=True)
        self.add_files(requirement_files, 'a', os.path.join(self.project_root, self.target_install_path))
