from typing import Tuple, List

from firebase_admin import firestore

DocumentSnapshot = firestore.firestore.DocumentSnapshot


class NotFound(Exception):
    pass


class AlreadyExists(Exception):
    pass


def does_site_key_exist(site_key: str) -> bool:
    """Return whether the site key exists in Firestore"""
    db = firestore.client()
    doc = db.document(f"siteKeys/{site_key}").get()
    return doc.exists


def does_doc_exist(docPath: str) -> bool:
    """Return whether a document exist in Firestore"""
    db = firestore.client()
    doc = db.document(docPath).get()
    return doc.exists


def get_site_key(site_key: str) -> dict:
    """Download a site key document and return the data as a dictionary"""
    if site_key == "":
        raise ValueError("Site key was an empty string.")

    db = firestore.client()
    doc = db.document(f"siteKeys/{site_key}").get()
    if doc.exists is False:
        raise NotFound(f"Site key {site_key} does not exist")
    return doc.to_dict()


def get_sk_user(site_key: str, uid: str) -> dict:
    """Download and return a site key user document"""
    if site_key == "":
        raise ValueError("Site key was an empty string.")
    if uid == "":
        raise ValueError("UID was an empty string.")
    db = firestore.client()
    doc = db.document(f"siteKeys/{site_key}/siteKeyUsers/{uid}").get()
    if doc.exists is False:
        raise NotFound(f"Site key user {uid} was not found.")
    return doc.to_dict()


def get_root_user(uid: str) -> dict:
    """Download and return the root user data."""
    if uid == "":
        raise ValueError("UID was an empty string.")
    db = firestore.client()
    doc = db.document(f"users/{uid}").get()
    if doc.exists is False:
        raise NotFound(f"Root user {uid} was not found.")
    output = doc.to_dict()
    output.update({"id": doc.id})
    return output


def query_all_site_keys() -> List[Tuple[str, dict]]:
    """Download all site key documents and return a list of tuples with (id, data)"""
    db = firestore.client()
    docs = db.collection("siteKeys").get()
    return [(doc.id, doc.to_dict()) for doc in docs]


def query_all_site_key_companies(site_key: str) -> List[Tuple[str, dict]]:
    """
    Download all site key company docs and return a list of tuples with (id, data)
    """
    db = firestore.client()
    docs = db.collection(f"siteKeys/{site_key}/siteKeyCompanies").get()
    result_list = [(doc.id, doc.to_dict()) for doc in docs]
    if len(result_list) == 0:
        raise NotFound("No site key companies were found. Please create one first.")
    return result_list


def query_all_sk_users(site_key: str) -> List[Tuple[str, dict]]:
    """Download all site key users for a given site key.

    Returns List of tuples (id, data_dict)
    """
    db = firestore.client()
    docs = db.collection(f"siteKeys/{site_key}/siteKeyUsers").get()
    return [(doc.id, doc.to_dict()) for doc in docs]


def query_all_site_locations(site_key: str) -> List[dict]:
    """Download all site key locations for a given site key.

    Returns List of dictionaries with added Firestore doc.id
    """
    db = firestore.client()
    docs = db.collection(f"siteKeys/{site_key}/locations").get()

    output: List[dict] = []
    for doc in docs:
        d = {"id": doc.id}
        d.update(doc.to_dict())
        output.append(d)

    return output


def update_site_key(site_key: str, updates: dict) -> None:
    """Update a single site key document"""

    db = firestore.client()
    db.document(f"siteKeys/{site_key}").update(updates)
    return


def set_site_key(site_key: str, updates: dict) -> None:
    """Set a single site key document"""

    db = firestore.client()
    db.document(f"siteKeys/{site_key}").set(updates)
    return


def set_site_key_user(site_key: str, uid: str, updates: dict) -> None:
    """Set a single site key user document"""
    db = firestore.client()
    db.document(f"siteKeys/{site_key}/siteKeyUsers/{uid}").set(updates)


def set_site_key_user_location(
    site_key: str, uid: str, location_id: str, updates: dict
) -> None:
    """Set a single site key user location document"""
    db = firestore.client()
    db.collection(f"siteKeys/{site_key}/siteKeyUsers/{uid}/userLocations").document(
        location_id
    ).set(updates)
    return


def set_site_key_user_private_data(site_key: str, uid: str, updates: dict) -> None:
    """Set the private data (permissions) document for a site key user"""
    db = firestore.client()
    db.document(f"siteKeys/{site_key}/siteKeyUsers/{uid}/privateColl/privateDoc").set(
        updates
    )
    return


def set_site_key_company(site_key: str, site_key_company: str, updates: dict) -> None:
    """Set a single site key company document"""

    db = firestore.client()
    db.document(f"siteKeys/{site_key}/siteKeyCompanies/{site_key_company}").set(updates)
    return
