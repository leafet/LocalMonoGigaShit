from PIL import Image

width, height = 500, 500

pixel_data = []

for y in range(height):
    for x in range(width):
        if (x // 10 + y // 10) % 2 == 0:
            pixel_data.append(255)
        else:
            pixel_data.append(0)

img = Image.new("L", (width, height))
img.putdata(pixel_data)

img.save("out.png")
