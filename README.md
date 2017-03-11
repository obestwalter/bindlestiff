# Bindlestiff

[![Project Status: Concept - Minimal or no implementation has been done yet.](http://www.repostatus.org/badges/latest/concept.svg)](http://www.repostatus.org/#concept)

![bindlestiff](docs/_static/logo.jpg)

Test a project in different vagrant boxes with pre installed Python versions without the need to set up a vagrant project for it yourself.

This should work on Windows, OsX and Linux.

### Prerequisites

* [Vagrant](https://www.vagrantup.com/)
* [VirtualBox](https://www.virtualbox.org/)

## How to use

### Settings

The defaults are shipped in [defaults.json](defaults.json). They contain what is needed to run tests for pytest/tox/devpi and related projects with [tox](https://tox.readthedocs.io/en/latest/). To override this copy the file to `settings.json` and adjust to your needs.

If you log in with `vagrant ssh` you will already be in the project mount folder with all configured projects mapped there. You can then descend into the project that you want to test and run `tox`.

All settings are documented in the [Vagrantfile](Vagrantfile).

    $ cd </path/to/bindlestiff/clone>
    $ vagrant up lin  # or vagrant up win
    $ vagrant ssh
    $ cd <one of the mapped projects in PROJECT_FOLDERS>
    $ tox

