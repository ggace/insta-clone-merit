import database.connection as database

def getFeedsByProfile(user_id):
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