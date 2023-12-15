import pandas as pd
import os

def open_excel(year, month, location):
    path = os.path.dirname(os.path. dirname(os.path.abspath(__file__)))

    # 엑셀 파일 불러오기
    file_path = path + "/data/" + str(year) + "년 " + str(month) + "월.xlsx"
    data = pd.ExcelFile(file_path)
    read_data = pd.read_excel(data, engine = "openpyxl", usecols=[0, 1, 2, 3, 4, 7])

    #필요한 데이터만 선택
    condition = (read_data["측정소코드"] == location)
    o3_data = read_data.loc[condition, ["측정일시", "O3"]]
    o3_data.fillna(float(0))
    data_list = o3_data.to_dict('records')
    
    return data_list