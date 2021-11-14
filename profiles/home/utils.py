from .constants import STATIC_PATH
import random
import os


def file_handler(file, static_dir='files/') -> str:
	"""
		the file parameter is a file object while the static_dir is the directory
		inside the static directory that the file will be created in.
		the file name will be the sum of all characters in the current file name
		returns the file name
	"""
	static_dir_path = os.path.join(STATIC_PATH, static_dir)
	file_name = str(random.randint(0, 9999999))
	file_path = os.path.join(static_dir_path, file_name)
	while os.path.exists(file_path):
		file_name = str(random.randint(0, 9999999))
		file_path = os.path.join(static_dir_path, file_name)
	with open(file_path, 'wb+') as dest:
		for chunk in file.chunks():
			dest.write(chunk)
	return file_name