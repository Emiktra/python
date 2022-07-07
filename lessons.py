def hi(elo):
  hi.max_num = elo[0]
  for i in elo:
    if i > hi.max_num: hi.max_num=i
  print(hi.max_num)

elo=[12,33,35,346,4123,3545,23435,13423,3434,2535,3425]
hi(elo)