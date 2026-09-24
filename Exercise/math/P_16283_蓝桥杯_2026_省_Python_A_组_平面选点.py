import sys
import math
""" 题目描述
在平面直角坐标系中，固定点 A 为坐标原点 (0,0)。

现在，考虑所有横坐标、纵坐标都在 0 到 2026 之间的整点。请你统计满足下列条件的点对 {B,C} 的数量：

B 与 C 都是上述整点，且都不与 A 重合；
B

=C；
由点 A,B,C 构成的三角形面积为整数。
其中，若 A,B,C 三点共线，则三角形面积记为 0，这种情况也计入答案。

点对 {B,C} 不区分顺序，即 {B,C} 与 {C,B} 视为同一点对。

输入格式
无

输出格式
这是一道结果填空题，你只需要算出结果后提交即可。本题的结果为一个整数，在提交答案时只填写这个整数，填写多余的内容将无法得分。 """
even_even = 1014 * 1014 - 1
odd_even = 1013 * 1014
even_odd = 1014 * 1013
odd_odd = 1013 * 1013

ans = even_even * (odd_even + even_odd + odd_odd)

ans += even_even * (even_even - 1) // 2
ans += odd_even * (odd_even - 1) // 2
ans += even_odd * (even_odd - 1) // 2
ans += odd_odd * (odd_odd - 1) // 2

print(ans)