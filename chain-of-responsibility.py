from abc import ABC, abstractmethod

class AbstractUser(ABC):
	def __init__(self, successor):
		self._successor = successor

	def handle(self, request):
		handled = self.login(request)
		if not handled :
			self._successor.handle(request)

	@abstractmethod
	def login(self, username):
		pass

# ------------------------------- #

class Admin(AbstractUser):
	def login(self,username):
		if username == 'admin' :
			print('login by Admin')
			return True

class Operator(AbstractUser):
	def login(self, username):
		if username == 'operator' :
			print('login by operator')
			return True

class Guest(AbstractUser):
	def login(self, username):
		print('login by guest')
		return True

# ------------------------------- #

class Client :
	def __init__(self):
		self.handler = Admin(Operator(Guest(None)))

	def delegate(self, requests):
		for request in requests :
			self.handler.handle(request)

# --------------------------------- #

all_requests = ['admin','charlie','operator','john']

c1 = Client()
c1.delegate( all_requests )
