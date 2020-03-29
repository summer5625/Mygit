import xml.etree.ElementTree as ET

# tree = ET.parse(r'C:\Users\夏天\Desktop\NR_AGV_param.xml')
# root = tree.getroot()

#打印xml里面的所有内容，有多少级目录就要循环多少次
# for child in root:
#     print('-------',child.tag,child.attrib)
#     for i in child:
#         print(i.tag,i.text)   #i.text只打印中间夹着的值

#只遍历year里面的内容
# for node in root.iter('year'):
#     print(node.tag,node.text)



#修改内容
# for node in root.iter('year'):
#     new_year = int(node.text)+1  #从xml文件里读到的是字符串，要转换
#     node.text = str(new_year)     #存的时候要转换成字符串
#     node.set = ('updated','year')
#
#
# tree.write(r'C:\Users\夏天\Desktop\param.xml')


#删除内容
#
# for country in root.findall('country'):
#     rank = int(country.find('rank').text)
#     if rank >50:
#         root.remove(country)
# tree.write(r'C:\Users\夏天\Desktop\outparam.xml')


#创建XML文档
new_xml = ET.Element('namelist')
name = ET.SubElement(new_xml,'name',attrib={'enrolled':'yes'})
age = ET.SubElement(name,'age',attrib={'checked':'no'})
sex = ET.SubElement(name,'sex')
sex.text = 'male'
name2 = ET.SubElement(new_xml,'name',attrib={'enrolled':'no'})
age = ET.SubElement(name2,'age')
age.text = '19'

et = ET.ElementTree(new_xml)  #生成文档对象
et.write(r'C:\Users\夏天\Desktop\out.xml',encoding='utf-8',xml_declaration=True)

ET.dump(new_xml)  #打印生成的格式