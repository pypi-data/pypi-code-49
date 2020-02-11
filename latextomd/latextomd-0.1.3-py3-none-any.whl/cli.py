import codecs
import sys

from latextomd import latextomd


def predict_encoding(file_path, n_lines=20):
    '''Predict a file's encoding using chardet'''
    import chardet

    # Open the file as binary data
    with open(file_path, 'rb') as f:
        # Join binary lines for specified number of lines
        rawdata = b''.join([f.readline() for _ in range(n_lines)])

    return chardet.detect(rawdata)['encoding']


def main():
    if len(sys.argv) == 1:
        print('Basic usage: latextomd source.tex export.md')
    else:
        if len(sys.argv) == 2:
            source_file = sys.argv[1]
            export_file = source_file.replace('.tex', '.md')
        elif len(sys.argv) == 3:
            source_file = sys.argv[1]
            export_file = sys.argv[2]

        print(predict_encoding(source_file))

        with codecs.open(source_file, 'r', 'utf-8') as f:
            latex_string = f.read()
            markdown_string = latextomd.to_markdown(latex_string, export_file)
            with codecs.open(export_file, 'w', 'utf-8') as f_out:
                f_out.write(markdown_string)


if __name__ == '__main__':
    main()
