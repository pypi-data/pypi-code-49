from mindspace_web import MindspaceFactory

f = MindspaceFactory()


@f.parser.command
def do_print(con, text):
    print(f'{con.transport.getPeer()} says: {text}')


@f.parser.command
def echo(con, string):
    con.send_command('alert', string)


if __name__ == '__main__':
    f.run()
