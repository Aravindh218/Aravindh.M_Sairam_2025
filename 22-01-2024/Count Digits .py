"""
Given an integer N, write a program to count the number of digits in N.

Input Format

Example 1: Input0: N = 12345

Example 2: Input1: N = 8394

Constraints

n <= 10000

Output Format

Output0: 5 Explanation: N has 5 digits

Output1: 4 Explanation: N has 4 digits

Sample Input 0

12345
Sample Output 0

5
Sample Input 1

876349
Sample Output 1

6

"""


n= int(input().strip())
if n<=1000000:
    num_n = len(str(n))
    print(num_n)
else:
    print("input not valid")
