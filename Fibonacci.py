n=int(input("Number of digits"))
a=0
b=1
count=0
if n<=0:
    print("not valid")
elif n==1:
    print("The fibonacci sequence upto",n,":")
    print(a)
else:
    print("The fibonacci sequence of numbers is:")
    while count<n:
        print(a)
        n1=a+b
        a=b
        b=n1
        count+=1
