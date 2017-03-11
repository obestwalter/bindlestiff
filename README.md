# Bindlestiff

![bindlestiff](docs/vagrant-with-bindlestiff.jpg)

Two vagrants with handy travel accessory containing all that is needed to test your projects with many different Python interpreters on Linux and **(not quite there yet)** Windows.

## How to use

### Prerequisites

This should run from Windows, OsX and Linux Hosts.

* [Vagrant](https://www.vagrantup.com/)
* [VirtualBox](https://www.virtualbox.org/)

### Settings

A `json` file containing paths to projects and other settings. These can be overridden with environment settings of the same name

The paths in `settings.json` `PROJECT_FOLDERS` will be mapped to `PROJECTS_MOUNT` inside the vagrant box. If you login with `vagrant ssh` you will already be in the project mount folder and only have to descend into the project that you want to test.

All settings are documented in the [Vagrantfile](Vagrantfile).

    $ cd </path/to/bindlestiff/clone>
    $ vagrant up linux
    $ vagrant ssh
    $ cd <one of the mapped projects in PROJECT_FOLDERS>
    $ tox

## TODO Windows 10

[install Python non interactive](http://stackoverflow.com/questions/6441353/non-interactive-installation-of-an-additional-python-environment-on-a-computer-w)
