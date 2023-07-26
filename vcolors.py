class Vcolors:
    BLUE = '\033[48;5;20m'
    ORANGE = '\033[48;5;214m'
    RED = '\033[48;5;160m'
    GREEN = '\033[48;5;22m'
    LTGREEN = '\033[48;5;46m'
    PINK = '\033[48;5;219m'
    LTBLUE = '\033[48;5;51m'
    GRAY = '\033[48;5;8m'
    ENDC = '\033[48;5;0m'
    BROWN = '\033[48;5;94m'
    OLIVE = '\033[48;5;2m'
    PURPLE = '\033[48;5;5m'
    YELLOW = '\033[48;5;11m'

    def printColor(self, x):

        match x:
            case 1:
                val = self.formatColor(x, self.BLUE)
            case 2:
                val = self.formatColor(x, self.ORANGE)
            case 3:
                val = self.formatColor(x, self.RED)
            case 4:
                val = self.formatColor(x, self.GREEN)
            case 5:
                val = self.formatColor(x, self.PINK)
            case 6:
                val = self.formatColor(x, self.LTBLUE)
            case 7:
                val = self.formatColor(x, self.GRAY)
            case 8:
                val = self.formatColor(x, self.BROWN)
            case 9:
                val = self.formatColor(x, self.OLIVE)
            case 10:
                val = self.formatColor(x, self.LTGREEN)
            case 11:
                val = self.formatColor(x, self.PURPLE)
            case 12:
                val = self.formatColor(x, self.YELLOW)
            case 0:
                val = self.formatColor(x, self.ENDC)

        return val

    def formatColor(self, x, theColor):
        return theColor + " " + " " + " " + self.ENDC
