import sys
input = sys.stdin.buffer.readline
def read():
    return map(float,input().split())
number1 ,number2 = read()
flag = 0
if(number1+number2 == 9 or number1*number2==9 or number1-number2==9 or number1/number2==9):
    flag = 1
if (flag == 0):
    print("Nein")
else:
    print("Nine")