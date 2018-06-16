import binascii
import pymysql
import pymysql.cursors
import random

def email_hash(email):
    return 100 * binascii.crc32(email.encode('utf-8')) + len(email)


def convert_birthday(birthday):
    # bday (check format) 1976-11-18 -> 13- 1-1984
    year, month, day = birthday.split('-')
    return "{0:>2}-{1:>2}-{2}".format(int(day), int(month), year)


def convert_timezone(timezone):
    matches = {-12.00: 'UTC',
                -11.00: 'Pacific/Midway',
                -10.00: 'Pacific/Honolulu',
                -9.50: 'Pacific/Marguesas'
                -9.00: 'America/Adak',
                -8.00: 'America/Anchorage',
                -7.00: 'America/Creston',
                -6.00: 'America/Belize',
                -5.00: 'America/Atikokan',
                -4.00: 'American/Anguilla',
                -3.00: 'America/Araguaina',
                -2.50: 'America/St. Johns',
                -2.00: 'America/Godthab',
                -1.00: 'Atlantic/Cape Verde',
                0.00: 'UTC',
                1.00: 'Africa/Algiers',
                2.00: 'Africa/Blantyre',
                3.00: 'Africa/Addis Ababa',
                4.00: 'Asia/Baku',
                4.50: 'Asia/Kabul',
                5.00: 'Asia/Colombo',
                5.75: 'Asia/Kathmandu',
                6.00: 'Antarctica/Vostok',
                6.50: 'Asia/Yangon',
                7.00: 'Antarctica/Davis',
                8.00: 'Asia/Brunei',
                8.50: 'Asia/Pyongyang',
                8.75: 'Australia/Eucla',
                9.00: 'Asia/Chita',
                9.50: 'Australia/Adelaide',
                10.00: 'Australia/Sydney',
                10.50: 'Australia/Lord Howe',
                11.00: 'Antarctica/Casey',
                12.00: 'Antarctica/McMurdo',
                12.75: 'Pacific/Chatham',
                13.00: 'Pacific/Apia',
                14.00: 'Pacific/Kiritimati'}
    return matches.get(timezone, 'UTC')


def prepare_insert_statement(table, data):
    fields = []
    values = []
    values_actual = []
    for k,v in data.items():
        fields.append('`'+k+'`')
        values.append('%s')
        values_actual.append(v)
    statement = "INSERT INTO `{0}` ({1}) VALUES ({2})".format(table,
                                                        ', '.join(fields),
                                                        ', '.join(values))
    return statement, values_actual

