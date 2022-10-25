"""An example of for in syntax."""

names: list[str] = ["Caroline", "Audrey", "Anna", "Zoe"]

# Example of iterating through names using a while loop
print("while output:")
i: int = 0
while i < len(names):
    name: str = names[i]
    print(name)
    i += 1

print("for...in output")
# The following for...in loop is the same as the while loop
for name in names:
    print(name)