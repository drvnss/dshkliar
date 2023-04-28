num = int (input ())
if num < 100:
for i in range (1, num + 1):
if i % 11 == 0:
print(i)
i += 1