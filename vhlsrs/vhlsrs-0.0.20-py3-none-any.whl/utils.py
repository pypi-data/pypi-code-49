"""Miscellaneous tools"""

from plumbum import local


def run_script(vivado_script):
    vivado_hls = local["vivado_hls"]
    vivado_hls(str(vivado_script))
