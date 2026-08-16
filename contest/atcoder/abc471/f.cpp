/* Problem Statement
You are given 
N strings 
S 
1
?
 ,¡­,S 
N
?
  consisting of digits.

Find the maximum possible value, when interpreted as a decimal integer (after removing extra leading zeros), of a string obtained by choosing exactly 
K of these strings and concatenating them in any order of your choice.

Here, the value obtained by interpreting a string consisting entirely of the character 0 as a decimal integer after removing extra leading zeros is defined to be 
0.

Constraints
1¡ÜK¡ÜN¡Ü10 
5
 
S 
i
?
  is a string of length between 
1 and 
10 (inclusive) consisting of digits.
N and 
K are integers.
Input
The input is given from Standard Input in the following format:

N 
K
S 
1
?
 
?
S 
N
?
 
Output
Output the answer.

Sample Input 1
Copy
3 2
123
45
6
Sample Output 1
Copy
45123
There are six strings obtained by choosing two of 123, 45, 6 and concatenating them: 12345, 1236, 45123, 456, 6123, 645.

Among these, the maximum value when interpreted as a decimal integer is 
45123.

Sample Input 2
Copy
5 3
00000
00
1
0000
000
Sample Output 2
Copy
1000000000
Sample Input 3
Copy
9 9
0000000001
000000002
00000003
0000004
000005
00006
0007
008
09
Sample Output 3
Copy
90080007000060000050000004000000030000000020000000001 */