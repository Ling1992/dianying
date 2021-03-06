# -*- coding: UTF-8 -*-

import MySQLdb


class MysqlLing(object):
    db = None
    cursor = None
    __instance = None

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(MysqlLing, cls).__new__(cls, *args, **kwargs)
            cls.db = MySQLdb.connect("localhost", "root", "root", "ling_index", charset="utf8")
            cls.cursor = cls.db.cursor()
            print 'MysqlLing __new__ '
        return cls.__instance

    def insert(self, sql_str):
        # print sql_str
        try:
            self.cursor.execute(sql_str)
            # insert_id = self.db.insert_id()
            # insert_id = self.cursor.lastrowid
            self.db.commit()
            return True
        except Exception, e:
            print e
            self.db.rollback()
            print 'rollback'
            return False

    def count(self, sql_str):
        count = self.cursor.execute(sql_str)
        return count

    def search(self, sql_str):
        print sql_str
        data = []
        try:
            self.cursor.execute(sql_str)
            results = self.cursor.fetchall()
            for row in results:
                author_id = row[0]
                name = row[1]
                media_id = row[2]
                fensi = row[3]
                guanzhu = row[4]
                author_type = row[5]
                data.append({'author_id': author_id, 'name': name, 'media_id': media_id, 'fensi': fensi, 'guanzhu': guanzhu, 'type': author_type})
        except Exception, e:
            print e
        return data

    def __del__(self):
        self.cursor.close()
        self.db.close()
        print 'db closed !'


if __name__ == '__main__':
    # sql = "insert into article(title, article) values ('%s', '%s') " % ('test_title ', '啊哈哈哈哈')
    # sql = "select * from article where title='aaaa'"
    # sql = "insert into article(article_id, title, article) values ('%d', '%s', '%s') " % (11, 'test_title ', '啊哈哈哈哈')
    sql = "insert into article_list(title, abstract, group_id, category_id) values ('%s', '%s', '%d', '%d', '%d') " % ('asdfjl', 'test_title ', 12, 131, 11)
    mysql = MysqlLing()
    res = mysql.insert(sql)
    if res:
        print 'yes', res
    else:
        print 'no'

