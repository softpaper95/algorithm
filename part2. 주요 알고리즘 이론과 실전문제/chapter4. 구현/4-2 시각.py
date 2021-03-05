count = 0
hours = int(input("시간을 입력하세요:"))
for hour in range(hours+1):
    for minute in range(60):
        for second in range(60):
            if "3" in str(hour)+str(minute)+str(second):
                count += 1
print(count)