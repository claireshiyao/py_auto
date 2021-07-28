import os


class Config:
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(root_path, "data/data.xlsx")
    case_path = os.path.join(root_path, 'test_cases')
    report_path = os.path.join(root_path, 'report')
    if not os.path.exists(report_path):
        os.mkdir(report_path)

class DevConfig(Config):
    host = 'http://120.78.128.25:8766/futureloan'

config = DevConfig()