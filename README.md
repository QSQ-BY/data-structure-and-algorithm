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

9 月 14 日的[世界冰球锦标赛与门电路练习日志](diary/Exercise/P_4799_CEOI_2015_世界冰球锦标赛_Day_2-P_13877_蓝桥杯_2023_省_Java_A_与或异或.md)记录了子集枚举的统计位置、折半搜索与二分计数，以及门电路的逐层计算。P4799 已改为回溯维护总价，日志区分了旧提交的 90 分结果和当前版本的本地验证；P13877 算得 30528。

9 月 10 日补齐了六道新题的练习日志：[回收处理、旋转九宫格、评测漏洞与宝塔](diary/Exercise/P_16276_蓝桥杯_2026_省_C_回收处理-P_10578_蓝桥杯_2024_国_A_旋转九宫格-P_16249_蓝桥杯_2026_省研究生组_评测漏洞-P_12253_蓝桥杯_2024_国_Java_B_宝塔.md)记录分界线与双堆、反向 BFS、前缀频次计数和位掩码约束搜索；[最大数字与不同的总分值](diary/Exercise/P_8801_蓝桥杯_2022_国_B_最大数字-P_12266_蓝桥杯_2024_国_Python_B_不同的总分值.md)整理 DFS 转记忆化搜索的状态定义，以及子集枚举的答案统计位置。

9 月 6 日至 7 日的[练习日志](diary/Exercise/P_1379_八数码难题-P_16251_蓝桥杯_2026_省研究生组_基态坍缩-P_16248_蓝桥杯_2026_省研究生组_2026_的出现次数-P_16270_蓝桥杯_2026_省_Java_B_组_共享单车.md)整理了八数码的整盘状态、末尾连续 1 的博弈判断、字符串匹配贪心，以及共享单车二维 DP 的状态范围。

此前的 [P1825、P2199 与 P2802 迷宫 BFS 日志](diary/Exercise/P_1825_USACO_11_OPEN_Corn_Maze_S-P_2199_最后的迷宫-P_2802_回家.md)已补全，分别记录了强制传送后的落点判重、可见位置集合的预处理，以及扣血、补给与完整状态判重的顺序。

最近的正式比赛是 AtCoder ABC474，[竞赛日志](contest/atcoder/abc474/2026-09-06_atcoder.md)与 A 到 E 的源码放在同一场次目录，重点记录最后一次操作决定顺序、正差值的权重构造，以及优惠券缺口与原价购买次数的关系。此前的 [Codeforces Round 1119（Div. 3）复盘](contest/codeforces/round_1119_Div3/2026-09-05_cf.md)保留了 C 题二分判定不单调的反例和双指针思路。

## 怎么阅读

按课程顺序学习时，可以先看 `source/basic_part` 中的基础实现，再进入 `source/improved_part`。想针对某个知识点刷题，可以直接浏览 `Exercise`。如果代码里省略了推导过程，相关背景通常能在 `diary` 或 `contest` 的复盘中找到。
