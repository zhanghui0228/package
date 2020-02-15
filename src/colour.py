'''
    调用方法：
	import col
	col.colour(color, status)
    功能：
	目前支持的颜色为绿色、黄色、红色
'''
class Colour(object):
    tag = 'colour'

    def __init__(self, color, status):
        self.__color__ = color
        self.__status__ = status

    def Status(self):
        if self.__color__ == 'green':
            green = "\033[32m {} \033[0m".format(self.__status__)
            return green
        elif self.__color__ == 'yellow':
            yellow = "\033[33m {} \033[0m".format(self.__status__)
            return yellow
        elif self.__color__ == 'red':
            red = "\033[31m {} \033[0m".format(self.__status__)
            return red



def colour(color, status):
    value = Colour(color, status)
    return (value.Status())


#if __name__ == '__main__':
#    print (colour('green', 'done'))

