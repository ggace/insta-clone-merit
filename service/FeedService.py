from database import FeedDatabase
from ResultData import ResultData
import ResultState

def getFeedsByProfile(user_id):
    data = FeedDatabase.getFeedsByProfile(user_id)

    return ResultData(ResultState.Success, data)