#from PIL import Image, ImageFont, ImageDraw
#from saenews.sae3 import *
from saenews.utils import quote, put_quote


title = "Krishna Gate, or the 'K-gate', one of the five entry/exit point of IIT Madras was closed in Dec 2019 quoting security reasons"
title = "All you need to know about the IIT Madras 'K-Gate protests'"
tag_line = ""
input_file_orig = "KG2.png"

title_list = ["1. Krishna Gate, or the 'K-gate', one of the five entry-exit point of IIT Madras, was closed in Dec 2019 quoting security reasons.","2. The entry point is prone to dealing with illicit banned substances. And is out of city police patrol.","3. The closure of the gate has affected some students and research scholars as they have to travel an additional 0.9 Km to reach their destinations.", "4. A group of students affected by the closure held protest on 9th January demanding the administration to re-open the gate", "5. While the Dean and the Director rejected immediate reopening, they agreed to discuss the issue and come to a mutually agreeable solution.","6. While the administration and students were discussing about a feasible solution, two far-left organizations Ambedkar Periyar Circle and it's proxy ChintaBaar hijacked the protests and gave it a completely communal color.", "7. Another protest was held on 16th January under the leadership of far-left students in the name of re-opening the K-gate. The students raised slogans 'Smash Brahminical Patriarchy', 'Director is Hitler' and some anti-Hindu slogans. They portrayed posters of Director that resembled Hitler.", "8. Students who are genuinely affected by the closure are now confused. A student said 'I am not a Brahmin. But I have nothing to go against Brahminism or whatever. I am here against the K-gate closure. But the motto seems more than K-gate. The protest now has a completely new agenda'", "9. The administration has rejected unconditional re-opening of the K-gate and the far-left students are not willing to discuss any feasible solution.", "10. Ambedkar Periyar Circle is a far-left Anti-Hindu organisation that conducts events like Beef fest to disturb communal harmony in the institute. The organisation is known to have strong network with political orgs including CPI-M, SFI and PFI and was banned for the same in 2015." ]


for title in title_list:
    put_quote(title=title, tag_line=tag_line, black_strip_dims=(0, 0, 0, 1), input_file_orig=input_file_orig, output_file='', title_cord=(0.0505, 0.100), title_font_size=90, tag_font_size=50, title_width_ratio=0.45, border_width='', logo_border='', border_color='brown', title_text_font='fonts/ChunkFive-Regular.otf', tag_text_font='', tag_width_ratio=0.44, tag_cord=(0.035, 0.766), focus='false', tw_logo='SAENEWS',fb_logo='www.sae.news', logo=False)

from saenews.utils import quote, put_quote
tag_line = ""
title = ''
for i in range(1,12):
    input_file_orig = str(i) + ".jpeg"
    put_quote(title=title, tag_line=tag_line, black_strip_dims=(0, 0, 0, 0.05), input_file_orig=input_file_orig, output_file='', title_cord=(0.0505, 0.100), title_font_size=90, tag_font_size=50, title_width_ratio=0.45, border_width='', logo_border='', border_color='red', title_text_font='', tag_text_font='', tag_width_ratio=0.44, tag_cord=(0.035, 0.766), focus='false', tw_logo='saenews_',fb_logo='www.sae.news', logo=True)

