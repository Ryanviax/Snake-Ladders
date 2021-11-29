import time

# --------------------------------------------------
# Animation class
# It's pretty much a counter with a timer.
# it changes to current frame number according to the timer.
# The Animation doesn't render anything. It just tells a SpriteSheet which frame to render.
# --------------------------------------------------


class Animation:

    # Constructor
    def __init__(self, length, speed, loop):

        self.length = length
        self.speed = speed  # speed in fps
        self.loop = loop

        self.frame = 0
        self.playing = False

        self.started = time.time()
        self.elapsed = 0
        self.frame_time = 1 / speed

    # Updates the frame according to the timer.
    def update(self):
        if self.playing:

            now = time.time()
            self.elapsed = now - self.started

            if self.elapsed > self.frame_time:
                self.frame += 1
                self.started = time.time()

                if self.frame >= self.length:
                    if self.loop:
                        self.frame = 0
                    else:
                        self.frame = self.length - 1

    def play(self): self.playing = True

    def stop(self): self.playing = False

    # Returns the current frame number.
    def getCurrentFrame(self): return self.frame
