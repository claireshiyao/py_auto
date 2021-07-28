# author by claire
import os
import shutil
import time

import pytest

from common.delete_log import clean_log
from common.dir_config import base_path, log_path

curTime = time.strftime("%Y-%m-%d %H_%M_%S")
src_path = os.path.join(base_path, "outputs/report/allure")
dst_path = os.path.join(base_path, "outputs/report/allure_{}".format(curTime))
shutil.move(src_path, dst_path)
os.mkdir("outputs/report/allure")

clean_log(log_path, 3)

pytest.main(["-s", "-v", "test_cases", "--reruns", "1", "--reruns-delay", "3",
             "--alluredir=outputs/report/allure"])

# pytest.main(["-s", "-v", "-m", "smoke", "--reruns", "1", "--reruns-delay", "3",
             # "--alluredir=outputs/report/allure"])

# pytest.main(["-s", "-v", "-m", "smoke"])
