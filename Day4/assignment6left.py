word = "Funwith"

for i in range(1, len(word) + 1):
    spaces = len(word) - i
    print(" " * spaces + word[:i])

for i in range(len(word) - 1, 0, -1):
    spaces = len(word) - i
    print(" " * spaces + word[:i])