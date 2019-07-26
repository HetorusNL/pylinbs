import inspect
import os
import pkgutil
import importlib

from pyplugin.plugin import Plugin


class PluginCollection(object):
    """Plugin Collection that collects the plugins in plugin_package that
    inherit the Plugin class"""

    def __init__(self, plugin_package):
        """Creates the plugin collection and initiates the reading of all
        available plugins"""
        self.plugin_package = plugin_package
        self.reload_plugins()

    def reload_plugins(self):
        """(Re)reads all available plugins in the plugin_package package"""
        self.plugins = []
        self.seen_paths = []

        print(f'Looking for plugins under package "{self.plugin_package}":')
        self._walk_package(self.plugin_package)
        print()  # add a newline after all plugins have been found

    def initialize(self):
        """Call the initialize function on all plugins, this initializes the
        plugin classes"""
        print("initializing plugins")

        for plugin in self.plugins:
            plugin.initialize()

    def configure(self):
        """Call the configure function on all plugins, this performs the (user)
        configuration of the plugin classes"""
        print("configuring plugins")

        for plugin in self.plugins:
            plugin.configure()

    def execute(self):
        """Call the execute function on all plugins, this executes the plugin's
        desired action that has been configured"""
        print("executing plugins")

        for plugin in self.plugins:
            plugin.execute()

    def _walk_package(self, package):
        """Recursively walk the supplied package to import all packages"""
        imported_package = importlib.import_module(package)
        # imported_package = __import__(package, fromlist=["blah"])

        for _, pluginname, ispkg in pkgutil.iter_modules(
            imported_package.__path__, imported_package.__name__ + "."
        ):
            if not ispkg:
                plugin_module = __import__(pluginname, fromlist=["blah"])
                clsmembers = inspect.getmembers(plugin_module, inspect.isclass)
                for (_, c) in clsmembers:
                    # Only add classes that are a sub class of Plugin,
                    # but NOT Plugin itself
                    if issubclass(c, Plugin) & (c is not Plugin):
                        print(
                            f"    Found plugin class: "
                            f"{c.__module__}.{c.__name__}"
                        )
                        self.plugins.append(c())

        # Now that we have looked at all the modules in the current package,
        # start looking recursively for additional modules in sub packages
        all_current_paths = []
        if isinstance(imported_package.__path__, str):
            all_current_paths.append(imported_package.__path__)
        else:
            all_current_paths.extend([x for x in imported_package.__path__])

        for pkg_path in all_current_paths:
            if pkg_path not in self.seen_paths:
                self.seen_paths.append(pkg_path)

                # Get all sub directory of the current package path directory
                child_pkgs = [
                    p
                    for p in os.listdir(pkg_path)
                    if os.path.isdir(os.path.join(pkg_path, p))
                ]

                # For each sub directory, apply the _walk_package method
                # recursively
                for child_pkg in child_pkgs:
                    self._walk_package(package + "." + child_pkg)
