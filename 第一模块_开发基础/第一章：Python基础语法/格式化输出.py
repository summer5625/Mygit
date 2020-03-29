name=input("name:")
age=float(input("age:"))
job=input("job:")
hometown=input("hometown:")
info="""
---------infor %s---------
Naem:      %s             
Age:       %f            
job:       %s             
Hometown:  %s             
----------end-------------
"""% (name,name,age,job,hometown)
print(info)