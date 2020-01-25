width, height = 0, 0

def set_dimensions(w, h):
    global width, height
    width, height = w, h


def get_track1():
    return (
        ( # Inner points
            (250, 350),
            (270, 408),
            (360, 460),
            (512, 475),
            (width - 360, 460),
            (width - 270, 408),
            (width - 250, 350),
            (width - 270, height - 408),
            (width - 360, height - 460),
            (512, height - 475),
            (360, height - 460),
            (270, height - 408)
        ),
        ( # Outer points
            (50, 350),
            (100, 540),
            (239, 637),
            (512, 650),
            (width - 239, 637),
            (width - 100, 540),
            (width - 50, 350),
            (width - 100, height - 540),
            (width - 239, height - 637),
            (512, height - 650),
            (239, height - 637),
            (100, height - 540)
        )
    )


def get_track2():
    