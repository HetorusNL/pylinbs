from pyplugin import Plugin


class Identity(Plugin):
    """This plugin is just the identity function: it returns the argument"""

    def __init__(self):
        super().__init__()
        self.name = "Identity function"
        self.description = "does nothing"

    def initialize(self):
        pass

    def configure(self):
        pass

    def execute(self):
        print("running identity function")
