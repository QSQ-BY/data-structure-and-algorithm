# 子集型枚举
import sys

input = sys.stdin.buffer.readline


def read():
    return map(int, input().split())


vitamin_count = int(input())
require = list(read())
feed_count = int(input())
feeds = [[0] * vitamin_count]
feeds.extend(list(read()) for _ in range(feed_count))
selected = [0] * feed_count


def check(count: int) -> bool:
    vitamin_sum = [0] * vitamin_count
    for index in range(count):
        feed_number = selected[index]
        for vitamin in range(vitamin_count):
            vitamin_sum[vitamin] += feeds[feed_number][vitamin]
    return all(
        vitamin_sum[vitamin] >= require[vitamin]
        for vitamin in range(vitamin_count)
    )


# 当前枚举的位置、当前可枚举的最小编号、目标饲料数量
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
