from pyplugin import Plugin


class DoublePositive(Plugin):
    """Test plugin that does some positive multiplication"""

    def __init__(self):
        super().__init__()
        self.name = "Double Positive"
        self.description = "performs double function"

    def initialize(self):
        pass

    def configure(self):
        pass

    def execute(self):
        print("performing argument *= 2")
