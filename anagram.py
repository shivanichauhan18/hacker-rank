a="fcrxzwscanmligyxyvym"
b="jxwtrhvujlmrpdoqbisbwhmgpmeoke"

t = {}
for c in a:
    if c not in t:
        t[c] = 0
    t[c] += 1

for c in b:
    if c not in t:
        t[c] = 0
    t[c] -= 1

total = 0
for key, val in t.items():
    total += abs(val)
print(total)

    
# c=a.split('')
# d=b.split('')
# console.log(c,d)

for i in a:
    for j in b:
        if i==j:
            print i,
