from configparser import ConfigParser
import pygame, pygame_gui
import sys, os

WINDOW_WIDTH = 320
WINDOW_HEIGHT = 256

config = ConfigParser()
config.read("settings.ini")
settings = {}

# Update the settings dictionary from settings.ini
def initUpdate():
	for section in config.sections():
		settings[section] = {}
		for item in config.items(section):
			settings[section][item[0] ] = item[1]

def remap(value, inMin, inMax, outMin, outMax):
	return outMin + (float(value - inMin) / float(inMax - inMin) * (outMax - outMin) )

pygame.init()
pygame.display.set_caption("GUI Test!")
windowSurface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT) )

windowBackground = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT) )
windowBackground.fill(pygame.Color("#000000") )

manager = pygame_gui.UIManager((WINDOW_WIDTH, WINDOW_HEIGHT) )
clock = pygame.time.Clock()

# ------------------------------------------------------------ UI Elements
volumeBackgroundLabel = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((16,16), (160,16) ), text="Background Volume")
buttonTest = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((16,32), (160,32) ), text="Hello, World!", manager=manager)

programRunning = True
while programRunning:
	delta = clock.tick(60) / 1000.0

	for event in pygame.event.get():
		if (event.type == pygame.QUIT):
			programRunning = False
		
		if (event.type == pygame_gui.UI_BUTTON_PRESSED):
			if (event.ui_element == buttonTest):
				print("Hello, World!")
		
		manager.process_events(event)
	
	manager.update(delta)

	windowSurface.blit(windowBackground, (0,0) )
	manager.draw_ui(windowSurface)
	pygame.display.update()