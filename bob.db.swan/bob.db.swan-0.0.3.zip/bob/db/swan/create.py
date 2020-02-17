from os.path import join
import re
import pkg_resources
from bob.io.base import create_directories_safe
from .common import swan_file_metadata


def create_subparser(subparsers):
    parser = subparsers.add_parser(
        'create', help="Creates the PAD file lists of the dataset.")
    parser.set_defaults(func=_create)  # action


IDS = (('IDIAP_00055', 'NTNU_00053', 'IDIAP_00049', 'MPH-IND_00043',
        'IDIAP_00031', 'NTNU_00045', 'IDIAP_00028', 'MPH-FRA_00001',
        'NTNU_00013', 'NTNU_00026', 'NTNU_00032', 'MPH-IND_00001',
        'NTNU_00024', 'IDIAP_00054', 'NTNU_00042'),
       ('IDIAP_00059', 'NTNU_00047', 'MPH-IND_00017', 'NTNU_00031',
        'NTNU_00035', 'NTNU_00030', 'MPH-IND_00002', 'NTNU_00004',
        'MPH-IND_00005', 'IDIAP_00011', 'MPH-IND_00007', 'IDIAP_00002',
        'MPH-IND_00031', 'MPH-FRA_00002', 'IDIAP_00022'),
       ('NTNU_00041', 'MPH-IND_00024', 'IDIAP_00014', 'IDIAP_00020',
        'NTNU_00029', 'MPH-IND_00028', 'MPH-IND_00041', 'IDIAP_00005',
        'IDIAP_00029', 'IDIAP_00039', 'IDIAP_00038', 'NTNU_00040',
        'IDIAP_00025', 'NTNU_00039', 'IDIAP_00017'),
       ('NTNU_00044', 'MPH-FRA_00007', 'MPH-IND_00012', 'NTNU_00002',
        'IDIAP_00050', 'IDIAP_00034', 'IDIAP_00021', 'NTNU_00046',
        'MPH-IND_00020', 'NTNU_00007', 'NTNU_00037', 'NTNU_00010',
        'MPH-IND_00036', 'MPH-IND_00034', 'IDIAP_00043'),
       ('IDIAP_00048', 'MPH-IND_00032', 'IDIAP_00001', 'MPH-IND_00039',
        'NTNU_00003', 'MPH-IND_00046', 'MPH-IND_00009', 'MPH-IND_00042',
        'NTNU_00008', 'NTNU_00036', 'NTNU_00012', 'NTNU_00038', 'IDIAP_00040',
        'IDIAP_00018', 'NTNU_00034'),
       ('MPH-IND_00045', 'IDIAP_00042', 'NTNU_00001', 'IDIAP_00010',
        'NTNU_00019', 'MPH-IND_00044', 'MPH-IND_00051', 'MPH-IND_00018',
        'NTNU_00018', 'IDIAP_00035', 'MPH-FRA_00003', 'MPH-IND_00025',
        'MPH-FRA_00005', 'MPH-IND_00050', 'IDIAP_00026'),
       ('MPH-IND_00055', 'MPH-IND_00011', 'IDIAP_00052', 'MPH-IND_00023',
        'IDIAP_00030', 'MPH-IND_00033', 'IDIAP_00046', 'MPH-IND_00030',
        'MPH-IND_00016', 'IDIAP_00013', 'NTNU_00014', 'MPH-IND_00008',
        'NTNU_00022', 'NTNU_00017', 'IDIAP_00041'),
       ('IDIAP_00027', 'NTNU_00052', 'IDIAP_00033', 'NTNU_00016', 'NTNU_00023',
        'IDIAP_00016', 'MPH-IND_00015', 'MPH-IND_00047', 'IDIAP_00004',
        'MPH-FRA_00006', 'IDIAP_00015', 'IDIAP_00032', 'MPH-IND_00010',
        'MPH-IND_00013', 'NTNU_00054'),
       ('NTNU_00005', 'NTNU_00027', 'IDIAP_00051', 'MPH-IND_00048',
        'NTNU_00028', 'MPH-IND_00038', 'MPH-IND_00006', 'NTNU_00033',
        'NTNU_00025', 'NTNU_00020', 'NTNU_00051', 'MPH-IND_00004',
        'IDIAP_00036', 'NTNU_00006', 'NTNU_00021'),
       ('IDIAP_00006', 'NTNU_00015', 'IDIAP_00019',
        'IDIAP_00058', 'MPH-IND_00026', 'MPH-IND_00049',
        'NTNU_00043', 'MPH-IND_00037', 'IDIAP_00047',
        'IDIAP_00012', 'MPH-IND_00040', 'IDIAP_00060',
        'MPH-IND_00014', 'IDIAP_00003', 'IDIAP_00024'))
