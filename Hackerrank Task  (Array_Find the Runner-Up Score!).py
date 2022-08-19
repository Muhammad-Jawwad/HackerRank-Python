'''
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.


Input Format :
The first line contains n. The second line contains an array A[] of n integers each separated by a space.

Constraints :
* 2 <= n <= 10
* -100 <= A[i] <= 100

Output Format :
Print the runner-up score.'''

# Writing a program to print runner-up score.
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    if 2<=n<=10 or -100 <= arr[i] <= 100:
        arr = list(dict.fromkeys(arr)) # using dict.fromkeys() to remove the duplicates.
        arr.sort() # using .sort() to arranging list in ascending order.
        arr.reverse() # using .reverse() to reversing the order of the list.
        print(arr[1]) 
