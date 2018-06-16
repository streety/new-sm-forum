import pymysql
import pymysql.cursors

def convert_fields_forum(orig):
    entry = {"forum_id":,
            "parent_id":,
            "left_id":,
            "right_id":,
            "forum_parents":, # Complex, check
            "forum_name": orig['name'],
            "forum_desc": orig['description'],
            "forum_desc_bitfield": "",
            "forum_desc_options": 7,
            "forum_desc_uid": "",
            "forum_link": "",
            "forum_password": "",
            "forum_style": 0,
            "forum_image": "",
            "forum_rules": "",
            "forum_rules_link": "",
            "forum_rules_bitfield": "",
            "forum_rules_options": 7,
            "forum_rules_uid": "",
            "forum_topics_per_page": 0 ,
            "forum_type":, # 0 for category, 1 for regular
            "forum_status": 0,
            "forum_last_post_id": orig['lastpost'].split('|')[2], # Check
            "forum_last_poster_id": orig['lastpost'].split('|')[2], # Check
            "forum_last_post_subject":, # Check
            "forum_last_post_time":orig['lastpost'].split('|')[0],
            "forum_last_poster_name": orig['lastpost'].split('|')[1],
            "forum_last_poster_colour": , # Check 
            "forum_flags":, # 32 and 48 seen
            "display_on_index":1,
            "enable_indexing":1,
            "enable_icons":1,
            "enable_prune":0,
            "prune_next":0,
            "prune_days":0,
            "prune_viewed":0,
            "prune_freq":0,
            "display_subforum_list":1,
            "forum_options":0,
            "forum_posts_approved":, # Count of posts
            "forum_posts_unapproved":0,
            "forum_posts_softdeleted": 0 ,
            "forum_topics_approved":, # Count of topics
            "forum_topics_unapproved":0,
            "forum_topics_softdeleted":0,
            "enable_shadow_prune":0,
            "prune_shadow_days":7,
            "prune_shadow_freq":1,
            "prune_shadow_next":0,}
    return entry

def convert_fields_thread(orig):
    entry = {}
    return entry

def convert_fields_posts(orig):
    pass

def convert_fields_polls(orig):
    pass

def convert_fields_attachments(orig):
    pass

# Connect to the xmb database
conn_old = pymysql.connect(host='192.168.99.100',
                             user='root',
                             password='science',
                             db='science_xmb1',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

# Connect to the phpbb database
conn_new = pymysql.connect(host='localhost',
                             user='demo',
                             password='demo',
                             db='demo',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

with conn_old.cursor() as cursor_old, conn_new.cursor() as cursor_new:
