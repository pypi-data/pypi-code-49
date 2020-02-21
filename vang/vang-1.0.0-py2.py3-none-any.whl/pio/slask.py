from vang.pio.shasum_diff_dirs import diff

d1 = dict([(1, 2), (3, 4)])
print(d1)

d2 = dict(zip(range(5), range(5, 10)))
print(d2)

print(list(range(10)[::2]))
print(list(range(10)[1::2]))


d3 = dict(zip([1, 2, 3], [4, 5, 6]))
print(d3)


diff('/Users/magnus/slask/condep/deploy/config/app.sign-1.0.0-SNAPSHOT', '/Users/magnus/slask/condep/work/config/app.sign-1.0.0-SNAPSHOT', [])