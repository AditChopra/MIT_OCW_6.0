#LECTURE 4

#defining a square root function
# def sqrt(x):
#     '''returns the value of sqaure root of x is x is a perfect square'''
   
#     count=0
#     if x>=0:
#         while (count**2<x):
#             count=count+1
#         if count**2!=x:
#             print x,'is not a perfect sqaure'
#             return none 
#         else: 
#             return count
#     else:
#         print x,'is a negative number'
#     return none

# # #defining a function f(x)
# def f(x):
#     x=x+1
#     return x

#QUESTION:- a farmer has some pigs and some chicken. In total he notices 20 heads and 56 legs. Then find the number of pigs and no of chicken. 
##lets formulate some basic linear equations:- 1) number(pigs)+number(chicken)=20 ;2) 4*number(pigs)+2*number(chicken)=56. 
##code is as follows

# def solve(numheads,numlegs):
#     for numchiks in range(1,numheads+1):
#         numpigs=numheads-numchiks
#         total_legs=numchiks*2+numpigs*4
#         if total_legs==numlegs:
#             return (numpigs,numchiks)

#     return (none,none)



# def main():
#     # heads=int(raw_input('enter number of heads:'))
#     # legs=int(raw_input('enter number of legs:'))
#     heads=20
#     legs=56
#     pigs,chicken=solve(heads,legs)
#     print 'number of pigs are', pigs
#     print 'number of chicken are', chicken

#main()
# Part-2 to the above problem .Let us consider that the farner alse has spiders on his farm. now we have 3 variables but only 2 equations.
#Thus , this cannot be solved by simple algebra. 
##NOTE:- a spider has 8 legs
###code will be changed as follows:

# def solve1(numHeads,numLegs):
#     print 'in Solve1'
#     for numSpiders in range(0,numHeads+1):
#         for numChiks in range(0,numHeads-numSpiders+1):
#             numPigs=numHeads-numSpiders-numChiks
#             total_Legs=numSpiders*8+numChiks*2+numPigs*4
#             if total_Legs==numLegs:
#                 return(numPigs,numChiks,numSpiders)
    
#     return (None,None,None)

# def main():
#     # heads=int(raw_input('enter number of heads: '))
#     # legs=int(raw_input('enter number of legs: '))
#     Heads=21
#     Legs=64
#     print 'Calling'
#     pigs,chicken,spiders=solve1(Heads,Legs)
#     print 'number of pigs are', pigs
#     print 'number of chicken are',chicken
#     print 'number of spiders are',spiders

# main()

#RECURSION
##1) break the problem into a simpler version of thje same problem and some other steps
### simple example of a code to calculate the factorial of a number

def cal_factorial(x):
    '''cal_factorial is a recursive function to calculate the factorial of a number'''
    if x==1:
        return 1
    else:
        return (x*(cal_factorial(x-1)))
x=4
print cal_factorial(x)


##printing reverse of a function
def reverse_string(s):
    my_string=''
    count=len(s)-1
    while count>=0:
        my_string=my_string+s[count]
        count=count-1
    return my_string

##Sum of n natural numbers
n=10
if n<=0:
    print 'please enter a positive number'
else:
    sum=0
    while (n>0):
        sum=sum+n
        n=n-1
    print 'the sum is ', sum


def getsum(n):
    sum = 0
    list_of_num = range(1, n+1)
    for num in list_of_num:
        sum = sum + num

    return sum

print getsum(8)

x = range(1, 10)
print x
print len(x)
for number in x:
    print number,
































