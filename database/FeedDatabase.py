import database.connection as database
import database.sqls as sqls

def profile(user_id):
    sql = sqls.get_sql_about_profile(user_id)
    
    return database.sqlRun(sql)

def search_feeds_count_by_similar_tag(tag):
    sql = sqls.get_sql_about_search_feeds_count_by_similar_tag(tag)
    
    return database.sqlRun(sql)

def search_feeds_by_tag(tag):
    sql = sqls.get_sql_about_search_feeds_by_tag(tag)
    
    return database.sqlRun(sql)