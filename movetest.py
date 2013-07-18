import pygame
from pygame.sprite import Sprite
from vec2d import vec2d

size = height, width = 640, 480

class GameObject(Sprite):
    def __init__(self, screen, img_filename, position, direction, speed):
        Sprite.__init__(self)
        self.screen = screen

        self.speed = speed
        self.base_image = pygame.image.load(img_filename).convert_alpha()
        self.image = self.base_image
        self.pos = vec2d(position)
        self.direction = vec2d(direction).normalized()
        self.image_w, self.image_h = self.image.get_size()
        self.bounds_rect = self.image.get_rect()

    def move(self):
        self.pos += self.speed
        if self.bounds_rect.right > height or self.bounds_rect.left < 0:
            self.speed.x = -self.speed.x
        if self.bounds_rect.top < 0 or self.bounds_rect.bottom > width:
            self.speed.y = -self.speed.y

    def blitme(self):
        draw_pos = self.image.get_rect().move(
                self.pos.x - self.image_w / 2,
                self.pos.y - self.image_h / 2)
        self.screen.blit(self.image, draw_pos)

def main():
    pygame.init()

    screen = pygame.display.set_mode(size)
    player_img = 'images/disk.bmp'
    beam_img = 'images/beam.bmp'
    background = pygame.image.load('images/background.bmp').convert()

    obj = GameObject(screen, player_img, (height/2, width/2), (1,0), (0, 0))
    shots = []

    while True:
        screen.blit(background, (0,0))
        for event in pygame.event.get():
            if event.type in (pygame.QUIT,):
                return

        keys = pygame.key.get_pressed()
        speed = vec2d((0,0))
        if keys[pygame.K_a]:
            shots.append(GameObject(screen, beam_img, (obj.pos.x, obj.pos.y), obj.direction, (0, 20)))
        if keys[pygame.K_UP]:
            speed.y = -5
        elif keys[pygame.K_DOWN]:
            speed.y = 5
        if keys[pygame.K_LEFT]:
            speed.x = -5
        elif keys[pygame.K_RIGHT]:
            speed.x = 5
        if keys[pygame.K_SPACE]:
            shots.append(GameObject(screen, beam_img, (obj.pos.x, obj.pos.y), obj.direction, (0, -20)))
        if keys[pygame.K_q]:
            print len(shots)
            print obj.pos
        if keys[pygame.K_ESCAPE]:
            return
        obj.speed = speed

        obj.move()
        obj.blitme()
        for s in shots:
            s.blitme()
        for s in shots:
            s.move()
            if s.bounds_rect.bottom < 0:
                shots.remove(s)
            else:
                s.blitme()

        pygame.display.update()
        pygame.time.delay(17)

if __name__ == '__main__':
    main()
