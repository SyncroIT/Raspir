opts = {
	#This is the default input that Raspberry receives by your IR receiver while there's no IR light pointed at. In my case it's 1.
	'defaultInput': 1, 

	#This is the amount of inputs equal to defaultInput to achieve to make Raspberry know that IR signal is ended. 
	'defaultCycles': 10000,

	#It's the GPIO pin where there's connected your IR receiver. NB: GPIO.BOARD numeration used.
	'signalPin': False,

	#It should be a number equal to 1/10 of defaultCycles. It's not random and if changed it will also make change the result of decoding operation.
	#It's used to mark a number as true or not (x < divider)
	'divider': 1000,

	#It's the amount of milliseconds to distinguish a new signal from the last one
	#Every signal sent after another one, in this timing will be treated as a copy of the last one.
	'floodInterval': 250
}

def setup(**options):
	for(name) in options:
		opts[name] = options[name]

