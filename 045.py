t = lambda n : n*(n+1)/2
p = lambda n : n*(3*n-1)/2
h = lambda n : n*(2*n-1)

ts = set([t(n) for n in range(285,301)])
ps = set([p(n) for n in range(165,301)])
hs = set([h(n) for n in range(143,301)])

up = 301
while True:
    ts = set([t(n) for n in range(286,up)])
    ps = set([p(n) for n in range(166,up)])
    hs = set([h(n) for n in range(144,up)])
    if (ts & ps & hs) == set():
        up += 100
    else:
        print(ts & ps & hs)
        break
