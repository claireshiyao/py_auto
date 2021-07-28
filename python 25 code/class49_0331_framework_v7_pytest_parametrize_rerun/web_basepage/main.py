import pytest

pytest.main(["-s","-v","-m","demo","--html=Outputs/report.html",
             "--reruns","2","--reruns-delay","5"])