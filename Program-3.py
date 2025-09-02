a = int(input("Enter a Number: "))

if a%2==0 :
    a=a-1
else:
    a=a

for i in range(1,2*a,2):
    print(i,end=", ")