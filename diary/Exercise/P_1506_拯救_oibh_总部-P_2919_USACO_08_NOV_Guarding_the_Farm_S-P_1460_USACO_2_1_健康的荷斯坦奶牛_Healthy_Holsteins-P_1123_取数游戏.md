# 从边界灌水到选择型搜索：四道练习里的状态设计

这几天新增的题目里，有几道都是直接统计网格连通块，写法和之前的练习很接近。这篇只留下四道让我换过一次思考角度的题：P1506、P2919、P1460 和 P1123。

## P1506 拯救 oibh 总部：从边界往里灌水

题目要数的是没有被洪水淹到的 `0`。与其逐块判断一片区域有没有封闭，不如顺着洪水的来源反过来想：洪水只能从地图边界进入，所以先从所有边界 `0` 出发，把能到达的位置全部淹掉，最后留下的 `0` 就是答案。

```python
def dfs(start_x,start_y):
    stack = [(start_x,start_y)]
    g[start_x][start_y] = "#"
    while(stack):
        x,y = stack.pop()
        for (dx, dy) in directions:
            next_x = x + dx
            next_y = y + dy

            if (
                0 <= next_x < n
                and 0 <= next_y < m
                and g[next_x][next_y] == "0"
            ):
                # 入栈时就标记，避免重复入栈
                g[next_x][next_y] = "#"
                stack.append((next_x, next_y))
```

搜索必须在入栈时标记。如果等到出栈才标记，同一个格子可能被多个邻居重复放进栈里。扫描完四条边以后，用 `sum(row.count("0") for row in g)` 统计剩余格子即可，整张图只会被处理常数次，时间复杂度是 $O(nm)$。

源码中还保留了并查集写法：额外建立编号为 `n*m` 的虚拟结点，把所有边界 `0` 与它合并。两种做法虽然形式不同，实际表达的是同一件事，即哪些位置与地图外部连通。

## P2919 Guarding the Farm：山顶是一个平台

这题不能逐格判断局部最大值。若多个八方向相邻的格子高度相同，它们共同组成一个平台；只要整个平台旁边出现一个更高的格子，这个平台就不算山顶。

我的做法是从一个未访问格子出发，只扩展到等高邻居，同时用 `is_peak` 记录整个平台是否遇到过更高位置。搜索结束后再决定是否给答案加一。这里容易混淆的是状态归属：`vis` 属于格子，`is_peak` 属于当前连通块。每个格子只进入一次栈，复杂度同样是 $O(nm)$。

## P1460 健康的荷斯坦奶牛：让枚举顺序承担答案要求

这题既要求饲料种数最少，又要求相同种数中字典序最小。我没有搜完所有子集再排序，而是从选择一种饲料开始逐渐增加目标数量；在固定数量内，饲料编号始终从小到大枚举。

```python
def dfs(pos: int, start: int, target_count: int) -> bool:
    if pos == target_count:
        if check(target_count):
            print(target_count, *selected[:target_count])
            return True
        return False

    for feed_number in range(start, feed_count + 1):
        selected[pos] = feed_number
        if dfs(pos + 1, feed_number + 1, target_count):
            return True
    return False


for count in range(1, feed_count + 1):
    if dfs(0, 1, count):
        break
```

`target_count` 控制当前只枚举多大的组合，`start` 保证编号严格递增，因此不会生成重复集合。外层第一次找到解时，种数一定最少；内层 DFS 第一次成功时，所选编号也一定是当前长度中字典序最小的。搜索顺序本身已经包含了题目的优先级。

## P1123 取数游戏：封锁次数不能只记真假

这题要求选出的任意两个数字在八方向上都不相邻。我最初选中一个格子后，用布尔值把周围格子标成不可选，但一个格子可能同时受到多个已选格子的影响。撤销其中一次选择时直接改回 `False`，会把仍然有效的另一层封锁也清掉。

后来我把标记改成封锁次数，并用 `pos` 固定搜索顺序：

```python
if(ban[x][y] == 0):
    changed = []
    for dx in (-1,0,1):
        for dy in (-1,0,1):
            nx = x+dx
            ny = y + dy
            if(0<=nx<n and 0<=ny<m):
                ban[nx][ny] += 1
                changed.append((nx,ny))
    dfs2(pos + 1,result + g[x][y])
    for (dx,dy) in changed:
        ban[dx][dy] -= 1
dfs2(pos+1,result)
```

每个位置依次尝试取或不取，下一层始终处理 `pos+1`，所以不会再按不同选择顺序反复生成同一方案。`ban` 的加减成对出现，重叠区域在撤销一次后仍会保留剩余计数。

我还把矩阵按这个顺序展开成一维数组，并计算后缀和。`result + suffix[pos]` 假设后面的数全部可以取，是一个偏大的上界；如果它仍然不超过当前答案，就可以直接结束这一支。这个上界不算紧，但判断是安全的。

P1123 的样例输出为 `271、172、99`。前面的调试也让我重新确认了一件事：回溯数组不能只描述“现在能不能走”，还得保存足够的信息，让递归返回时准确还原上一层。

这四道题写完后，我对搜索状态的检查顺序更明确了。先写清楚递归参数代表什么，再确认状态在哪里改变、怎样恢复，最后才考虑剪枝。
