# save a single generated image into disk

# noLoop to prevent auto drawing, and redraw to run code in draw a single time
def setup():
    size(100, 100)
    noLoop()


def draw():
    background(255, 204, 0)
    fill(0)
    save("testImage.png")