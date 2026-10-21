lst = ["Apple", "Blueberry", "Orange", "Banana", "Grapes"]
print("Length of list", len(lst))
print("First element of list", lst[0])
print("Last element of list", lst[-1])

lst.append("Mango")
print("Updated list", lst)

lst.remove("Grapes")
print("Remove Grapes from list", lst)
lst.sort()
print("Sorted List", lst)
lst.pop(3)
print("Updated list after popping fruit", lst)

lst.reverse()
print("Reversed List", lst)
print("Multiplication on List", lst*2)
lst.slice[:4]
print("Sliced List", lst[:4])
lst.clear()
print("Updated and cleared list", lst)