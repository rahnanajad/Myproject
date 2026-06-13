x=int(input("enter a number:"))
count=0
for a in range(1,x+1):
    if a%x==0:
        count=count+1
print(count)
if count==2:
    print("its a prime number")
else:
    print("its not a prime number")