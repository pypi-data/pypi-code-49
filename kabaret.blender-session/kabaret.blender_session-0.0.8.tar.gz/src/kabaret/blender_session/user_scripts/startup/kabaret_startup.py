from __future__ import print_function

import sys
import os
import logging

logger = logging.getLogger()


def patch_addon_paths():
    import addon_utils

    logger.info("[KABLENDER] Patching Addon Path to support multiple paths")

    extras = [
        i.strip() for i in os.environ["BLENDER_EXTRA_SCRIPTS"].split(";") if i.strip()
    ]
    logger.info("[KABLENDER] Settings Addon Paths:")
    for p in extras:
        logger.info("[KABLENDER]    " + p)

    addon_utils._orig_paths = addon_utils.paths

    def uas_addon_paths(extras=extras):
        return addon_utils._orig_paths() + extras

    addon_utils.paths = uas_addon_paths


def register():
    logger.info("[KABLENDER] Kabaret Blender Registering.")
    extra_sites = os.environ["BLENDER_EXTRA_SITES"].split(";")
    # sys.path.extend(extra_sites)
    import site

    for site_path in extra_sites:
        logger.info("[KABLENDER] Adding Site: " + site_path)
        site.addsitedir(site_path)

    patch_addon_paths()

    from kabaret.blender_session.session import BlenderEmbeddedSession

    logger.info("[KABLENDER] Building Session")
    session = BlenderEmbeddedSession(
        home_oid=os.environ.get("KABARET_SESSION_HOME"),
        session_name="KaBlender",
        debug=True,
    )
    # This is hacky, but I'm fine with it ^^
    # At least until https://gitlab.com/kabaretstudio/kabaret/issues/60 is fixed.
    import kabaret

    kabaret.session = session

    logger.info("[KABLENDER] Starting Session")
    session.cmds.Cluster.connect_from_env()
    session.start()
