import sys
import os
import json
import pprint
import pygame
import time

class Explosion(pygame.sprite.Sprite):
	def __init__(self, center, explosion_anim):
		pygame.sprite.Sprite.__init__(self)
		self.explosion_anim = explosion_anim
		self.image = self.explosion_anim[0]
		self.rect = self.image.get_rect()
		self.rect.center = center
		self.frame = 0
		self.last_update = pygame.time.get_ticks()
		self.frame_rate = 50

	def update(self):
		now = pygame.time.get_ticks()
		if now - self.last_update > self.frame_rate:
			self.last_update = now
			self.frame += 1
			if self.frame == len(self.explosion_anim):
				self.kill()
			else:
				center = self.rect.center
				self.image = self.explosion_anim[self.frame]
				self.rect = self.image.get_rect()
				self.rect.center = center

	def sss(self):
		self.kill()

def mykwargs(argv):

	args = []
	kargs = {}

	for arg in argv:
		if '=' in arg:
			key, val = arg.split('=')
			kargs[key] = val
		else:
			args.append(arg)

	return args, kargs

def main(**kwargs):
	all_sprites = pygame.sprite.Group()
	print("Printing kwargs from main function")
	pprint.pprint(kwargs)

	timer = pygame.time.Clock()

	x = int(kwargs['startX'])
	y = int(kwargs['startY'])

	bg_x = -(int(kwargs['startX']))
	bg_y = -(int(kwargs['startY']))

	width = 20
	height = 20
	vel = 10

	pygame.init()

	window = pygame.display.set_mode((int(kwargs['width']), int(kwargs['height'])))
	pygame.display.set_caption(kwargs['title'])

	bg = pygame.image.load(kwargs['background_image'])
	bg = pygame.transform.scale(bg, (int(kwargs['width']) * 3, int(kwargs['height']) * 3))

	car = pygame.image.load(kwargs['player_image'])
	car = pygame.transform.scale(car, (50, 30))

	gameLoop = True
	
	explosion = []
	for i in range(15):
		if i < 9:
			explosion.append(pygame.image.load("explosion/green_blob_explosion_01_00" + str(i + 1) + ".png").convert_alpha())
		else:
			explosion.append(pygame.image.load("explosion/green_blob_explosion_01_0" + str(i + 1) + ".png").convert_alpha())

	flag_l = True
	flag_r = True
	flag_u = True
	flag_d = True
	flag = False

	while gameLoop:
		pygame.time.delay(10)

		for event in pygame.event.get():
			if(event.type == pygame.QUIT):
				gameLoop = False

		keys = pygame.key.get_pressed() 


		if keys[pygame.K_LEFT] and bg_x < int(kwargs['width']) / 2 - 25:
			flag_l = True
			bg_x += vel

		if keys[pygame.K_LEFT] and bg_x >= int(kwargs['width']) / 2 - 25:
			flag_l = False

		if keys[pygame.K_RIGHT] and  bg_x > -int(kwargs['width']) * 2 - int(kwargs['width']) / 2 + 25:
			flag_r = True
			bg_x -= vel
			
		if keys[pygame.K_RIGHT] and  bg_x <= -int(kwargs['width']) * 2 - int(kwargs['width']) / 2 + 25:
			flag_r = False

		if keys[pygame.K_UP] and bg_y < int(kwargs['height']) / 2 - 15:
			flag_u = True
			bg_y += vel

		if keys[pygame.K_UP] and bg_y >= int(kwargs['height']) / 2 - 15:
			flag_u = False

		if keys[pygame.K_DOWN] and bg_y > -int(kwargs['height']) * 2 - int(kwargs['height']) / 2 + 15:
			flag_d = True
			bg_y -= vel

		if keys[pygame.K_DOWN] and bg_y <= -int(kwargs['height']) * 2 - int(kwargs['height']) / 2 + 15:
			flag_d = False



		window.fill((0,0,0))
		window.blit(bg, (bg_x,bg_y))
		window.blit(car, (int(kwargs['width']) / 2 - 25, int(kwargs['height']) / 2 - 15))

		if flag_l and flag_r and flag_u and flag_d:
			all_sprites = pygame.sprite.Group()
		else:
			expl = Explosion((int(kwargs['width']) / 2, int(kwargs['height']) / 2 - 30), explosion)
			all_sprites.add(expl)

		if bg_x < int(kwargs['width']) / 2 - 25 and bg_x > -int(kwargs['width']) * 2 - int(kwargs['width']) / 2 + 25 and bg_y < int(kwargs['height']) / 2 - 15 and bg_y > -int(kwargs['height']) * 2 - int(kwargs['height']) / 2 + 15:
			all_sprites = pygame.sprite.Group()

		all_sprites.update()
		all_sprites.draw(window)
		pygame.display.flip()

	pygame.quit()

def usage():
	print("Usage: python test.py title='Move_My_Player' player_image=car.png width=640 height=480 startX=100 startY=100 background_image=background.png")
	print("Example:\n\n\t python basic.py title='Game 1' imag_path=./sprit.png width=640 height=480\n")

	sys.exit()


if __name__=='__main__':
	argv = sys.argv[1:]

	if len(argv) < 6:
		print(len(argv))
		usage()

	args, kwargs = mykwargs(argv)

	print("printing dictionary from name == main:")
	pprint.pprint(kwargs)


	main(**kwargs)