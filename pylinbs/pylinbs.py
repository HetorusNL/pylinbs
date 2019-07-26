from pyplugin import PluginCollection


class PyLinBS(object):
    """Python Linux BootStrap class to initialize and configure a brand new
    Linux system"""

    def __init__(self):
        """Initializes PyLinBS by searching for available plugins"""
        self.plugins = PluginCollection("plugins")

    def select_plugins(self):
        pass

    def configure_plugins(self):
        pass

    def execute_plugins(self):
        pass
