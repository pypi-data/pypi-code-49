import tarfile
import magic
import re
import os
import shutil
from os.path import islink, join, dirname, exists, isfile
from tempfile import NamedTemporaryFile

EXCLUDE_PREFIXES = [".", "/dev/", "/home/", "/proc/" "/sys/", "/etc/", "/run/"]


def create_tar(file_list):

    tmp_tar_file = NamedTemporaryFile(delete=False)
    with tarfile.open(tmp_tar_file.name, "w") as tar:
        while len(file_list) > 0:
            name = file_list[0]
            file_list.remove(name)
            skip_item = False
            for prefix in EXCLUDE_PREFIXES:
                if name.startswith(prefix):
                    skip_item = True
                    break
            if skip_item:
                continue
            tar.add(name)
            # Follow symbolic links
            if islink(name):
                link_target = os.readlink(name)
                link_target = join(dirname(name), link_target)
                if link_target not in file_list:
                    file_list.append(link_target)
            else:
                if isfile(name):
                    with open(name, "r") as f:
                        magic_name = magic.detect_from_fobj(f).name
                        dl = re.findall(
                            "dynamically linked, interpreter ([^,]*)", magic_name
                        )
                        if len(dl) == 0 or dl in file_list:
                            continue
                        dl = dl[0]
                        file_list.append(dl)
    return tmp_tar_file.name


def extract_tar(tar_filename, output_dir, force_overwrite):
    rootfs_dir = join(output_dir, "rootfs")
    if force_overwrite and exists(rootfs_dir):
        shutil.rmtree(rootfs_dir)
    os.makedirs(rootfs_dir)
    with tarfile.open(tar_filename, "r") as tar:
        tar.extractall(rootfs_dir)
    return output_dir


def create_config_json(bundle_dir, command_args):
    """ Create an OCI config file using a templatete """
    config_template = join(dirname(__file__), "config.json")
    with open(config_template) as template_file:
        template_data = template_file.read()
    quoted_args = [f'"{arg}"' for arg in command_args]
    quoted_args = "[{}]".format(",".join(quoted_args))
    template_data = template_data.replace('"%ARGS%"', quoted_args)
    bundle_config = join(bundle_dir, "config.json")
    with open(bundle_config, "w") as config_file:
        config_file.write(template_data)
