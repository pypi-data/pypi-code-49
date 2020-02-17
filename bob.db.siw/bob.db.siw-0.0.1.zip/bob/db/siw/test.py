"""Test Units
"""
from bob.db.siw.config import database as db
from bob.db.siw import SIW_FRAME_SHAPE
import nose


def assert_nfiles(files, total, nbonafide, nattack):
    len_files = len(files)
    len_bonafide = len([f for f in files if f.attack_type is None])
    len_attack = len_files - len_bonafide
    assert len_files == total, (
        len_files,
        len_bonafide,
        len_attack,
        total,
        nbonafide,
        nattack,
    )
    assert len_bonafide == nbonafide, (len_bonafide, nbonafide)
    assert len_attack == nattack, (len_attack, nattack)


def test_database():
    # 80 identities in train
    # 10 identities in dev
    # 75 identities in eval
    # 8 BF recordings (2 sensor * 2 medium * 2 session)
    # 2 Print attacks (2 mediums)
    # 16 Replay attacks (2 sensor * 4 medium * 2 session)

    protocol = "Protocol_1"
    db.protocol = protocol
    assert len(db.all_files()[0])
    assert len(db.all_files()[1])
    assert_nfiles(db.objects(protocol=protocol), 4469, 1313, 3156)
    assert_nfiles(db.objects(protocol=protocol, groups="train"), 2140, 636, 1504)
    assert_nfiles(db.objects(protocol=protocol, groups="dev"), 276, 78, 198)
    assert_nfiles(db.objects(protocol=protocol, groups="eval"), 2053, 599, 1454)

    protocol = "Protocol_2_1"
    db.protocol = protocol
    assert_nfiles(db.objects(protocol=protocol), 2616, 636 + 78 + 599, 1303)
    assert_nfiles(db.objects(protocol=protocol, groups="train"), 1519, 636, 883)
    assert_nfiles(db.objects(protocol=protocol, groups="dev"), 198, 78, 120)
    assert_nfiles(db.objects(protocol=protocol, groups="eval"), 899, 599, 300)

    protocol = "Protocol_2_2"
    db.protocol = protocol
    assert_nfiles(db.objects(protocol=protocol), 2612, 636 + 78 + 599, 1299)
    assert_nfiles(db.objects(protocol=protocol, groups="train"), 1519, 636, 883)
    assert_nfiles(db.objects(protocol=protocol, groups="dev"), 198, 78, 120)
    assert_nfiles(db.objects(protocol=protocol, groups="eval"), 895, 599, 296)

    protocol = "Protocol_2_3"
    db.protocol = protocol
    assert_nfiles(db.objects(protocol=protocol), 2612, 636 + 78 + 599, 1299)
    assert_nfiles(db.objects(protocol=protocol, groups="train"), 1521, 636, 885)
    assert_nfiles(db.objects(protocol=protocol, groups="dev"), 198, 78, 120)
    assert_nfiles(db.objects(protocol=protocol, groups="eval"), 893, 599, 294)

    protocol = "Protocol_2_4"
    db.protocol = protocol
    assert_nfiles(
        db.objects(protocol=protocol), 1595 + 198 + 848, 636 + 78 + 599, 959 + 120 + 249
    )
    assert_nfiles(db.objects(protocol=protocol, groups="train"), 1594, 636, 958)
    assert_nfiles(db.objects(protocol=protocol, groups="dev"), 198, 78, 120)
    assert_nfiles(db.objects(protocol=protocol, groups="eval"), 849, 599, 250)

    protocol = "Protocol_3_1"
    protocol = protocol

    assert_nfiles(db.objects(protocol=protocol), 2792, 1313, 1479)
    assert_nfiles(db.objects(protocol=protocol, groups="train"), 937, 636, 301)
    assert_nfiles(db.objects(protocol=protocol, groups="dev"), 116, 78, 38)
    assert_nfiles(db.objects(protocol=protocol, groups="eval"), 1739, 599, 1140)

    protocol = "Protocol_3_2"
    protocol = protocol

    assert_nfiles(db.objects(protocol=protocol), 2990, 1313, 1677)
    assert_nfiles(db.objects(protocol=protocol, groups="train"), 1839, 636, 1203)
    assert_nfiles(db.objects(protocol=protocol, groups="dev"), 238, 78, 160)
    assert_nfiles(db.objects(protocol=protocol, groups="eval"), 913, 599, 314)


def test_frames():
    protocol = "Protocol_1"
    db.protocol = protocol
    if db.original_directory is None:
        raise nose.SkipTest(
            "Please configure bob.db.siw (refer to package documentation) "
            "to point to the directory where the database's raw data are. This"
            " way we can test more features of the database interface."
        )
    padfile = db.all_files()[0][0]
    assert padfile.number_of_frames == 599, padfile.number_of_frames
    for i, frame in enumerate(padfile.frames):
        pass
    assert i == 598, i
    assert frame.shape == SIW_FRAME_SHAPE, frame.shape


def test_annotations():
    protocol = "Protocol_1"
    db.protocol = protocol
    if db.original_directory is None:
        raise nose.SkipTest(
            "Please configure bob.db.siw (refer to package documentation) "
            "to point to the directory where the database's raw data are. This"
            " way we can test more features of the database interface."
        )
    padfile = db.all_files()[0][0]
    annot = padfile.annotations["0"]
    # leye x must be higher than reye x to conform to Bob format
    assert annot["leye"][1] > annot["reye"][1], annot
