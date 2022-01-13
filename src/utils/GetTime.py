# Module to get currentime of system.
from time import gmtime, strftime, time


class Time:
    current_time = None

    def __init__(self):
        self.current_time = strftime("%Y-%m-%d %H-%M-%S", gmtime())

    def get_time(self):
        return str(self.current_time)

# z=Time()
# print(z.get_time())
