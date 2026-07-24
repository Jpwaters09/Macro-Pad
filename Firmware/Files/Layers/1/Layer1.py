def layer(display):
    display.line(0, 15, 127, 15, 1)

    display.text("L1", 1, 4, 1)

    display.ellipse(71, 7, 5, 5, 1, False)

    display.text("Volume", 79, 4, 1)

    display.line(71, 2, 71, 6, 1)

    display.line(0, 31, 128, 31, 1)
    display.line(0, 47, 127, 47, 1)
    display.line(32, 16, 32, 64, 1)
    display.line(64, 16, 64, 64, 1)
    display.line(96, 16, 96, 64, 1)

    display.text("COPY", 0, 20, 1)
    display.text("PSTE", 32, 20, 1)
    display.text("CUT", 69, 20, 1)
    display.text("SALL", 97, 20, 1)
    display.text("UNDO", 0, 36, 1)
    display.text("REDO", 32, 36, 1)
    display.text("FIND", 65, 36, 1)
    display.text("PSCR", 97, 36, 1)
    display.text("NEWF", 0, 52, 1)
    display.text("OPEN", 32, 52, 1)
    display.text("SAVE", 65, 52, 1)
    display.text("LOCK", 97, 52, 1)

    display.show()