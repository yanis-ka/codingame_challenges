import sys

N, price = map(int, (input(), input()))
out = []
budgets = sorted(int(input()) for i in range(N))

for i in range(N, 0, -1):
    share = min(price//i, budgets.pop(0))
    price -= share
    out += [share]
    
print('IMPOSSIBLE' if price else '\n'.join(map(str, out)))
