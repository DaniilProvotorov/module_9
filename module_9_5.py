import itertools

def all_variants(text):
    for i in range(len(text)):
        res = itertools.combinations(text, i + 1)
        yield res

f = all_variants('mom')
for val in f:
    for a in val:
        print(a)
