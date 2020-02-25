from musurgia.agrandom import AGRandom

ar_1 = AGRandom(pool=[5, 2, 3, 1, 2, 1])
print(ar_1.pool)
ar_2 = AGRandom(pool=[5.3, 2.2, 3, 1, 2, 1])
print(ar_2.pool)
ar_3 = AGRandom(pool=['1', '2', '3', '4'])
print(ar_3.pool)
ar_4 = AGRandom(pool=[4, 3, 5.3, 2.2, 3, 1, 2, 1])
print(ar_4.pool)
#
# pool = ['1', '2', '3', '4']
# print(sorted(list(set(pool))))

