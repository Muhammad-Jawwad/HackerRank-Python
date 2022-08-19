'''
TASK:-
The included code stub will read an integer,1<=n<=150, from STDIN.
Without using any string methods, try to print the following: 123...n
Note that "..." represents the consecutive values in between.

Example
n=5
Print the string: 12345
Input Format: The first line contains an integer n.'''

# Writing a program

n = int(input("Enter n:"))
if 1<=n<=150:
    for i in range(1,n+1):
        i = str(i)
        print(i,end="")
