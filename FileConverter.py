from PythonFileLibrary.Reader import *

"""
    FileConverter.py

    Converts a file using plugin logic.
"""
class FileConverter(Reader):
    def __init__(self, fileName):
        super().__init__(fileName)

        # Plugin.py objects. Order determines call.
        self.plugins = []

        # An array of strings representing the converted file.
        self.convertedFile = [];

    # Adds a plugin. "plugin" should be passed by type.
    # Returns a reference to the plugin.
    def AddPlugin(self, plugin):
        plugin = plugin(self)
        self.plugins.append(plugin)

        return plugin

    # Returns the first instance of a
    # plugin given its type.
    def AccessPlugin(self, pluginType):
        for plugin in self.plugins:
            if type(plugin) == pluginType:
                return plugin

        return None

    # Converts the file by merging the results of plugins.
    def Convert(self):
        assert self.canParse, "FileConverter.py: Could not read \"%s\"" % (self.fileName)

        for plugin in self.plugins:
            self.convertedFile.extend(plugin.WrappedConvert())
