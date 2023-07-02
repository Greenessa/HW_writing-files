# Домашнее задание по записи в файл и чтению из файла.
lst = ["1.txt", "2.txt", "3.txt"]
lst_len = []
for file in lst:
    with open(file, encoding = 'cp1251') as f:
        l = len(f.readlines())
        lst_len.append(l)
        print(lst_len)
new_t = zip(lst, lst_len)
lst_new = sorted(new_t,key = lambda x: x[1])
print(lst_new)
with open('4.txt', 'a', encoding = 'cp1251') as f1:
    for name, lengh in lst_new:
        f1.write(name + "\n")
        f1.write(str(lengh) + "\n")
        with open(name, encoding = 'cp1251') as f:
            f1.write(f.read() + "\n")
