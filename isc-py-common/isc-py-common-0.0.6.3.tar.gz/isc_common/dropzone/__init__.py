class Dz:
    dzchunkbyteoffset = None,
    dzchunkindex = None,
    dzchunksize = None,
    dztotalchunkcount = None,
    dztotalfilesize = None,
    dzuuid = None

    def __init__(self, POST):
        for k, v in POST.dict().items():
            setattr(self, k, v)
