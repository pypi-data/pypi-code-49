from mindspace_web import MindspaceFactory

f = MindspaceFactory()


@f.parser.command
def echo(con, string):
    con.send_command('alert', string)


if __name__ == '__main__':
    f.run()
