import os

def connect():
	try:
		import config
	except ImportError:
		print("config file does not exist")
	if not hasattr(config, 'PORT'): 
		print('PORT not set')
	else:
		os.system('''sudo mpfshell -c "open {}"'''.format(config.PORT))