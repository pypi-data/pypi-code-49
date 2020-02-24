# THIS FILE IS GENERATED FROM PADDLEPADDLE SETUP.PY
#
full_version    = '1.7.0'
major           = '1'
minor           = '7'
patch           = '0'
rc              = '0'
istaged         = False
commit          = '40cf4bd163b2c9c930c1be95117822458fcb77ab'
with_mkl        = 'ON'

def show():
    if istaged:
        print('full_version:', full_version)
        print('major:', major)
        print('minor:', minor)
        print('patch:', patch)
        print('rc:', rc)
    else:
        print('commit:', commit)

def mkl():
    return with_mkl
