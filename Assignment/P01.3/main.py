import sys
import os
import json
import pprint
import pygame

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

	animation_frame = []

	print("Printing kwargs from main function")
	pprint.pprint(kwargs)

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

	bg_change = bg.convert_alpha()
	w, h = bg_change.get_size()
	for i in range(int(w / 10)):
		animation_frame.append(bg_change.subsurface((i * 10, 0, 10, 480)))

	car = pygame.image.load(kwargs['player_image'])
	car = pygame.transform.scale(car, (50, 30))

	gameLoop = True
	
	count_x = 0

	while gameLoop:
		pygame.time.delay(10)

		for event in pygame.event.get():
			if(event.type == pygame.QUIT):
				gameLoop = False

		keys = pygame.key.get_pressed() 

		if keys[pygame.K_LEFT]:
			count_x -= 1

		if keys[pygame.K_RIGHT]:
			count_x += 1

		if keys[pygame.K_UP] and bg_y < int(kwargs['height']) / 2 - 15:
			bg_y += vel

		# if keys[pygame.K_DOWN] and y<480-30: 
		# 	y += vel 

		# if keys[pygame.K_DOWN] and y>=480-30 and bg_y > -480 * 2: 
		# 	bg_y -= vel 

		if keys[pygame.K_DOWN] and bg_y > -int(kwargs['height']) * 2 - int(kwargs['height']) / 2 + 15:
			bg_y -= vel

		window.fill((0,0,0))
		# window.blit(bg, (bg_x,bg_y))
		start_point = 0
		try:
			for i in range(count_x, int(640 / 10) + count_x):
				window.blit(animation_frame[i], (10 * start_point, 0))
				start_point += 1
				# window.blit(animation_frame[1], (10, 0))
		except:
			count_x = 0
			for i in range(count_x, int(640 / 10) + count_x):
				window.blit(animation_frame[i], (10 * start_point, 0))
				start_point += 1

		window.blit(car, (int(kwargs['width']) / 2 - 25, int(kwargs['height']) / 2 - 15))
		# pygame.draw.rect(window, (255, 0, 0), (x, y, width, height)) 
		pygame.display.flip()

		# pygame.display.update() 

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


# python test.py title=Game1 imag_path=./sprit.png width=640 height=480