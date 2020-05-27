import time

from src.FileHandler import FileHandler
from src.Point import Point
from src.FileInfo import FileInfo
from src.FileStatus import FileStatus

if __name__ == '__main__':
	file_handler = FileHandler()
	point = Point(file_handler)

	if not point.document_manager_screen_up():
		path = file_handler.get_current_person_path()
		file_info = FileInfo(FileStatus.CONT_WITH_CURR_PERSON, path)
		point.open_person(file_info)

	while True:
		time.sleep(2)
		print(file_handler.cur_person[1:])
		point.verify_file(file_handler.cur_person[1:])
		file_info = file_handler.determine_directory_status()
		point.reload(file_info)

