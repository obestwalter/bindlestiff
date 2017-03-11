require 'json'
require 'tmpdir'

settingsName = File.exists?("settings.json") ? 'settings.json' : 'defaults.json'
$SETTINGS = JSON.parse(IO.read(settingsName))

def get_settings(key)
   return ENV[key] || $SETTINGS[key]
end

INTERPRETERS = get_settings("INTERPRETERS")
puts "bla #{INTERPRETERS} blub"
