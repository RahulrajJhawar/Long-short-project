n = int(input('number of inputs you want: '))

data = []

i = 0         #use for loop
while i < n:
    m = input('enter long or short: ')
    i = i+1
    data.append(m)


longcount = data.count('long')
shortcount = data.count('short')     #try to do without.count,don't use a list

print(" Number of long commands =" + str(longcount))
print("Number of short commands = " + str(shortcount))


# for i in range(n):
#     inp = input('enter bs')
#     if inp == "long":
#         longcount += 1
#     else if inp == "short":
#         shortcount += 1
#
# print both





