'''
#Average
n = int(input("Enter the number of elements to be inserted: "))
a =[]
for i in range(0,n):
    elem=int(input("Enter element: "))
    a.append(elem)
avg = sum(a)/n
print("Average of elements in the list",round(avg,2))

#positive or negative
n=int(input("Enter number: "))
if(n>0):
    print("Number is positive")
else:
    print("Number is negative")

#Exchange the valaue
a=int(input("Enter value of first variable: "))
b=int(input("Enter value of second variable: "))
a=a+b
b=a-b
a=a-b
print("a is:",a," b is:",b)

# convert cm in inches and feet
cm=int(input("Enter the height in centimeters:"))
inches=0.394*cm
feet=0.0328*cm
print("The length in inches",round(inches,2))
print("The length in feet",round(feet,2))

#smallest divisor
n = int(input("Enter an integer:"))
a = []
for i in range(2,n+1):
    if(n%i==0):
        a.append(i)
a.sort()
print("Smallest divisor is:",a[0])

# genereator all divisor
n=int(input("Enter an integer:"))
print("The divisors of the number are:")
for i in range(1,n+1):
    if(n%i==0):
        print(i)
'''
# print all possible digit
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
f=int(input("Enter third number:"))
e=int(input("Enter third number:"))
d=[]
d.append(a)
d.append(b)
d.append(c)
d.append(f)
d.append(e)
for i in range(0,5):
    for j in range(0,5):
        for k in range(0,5):
            for l in range(0, 5):
                for m in range(0, 5):
                    if(i!=j&j!=k&k!=l&l!=m&m!=i):
                        print(d[i],d[j],d[k],d[l])





