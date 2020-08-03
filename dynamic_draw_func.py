import scipy as sp
import pyglet


class ChainArrows:
    def __init__(self, c_n, batch, group=2):
        if len(c_n) % 2 == 0 and len(c_n) < 3:
            raise ValueError("length of c_n is improper.")

        self.t = 0
        self.arrow_img = pyglet.image.load("img/arrow.png")
        self.arrow_img.anchor_y = self.arrow_img.height // 2

        arrows = [pyglet.sprite.Sprite(self.arrow_img, batch=batch, group=group)
                  for _ in range(len(c_n) * 2 + 1)]
        self.c_n = c_n.copy()
        self.c_len = len(c_n)
        for arrow, c in zip(arrows, c_n):
            arrow.scale = sp.sqrt(c.real ** 2 + c.imag ** 2)
            arrow.rotation = (sp.log(c / arrow.scale).imag / sp.pi) * 180

        arrow0 = arrows.pop(-len(c_n)//2)
        self.arrows = []
        for i in range(len(arrows) // 2):
            self.arrows.append(arrows[-i])
            self.arrows.append(arrows[i])
        self.arrows.append(arrow0)
        self.arrows.reverse()

    def update(self, dt):
        self.t += dt
        for i in range(self.c_len):
            if
