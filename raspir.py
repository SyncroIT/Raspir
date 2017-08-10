from . import config
from . import decoder
from datetime import datetime
import RPi.GPIO as GPIO


def listen(callback):
	try:
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(config.signalPin, GPIO.IN)

		dec = decoder.Decoder()
		while True:
			defaultCycles = 0
			value = config.defaultInput

			while(value == config.defaultInput):
				value = (GPIO.input(config.signalPin))

			lastTime = datetime.now()
			previousValue = value

			while True:
				if(previousValue != value):
					diff = datetime.now()-lastTime
					dec.record((datetime.now()-lastTime).microseconds)
					lastTime = datetime.now()

				previousValue = value

				if(value == config.defaultInput):
					defaultCycles = defaultCycles+1
				
				if(defaultCycles > config.defaultCycles):
					result = dec.decode()
					dec.reset()
					callback(result)
					break

				value = GPIO.input(config.signalPin)
	finally:
		GPIO.cleanup()
