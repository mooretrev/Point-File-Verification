from src.Input import Input
from src.AHKFunction import AHKFunction
from src.FileHandler import FileInfo, FileStatus, FileHandler
import time


class Point:

    def __init__(self, _file_handler:FileHandler):
        self.input = Input()
        self.file_name = None
        self.category = None
        self.type = None
        self.ahk = AHKFunction()
        self.ahk.activate_point()
        self.file_hander = _file_handler

    def __str__(self):
        return 'category: {} type: {}'.format(self.category, self.type)

    def read_file_name(self):
        self.file_name = self.ahk.get_file_name().lower()

    def analyze_file_name(self):
        for r in range(self.input.master_list.shape[0]):
            for c in range(2, self.input.master_list.shape[1]):
                if self.input.master_list.iloc[r, c] is not None:
                    if str(self.input.master_list.iloc[r, c]) in self.file_name:
                        self.category = self.input.master_list.iloc[r, 0]
                        self.type = self.input.master_list.iloc[r, 1]
                        return None
        self.type = 'Miscellaneous All'

    def select_category(self):
        self.ahk.input_category(self.category)

    def select_type(self):
        self.ahk.input_type(self.type)

    def reset(self):
        self.file_name = None
        self.category = None
        self.type = None

    def protected_pdf_screen_up(self) -> bool:
        return self.ahk.protected_pdf_screen()

    def loading_screen_up(self) -> bool:
        return self.ahk.loading_screen()

    def document_info_screen_up(self) -> bool:
        return self.ahk.document_info_screen()

    def document_manager_screen_up(self) -> bool:
        return self.ahk.document_manager_screen()

    def main_screen_up(self) -> bool:
        return self.ahk.main_screen()

    def reload(self, file_info: FileInfo):
            self.change_person(file_info)

    def add_files(self, path):
        self.wait_for_doc_manager()
        self.ahk.add_files(path)
        self.clear_errors()

    def wait_for_doc_manager(self):
        while not self.document_manager_screen_up():
            time.sleep(2)
            print('waiting for doc manager')

    def clear_errors(self):
        i = 0
        while not self.document_info_screen_up():
            self.ahk.clear_errors()

            if self.protected_pdf_screen_up():
                self.close_protected_pdf_error()

            if self.ahk.close_word_error():
                self.ahk.close_word_error()

            time.sleep(5)

            if not self.ahk.adding_files_screen():
                # only start count error cycles if the file window has responded
                i += 1

            if i >= 9:
                # error cleaning has failed, moving to the next person
                file_info = self.file_hander.move_to_next_person()
                self.reload(file_info)

    def close_protected_pdf_error(self):
        self.ahk.close_protected_pdf_error()

    def close_document_manager(self):
        print('close document manager')
        self.ahk.close_document_manager()

    def open_document_manager(self):
        self.ahk.open_document_manager()

    def change_person(self, file_info):
        self.ahk.close_document_manager()
        self.ahk.close_point_file()
        self.ahk.save_point_file()
        time.sleep(2)
        self.open_person(file_info)

    def open_person(self, file_info:FileInfo):
        self.ahk.open_file_explorer(file_info.path)
        self.ahk.open_point_file(file_info.get_lender_num())
        self.ahk.open_document_manager()
        time.sleep(2)

    def remove_upload_error(self):
        self.ahk.remove_upload_error()

    def verify_file(self, person):
        self.ahk.verify_file(person)



