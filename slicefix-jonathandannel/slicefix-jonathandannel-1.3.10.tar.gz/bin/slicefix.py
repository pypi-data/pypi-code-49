#!/usr/bin/python3

from optparse import OptionParser
from bs4 import BeautifulSoup
from datetime import datetime
import slicefix
import re


def get_cli_args():
    cli_parser = OptionParser()
    cli_parser.add_option("-f", dest="file",
                          help="Path of HTML file to fix")
    cli_parser.add_option("-d", dest="domain",
                          help="Domain where the images are hosted")
    (args, _) = cli_parser.parse_args()
    return args


def read_input_file(path):
    parsed = None
    with open(path) as input:
        parsed = BeautifulSoup(input, "html.parser")
    return parsed


def add_style_tags(parsed_html):
    while parsed_html.find("img", {"style": None}):
        cur_img = parsed_html.find("img", {"style": None})
        cur_img["style"] = "display: block; border: 0; font-size: 0; line-height: 0"


def add_image_domains(domain, parsed_html):
    while parsed_html.find("img", {"src": re.compile("^images")}):
        cur_img = parsed_html.find("img", {"src": re.compile("^images")})
        cur_img["src"] = f"http://{domain}/eblasts/{cur_img['src']}"


def add_before_and_after_table(parsed_html):
    html_string_before = """ 
    <center>
      <div style="font-size:10px; font-family:Arial, Helvetica, sans-serif;">
        <br />
        You have been sent this e-blast because you have registered with South
        District.<br />
        View the online version of this e-blast <webversion>here.</webversion>
      </div>
      <br />
  """

    html_string_after = """
      <br />
      <div style="font-size:9px; font-family:Arial, Helvetica, sans-serif;">
        The Corporation <br />485 Broadview Ave. <br />Toronto, Ontario<br /><br />
        Sent by Fake Company<br />
        No longer interested in receiving information? Unsubscribe
        <unsubscribe>here</unsubscribe>.
      </div>
      <div
        style="font-size:9px; color:#FFF;width:750px;margin: 0 auto;text-align: center"
      >
        Pitchfork raclette small batch fingerstache thundercats selvage, truffaut
        eiusmod raw denim. Aute dolor readymade subway tile stumptown small batch in
        labore 90's truffaut irure. Minim umami plaid pinterest lorem. Health goth 
        poke bicycle rights, subway tile literally jean shorts enamel pin ugh humblebrag
        cardigan hammock reprehenderit vape mlkshk. Tilde kinfolk reprehenderit fam. 
        Tofu etsy +1 art party tumblr lyft blue bottle chia. Duis tofu venmo hashtag
        drinking vinegar, deserunt disrupt migas forage.
      </div>
    </center>
  """
    parsed_html.table.insert_before(html_string_before)
    parsed_html.table.insert_after(html_string_after)


def write_new_file(html_src_path, parsed_html):
    timestamp_secs = str(datetime.now())[-6:]
    new_filename = html_src_path[:-5] + f"_{timestamp_secs}.html"

    with open(new_filename, "w") as output:
        output.write(parsed_html.prettify(formatter=None))
        print(f"New file successfully created: {new_filename}")


def fix_and_save():
    cli_args = get_cli_args()
    (html_src_path, image_domain) = (cli_args.file, cli_args.domain)

    HTML_OBJECT = read_input_file(html_src_path)

    add_style_tags(HTML_OBJECT)
    add_before_and_after_table(HTML_OBJECT)
    add_image_domains(image_domain, HTML_OBJECT)
    write_new_file(html_src_path, HTML_OBJECT)

if __name__ == '__main__':
  fix_and_save()
