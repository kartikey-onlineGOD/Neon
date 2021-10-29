# Program 1
a = [123 , 456 , 789 , 456]
print(a)

# Method 1 
def rev(a):
    m = a
    k = 0
    while(m > 0):
        d = m%10
        k = (k*10) + d
        m = m//10

    return k

for i in range(len(a)):
    a[i] = rev(a[i])

print(a)    

# Method 2
b = [123 , 456 , 789 , 456]
print(b)
for i in range(len(b)):
    m = b[i]
    k = 0
    while(m > 0):
        d = m%10
        k = (k*10) + d
        m = m//10
    b[i] = k 
print(b)
