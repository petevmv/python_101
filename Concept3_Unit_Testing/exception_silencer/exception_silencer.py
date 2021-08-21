class ExceptionSilencer:

	def __init__(self, exception_to_silance):
		self.exception_to_silance = exception_to_silance

	def __enter__(self):
		print('enter method')

	def __exit__(self, exc_type, exc_value, traceback):
		print('exit method')
		if exc_type is self.exception_to_silance:	
			print(exc_type)
			return True



# with ExceptionSilencer(ValueError):
#     int("aa")
# print("We can reach this point, because the exception was not propagated")


# with ExceptionSilencer(Exception):
# 	int('aa')

# print("We cannot reach this point, because the exception was propagated")