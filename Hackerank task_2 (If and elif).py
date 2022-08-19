#Hackerank task_02
'''Task:-
Given an integer, 1 <= n <= 100, perform the following conditional actions by using if and else:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird '''

# Writing a program
n = int(input("Enter a number:"))
if 1 <= n <= 100:
    if (n%2)!=0:
        print("Weird")
    elif  2 <= n <= 5 and (n%2)==0:
        print("Not Weird")
    elif  6<=n<=20 and (n%2)==0:
        print("Weird")
    elif (n%2)==0 and n>20:
        print("Not Weird")
else:
    print("Out of range")        
