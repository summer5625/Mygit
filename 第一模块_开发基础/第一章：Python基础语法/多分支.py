score=int(input("score:"))
#if score>=0 and score<=39:
#    print("rank:E")
#elif score>39 and score<=59:
 #   print("rank:D")
#elif score > 59 and score <= 79:
   # print("rank:C")
#elif score > 79 and score <= 89:
 #   print("rank:B")
#elif score >89 and score <= 100:
 #   print("rank:A")
#else:
   # print("满分一百分，请输入正确的分数")


#if score>100:
# print("满分一百分，请输入正确的分数")
#elif  score >= 90:
 #   print("rank:A")
#elif  score >= 80:
  #  print("rank:B")
#elif  score>=60:
  #  print("rank:C")
#elif score >= 40:
 #   print("rank:D")
 #elif score>=0:
 #print("rank:E")
#else:
   # print("成绩不能是负数")

if  score<0:
  print("成绩不能是负数")
elif  score <40:
   print("rank:E")
elif  score <60:
    print("rank:D")
elif  score<80:
    print("rank:C")
elif score < 90:
    print("rank:B")
elif score <= 100:
    print("rank:A")
else:
    print("满分一百分，请输入正确的分数")
