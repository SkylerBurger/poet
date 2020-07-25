def poetry_proxy(command, args):
    """This function acts as a proxy for running standard Poetry commands.
    
    Arguments:
        command (str) - The command to run
        args (list[str]) - Additional arguments required to run the command
    """
    print('Proxy - args:', args)
    command_string = f'{command} '
    command += " ".join(args) if args else ''
    print('Proxy - Command String:', command_string)
    os.system(f'poetry {command_string}')
    print(f'\nPoet has completed the following task: {command_string}\n')


if __name__ == "__main__":
    poetry_proxy('remove', ['setuptools'])