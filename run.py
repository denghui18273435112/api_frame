#主运行

import os
import pytest

from common import Base
from config import Conf



if __name__ == '__main__':

    report_path = Conf.get_report_path()+os.sep+"result"
    report_html_path = Conf.get_report_path()+os.sep+"html"
    print(report_path)
    pytest.main(["-s","--alluredir",report_path])
    #Base.send_mail()
