# Raspir
A simple Python library to detect IR receivers signal

### Installation
It's quite easy to start using this library.
You can download it by using `pip` / `pip3` package manager.

```
pip3 install raspir
```

After this, just import the library in your Python file: 

```
from raspir import raspir
```

### Get started
To start using this library you should first configure it, you can setup your Raspir by using:

```
# GPIO.BOARD numeration used
raspir.setup(signalPin=YOUR_SIGNAL_PIN)
raspir.listen(YOUR_CALLBACK)
```

`raspir.setup(**values)` accepts more than one option, but I suggest you to don't edit other options if it's not necessary. 

`raspir.listen(callback)` will call your callback by passing in the value received from your sensor.


#### Fast example

```
from raspir import raspir
raspir.setup(signalPin=3)
raspir.listen(print)
```

Now it will print every IR signal received by the sensor.

### Options
- defaultInput (default: 1)

It's the input that your Raspberry will usually receive when there's not an infrared light pointed to the sensor.

- defaultCycles (default: 10000)

When a signal is received, Raspberry doesn't know when signal transmission ends. So it will wait to receive the defaultValue so many times as much is written in defaultCycles value. If the script is not working you can try to change this value according to your CPU frequency. 

- signalPin (default: False)

This value is required to start using the script.
It's the PIN number where Raspberry needs to listen for signal. It must be expressed as GPIO.BOARD number (not BCM!)

- divider (default: 1000)

It's used to mark some numbers as true or not. Change it only if your code is not working with default value. Changing this parameter will change the decoding process, so it will change the final result.

- floodInterval (default: 250)

It's the amount of milliseconds after receiving a signal in which Raspberry will consider all other signals received as a copy of the last one.  


### How to contribute
- Open a new branch for every feature / fix you're coding!
- Take a minute to think what you're next to do
- Take another minute
- Just a little bit more..
- Now you're ready
- Write your feature and, if possible, test it on a Raspberry
- Make a pull request to this repository
