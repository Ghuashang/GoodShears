import unittest
class test_reg_user(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("开始")
    @classmethod
    def tearDownClass(cls) -> None:
        print("结束")
    def setUp(self) -> None:
        print("初始化")
    def tearDown(self) -> None:
        print("结束清理")
    def test_reg001(self):
        print("注册用户1")
    def test_reg002(self):
        print("该用户以注册")
