from abc import abstractmethod, ABCMeta


class Plugin(object, metaclass=ABCMeta):
    """Base Plugin class that each plugin must inherit. All methods that
    plugins should implement are defined here (abstract)
    """

    def __init__(self):
        self.description = "Base Plugin"
        self.version = 1.0
        self.config = {}

    @abstractmethod
    def initialize(self):
        """Perform initialization cycle here"""

    @abstractmethod
    def configure(self):
        """The configuration (if needed) of the plugin (by the user) happens
        here"""

    @abstractmethod
    def execute(self):
        """Execute the plugin's actions here"""
