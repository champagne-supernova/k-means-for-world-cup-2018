filename = r'result\backfielder.txt'
# 默认路径包含\，某些情况下可能会被转义，为防止类似情况发生。可以在字符串前加上个r、表示raw字符、不进行转义
result = ''
with open(filename) as file_object:
    for line in file_object:
        line = line.replace('\n', '；')
        result += line
print(result)