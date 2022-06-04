# Python has a special basic data type that defines a single special data object
# called None. There is only instance of None in the entire Python system.

print("try " + "it")

# Python 2: raw_input();
# Python 3: input();
# name = input("Name: ")
# print(name)

# List
# List can contain different types of elements
x = [2, "two", [1, 2, 3]]

# Slicing, append, extend, insert, del, remove
x = [1, 2, 3, 4]
y = [5, 6, 7]

# If we try to append one list to another, the list get appended as single element
# of the main list
x.append(y)
print(x)

# extend method allows us to add one list to another.
x.extend(y)
print(x)

# insert method to insert new list elements. It take in two arguments, the first is the index position in the list
# where the new element should be inserted.
x = [2, "two", "three"]
x.insert(2, 3)
print(x)

# delete elements in a list.
del x[0]
print(x)

# remove method looks for the first instance of a given value in a list and remove that value from the list
x = [1, 2, 3, 4, 5, 3, 6, 7, 8]
x.remove(3)
print(x)

# reverse method efficiently reverse a list
x = [2, "two", [1, 2, 3]]
x.reverse()
print(x)

# List membership with 'in/not in' operator
3 in [1, 3, 4, 5]

# '+' operator: Concatenating two existing list.
z = [1, 2, 3] + [4, 5]
print(z)

# '*' operator: To produce a list of given size. More efficiency, A list that
# doesn't change in size doesn't incur any memory reallocation.
z = [None] * 4
z = [3, 1] * 2

# index() search through a list looking for a list element equivalent
# to a given value and returns the position of that list element
x = [1, 3, 7]
x.index(7) # return the index of element 7: 2


# Nested list and deep copies
print("Nested")
nested = [0]
original = [nested, 1]
print(original)

# shallow copy
original = [[0], 1]
shallow = original[:]
shallow[0][0] = "zero"
print("Original: "+ str(original))
print("Shallow: " + str(shallow) + "\n")

shallow[1] = 50
print("Original: " + str(original))
print("Shallow: " + str(shallow))

# deep copy
import copy

original = [[0], 1]
deep = copy.deepcopy(original)
deep[0][0] = "zero"

print("Original: " + str(original))
print("Deep: " + str(deep))

## Tuples
# Tuples are data structures that are very similar to list, but can't be modified.
x = ([1,2,3], 'b', 'c')
print(x[:])

# Tuple itself can't be modified. But if they contain any mutable objects
# ex. list, dict. these may be changed.
x[0][0] = "Hello"
print(x[:])

'''
variable scope
unlike java, a python variable is in scope for the whole of the function(or class, or module), where it appears, not just
in the inner most block. its is as though you declared int x at the top of the function except in python you don't have 
to declare variables.

1. nonlocal bindings can only be used inside of nested functions. A nonlocal variable has to be defined in the enclosing
function scope. 

2. If the variable is not defined in the enclosing function scope, the variable cannot be defined in the nested scope.
'''
# local - enclosure -global - build-in (while,if,for之类没有作用域功能，只有module, def, class, lambdad等有)
# 在一个作用域中声明的变量可以在该作用域及他包含的下一级作用域中使用
# 如果在下一级作用域中，重新声明了一个同名的变量，则下一级作用域中的变量将会覆盖上一层的变量
a = 100
def test():
    global a
    a = a + 1
    if True:
        b = 100
    print(a)
    print(b)

def external():
    b = 100

    def internal():
        # nonlocal b
        print(b)
        b = 200
        return b

    internal()
    print(b)

test()
#external()

