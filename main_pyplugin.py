"""Test function for the Plugin(Collection)"""

from pyplugin import PluginCollection


def main():
    plugins = PluginCollection("plugins")

    # initialize all plugins
    plugins.initialize()

    # perform configuration of all plugins
    plugins.configure()

    # execute the plugins
    plugins.execute()


if __name__ == "__main__":
    main()
