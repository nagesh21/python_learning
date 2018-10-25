import random
a=random.random()
print(a)
a=random.randint(5,30)
print(a)
a=random.randrange(5,30)
print(a)
a=random.seed(5)
a=random.randint(5,20)
print(a)

#random list
l=[1,2,44,66,88]
print(random.choice(l))

#random shuffle

l=[1,2,5,6,8,0]
random.shuffle(l)
print(l)
