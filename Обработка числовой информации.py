f = open('17-257.txt')
# считать список всех чисел
a = list(map(int, f.readlines()))
# найдем минимальное и максимальное нечетное значение.
maxE = 0
minE = 10 ** 10
for i in a:
    if i % 2!= 0:
        minE = min(minE, i)
        maxE = max(maxE, i)

minsum = 10 ** 10
cnt = 0
# по всем элементам, кроме последнего и буду рассматривать элементы a[i] + 1
for i in range(len(a) - 1):
    # два последовательных идущих элементов. Кол-во пар ищу и она больше сумма нечетных макасимального и минимального элемента
    if (a[i] + a[i + 1]) % 2 == 0 and a[i] + a[i + 1] > minE + maxE:
        cnt += 1
        # ищу минимальный элемент
        if a[i] + a[i + 1] < minsum:
            minsum = a[i] + a[i + 1]
print(cnt, minsum)

# 2
f = open('17-257.txt')
# считать список всех чисел
a = list(map(int, f.readlines()))

cnt17 = cnt11 = 0
min11 = 10 ** 10
max17 = 0

for i in a:
    if i % 11 == 0:
        cnt11 += 1
        # минимальный кратный 11 и максимальный кратный 17 найти нужно
        # минимальный кратный 11, если вдруг окажется минимальный кратный 11 меньше, то в ответ записываем, а возможно и i меньше
        min11 = min(min11, i)
    if i % 17 == 0:
        cnt17 += 1
        min17 = max(max17, i)
# кол-во кратных 11 оказывается больше чем кол-во кратных 17
if cnt11 > cnt17:
    print(cnt11, min11)
else:
    print(cnt17, max17)
# print(cnt11, cnt17) 17 and 56

# 3
# a[i] a[i + 1] a[i + 2] - кол-во троек
f = open('17-1.txt')
# считать список всех чисел
a = list(map(int, f.readlines()))
# среднее арифметическое
sa = sum(a)/len(a)
cnt = 0
maxsum = 0
# print(sa) -105.6732
for i in range(len(a)-2):
    # хотя-бы из этой элемент из тройки должен быть меньше чем среднее арифметическое
    # одновременно с этим, один из элементов троек должна содержать цифру 8
    if (a[i] < sa or a[i + 1] < sa or a[i + 2] < sa) and \
            (('8' in str(a[i])) or ('8' in str(a[i + 1])) or ('8' in str(a[i+2]))):
        cnt += 1
        if a[i] + a[i+1] + a[i+2] > maxsum:
            maxsum = a[i] + a[i+1] + a[i+2]
print(cnt, maxsum)