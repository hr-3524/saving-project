# var= 1      #تعریف متغیر
# var2= 2
# var_input= int(input("وارد کنید :"))    #ورودی دادن
# if var_input == var2:         #اگه متغیر اینپوت برابر متغیر 2 بود
#     print("صحیح")
#     qwertyi
#     qwety
# else:
#     print("نادرست")      #پرینت کردن
######################################
# var=int(input("""      وارد کن
# """))
# var2=int(input("وارد کنید"))
# print(var+var2)
####################################
# import colorama
# from colorama import *
# user1 =input("اسم کوچیک :")
# user2=input("""  نام خانوادگی """)
# print(f"{Fore.RED}اسم شاگرد{user1,user2} ")
#############################################
# d=2
# a=5
# result=(d**2,a**7)
# print(result)
###############################
# def theName_of_Tabe() :    # ساخت تابع
#     result = 2+2
#     return result
#     print(result)
# theName_of_Tabe() #صدا زنی تابع
#
# def riazi(): #ساختن تابع
#     d=2
#     a=5
#     result=(d**2,a**7)
#     print(result)
# riazi()
###########################x
# for var in range (1,11):
#     if var % 2 == 0:
#         print(var)
#########################
# var1=int(input("enter number"))
# if var1==5:
#     print("hello world")
# else:
#     print("goodbye")
#########################
# for i in range(10):
#     var_input=input("Enter a number:")
#     print(var_input)
# ########################
# for i in range(1,11):               #1,2,3,4,5,6,7,8,9,10
#     for j in range(1,11):           #1,2,3,4,5,6,7,8,9,10
#         print(i*j,end=" ")                  #
#
##############################
# for var in range(10):
#     var1 = input("ورودی را وارد کنید")
############################
# while True:
#     user1 = int(input("Enter a number: "))
#
#     if user1 == 1:              #شرط اول=2
#         x=int(input("number1: "))
#         i=int(input("number2: "))
#         print(x*i)
#
#     elif user1==2:      #شرط دوم= 3
#         print(5%2)
#
#     else :              #شرط آخر
#         print("program ended")  #مذفری
##########################################
# for i in range(10):
#     var=input("Enter txt")
#     print(var)
#########################################
# dadbin=[]
# for i in range(10):
#     pipi=input("مرتیکه ورودی بده")
#     dadbin.append(pipi)
# print(dadbin)
#######################################
# "از کاربر دوتا ورودی بگیره و حاصلشونو تو لیست بندازه و مجموعا 3تا حاصل تتوی لیست بایذ باشه "
# def gamkardan ():
#     list1=[]
#     for i in range(3):
#         var_input=int(input("ورودی وارد کنید"))
#         var_input2=int(input("ورودی وارد کنید2"))
#         result= int(var_input ** var_input2)
#         list1.append(result)
#     print(list1)
# gamkardan()
###########################################
# list_GUNS=["scar_L","shotgun","pistol","kninfe"]
# for pipi in list_GUNS:
#######################
# def hello():
#     myList=[80,80]
#     box= None
#     for num in myList:
#         if box is None or num >box:
#             box = num
#     return box
# print(hello())
#################
# myList=[2,45,80,80,53]
# var1= ("سلام")
# var2=2
# print(type(myList))
# print(type(var1))
# print(type(var2))
########################
# animal = ['cat', 'dog', 'rabbit', 'pig']
# print(animal)
# animal.remove('rabbit')
# print('Updated animal list: ', animal)
# #########################
#    متود لن
###############################################
#          8 MILL    , 3 MILL  ,    6 MILL   ,    13 MILL
# list1=["G1-Cyberpunk","G2-Pubg","G3-God of war","G4-ninja giden","bat1"]
# list2=[]
# for i in range (len(list1)):
#     var_input=input("Enter a number: ")
#     list2.append(var_input)
#     print(list1)
#     print(list2)
####################################
# MY_list=["Engine v12", "v8","v16"]
# print("""ورودی خود را انتخواب کنید:
# 1=اضافه کردن به لیست
# 2=مرطب کردن لیست""")
# while True :
#     var_iput=int(input("here:"))
#     if var_iput ==1:
#         for i in range(4):
#             var_iput2=str(input(f"{i+1}ورودی لیست"))
#             MY_list.append(var_iput2)
#         print(MY_list)
#     elif var_iput ==2:
#         MY_list.sort()
#         print(MY_list)
#
#     elif var_iput ==3:
#         var_Bazgasht=MY_list.pop(0)
#         print('Updated List: ', MY_list)
#
#
#     elif var_iput ==0:
#         break
#########################
# engine=[12,34,45,65]
# var_input=int(input("vorde bdh mrtekh"))
# if var_input==1:
# 	for i in range(4):
# 		var_input2=input("vorde bdh Spider")
# 		engine.append(var_input2)
# 		print(engine)
# elif var_input==2:
# 	engine.sort()
#########################
# var_input2 =int(input("vard koned"))
# for i in range(var_input2):
# 	print("slam mrtekh")
# # ii = input("vared")
# # for i in range(ii):
#######################
# list1=[]
# print("اگه 1 وارد کنید از شما 4 تا ورودی گرفته میشود_ 0= برنامه پایان میابد")
# var_input=input("enter ")
# if var_input == 1:
#     for i in range(4):
#         var_input2=input("enter hnrogh ")
#         list1.append(var_input2)
#         print(f"NEW LIST:", list1 )
#######################
# #جلسه جدید
# #لیست کامپیرشن
# list_1=[int(input("enater a number")) for i in range(10) if i>5]
# print(list_1)
##########جلسه 14########
import colorama
from colorama import *
# def years():
#     day=int(input("enter day"))
#     moth="شهریور"
#     year=int(input("enter year"))
#     print(f"1-dadbin birthday is:{day}/{moth}/{year}")
#     print("2-dadbin birthday is:"+str(year)+" "+str(moth)+" "+str(day))
#     tarigh=str(day)+"/"+str(moth)+"/"+str(year)
#     print(tarigh)
#     print("3-dadbin birthday is:"+tarigh)
# years()
############ جلسه 15###########
# year="HR"
# moth="KR"
# day=3
# print("4-dadbin \nbirthday is: {} {} {} ".format(year , moth , day))