def convert_fields(m):
    new_m = {"user_permissions": None, # cached value from other tables?
            "user_perm_from": 0, # 0 for everyone?
            "user_passchg": 0, # 0
            "user_lastmark": 0, # 0
            "user_lastpost_time": 0,
            "user_lastpage": '',
            "user_last_confirm_key": '',
            "user_last_search": 0, # 0
            "user_warnings": 0, # 0
            "user_last_warning": 0, # 0
            "user_login_attempts": 0, # 0
            "user_inactive_reason": 0, # 0
            "user_inactive_time": 0, # 0
            "user_lang": 'en', # en
            "user_style": 1, # 1
            "user_new_privmsg": 0, # 0
            "user_unread_privmsg": 0, # 0
            "user_last_privmsg": 0, # 0
            "user_message_rules": 0, # 0
            "user_full_folder": -3, # -3
            "user_emailtime": 0, # 0
            "user_topic_show_days": 0, # 0
            "user_topic_sortby_type": 't' # t
            "user_topic_sortby_dir": 'd' # d
            "user_post_show_days": 0, # 0
            "user_post_sortby_type": 't', # t
            "user_post_sortby_dir": 'a', # a
            "user_notify": 0, # 0
            "user_notify_pm": 1, # 1
            "user_notify_type": 0, # 0
            "user_allow_pm": 1, # 1
            "user_allow_viewemail": 0, # 0
            "user_allow_massemail": 1, # 1
            "user_options": 230271, # 230271
            "user_avatar": '', # NULL
            "user_avatar_type": '', # NULL
            "user_avatar_width": 0, # 0
            "user_avatar_height": 0, # 0
            "user_sig_bbcode_uid": '',
            "user_sig_bbcode_bitfield": '',
            "user_actkey": ''
            "user_newpasswd": '',
            "user_new": 1,
            "user_reminded": 0,
            "user_reminded_time": 0,}
    new_m["user_type"] = 0# 0 for normal user, 3 for site admin https://wiki.phpbb.com/Table.phpbb_users
    new_m["group_id"] = 2# 5 for site admin
    new_m["user_ip"] = m['regip']# regip
    new_m["user_regdate"] = m['regdate']# regdate
    new_m["username"] = m['username']# username
    new_m["username_clean"] = m['username'].lower() # username.lower()
    new_m["user_password"] = m['password']# password
    new_m["user_email"] = m['email']
    new_m["user_email_hash"] = email_hash(m['email']) #  https://github.com/phpbb/phpbb/blob/1b110139888dbe5ba6338d348287e43bdc193c2a/phpBB/includes/functions.php#L254
    new_m["user_birthday"] = convert_birthday(m['bday']) # bday (check format) 1976-11-18 -> 13- 1-1984
    new_m["user_lastvisit"] = m['lastvisit']# lastvisit
    new_m["user_posts"] = # compute from posts
    new_m["user_timezone"] = convert_timezone(m['timeoffset']) # convert timeoffset
    new_m["user_dateformat"] = m['dateformat']# dateformat
    new_m["user_rank"] = 0
    new_m["user_colour"] = ''# Depends on member type AA0000 for site admin
    new_m["user_allow_viewonline"] = # invisible
    new_m["user_sig"] = m['sig']# sig
    new_m["user_jabber"] = ''
    new_m["user_form_salt"] = ''.join(random.choices('0123456789abcdef', k=16))
    return new_m

def convert_fields_profile(m, user_id):
    new_m = {"user_id": user_id,
            "pf_phpbb_location": m['location'],
            "pf_phpbb_icq": m['icq'],
            "pf_phpbb_website": m['site'],
            "pf_phpbb_yahoo": m['yahoo'],
            "pf_phpbb_aol": m['aim'],}
    return new_m

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
    # Read a single record
    sql = "SELECT * FROM `xmb_members`"
    cursor_old.execute(sql)
    for member in cursor_old.fetchall():
        # Skip if user is Polverone
        # Account is created during forum setup
        if member['username'] == 'Polverone':
            continue
        # Insert user in phpbb_users table
        migrated_fields = convert_fields(member)
        statement, values = prepare_insert_statement('phpbb_users', migrated_fields)
        cursor_new.execute(statement, values)
        conn_new.commit()
        user_id = cursor_new.lastrowid
        # Add user to phpbb_user_group table
        group_memberships = ['REGISTERED']
        if member['status'] == 'Super Moderator':
            group_memberships.append('GLOBAL_MODERATORS')
        elif member['status'] == 'Administrator':
            group_memberships.append('GLOBAL_MODERATORS')
            group_memberships.append('ADMINISTRATORS')
        elif member['status'] == 'Super Administrator':
            group_memberships.append('GLOBAL_MODERATORS')
            group_memberships.append('ADMINISTRATORS')
        for group_type in group_memberships:
            sql = "INSERT INTO `phpbb_user_group` (`group_id`, `user_id`, `group_leader`, `user_pending`) VALUES (SELECT `group_id` FROM `phpbb_groups` WHERE `group_name` = %s, %s, 0, 0)"
            cursor_new.execute(sql, (group_type, user_id))
            conn_new.commit()

        # Add profile information to phpbb_profile_fields_data
        migrated_profile_fields = convert_fields_profile(member, user_id)
        statement, values = prepare_insert_statement('phpbb_profile_fields_data', migrated_profile_fields)
        cursor_new.execute(statement, values)
        conn_new.commit()

        
