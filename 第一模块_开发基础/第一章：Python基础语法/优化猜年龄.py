# n = 0
# while n<3:
#     age=25
#     cage=int(input("age:"))
#     if age==cage:
#         print("恭喜你猜对了")
#         break
#     n += 1
n=0
age=25
while n<3:
    user_age=int(input("age:"))
    if age==user_age:
        print("恭喜你猜对了")
        break
    n += 1
    if n==3:
       c=input("是否继续猜？输入y或者Y，继续，输入其他退出")
       if c=="y" or c=="Y":
         n=0
