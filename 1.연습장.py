from collections import Counter
clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
kind_of_clothes = Counter([clothe for _ , clothe in clothes])
# cases = 1
# kind_of_clothes = Counter([clothe for _ , clothe in clothes])
# for value in kind_of_clothes.values():
#     cases *= value +1
# result = cases -1


# for key in kind_of_clothes:
#     print(key)

# print(counter_each_category)
# clothes_sort = sorted(clothes, key=lambda x: x[1])
# print(clothes_sort)
# sum = 1
# count = 1
#
# for x,y in zip(clothes_sort, clothes_sort[1:]):
#     if x[1] == y[1]:
#         count +=1
#     else:
#         sum *= count+1
#         count = 1
# sum = sum * (count+1) -1
# print(sum)

# for i in range(0, len(clothes)-1):
#     if clothes_sort[i][1] == clothes_sort[i+1][1]:
#         print("같음",clothes_sort[i][1],clothes_sort[i+1][1])
#         count += 1
#         print('count', count)
#     else:
#
#         sum *= count+1
#         print("다름", clothes_sort[i][1], "count",count,"sum",sum)
#         count = 1
# sum = sum - 1
# print(sum)



# sum = 1
# count = 1
#
# for i in range(0, len(clothes)-1):
#     if clothes_sort[i][1] == clothes_sort[i+1][1]:
#         count += 1
#     else:
#         sum *= count
#         count =1
# sum = sum * count
# print(clothes_sort)