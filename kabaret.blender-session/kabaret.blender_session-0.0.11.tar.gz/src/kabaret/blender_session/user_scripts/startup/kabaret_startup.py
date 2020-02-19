from __future__ import print_function

import sys
import os
import logging

logger = logging.getLogger("[KABLENDER]")
logger.setLevel("INFO")


class logger:
    # TMP, for debug, sorry :p

    def info(text):
        print(text)


def patch_addon_paths():
    import bpy
    import addon_utils

    logger.info("[KABLENDER] Patching Addon Path to support multiple paths")

    extras = [
        i.strip() for i in os.environ["BLENDER_EXTRA_SCRIPTS"].split(";") if i.strip()
    ]

    # We used BLENDER_SCRIPT_PATH to force blender to execute this file at startup.
    # This means the default 'automatic' value for script path is not set.
    # Most users will complain that their addons are not available
    # (the ones they installed in a not-production-provided blender)
    # So we add it here:
    # TODO: Have an env-var to disable this if needed
    # In order to find out where the user-installed would be stored, we
    # build the path from the config resource (could not find a way to
    # ask blender for the roaming path)
    user_addons_path = os.path.normpath(
        os.path.join(bpy.utils.user_resource("CONFIG"), "..", "scripts", "addons")
    )
    if user_addons_path not in addon_utils.paths():
        extras.append(user_addons_path)

    logger.info("[KABLENDER] Original Script Paths:")
    for p in addon_utils.paths():
        logger.info("[KABLENDER]    " + p)
    logger.info("[KABLENDER] Extending Script Paths:")
    for p in extras:
        logger.info("[KABLENDER]    " + p)

    addon_utils._orig_paths = addon_utils.paths

    def uas_addon_paths(extras=extras):
        return addon_utils._orig_paths() + extras

    addon_utils.paths = uas_addon_paths


def register():
    logger.info("[KABLENDER] Kabaret Blender Registering.")
    extra_sites = os.environ["BLENDER_EXTRA_SITES"].split(";")

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
