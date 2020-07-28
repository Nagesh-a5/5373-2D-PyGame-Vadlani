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
	print("Printing kwargs from main function")
	pprint.pprint(kwargs)

	x = 200
	y = 160
	width = 100
	height = 60
	vel = 10

	pygame.init()

	window = pygame.display.set_mode((int(kwargs['width']), int(kwargs['height'])))
	pygame.display.set_caption(kwargs['title'])

	bg = pygame.image.load(kwargs['imag_path'])
	bg = pygame.transform.scale(bg, (640, 480))

	car = pygame.image.load('car.png')
	car = pygame.transform.scale(car, (100, 60))

	gameLoop = True
	

	while gameLoop:
		pygame.time.delay(10)

		for event in pygame.event.get():
			if(event.type == pygame.QUIT):
				gameLoop = False

		keys = pygame.key.get_pressed() 

		if keys[pygame.K_LEFT] and x>0:
			x -= vel 
		  
		if keys[pygame.K_RIGHT] and x<640-width: 
			x += vel 
		     
		if keys[pygame.K_UP] and y>0: 
			y -= vel 

		if keys[pygame.K_DOWN] and y<480-height: 
			y += vel 

		window.fill((0,0,0))
		window.blit(bg, (0,0))
		window.blit(car, (x, y))
		# pygame.draw.rect(window, (255, 0, 0), (x, y, width, height)) 
		pygame.display.flip()

		# pygame.display.update() 

	pygame.quit()

def usage():
	print("Usage: python basic.py title=string imag_path=string width=int height=int [jsonfile=string]")
	print("Example:\n\n\t python basic.py title='Game 1' imag_path=./sprit.png width=640 height=480\n")

	sys.exit()


if __name__=='__main__':
	argv = sys.argv[1:]

	if len(argv) < 4:
		print(len(argv))
		usage()

	args, kwargs = mykwargs(argv)

	print("printing dictionary from name == main:")
	pprint.pprint(kwargs)

	main(**kwargs)


# python test.py title=Game1 imag_path=./sprit.png width=640 height=480