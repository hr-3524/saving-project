####_____CLASS_____###
# class Sherkat_CAR:
#     def __init__(self,name,speed):
#         self.name = name
#         self.speed = speed
#
# car1= Sherkat_CAR("Car1",100)

####____DECORATOR ____####
# def Deco(funk):
#     def inner_def():
#         main=funk()
#         var_input=input("Enter your lastname: ")
#         return (f"""name: {main}
# lastname: <{var_input}>""")
#     return inner_def
#
# @Deco
# def main():
#     name = "<HOOMAN>"
#     return name
# print(main())

####____TAMRIN_CLASS____####
# from colorama import *
# class SuperHero_game:
#     def __init__(self, nickname, lastname,power,speed,mind):
#         self.name=nickname
#         self.lastname=lastname
#         self.power=power
#         self.speed=speed
#         self.mind=mind
#
#     def __repr__(self):
#         return (f"Hero(Nickname: {self.name}, Power: {self.power}, Speed: {self.speed})")
#
# character_1=SuperHero_game(f"{Fore.RED}Spider_Man{Fore.RESET}","peterparker",150,320,150)
# character_2=SuperHero_game(f"{Fore.YELLOW}Wolverine{Fore.RESET}","Logan",230,250,90)
# character_3=SuperHero_game(f"{Fore.BLUE}Iron_Man{Fore.RESET}","Tony stark",200,200,200)
# character_4=SuperHero_game(f"{Fore.CYAN}Captain_America{Fore.RESET}","Stive ragers",250,250,140)
# list_Characters=[character_1,character_2,character_3,character_4]
# print(enumerate(list_Characters))
# for i in range(len(list_Characters)):
#     for j in range(i+1,len(list_Characters)):
#         C1=list_Characters[i]   #ارث بری کردن
#         C2=list_Characters[j]
#         print(f"{C1.name} VS {C2.name}")
#
#         if C1.power > C2.power:
#             print(f"{C1.name} :{C1.power} > {C2.name}:{C2.power}\n")
#         elif C1.power < C2.power:
#             print(f"{C1.name} :{C1.power} < {C2.name}:{C2.power}\n")
#         else:
#             print(f"{C1.name} :{C1.power} = {C2.name}:{C2.power}\n")
#################################
class python_class :                #1_ ساخت کلس
    def __init__(self, name, last_name ,age, rule):      #2_ متد و ویژگی های دلخواه
        self.name = name
        self.last_name = last_name
        self.age = age
        self.rule = rule
#3_ساخت اشیا
object1=python_class("Hooman","Rahnama",22, "teacher")
object2=python_class("Dadbin","gholami",15, "student")لهف
#باید ویژگی هارو به ترطیب int__((self, name, last_name ,age, rule))__g
#با توجه به ترطیب به صورت هوشمند تشخیص میده که مثلا 22میشه age چون سومین تعریف در self است

print(f"name:{object1.name} is {object1.rule}")  #"صدا زدن ویژگی ها"
print(f"name:{object2.name} is {object2.rule}")

#درخواست ویژگی با اینپوت
var_input=input("enter the name you want to see his age :")
list=[object1,object2]
for item in list:
    if item.name==var_input:
        print(item.age)
#################
# dict_score = {
#     "mehran":300,
#     "sara":150,
#     "mahsa":200,
#     "parsa":80
# }
# varSort= sorted(dict_score.items(), key=lambda x: x[1])
# print(varSort)
# varSor2= sorted(dict_score.items(), key=lambda x: x[1], reverse=True)
# print( varSor2)





# for shomaresh, vlue_list in enumerate(list_Characters,start=1):
#     print(shomaresh, vlue_list)

