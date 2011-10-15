import pygame

size = height, width = 640, 480

class Vector:
	def __init__(self, x, y):
		self.x = x
		self.y = y

class GameObject:
	def __init__(self, image, position, speed):
		self.speed = speed
		self.image = image
		self.pos = image.get_rect().move(position.x, position.y)

	def move(self):
		self.pos = self.pos.move(self.speed.x, self.speed.y)
		if self.pos.right > height or self.pos.left < 0:
			self.speed.x = -self.speed.x
		if self.pos.top < 0 or self.pos.bottom > width:
			self.speed.y = -self.speed.y

# TODO considerar usar NumPy para vetores
def main():
	pygame.init()
	
	screen = pygame.display.set_mode(size)
	player = pygame.image.load('images/disk.bmp').convert()
	background = pygame.image.load('images/background.bmp').convert()
	screen.blit(background, (0,0))

	obj = GameObject(player, Vector(height/2, width/2), Vector(0, 0))

	while True:
		for event in pygame.event.get():
			if event.type in (pygame.QUIT,):
				return

		keys = pygame.key.get_pressed()
		speed = Vector(0,0)
		if keys[pygame.K_UP]:
			speed.y = -5
		elif keys[pygame.K_DOWN]:
			speed.y = 5
		if keys[pygame.K_LEFT]:
			speed.x = -5
		elif keys[pygame.K_RIGHT]:
			speed.x = 5
		if keys[pygame.K_ESCAPE]:
			return
		obj.speed = speed

		screen.blit(background, obj.pos, obj.pos)
		obj.move()
		screen.blit(obj.image, obj.pos)

		pygame.display.update()
		pygame.time.delay(17)

if __name__ == '__main__':
	main()
