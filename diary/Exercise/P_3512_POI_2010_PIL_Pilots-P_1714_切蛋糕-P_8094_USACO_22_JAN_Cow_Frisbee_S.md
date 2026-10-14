# 单调队列里的候选与单调栈里的遮挡

## P3512 PIL Pilots：从二分窗口长度改成一次扫描

[源码](../../Exercise/monotonic_queue&stack/P_3512_POI_2010_PIL_Pilots.py)

我在对话里先检查了二分加单调队列的写法，后来又问了如何使用双指针，并把 Python 版本写进 solution2。

 可变窗口仍用两个队列维护最大、最小值。右端加入元素后，如果极差超过 k，就持续右移左端，直到窗口重新合法。下面省略加入新元素时对队尾的维护，保留收缩窗口和更新答案的部分：

```python
# 极差超过 k 时，移动左端点直到窗口合法
while arr[qmax[0]] - arr[qmin[0]] > k:
    left += 1
    while qmax and qmax[0] < left:
        qmax.popleft()
    while qmin and qmin[0] < left:
        qmin.popleft()

ans = max(ans, right - left + 1)
```

如果某个左端点已经因为极差过大而失效，右端继续扩展也不会使极差变小，它以后不用再尝试。因此左指针只向右走，就能对每个右端点找到最长合法窗口。

 每个下标在两个单调队列中都最多入队、出队一次，总时间 O(n)，省去了二分版 O(log n) 次的重复扫描，空间上界为 O(n)。另外，二分的 check(L) 必须真的形成长度为 L 的窗口后才能判断；窗口还不够长时的极差没有回答原来的判定问题。

## P1714 切蛋糕：队列维护的是前缀和，不是原数组的最小值

[源码](../../Exercise/monotonic_queue&stack/P_1714_切蛋糕.py)

有了前缀和，固定右端点 r 后，区间和就是 prefix[r]-prefix[j]。长度在 1 到 m 之间，意味着 max(0,r-m)≤j≤r-1，因此只需找这一范围内最小的前缀和。

 当前代码的核心循环如下：

```python
q = deque([0])
ans = arr[0]
for right in range(1,n+1):
    while q and q[0]< right - m:
        q.popleft()
    ans = max(ans,prefix[right] - prefix[q[0]])
    while q and prefix[q[-1]] >= prefix[right]:
        q.pop()
    q.append(right)
```

先移除过期下标，再计算答案，最后把当前前缀和加入候选。这个顺序保证 j<r，不会把空区间算成收益 0；答案初始化为 arr[0]，也保留了全负数时必须选非空区间的要求。

 新前缀和更小、位置又更靠后时，旧候选既不更优、也不更晚过期，可以从队尾删除。时间 O(n)，前缀和及队列空间 O(n)。

## P8094 Cow Frisbee：按较矮的端点寻找最近的更高者

[源码](../../Exercise/monotonic_queue&stack/P_8094_USACO_22_JAN_Cow_Frisbee_S.py)

飞盘能在两头之间传递，要求中间所有牛都比两头矮。固定较矮的端点后，朝一个方向能与它配对的更高端点，只能是最近的那头；若还向外找，眼前这头更高的牛就会挡住它。

 源码分别从左向右、从右向左维护单调栈。这里摘出左侧扫描：

```python
# 找左边最近的、更高的牛
for i in range(n):
    while stack and arr[stack[-1]] < arr[i]:
        stack.pop()

    if stack:
        ans += i - stack[-1] + 1
    stack.append(i)
```

当前牛会淘汰栈顶比自己矮的候选，剩下的栈顶就是左边最近的更高牛，贡献是两端距离加 1。反向扫描处理更高端点在右侧的情况。在题目身高互不相同的前提下，每对合法端点由较矮一端统计一次，不会两边重复计算。

 两趟扫描中，每个位置最多各入栈、出栈一次，时间 O(n)，辅助空间 O(n)。这里找“最近”由遮挡条件决定，不能直接把栈里所有更高的牛都加进答案。
