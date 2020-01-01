import pymysql

def connect_into_database():
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='syddbw5200608',db='test2', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    cursor=conn.cursor(pymysql.cursors.DictCursor)
    return cursor

def connect_into_database_up():
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='syddbw5200608',db='test2', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    cursor=conn.cursor(pymysql.cursors.DictCursor)
    return cursor,conn