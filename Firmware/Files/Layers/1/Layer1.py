def layer(display):
    display.line(0, 15, 127, 15, 1)

    display.text("L1", 1, 4, 1)

    display.ellipse(87, 7, 5, 5, 1, False)

    display.text("None", 95, 4, 1)

    display.line(87, 2, 87, 6, 1)

    display.line(0, 31, 128, 31, 1)
    display.line(0, 47, 127, 47, 1)
    display.line(32, 16, 32, 64, 1)
    display.line(64, 16, 64, 64, 1)
    display.line(96, 16, 96, 64, 1)

    display.text("NONE", 0, 20, 1)
    display.text("NONE", 32, 20, 1)
    display.text("NONE", 65, 20, 1)
    display.text("NONE", 97, 20, 1)
    display.text("NONE", 0, 36, 1)
    display.text("NONE", 32, 36, 1)
    display.text("NONE", 65, 36, 1)
    display.text("NONE", 97, 36, 1)
    display.text("NONE", 0, 52, 1)
    display.text("NONE", 32, 52, 1)
    display.text("NONE", 65, 52, 1)
    display.text("NONE", 97, 52, 1)

    display.show()