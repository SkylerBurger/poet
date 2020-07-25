<img src="https://imgur.com/q9SAHMk.png" style="display:block;margin:auto;">

# Poet

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

- `poet` or `poet status` - Returns the active status of the Poetry shell

- `poet new <project_name> <python_version>` - Initializes a new Poetry project and accompanying virtual environment. Sets the new virtual environment as the local version of Python for the project directory. Also changes the default `README.rst` to `README.md`

- Poet can also act as a proxy to run these typical Poetry commands:
  - `poet add <dependency_name>` - Install and add a dependency to your project
  - `poet init` - Initialize a new project with Poetry
  - `poet install` - Install project dependencies listed in `pyproject.toml`
  - `poet remove <dependency_name>` - Uninstall and remove a project dependency 
  - `poet shell` - Activate Poetry's shell