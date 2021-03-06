import os
import re
import sys 


def poetry_shell_status(_, __):
    """Checks your operating system's environment variables to verify whether 
       or not Poetry's shell is active.
    """
    active = os.environ.get('POETRY_ACTIVE')
    if active:
        print('** Poetry Shell: ACTIVE **')
    else:
        print('** Poetry Shell: NOT Active **')


def create_new_project(_, args):
    """Creates a virtual environment for your project and runs Poetry's new 
       project command.
    
    Arguments:
        args (list[str]) - Additional arguments required to run the command
    """
    # command = args.pop(0) if len(args) else None
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


def export_reqs_to_txt(_, __):
    """This function exports Poetry project dependencies into a 
       requirements.txt file.
    """
    os.system('poetry export -f requirements.txt > requirements.txt')


def poetry_proxy(command, args):
    """This function acts as a proxy for running standard Poetry commands.
    
    Arguments:
        command (str) - The command to run
        args (list[str]) - Additional arguments required to run the command
    """
    command_string = f'{command} '
    command_string += " ".join(args) if args else ''
    
    os.system(f'poetry {command_string}')
    print(f'\nPoet has completed the following task: {command_string}\n')

def extract_pipfile_packages(contents, start):
    package_list = []
    for line in contents[start:]:
        if line == "\n":
            break
        regex_obj = re.compile('^(\w+-?)+')
        match_obj = regex_obj.search(line)
        if match_obj:
            package_list.append(match_obj[0])
    return package_list


def pipfile_install(_, __):
    filepath = f'{os.getcwd()}/Pipfile'
    with open(filepath) as file:
        contents = file.readlines()

    packages_start = None
    dev_packages_start = None

    for index, line in enumerate(contents):
        if packages_start and dev_packages_start:
            break
        if line == '[packages]\n':
            packages_start = index
        if line == '[dev-packages]\n':
            dev_packages_start = index

    packages = extract_pipfile_packages(contents, packages_start)
    dev_packages = extract_pipfile_packages(contents, dev_packages_start)
    
    if packages:
        os.system(f'poetry add {" ".join(packages)}')
    if dev_packages:
        os.system(f'poetry add --dev {" ".join(dev_packages)}')


def conductor():
    """Determines which task the user was trying to execute. 
       Calls the function associated with that task and passes along the user arguments.
    """
    command = sys.argv[1] if len(sys.argv) > 1 else None
    arguments = sys.argv[2:] if len(sys.argv) > 2 else None

    if command:
        task_function = tasks.get(command)
        if task_function:
            task_function(command, arguments)
        else:
            print(f'Poet did not recognize the command: {command}')
    else:
        poetry_shell_status(command, arguments)


tasks = {
    'add': poetry_proxy,
    'build': poetry_proxy,
    'check': poetry_proxy,
    'config': poetry_proxy,
    'env': poetry_proxy,
    'export': export_reqs_to_txt,
    'init': poetry_proxy,
    'install': poetry_proxy,
    'lock': poetry_proxy,
    'new': create_new_project,
    'pipfile-install': pipfile_install,
    'prep': False,
    'publish': poetry_proxy,
    'remove': poetry_proxy,
    'run': poetry_proxy,
    'search': poetry_proxy,
    'shell': poetry_proxy,
    'show': poetry_proxy,
    'status': poetry_shell_status,
    'update': poetry_proxy,
}


if __name__ == '__main__':
    conductor()
