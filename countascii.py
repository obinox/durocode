from itertools import groupby


with open('durocode/duroasciiart.txt','r') as d:
    dl = d.read()
dsyl = list(set(list(dl)))
ddict: dict = {}
for s in dsyl:
    ddict[s] = ord(s), dl.count(s)
print(ddict)

dhex = [ord(x) for x in list(dl)]
dhexgroup = [list(g) for _, g in groupby(dhex)]
with open('durocode/duroasciicode.txt','w') as d:
    d.write('\n'.join([f'{len(x)} {x[0]}' for x in dhexgroup]))

with open('durocode/duroasciicode.txt', 'r') as d:
    dlines = d.readlines()

with open('durocode/counterr.txt', 'r') as c:
    cr = [r.replace("\n", "") for r in c.readlines()]
with open('durocode/counterl.txt', 'r') as c:
    cl = [r.replace("\n", "") for r in c.readlines()]

tex = [0, 0, 10, {42, 43, 44, 45}, 0, 0, {32, 33, 35, 36}, {58, 59}, 0, 0, {61, 64}, 126, 0, 0]

t = [0, 0, 10, 42, 0, 0, 33, 58, 0, 0, 61, 126, 0, 0]
k = [x.split(' ') for x in dlines]
cs = '>++++++++++[>+>++++>>>+++>+++++>>>++++++>++++++++++++<<<<<<<<<<-]>>++>>>+++>++++++++>>>+>++++++<<<<'

pointer = 0 # 58
if int(k[0][1]) == 10: pointer = 2
elif int(k[0][1]) in {42, 43, 44, 45}: pointer = 3
elif int(k[0][1]) in {32, 33, 35, 36}: pointer = 6
elif int(k[0][1]) in {58, 59}: pointer = 7
elif int(k[0][1]) in {61, 64}: pointer = 10
elif int(k[0][1]) == 126: pointer = 11
fpointer = 0

const = 0

for i in range(len(k)):
    n = int(k[i][0])
    arg = int(k[i][1])

    if arg == 10: fpointer, lr = 2, 0
    elif arg in {42, 43, 44, 45}: fpointer, lr = 3, 1
    elif arg in {32, 33, 35, 36}: fpointer, lr = 6, 0
    elif arg in {58, 59}: fpointer, lr = 7, 1
    elif arg in {61, 64}: fpointer, lr = 10, 0
    elif arg == 126: fpointer, lr = 11, 1

    dp = fpointer - pointer 
    if dp > 0: cs += ">"*dp
    elif dp < 0: cs += "<"*(-1*dp)
    pointer = fpointer

    if t[pointer] > arg:
        cs += "-"*(t[pointer] - arg)
        t[pointer] = arg
    elif t[pointer] < arg:
        cs += "+"*(arg - t[pointer])
        t[pointer] = arg
    
    if n >= 10: const = 2
    else: const = 0
    if lr == 0: cs += "<"*const + cr[n-1]
    elif lr == 1: cs += ">"*const + cl[n-1]

with open('durocode/durobfcode.txt', 'w', encoding='utf-16be') as d:
    for i in range(2):
        cs = cs.replace("><", "")
        cs = cs.replace("<>", "")
    csl = [list(g) for _, g in groupby(list(cs))]
    sym = {
    "따이":"[<.>-]",
    "딱따라딱":"[>.<-]",
    "여러분":"[<",
    "ㄱㄷ":">-]<",
    "77ㅓ억":"[>",
    "ㅇㅈㅅ": "<-]>",
    "ㅇㅅㅇ": ".",
    "지대루":">",
    "어구래":"<",
    "아":"+",
    "안해":"-",
    "못참지":"[",
    "아이좋아":"]",
    }
    for i,j in sym.items():
        cs = cs.replace(j,i)
    d.write(cs)

# test = list(set([int(x.split(' ')[0]) for x in dlines]))
# test.sort()
# print(test)
