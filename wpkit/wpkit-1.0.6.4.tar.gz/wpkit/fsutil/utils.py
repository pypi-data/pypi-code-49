import os,shutil,glob

def copy_files_to(files,dst,overwrite=False):
    if not os.path.exists(dst):
        os.makedirs(dst)
    for i,f in enumerate(files):
        fn=os.path.basename(f)
        f2=dst+'/'+fn
        if os.path.exists(f2):
            if os.path.samefile(f, f2):
                print("ignoring same file:", f, f2)
                continue
            if not overwrite:
                raise Exception("file %s already exists."%(f2))
            else:
                print("overwriting %s to %s ..."%(f,f2))
                os.remove(f2)
        shutil.copy(f,f2)
def tranverse_files(dir,func):
    fs=glob.glob(dir+'/*')
    for f in fs:
        if os.path.isfile(f):
            func(f)
        elif os.path.isdir(f):
            tranverse_files(f,func)
def tranverse_dirs(dir,func):
    fs=glob.glob(dir+'/*')
    for f in fs:
        if os.path.isfile(f):
            pass
        elif os.path.isdir(f):
            func(f)
            tranverse_dirs(f,func)
def remove(path,not_exist_ok=True):
    if os.path.exists(path):
        if os.path.isdir(path) :
            shutil.rmtree(path)
        else:
            os.remove(path)
    elif not not_exist_ok:
        raise Exception('File or dir %s does not exist'%(path))
def remake(dir):
    if os.path.exists(dir):shutil.rmtree(dir)
    os.makedirs(dir)
def compare_dirs(src1,src2,dst='./compare_results'):
    files1=glob.glob(src1+'/*.*')
    files2=glob.glob(src2+'/*.*')
    same1=dst+'/1_same'
    same2=dst+'/2_same'
    diff1=dst+'/1_diff'
    diff2=dst+'/2_diff'
    remake(same1)
    remake(same2)
    remake(diff1)
    remake(diff2)
    names1=[os.path.basename(f) for f in files1]
    names2=[os.path.basename(f) for f in files2]
    ds1=set(names1)-set(names2)
    ds2=set(names2)-set(names1)
    ss=set(names1).intersection(set(names2))
    dl1=[src1+'/'+f for f in ds1]
    dl2=[src2+'/'+f for f in ds2]
    sl1=[src1+'/'+f for f in ss]
    sl2=[src2+'/'+f for f in ss]
    copy_files_to(dl1,diff1)
    copy_files_to(dl2,diff2)
    copy_files_to(sl1,same1)
    copy_files_to(sl2,same2)
