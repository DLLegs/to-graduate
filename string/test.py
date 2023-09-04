def add_mul(what, *args):
    if what == "add":
        result = 0
        for i in args:
            result = result + i
    elif what == "mul":
        result = 1
        for i in args:
            result = result * i
    return result

result = add_mul('add', 1,2,3,4,5)
print(result)
result = add_mul('mul', 1,2,3)
print(result)