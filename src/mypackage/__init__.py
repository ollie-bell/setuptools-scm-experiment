from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("mypackage")
except PackageNotFoundError:
    # package is not installed
    pass
