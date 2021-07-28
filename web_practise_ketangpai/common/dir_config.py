import os

base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

screenshots_path = os.path.join(base_path, "outputs/screenshots")
report_path = os.path.join(base_path, "outputs/report")
log_path = os.path.join(base_path, "outputs/log")

testdata_path = os.path.join(base_path, "test_datas")
testcase_path = os.path.join(base_path, "test_cases")

