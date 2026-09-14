from colorama import Fore, Back, Style
def p1():
    list_Book = ["Komdi elahi","HAFEZ","Kimiagar"]
    list_price =[]
    while True:
        print(""f"""{Fore.YELLOW} 
        enter rhe number of your proxes ...{Fore.RESET} 
        (1= jam, 2= tafrigh, 3= PRINT LIST, 4= add to list, 5= Delete 6=Show deleted value, 7=add price, 8=max price:   """"")
        var_input = int(input(""))
###########################
        if var_input == 1:
            result1=2+2
            print(result1)
##########################
        elif var_input == 2:
            var_tafrigh1 = int(input("enter the number1 you want to tafrigh"))
            var_tafrigh2 = int(input("enter the number2 you want to tafrigh"))
            result = var_tafrigh1 - var_tafrigh2
            print(result)
#########################
        elif var_input == 3:
            print(list_Book)
########################
        elif var_input == 4:
            list_input = input("""enter the new valiu of list: 
            """)
            list_Book.append(list_input)
###########################
        elif var_input == 5:
            var_dr = list_Book.pop(int(input("enter the new valiu of list:")))
            print(list_Book)
##############################
        elif var_input == 6:
            print("/The Deleted value:",var_dr,"/")
###############################
        # elif var_input == 7:
        #      for i in range(len(list_Book)):
        #       var_input_user = list_price.append(int(input("enter the new valiu of list:")))
        #      name_and_price =zip(list_Book,list_price)
        #      print()
###############################
        elif var_input == 7:
            for i in range(len(list_Book)):
                input_price = int(input(f"{i+(1)} enter the new price:"))
                list_price.append(input_price)
            result=[print(f"  {i} {Fore.YELLOW} {B} = {P} {Fore.RESET}" ,end="  | ")for i,(B,P) in
            enumerate(zip(list_Book,list_price),start=1)]
    ###############################
        elif var_input == 8:
            if not list_price:
                print("/ * enter the price value * /")
            else:
                varmax = max(list_price)
                print(f"the max price is (* {varmax} *)")
p1()