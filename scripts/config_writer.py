import os

CUR_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(CUR_DIR, 'config.py')

def write_config(key, value):
	if not os.path.isfile(CONFIG_PATH):
		with open(CONFIG_PATH, 'w') as conf:
			conf.write("CONFIG_PATH='{}'\n".format(CONFIG_PATH))

	if key=='PORT':
		value = os.path.basename(value)

	with open(CONFIG_PATH, 'a') as conf:
		conf.write("{}='{}'\n".format(key, value))