class ImportantCoordinates:
    def __init__(self, _start_drag_x, _start_drag_y, _end_drag_x, _end_drag_y, _cat_x, _cat_y, _type_x,    _type_y,_add_file_x, _add_file_y, _ok_button_x, _ok_button_y, _file_url_x, _file_url_y, _first_file_x, _first_file_y, _add_button_x, _add_button_y, _clear_error_x, _clear_error_y,_doc_close_x, _doc_close_y,_file_menu_x, _file_menu_y,_close_file_x, _close_file_y,_advance_search_x, _advance_search_y,_select_all_x, _select_all_y,_search_bar_x, _search_bar_y, _search_button_x, _search_button_y, _file_x, _file_y,_doc_menu_x, _doc_menu_y,_doc_manager_button_x, _doc_manager_button_y,_save_button_x, _save_button_y,_close_protect_x, _close_protect_y,_close_word_x, _close_word_y, _upload_error_x, _upload_error_y):

        self.start_drag = Coordinates(_start_drag_x, _start_drag_y)
        self.end_drag = Coordinates(_end_drag_x, _end_drag_y)
        self.category = Coordinates(_cat_x, _cat_y)
        self.type = Coordinates(_type_x, _type_y)
        self.add_file_button = Coordinates(_add_file_x, _add_file_y)
        self.ok_button = Coordinates(_ok_button_x, _ok_button_y)
        self.file_url = Coordinates(_file_url_x, _file_url_y)
        self.first_file = Coordinates(_first_file_x, _first_file_y)
        self.add_button = Coordinates(_add_button_x, _add_button_y)
        self.clear_error = Coordinates(_clear_error_x, _clear_error_y)
        self.doc_manager_exit = Coordinates(_doc_close_x, _doc_close_y)
        self.file_menu = Coordinates(_file_menu_x, _file_menu_y)
        self.close_file = Coordinates(_close_file_x, _close_file_y)
        self.advance_search = Coordinates(_advance_search_x, _advance_search_y)
        self.select_all = Coordinates(_select_all_x, _select_all_y)
        self.search_bar = Coordinates(_search_bar_x, _search_bar_y)
        self.search_button = Coordinates(_search_button_x, _search_button_y)
        self.file = Coordinates(_file_x, _file_y)
        self.doc_menu = Coordinates(_doc_menu_x, _doc_menu_y)
        self.doc_manager_button = Coordinates(_doc_manager_button_x, _doc_manager_button_y)
        self.save_button = Coordinates(_save_button_x, _save_button_y)
        self.close_protected_pdf = Coordinates(_close_protect_x, _close_protect_y)
        self.close_word_error = Coordinates(_close_word_x, _close_word_y)
        self.upload_error = Coordinates(_upload_error_x, _upload_error_y)


class Coordinates:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

    def __str__(self):
        return 'x: {} y: {}'.format(self.x, self.y)