from src.FileStatus import FileStatus


class FileInfo:

	def __init__(self, _status: FileStatus = None, _path: str = None):
		self.status = _status
		self.path = _path

	def get_lender_num(self) -> str:
		strs = self.path.split('~')
		return strs[1].strip()

