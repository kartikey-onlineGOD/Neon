print("Program 6")
a = [1,5,9,2]
b = [5,8,3,6]
c =[]

for i in range(len(a)):
    c.append(a[i] + b[i])

print(c)


print("Program 3")
m = []
ch = True
while(ch == True):
    k = int(input("Enter a number between 1 and 12 :  "))
    if(k > 10):
        k = 10 
    m.append(k)
    g = input(" Do you want to enter more numbers [ y/n ] :  ")
    if(g == "y"):
        ch = True
    else :
        ch = False 
    
print(m)
