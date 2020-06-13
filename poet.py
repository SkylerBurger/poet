import os
import sys 


def poetry_shell_status(args):
    """
    Checks your operating system's environment variables to verify whether or not Poetry's shell is active.
    """
    active = os.environ.get('POETRY_ACTIVE')
    if active:
        print('** Poetry Shell: ACTIVE **')
    else:
        print('** Poetry Shell: NOT Active **')


def create_new_project(args):
    """
    Creates a virtual environment for your project and runs Poetry's new project command.
    """
    project_name = args.pop(0) if len(args) else 'new_project'
    python_version = args.pop(0) if len(args) else 'system'

    # Create virtual environment
    os.system(f'pyenv virtualenv {python_version} {project_name}')
    os.system(f'pyenv local {project_name}')

    # Initiate Poetry project
    os.system(f'poetry new -q {project_name}')
    os.system(f'mv .python-version {project_name}')
    os.system(f'cd {project_name} && mv README.rst README.md')
    
    print(f'\nCreated Project: {project_name}')
    print(f'Python Version: {python_version}')


def conductor():
    """
    Determines which task the user was trying to execute. 
    Calls the function associated with that task and passes along the remaining user arguments.
    """
    arguments = sys.argv[1:]
    if len(arguments):
        task = tasks.get(arguments[0])
        if task:
            task(arguments[1:])
        else:
            print(f'Poet did not recognize the command: {arguments[0]}')
    else:
        poetry_shell_status(arguments[1:])


tasks = {
    'status': poetry_shell_status,
    'new': create_new_project,
}


if __name__ == '__main__':
    conductor()