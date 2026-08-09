# 数据结构与算法学习记录

这个仓库记录了我从零开始学习数据结构与算法的过程。

`source` 保存课程主线的基础实现与配套练习，`Exercise` 按知识点收录额外的洛谷日练，`contest/codeforces` 单独保存比赛代码和复盘。`diary` 记录每天学了什么、卡在哪里，以及后来是怎么想明白的。

这里不只收集最后能够运行的代码。我更想保留学习过程中那些逐渐连起来的线索：顺序表为什么要区分容量和元素个数，链表题为什么总是在找指针关系，括号匹配如何把栈从一个结构体变成一种思考方式，递归又是怎么在二叉树里真正派上用场的。

## 目前写到哪里

截至 2026-08-09，仓库里已经有这些内容：

| 章节 | 核心内容 | 练习方向 |
| --- | --- | --- |
| 顺序表 | 动态数组、增删改查 | 二分、滑动窗口、前缀和 |
| 前缀和与差分 | 一维与二维前缀和、区间差分 | 区间查询、区间修改、二分答案 |
| 链表 | 单链表、循环链表、双向链表 | 反转、删除、判环、旋转 |
| 递归函数 | 递归出口、回溯框架 | 排列、组合、子集 |
| 栈与队列 | 数组栈、循环队列、链表队列 | 括号、表达式、栈序列 |
| 二叉树 | 遍历、线索化、序列化、哈夫曼编码 | 层序遍历与树题 |
| 堆与优先队列 | 建堆、堆排序、优先队列 | 数据流、合并与贪心维护 |
| 排序算法 | 八类经典排序、`std::sort` | 归并、逆序对、贪心排序 |
| 查找算法 | 二分、跳跃表、哈希表、布隆过滤器 | 判重、区间查找、答案二分 |
| 平衡树 | BST、AVL、红黑树、B 树 | 插入、旋转、分裂与合并 |
| 递归转非递归 | 系统栈模拟、状态码、拓扑顺序 | 遍历、排序与路径问题 |
| 森林与并查集 | 路径压缩、按大小合并、带权关系 | 连通块、关系约束与离散化 |
| 单调栈与单调队列 | 最近元素、定长与变长窗口 | 窗口最值、最大子序列和、最大矩形 |
| 回溯算法 | DFS、状态树、剪枝、迭代加深 | 路径搜索、字串变换、位掩码状态压缩 |

单调栈与单调队列的基础实现和八道练习已经完成。最后三题分别用单调栈模拟接雨水、用前缀和与单调队列寻找最短子数组，并从单调结构的形成过程判断双生序列。

回溯算法的十一道主线练习也已经完成，从 N 皇后、迷宫路径到单词接龙、字串变换和双脑分配，分别练习了访问标记、状态压缩、剪枝和迭代加深。当前先暂停向下推进，集中复习这十一道题，尤其是位掩码与 lowbit 的状态变化。

从 2026-08-03 起，除 Codeforces 比赛日外，每天至少完成两道洛谷额外练习，统一收录到 `Exercise`。8 月 3 日完成了 P1102 和 P1918，8 月 4 日完成了 P5250 和 P5266，8 月 6 日又写了「小梦的 AB 交换」与 B3612「求区间和」。

8 月 9 日没有继续向后推进课程，而是集中补齐了一维前缀和、二维前缀和与差分数组，并用多道区间查询、区间修改题巩固。当天还补完了蓝桥杯 2026 省赛 A 组 E 题，参加了 Codeforces Round 1116（Div. 2），赛后继续整理了 B、C 两题。

## 目录结构

