from colorama import *
class SuperHero:
    def __init__(self,Nickname,Name,Power,Speed,Mind):
        self.Nickname=Nickname
        self.Name=Name
        self.Power=Power
        self.Speed=Speed
        self.Mind=Mind
    def Get_Stars(self, value):
       if value >= 200:
           return "**"
       else:
           return "*"
    def __repr__(self):
        stars=self.Get_Stars(self.Power)+ self.Get_Stars(self.Speed)+self.Get_Stars(self.Mind)
        stars_count=len(stars)

        return f'Hero name:{self.Nickname} Name: {self.Name} Power: {self.Power} Speed: {self.Speed} Mind: {self.Mind} < {stars} > {stars_count}*\n'
character_1=SuperHero(f"{Fore.RED}SPIDER_MAN{Fore.RESET}","peter parker",150,320,150)
character_2=SuperHero(f"{Fore.YELLOW}Wolverine{Fore.RESET}","Logan",230,250,90)
character_3=SuperHero(f"{Fore.BLUE}Iron_Man{Fore.RESET}","Tony stark",200,200,200)
character_4=SuperHero(f"{Fore.LIGHTCYAN_EX}Captain_America{Fore.RESET}","Stive ragers",250,250,140)

list=[character_1,character_2,character_3,character_4]
for i,j in enumerate(list,start=1):
    print(i,j)
#("انتخاب کرکتر")
fighters=[]
for i in range(2):
    var_input=input(f"{Fore.MAGENTA}player_{i+1} Chose your HERO...")
    for characters in list:
        clean_name=characters.Nickname.replace(Fore.RED,"").replace(Fore.YELLOW,"").replace(Fore.LIGHTCYAN_EX,"").replace(Fore.BLUE,"").replace(Fore.RESET,"")
        if var_input.upper() == clean_name.upper():
            print(characters)
            print(f""""                         {Fore.BLUE} {clean_name} is selected{Fore.RESET}\n""")
            fighters.append(var_input)

        elif var_input.upper() == (clean_name + " secret").upper(): # ("اگه کنار کرکتر secret نوشته شد قدرت واقعی رو نشون بده ")
            total = characters.Power + characters.Speed + characters.Mind
            print(f" {clean_name}: Total: {total}")
print(f"\n {fighters[0]} vs {fighters[1]}")

print("my name is Rahnama")

# random test
# nkjnknjknn;
# j
# jopjjmpoj
# kkkjkjpo

#################
