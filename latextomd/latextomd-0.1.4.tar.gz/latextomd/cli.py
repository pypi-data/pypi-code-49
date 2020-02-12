import argparse
import codecs
import sys

from latextomd import __version__, latextomd

parser = argparse.ArgumentParser(description="latextomd")
parser.add_argument("-i", help="input file path. Must be a .tex file")
parser.add_argument(
    "-o", help="output file name. By default the input file path with .md"
)
parser.add_argument("-d", action="store_true", help="debug mode")

args = parser.parse_args()


def predict_encoding(file_path, n_lines=20):
    """Predict a file's encoding using chardet"""
    import chardet

    # Open the file as binary data
    with open(file_path, "rb") as f:
        # Join binary lines for specified number of lines
        rawdata = b"".join([f.readline() for _ in range(n_lines)])

    return chardet.detect(rawdata)["encoding"]


def main():

    if not args.i:
        print("An input file must be specified.")
        sys.exit(2)
    source_file = args.i
    if not args.o:
        export_file = source_file.replace(".tex", ".md")
    else:
        export_file = args.o
    print("Source encoding:", predict_encoding(source_file))
    with codecs.open(source_file, "r", "utf-8") as f:
        latex_string = f.read()
        markdown_string = latextomd.to_markdown(latex_string, export_file)
        with codecs.open(export_file, "w", "utf-8") as f_out:
            f_out.write(markdown_string)


if __name__ == "__main__":
    main()
