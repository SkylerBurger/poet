<img src="https://imgur.com/oRacQdD.png">

Poet was created for Python devs using a specific workflow involving Pyenv, Virtualenv, and Poetry to manage their project dependencies and environments as detailed in my post, [PVP- A Workflow for Python Projects](https://dev.to/skybur/pvp-a-workflow-for-python-projects-29h3). Poet allows you to initialize a Poetry project, create a clearly-labelled virtual environment, and set that environment as the local Python version for your project, all in a single command. Poet also lets you easily determine if Poetry's shell is active and can act as a proxy to run common Poetry commands.

## Installing

### Dependencies

To use Poet you will need to have completed setup as described in [PVP Workflow Requirements](https://dev.to/skybur/pvp-a-workflow-for-python-projects-29h3#requirements).

### Script and Alias

Poet is pretty easy to get setup.

1. Clone this GitHub repository to your machine. [(Clone Link)](https://github.com/SkylerBurger/poet.git)

2. Add the following alias to your `~/.bashrc` or `~/.profile` file, replacing `{path_to}` with the file path to the `poet.py` file in the cloned repository:

    Template:

    `alias poet='python3 ~/{path_to}/poet.py'`

    Example:

    `alias poet='python3 ~/Coding/Projects/poet/poet.py'`

That's it! You're ready to call on Poet to help you initalize and manage projects with added convenience!

## Commands


### Unique to Poet

- `poet` or `poet status` - Returns the active status of the Poetry shell

- `poet new <project_name> <python_version>` - Initializes a new Poetry project and accompanying virtual environment. Sets the new virtual environment as the local version of Python for the project directory. Also changes the default `README.rst` to `README.md`

- `poet export` - Poetry only supports exporting project dependencies to a `requirements.txt` file. This shortened command fills in the remaining arguments so you don't have to search around for the only command string that works with Poetry's exporting abilities.

### Proxy for Poetry

Poet can also act as a proxy to run these [Poetry commands](https://python-poetry.org/docs/cli/), simply refer to `poet` rather than `poetry`:
  
- `poet add <dependency_name>` - Install and add a dependency to your project
- `poet build` - Builds your project into source and wheels that can then be published to PyPI
- `poet check` - Verifies the structure of your `pyproject.toml` file
- `poet config` - Manage Poetry's configs
- `poet env <options>` - Various tasks related to managing Poetry's virtual environments
- `poet init` - Initialize a new project with Poetry
- `poet install` - Install project dependencies listed in `pyproject.toml`
- `poet lock` - Locks the current versions of your Poetry project dependencies to your `poetry.lock` file
- `poet publish` - Publishes a previously built Poetry project to PyPI
- `poet search <dependency_name>` - Search through packages from PyPI for potential tools for your project
- `poet remove <dependency_name>` - Uninstall and remove a project dependency
- `poet run <command_string>` - Runs the given command string within Poetry's virtual environment 
- `poet shell` - Activate Poetry's shell
- `poet show` - Lists all of the current project dependencies
- `poet update` - Updates your project's dependencies and adds the changes to your `poetry.lock` file
