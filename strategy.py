from abc import ABC , abstractmethod

class TellCenter:
	def __init__(self, city, tell):
		self._city = city
		self.tell = tell
	
	@property
	def city(self):
		return self._city

	@city.setter
	def city(self, the_city):
		self._city = the_city

	def save_tell(self):
		return self.city.set_prefixe(self.tell)

# ------------------------------ #

class GeneratePrefixe(ABC):
	@abstractmethod
	def set_prefixe(self, tell):
		pass

class Kish(GeneratePrefixe):
	def set_prefixe(self, tell):
		return f'076{tell}'

class Tehran(GeneratePrefixe):
	def set_prefixe(self, tell):
		return f'021{tell}'

# ------------------------------ #

t1 = TellCenter(Tehran(),'999999')
print(t1.save_tell())
