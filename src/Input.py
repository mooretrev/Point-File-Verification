from openpyxl import load_workbook
from src.ImportantCoordinates import ImportantCoordinates
import pandas as pd


class Input:

    def __init__(self):
        wb = load_workbook(filename='../data/Master Table.xlsx')
        ws = wb['Sheet1']
        df = pd.DataFrame(ws.values)
        self.special_project_dir = df.iloc[0,0]
        self.base_dir = self.special_project_dir + '\\Cleaned'
        self.done_dir = self.special_project_dir + '\\Done'
        df = df.drop(0, 0)
        self.coords = ImportantCoordinates(df.iloc[1, 0], df.iloc[2, 0], df.iloc[1, 1], df.iloc[2, 1], df.iloc[1, 2], df.iloc[2, 2], df.iloc[1, 3],
                                          df.iloc[2, 3], df.iloc[1, 4],
                                          df.iloc[2, 4], df.iloc[1, 5],
                                          df.iloc[2, 5], df.iloc[1, 6],
                                          df.iloc[2, 6], df.iloc[1, 7],
                                          df.iloc[2, 7], df.iloc[1, 8],
                                          df.iloc[2, 8], df.iloc[1, 9],
                                          df.iloc[2, 9], df.iloc[1, 10],
                                          df.iloc[2, 10], df.iloc[1, 11],
                                          df.iloc[2, 11], df.iloc[1, 12],
                                          df.iloc[2, 12], df.iloc[1, 13],
                                          df.iloc[2, 13], df.iloc[1, 14],
                                          df.iloc[2, 14], df.iloc[1, 15],
                                          df.iloc[2, 15], df.iloc[1, 16],
                                          df.iloc[2, 16], df.iloc[1, 17],
                                          df.iloc[2, 17], df.iloc[1, 18],
                                          df.iloc[2, 18], df.iloc[1, 19],
                                          df.iloc[2, 19], df.iloc[1, 20],
                                          df.iloc[2, 20], df.iloc[1, 21],
                                          df.iloc[2, 21], df.iloc[1, 22],
                                          df.iloc[2, 22], df.iloc[1, 23],
                                          df.iloc[2, 23])
        self.master_list = df.iloc[3:, :]
        self.master_list = self.master_list.reset_index()
        self.master_list = self.master_list.drop('index', 1)



