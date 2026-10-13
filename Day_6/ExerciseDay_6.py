'''

empty_tuple=()
empty_t=tuple()
print(empty_tuple) # ()
print(empty_t)     # ()



simple=("a","b","c")
capital=("A","B","C")
all= simple + capital
print(all) # ('a', 'b', 'c', 'A', 'B', 'C')
print(len(all)) # 6
simple=list(simple)
simple.append("d")
simple=tuple(simple)
print(simple) # ('a', 'b', 'c', 'd')

'''


fruits=('banana', 'orange', 'mango', 'lemon')
vegetables=('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
animal=('Tiger', 'Lion', 'Deer', 'Monkey')
food_stuff_tp=fruits + vegetables + animal
print(food_stuff_tp) # ('banana', 'orange', 'mango', 'le
food_stuff_tp=list(food_stuff_tp)
'''
middle=len(food_stuff_tp) // 2
print(food_stuff_tp[middle -1:middle + 1]) # ['lemon', 'Tomato']
'''
first_3=food_stuff_tp[:3]
print(first_3) # ['banana', 'orange', 'mango']
last_3=food_stuff_tp[-3:]
print(last_3) # ['Deer', 'Monkey', 'Tiger']
food_stuff_tp=tuple(food_stuff_tp)
del food_stuff_tp
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia" in  nordic_countries) # False
print("Iceland" in nordic_countries) # True
