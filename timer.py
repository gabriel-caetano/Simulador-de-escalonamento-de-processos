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
		self.__interruptions = sorted(self.__interruptions, key=lambda k: k['time'])


	def getInterr(self):
		if len(self.__interruptions):
			if self.__time >= self.__interruptions[0]['time']:
				interr = self.__interruptions[0]
				if self.__interruptions[0]['type'] == 0:
					self.__interruptions.pop(0)
				else:
					updated_time = self.__interruptions[0]['freq'] + self.__time
					self.__interruptions[0]['time'] = updated_time
					self.__interruptions = sorted(self.__interruptions, key=lambda k: k['time'])
				return interr['code']
		return 0
