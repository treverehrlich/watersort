import vcolors as v

c = v.Vcolors()


class Vial():

    def __init__(self, vial_id, maxsize, vial):
        self.maxsize = maxsize
        self.vial = vial
        self.vial_id = vial_id

    def showContents(self):

        val = ''

        for x in self.vial:
            val = val + c.printColor(x)

        return val

    def getId(self):
        return self.vial_id

    def getRemainingSpace(self):
        return self.maxsize - len(self.vial)

    def isEmpty(self):
        if not self.vial:
            return True
        return False

    def isFull(self):
        if len(self.vial) == self.maxsize:
            return True
        return False

    def nextColor(self):
        if self.vial:
            return self.vial[-1]
        return 0

    # find out how much of that color is in the vial
    def nextColorDepth(self):
        topColor = self.vial[-1]

        depth = 0
        for x in reversed(self.vial):
            if topColor == x:
                depth += 1
            else:
                break

        return depth

    def addColor(self, color):
        self.vial.append(color)

    def removeColor(self):
        return self.vial.pop(-1)

    # are all the colors in vial the same?
    def isAllSame(self):
        return (self.vial.count(self.vial[0]) == len(self.vial))
