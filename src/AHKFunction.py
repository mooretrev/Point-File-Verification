from ahk import AHK
from src.Input import Input
import pyperclip

class AHKFunction:

    def __init__(self):
        self.ahk = AHK(executable_path=r'C:\Program Files\AutoHotkey\AutoHotkey.exe')
        self._in = Input()
        self.manager_title = 'Document Management'
        self.document_view_title = 'Document Information Preview'
        self.loading_title = 'Point Data Server'
        self.secured_pdf_title = 'Warning: Secured PDF'
        self.word_error_title = 'Word Version Not Supported'
        self.adding_files_screen_title = 'Add Document'
        self.main_screen_title = 'Point'
        self.coords = self._in.coords

    def point_main_screen_open(self) -> bool:
        windows = self.list_windows_names()
        for window in windows:
            if window == "Point":
                return True
        return False

    def list_windows_names(self) -> list:
        script = """
            WinGet windows, List
            Loop %windows%
            {
                id := windows%A_Index%
                WinGetTitle wt, ahk_id %id%
                r .= wt . "`n"
            }
            clipboard := ""
            clipboard := r
            ClipWait
        """
        self.ahk.run_script(script)
        windows = pyperclip.paste()
        list = windows.split('\n')
        return AHKFunction.remove_empty_indexs(list)

    @staticmethod
    def remove_empty_indexs(list:list) -> list:
        i = len(list) - 1
        while i >= 0:
            if list[i] == '':
                list.pop(i)
            i = i - 1
        return list


    def activate_point(self):
        script = 'WinActivate, Document Information Preview'
        self.ahk.run_script(script)

    def get_file_name(self):
        script = """
            WinActivate, Document Information Preview   
            MouseClickDrag, left, {}, {}, {}, {}
            Sleep, 400
            sendinput, ^c
            ClipWait
            return
        """.format(self.coords.start_drag.x, self.coords.start_drag.y, self.coords.end_drag.x, self.coords.end_drag.y)
        self.ahk.run_script(script)
        text = pyperclip.paste()
        return text

    def input_category(self, str):
        if str is not None:
            script = """
                WinActivate, Document Information Preview   
                MouseClick, left, {}, {}
                Send {}{{return}}
                return
                """.format(self.coords.category.x, self.coords.category.y, str)

            self.ahk.run_script(script)

    def input_type(self, str):
        script = """
            WinActivate, Document Information Preview
            MouseClick, left, {}, {}
	        Send {}{{return}}
            """.format(self.coords.type.x, self.coords.type.y, str)
        self.ahk.run_script(script)

    def add_files(self, path):
        script = """
            Sleep, 1000
            WinActivate, Document Management
            Sleep, 2000
            
            MouseClick, left, {}, {}
            Sleep, 1000
            MouseClick, left, {}, {}
            Sleep, 1000
            MouseClick, left, {}, {}
            Sleep, 400
            Send % "{}"
            Send, {{enter}}
            Sleep, 1000
            MouseClick, left, {}, {}
            Sleep, 1000
            sendinput, ^a
            Sleep, 1000
            MouseClick, left, {}, {}
            Sleep, 1000
        """.format(self.coords.add_file_button.x, self.coords.add_file_button.y, self.coords.ok_button.x, self.coords.ok_button.y, self.coords.file_url.x, self.coords.file_url.y, path, self.coords.first_file.x, self.coords.first_file.y, self.coords.add_button.x, self.coords.add_button.y)
        self.ahk.run_script(script)

    def clear_errors(self):
        script = 'MouseClick, left, {}, {}\nSleep, 500'.format(self.coords.clear_error.x, self.coords.clear_error.y)
        self.ahk.run_script(script)

    def close_document_manager(self):
        script = """
                    WinActivate, Document Management
                    Sleep, 1000

                    MouseClick, left, {}, {}
                    Sleep, 1000
            """.format(self.coords.doc_manager_exit.x, self.coords.doc_manager_exit.y)
        self.ahk.run_script(script)


    def close_point_file(self):
        script = """
            Sleep, 1000
        
            MouseClick, left, {}, {}
            Sleep, 1000
        
            MouseClick, left, {}, {}
            Sleep, 1000
        """.format(self.coords.file_menu.x, self.coords.file_menu.y, self.coords.close_file.x, self.coords.close_file.y)
        self.ahk.run_script(script)

    def open_point_file(self, loan_number):
        script = """
        Sleep, 1000
        WinActivate, Point
        Sleep, 2000

        MouseClick, left, {}, {}
        Sleep, 1000
    
        MouseClick, left, {}, {}
        Sleep, 1000
    
        MouseClick, left, {}, {}, 2
        Sleep, 1000
    
        Send, {}
        Sleep, 1000
    
        MouseClick, left, {}, {}
        Sleep, 5000
    
        MouseClick, left, {}, {}
        Sleep, 200
        MouseClick, left, {}, {}
        Sleep, 5000
        """.format(self.coords.advance_search.x, self.coords.advance_search.y, self.coords.select_all.x, self.coords.select_all.y, self.coords.search_bar.x, self.coords.search_bar.y, loan_number, self.coords.search_button.x, self.coords.search_button.y, self.coords.file.x, self.coords.file.y, self.coords.file.x, self.coords.file.y)
        self.ahk.run_script(script)

    def open_document_manager(self):
        script = """
        Sleep, 2500
        MouseClick, left, {}, {}
        Sleep, 2500
        MouseClick, left, {}, {}
        Sleep, 1000
        """.format(self.coords.doc_menu.x, self.coords.doc_menu.y, self.coords.doc_manager_button.x, self.coords.doc_manager_button.y)
        self.ahk.run_script(script)

    def save_point_file(self):
        script = """
            WinActivate, Point
            Sleep, 1000
            """
        self.ahk.run_script(script)

        if self.save_point_file_screen():
            script = """
                MouseClick, left, {}, {}
                Sleep, 5000
            """.format(self.coords.save_button.x, self.coords.save_button.y)
            self.ahk.run_script(script)

    def close_protected_pdf_error(self):
        script = """
        Sleep, 1000
        WinActivate, Warning: Secured PDF
        MouseClick, left, {}, {}
        """.format(self.coords.close_protected_pdf.x, self.coords.close_protected_pdf.y)
        self.ahk.run_script(script)

    def close_word_error(self):
        script = """
        Sleep, 1000
        WinActivate, Word Version Not Supported
        MouseClick, left, {}, {}
        """.format(self.coords.close_word_error.x, self.coords.close_word_error.y)
        self.ahk.run_script(script)

    def remove_upload_error(self):
        script = """
        WinGetActiveStats, Title, Width, Height, X, Y

        if (Width == 835){{
            MouseClick, left, {} , {}
        }} 
        """.format(self.coords.upload_error.x, self.coords.upload_error.y)
        self.ahk.run_script(script)


    def loading_screen(self) -> bool:
        script = """
            clipboard := ""
            clipboard := WinExist("{}")
            ClipWait
        """.format(self.loading_title)
        self.ahk.run_script(script)
        results = pyperclip.paste()
        return results != '0x0'

    def document_info_screen(self) -> bool:
        script = """
                    clipboard := ""
                    clipboard := WinExist("{}")
                    ClipWait
                """.format(self.document_view_title)
        self.ahk.run_script(script)
        results = pyperclip.paste()
        return results != '0x0'

    def document_manager_screen(self) -> bool:
        script = """
                    clipboard := ""
                    clipboard := WinExist("{}")
                    ClipWait
                """.format(self.manager_title)
        self.ahk.run_script(script)
        results = pyperclip.paste()
        return results != '0x0'

    def protected_pdf_screen(self) -> bool:
        script = """
                            clipboard := ""
                            clipboard := WinExist("{}")
                            ClipWait
                        """.format(self.secured_pdf_title)
        self.ahk.run_script(script)
        results = pyperclip.paste()
        return results != '0x0'

    def word_error_screen(self) -> bool:
        script = """
                            clipboard := ""
                            clipboard := WinExist("{}")
                            ClipWait
                        """.format(self.word_error_title)
        self.ahk.run_script(script)
        results = pyperclip.paste()
        return results != '0x0'

    def adding_files_screen(self) -> bool:
        script = """
                            clipboard := ""
                            clipboard := WinExist("{}")
                            ClipWait
                        """.format(self.adding_files_screen_title)
        self.ahk.run_script(script)
        results = pyperclip.paste()
        return results != '0x0'

    def main_screen(self) -> bool:
        script = """
                            clipboard := ""
                            clipboard := WinExist("{}")
                            ClipWait
                        """.format(self.main_screen_title)
        self.ahk.run_script(script)
        results = pyperclip.paste()
        return results != '0x0'

    def save_point_file_screen(self) -> bool:
        windows = self.list_windows_names()
        for window in windows:
            if window == 'Point':
                return True
        return False

    def verify_file(self, person):
        script = """
        MsgBox, Verify File
        
        WinClose, {}
        """.format(person)
        self.ahk.run_script(script)

    def open_file_explorer(self, path):
        script = """
            MyVar := "{}"
            Run, explore %MyVar%
            Sleep, 1000
            WinActivate, Point
            """.format(path)
        self.ahk.run_script(script)