BIO_FOLDS = (('1', (0, 1, 2), (3, 4, 5, 6, 7, 8, 9)),
             ('2', (3, 4, 5), (0, 1, 2, 6, 7, 8, 9)),
             ('3', (6, 7, 8), (0, 1, 2, 3, 4, 5, 9)),
             ('4', (0, 3, 6), (1, 2, 4, 5, 7, 8, 9)),
             ('5', (1, 4, 9), (0, 2, 3, 5, 6, 7, 8)),)
PAD_FOLDS = (('1', (2, 0, 5, 8, 4), (9, 7), (1, 6, 3)),
             ('2', (7, 8, 2, 9, 1), (6, 0), (4, 3, 5)),
             ('3', (8, 3, 6, 0, 1), (5, 2), (9, 7, 4)),
             ('4', (9, 4, 7, 0, 2), (6, 5), (1, 8, 3)),
             ('5', (8, 2, 9, 0, 1), (5, 4), (6, 7, 3)))


def get_ids(ids):
    return tuple(x for i in ids for x in IDS[i])


def empty_norm(folder):
    path = join(folder, 'norm')
    create_directories_safe(path)
    path = join(path, 'train_world.lst')
    with open(path, 'w'):
        pass


def enrollment_probes(folder, files, group, pattern, ids, cls='enroll'):
    path = join(folder, group)
    create_directories_safe(path)
    if cls == 'probe':
        path = join(path, 'for_probes.lst')
    elif cls == 'attack':
        path = join(path, 'for_scores.lst')
    else:
        path = join(path, 'for_models.lst')
    regex = re.compile(pattern)
    files = filter(regex.search, files)
    with open(path, 'w') as f:
        for line in files:
            path = line.strip()
            client_id = swan_file_metadata(path)[0].id
            if client_id not in ids:
                continue
            if cls == 'probe':
                f.write('{0} {1}\n'.format(path, client_id))
            elif cls == 'attack':
                attack_type = path.split('/')[2]
                f.write('{0} {1} {1} attack/{2}\n'.format(
                    path, client_id, attack_type))
            else:
                f.write('{0} {1} {1}\n'.format(path, client_id))


def licit_protocols(
    out_folder, files, patterns, attack=False, modalities=('eye', 'face', 'voice')
):
    for fold, dev_ids, eval_ids in BIO_FOLDS:
        for modality in modalities:
            folder = '{}_{}_f{}'.format(out_folder, modality, fold)
            # create empty norm folder
            empty_norm(folder)

            # create enrollments
            pattern = patterns[(modality, 'enroll')]
            enrollment_probes(folder, files, 'dev',
                              pattern, get_ids(dev_ids))
            enrollment_probes(folder, files, 'eval',
                              pattern, get_ids(eval_ids))

            # create probes
            pattern = patterns[(modality, 'probe')]
            enrollment_probes(folder, files, 'dev',
                              pattern, get_ids(dev_ids),
                              cls='attack' if attack else 'probe')
            enrollment_probes(folder, files, 'eval',
                              pattern, get_ids(eval_ids),
                              cls='attack' if attack else 'probe')


