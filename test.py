# from jeff_function import trim 
# from jeff_function import testTrim
# testTrim()
#yourName=input("please enter your name!\n:")
print("hello","wujinfeng")
i=0
sum=0
while i<=100:
    sum+=i
    i+=1
print(sum)
i=0
sum=0
for i in range(101):
    sum+=i
    i+=1
print("16进制sum=",hex(sum),"10进制sum=",sum)
print([x**2 for x in range(1,11)])