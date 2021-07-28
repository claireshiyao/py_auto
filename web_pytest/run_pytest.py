import os
import shutil
import time

import pytest

from common.dir_config import base_path

curTime = time.strftime("%Y-%m-%d %H_%M_%M")

src_path = os.path.join(base_path, "outputs/report/allure")
dst_path = os.path.join(base_path, "outputs/report/allure_{}".format(curTime))

shutil.move(src_path, dst_path)
os.mkdir("outputs/report/allure")

pytest.main(["-s", "-v", "-m", "login",
            "--reruns",  "1",  "--reruns-delay", "3",
             "--alluredir=outputs/report/allure"
            ])

# "--html=outputs/report/pytest_report/040401.html",
