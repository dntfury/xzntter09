# For making colorful string
# Return colored string for logging
# RED GREEN YELLOW LIGHTPURPLE

class ColorString:
    string = None

    def __init__(self):
        pass

    def rrFail(self, data: str):
        self.string = str(("\033[91m {}\33[00m" .format(data)))
        return self.string

    def rrPass(self, data: str):
        self.string = str(("\033[92m {}\33[00m" .format(data)))
        return self.string

    def rrWarning(self, data: str):
        self.string = str(("\033[93m {}\33[00m" .format(data)))
        return self.string

    def rrInfo(self, data: str):
        self.string = str(("\033[94m {}\33[00m" .format(data)))
        return self.string


# data = ColorString()
# print(data.rrFail("Hello"))
# print(data.rrPass("Hello"))
# print(data.rrWarning("Hello"))
# print(data.rrInfo("Hello"))
