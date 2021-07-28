# author by claire

f = open('data.log', encoding='utf-8')
lines = f.readlines()

# print(lines)
# # ['TestID,TestTime,Success\n', '0,149,0\n', '1,69,0\n', '2,45,0\n', '3,18,1\n', '4,18,1']

new_lines = []
for line in lines:
    new_line = line.rstrip()
    new_lines.append(new_line)
print(new_lines)
# ['TestID,TestTime,Success', '0,149,0', '1,69,0', '2,45,0', '3,18,1', '4,18,1']

log_data = []
header = new_lines[0].split(',')  # ['TestID', 'TestTime', 'Success']
for row in new_lines[1:]:
    row_list = row.split(',')
    lines_to_dict = dict(zip(header, row_list))
    log_data.append(lines_to_dict)
print(log_data)

success_log = []
for log_row in log_data:
    if log_row['Success'] == '0':
        success_log.append(log_row)
print(success_log)

test_time = []
for log_row in success_log:
    test_time_value = log_row['TestTime']
    test_time.append(test_time_value)
print(test_time)
# print(len(test_time))

max = int(test_time[0])
for num in test_time:
    if int(num) > max:
        max = int(num)
print(max)  # 打印最大TestTime

min = int(test_time[0])
for num in test_time:
    if int(num) < min:
        min = int(num)
print(min)  # 打印最小TestTime

sum = 0
for num in test_time:
    sum += int(num)
average = sum / len(test_time)
average_2 = '%.2f' % average  # 保留两位小数
print(average_2)








