# from zeroinger.compression.abs_cfu import AbstractCompressedFileUtil
#
#
# class CompressedFileUtil7z(AbstractCompressedFileUtil):
#     def compress_lines_to_archive(self, file_path: str, lines: str) -> None:
#         pass
#
#     def compress_iterator_to_archive(self, file_path: str, line_iterator: iter) -> None:
#         pass
#
#     def load_lines(self, file_name: str) -> iter:
#         pass
#
#     def load_line_iterator(self, file_name: str) -> iter:
#         with open(file_name, 'rb') as fh:  # automatically closes filehandler when finished
#             archive = py7zlib.Archive7z(fh)
#             current_line = ''
#             for block in archive.getblock():  # I do not know how you get a block of uncompressed data, so I ''abstract'' the call, you get the idea...
#                 current_line += block
#                 while '\n' in current_line:
#                     yield current_line[:current_line.index('\n') + 1]  # gives all until '\n' to the caller
#                     current_line = current_line[current_line.index(
#                         '\n') + 1:]  # now, initialize current_line with the rest of your block.
#             yield current_line  # return the end of file
#         pass
