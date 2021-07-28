# author by claire
import os
import unittest
testloader = unittest.TestLoader()

dir_path = os.path.dirname(os.path.abspath(__file__))
case_path = os.path.join(dir_path, 'test_cases')
suite = testloader.discover(case_path)

report_path = os.path.join(dir_path, 'report')
if not os.path.exists(report_path):
    os.mkdir(report_path)

file_path = os.path.join(report_path, 'test_result.txt')

with open(file_path, "w", encoding="utf-8") as f:
    runner = unittest.TextTestRunner(f, verbosity=2)
    runner.run(suite)
