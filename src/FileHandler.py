import os
from src.Input import Input
from src.FileStatus import FileStatus
from src.FileInfo import FileInfo
import shutil
from src.Log import Log


class FileHandler:
	def __init__(self, base=None, person=None):
		self._in = Input()
		self.file = None
		self.status = FileStatus.CONT_WITH_CURR_PERSON
		self.cur_person = None
		self.log = Log()

		if base is None:
			self.base_dir = self._in.base_dir
		else:
			self.base_dir = base

		self.people = self.ls(self.base_dir)

		if person is None:
			self.set_cur_person()
		else:
			self.cur_person = person

	def get_file_path(self):
		if self.file is None:
			return None
		if self.file[0] != '\\':
			return self.get_current_person_path() + '\\' + self.file
		else:
			return self.get_current_person_path() + self.file

	def ls(self, path) -> list:
		path = os.listdir(path)
		path.sort()
		return path

	def remove(self):
		try:
			os.remove(self.get_file_path())
		except FileNotFoundError:
			self.auto_complete_remove()

	def auto_complete_remove(self):
		self.file = self.remove_extension(self.file)
		files = self.ls_person()
		lowered_files = self.lower_list(files)

		for i in range(len(files)):
			if self.file in lowered_files[i]:
				self.file = files[i]
				os.remove(self.get_file_path())

	def create_file_path(self, file):
		if file[0] == '\\':
			return self.get_current_person_path() + file
		else:
			return self.get_current_person_path() + '\\' + file

	def set_cur_person(self):
		if self.ls(self.base_dir) == []:
			self.status = FileStatus.FINISHED
			exit(1)

		elif self.cur_person is None:
			self.cur_person = '\\' + self.people[0]

	def determine_directory_status(self):
		if self.directory_finished(self.ls_person()):
			self.move_to_next_person()
			self.log.move_person(self.cur_person)
		else:
			self.status = FileStatus.CONT_WITH_CURR_PERSON
			self.log.cont_person(self.cur_person)

		return FileInfo(self.status, self.get_current_person_path())

	def set_cur_person(self):
		if not self.people == 0:
			person = self.people[0]
		else:
			exit(1)

		if person[0] == '\\':
			self.cur_person = person
		else:
			self.cur_person = '\\' + person

	def move_to_next_person(self):
		self.move_folder(self.get_current_person_path(), r'C:\Users\trevormoore\Dropbox (Home USA Mortgage)\Home USA Mortgage Team Folder\Special projects\Verfied')
		self.people.pop(0)
		self.set_cur_person()
		self.status = FileStatus.MOVE_TO_NEXT_PERSON

	def move_folder(self, target, des):
		try:
			shutil.move(target, des)
		except PermissionError:
			print('error in moving the folder')

	def delete(self, list):
		for item in list:
			self.file = item
			self.remove()

	def get_current_person_path(self) -> str:
		if self.cur_person[0] == '\\':
			return self.base_dir + self.cur_person
		else:
			return self.base_dir + '\\' + self.cur_person

	def get_file_path(self):
		out = self.get_current_person_path()

		if self.file[0] == '\\':
			return out + self.file
		else:
			return out + '\\' + self.file

	def separate_file_extension(self, files=None, return_extensions=False) -> list:
		res = []
		for file in files:
			res.append(self.remove_extension(file, return_extensions))
		return res

	def remove_extension(self, file, return_extension=False):
		file_name_split = file.split('.')
		if return_extension:
			return file_name_split[len(file_name_split) - 1]
		else:
			return file_name_split[0]

	def directory_finished(self, files):
		return True

	def ls_person(self):
		return self.ls(self.get_current_person_path())

	def lower_list(self, list):
		out = []
		for item in list:
			out.append(item.lower())

		return out
