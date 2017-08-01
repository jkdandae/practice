color = ["red", "blue", "green"]
color2 = ['orange', 'black', 'white']
print(color + color2)
print(color[0])
color[0] = "yellow"
print(color[0])
print(color * 2)
print("blue" in color2)
total_color = color + color2
print(total_color)
color.append("white")
print(color)
color.extend(["black", "purple"])
print(color)
color.insert(0, "orange")
print(color)
color.remove("white")
print(color)
del color[0]
print(color)
