import random

list = open('List.csv').read().split(',')
listRand = random.sample(list,300)
file= open('Results.txt', 'w')
file.write(str(listRand))
file.close()
