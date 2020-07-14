"""
    Plugin.py

    A base class meant for abstracting file conversion logic into
    modular classes.
"""
class Plugin:
    def __init__(self, reader):
        # A Reader.py class to read the file.
        self.reader = reader

    # Resets the reader before converting the file.
    def WrappedConvert(self):
        self.reader.ResetReader()
        return self.Convert()

    # Returns a list of strings representing lines to be appended to the file.
    def Convert(self):
        return []
