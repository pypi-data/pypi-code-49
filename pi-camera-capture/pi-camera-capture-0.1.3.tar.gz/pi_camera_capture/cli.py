import fire
from pi_camera_capture.app import main


def cli():
    fire.Fire(main)


if __name__ == "__main__":
    cli()
