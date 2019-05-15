import xlrd
import sklearn


def load_data(sheet_name):
    '''从excel中载入数据'''
    file = 'dataset.xlsx'
    wb = xlrd.open_workbook(filename=file)
    ws = wb.sheet_by_name(sheet_name)
    data = []
    for r in range(1, ws.nrows):
        col = []
        for c in range(ws.ncols):
            col.append(ws.cell(r, c).value)
        data.append(col)
    return data


def process_data(data):
    '''剔除出场时间为零的球员'''
    data = list(filter(lambda x: x[4], data))
    # filter(function,data)把传入的函数依次作用于data里每个元素，返回值是True的保留。
    # lambda表达式是一种匿名函数，用于简化书写，格式为：lambda 参数 ：操作（参数）
    return data


def normalize_data(data):
    '''数据归一化'''
    return sklearn.preprocessing.scale([i[3:] for i in data])




