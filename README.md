# Bindlestiff

The vagrants handy travel accessory containing all that is needed to test your project with many different Python interpreters on Linux and **(not quite yet)** Windows.

![bindlestiff](docs/vagrant-with-bindlestiff.jpg)

## What is this?

Vagrant boxes with pre installed Python interpreters and a simple way to configure folders that should be mapped into the boxes for development.

## How to use

The paths in `settings.json` `PROJECT_FOLDERS` will be mapped to `PROJECTS_MOUNT` inside the vagrant box. If you login with `vagrant ssh` you will already be in the project mount folder and only have to descend into the project that you want to test.

    $ cd </path/to/bindlestiff/clone>
    $ vagrant up linux
    $ vagrant ssh
    $ cd <one of the mapped projects in PROJECT_FOLDERS>
    $ tox
