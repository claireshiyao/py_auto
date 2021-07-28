#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: test_param
# Author: 简
# Time: 2019/7/27
import pytest

a = [(1,2),(100,200),(120,220)]

@pytest.mark.parametrize("a,b",a)
def test_aa(a, b):
    print(a, b)


@pytest.mark.parametrize("a", a)
def test_aa(a):
    print(a)


@pytest.mark.parametrize("x", [0, 1])
@pytest.mark.parametrize("y", [2, 3])
def test_foo(x, y):
    pass
