d = dict(line.split() for line in open("input.txt"))
a, b = float(d["a"]), float(d["b"])

result_sum = a + b
print(result_sum)