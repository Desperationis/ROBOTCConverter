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

    # Given a line, get a string representing the
    # inside of anything between '()'
    def GetConditions(self, index, line):
        conditions = ""
        depth = 0
        collect = False
        for char in line:
            if char == ')':
                depth -= 1

                if depth == 0:
                    collect = False

            if collect:
                conditions += char

            if char == '(':
                depth += 1
                collect = True

        if collect:
            print('TaskPlugin.py: Had trouble reading line %s of %s.' % (index, self.reader.fileName))
            return ''
        else:
            return conditions

    # Given a string of conditions replace them with anything inside
    # line's ()
    def ReplaceConditions(self, line, conditions):
        newLine = ""
        collect = True
        for char in line:
            if char == ')':
                collect = True

            if collect:
                newLine += char

            if char == '(':
                newLine += conditions
                collect = False

        return newLine


    def Convert(self):
        # To make tasks thread-able, a condition has to be
        # inserted in its while loop to allow it to exit
        # at any time.
        for index, line in self.GetLoops():
            conditions = self.GetConditions(index, line)

            if conditions != '':
                conditions += " && TASKTRUE"

            self.reader.lines[index] = self.ReplaceConditions(line, conditions)




        return []
