# Bindlestiff

The vagrants handy travel accessory containing all that is needed to test your project with many different Python interpreters on Linux and **(not quite yet)** Windows.

![bindlestiff](docs/vagrant-with-bindlestiff.jpg)

## What is this?

Vagrant boxes with pre installed Python interpreters and a simple way to configure folders that should be mapped into the boxes for development.

## How to use

$ cd </path/to/bindlestiff/clone>
$ vagrant up linux
$ vagrant ssh
$ cd <one of the mapped projects in PROJECT_FOLDERS>
$ tox

