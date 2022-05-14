class Monitor:
    displayResolution = 0
    screenSize = 0
    rate = 0
    def __init__(self,px,dm,Hz):
        print("Create new Monitor")
        self.displayResolution = px
        self.screenSize = dm
        self.rate = Hz
    def printInfo(self,name):
        print("f{name:*10}")
        print("DisplayResolution", lg.displayResolution)
        print("Screen Size", lg.screenSize)
        print("Image refresh rate", lg.rate)
        def test(self):
            print"test"
class Phone:


lg = Monitor(1500,500,1000)
philips = Monitor(500, 345, 6789)
lg.printInfo("LG")
philips.printInfo("PHILIPS")
print("LG")


