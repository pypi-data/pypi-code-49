
start_nuxmv()
x = 0
for x in range(0, 10, 2):
  x += 1

ltlspec("F x = 4")
end_nuxmv()

start_nuxmv()
x = 11

invarspec("x = 11")
end_nuxmv()
