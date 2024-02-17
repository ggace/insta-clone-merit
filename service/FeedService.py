from database import FeedDatabase
from ResultData import ResultData
import ResultState

def profile(user_id):
    data = FeedDatabase.profile(user_id)

    return ResultData(ResultState.Success, data)

def search_feeds_count_by_similar_tag(tag):

    data = FeedDatabase.search_feeds_count_by_similar_tag(tag)
    return ResultData(ResultState.Success, data)

def search_feeds_by_tag(tag):
    data = FeedDatabase.search_feeds_by_tag(tag)
    return ResultData(ResultState.Success, data)