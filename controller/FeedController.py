from service import FeedService

def feeds(action, options):
    option_list = {
        'action': ["search_feeds_count_by_similar_tag", "profile", "search_feeds_by_tag"]
    }
    if("data" in options):
        if(action == option_list["action"][0]):
            return FeedService.search_feeds_count_by_similar_tag(options["data"]).to_string()
        elif(action == option_list["action"][1]):
            return FeedService.profile(options["data"]).to_string()
        elif(action == option_list["action"][2]):
            return FeedService.search_feeds_by_tag(options["data"]).to_string()
    else:
        return "Fail: It is not enough data when you approach"