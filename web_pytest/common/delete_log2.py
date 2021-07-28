
#  -*-coding:utf8 -*-
import datetime
import os

from common.dir_config import log_path


def clean_log(path):
    if os.path.exists(path) and os.path.isdir(path):
        today = datetime.date.today().strftime('%Y-%m-%d')
        yesterday = (datetime.date.today() + datetime.timedelta(-1)).strftime('%Y-%m-%d')
        before_yesterday = (datetime.date.today() + datetime.timedelta(-2)).strftime('%Y-%m-%d')
        file_name_list = [today, yesterday, before_yesterday]
        print(file_name_list)
        for file in os.listdir(path):
            file_name_sp = file.split('.')
            if len(file_name_sp) > 2:
                file_date = file_name_sp[1]  # 取文件名里面的日期
                # print type(file_date)
                # print type(file_name_list[0])
                if file_date not in file_name_list:
                    abs_path = os.path.join(path, file)
                    print('删除的文件是%s,' % abs_path)
                    os.remove(abs_path)
                else:
                    print('没有删除的文件是%s' % file)
    else:
        print('路径不存在/不是目录')

if __name__ == '__main__':
    clean_log(log_path)
