import sys


print("=== Comand Quest ===")
i = 1
argv_count = len(sys.argv)
print(f"Program name: {sys.argv[0]}")
if argv_count < 2:
    print("No arguments provided!")
else:
    print(f"Arguments received: {argv_count - 1}")
    for arg in sys.argv[1:]:
        print(f"Argument {i}: {arg}")
        i += 1
print(f"Total arguments: {argv_count}")
print()
