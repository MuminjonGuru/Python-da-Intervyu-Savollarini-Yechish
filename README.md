# Python-da Intervyu Savollarini Yechish

# List - Ordered & Mutable

    my_list = [1,2,3,4,5]
    print(my_list[2])
    print(my_list[-1])
    print(my_list[1:4])
    print(my_list[2:])
    
    # List: modifying items
    my_list = [1,2,3,4,5]
    my_list[2] = 30
    print(my_list)
    my_list[:2] = [10, 20]
    print(my_list)
    
    # List: methods
    my_list = [10, 20, 30, 40, 50]
    # Append(60) - list oxiriga
    # Remove(50) - berilgan itemni olib tashlaydi
    my_list.pop() - oxirgi elementni olib tashlaydi    
    print(my_list)
    my_list.count(40)
    
# Tuple - Ordered & Immutable

    my_new_tuple = 1, 'apple', 2, 'banana'
    my_tuple = (1, 'apple', 2, 'banana', 'delphi')
    print(my_tuple)
    my_tuple_two = 1, 'apple', 2, 'banana', 'pascal'
    print(my_tuple)
	
    print('my_tuple[0]', my_tuple[0])
    print('my_tuple[1:5], my_tuple[1:5])

# Set - Unordered Collection with No Duplicate
	
    my_set1 = set([1, 2, 3, 4, 5])
    my_set2 = set([3, 4, 5, 6, 7])
    my_set1.add(6)
    print(my_set1)
    my_set1.remove(6)
    print(my_set1)
    print(my_set1.union(my_set2))
    print(my_set1.intersection(my_set2))
    print(my_set1.difference(my_set2))

# Dictionary - KeyValue Pairs

    fruits = {'apple': 10, 'orange': 5, 'banana': 9}
    print(fruits)
    
    fruits2 = dict([('apple', 1), ('orange', 6), ('banana', 9)])
    print(fruits2)
    
    print(fruits['apple'])
    
    print(fruits.items())
    print(list(fruits.items()))
    
    print(fruits.keys())
    print(fruits.values())
    
    print(fruits.popitem())
    print(fruits)
    
    my_list = [1,2,3,4,5]
    print(30 in my_list)
