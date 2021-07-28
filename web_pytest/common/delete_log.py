#  -*-coding:utf8 -*-
import time
import os, sys

# N = 2  # 设置删除多少天前的文件
from common.dir_config import log_path


def deletefile(path, N):
    for eachfile in os.listdir(path):
        filename = os.path.join(path, eachfile)
        if os.path.isfile(filename):
            lastmodifytime = os.stat(filename).st_mtime
            endfiletime = time.time() - 3600 * 24 * N  # 设置删除多久之前的文件
            if endfiletime > lastmodifytime:
                if filename[-4:] == ".log":
                    os.remove(filename)
                    # print "删除文件 %s 成功" % filename
        elif os.path.isdir(filename):  # 如果是目录则递归调用当前函数
            deletefile(filename)


if __name__ == '__main__':

    deletefile(log_path, 2)
