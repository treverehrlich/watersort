import vcolors as vc

c = vc.Vcolors()


class VialSet():

    doDebug = True

    def __init__(self, vials):
        self.vials = vials
        self.answer = ''
        self.maxlevel = 0
        self.moves = []
        self.tryCounter = 0

    def runLoop(self, level, thisaction, prev_fromvial_id, prev_tovial_id):

        if (level < 5):
            print("currently at level " + str(level))
            print(str(len(self.moves)) + ":" + str(self.moves))
            print(thisaction)

        if self.isSuccessful():
            # this is the success case\
            self.maxlevel = level
            return 0

        else:
            # iterate through all possible moves
            # check all vials we can pour FROM
            for fromvial in self.vials:

                # print("From vial: " + str(fromvial.getId()))

                # make sure not empty
                if fromvial.isEmpty():
                    continue

                # see if we can pour TO another vial, check all vials
                for tovial in self.vials:

                    # print("   To vial: " + str(tovial.getId()))

                    potentialMoveStr = str(fromvial.getId()) + "-" + str(tovial.getId()) + "-" + str(
                        fromvial.nextColor()) + "-" + str(fromvial.nextColorDepth())

                    # check if this to vial is viable
                    if (self.passesMoveRules(level, fromvial, tovial, prev_fromvial_id, prev_tovial_id)):

                        # print("=======================================")

                        # print(str(level) + " : " + str(fromvial.getId() + 1) + " (" + str(c.printColor(fromvial.nextColor())) + ") " +
                        #      " to " + str(tovial.getId() + 1) + " (" + str(c.printColor(tovial.nextColor())) + ")")

                        # print(self.displayVials())

                        # since it's viable, make the pour, and save how much we pour so we can reverse if needed
                        amount_poured = self.processPour(fromvial, tovial)

                        # string to eventually return describing the move
                        thisaction = (
                            f'{fromvial.getId()+1} -> {tovial.getId()+1}')

                        # add this move to the moves stack
                        self.moves.append(potentialMoveStr)

                        # print the moves array
                        # print(str(len(self.moves)) + ":" + str(self.moves))

                        # now we'll call the recursive function
                        thataction = self.runLoop(
                            level + 1, thisaction, fromvial.getId(), tovial.getId())

                        if (thataction == 0):

                            self.displayMove(fromvial, tovial,
                                             amount_poured, level)

                            for z in range(amount_poured):
                                pourColor = tovial.removeColor()
                                fromvial.addColor(pourColor)

                            return 0

                        # after coming back, reverse the pour

                        for z in range(amount_poured):
                            # print("oops - repouring")
                            pourColor = tovial.removeColor()
                            fromvial.addColor(pourColor)

                        # remove this move from the moves array
                        del self.moves[-1]

    def processPour(self, fromvial, tovial):

        from_vial_depth = fromvial.nextColorDepth()
        to_space = tovial.getRemainingSpace()

        # start by assuming we can pour the full amount
        amount_to_pour = from_vial_depth

        # but if not enough room, only pour what there's room for
        if from_vial_depth > to_space:
            amount_to_pour = to_space

        for x in range(amount_to_pour):
            pourColor = fromvial.removeColor()
            tovial.addColor(pourColor)

        return amount_to_pour

        # finish pouring

    def passesMoveRules(self, level, fromvial, tovial, prev_fromvial_id, prev_tovial_id):

        # print("The current level is " + str(level))

        self.tryCounter = self.tryCounter + 1

        # if too deep, don't allow
        if level > 100:
            return False

        # can't pour into own vial
        if tovial is fromvial:
            return False

        # can't pour if full
        if tovial.isFull():
            return False

        # can't pour if not empty and different color
        if (not tovial.isEmpty()) and (tovial.nextColor() != fromvial.nextColor()):
            return False

        # make sure it's not a senseless move between empty vials
        # do this by first making sure this is the only color in the from vial
        # and then also make sure to vial is empty
        if ((fromvial.nextColorDepth() + fromvial.getRemainingSpace() == fromvial.maxsize) and tovial.isEmpty()):
            return False

        # make sure we're not just doing the opposite of the last move - pouring back and forth
        if ((fromvial.getId() == prev_tovial_id) and (tovial.getId() == prev_fromvial_id)):
            return False

        # check if this move has happened in the past, to prevent too much non-sequentials pours back and forth

        moveStr = str(fromvial.getId()) + "-" + str(tovial.getId()) + "-" + \
            str(fromvial.nextColor()) + "-" + str(fromvial.nextColorDepth())

        if (self.moves.count(moveStr) > 1):
            return False

        # print("found this particular move " +
        #      str(self.moves.count(moveStr)) + " times already.")

        # experimental: disallow if can't pour the entire color into the to vial
        if (fromvial.nextColorDepth() > tovial.getRemainingSpace()):
            return False

        # OK, we can pour into here
        return True

     # check all vials to see if we've achieved success

    def isSuccessful(self):

        # start off true then negate if necessary
        successValue = True

        for x in self.vials:
            if x.isEmpty():
                continue
            elif x.isAllSame() and x.isFull():
                continue

            else:
                # vial isn't empty and colors are different
                successValue = False
                break

        return successValue

    def displayVials(self):

        val = ''

        for x in self.vials:
            val = val + str(x.getId() + 1) + x.showContents() + "\n"

        return val

    def displayMove(self, fromvial, tovial, amount_poured, level):

        val = "======================\n"

        val = val + "Move #" + str(level + 1) + ": Pouring from vial " + str(fromvial.getId() + 1) + " to vial " + str(
            tovial.getId() + 1) + ": amount = " + str(amount_poured) + "\n"

        val = val + self.displayVials() + "\n"

        self.answer = val + self.answer
