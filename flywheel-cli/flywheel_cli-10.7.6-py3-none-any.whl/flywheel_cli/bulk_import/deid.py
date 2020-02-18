"""Provides load_deid_profile function"""

import datetime
import itertools

from flywheel_migration import deidentify

from .db.models import DeidLog


def load_deid_profile(profile_name, profiles):
    """Get deid profile"""
    profile_name = profile_name or "minimal"

    if profiles:
        loaded_profiles = []
        for config in profiles:
            profile = deidentify.DeIdProfile()
            profile.load_config(config)
            loaded_profiles.append(profile)
        profiles = loaded_profiles

    default_profiles = deidentify.load_default_profiles()
    for profile in itertools.chain(profiles, default_profiles):
        if profile.name == profile_name:
            errors = profile.validate()
            if errors:
                raise Exception("Invalid deid profile")
            return profile
    raise Exception("Unknown deid profile")

def get_deid_profile_config(profile_name, profiles):
    """Get raw (dict) deid profile config by name.

    Args:
        profile_name (str): Profile name
        profiles (list): Profiles

    Returns:
        dict: The found deid profile or None

    """
    if profiles:
        for profile in profiles:
            if profile["name"] == profile_name:
                return profile
    return None


def get_subjects_mapping_config(profile_name, profiles):
    """Get subjects mapping config of a given profile"""
    profile = get_deid_profile_config(profile_name, profiles)
    if profile:
        return profile.get("subjects-mapping")
    return None


class DeidLogger:  # pylint: disable=too-few-public-methods

    """Docstring for DeidLogger. """

    def __init__(self, deid_log_mapper, ingest_id):
        self.deid_log_mapper = deid_log_mapper
        self.ingest_id = ingest_id

    def write_entry(self, log_entry):
        """TODO: Docstring for write_entry.

        Args:
            log_entry (TODO): TODO

        Returns: TODO

        """
        path = log_entry.pop("path")
        log_type = log_entry.pop("type")
        deid_log = DeidLog(
            ingest_id=self.ingest_id,
            path=path,
            log_type=log_type,
            field_values=log_entry,
            created=datetime.datetime.now(),
        )
        self.deid_log_mapper.insert(deid_log)
