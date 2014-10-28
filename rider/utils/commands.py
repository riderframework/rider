from os import path, chdir, getcwd
import sys
from shutil import copytree


def main(out=False):
    args = sys.argv[1:]
    if len(args) == 0:
        get_help(out)
    elif args[0] in COMMANDS:
        COMMANDS[args[0]](out, args[1:])
    else:
        print("No command '%s' found" % args[0])


def get_help(out, args=[]):
    '''
    shows help about command
    '''
    if any(args):
        command = args[0]
        if command in COMMANDS:
            print('%s\n' % command)
            print(COMMANDS[command].__doc__)
        else:
            print("No help for command '%s' found." % args[0])
    else:
        for command in COMMANDS.keys():
            print('%s\n' % command)


def create(out, args):
    '''
    creates project or app
    '''

    project_app = args[0].split('.')

    if len(project_app) > 2:
        #TODO
        print('Error: TODO')
        return

    project = project_app[0]
    try:

        app = project_app[1]
    except IndexError:
        app = None

    if not app:
        copytree(path.join(path.dirname(__file__), '..', 'conf/project_template'), project)
    else:
        createapp([app])


def createapp(out, args):
    if len(args) != 1 or '.' in args[0]:
        print('TODO')
        return
    print('TODO creating app %s' % args[0])



def run(out, args):
    '''
    starts develop server
    '''
    if out:
        if args:
            chdir(args[0])
        sys.path.append(getcwd())
        __import__('__init__')
    from rider.http import server
    server.run()


COMMANDS = {
    'help': get_help,
    'create': create,
    'run': run
}
