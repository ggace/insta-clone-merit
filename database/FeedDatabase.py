import database.connection as database

def profile(user_id):
    sql = f'''
SELECT feeds.id, feeds.content, media.media AS first_media, users.user_id, users.nickname, users.description, users.profile_img
FROM feeds 
INNER JOIN media 
INNER JOIN users 
ON media.feed_id = feeds.id 
AND users.id=feeds.owner_id 
WHERE users.id={user_id}
GROUP BY feeds.id
        '''
    
    return database.sqlRun(sql)

def search_feeds_count_by_similar_tag(tag):
    sql = f"""
SELECT tag, COUNT(DISTINCT feed_id) AS `count`
FROM feed_tag
WHERE tag LIKE "%{tag}%"
GROUP BY tag
"""
    
    return database.sqlRun(sql)

def search_feeds_by_tag(tag):
    sql = f"""
SELECT feeds.id, feeds.content, media.media AS first_media, IF(users.nickname=NULL, users.nickname, users.user_id) as user, users.profile_img
FROM feeds 
INNER JOIN media 
INNER JOIN users 
INNER JOIN feed_tag
ON media.feed_id = feeds.id 
AND feed_tag.feed_id = feeds.id
AND users.id=feeds.owner_id
WHERE feed_tag.tag = "{tag}"
GROUP BY feeds.id
"""
    
    return database.sqlRun(sql)