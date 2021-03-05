data = [1, 2, 3, 2, 5]
m = 5
n = 5
start = 0
end = 0
count = 0
interval_sum = 0

# 고려해야 하는 사항들
# 1. interval_sum > m 일때
# 2. interval_sum < m 일때
# 3. interval_sum == m 일때


while end < n and start < n:
    if interval_sum > m :
        print("전 start", start)
        interval_sum -= data[start]
        start += 1
        print("후 start", start, "interver_sum", interval_sum)

    elif interval_sum < m :
        print("end",end)
        interval_sum += data[end]
        end += 1
        print("interval_sum < m",interval_sum)
    elif interval_sum == m:
        print("전 interval_sum", interval_sum, "data[start]", data[start])
        count += 1
        interval_sum -= data[start]
        print("후 interval_sum", interval_sum, "data[start]", data[start], "count",  count)

print("count", count)