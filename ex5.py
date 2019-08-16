name = 'Zed a. Shaw'
age  = 35 # not a lie
height = 74 * 2.54 # inches trans to cm
weight = 180 * 0.45  # lbs trans to kgs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's a talk about {name}")
print(f"He's {height} cm tall.")
print(f"He's {weight} kgs heavy.")
print(f"Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it eacctly right
total = round(age + height + weight)
print(f"If I add {age}, {height} and {weight} I get {total}.")
