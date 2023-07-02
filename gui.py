import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from lightningUi import Ui_Main
from configparser import ConfigParser

# pyside6-uic LightningUi.ui > lightningUi.py

config = ConfigParser()
config.read("settings.ini")
settings = {}

class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.ui = Ui_Main()
		self.ui.setupUi(self)
		
	def volumeBackgroundUpdate(self):
		self.ui.volumeBackgroundValue.setText(str(int(self.ui.volumeBackgroundSlider.value() ) ) )
	
	def volumeEffectsUpdate(self):
		self.ui.volumeEffectsValue.setText(str(int(self.ui.volumeEffectsSlider.value() ) ) )

def remap(value, inMin, inMax, outMin, outMax):
	return outMin + (float(value - inMin) / float(inMax - inMin) * (outMax - outMin) )

# Update the settings dictionary from settings.ini
def initUpdate():
	for section in config.sections():
		settings[section] = {}
		for item in config.items(section):
			settings[section][item[0] ] = item[1]

if (__name__ == "__main__"):
	app = QApplication(sys.argv)

	initUpdate()
	
	window = MainWindow()
	
	volumeBackgroundValue = remap(float(settings["mixer"]["volumebackground"] ), 0.0,1.0, 0.0, 100.0)
	window.ui.volumeBackgroundValue.setText(str(int(volumeBackgroundValue) ) )
	window.ui.volumeBackgroundSlider.setValue(int(volumeBackgroundValue) )
	window.ui.volumeBackgroundSlider.valueChanged.connect(window.volumeBackgroundUpdate)

	volumeEffectsValue = remap(float(settings["mixer"]["volumeeffects"] ), 0.0,1.0, 0.0, 100.0)
	window.ui.volumeEffectsValue.setText(str(int(volumeEffectsValue) ) )
	window.ui.volumeEffectsSlider.setValue(int(volumeEffectsValue) )
	window.ui.volumeEffectsSlider.valueChanged.connect(window.volumeEffectsUpdate)

	window.ui.lightningDelayMinSpinbox.setValue(float(settings["delays"]["lightningdelaymin"] ) )
	window.ui.lightningDelayMaxSpinbox.setValue(float(settings["delays"]["lightningdelaymax"] ) )
	window.ui.thunderDelayMinSpinbox.setValue(float(settings["delays"]["thunderdelaymin"] ) )
	window.ui.thunderDelayMaxSpinbox.setValue(float(settings["delays"]["thunderdelaymax"] ) )

	window.show()
	
	sys.exit(app.exec() )