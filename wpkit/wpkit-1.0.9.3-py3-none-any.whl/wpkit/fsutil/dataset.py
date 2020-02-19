import os, shutil, glob, random
from wpkit.fsutil import copy_files_to


def newdir(out_dir):
    if os.path.exists(out_dir): shutil.rmtree(out_dir)
    os.makedirs(out_dir)


def split_train_val(data_dir, train_dir, val_dir, val_split=0.1, num_val=None, ext='.jpg', shuffle=True, sort=False):
    newdir(train_dir)
    newdir(val_dir)
    fs = glob.glob(data_dir + '/*' + ext)
    if sort:
        fs.sort()
    elif shuffle:
        random.shuffle(fs)
    if not num_val:
        num_val = int(len(fs) * val_split)
    val_files = fs[:num_val]
    train_files = fs[num_val:]
    copy_files_to(train_files, train_dir)
    copy_files_to(val_files, val_dir)


def split_train_val_imagefolder(data_dir, train_dir, val_dir, val_split=0.1, num_val=None, ext='.jpg', shuffle=True,
                                sort=False):
    newdir(train_dir)
    newdir(val_dir)
    for cls in os.listdir(data_dir):
        cls_dir = data_dir + '/' + cls
        train_cls_dir = train_dir + '/' + cls
        val_cls_dir = val_dir + '/' + cls
        split_train_val(cls_dir, train_dir=train_cls_dir, val_dir=val_cls_dir, val_split=val_split, num_val=num_val,
                        ext=ext, shuffle=shuffle, sort=sort)

if __name__ == '__main__':
    split_train_val_imagefolder(
        data_dir='/home/ars/disk/datasets/car_datasets/stanford/images/train',
        train_dir='/home/ars/disk/datasets/car_datasets/stanford/classify_dataset/train',
        val_dir='/home/ars/disk/datasets/car_datasets/stanford/classify_dataset/val',
        val_split=0.1
    )