truck_weights = [7, 4, 5, 6]

list = [[k,0] for k in truck_weights]
len_truck_weights = len(truck_weights)
# bridge_on = [[4, 2], [5, 1]]
bridge_length = 3
weight = 10
current_weight = 0
time = 1

list[0][1] = 1
current_weight += list[0][0]
for j in range(10):
    time += 1
    for i in list[:bridge_length]:
        if current_weight + i[0] > weight:
            pass
        else:
            i[1] += 1
            current_weight += i[0]

        if i[1] > 0:
            i[1] += 1

        if i[1] == bridge_length + 1:
            current_weight -= i[0]
            list.remove(i)

        print('time:',time,'list:',list,'current_weight:',current_weight)



# for i in bridge_on[::-1]:
#     if i[1] == bridge_length:
#         arrive.append(i[0])
#         bridge_on.remove(i)
#         current_weight -= i[0]
#     i[1] += 1
#     print(bridge_on)

    #     arrive.append(i[0])
    #     bridge_on.remove(i)
    #     current_weight -= i[0]
    # i[1] += 1
    # print("bridge_on:",bridge_on)

