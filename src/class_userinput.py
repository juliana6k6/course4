from src.class_api import HeadHunter_API, SuperJob_API
from src.class_my_list import My_List
import copy

class UserInput:

    param_zero = {}

    def __init__(self):
        self.hh_api = HeadHunter_API()
        self.sj_api = SuperJob_API()
        self.all_list = My_List()
        self.favorite_list = My_List()
        self.param = copy.deepcopy(self.param_zero)


    def __call__(self):
        pass