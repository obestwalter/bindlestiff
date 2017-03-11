require 'json'
require 'pathname'
require 'tmpdir'

$SETTINGS = JSON.parse(IO.read('settings.json'))
def get_settings(key)
   return ENV[key] || $SETTINGS[key]
end

INTERPRETER_DEFAULTS = "3.6.0 3.5.2 3.4.5 3.3.6 2.7.13 2.6.9 pypy2-5.6.0"
INTERPRETER = ENV["BINDLESTIFF_INTERPRETERS"] || INTERPRETER_DEFAULTS
PROJECT_FOLDERS = get_settings("PROJECT_FOLDERS")
PROJECTS_MOUNT = "/vagrant"
HOST_TMP_DIR = File.join(Dir.tmpdir(), get_settings("TMPDIR"))
GUEST_TMP_DIR = "/home/vagrant/tmp"
PYENV_BIN_PATH = "/home/vagrant/.pyenv/bin"

Vagrant.configure("2") do |config|
    config.vm.define :linux do |lin|
        lin.vm.box = "obestwalter/tox-dev-arch-linux"
        lin.vm.provider "virtualbox" do |vb|
            vb.memory = "2048"
        end

        # If externally mapped is to slow: add extra vdi or use different box
        Dir.mkdir(HOST_TMP_DIR) unless File.exists?(HOST_TMP_DIR)
        lin.vm.synced_folder HOST_TMP_DIR, "/vagrant/home/tmp"

        PROJECT_FOLDERS.each do |path|
            if File.directory?(path) then
                lin.vm.synced_folder path,
                    File.join(PROJECTS_MOUNT, Pathname(path).basename),
                    :mount_options => ["rw"]
            end
        end

        # Install pyenv, python interpreters, activate them and install tox
        installPyenvScript = <<-HEREDOC
            export TMPDIR="#{GUEST_TMP_DIR}"
            if [ -d "#{PYENV_BIN_PATH}" ]; then
                #{PYENV_BIN_PATH}/pyenv update
            else
                sudo pacman --noconfirm -S base-devel openssl zlib git xz
                curl pyenv.run | sh
                sed -i '$ a\\export PATH="$HOME/.pyenv/bin:$PATH"' .bashrc
                sed -i '$ a\\eval "$(pyenv init -)"' .bashrc
                sed -i '$ a\\export TMPDIR="#{GUEST_TMP_DIR}"' .bashrc
                sed -i '$ a\\cd /vagrant' .bashrc
            fi
            export PATH="#{PYENV_BIN_PATH}:$PATH"
            eval "$(pyenv init -)"
            for version in #{INTERPRETER}; do
                pyenv install -s $version
            done
            pyenv global #{INTERPRETER}
            pip install -U tox
            # pytest fails with ImportMismatchError if we don't tidy up
            find /vagrant -name '*.pyc' -delete
        HEREDOC
        lin.vm.provision "shell",
            name: "install pyenv",
            inline: installPyenvScript,
            privileged: false
    end

    # No automation here, would use salt, if I got around to it
    config.vm.define :win10 do |win|
        win.vm.box = "inclusivedesign/windows10-eval"
    end
end
