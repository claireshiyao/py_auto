#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: main_pytest
# Author: 简
# Time: 2019/7/27

import pytest

if __name__ == '__main__':
    pytest.main(["-s","-v","TestCases/ModeA/test_login.py","--html=Outputs/reports/pytest.html"])
