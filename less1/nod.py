a= int(input())
b= int(input())
c1 = min(a,b)
print (c1)
for i in range(2, c1+1):
    print(i)
    if a%i ==0 and b%i ==0:
        print("SSSS")
        a=a//i
        b=b//i
print(a) 
print(b)