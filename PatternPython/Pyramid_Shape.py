#    *
#   * *
#  * * *
# * * * *

num = int(input("Enter Number of Rows: "))
# num = 4
for i in range(0,num):
    for j in range(0,num-i-1):
        print(end=" ")
    for j in range(0,i+1):
        print("*", end=" ")
    print()
    
    
    
#No Spaces Pyramid 
#num = int(input("Enter Number of Rows: "))
## num = 4
#for i in range(0,num):
#    for j in range(0,num-i-1):
#        print(end=" ")
#    for j in range(0,2*i+1):
#        print("*", end="")
#    print()