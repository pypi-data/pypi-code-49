from pathlib import Path
import csv
import json
import pkg_resources
import bob.extension


def get_file_names(datadir):
    """
    Get absolute path of files in a data directory (recursively).
    
    Parameters
    ----------
    
    data_dir : a Path object
    
    Returns:
    -------
    file_path: list
        a sorted list of paths to all files in the given data directory. Ignores hidden files (suchs as .DS_Store)
        
    """

    file_paths = sorted(list(datadir.glob('**/*?.*')))
    rel_file_paths = [f.relative_to(datadir) for f in file_paths]
    return rel_file_paths


def read_split(file):
    """
    Reads a csv file with two columns: image_file_name, ground_truth_file_name.
    
    Returns
    -------
    file_list : list
        list containing two tuples. The first one contains image file names, the second the ground truth file names
    """

    file = open(file,"r")
    rows = csv.reader(file)
    file_list = list(zip(*rows))
    file.close()
    return file_list


def create(args):
    """ 
    Writes a 'database' json file to disk

    Parameters
    ----------
    args.train   : csv containg train img, gt pairs
    args.test    : csv containg test img,gt pairs
    args.datadir : path to the dataset on disk
    args.output  : name of the output file

    Returns
    -------
    int : 0 

    """
    # read file name pairs as defined in the csv
    basedir = Path(pkg_resources.resource_filename(__name__, ''))
    train_split = read_split(basedir.joinpath(args.train))
    test_split = read_split(basedir.joinpath(args.test))
    
    # get actual file paths and create dictionary (filname, path)
    files = get_file_names(Path(args.datadir))
    filedict = dict([(f.name, f) for f in files])

    # map split to files
    train_images = [str(filedict[img]) for img in train_split[0]]
    train_ground_truths = [str(filedict[gt]) for gt in train_split[1]]
    test_images = [str(filedict[img]) for img in test_split[0]]
    test_ground_truths = [str(filedict[gt]) for gt in test_split[1]]
    
    # sense check 
    assert len(train_images) == len(train_ground_truths)
    assert len(test_images) == len(test_ground_truths)
    
    # zip together and create dict
    train = list(zip(train_images,train_ground_truths))
    test = list(zip(test_images,test_ground_truths))
    db = {'train':train,'test':test}

    # json
    with open(basedir.joinpath(args.output),'w') as outfile:
        json.dump(db, outfile, indent = 1)
    
    # return 0 for self-test
    return 0


def add_command(subparsers):
    """Add specific subcommands that the action "create" can use"""
    from argparse import SUPPRESS

    parser = subparsers.add_parser('create', help='Creates json file with train and test splits')
    parser.add_argument('-D', '--datadir', metavar='DIR', default=bob.extension.rc['bob.db.rimoner3.datadir'], help='path to RIM-ONE r3 dataset, default uses bob config settings (to check use: bob config show).')
    parser.add_argument('-T', '--train', metavar='STR', default='rimoner3_train_od.csv', help='csv containg train img,gt pairs')
    parser.add_argument('-E', '--test', metavar='STR', default='rimoner3_test_od.csv', help='csv containg test img,gt pairs')
    parser.add_argument('-O', '--output', metavar='STR', default='rimoner3_db_default_od.json', help='output file name')
    parser.add_argument('--self-test', dest="selftest", default=False, action='store_true', help=SUPPRESS)
    parser.set_defaults(func=create) #action
    parser.set_defaults(func=create) #action
