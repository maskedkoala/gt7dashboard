class Lap:
    def __init__(self):
        self.DataTires = []
        self.PositionsX = []
        self.PositionsY = []
        self.PositionsZ = []
        self.Title = ""
        self.LapTicks = 1
        self.LapTime = 0
        self.LapLiveTime = 0
        self.Number = 0
        self.ThrottleAndBrakesTicks = 0
        self.NoThrottleNoBrakeTicks = 0
        self.FullBrakeTicks = 0
        self.FullThrottleTicks = 0
        self.TiresOverheatedTicks = 0
        self.TiresSpinningTicks = 0
        self.DataThrottle = []
        self.DataBraking = []
        self.DataCoasting = []
        self.DataSpeed = []
        self.DataTime = []
        self.DataRPM = []
        self.FuelAtStart = 0
        self.FuelAtEnd = -1
        self.FuelConsumed = -1

    def __str__(self):
        return ('\n %s, %2d, %1.f, %4d, %4d, %4d' % (
            self.Title,
            self.Number,
            self.FuelAtEnd,
            self.FullThrottleTicks,
            self.FullBrakeTicks,
            self.NoThrottleNoBrakeTicks))

    def format(self):
        return ('Lap %2d, %s (%d Ticks)' % (
            self.Number,
            self.Title,
            len(self.DataSpeed)))
