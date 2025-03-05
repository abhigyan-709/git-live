# immutable in nature
# normal tuple
t = 1, 2, 3
print("Normal Tuple: ", t, type(t))

# mixed tuple
t1 = 1, 2, 3, "1", [1, 2, 3], 5.8, False
print("Mixed tuple: ", t1, type(t1))

# nested tuple
t3 = t1, t
print("Nested tuple: ", t3, type(t3))

# tuples are immuatable in nature, once declared with vairable, their elements can not be changed
# tuple do not support item assignments 

# tuples can contain mutable objects 
t4 = ([1, 2, 3], [1, 2, 4])
l1 = [(1, 2, 3), (1, 2, 4)]

l1[0] = (1, 2)
print(l1)

t4[0][0] = "hello"
print(t4)


# new_way

t6 = ()
print(t6, type(t6), len(t6))

t7 = "hello_world", "hello",
len(t7)
print(t7, type(t7), len(t7))

# unpacking the tuples

t10 = 12345, 6789, 10 # packing of tuple
x, y, z = t10 # unpacking of tuple

# x -- > 12345
# y -- > 6789
# z -- > 10
# a -- > 100

print(x + y + z, type(x))

