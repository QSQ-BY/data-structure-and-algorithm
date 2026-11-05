# 护盾上限与从两端向内计算的区间

2026-10-23 的练习，2026-10-24 补记。

源码：[P15436](../../Exercise/dynamic_programming/P_15436_蓝桥杯_2025_国_Python_B_魔法护盾.py) · [P9232](../../Exercise/dynamic_programming/P_9232_蓝桥杯_2023_省_A_更小的数.py) · [P9325](../../Exercise/dynamic_programming/P_9325_CCC_2023_S_2_Symmetric_Mountains.py)

## P15436 魔法护盾：上限使过去的收益不能随时补回来

我开始想用二分加反悔贪心，并要求先忽略 `limit`，把这个想法实现出来。没有上限时，遇到护盾不足，可以从已经经过的正收益房间里挑最大的增幅；恢复上限后，这种补选就有问题。早先房间的额外收益可能当时就被上限截掉，不能等未来不足时再完整补回来。

二分最多用几次技能仍有单调性，但内部判定需要记录护盾变化。后来我追问了直接 DP：`dp[i][j]` 表示通过前 `i` 个房间、恰好用 `j` 次增幅时能保留的最大护盾。当前源码已压成一维，倒序更新 `j`：

```python
for i, (s, a) in enumerate(zip(arr1, arr2), start=1):
    for j in range(i,-1,-1):
        best = -1
        # 当前房间不增幅，之前已经使用了j次
        if dp[j] >= 0:
            best = min(limit, dp[j] + s)
        # s <= 0 时，增幅没有好处，不需要考虑
        if j > 0 and s > 0 and dp[j - 1] >= 0:
            best = max(best, min(limit, dp[j - 1] + 2 * s))

        dp[j] = best if best >= a else -1
```

每个房间分别考虑不增幅与增幅，先把护盾截到 `limit`，再判断是否承受得住攻击。攻击只检查护盾是否达标，不扣掉攻击值；`-1` 表示无法继续。

处理相同数量的房间、使用相同次数技能时，护盾更多的状态不会更差，所以只保留最大值。直接 DP 时间为 $O(n^2)$，当前一维实现空间为 $O(n)$；最后按次数从小到大找第一个可行状态，不需要再包二分。

## P9232 更小的数：相等端点把比较交给内部

反转区间后，区间外不变，大小比较从左端开始。原左端大于原右端，反转后立刻变小；原左端更小，则立刻变大；两端相等时，再比较内部反转的效果。

```python
for length in range(2,n+1):
    #length表示数组的长度，i表示右端点
    for j in range(length-1,n):
        i = j - length + 1 
        if s[i] > s[j]:
            dp[i][j] = 1
        elif s[i] < s[j]:
            dp[i][j] = 0
        else:
            dp[i][j] = dp[i + 1][j - 1]
        ans += dp[i][j]
```

`dp[i][j]` 只需要保存是否变小，不必构造反转后的字符串。长度从小到大枚举，保证相等端点时依赖的内部区间已有结果。

我要求保留二维数组，源码用每行一个 `bytearray` 保存 0/1。时间和逻辑空间都是 $O(n^2)$，比用 Python 列表逐格保存引用更省内存。

## P9325 Symmetric Mountains：独立加入一对端点的贡献

不整齐度是对称位置的高度差绝对值之和。去掉最外一对，剩下正好是内部区间，因此：

$$
dp[l][r]=dp[l+1][r-1]+|a_l-a_r|.
$$

源码先处理长度 2、3，再从长度 4 开始递推：

```python
for length in range(4,n+1):
    new_ans = float("inf")
    for right in range(length-1,n):
        left = right - length+1
        dp[left][right] = dp[left+1][right-1]+abs(arr[left] - arr[right])
        new_ans = min(new_ans,dp[left][right])
    ans.append(new_ans)
```

每个长度都要独立求所有起点的最小值，`new_ans` 放在长度循环内部重置。长度 1 的不整齐度是 0，偶数长度最终依赖长度 2，奇数长度最终依赖长度 3。时间、空间都是 $O(n^2)$。

这两道区间题都在比较两端，但保存的答案不同：P9232 保存大小关系是否成立，P9325 保存累加的数值。写转移前，我需要先说清区间的答案究竟是什么。
