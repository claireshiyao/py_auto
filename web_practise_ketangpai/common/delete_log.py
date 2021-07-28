
#  -*-coding:utf8 -*-
import datetime
import os
import time

from common.dir_config import log_path


def clean_log(path, n):
    """清除n天前的日志"""
    if os.path.exists(path) and os.path.isdir(path):
        n_days_before = (datetime.date.today() + datetime.timedelta(-n)).strftime('%Y-%m-%d')
        n_days_before = time.strptime(n_days_before, "%Y-%m-%d")
        for file in os.listdir(path):
            file_name_sp = file.split('.')
            if len(file_name_sp) > 2:
                file_date = file_name_sp[1]  # 取文件名里面的日期
                file_date = time.strptime(file_date, "%Y-%m-%d")
                if file_date < n_days_before:
                    abs_path = os.path.join(path, file)
                    print('删除的文件是%s,' % abs_path)
                    os.remove(abs_path)
                else:
                    print('没有删除的文件是%s' % file)
    else:
        print('路径不存在/不是目录')

if __name__ == '__main__':
    clean_log(log_path, 2)
