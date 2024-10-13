for i in range(5):
    print('Python')

for i in 'Python':
    print(i)

lst1 = ['1', '2', '3', '4', '5']
lst2 = ['a', 'b', 'c', 'd', 'e']
for i in lst1:
    for j in lst2:
        print(i + j)



a = 1
while a < 5:
    print('условие верно')
    a = a + 1
    else:
    print('условие неверно')

a = 1
while a < 5:
    a += 1
    if a == 3:
        continue
    print(a)  # 2, 4, 5