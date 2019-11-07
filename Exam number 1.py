#*, /, +, -, %, //


s=10
for i in range(0, 3):
    for j in range(i, 3):
        s += (i - j)

print(s)