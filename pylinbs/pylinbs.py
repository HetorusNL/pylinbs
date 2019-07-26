from PyInquirer import prompt

from pyplugin import PluginCollection


class PyLinBS(object):
    """Python Linux BootStrap class to initialize and configure a brand new
    Linux system"""

    def __init__(self):
        """Initializes PyLinBS by searching for available plugins"""
        self.plugin_collection = PluginCollection("plugins")

    def select_plugins(self):
        choices = [
            {"name": f"{plugin.name}: {plugin.description}", "value": plugin}
            for plugin in self.plugin_collection.plugins
        ]
        question = {
            "type": "checkbox",
            "name": "plugins",
            "message": "Which plugins to you want to run?",
            "choices": choices,
        }
        self.selected_plugins = prompt([question]).get("plugins")
        print()  # add a newline after the plugin selector

    def initialize_plugins(self):
        if not self.selected_plugins:
            print("No plugins to initialize!")
            return

        print("Initializing the selected plugins:")

        for plugin in self.selected_plugins:
            print(f' => Initializing "{plugin.name}"')
            plugin.initialize()

        print()  # add a newline after initializing the plugins

    def configure_plugins(self):
        if not self.selected_plugins:
            print("No plugins to configure!")
            return

        print("Configuring the initialized plugins:")

        for plugin in self.selected_plugins:
            print(f' => Configuring "{plugin.name}"')
            plugin.configure()

        print()  # add a newline after configuring the plugins

    def execute_plugins(self):
        if not self.selected_plugins:
            print("No plugins to execute!")
            return

        print("Executing the configured plugins:")

        for plugin in self.selected_plugins:
            print(f' => Executing "{plugin.name}"')
            plugin.execute()

        print()  # add a newline after executing the plugins
