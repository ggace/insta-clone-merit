from service import FeedService

def feeds(options):
    option_list = {
        'action': ["serach", "profile"]
    }
    if("action" in options and "data" in options):
        if(options["action"] == option_list["action"][0]):
            return "test"
        elif(options["action"] == option_list["action"][1]):
            return FeedService.getFeedsByProfile(options["data"]).to_string()
    else:
        return "It is not enough data when you approach"