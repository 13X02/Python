import functools

n = int(input("Enter the Number"))
list = [1]
for i in range(n):
    list.append(i+1)

result = functools.reduce(lambda x,y:x*y,list)

print(" factorial is ",result)