from random import randint
from random import choice
def createRandomList(size):
    list = []
    for i in range(size):
        value = choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") + str(randint(100, 999))
        lista.append(value)
    return list, max(list), min(list)
siz = 100
li, maxli, minli = createRandomList(siz)

end = 100
while end > 1:
    changed = False
    x = 0
    while x <(end - 1):
        if li[x] > li[x + 1]:
            changed = True
            var_temp = li[x]
            li[x] = li[x + 1]
            li[x + 1] = var_temp
        x = x + 1
    if not changed:
        break
    end = end - 1

for element in li:
    print(element)
