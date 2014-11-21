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
        copytree(path.join(path.dirname(__file__), '..', 'conf/app_template'), path.join(project, app))


def debug(out, args):
    # if len(args) == 2:
    #     test_file = args[1]
    #     args = args[1:]
    # else:
    #     test_file = None
    try:
        from coverage import coverage
        cov = coverage()
        cov.start()
    except ImportError:
        coverage = None

    run(out, args, debug=True)

    if coverage:
        cov.stop()


def run(out, args, debug=False):
    '''
    starts develop server
    '''
    load_project(out, args)
    from rider.core import server
    server.run(debug=debug)


def load_project(out, args):
    if out:
        if args:
            chdir(args[0])
        sys.path.append(getcwd())
        __import__('__init__')


COMMANDS = {
    'help': get_help,
    'create': create,
    'run': run,
    'debug': debug
}
