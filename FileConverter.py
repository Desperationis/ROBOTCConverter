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

        # An array of strings representing the file.
        self.convertedFile = [];

    # Adds a plugin. "plugin" should be passed by type.
    def AddPlugin(self, plugin):
        self.plugins.append(plugin(self))

    # Converts the file by merging the results of plugins.
    def Convert(self):
        assert self.canParse, "FileConverter.py: Could not read \"%s\"" % (self.fileName)

        for plugin in self.plugins:
            self.convertedFile.extend(plugin.Convert())
