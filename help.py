# #"آمورش یاخت ستاره با توجه بر مقادیر و ویژگی ها "
# #"کاربرد ریترن و این که چرا بهش میگن تابع بازگشتی"
# class CAR_class:
#     def __init__(self,Name,Start_Speed,final_speed,Power,):
#         self.Name=Name
#         self.Start_Speed=Start_Speed
#         self.final_speed=final_speed
#         self.Power=Power
#     def Stars(self,value):
#         if value<=180:
#             return "*"
#         if value>180:
#             return "**"
#         if value>300:
#             return "***"
#     def __repr__(self):
#         star=self.Stars(self.Start_Speed)+self.Stars(self.final_speed)+self.Stars(self.Power)
#         star_counter= len(star)
#         return f"{self.Name} {self.Start_Speed} {self.final_speed} {self.Power} {star} /{star_counter}*\n"
# car1=CAR_class("BMW",30,300,400)
# car2=CAR_class("lamborghini",210,500,400)
# car3=CAR_class("Pride",10,180,100)
#
# print(car1)
# print(car2)
# print(car3)
###########
# def gam_adad(n):
#     if n <= 0:  # شرط پایه: جمع تا صفر، صفر است
#         return 0
#     else:
#         return n + gam_adad(n - 1) # عدد فعلی + جمع اعداد قبلی
#
# print(gam_adad(3)) # خروجی: 6
# print(gam_adad(5)) # خروجی: 15
# #################
# def greet(name):
#     return  "salam" + name +"!"
# massage = greet(input("اسم را وارد کنید "))
# print(massage)
# ###############
# def tabe_name():
#     name= input("Please enter your name : ")
#     return name
#
# def tabe_age():
#     age=input("What is your age?")
#     return age
#
# def result(name,age):
#     return f"hello {name}, you are {age} years old"
#
# user_Name=tabe_name() # نام را از تابع اول می‌گیریم
# user_age=tabe_age() # سن را از تابع میگیریم
# print(result(user_Name,user_age))
# ######################
# def get_name():
#     return input("Please enter your name: ")
#
# def get_age():
#     return input("What is your age? ")
#
# # بخش اصلی برنامه (Main logic)
# name = get_name()
# age = get_age()
#
# # استفاده از f-string برای نمایش زیبا و بدون خطا
# print(f"Hello {name}, your age is {age}.")

# list=[]
# def list_function():
#     for i in range (10):
#         if i % 2 == 0 and i>=5:
#             list.append(i)
# list_function()
# print(list)
#
# list_1=[var for var in range(10) if var%2==0 if var>=5] #بجای if میتونیم and هم بنویسیم
# print(list_1)

list3=[(i,"Even" if i%2==0 else "Odd" )for i in range(10)]
print(list3)


