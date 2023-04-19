def brightness(r, g, b):
    return (0.2126*r + 0.7152*g + 0.0722*b)

print(brightness(255, 255, 255)) # output: 255.0
print(brightness(0, 0, 0)) # output: 0.0
print(brightness(255, 0, 0)) # output: 54.213
