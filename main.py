from calculation.calc import control_data
from excel.input import open_excel
from excel.output import write_excel

def main():
    year = 2022
    result = []
    for month in range(1, 12):
        data = open_excel(2022, month)

        # 계산하는 function 호출
        count = 1

        result.append([str(month) + "월", count])

    success = write_excel(result)
    if success == True:
        print("success!")
    else:
        print("fail...")
    
if __name__ == '__main__':
    main()