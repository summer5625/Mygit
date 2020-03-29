#等待用户输入名字、地点、爱好，根据用户的名字和爱好进行任意显示：如：敬爱可爱的xxx，最喜欢在xxx地方干xxx
name=input("名字：")
address=input("地址：")
hobby=input("爱好：")
inforn="敬爱可爱的%s，最喜欢在%s干%s" %(name,address,hobby)
print(inforn)