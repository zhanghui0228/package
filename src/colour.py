class Colour(object):
    tag = 'colour'

    def __init__(self, status):
        self.__status__ = status

    def Status(self):
        if self.__status__ == 'running':
            green = "\033[32m running \033[0m"
            return green
        elif self.__status__ == 'done':
            green = "\033[32m done \033[0m"
            return green
        elif self.__status__ == 'warning':
            yellow = "\033[33m warning \033[0m"
            return yellow
        else:
            red = "\033[31m {} \033[0m".format(self.__status__)
            return red



def colour(status):
    value = Colour(status)
    return (value.Status())
