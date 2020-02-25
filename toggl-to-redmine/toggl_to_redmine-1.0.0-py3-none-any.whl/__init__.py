from toggl_to_redmine.platforms.CLI_platform import CLIPlatform
import click


@click.command()
def main():
    CLIPlatform().entry_point()


main()
