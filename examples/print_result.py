import sys
sys.path.append('../')
from raspir import listen

listen(printResult)
def printResult(result):
	print(result)
