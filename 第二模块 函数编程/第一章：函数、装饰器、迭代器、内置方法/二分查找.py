datas = list(range(10000))


def look(data, n):
    mid = int(len(data) / 2)
    if mid > 0:
        if data[mid] > n:
            new_data = data[:mid]
            print('中数%s大于要查找的数%s' % (data[mid], n))
            look(new_data, n)
        elif data[mid] < n:
            new_data = data[mid:]
            print('中数%s小于要查找的数%s' % (data[mid], n))
            look(new_data, n)
        else:
            print('找到%s,索引值为%s' % (n, list(range(10000)).index(n)))

    else:
        if data[mid] == 0:
            print('找到%s,索引值为%s' % (data[0], 0))
        else:
            print('要查找的内容不存在')


look(datas, 1)
