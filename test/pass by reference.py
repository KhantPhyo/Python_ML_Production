def modify_immutable(x):
    print(f"Before modification (immutable): {x}")
    x = 42
    print(f"After modification (immutable): {x}")

def modify_mutable(lst):
    print(f"Before modification (mutable): {lst}")
    lst.append(42)
    print(f"After modification (mutable): {lst}")

# Immutable object example
a = 10
print(f"Original immutable a: {a}")
modify_immutable(a)
print(f"After function call, a: {a}")

print()

# Mutable object example
b = [1, 2, 3]
print(f"Original mutable b: {b}")
modify_mutable(b)
print(f"After function call, b: {b}")
