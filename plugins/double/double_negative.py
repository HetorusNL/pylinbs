from pyplugin import Plugin


class DoubleNegative(Plugin):
    """Test plugin that does some negative multiplication"""

    def __init__(self):
        super().__init__()
        self.name = "Double Negative"
        self.description = "performs negative double function"

    def initialize(self):
        pass

    def configure(self):
        pass

    def execute(self):
        print("performing argument *= -2")
