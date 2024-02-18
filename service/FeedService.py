from database import FeedDatabase
from ResultData import ResultData
import ResultState

def get_profile(user_id):
    data = FeedDatabase.get_profile(user_id)

    return ResultData(ResultState.Success, data)

def get_search_feeds_count_by_similar_tag(tag):

    data = FeedDatabase.get_search_feeds_count_by_similar_tag(tag)
    return ResultData(ResultState.Success, data)

def get_search_feeds_by_tag(tag):
    data = FeedDatabase.get_search_feeds_by_tag(tag)
    return ResultData(ResultState.Success, data)

def get_view_all_profile_feeds(user_id):
    data = FeedDatabase.get_view_all_profile_feeds(user_id)

    return ResultData(ResultState.Success, data)