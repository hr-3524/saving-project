# n = 10
# while n > 0:
#     print("*" * n )
#     n -= 1
##############
# for i in range(10):
#     print("*" * i )
#     i-=1

############
# for x in range(2):
#     for i in range(1,10):
#         while i-1==0:
#             print("*",end=" ")
#     print("\n")
#############
# m=10
# for i in range(m):
#     print("*")
#     for j in range(m):
#          print(i+j)
#####################
n=5
for i in range(n):
    star=" *"*i
    space=" " * (n-i)
    print(space+star)

