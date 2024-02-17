from database import UserDatabase
from ResultData import ResultData
import ResultState

def get_login(user_id, user_pw):
    data = UserDatabase.get_login(user_id, user_pw)

    return ResultData(ResultState.Success, data)

def get_logout():
    data = UserDatabase.get_logout()

    return ResultData(ResultState.Success, data)