input1 = "input.1"
input2 = "input.2"
output = "output.1"

f1 = open(input1, "r")
f2 = open(input2, "r")
f3 = open(output, "w")

while True:
    r1 = f1.readline()
    r2 = f2.readline()
    if r1 == "" or r2 == "":
        break
    f3.write(r1.strip() + "\t" + r2.strip() + "\n")

f1.close()
f2.close()
f3.close()
