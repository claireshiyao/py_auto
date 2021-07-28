import os

def anaysis_data():
    test_times = []
    # 打开data.log文件
    with open(os.getcwd() + "/data.log") as fs:
        for line in fs.readlines():  # 按行读取
            temp = line.strip("\n").split(",") # 去掉换行符之后，再按,分割
            print("temp",temp)
            if temp[-1] == str(0): # 筛选success字段为0的TestTime
                test_times.append(int(temp[-2]))

    if len(test_times) > 0:
        avg_time = sum(test_times) / len(test_times) # 平均值
        max_time = max(test_times)
        min_time = min(test_times)
        print("最大的TestTime: ",max_time,",最小的TestTime: ",min_time,",平均TestTime: ",avg_time)


if __name__ == '__main__':
    anaysis_data()