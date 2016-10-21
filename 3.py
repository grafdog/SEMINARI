import string as st

file_license = open("/usr/share/licenses/python/LICENSE", "r")
data = file_license.read()
a= list((data.split()))
for x in a:
    if x in st.punctuation:
        a.pop(a.index(x))
d = {}
k = []
n = {}
r = []
for x in a:
    r.append(x.lower())
for w in r:
    if w in d:
        d[w] += 1
    else:
        d[w] = 1
b = []
n = {d[s]:s for s in d}
for i in range(1):
    k = max(n)
    f = n[k]
    b.append(f)
    b.append(k)
    del n[k]
print(b)
