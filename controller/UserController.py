from service import UserService
import json

def get_users(action, options):
    if("data" in options):
        
        if(action == "login"):
            if("user_id" in options["data"] and "user_pw" in options["data"]):
                return UserService.get_login(options["data"]["user_id"], options["data"]["user_pw"]).to_string()
            else:
                return "Fail: It is not enough data when you approach"
        elif(action=="logout"):
            return UserService.get_logout().to_string()
        else:
            return "Fail: It is not existed action that you write"
    else:
        return "Fail: It is not enough data when you approach"

def post_users(action, options):
    return "post_users"

def put_users(action, options):
    return "put_users"

def delete_users(action, options):
    return "delete_users"