def pad_list(folder, files, bf, pa, ids):
    create_directories_safe(folder)
    bf = re.compile(bf)
    pa = re.compile(pa)
    bf_files = filter(bf.search, files)
    pa_files = filter(pa.search, files)
    for name, lines in [
        ('for_real.lst', bf_files),
        ('for_attack.lst', pa_files),
    ]:
        with open(join(folder, name), 'w') as f:
            for line in lines:
                path = line.strip()
                client_id = swan_file_metadata(path)[0].id
                if client_id not in ids:
                    continue
                if name == 'for_real.lst':
                    f.write('{0} {1}\n'.format(path, client_id))
                else:
                    attack_type = path.split('/')[2]
                    f.write('{0} {1} {2}\n'.format(
                        path, client_id, attack_type))


def pad_protocols(out_folder, files, patterns):
    for fold, train_ids, dev_ids, eval_ids in PAD_FOLDS:
        folder = '{}_f{}'.format(out_folder, fold)

        for group, ids in (
            ('train', train_ids),
            ('dev', dev_ids),
            ('eval', eval_ids),
        ):
            bf = patterns[(group, 'bf')]
            pa = patterns[(group, 'pa')]
            pad_list(join(folder, group), files,
                     bf, pa, get_ids(ids))


def bio_protocol_1(out_folder, files):
    # This give the variation for indoor versus outdoor.
    # enroll with session 2
    # probe with session 3
    # Data Partition: 30% development and 70% evaluation.
    # 5 Folds
    # Enrollment: 2 images corresponding to 2 video.
    # Probe: All Video and Images.
    # For EYE biometrics: We can enroll Assisted and probe self capture.
    patterns = {
        ('eye', 'enroll'): r'.*session_02/iPhone/.*/.*_02_0[1-2]_p_3\.mp4',
        ('face', 'enroll'): r'.*session_02/iPhone/.*/.*_02_0[1-2]_p_1\.mp4',
        ('voice', 'enroll'): r'.*session_02/iPhone/.*/.*_02_0[1-2]_p_2\.mp4',
        ('eye', 'probe'): r'.*session_03/iPhone/.*/.*_03_((0[6-9]|10)_p_3\.png|0[3-4]_p_3\.mp4)',
        ('face', 'probe'): r'.*session_03/iPhone/.*/.*_03_0[1-2]_p_1.*',
        ('voice', 'probe'): r'.*session_03/iPhone/.*/.*_03_0[3-4]_p_2.*',
    }
    licit_protocols(out_folder, files, patterns)


def bio_protocol_2(out_folder, files):
    # This will give variation for Indoor controlled.
    # enroll with session 1
    # probe with session 2
    # Data Partition: 30% development and 70% evaluation.
    # 5 Folds
    # Enrollment: 2 images corresponding to 2 video.
    # Probe: All Video and Images.
    # For EYE biometrics: We can enroll Assisted and probe self capture.
    patterns = {
        ('eye', 'enroll'): r'.*session_01/iPhone/.*/.*_01_0[1-2]_p_3\.mp4',
        ('face', 'enroll'): r'.*session_01/iPhone/.*/.*_01_0[1-2]_p_1\.mp4',
        ('voice', 'enroll'): r'.*session_01/iPhone/.*/.*_01_0[1-2]_p_2\.mp4',
        ('eye', 'probe'): r'.*session_02/iPhone/.*/.*_02_((0[6-9]|10)_p_3\.png|0[3-4]_p_3\.mp4)',
        ('face', 'probe'): r'.*session_02/iPhone/.*/.*_02_0[1-2]_p_1.*',
        ('voice', 'probe'): r'.*session_02/iPhone/.*/.*_02_0[3-4]_p_2.*',
    }
    licit_protocols(out_folder, files, patterns)


