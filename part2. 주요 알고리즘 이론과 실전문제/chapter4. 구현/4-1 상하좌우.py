R = 1
L = -1
U = -1
D = 1
x = 1
y = 1
listA = list(map(str,input("알파벳을 입력하세요:").split()))
N = int(input("N값을 입력하세요"))

for i in listA :nz
    if i == "R":
        y += 1
        if y > N:
            y = N
    elif i == "L":
        y -= 1
        if y <= 0:
            y = 1
    elif i == "D":
        x += 1
        if x > N:
            x = N
    elif i == "U":
        x -= 1
        if x <= 0:
            x = 1
print(x, y)


# def X(i, R, L, N):
#     x = 1
#     if i == R:
#         x += 1
#         if x > N:
#             x -= 1
#     elif i == L:
#         x -= 1
#         if x < 0:
#             x += 1
#     return x
#
# def Y(i, D, U, N):
#     y = 1
#     if i == D:
#         y += 1
#         if y > N:
#             y -= 1
#     elif i == U:
#         y -= 1
#         if y < 0:
#             y += 1
#     return y