```text
.
├─ source
│  ├─ basic_part
│  │  ├─ vector / linked list / recursive_function
│  │  ├─ stack&queue / binary_tree / heap&priority_queue
│  │  ├─ sort_algorithm / lookup_algorithm / balanced_tree
│  │  └─ recursion_to_non-recursion / Forest&disjoint_set_union
│  └─ improved_part
│     ├─ monotonic_queue&stack
│     └─ backtrack_algorithm
├─ Exercise
│  ├─ hash
│  │  ├─ lg_p1102_A-B.cpp
│  │  ├─ lg_p1918.cpp
│  │  ├─ lg_p5250.cpp
│  │  └─ lg_p5266.cpp
│  └─ prefix&difference
│     ├─ lg_b3612.cpp
│     ├─ lg_b3693.cpp
│     ├─ lg_cf816b.cpp
│     ├─ lg_p3131.cpp
│     └─ lg_u535928.cpp
├─ contest
│  ├─ blue_bridge
│  └─ codeforces
│     ├─ round_1109_Div3
│     └─ round_1116_Div2
├─ python
├─ diary
│  ├─ vector_linklist_recursive_func
│  ├─ stack_queue
│  ├─ binary_tree
│  ├─ heap&priority_queue
│  ├─ sort_algorithm
│  ├─ lookup_algorithm
│  ├─ balanced_tree
│  ├─ recursion_to_non_recursion
│  ├─ forest&disjoint_set_union
│  ├─ monotonic_queue&stack
│  └─ backtrack_algorithm
└─ .build
```

每个章节的源码大致分成两类：

- `basic_definition&operation`：自己实现基础结构，并保留可单独运行的入口。
- `exercise`：围绕当前章节完成的练习题。
- 根目录下的 `Exercise`：课程主线之外的洛谷日练，按知识点分类。

## 怎么阅读这个仓库

如果想看课程主线，可以先读 `source` 中对应章节的基础实现，再看 `exercise` 里的配套题目；额外练习则放在根目录的 `Exercise` 中。

学习日志按日期放在 `diary`，记录从跟着课程实现到独立重写、整理思路的过程。

### 精选日志

- 起步：[顺序表、链表与递归函数](diary/vector_linklist_recursive_func/2026-05-10_to_05-20.md)
- 建模：[表达式计算：把表达式看成一棵树](diary/stack_queue/2026-05-26.md)
- 优化：[重写建堆，再用堆优化哈夫曼编码](diary/heap&priority_queue/2026-06-11.md)
- 复杂结构：[B 树，最难的是让每一个下标对齐](diary/balanced_tree/2026-07-29.md)
- 思维转换：[递归落到栈里，也第一次走进 Codeforces](diary/recursion_to_non_recursion/2026-07-30.md)
- 模板沉淀：[把并查集从现场手搓变成两套模板](diary/forest&disjoint_set_union/2026-08-01.md)
- 当前进度：[从最近元素到窗口最值](diary/monotonic_queue&stack/2026-08-01_to_08-03.md)
- 查找复习：[map 理顺以后，哈希查找也顺了](diary/lookup_algorithm/2026-08-04.md)
- 章节交接：[单调结构收尾，回溯从八皇后开始](diary/backtrack_algorithm/2026-08-06.md)
- 回溯收尾：[比赛、真题与回溯收尾](diary/backtrack_algorithm/2026-08-07_to_2026-08-08.md)
- 知识补漏：[补上前缀和与差分，再打一场 Div. 2](diary/backtrack_algorithm/2026-08-09.md)

比赛过程单独记录在 [Codeforces Round 1109（Div. 3）复盘](contest/codeforces/round_1109_Div3/2026-07-30_cf.md) 和 [Codeforces Round 1116（Div. 2）复盘](contest/codeforces/round_1116_Div2/2026-08-09_cf.md) 中。

## 本地运行

仓库里的代码以 C/C++ 基础练习为主，多数文件可以单独编译。部分代码使用了 `nullptr` 和 `and`，建议使用 `g++`。

## 关于更新

这个仓库会跟着学习进度继续长下去。写代码、做题、复盘，再回头重写一遍不够熟练的部分，是目前最适合我的节奏。
