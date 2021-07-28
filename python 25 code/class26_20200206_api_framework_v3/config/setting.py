import os


class Config:
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(root_path, "data/data.xlsx")
    case_path = os.path.join(root_path, 'test_cases')
    config_path = os.path.join(root_path, 'config/config.yaml')

    report_path = os.path.join(root_path, 'report')
    if not os.path.exists(report_path):
        os.mkdir(report_path)

    log_path = os.path.join(root_path, 'log')
    if not os.path.exists(log_path):
        os.mkdir(log_path)

class DevConfig(Config):
    host = 'http://120.78.128.25:8766/futureloan'

config = DevConfig()