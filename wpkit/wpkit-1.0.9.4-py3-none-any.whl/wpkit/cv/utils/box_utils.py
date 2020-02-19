def json_load(f,encoding='utf-8',*args,**kwargs):
    import json
    with open(f,'r',encoding=encoding) as fp:
        return json.load(fp,*args,**kwargs)
def json_dump(obj,fp,encoding='utf-8',*args,**kwargs):
    import json
    with open(fp,'w',encoding=encoding) as f:
        json.dump(obj,f,*args,**kwargs)

def pickle_dump(obj,fp):
    import pickle
    with open(fp,'wb') as f:
        pickle.dump(obj,f)
def pickle_load(fp):
    import pickle
    with open(fp,'rb') as f:
        return pickle.load(f)


def sort_boxes(boxes):
    from functools import cmp_to_key
    boxes=[ltrb_to_ccwh(box) for box in boxes]
    boxes=[[box] for box in boxes]
    def block_cmp(b1, b2):
        list1 = [b1[0][0], b1[0][1], b1[0][2], b1[0][3]]
        list2 = [b2[0][0], b2[0][1], b2[0][2], b2[0][3]]
        if len(b1[0]) == 4:
            list1[0] += list1[2] / 2
            list1[1] += list1[3] / 2
            list2[0] += list2[2] / 2
            list2[1] += list2[3] / 2

        flag = 1
        if list1[0] > list2[0]:
            list1, list2 = list2, list1
            flag = -1

        if list2[1] + list1[3] / 2 < list1[1]:
            return flag
        return -flag

    boxes.sort(key=cmp_to_key(block_cmp), reverse=False)
    boxes=[box[0] for box in boxes]
    boxes=[ccwh_to_ltrb(box) for box in boxes]
    return boxes

def ltrb_to_four_corners(box):
    l,t,r,b=box
    # box2=[r,t,r,t,r,b,l,b]
    box2=[l,t,r,t,r,b,l,b]
    return box.__class__(box2)
def four_coners_to_ltrb(box,sort=False):
    x1,y1,x2,y2,x4,y4,x3,y3=box
    l=min(x1,x3)
    r=max(x2,x4)
    t=min(y1,y2)
    b=max(y3,y4)
    if sort:
        newbox = [min(l, r), min(t, b), max(l, r), max(t, b)]
    else:
        newbox=[l,t,r,b]
    return box.__class__(newbox)
def ltrb_to_ccwh(box):
    l, t, r, b = box
    w = r - l
    h = b - t
    cx = (l + r) // 2
    cy = (t + b) // 2
    return box.__class__([cx,cy,w,h])
def ccwh_to_ltrb(box):
    cx,cy,w,h=box
    l=cx-w//2
    t=cy-h//2
    r=cx+w//2
    b=cy+h//2
    return box.__class__([l,t,r,b])
def xywh_to_ltrb(box):
    x,y,w,h=box
    return box.__class__([int(i) for i in (x,y,x+w,y+h)])
def ltrb_to_xywh(box):
    l,t,r,b=box
    return box.__class__([l,t,r-l,b-t])
def trbox_to_ltrb(box):
    x,y,w,h=box
    return box.__class__([x,y,x+w,y+h])
def resize_box(box,size):
    cx,cy,w,h=ltrb_to_ccwh(box)
    nw,nh=size
    l=cx-nw//2
    r=cx+nw//2
    t=cy-nh//2
    b=cy+nh//2
    return box.__class__([l,t,r,b])
def limit_box(box,limits):
    if len(limits)==2:
        ml,mt=0,0
        mr,mb=limits
    else:
        assert len(limits)==4
        ml,mt,mr,mb=limits
    l,t,r,b=box
    l=max(ml,l)
    t=max(mt,t)
    r=min(mr,r)
    b=min(mb,b)
    if l>=r:
        return None
    if t>=b:return None
    return box.__class__([l,t,r,b])

def contain_chinese(text):
    import re
    zh_pattern = re.compile(u'[\u4e00-\u9fa5]+')
    def contain_zh(word):
        match = zh_pattern.search(word)
        return match
    return contain_zh(text)
def pad_box(box,pad_size=5,pad_ratio=None,max_w=None,max_h=None):
    from math import inf

    w=max_w or inf
    h=max_h or inf
    l,t,r,b=box
    bh=b-t
    bw=r-l
    if pad_ratio:
        pad_size=int(min(bh,bw)*pad_ratio)
    l=max(0,l-pad_size)
    t=max(0,t-pad_size)
    r=min(w,r+pad_size)
    b=min(h,b+pad_size)
    return box.__class__([l,t,r,b])
# #################Rich Box#########################
# #################Rich Box#########################

def enrich_box(box):
    from .tools import IterObject
    l,t,r,b=box
    B=IterObject(
        w=r - l,
        h = b - t,
        cx = (l + r) // 2,
        cy = (t + b) // 2,
        xmin=l,
        ymin=t,
        xmax=r,
        ymax=b,
        l=l,
        t=t,
        r=r,
        b=b
    )
    return B
def to_plain_box(box):
    return [box.xmin,box.ymin,box.xmax,box.ymax]
def _rowify_boxes(boxes,thresh=0.3):
    rows = []
    boxes.sort(key=lambda box: int(box['cy']))
    for box in boxes:
        if len(rows) == 0:
            row = [box]
            rows.append(row)
            continue
        last_box = rows[-1][-1]
        if box['cy'] <= last_box['cy'] + int(min(last_box['h'],box['h']) * thresh):
            rows[-1].append(box)
        else:
            row = [box]
            rows.append(row)
    for row in rows:
        row.sort(key=lambda box: int(box['cx']))
    return rows
def _group_boxes(boxes,mode='row'):
    if mode=='row':
        groups=_rowify_boxes(boxes)
    else:
        print("Only support row mode.")
        return
    return groups
def _union_boxes_herizonal(boxes,max_gap_ratio=2):
    newboxes=[]
    # boxes=[to_plain_box(box) for box in boxes]
    def union_two(box1,box2):
        newbox=[min(box1[0],box2[0]),min(box1[1],box2[1]),max(box1[2],box2[2]),max(box1[3],box2[3])]
        return newbox
    last=None
    for box in boxes:
        if not last:
            last=box
            newboxes.append(last)
        h_last=last[3]-last[1]
        h_now=box[3]-box[1]
        if((box[0]-last[2])<=min(h_last,h_now)*max_gap_ratio):
            last=union_two(last,box)
            newboxes[-1]=last
        else:
            last=box
            newboxes.append(last)
    # newboxes=[enrich_box(box) for box in newboxes]
    return newboxes
def group_and_union_boxes(boxes,union_thresh=2):
    boxes = [enrich_box(box) for box in boxes]
    rows=_group_boxes(boxes)
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            rows[i][j]=to_plain_box(rows[i][j])
    rows = [_union_boxes_herizonal(row,max_gap_ratio=union_thresh) for row in rows]
    return rows


