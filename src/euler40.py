print('project euler problem 40')

# create the string

champernownes = ''
for i in range(0, 1000001):
  champernownes += str(i)


print ('solution is ', int(champernownes[1]) * int(champernownes[10]) * int(champernownes[100]) * int(champernownes[1000]) * int(champernownes[10000]) * int(champernownes[100000]) * int(champernownes[1000000]))