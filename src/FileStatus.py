from enum import Enum


class FileStatus(Enum):
	CONT_WITH_CURR_PERSON = 1
	MOVE_TO_NEXT_PERSON = 2
	FINISHED = 3