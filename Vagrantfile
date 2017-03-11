require 'json'
require 'pathname'
require 'tmpdir'

name = File.exists?("settings.json") ? 'settings.json' : 'defaults.json'
$SETTINGS = JSON.parse(IO.read(name))

# Array of python interpreters to use (full semver string)
INTERPRETERS = $SETTINGS["INTERPRETERS"]
# Array of paths to projects you want to map into the boxes
PROJECT_FOLDERS = $SETTINGS["PROJECT_FOLDERS"]
# path were the PROJECT_FOLDERS will be mpunted to
PROJECTS_MOUNT = $SETTINGS["PROJECT_MOUNT"]
# Name of the directory where tmp files will be stored in hosts tempdir
HOST_TMP_DIR = File.join(Dir.tmpdir(), "bindlestiff")
GUEST_TMP_DIR = "/home/vagrant/tmp"
PYENV_BIN_PATH = "/home/vagrant/.pyenv/bin"

Vagrant.configure("2") do |config|
    config.vm.define :linux do |lin|
        lin.vm.box = "obestwalter/tox-dev-arch-linux"
        lin.vm.provider "virtualbox" do |vb|
            vb.memory = $SETTINGS["VB_MEMORY"]
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
                sed -i '$ a\\cd #{PROJECTS_MOUNT}' .bashrc
            fi
            export PATH="#{PYENV_BIN_PATH}:$PATH"
            eval "$(pyenv init -)"
            for version in #{INTERPRETERS.join(" ")}; do
                pyenv install -s $version
            done
            pyenv global #{INTERPRETERS.join(" ")}
            pip install -U tox
            # pytest fails with ImportMismatchError if we don't tidy up
            find #{PROJECTS_MOUNT} -name '*.pyc' -delete
        HEREDOC
        lin.vm.provision "shell",
            name: "install pyenv",
            inline: installPyenvScript,
            privileged: false
    end

    # No automation here yet, just the bare box wating to be configured ...
    config.vm.define :win10 do |win|
        win.vm.box = "inclusivedesign/windows10-eval"
    end
end
