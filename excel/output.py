import pandas as pd
import os

def write_excel(result):
    df = pd.DataFrame(result, columns =['월','기준치 초과일수'])
    path = os.path.dirname(os.path. dirname(os.path.abspath(__file__)))

    file_path = path + "/result/" + "result.xlsx"

    #엑셀 파일에 데이터 입력
    excel_writer = pd.ExcelWriter(file_path, engine='xlsxwriter')
    df.to_excel(excel_writer, index=False)
    excel_writer.close()

    return True