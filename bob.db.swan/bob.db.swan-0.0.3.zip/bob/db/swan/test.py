#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

"""Test Units
"""

import logging

logger = logging.getLogger(__name__)


def _test_numbers(files, n_total_files, n_clients, n_recordings,
                  n_devices, n_sessions, session_list, sites):
    n_clients_ = len(set(f.client_id for f in files))
    assert n_clients_ == n_clients, n_clients_

    n_recordings_ = len(set(f.nrecording for f in files))
    assert n_recordings_ == n_recordings, n_recordings_

    n_devices_ = len(set(f.device for f in files))
    assert n_devices_ == n_devices, n_devices_

    n_sessions_ = len(set(f.session for f in files))
    assert n_sessions_ == n_sessions, n_sessions_

    session_list_ = set(f.session for f in files)
    assert session_list_ == set(session_list), session_list_

    sites_ = set(f.client.institute for f in files)
    assert sites_ == set(sites), sites_

    assert len(files) == n_total_files, len(files)


def _test_annotation(db, files):
    try:
        annot = db.annotations(files[0])
        assert annot is None or isinstance(annot, dict), type(annot)
    except AssertionError:
        raise
    except Exception:
        logger.warn(
            "annotations tests failed. Maybe the annotations files are "
            "missing?", exc_info=True)


def test_pad_protocols():
    from .query_pad import Database

    protocol = 'pad_p2_face_f1'
    db = Database(protocol=protocol)

    bf, pa = db.all_files(groups='train')
    assert len(bf) == 750, len(bf)
    assert len(pa) == 1251, len(pa)

    # check the filter argument
    def filter_samples(sample):
        return "IDIAP" in sample.client_id

    db.all_files_options = dict(filter_samples=filter_samples)
    bf, pa = db.all_files(groups='train')
    assert len(bf) == 230, len(bf)
    assert len(pa) == 391, len(pa)
