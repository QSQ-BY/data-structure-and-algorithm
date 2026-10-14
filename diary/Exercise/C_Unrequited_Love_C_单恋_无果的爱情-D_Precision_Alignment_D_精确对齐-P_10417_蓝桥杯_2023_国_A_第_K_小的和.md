# 三和弦计数、精确对齐与第 K 小的和

## Unrequited Love：先按和弦值配对，再扣除有限的重叠

[源码](../../Exercise/Ad-hoc/C_Unrequited_Love_C_单恋_无果的爱情.py)

以 j 开头的三和弦使用 j、j+2、j+4 三个位置，值为 a[j]+a[j+2]-a[j+4]。如果对所有相同值的历史和弦逐一检查重叠，频次很高时仍会退化。

 对两个不同起点，按键发生重叠只可能相差 2 或 4。因此先用频次字典累计相同值的历史数量，再检查这两个固定偏移就够了。

```python
values = [arr[i] + arr[i+2] - arr[i+4] for i in range(n-4)]
freq = {}
ans = 0
for j, value in enumerate(values):
    ans += freq.get(value, 0)
    if j >= 2 and values[j-2] == value:
        ans -= 1
    if j >= 4 and values[j-4] == value:
        ans -= 1
    freq[value] = freq.get(value, 0) + 1
```

先计数、再加入当前和弦，保证每对不同起点只统计一次。区间在几何上看起来相交，也不一定使用相同按键，例如相差 1 的起点可能互不重叠；判断依据是实际下标集合。

 平均时间 O(n)，空间 O(n)。这次消除逐一检查，依靠的是非法配对只有两种偏移，可以在总计数后用常数次修正排除。

## Precision Alignment：先求单个实验室费用，再汇总二分

[源码](../../Exercise/binary_search/D_Precision_Alignment_D_精确对齐.py)

目标是最大化所有实验室三数之和的最小值。我先固定目标 T，分别计算每个初始总和 s<T 的实验室提升到 T 的最小费用。

 三数全等时，所有可用调整都为 0，所以这类实验室给出答案上限。对其他实验室，当前方案把费用写成 T-s+extra；若 a≤b≤c，需要先离开不能直接增大的状态，extra=2(min(b-a,c-b)+1)，其他情况 extra=0。

 将可调整实验室按 s 排序，预处理 extra-s 的前缀和后，一次判定只需找到 s<T 的前缀：

```python
while left < right:
    mid = (left + right + 1) // 2

    # 只有初始总和严格小于 mid 的实验室需要操作
    count = bisect_left(sums, mid)

    # 总费用 = Σ(mid - s + extra)
    cost = count * mid + prefix[count]

    if cost <= k:
        left = mid
    else:
        right = mid - 1
```

count 个实验室共同需要 count·T+prefix[count] 次操作。bisect_left 保证 s==T 的实验室不被收进来，它们本来就满足要求，不该支付额外启动费用。

 目标越大，所需费用不会减少，因此可以二分。设搜索范围宽度为 R，排序和前缀预处理 O(n log n)，每轮判定 O(log n)，总时间 O(n log n+log R·log n)，空间 O(n)。这道题的工作主要在单个实验室的费用公式，二分只是最后把费用与预算 k 对起来。

## P10417 第 K 小的和：堆的常数优化不能省掉 k 次生成

[源码](../../Exercise/binary_search/P_10417_蓝桥杯_2023_国_A_第_K_小的和.py)

我先检查了堆生成版的正确性，接着问怎么解决超时。固定 a[i] 后，同样可以把所有配对和分成有序的行，堆维护每行最小的未取项。

 当前 solution2 已经把较短数组作为行，只初始化前 min(n,k) 行，并用 heapreplace 合并弹出、补入操作。这些能减小堆和操作常数，但仍需要生成前 k 个和值；k 很大时，主要耗时仍然保留。

 文件中另有 solution1：二分阈值 x，统计 cnt(x)，求使 cnt(x)≥k 的最小整数 x。下面摘出双指针计数，省略函数开头、j=m-1 的初始化及最后的 False 返回：

```python
for value in a:
    while j >= 0 and value + b[j] > x:
        j -= 1

    if j < 0:
        break  # 后面的 a 更大，也不会有合法配对

    count += j + 1
    if count >= k:
        return True
```

a、b 排序后，随着 a 的当前值增大，合法 b 的右端 j 只会向左移动，不用为每一行重新从末尾开始。当前行能提供 j+1 个和值；累计到 k 就可以提前结束判定。

 设 h=min(n,m,k)，堆版在排序后约为 O(h+k log(h+1))；二分版每次统计 O(n+m)，总计 O((n+m)log R)，另外加上两数组排序的成本。重复和值按不同配对计入 cnt，不需要去重。

 k 较小、需要前若干个和值时，堆生成很合适；只问第 k 小且 k 很大时，二分答案能够直接跳过中间那些不必输出的和值。当前源码末尾仍调用 solution2()，要用二分版本运行还需切换入口。
