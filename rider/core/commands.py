from os import path
import sys
from shutil import copytree, ignore_patterns
from utils import load_project


def main(out=False):
    args = sys.argv[1:]
    if len(args) == 0:
        get_help(out)
    elif args[0] in COMMANDS:
        COMMANDS[args[0]](out, args[1:])
    else:
        print("No command '%s' found" % args[0])


def get_help(out, args=[]):
    """
    shows help about command
    """
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
    """
    creates project or app
    """

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

    ignore = ignore_patterns('*.pyo', '*.pyc', '*.py.class')

    if not app:
        copytree(path.join(path.dirname(__file__), '..', 'conf/project_template'), project, ignore=ignore)
    else:
        copytree(path.join(path.dirname(__file__), '..', 'conf/app_template'), path.join(project, app), ignore=ignore)


def run(out, args):
    """
    starts server
    """

    if out:
        try:
            cd = args[0]
        except IndexError:
            cd = ''
        load_project(cd)

    from rider.core.server import main_server
    main_server.start()


COMMANDS = {
    'help': get_help,
    'create': create,
    'run': run
}
