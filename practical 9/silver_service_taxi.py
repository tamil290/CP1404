# Silver Service taxi


from taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel, 1.23 * fanciness)
        self.fanciness = fanciness

    def get_fare(self):
        base_fare = super().get_fare()
        return self.flagfall + base_fare

    def __str__(self):
        return super().__str__() + " plus flagfall of ${:.2f}".format(self.flagfall)

