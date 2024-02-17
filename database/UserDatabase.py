import database.connection as database
import database.sqls as sqls

def get_login(user_id, user_pw):
    sql = sqls.get_sql_about_login(user_id, user_pw)

    database.sqlRun(sql)

    return "End"

def get_logout():
    sql = sqls.get_sql_about_get_logout()

    database.sqlRun(sql)

    return "End"

