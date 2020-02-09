from __future__ import unicode_literals
import os
import sys
import subprocess


class RadianApplication(object):
    instance = None
    r_home = None

    def __init__(self, r_home, ver):
        RadianApplication.instance = self
        self.r_home = r_home
        self.ver = ver
        super(RadianApplication, self).__init__()

    def set_env_vars(self, options):
        if options.vanilla:
            options.no_history = True
            options.no_environ = True
            options.no_site_file = True
            options.no_init_file = True

        if options.no_environ:
            os.environ["R_ENVIRON"] = ""
            os.environ["R_ENVIRON_USER"] = ""

        if options.no_site_file:
            os.environ["R_PROFILE"] = ""

        if options.no_init_file:
            os.environ["R_PROFILE_USER"] = ""

        if options.local_history:
            if not os.path.exists(".radian_history"):
                open(".radian_history", 'w+').close()

        doc_dir = os.path.join(self.r_home, "doc")
        include_dir = os.path.join(self.r_home, "include")
        share_dir = os.path.join(self.r_home, "share")
        if not (os.path.isdir(doc_dir) and os.path.isdir(include_dir) and os.path.isdir(share_dir)):
            try:
                paths = subprocess.check_output([
                    os.path.join(self.r_home, "bin", "R"), "--slave", "--vanilla", "-e",
                    "cat(paste(R.home('doc'), R.home('include'), R.home('share'), sep=':'))"
                ])
                doc_dir, include_dir, share_dir = paths.decode().split(":")
            except Exception:
                pass

        os.environ["R_DOC_DIR"] = doc_dir
        os.environ["R_INCLUDE_DIR"] = include_dir
        os.environ["R_SHARE_DIR"] = share_dir

        # enable crayon on windows
        if sys.platform.startswith("win"):
            os.environ["ANSICON"] = "1"

    def run(self, options, cleanup=None):
        from .session import create_radian_prompt_session
        from .console import create_read_console, create_write_console_ex
        import rchitect
        from . import rutils, settings

        self.set_env_vars(options)

        args = ["radian", "--quiet", "--no-restore-history"]

        if sys.platform != "win32":
            args.append("--no-readline")

        if options.no_environ:
            args.append("--no-environ")

        if options.no_site_file:
            args.append("--no-site-file")

        if options.no_init_file:
            args.append("--no-init-file")

        if options.ask_save is not True:
            args.append("--no-save")

        if options.restore_data is not True:
            args.append("--no-restore-data")

        rchitect.init(args=args)

        rutils.source_radian_profile(options.profile)

        settings = settings.radian_settings
        settings.load()
        self.session = create_radian_prompt_session(options, settings)

        rchitect.def_callback(name="read_console")(create_read_console(self.session))
        rchitect.def_callback(name="write_console_ex")(
            create_write_console_ex(self.session, settings.stderr_format))

        rutils.load_custom_key_bindings()

        from radian import main
        if main.cleanup:
            rutils.register_cleanup(main.cleanup)

        from . import reticulate
        reticulate.configure()

        # print welcome message
        if options.quiet is not True:
            self.session.app.output.write(rchitect.interface.greeting())

        rchitect.loop()
