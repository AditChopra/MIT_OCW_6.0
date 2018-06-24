#print(3+'ab)
#static semantic error will be obtained in line 1 as 3 is an integer data type and ab is a string
print(str(3)+'ab')
print('3'+'ab')
print 4<'3'
#Notice, in line 5, 4 is less than string 3, whereas
print'4'<'3'
#string 4 is not less than string 3.REASON:- Every symbol gets translated into a particular encoding, a string of bit, inside the machine. there is a particular one called  ASCII, and that is what the machine is actually compating here. 
#exercise some type discipline
print'4'>'3'
#result is true.
print(9/5)
#output=1. This is the greatest integer associated with 9/5. 
#we can find the remainder as follows by using the % operator as the remainder function
print(9%5)
#BODMAS application in Python: Operator preference- **(exponent)>* or / > + or-
#example:-
print(3+4*5)
#result is 23 as expected. 
#if we want 35 as the result, we need to specify that explicitly in the code. 
print((3+4)*5)#the result is 35. 



x=3
x=x*x
print x
n= raw_input('enter a number: ')
print '\n'
print n + 2