def bio_protocol_3(out_folder, files):
    # This will give variation for indoor controlled versus indoor/outdoor uncontrolled
    # enroll with session 2
    # probe with session 3,4,5,6
    # Data Partition: 30% development and 70% evaluation.
    # 5 Folds
    # Enrollment: 2 images corresponding to 2 video.
    # Probe: All Video and Images.
    # For EYE biometrics: We can enroll Assisted and probe self capture.
    patterns = {
        ('eye', 'enroll'): r'.*session_02/iPhone/.*/.*_02_0[1-2]_p_3\.mp4',
        ('face', 'enroll'): r'.*session_02/iPhone/.*/.*_02_0[1-2]_p_1\.mp4',
        ('voice', 'enroll'): r'.*session_02/iPhone/.*/.*_02_0[1-2]_p_2\.mp4',
        ('eye', 'probe'): r'.*session_0[3-6]/iPhone/.*/.*_0[3-6]_((0[6-9]|10)_p_3\.png|0[3-4]_p_3\.mp4)',
        ('face', 'probe'): r'.*session_0[3-6]/iPhone/.*/.*_0[3-6]_0[1-2]_p_1.*',
        ('voice', 'probe'): r'.*session_0[3-6]/iPhone/.*/.*_0[3-6]_0[3-4]_p_2.*',
    }
    licit_protocols(out_folder, files, patterns)


def bio_protocol_4(out_folder, files):
    # This is just like protocol 3 but faces are talking faces
    patterns = {
        ('face', 'enroll'): r'.*session_02/iPhone/.*/.*_02_0[1-2]_p_2\.mp4',
        ('face', 'probe'): r'.*session_0[3-6]/iPhone/.*/.*_0[3-6]_0[3-4]_p_2.*',
    }
    licit_protocols(out_folder, files, patterns, modalities=['face'])


def spoof_protocol_3(out_folder, files):
    # This will give variation for indoor controlled versus indoor/outdoor
    # uncontrolled
    # enroll with session 2
    # probe with session 3,4,5,6
    # Data Partition: 30% development and 70% evaluation.
    # 5 Folds
    # Enrollment: 2 images corresponding to 2 video.
    # Probe: All Video and Images.
    # For EYE biometrics: We can enroll Assisted and probe self capture.
    patterns = {
        ('eye', 'enroll'): r'.*session_02/iPhone/.*/.*_02_0[1-2]_p_3\.mp4',
        ('face', 'enroll'): r'.*session_02/iPhone/.*/.*_02_0[1-2]_p_1\.mp4',
        ('voice', 'enroll'): r'.*session_02/iPhone/.*/.*_02_0[1-2]_p_2\.mp4',
        ('eye', 'probe'): r'pa-database/Eye/.*',
        ('face', 'probe'): r'pa-database/StillFace/.*',
        ('voice', 'probe'): r'pa-database/Voice/.*',
    }
    licit_protocols(out_folder, files, patterns, attack=True)


def spoof_protocol_4(out_folder, files):
    # spoof protocol for talking faces that matches bio_protocol_4
    patterns = {
        ('face', 'enroll'): r'.*session_02/iPhone/.*/.*_02_0[1-2]_p_2\.mp4',
        ('face', 'probe'): r'pa-database/TalkingFace/.*',
    }
    licit_protocols(out_folder, files, patterns, attack=True, modalities=['face'])


