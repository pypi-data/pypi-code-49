from BTrees.OOBTree import OOBTree
import transaction


def set_to_oobtree_if_not_set(root, path: str) -> None:
    if not hasattr(root, path):
        setattr(root, path, OOBTree())


def seed_db_if_needed(db):
    conn = db.open()
    root = conn.root
    set_to_oobtree_if_not_set(root, 'main')
    transaction.commit()