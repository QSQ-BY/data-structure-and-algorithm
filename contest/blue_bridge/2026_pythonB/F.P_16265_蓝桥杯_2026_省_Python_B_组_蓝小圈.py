""" 题目描述
手机屏幕幽幽地亮起，“蓝小圈”社交平台的图标微微闪动。小蓝作为该平台的后端架构师，正盯着流量监控面板上不断跳动的数据。

为了提升用户粘性，平台产品经理提出了全新的“圈层互动”功能。系统中共有 N 个用户结点，初始时，每位用户的“活跃度”均为 0，且彼此之间处于陌生人状态，没有任何社交关联。

随着产品功能的上线，后台日志将按顺序记录 Q 条用户行为指令。这些指令如下：

建立好友：用户 X 与用户 Y 相互关注，双方所在的社交圈正式连通。若两者已处于同一社交圈，则忽略此操作。
发布个人动态：用户 X 发布了一条个人动态，其个人活跃度提升 A 个单位。
圈层热议：用户 X 发起了一个热门话题，该话题产生极强的辐射效应，使得所有与 X 处于同一社交圈（即通过好友关系可直接或间接连通）的用户，其活跃度同步追加 A 个单位。
数据查询：运营团队请求获取用户 X 当前的活跃度数，用于分析用户质量。
随着用户量激增，高频的社交互动请求让服务器核心计算模块面临巨大压力。作为小蓝的协助者，请你接管日志处理单元，并按顺序输出所有的查询结果。

输入格式
第一行包含两个正整数 N 和 Q，分别代表平台用户总数与行为日志的总条数。

随后 Q 行，每行描述一条具体的行为指令，格式遵循以下四种类型之一：

1 X Y: 执行“建立好友”，连通用户 X 与 Y 的社交圈。
2 X A: 执行“个人动态”，为用户 X 的活跃度增加 A。
3 X A: 执行“圈层热议”，为 X 所在社交圈内的所有用户活跃度增加 A。
4 X: 执行“数据查询”，查询用户 X 的当前活跃度。
输出格式
针对每一条“数据查询”指令，输出单独的一行整数，代表目标用户当前的活跃度数值。

输入输出样例
输入 #1复制

3 6
1 1 2
1 1 3
2 1 5
3 2 5
4 1
4 2
输出 #1复制

10
5
说明/提示
【评测用例规模与约定】
对于 30% 的评测用例，1≤N≤1000，1≤Q≤1000。

对于所有评测用例，1≤N≤2×10 
5
 ，1≤Q≤2×10 
5
 ，1≤X,Y≤N，1≤A≤10 
9
 。保证测试数据中至少包含一条类型为 4 的“数据查询”指令。 """
import sys
input = sys.stdin.buffer.readline
def read():
    return map(int,input().split())
class UnionSet:
    def __init__(self,n):
        self.collections_count = n
        self.elements_count = n
        self.size = [1]*n
        self.father = [i for i in range(n)]
        self.activity = [0]*n#记录每个节点单独获得的值
        self.tag = [0]*n #根节点记录集合统一增加的值
        self.delta = [0]*n #到父节点的补偿值

    def find(self,x:int):
        if(self.father[x] != x):
            father_x = self.father[x]
            self.father[x] = self.find(father_x)
            self.delta[x] += self.delta[father_x]
        return self.father[x]

    def merge(self,a:int,b:int)->bool:
        root_a = self.find(a)
        root_b = self.find(b)
        if(root_a == root_b):
            return False
        if(self.size[root_a] > self.size[root_b]):
            root_a,root_b = root_b,root_a
        self.father[root_a] = root_b
        self.delta[root_a] = self.tag[root_a] - self.tag[root_b]
        self.size[root_b] += self.size[root_a]
        self.collections_count -= 1
        return True

    def improve_all_activity(self,x:int,improvement:int):
        root_x =self.find(x)
        self.tag[root_x] += improvement

    def improve_activity(self,x:int,improvement:int):
        self.activity[x] += improvement

    def get_activity(self,x:int):
        root_x = self.find(x)
        return self.activity[x] + self.delta[x] + self.tag[root_x]

N,Q = read()
u = UnionSet(N+1)
while Q:
    arr = list(read())
    match arr[0]:
        case 1:
            u.merge(arr[1],arr[2])
        case 2:
            u.improve_activity(arr[1],arr[2])
        case 3:
            u.improve_all_activity(arr[1],arr[2])
        case 4:
            print(u.get_activity(arr[1]))
    Q -= 1