def all_pad_protocols(out_folder, files):
    # protocol 1
    # eye
    patterns = {
        ('train', 'bf'): r'.*session_02/iPhone/.*/.*_02_0[1-4]_p_3\.mp4',
        ('dev', 'bf'): r'.*session_02/iPhone/.*/.*_02_0[1-4]_p_3\.mp4',
        ('eval', 'bf'): r'.*session_0[2-6]/iPhone/.*/.*_0[2-6]_0[1-4]_p_3\.mp4',
        ('train', 'pa'): r'pa-database/Eye/PA\.EI\.1/.*',
        ('dev', 'pa'): r'pa-database/Eye/PA\.EI\.1/.*',
        ('eval', 'pa'): r'pa-database/Eye/PA\.EI\.1/.*',
    }
    pad_protocols(out_folder + 'pad_p1_pae1', files, patterns)
    patterns = {
        ('train', 'bf'): r'.*session_02/iPhone/.*/.*_02_0[1-4]_p_3\.mp4',
        ('dev', 'bf'): r'.*session_02/iPhone/.*/.*_02_0[1-4]_p_3\.mp4',
        ('eval', 'bf'): r'.*session_0[2-6]/iPhone/.*/.*_0[2-6]_0[1-4]_p_3\.mp4',
        ('train', 'pa'): r'pa-database/Eye/PA\.EI\.4/.*',
        ('dev', 'pa'): r'pa-database/Eye/PA\.EI\.4/.*',
        ('eval', 'pa'): r'pa-database/Eye/PA\.EI\.4/.*',
    }
    pad_protocols(out_folder + 'pad_p1_pae4', files, patterns)
    patterns = {
        ('train', 'bf'): r'.*session_02/iPhone/.*/.*_02_0[1-4]_p_3\.mp4',
        ('dev', 'bf'): r'.*session_02/iPhone/.*/.*_02_0[1-4]_p_3\.mp4',
        ('eval', 'bf'): r'.*session_0[2-6]/iPhone/.*/.*_0[2-6]_0[1-4]_p_3\.mp4',
        ('train', 'pa'): r'pa-database/Eye/PA\.EI\.5/.*',
        ('dev', 'pa'): r'pa-database/Eye/PA\.EI\.5/.*',
        ('eval', 'pa'): r'pa-database/Eye/PA\.EI\.5/.*',
    }
    pad_protocols(out_folder + 'pad_p1_pae5', files, patterns)
    # face
    patterns = {
        ('train', 'bf'): r'.*session_02/iPhone/.*/.*_02_0[1-2]_p_1\.mp4',
        ('dev', 'bf'): r'.*session_02/iPhone/.*/.*_02_0[1-2]_p_1\.mp4',
        ('eval', 'bf'): r'.*session_0[2-6]/iPhone/.*/.*_0[2-6]_0[1-2]_p_1\.mp4',
        ('train', 'pa'): r'pa-database/TalkingFace/PA\.F\.1/.*',
        ('dev', 'pa'): r'pa-database/TalkingFace/PA\.F\.1/.*',
        ('eval', 'pa'): r'pa-database/TalkingFace/PA\.F\.1/.*',
    }
    pad_protocols(out_folder + 'pad_p1_paf1', files, patterns)
    patterns = {
        ('train', 'bf'): r'.*session_02/iPhone/.*/.*_02_0[1-8]_p_2\.mp4',
        ('dev', 'bf'): r'.*session_02/iPhone/.*/.*_02_0[1-8]_p_2\.mp4',
        ('eval', 'bf'): r'.*session_0[2-6]/iPhone/.*/.*_0[2-6]_0[1-8]_p_2\.mp4',
        ('train', 'pa'): r'pa-database/TalkingFace/PA\.F\.5/.*',
        ('dev', 'pa'): r'pa-database/TalkingFace/PA\.F\.5/.*',
        ('eval', 'pa'): r'pa-database/TalkingFace/PA\.F\.5/.*',
    }
    pad_protocols(out_folder + 'pad_p1_paf5', files, patterns)
    patterns = {
        ('train', 'bf'): r'.*session_02/iPhone/.*/.*_02_0[1-8]_p_2\.mp4',
        ('dev', 'bf'): r'.*session_02/iPhone/.*/.*_02_0[1-8]_p_2\.mp4',
        ('eval', 'bf'): r'.*session_0[2-6]/iPhone/.*/.*_0[2-6]_0[1-8]_p_2\.mp4',
        ('train', 'pa'): r'pa-database/TalkingFace/PA\.F\.6/.*',
        ('dev', 'pa'): r'pa-database/TalkingFace/PA\.F\.6/.*',
        ('eval', 'pa'): r'pa-database/TalkingFace/PA\.F\.6/.*',
    }
    pad_protocols(out_folder + 'pad_p1_paf6', files, patterns)
    # voice
    patterns = {
        ('train', 'bf'): r'.*session_02/iPhone/.*/.*_02_0[1-8]_p_2\.mp4',
        ('dev', 'bf'): r'.*session_02/iPhone/.*/.*_02_0[1-8]_p_2\.mp4',
        ('eval', 'bf'): r'.*session_0[2-6]/iPhone/.*/.*_0[2-6]_0[1-8]_p_2\.mp4',
        ('train', 'pa'): r'pa-database/Voice/PA\.V\.4/.*',
        ('dev', 'pa'): r'pa-database/Voice/PA\.V\.4/.*',
        ('eval', 'pa'): r'pa-database/Voice/PA\.V\.4/.*',
    }
    pad_protocols(out_folder + 'pad_p1_pav4', files, patterns)
    patterns = {
        ('train', 'bf'): r'.*session_02/iPhone/.*/.*_02_0[1-8]_p_2\.mp4',
        ('dev', 'bf'): r'.*session_02/iPhone/.*/.*_02_0[1-8]_p_2\.mp4',
        ('eval', 'bf'): r'.*session_0[2-6]/iPhone/.*/.*_0[2-6]_0[1-8]_p_2\.mp4',
        ('train', 'pa'): r'pa-database/Voice/PA\.V\.7/.*',
        ('dev', 'pa'): r'pa-database/Voice/PA\.V\.7/.*',
        ('eval', 'pa'): r'pa-database/Voice/PA\.V\.7/.*',
    }
    pad_protocols(out_folder + 'pad_p1_pav7', files, patterns)
    # protocol 2
    # eye
    patterns = {
        ('train', 'bf'): r'.*session_02/iPhone/.*/.*_02_0[1-4]_p_3\.mp4',
        ('dev', 'bf'): r'.*session_02/iPhone/.*/.*_02_0[1-4]_p_3\.mp4',
        ('eval', 'bf'): r'.*session_0[2-6]/iPhone/.*/.*_0[2-6]_0[1-4]_p_3\.mp4',
        ('train', 'pa'): r'pa-database/Eye/.*',
        ('dev', 'pa'): r'pa-database/Eye/.*',
        ('eval', 'pa'): r'pa-database/Eye/.*',
    }
    pad_protocols(out_folder + 'pad_p2_eye', files, patterns)
    # face
    patterns = {
        ('train', 'bf'): r'.*session_02/iPhone/.*/.*_02_0[1-8]_p_[1-2]\.mp4',
        ('dev', 'bf'): r'.*session_02/iPhone/.*/.*_02_0[1-8]_p_[1-2]\.mp4',
        ('eval', 'bf'): r'.*session_0[2-6]/iPhone/.*/.*_0[2-6]_0[1-8]_p_[1-2]\.mp4',
        ('train', 'pa'): r'pa-database/TalkingFace/.*',
        ('dev', 'pa'): r'pa-database/TalkingFace/.*',
        ('eval', 'pa'): r'pa-database/TalkingFace/.*',
    }
    pad_protocols(out_folder + 'pad_p2_face', files, patterns)
    # voice
    patterns = {
        ('train', 'bf'): r'.*session_02/iPhone/.*/.*_02_0[1-8]_p_2\.mp4',
        ('dev', 'bf'): r'.*session_02/iPhone/.*/.*_02_0[1-8]_p_2\.mp4',
        ('eval', 'bf'): r'.*session_0[2-6]/iPhone/.*/.*_0[2-6]_0[1-8]_p_2\.mp4',
        ('train', 'pa'): r'pa-database/Voice/.*',
        ('dev', 'pa'): r'pa-database/Voice/.*',
        ('eval', 'pa'): r'pa-database/Voice/.*',
    }
    pad_protocols(out_folder + 'pad_p2_voice', files, patterns)


def _create(args):
    # list all files
    files = open(pkg_resources.resource_filename(
        __name__, 'lists/swan_noextra.lst')).readlines()
    # create protocols
    path = pkg_resources.resource_filename(__name__, 'lists/licit_p1')
    bio_protocol_1(path, files)
    path = pkg_resources.resource_filename(__name__, 'lists/licit_p2')
    bio_protocol_2(path, files)
    path = pkg_resources.resource_filename(__name__, 'lists/licit_p3')
    bio_protocol_3(path, files)
    path = pkg_resources.resource_filename(__name__, 'lists/spoof_p3')
    spoof_protocol_3(path, files)
    path = pkg_resources.resource_filename(__name__, 'lists/spoof_p4')
    spoof_protocol_4(path, files)
    path = pkg_resources.resource_filename(__name__, 'lists/')
    all_pad_protocols(path, files)
    path = pkg_resources.resource_filename(__name__, 'lists/licit_p4')
    bio_protocol_4(path, files)
