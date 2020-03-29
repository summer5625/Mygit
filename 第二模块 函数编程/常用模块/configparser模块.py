import configparser
conf = configparser.ConfigParser()


conf.read('cong.ini')
# print(conf.sections())
# print(type(conf.sections()))
# print(conf.default_section())

# print(list(conf['bitbucket.org'].keys()))
# print(conf['bitbucket.org']['User'])

for k,v in conf['group3'].items():
    print(k,v)


#读取文件内容

# print(conf.options('group3'))
# print(conf['group3']['name'])

#增加内容


# conf.add_section('group4')
conf['group3']['name'] = 'hefanghua123'
conf['group3']['age'] = '25'
conf.write(open('cong.ini','w'))

#删除内容

# conf.remove_option('group2','k3')
#
# conf.remove_section('group2')
#
#
# conf.write(open('cong.ini','w'))

