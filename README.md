# Bindlestiff

![bindlestiff](docs/vagrant-with-bindlestiff.jpg)

Two vagrants with handy travel accessory containing all that is needed to test your projects with many different Python interpreters on Linux and **(not quite there yet)** Windows.

This should run from Windows, OsX and Linux Hosts.

## How to use

### Prerequisites

* [Vagrant](https://www.vagrantup.com/)
* [VirtualBox](https://www.virtualbox.org/)

### Settings

The defaults are shipped in `defaults.json`. They contain what is needed to run tests for pytest/tox/devpi and related projects with [tox](https://tox.readthedocs.io/en/latest/). To override this copy the file to `settings.json` and adjust to your needs.

If you log in with `vagrant ssh` you will already be in the project mount folder with all configured projects mapped there. You can then descend into the project that you want to test and run `tox`.

All settings are documented in the [Vagrantfile](Vagrantfile).

    $ cd </path/to/bindlestiff/clone>
    $ vagrant up linux
    $ vagrant ssh
    $ cd <one of the mapped projects in PROJECT_FOLDERS>
    $ tox

## TODO Windows 10

[install Python non interactive](http://stackoverflow.com/questions/6441353/non-interactive-installation-of-an-additional-python-environment-on-a-computer-w)
