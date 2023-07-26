import vial as v
import vialset as s

import ctypes
kernel32 = ctypes.WinDLL('kernel32')
hStdOut = kernel32.GetStdHandle(-11)
mode = ctypes.c_ulong()
kernel32.GetConsoleMode(hStdOut, ctypes.byref(mode))
mode.value |= 4
kernel32.SetConsoleMode(hStdOut, mode)

vialsize = 4

BLUE = 1
ORANGE = 2
RED = 3
GREEN = 4
PINK = 5
LTBLUE = 6
GRAY = 7
BROWN = 8
OLIVE = 9
LTGREEN = 10
PURPLE = 11
YELLOW = 12

vial0 = v.Vial(0, vialsize, [BROWN, ORANGE, GRAY, BROWN])
vial1 = v.Vial(1, vialsize, [PURPLE, LTBLUE, OLIVE, PINK])
vial2 = v.Vial(2, vialsize, [RED, ORANGE, OLIVE, GRAY])
vial3 = v.Vial(3, vialsize, [PINK, BROWN, RED, BLUE])
vial4 = v.Vial(4, vialsize, [GREEN, BLUE, YELLOW, ORANGE])
vial5 = v.Vial(5, vialsize, [BLUE, ORANGE, LTGREEN, YELLOW])
vial6 = v.Vial(6, vialsize, [LTBLUE, LTGREEN, LTGREEN, BLUE])
vial7 = v.Vial(7, vialsize, [OLIVE, GREEN, PURPLE, PINK])
vial8 = v.Vial(8, vialsize, [YELLOW, GREEN, LTGREEN, OLIVE])
vial9 = v.Vial(9, vialsize, [LTBLUE, BROWN, GRAY, PURPLE])
vial10 = v.Vial(10, vialsize, [LTBLUE, GRAY, PURPLE, GREEN])
vial11 = v.Vial(11, vialsize, [PINK, RED, RED, YELLOW])
vial12 = v.Vial(12, vialsize, [])
vial13 = v.Vial(13, vialsize, [])


myvials = [vial0, vial1, vial2, vial3, vial4, vial5, vial6,
           vial7, vial8, vial9, vial10, vial11, vial12, vial13]

vialset = s.VialSet(myvials)

print(vialset.displayVials())

vialset.runLoop(0, '', 0, 0)

print(vialset.answer)
print("Found answer in " + str(vialset.maxlevel) + " moves!")
print("During the process, tried " + str(vialset.tryCounter) + " potential moves!")
