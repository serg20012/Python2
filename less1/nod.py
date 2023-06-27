a= int(input())
b= int(input())
c1 = min(a,b)
print (c1)
for i in range(1, c1//2+1):
    print(i)
    if a%i ==0 and b%i ==0:
        a=a//i
        b=b//i
print(a) 
print(b)