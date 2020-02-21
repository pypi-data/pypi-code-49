import pkg_resources

try:
    __version__ = pkg_resources.get_distribution("mimosa-monomer").version
except Exception:
    __version__ = "unknown"
