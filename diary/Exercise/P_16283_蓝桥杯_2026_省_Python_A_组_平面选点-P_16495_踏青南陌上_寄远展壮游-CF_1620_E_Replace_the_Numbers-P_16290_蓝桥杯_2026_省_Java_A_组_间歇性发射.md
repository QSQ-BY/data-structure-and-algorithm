# 平面选点、踏青、整体替换与间歇性发射

2026 年 9 月 18 日

## P16283：面积是否为整数，只取决于坐标的奇偶性

[源码](../../Exercise/math/P_16283_蓝桥杯_2026_省_Python_A_组_平面选点.py)

点 $A$ 固定在原点，三角形面积可以写成

$$
S_{\triangle ABC}=\frac{|x_B y_C-y_B x_C|}{2}.
$$

所以问题并不需要枚举四百多万个整点。面积是否为整数，只看行列式 $x_B y_C-y_B x_C$ 是奇数还是偶数，也就只看四个坐标模 2 之后的结果。

我把所有点按 $(x\bmod 2,y\bmod 2)$ 分成四类。横纵坐标各有 1014 个偶数和 1013 个奇数，其中偶偶类还要去掉原点：

```python
even_even = 1014 * 1014 - 1
odd_even = 1013 * 1014
even_odd = 1014 * 1013
odd_odd = 1013 * 1013

ans = even_even * (odd_even + even_odd + odd_odd)

ans += even_even * (even_even - 1) // 2
ans += odd_even * (odd_even - 1) // 2
ans += even_odd * (even_odd - 1) // 2
ans += odd_odd * (odd_odd - 1) // 2
```

同一类中的两个点一定合法，因为两个乘积的奇偶性相同，作差后是偶数。偶偶类与其他三类搭配也一定合法。剩下三种非零奇偶类型两两搭配时，行列式为奇数，面积会多出 $\frac12$，不能计入答案。

这样只需统计四类点的数量，再做组合计数。当前程序算出的答案是 `5277593321988`。

## P16495：不维护景点之间的边，改维护“缺少的景色”

[源码](../../Exercise/unionset/P_16495_踏青南陌上_寄远展壮游.py)

如果直接把景点当作节点，那么每加入一个景点，都要检查它与以前所有景点能否相邻，总复杂度会到 $O(q^2)$。这题真正有用的限制是 $n\le 60$，景色种类很少，而景点很多。

令 `mask` 表示全部景色，`reject = mask ^ spot` 就是当前景点缺少的景色集合。两个景点可以相邻，当且仅当它们至少共同缺少一种景色。于是我不再给景点连边，而是用并查集维护至多 60 个二进制位：一个景点缺少多个景色时，就把这些位连在一起。

```python
        # 当前景点缺少哪些景色
        reject = mask ^ spot

        # 111...111
        if reject == 0:
            alone += 1
            print(u.component_count + alone)
            continue

        bits = []
        x = reject
        while x:
            lowbit = x & -x
            bit = lowbit.bit_length() - 1
            bits.append(bit)
            u.add(bit)
            x -= lowbit

        first = bits[0]
        for bit in bits[1:]:
            u.merge(first, bit)
```

这里可以把每个景点看成一条连接若干“缺失位”的超边。两个景点若有共同的缺失位，就落在同一个连通块；若能通过若干景点间接相连，对应的缺失位也会被并查集合并。因此，有效二进制位的连通块数，就是非孤立景点图的连通块数。

还有一种必须单独处理的景点：如果 `reject == 0`，它已经包含全部景色，与任何景点按位或都会得到 `mask`，连自己也不能相邻。每出现一次都要多安排一次踏青，所以用 `alone` 单独累计。

每个景点最多枚举 $n$ 个二进制位，时间复杂度为 $O(qn\alpha(n))$，并查集本身只需要 $O(n)$ 空间。题目样例的四次答案 `1 2 1 2` 与当前程序输出一致。

## CF1620E：倒着看，整体替换就不再需要碰数组

[源码](../../Exercise/Ad-hoc/CF_1620_E_Replace_the_Numbers.py)

正向处理 `2 x y` 时，如果真的扫描数组并替换所有 `x`，一次操作就可能花掉线性时间。更麻烦的是，先前加入的 `x` 会被替换，后来加入的 `x` 却不受这次操作影响，不能只维护一个从原值到当前值的静态映射。

把所有操作倒过来以后，这个时间关系清楚了。扫描到某次插入时，它后面的全部替换都已经处理完，字典里可以直接查到这个数最后会变成什么：

```python
for operation in reversed(operations):
    scode = operation[0]
    match(scode):
        case 1:
            number = operation[1]
            arr.append(replace.get(number,number))
        case 2:
            x, y = operation[1], operation[2]
            # x -> y
            # 而 y 之后可能还会继续变化
            replace[x] = replace.get(y, y)

arr.reverse()
print(*arr)
```

倒序遇到 `2 x y` 时，含义是：在这次操作之前出现的 `x`，从此要沿用 `y` 在后缀操作中的最终结果。因此更新 `replace[x] = replace.get(y, y)` 即可，不需要修改已经收集的答案。倒序收集的插入值最后再整体反转，恢复原来的排列顺序。

每个操作只处理一次，时间复杂度为 $O(q)$，操作列表、答案与映射共占 $O(q)$ 空间。当前程序重新跑过题目第一、第三组样例，分别输出 `3 2 2 3 2` 和 `1 3 3 7`。

## P16290：把工作与休眠压成四个时刻一组

[源码](../../Exercise/math/P_16290_蓝桥杯_2026_省_Java_A_组_间歇性发射.py)

题目从 $2A$ 开始计时。观察 $V=\lfloor k/2\rfloor-A+1$ 的奇偶性，可以发现发射机连续工作两个时刻，再休眠两个时刻：

$$
[2A+4t,\ 2A+4t+1]
$$

是第 $t$ 个完整周期中需要参与异或的部分。每个工作块里的两个数是相邻的偶数与奇数，它们的异或恒为 1。

```python
diff = M - 2*A + 1
group , left = divmod(diff,4)
print(group,left)
number1 = 1
number2 = 98765432109874
ans = number1 ^ S ^ number2
print(ans)
```

代入题目的范围后，共有 `18518518576851` 个完整周期，数量为奇数，所以这些周期的异或总贡献是 1；还剩一个时刻，正好是 $M=98765432109874$，它也处于工作状态。再与初始值 $S=20260411$ 异或，最后一行得到 `98765445405960`。
