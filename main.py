from configparser import ConfigParser
from pygame import mixer
from time import sleep
# from sys import exit
import serial, random, sys, os

# Parse the settings.ini file
config = ConfigParser()
config.read("settings.ini")
VOLUME_BACKGROUND = config.getfloat("mixer", "volumeBackground")
VOLUME_EFFECTS = config.getfloat("mixer", "volumeEffects")
LIGHTNING_DELAY_MIN = config.getfloat("delays", "lightningDelayMin")
LIGHTNING_DELAY_MAX = config.getfloat("delays", "lightningDelayMax")
THUNDER_DELAY_MIN = config.getfloat("delays", "thunderDelayMin")
THUNDER_DELAY_MAX = config.getfloat("delays", "thunderDelayMax")

# Channels are not polyphonic! Change if it becomes a problem!
# Initialize mixer and channels
mixer.init(48000, -16, 1, 1024)
mixer.music.set_volume(VOLUME_BACKGROUND)
channelEffects = mixer.Channel(1)
channelEffects.set_volume(VOLUME_EFFECTS)

# Handle thunder sounds
thunderSounds = []
for snd in os.listdir("audio/samples"):
    thunderSounds.append("audio/samples/" + snd)

# Setup the delays for lightning and thunder
lightningDelay = round(random.uniform(LIGHTNING_DELAY_MIN, LIGHTNING_DELAY_MAX), 2)
thunderDelay = round(random.uniform(THUNDER_DELAY_MIN, THUNDER_DELAY_MAX), 2)

# Loop background audio
backgroundAudioPath = None
for file in os.listdir("audio"):
	if file.endswith(".ogg"):
		backgroundAudioPath = os.path.join("audio", file)

if (backgroundAudioPath == None):
	sys.exit("No background audio file found!")

# Play background audio on loop
mixer.music.load(backgroundAudioPath)
mixer.music.play(-1, 0, 2000)


def handleLeds():
	# Wiggle the LED brightness value around, then return it to zero
	print("↯")
	sleep(0.1)
	# os.system("cls")
	pass

while(True):
    # Delay for next lightning strike
	sleep(lightningDelay)
	
	# Handle LED's here
	handleLeds()

	# Flash lightning and delay for thunder
	sleep(thunderDelay)
	
	# Randomize the delay and play sound effect
	lightningDelay = round(random.uniform(LIGHTNING_DELAY_MIN, LIGHTNING_DELAY_MAX), 2)
	thunderDelay = round(random.uniform(THUNDER_DELAY_MIN, THUNDER_DELAY_MAX), 2)
	channelEffects.play(mixer.Sound(random.choice(thunderSounds) ) )