import pymysql


def _our_unknown_hash(password):
    return {
        "pass" : "bf6116af8e4b3e83a7646640590b9d5f5c95b06bf7eebf6c424487ff39293833",
        "test": "62fc22c0da68a727562013a405e45ad29fe67725db24870d8dff48a39b37f5ae",
        "secret": "94d1297b55907d7158b27cd91f0d0b0d212abc0ccd4a3e861b1f4e1f404c67e0"
    }[password]

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='oxwa166',
                             password=']R44u83pS@',
                             db='oxwa166',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = """INSERT INTO `ow_base_user` (`username`, `email`, `password`, `joinIp`)
                 VALUES ("{}", "{}", "{}", "2130706433")"""
        cursor.execute(sql.format('test', 'tcdg@python.org', _our_unknown_hash('secret')))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `username`, `password` FROM `ow_base_user`"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    connection.close()



import pymysql

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='user',
                             password='passwd',
                             db='db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('webmaster@python.org',))
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()
