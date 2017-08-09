import math
import time
import config

class Decoder:
	recorded = []
	lastDecode = False
	lastDecodeTime = time.time()

	def record(self, value):
		self.recorded.append(value)

	def decode(self):
		ms = time.time()*1000
		if(self.lastDecodeTime and (ms-self.lastDecodeTime) > config.floodInterval):
			binary = []
			for (timing) in self.recorded:
				binary.append(int(timing > config.divider))
			self.lastDecode = int("".join(map(str, binary)),2)%10000

		self.lastDecodeTime = ms
		return self.lastDecode

	def reset(self):
		self.recorded = []