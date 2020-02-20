def cli(hub):
    hub.pop.conf.integrate(
        ["pop_release"], cli="pop_release", roots=True, loader="yaml"
    )
    hub.pop_release.PATHNAME = hub.OPT["pop_release"]["name"].replace("-", "_")
    hub.pop_release.init.seq()


def seq(hub):
    ver = hub.OPT["pop_release"]["ver"]
    hub.pop_release.version.set_ver()
    hub.pop_release.version.set_doc()
    hub.pop_release.test.pytest()
    hub.pop_release.git.commit()
    hub.pop_release.git.tag()
    hub.pop_release.clean.all()
    hub.pop_release.rel.build()
    choice = input(f"Build for version {ver} is complete, Puth to git and pypi? [Y,n] ")
    if not choice:
        choice = "y"
    if choice.lower().startswith("y"):
        print("Pushing to git and pypi")
        hub.pop_release.rel.push()
        hub.pop_release.git.push()
