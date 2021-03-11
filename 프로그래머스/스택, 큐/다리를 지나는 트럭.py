truck_weights = [10]
len_truck_weights = len(truck_weights)
bridge_on = []
bridge_length = 100
weight = 100
current_weight = 0
arrive = []

#처음 아무것도 없을때 입
bridge_on.append([truck_weights[0],1])
current_weight += truck_weights[0]
truck_weights.remove(truck_weights[0])
answer = 1

while truck_weights:
    answer +=1
    for i in bridge_on[::-1]:
        if i[1] == bridge_length:
            arrive.append(i[0])
            bridge_on.remove(i)
            current_weight -= i[0]
        i[1] += 1

    if current_weight + truck_weights[0] <= weight:
        bridge_on.append([truck_weights[0],1])
        current_weight += truck_weights[0]
        truck_weights.remove(truck_weights[0])
    # print('answer:', answer, 'bridge_on', bridge_on, 'truck_weights', truck_weights, 'current_weight', current_weight,
    #       'arrive', arrive)
while bridge_on:
    answer += 1
    for i in bridge_on[::-1]:
        if i[1] == bridge_length:
            arrive.append(i[0])
            bridge_on.remove(i)
            current_weight -= i[0]
        i[1] += 1
print(answer)


# print('answer:',answer,'bridge_on',bridge_on,'truck_weights',truck_weights,'current_weight',current_weight,'arrive',arrive)

# 다른사람풀이 + 내풀이
def solution(bridge_length, weight, truck_weights):
    current_weight = 0
    bridge_on = [0] * bridge_length
    sec = 0
    while bridge_on:
        sec += 1
        if bridge_on[0] > 0:
            current_weight -= bridge_on[0]
            bridge_on.pop(0)
        else:
            bridge_on.pop(0)

        if truck_weights:
            if current_weight + truck_weights[0] <= weight:
                bridge_on.append(truck_weights.pop(0))
                current_weight += bridge_on[-1]
            else:
                bridge_on.append(0)
    return sec