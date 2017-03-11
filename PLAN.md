# TODO

* make it work as developer installation

## Arch

* https://www.ideaplexus.com/2015/09/05/create-an-arch-linux-based-vagrant-base-box/
* use shell script for provisioning http://stackoverflow.com/questions/15461898/passing-variable-to-a-shell-script-provisioner-in-vagrant

## Win10

* http://huestones.co.uk/node/305
* http://www.hurryupandwait.io/blog/fixing-winrm-firewall-exception-rule-not-working-when-internet-connection-type-is-set-to-public
* http://www.hurryupandwait.io/blog/in-search-of-a-light-weight-windows-vagrant-box?rq=windows%2010
* 
* [install Python non interactive](http://stackoverflow.com/questions/6441353/non-interactive-installation-of-an-additional-python-environment-on-a-computer-w)


## Later

* Make it work when it is installed properly (paths, package data, etc)

### Maybe

* https://www.vagrantup.com/docs/provisioning/salt.html

# Ideas

## Different modes

### Simple mode

    $ pip install bindlestiff
    $ bindlestiff ssh arch
    $ bindlestiff tox arch

Creates, and starts an arch linux box with the current folder mapped into the machine

### Multi mode

The defaults are shipped in [defaults.json](defaults.json). They contain what is needed to run tests for pytest/tox/devpi and related projects with [tox](https://tox.readthedocs.io/en/latest/). To override this copy the file to `settings.json` and adjust to your needs.

If you log in with `vagrant ssh` you will already be in the project mount folder with all configured projects mapped there. You can then descend into the project that you want to test and run `tox`.

Settings are documented in the [Vagrantfile](Vagrantfile).

## Generate Vagrantfile

If you are happy with what bindlestiff does you can add your use case to your project by having a customized Vagrantfile generated into your project (jinja2 templating like cookiecutter)

read config from yaml file

* preferred box that should come up (bindlestiff ssh == bindlestiff ssh arch-linux)


## Howto

Vagrantfile outside of project

http://stackoverflow.com/questions/17308629/specify-vagrantfile-path-explicity-if-not-plugin

`VAGRANT_CWD=~/some/path/ vagrant ssh-config`

and/or ?? `VAGRANT_VAGRANTFILE`


# Plan


cookiecutter template for my kind of project
