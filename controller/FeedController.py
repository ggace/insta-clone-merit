from service import FeedService

def feeds(options):
    option_list = {
        'action': ["search_feeds_count_by_similar_tag", "profile", "search_feeds_by_tag"]
    }
    if("action" in options and "data" in options):
        if(options["action"] == option_list["action"][0]):
            return FeedService.search_feeds_count_by_similar_tag(options["data"]).to_string()
        elif(options["action"] == option_list["action"][1]):
            return FeedService.profile(options["data"]).to_string()
        elif(options["action"] == option_list["action"][2]):
            return FeedService.search_feeds_by_tag(options["data"]).to_string()
    else:
        return "It is not enough data when you approach"