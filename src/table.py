import prettytable as pt



class Tabl(object):
    tag = 'Print in tabular form'

    def __init__(self, head, line):
        '''
        head 为打印输出的表头 格式为 list []
        line 为打印输出的每列内容  格式为 多个list整合为 tuple  ([],[],...,[])
        '''
        self.__head__ = head
        self.__line__ = line

    def Info(self):
        tb = pt.PrettyTable()
        tb.field_names = self.__head__
        for l in range(len(self.__line__)):
            tb.add_row(self.__line__[l])
        return tb


# 表格实例化
def table(head, line):
    tal = Tabl(head, line)
    return tal.Info()


#if __name__ == '__main__':
#    h = ['name', 'num']
#    l = (['a', 1], ['b', 2], ['c', 3])
#    print (table(h, l))

