from service import FeedService

#조회
def get_feeds(action, options):
    option_list = {
        'action': ["search_feeds_count_by_similar_tag", "profile", "search_feeds_by_tag"]
    }
    if("data" in options):
        if(action == option_list["action"][0]):
            return FeedService.get_search_feeds_count_by_similar_tag(options["data"]).to_string()
        elif(action == option_list["action"][1]):
            return FeedService.get_profile(options["data"]).to_string()
        elif(action == option_list["action"][2]):
            return FeedService.get_search_feeds_by_tag(options["data"]).to_string()
        else:
            return "Fail: It is not existed action that you write"
    else:
        return "Fail: It is not enough data when you approach"
    
#추가
def post_feeds(action, options):
    return "post_feeds"

#수정
def put_feeds(action, options):
    return "put_feeds"

#삭제
def delete_feeds(action, options):
    return "delete_feeds"