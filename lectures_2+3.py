x=15
y=11
z=10
if x<y and x<z :
    print 'x is least'
elif y<z:
    print 'y is least'
else: print 'z is least'
x= -4
x1 = abs(x)
y=0
itersleft=x1 
while(itersleft>0):
    y=y+x1
    itersleft=itersleft-1
print y
x=15968016
count=1
if x<0: 
    x1=abs(x)
    while(count**2<x1):
        count = count+1
    print str(count)+'i'
elif x>0:
    while(count**2<x):
        count=count+1
    print count

x=15968016
count=1
if x>0:
    while(count**2<x):
        count=count+1
    if count**2==x:
        print count
    else:
        print 'this number is not a perfect square'

# x=36
# count=1
# while(count<x):
#   if x%count==0:
#         print 'divisor is', count
#   count=count+1

#using for loop for finding divisors of a number

x=15
for count in range(1,x+1):
    if x%count==0:
        print 'divisor is ',count


# r1 = range(1, 10)
# print type(r1)
# print r1
# r2 = range(10)
# print r2
# r3 = range(1, 10, 2)
# print r3

# for ix in range(4):
#     print ix

#TUPLE:- ordered sequence of elements ( it's immutable)
test=(1,2,3,4,5)
print test[0]#gives result as (1)
print test[-1]#gives result as (5)
print test[1:3]#gives result as (2,3)
print test[:3]#gives result as (1,2,3)
print test[2:]#gives result as (3,4,5)

#solving the divisor example by tuplelist method
x=100
divisors=[]
for i in range(1,x):
    if x%i==0:
        divisors.append(i)
print divisors

test = (1,2,3,4) ##immutable
test_l = [1,2,3,4] ##mutable
print test[0]
print test_l[0]

test_l[1] = 5
print test_l 


























