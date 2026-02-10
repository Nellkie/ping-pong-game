from pygame import *

window = window = display.set_mode((900, 800))

clock = time.Clock()
BG = "#b289ff"
game = True


class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, width, height, speed):
        super().__init__()
        self.image = transform.scale(image.load(img), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



while game:
    window.fill(BG)

    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(60)

