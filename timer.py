from operator import itemgetter

class Timer:
	def __init__(self):
		self.__time = 0
		self.__interruptions = []

	def increment(self):
		self.__time += 1
	
	def getTime(self):
		return self.__time

	def newInterr(self, inter_type, code, time, freq = 0):
		interruption = {
			"type": inter_type,
			"code": code,
			"freq": freq,
			"time": freq + self.__time if freq > 0 else time + self.__time
		}
		self.__interruptions.append(interruption)
		print(self.__interruptions)
		self.__interruptions = sorted(self.__interruptions, key=lambda k: k['time'])
		print(self.__interruptions)


	def getInterr(self):
		return self.__interruptions
		if self.__time == self.__interruptions[0]['time']:
			if self.__interruptions[0]['type'] == 0:
				return self.__interruptions.pop(0)['code']
			else:
				interr = self.__interruptions.pop(0)
				interr['time'] = interr['freq'] + self.__time
				self.__interruptions.append(interr)
				self.__interruptions = sorted(self.__interruptions, key=lambda k: k['time'])
				return interr['code']
		return 0

new = Timer()
new.newInterr(0, 5, 3)
new.newInterr(0, 4, 10)
new.newInterr(0, 5, 7)
new.newInterr(0, 5, 1)
new.newInterr(1, 5, 0, 3)
new.newInterr(1, 5, 0, 6)
new.newInterr(1, 5, 0, 5)

# new.getInterr()