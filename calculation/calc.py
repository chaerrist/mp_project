import calendar
import numpy as np

def calc_data(day_list):
    count = 0
    standard = 0.06     #오존 농도 8시간 기준치
    
    #데이터를 일자별로 계산, 기준치를 넘어가는 날짜가 있다면 count에 +1
    for i in day_list :
        flag = False
        while True :
            for hour in range(17):
                daytime = i[hour:(hour+8)]
                mean_data = np.mean(daytime)
                if mean_data > standard :
                    count += 1
                    flag = True
                    break
                flag = True
            if flag :
                break
                
    return count

def control_data(year, month, data):
    weekday, days = calendar.monthrange(year, month)
    day_list = []
    
    #데이터 중 오존 값만 추출
    o3_data = [ d["O3"] for d in data ]
    
    #데이터를 일자별로 슬라이스
    for date in range(1, days + 1):
        start = (date - 1)*24
        end = start + 24        
        day_list.append(o3_data[start:end])       

    #슬라이스 된 데이터를 계산
    result = calc_data(day_list)

    return result