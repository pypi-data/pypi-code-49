from typing import Tuple, List

from firebase_admin import firestore


class NotFound(Exception):
    pass


def get_site_key(site_key: str) -> dict:
    """Download a site key document and return the data as a dictionary"""
    if site_key == "":
        raise ValueError("Site key was an empty string.")

    db = firestore.client()
    doc = db.document(f"siteKeys/{site_key}").get()
    if doc.exists is False:
        raise NotFound(f"Site key {site_key} does not exist")
    return doc.to_dict()


def query_all_site_keys() -> List[Tuple[str, dict]]:
    """Download all site key documents and return a list of tuples with (id, data)"""
    db = firestore.client()
    docs = db.collection("siteKeys").get()
    return [(doc.id, doc.to_dict()) for doc in docs]


def update_site_key(site_key: str, updates: dict) -> None:
    """Update a single site key document"""

    db = firestore.client()
    db.document(f"siteKeys/{site_key}").update(updates)
    return
