from calculation.calc import control_data
from excel.input import open_excel
from excel.output import write_excel

def main():
    year = 2022
    # 측정소 코드 입력
    location = 831151
    result = []
    for month in range(1, 13):
        data = open_excel(year, month, location)

        # 계산하는 function 호출
        count = control_data(year, month, data)

        result.append([str(month) + "월", count])

    #실행 결과를 파일에 입력
    success = write_excel(result)

    if success == True:
        print("success!")
    else:
        print("fail...")

if __name__ == '__main__':
    main()