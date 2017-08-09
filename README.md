# Raspir
A simple Python library to detect IR receivers signal

### Get started
It's so easy to start using this library, just download it and follow next steps:
- Open file "config.py" and set your PIN where you should receive signal from IR receiver (GPIO.BOARD numeration system used!)
- Leave other parameters as they are and adjust them only if the script is not working
- Create a Python file, it will be **yours**
- Write your script to listen the IR receiver inside the file, like in the following example:

```
import sys
sys.path.append('../') # Here goes your path to the library 
from raspir import listen 

listen(printResult) # It's the call to the entry point function

# That's the function you could use as a callback. 
# It should receive a parameter that will contain the detected input signal (result)
def printResult(result): 
	print(result)
```

### How to contribute
- Open a new branch for every feature / fix you're coding!
- Take a minute to think what you're doing
- Take another minute
- Just a little bit more..
- Now you're ready
- Write your feature and, if possible, test it on a Raspberry
- Make a pull request to this repository
