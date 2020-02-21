    
def quote(title,tag_line,input_file, output_file='', title_cord = (0.035,0.666), title_font_size='', tag_font_size='', title_width_ratio='', border_width='', logo_border='', border_color='red', title_text_font = '', tag_text_font = '', tag_width_ratio=0.055, tag_cord='', focus='', *args, **kwargs):

    repo_path = get_path()
    if output_file == '':
        output_file = str(datetime.datetime.now()) + '.png'
    a = sae2() # Do not Remove # Class Initiation
    a.input_file = input_file # Name of Input  File
    file_name = input_file.split('.')[0]
    H,W = cv2.imread(a.input_file,1).shape[:2]
    img = Image.open(a.input_file)
    scale = (H/W)
    WW = 1440
    HH = round(WW*scale)
    W,H = WW,HH
    aa = img.resize((WW,HH)).save( '_resize.png')

    ## For the Title
    xy = (round(W*title_cord[0]),round(H*title_cord[1]))
    if title_text_font == '':
        title_text_font=repo_path + '/fonts/OTF/Akrobat-Black.otf'
    if title_font_size == '':
        title_font_size = W//25 # Font Size Enter Manually if required
    if title_width_ratio == '':
        title_width_ratio = 1 # Width of the caption. Reduce if the text is going outside the image
    title_width = (title_width_ratio*(W//25))
    if border_width == '':
        border_width = W//72 # Width of the Border
    if logo_border == '':
        logo_border = (W//36,W//36) # How much away from the edge should the logo appear?? Have put (Width of Image)/40. But change if required.
    font_title = ImageFont.truetype(title_text_font, size=title_font_size)
    draw = ImageDraw.Draw(img)
    w,h = draw.textsize(title, font=font_title)
    ### Do not edit below unless you know the exact working of the functions
    if focus == 'centre':
        out = a.get_vignet_face('_resize.png',fxy='centre' )
    elif focus == 'false':
        out = '_resize.png'
    else:
        out = a.get_vignet_face('_resize.png' )
    # If you do not want to put focus

    out = a.put_caption(input_file=out, caption=title,caption_width=title_width,font_size=title_font_size, xy = xy, text_font=title_text_font)        
    if tag_text_font == '':
        tag_text_font = repo_path + '/fonts/PTS56F.ttf'
    if tag_font_size == '':
        tag_font_size = W//36 # Font Size Enter Manually if required
    # xy_tagline = (xy[0], xy[1]+ font_size+10)
    if tag_cord == '':
        xy_tagline = (xy[0], xy[1]+h*2)
    else :
        xy_tagline = tag_cord[0]*W, tag_cord[1]*H
    tag_width = round(W*tag_width_ratio)
    out = a.put_caption(input_file=out, caption=tag_line,caption_width=tag_width,font_size=tag_font_size, xy = xy_tagline, text_font=cap_text_font)
    out = a.add_border(width=border_width,color=border_color,input_file=out,  )

    out = a.put_logo(input_file=out,border=logo_border, output_file=output_file)
    return(out)    
    
def add_border(input_image, output_image, border, border_color='black'):
    img = Image.open(input_image) 
    if isinstance(border, int) or isinstance(border, tuple):
        bimg = ImageOps.expand(img, border=border, fill=border_color)
    else:
        raise RuntimeError('Border is not an integer or tuple!')
    bimg.save(output_image)
    print (output_image)

def put_quote(input_file_orig, black_strip_dims=(0,0,0,0), *args, **kwargs):
    in_img = input_file_orig
    img = Image.open(in_img)
    W,H = img.size
    a = black_strip_dims
    border_len = (round(a[0]*W),round(a[1]*H),round(a[2]*W),round(a[3]*H))
    add_border(in_img,
               output_image='bordered.jpg',
               border=border_len)
    quote(input_file='bordered.jpg', *args,**kwargs)
    
    
    
