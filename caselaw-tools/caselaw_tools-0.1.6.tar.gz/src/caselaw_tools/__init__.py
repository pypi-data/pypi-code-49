# Let users know if they're missing any of our hard dependencies
hard_dependencies = ("numpy", "pytz", "tqdm", "pandas", "requests", "lxml")
missing_dependencies = []

for dependency in hard_dependencies:
    try:
        __import__(dependency)
    except ImportError as e:
        missing_dependencies.append("{0}: {1}".format(dependency, str(e)))

if missing_dependencies:
    raise ImportError(
        "Unable to import required dependencies:\n" + "\n".join(missing_dependencies)
    )
del hard_dependencies, dependency, missing_dependencies

def hello():
    return (u'Hello to you too')