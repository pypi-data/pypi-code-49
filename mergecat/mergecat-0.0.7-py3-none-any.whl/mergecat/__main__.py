from subprocess import call
from os import path, remove
import click
import tempfile


@click.command(help="Given a video file and a timing file, "
                    "a clip will be created by cutting at given timestamps and then combining.\n\n"
                    "FFmpeg needs to be installed on your system in order to use this program.\n\n"
                    "The timing file should be a text file with clip timestamps separated by new lines,"
                    "in a format like this '30 70'.")
@click.argument("video_file",
                type=click.Path())
@click.argument("timing_file",
                type=click.File())
@click.option("--out",
              default=None,
              help="Output file, default is out.mkv in current directory",
              type=click.Path(writable=True))
def mergecat(video_file: str, timing_file, *, out):
    tmp_dir = tempfile.gettempdir()
    name = path.splitext(path.basename(video_file))[0]
    tmp_files = []

    # create the concat file
    concat_file = path.join(tmp_dir, f"{name}-concat.txt")
    tmp_files.append(concat_file)

    with open(concat_file, "w") as concat:
        # cut each clip based on given times
        for count, timestamp in enumerate(timing_file):
            start, end = timestamp.split(" ")
            duration = str(int(end) - int(start))

            clip_file = path.join(tmp_dir, f"{name}-clip{count}.mkv")
            tmp_files.append(clip_file)

            click.echo(f"Creating clip {count}")
            call(["ffmpeg", "-y", "-loglevel", "panic",
                  "-i", video_file,
                  "-ss", start,
                  "-t", duration,
                  "-c", "copy", clip_file])
            concat.write(f"file '{clip_file}'\n")

    if out is None:
        out = f"{name}-mergecat.mkv"

    # save the concatenated clips
    click.echo(f"Creating final output")
    call(["ffmpeg", "-y", "-loglevel", "error",
          "-f", "concat",
          "-safe", "0",  # since we are forced to use exact paths
          "-i", concat_file,
          "-c", "copy", out])

    # clean up any temp files
    for tmp_file in tmp_files:
        remove(tmp_file)


if __name__ == "__main__":
    mergecat()
