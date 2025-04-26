# Creteate an empty set
s = set()

# Add elements to set
s.add("one")
s.add("two")
s.add("three")
s.add("four")
print(s)                # Sets unordered


s.remove("three")
print(s)

print(f"The set has {len(s)} elements.")

 # Listas
s = []

s.append("one")         #  List ordered
s.append("two")
s.append("three")
s.append("four")

s.remove("three")

print(s)
print(f"The list has {len(s)} elements.")