# import colorama
# from colorama import *
#
# def tabe1():
#     years=input(Back.CYAN + f"Enter the {Fore.YELLOW}years{Fore.RESET} you want: ")
#     moth=input(Style.BRIGHT+ "Enter the moth: "+ Style.RESET_ALL+Back.CYAN)
#     day=input(Fore.MAGENTA + "Enter the day: "+Fore.RESET)
#     print("your data is : {}/{}/{}".format(years,moth,day)+Back.RESET)
# tabe1()
#########################
# from colorama import Fore, Style, init
#
# init(autoreset=True)  # برای اینکه رنگ ها بعد از هر چاپ ریست بشن
#
# colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE,
# Fore.MAGENTA,
# Fore.CYAN, Fore.WHITE, Fore.LIGHTRED_EX,
# Fore.LIGHTGREEN_EX, Fore.LIGHTBLUE_EX]
# for i in range(10):
#     print(f"{colors[i]}{i}", end=" ")
# ##############################
# import colorama
# from colorama import *
# print(f"{Fore.YELLOW} hellow {Fore.RED} World")
##############################
# list1 = [423,5,33,86]
# list2 = []
#
# for i in range (len(list1)):
#     input_1= input(str(i+1) +" enter number")
#     list2.append(input_1)
#     var_t = list2.sort()
#
# var_s =list1.sort()
# var_zip =zip(list2,list1)
# print(list(var_zip))

##################

# def music(track1,track2):
#     print(int(track1 + track2))
# music(10,20)

###############
#                 # 0     1     2      3      4
# list_laptop = ["asus","tuf","ROG","lenovo","hp"]
# print(list_laptop[0])
# list_price = []
# for i in range(5):
#     var=input("قیمت رو وارد کن")
#     list_price.append(var)
# print(list_price)
# varzip=zip(list_laptop,list_price)
# print(list(varzip))
# ##########################
# person = {"name":"قاتل25","age":12 ,"fild":"programer", "years":1393, "moth":"sharivar"}
# for key,valu in person.items():
#     print(f"{key}: {valu}")
