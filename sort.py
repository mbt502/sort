begin = open('begin.txt','r')# чтение файла и запись в список
s = begin.read().split()
begin.close()


a,b,c,d,e = [],[],[],[],[]


for i in s:# первоначальная сортировка на слова, цифры и слова со знаками
    if i.isdigit() and not(i.isalpha()):
        a.append(i)    
    elif i.isalpha() and not(i.isdigit()):
        b.append(i)
    else:
        d.append(i)
s.clear()


for i in d:# удаление знаков и формирование двойного списка слов
    for j in range(len(i)):
        if not(i[j].isalnum()):
            i = i.replace(i[j],' ')
    c.append(i.split())
d.clear()


for i in c:# разбиение двойного списка на два одинарных
    for j in i:
        if len(i)>1:
            d.append(j)
        else:
            e.append(j)
c.clear()


for j in d,e:# сортировка оставшихся элементов
    for i in j:
        if i.isdigit() and not(i.isalpha()):
            a.append(i)    
        elif i.isalpha() and not(i.isdigit()):
            b.append(i)
        else:
            c.append(i)
d.clear()
e.clear()


a.sort()# сортировка в порядке возрастания по первому символу
b.sort()
c.sort()


res = open('begin.txt','a')#запись в файл
res.write('\n')
res.write('\n')
for i in a,b,c:
    for j in i:
        res.write(j)
        res.write('\n')
    res.write('\n')
res.close()
