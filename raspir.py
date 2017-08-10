from . import config
from . import decoder
from datetime import datetime
import RPi.GPIO as GPIO

def setup(**options):
	return config.setup(**options)

def listen(callback):
	try:

		if(not config.opts['signalPin']):
			raise Exception('You should set your signal PIN by using setup() function before listening')
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(config.opts['signalPin'], GPIO.IN)

		dec = decoder.Decoder()
		while True:
			defaultCycles = 0
			value = config.opts['defaultInput']

			while(value == config.opts['defaultInput']):
				value = (GPIO.input(config.opts['signalPin']))

			lastTime = datetime.now()
			previousValue = value

			while True:
				if(previousValue != value):
					diff = datetime.now()-lastTime
					dec.record((datetime.now()-lastTime).microseconds)
					lastTime = datetime.now()

				previousValue = value

				if(value == config.opts['defaultInput']):
					defaultCycles = defaultCycles+1
				
				if(defaultCycles > config.opts['defaultCycles']):
					result = dec.decode()
					dec.reset()
					callback(result)
					break

				value = GPIO.input(config.opts['signalPin'])
	finally:
		GPIO.cleanup()
