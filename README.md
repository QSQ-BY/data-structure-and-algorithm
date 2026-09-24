# 数据结构与算法学习记录

这是我学习数据结构与算法时使用的代码仓库。内容最初以 C/C++ 为主，现在已经逐步转向 Python。

这里的源码既有数据结构与算法的手写实现，也有围绕同一知识点完成的练习。写出能运行的代码只是第一步；遇到边界处理、状态定义或复杂度问题时，我会继续修改原来的实现，并把当时的错误和重写原因记下来。这样再次复习时，看到的不只是答案，还能找到思路是从哪里转过来的。

仓库把课程主线和独立练习分开整理。`source` 按学习顺序保存基础实现与进阶专题，`Exercise` 用来集中收录课程之外的题目。比赛中的代码、赛后补题和复盘放在 `contest`，`diary` 记录每天的代码总结。

## 目录结构

```text
.
├─ source/
│  ├─ basic_part/
│  └─ improved_part/
├─ Exercise/
├─ contest/
│  ├─ atcoder/
│  ├─ blue_bridge/
│  ├─ codeforces/
│  └─ 牛客/
└─ diary/
```

- [`source/basic_part`](source/basic_part) 保存基础部分的实现。这里更关注数据结构本身，包括接口、基本操作、边界处理和配套练习。
- [`source/improved_part`](source/improved_part) 保存进阶专题。内容更偏向解题方法、状态设计、算法组合和优化。
- [`Exercise`](Exercise) 收录课程主线之外的练习，按知识点分类，方便集中复习同一类题目。
- [`contest`](contest) 按比赛平台和场次整理代码。赛后补题与复盘也放在对应场次中，不混入 README。
- [`diary`](diary) 按学习主题整理日志。日期只用于定位记录，具体的学习进度、卡点和理解变化都留在这里。

## 学习章节

| 编号 | 章节 | 主要内容 |
|---:|---|---|
| 1 | [顺序表](source/basic_part/1.vector) | Vector 基本操作、数组处理、前缀和与差分 |
| 2 | [链表](source/basic_part/2.linked%20list) | 链表实现、循环链表、反转、旋转与删除 |
| 3 | [递归函数](source/basic_part/3.recursive_function) | 阶乘、组合、排列与子集生成 |
| 4 | [栈与队列](source/basic_part/4.stack&queue) | 基本实现、表达式计算、括号匹配与循环队列 |
| 5 | [二叉树](source/basic_part/5.binary_tree) | 遍历、线索化、序列化、重建与 Huffman 编码 |
| 6 | [堆与优先队列](source/basic_part/6.heap&priority_queue) | 建堆、堆排序、优先队列及合并、排名、中位数问题 |
| 7 | [排序算法](source/basic_part/7.sort_algorithm) | 基础排序、归并、快速、基数排序及相关应用 |
| 8 | [查找算法](source/basic_part/8.lookup_algorithm) | 二分、跳表、哈希表、布隆过滤器与映射 |
| 9 | [平衡树](source/basic_part/9.balanced_tree) | 二叉搜索树、AVL、红黑树与 B 树 |
| 10 | [递归转非递归](source/basic_part/10.recursion_to_non-recursion) | 显式栈模拟递归与拓扑排序 |
| 11 | [森林与并查集](source/improved_part/11.Forest&disjoint_set_union) | Quick Find、Quick Union、加权合并与连通性问题 |
| 12 | [单调队列与单调栈](source/improved_part/12.monotonic_queue&stack) | 滑动窗口、区间最值、柱状图、接雨水与子数组问题 |
| 13 | [回溯算法](source/improved_part/13.backtrack_algorithm) | 搜索状态、路径恢复、剪枝与排列组合问题 |
| 14 | [贪心算法](source/improved_part/14.greedy_algorithm) | 局部选择、排序贪心、区间与任务安排 |
| 15 | [动态规划](source/improved_part/15.dynamic_programming) | 递推建模、经典 DP、背包与序列模型及状态优化 |

## 练习与竞赛

[`Exercise`](Exercise) 是课程之外的分类刷题区，只保存按主要知识点归档的题目代码。课程主线暂停后，值得复盘的练习日志统一放进 [`diary/Exercise`](diary/Exercise)，用题号而不是日期命名，如果想看具体某一道题的解题思路可以直接在该文件夹里面搜索对应的题号。

[`contest`](contest) 按平台和场次保存正式比赛代码、赛后补题与复盘。它和 `Exercise` 都不计入上面的课程章节编号。

最近的练习记录：[奇怪的地图：从移动方向推导距离和排序依据](diary/Exercise/P_16293_蓝桥杯_2026_省_Java_A_组_奇怪的地图.md)（2026-09-24），记录了六边形网格距离的下界与路径构造、`x-y` 与 `x+y` 的区别，以及 Python `lambda` 排序和极差扫描的性能差异。

9 月 24 日还补记了 9 月 22 日遗漏的练习：[纯职业小组、底层协议与研发资源分配](diary/Exercise/P_11006_蓝桥杯_2024_省_Python_B_纯职业小组-P_16299_蓝桥杯_2026_省_Python_C_组_底层协议-P_12161_蓝桥杯_2025_省_Java_B_研发资源分配.md)整理最大失败规模、互补余数和排列循环；[项链排列与乘积最大](diary/Exercise/P_12834_蓝桥杯_2025_国_B_项链排列-P_8669_蓝桥杯_2018_省_B_乘积最大.md)记录连续段构造和符号交换；[水质检测、灯塔与三国游戏](diary/Exercise/P_12135_蓝桥杯_2025_省_B_水质检测-P_15433_蓝桥杯_2025_国_Python_B_灯塔-P_13887_蓝桥杯_2023_省_Python_A_三国游戏.md)分别讨论连通状态、操作顺序和事件贡献。

## 怎么阅读

按课程顺序学习时，可以先看 `source/basic_part` 中的基础实现，再进入 `source/improved_part`。想针对某个知识点刷题，可以直接浏览 `Exercise`。如果代码里省略了推导过程，相关背景通常能在 `diary` 或 `contest` 的复盘中找到。
