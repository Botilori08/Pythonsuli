class Uzenet:
    def __init__(self,sor1,sor2):
        #1 13
        #abor# #e#tun###agy#szel#2# #o##h#d#g ##rkasn#o#oka# #a#tunk e####a#akn##$#$#$##$$$$$$####
        self.nap = int(sor1.split(" ")[0])
        self.amator = int(sor1.split(" ")[1])

        self.uzenet = sor2

    def farkasKereso(self):
        return "farkas" in self.uzenet
    '''
        if "farkas" in self.uzenet:
            return True
        else:
            return False
    '''