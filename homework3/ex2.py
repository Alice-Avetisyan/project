colors = ["red", "green", "blue", "yellow"]
print("Enter a color: ")
coloradd = input()
colors.append(coloradd)
print("a) total number of colors: ", len(colors))
print("b) colors on even positions: ", colors[::2])
