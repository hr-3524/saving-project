# class MARVEL_VS_CAPCOP:
#     def __init__(self,Name,Power,Speed,type):
#         self.Name = Name
#         self.Power=Power
#         self.Speed=Speed
#         self.type=type
#     def COUNT_STARS(self,value):
#         if value >= 200:
#             return "**" ""
#         else:
#             return "*" ""
#     def __repr__(self):
#         stars=self.COUNT_STARS(self.Power)+self.COUNT_STARS(self.Speed)
#         t_stars=(len(stars))
#         return (f"HERO NAME: {self.Name} POWER: {self.Power} SPEED: {self.Speed} {stars} {t_stars}`")
# C1=MARVEL_VS_CAPCOP("SPIDER_MAN",10,300,"LEGENDARY")
# C2=MARVEL_VS_CAPCOP("IRON_MAN",400,400,"EPIC")
# list_Heroes=[C1,C2]
# for shomarnde , N in enumerate(list_Heroes,start=1):
#     print(shomarnde,N)
# var_input=input("Enter your Hero name: ")
# for heros in list_Heroes:
#     if var_input ==heros.Name:
#         print(f"{heros.Name,heros.Power,heros.Speed}")
#     elif var_input.upper() == (heros.Name+"type").upper():
#         total=heros.Power+heros.Speed
#         print(f"{heros.Name} IS {heros.type} total: {total}")
################################################################
    #آموزش دیکشنری
# person = {"name":"Ali","age":20,"high":180,"city":"tehran"}
# person2 = dict(name="terever",age=42,city="LA")
# # del person["age"]        # حذف کلید age
# age_value = person.pop("age", None)  # حذف و گرفتن مقدار
# print(person)
# if "key test" in person:
#     print(person["key test"])
########################
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
#
###########################
# import requests
# import json
#
# url = "https://stat.ripe.net/data/announced-prefixes/data.json?resource=AS3333&starttime=2011-12-12T12:00"
# request_var = requests.request("GET", url)
# result = request_var.json()
#
# prefixes = result["data"]["prefixes"]
#
# for item in prefixes:
#     for t in item["timelines"]:
#         print(t["starttime"])
#
#
#############################
# import requests
# import json
#
# myURL = "https://stat.ripe.net/data/announced-prefixes/data.json?resource=AS3333&starttime=2011-12-12T12:00"
#
# response = requests.get(myURL)
#
# data = response.json()
#
# print(json.dumps(data, indent=4, ensure_ascii=False))


#############################################
# Falseimport requests
# import json_data
# my_url="https://stat.ripe.net/data/announced-prefixes/data.json"
# var1= requests.request("GET", my_url)
# result= var1.json()
#
# varFind=result["status_code"]result["version"]
# print(varFind)
###############################
# dict1={
#     "student1":{
#         "name":"ALex","age":15,"city":"new york city","fild":"math"
#         },
#     "student2":{
#         "name":"max","age":16,"city":"washington dc","fild":"physics"
#     }
# }
# print(("چاپ اسم و رشته--> ")+ dict1["student1"]["name"],dict1["student1"]["fild"])
# for k,v in dict1["student1"].items():
#     print(("چاپ همه کلید و  ولیو ها")+k,v)
######################################
# from datetime import datetime
#
# now= datetime.now()
# day = now.strftime("%d")
# month = now.strftime("%m")
# year = now.strftime("%Y")
# print(f"روز:{day}")
# print(f"ماه:{month}")
# print(f"سال:{year}")
# print(f"{year}/{month}/{day}\n")

#######################
# import requests
# import json
# import datetime
# now = datetime.datetime.now()
#
# day=strftime("%d")
# month=now.strftime("%m")
# year=now.strftime("%Y")
# hour=now.strftime("%H")
# minute=now.strftime("%M")
# url = f"https://stat.ripe.net/data/announced-prefixes/data.json?resource=AS3333&starttime={year}-{month}-{day}T{hour}:{minute}"
# request_var= requests.request("GET", url)
# result =request_var.json()
# var_itreration = result["data"]["prefixes"]
# for item in var_itreration:
#     print(item["prefix"])
#####################################import requests
# from datetime import datetime
# import requests
#
# now = datetime.now()
#
# starttime = now.strftime("%Y-%m-%dT%H:%M")
#
# url = f"https://stat.ripe.net/data/announced-prefixes/data.json?resource=AS3333&starttime={starttime}"
# print(url)
#
# response = requests.get(url)
# result = response.json()
# var_itreration = result["data"]["prefixes"]
# for item in var_itreration:
#     print(item["prefix"])
#########################################
#
# import requests
#
# myURL= "https://brsapi.ir/Api/Market/Sample/FreeApi_Gold_Currency.json"
# varRE = requests.request("GET", myURL)
# cover_to_dict = varRE.json()
# result = cover_to_dict["gold"]
# x=result[0]
# print("نام:",x["name"])
# print("قیمت:",x["price"],x["unit"],x["date"])
#
# for item in result:
#     print(item["name"],item["price"],item["unit"],item["date"],item["time"])
#################################
# import time
#
# score = 0
#
# def level_up():
#     print("🚀 لِوِل آپ! بریم مرحله بعد!")
#     filepath=r"C:\Users\ASUS\Desktop\dragon.txt"
#     with open(filepath, "r", encoding="utf-8") as f:
#         dragon = f.read()
#     print(dragon)
#
# while score < 100:
#     score += 20
#     print(f"امتیاز: {score}")
#     time.sleep(0.5)  # یه مکث کوتاه
#
#     if score == 100:
#         level_up()

#########################
# import requests
# class dictAPI:
#     def __init__(self,url):
#         self.url = url
#     def tabe(self):
#         request_var = requests.request("GET", url)
#         result = request_var.json()
#         var_itreration = result["data"]["prefixes"]
#         for item in var_itreration:
#             print(item["prefix"])
# url = input("Enter the URL: ")
# obj1 = dictAPI(url).tabe()
#######################
# import requests
#
# class Mainclass:
#     def __init__(self,url):
#         self.url = url
#
#     def request_for_content(self):
#         req_data = requests.request("GET",self.url).json()
#         var_find = req_data['data']["prefixes"]
#         data_list = []
#         for i in var_find:
#             data_list.append(i["prefix"])
#         yield data_list
# url = input("Enter your url")
# obj1 = Mainclass(url).request_for_content()
# for i in obj1:
#     print(i)

######################
# import requests
# class mainclass:
#     def __init__(self,url):
#         self.url = url
#     def getData(self):
#         req_data=requests.request("GET",self.url).json()
#         request_content=req_data["data"]["prefixes"]
#         data_list=[]
#         for i in request_content:
#             data_list.append(i["prefix"])
#
################
# import json
# import fastapi
# from fastapi import FastAPI
#
# app=FastAPI()
# db=[
#     {"id":1,"name":"python"},
#     {"id":2,"name":"advance"},
# ]
# @app.get("/")
# def getdata():
#     return db
##################
list_compierhenshen=[var_i for var_i in range(20)]
print(list_compierhenshen)