from Plugin import *

"""
    TaskPlugin.py

    Deals with making tasks thread-able by adding a condition to it.
"""
class TaskPlugin(Plugin):
    def __init__(self, reader):
        super().__init__(reader)

    # Yields all 'while' statements.
    def GetLoops(self):
        for index, line in enumerate(self.reader.lines):
            if 'while' in line:
                yield [index, line]

    # Given a line, checks if each '(' and ')' are paired.
    def ParenthesisCheck(self, line):
        depth = 0
        for char in line:
            depth += char == '('
            depth -= char == ')'

        return depth == 0


    # Given a line, get a string representing the
    # contents of anything between root '()' nodes.
    def GetConditions(self, index, line):
        conditions = ""
        depth = 0
        for char in line:
            # If ')' is found, decrease depth
            depth -= char == ')'

            collect = depth != 0

            # If '(' is found, increase depth
            depth += char == '('

            if collect:
                conditions += char

        return conditions

    # Given a string of conditions, replace them with anything inside
    # a line's '()' parent nodes
    def ReplaceConditions(self, line, conditions):
        newLine = ""
        depth = 0
        for char in line:

            # If ')' is found, decrease depth
            depth -= char == ')'

            collect = depth == 0

            # If '(' is found, increase depth
            depth += char == '('

            if collect:
                newLine += char

            elif conditions not in newLine:
                newLine += conditions

        return newLine


    def Convert(self):
        # To make tasks thread-able, a condition has to be
        # inserted in its while loop to allow it to exit
        # at any time.
        for index, line in self.GetLoops():
            if self.ParenthesisCheck(line):
                conditions = '(' + self.GetConditions(index, line) + ") && !killAll"

                self.reader.lines[index] = self.ReplaceConditions(line, conditions)

            else:
                print('TaskPlugin.py: Had trouble reading line %s of %s.' % (index, self.reader.fileName))


        return []
