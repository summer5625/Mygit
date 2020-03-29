#查找列表中的元素，移除每个元素的空格，并查找以a或者A开头并且以c结尾的所以元素
li=['alec','aric','Alex','Tony','rain']
tu=('alec','aric','Alex','Tony','rain')
dic={'k1':"alex",'k2':"aric",'k3':"Alex",'k4':"Tony"}
# for i in li:
#     print(i.strip())
# for j in tu:
#     print(j.strip())
# for k in dic:
#     print(k.strip() )
# print(dic)
# for i in li:
#     if i.startswith('a') or  i.startswith('A'):
#         if i.endswith('c'):
#             print(i)
# for i in tu:
#     if i.startswith('a') or  i.startswith('A'):
#         if i.endswith('c'):
#             print(i)
for  i in dic :
    if (dic[i].startswith('a') or  dic[i].startswith('A')) and dic[i].endswith('c'):
        print(dic[i])
