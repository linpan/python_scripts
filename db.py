#!/user/bin/env python
# -*- coding:utf-8 -*-
import sys
import MySQLdb
import psycopg2
from contextlib import closing
import MySQLdb.cursors as mc
DictCursor = mc.DictCursor
Cursor = mc.DictCursor

reload(sys)
sys.setdefaultencoding('utf-8')

#  postgres connection settings
DSN = dict(
    host='127.0.0.1',
    user='postgres',
    password='postgres')

#  mysql connection settings, pointed out that get dict format

# MYS = dict(
#     host='127.0.0.1',
#     user='root',
#     passwd='',
#     db='new_oa',
#     cursorclass=Cursor
# )

MYS = dict(
    host='10.16.9.243',
    user='e-troin@admin',
    passwd='#MZYK1!ZRjPdbe7u',
    db='auction-oa',
    cursorclass=Cursor
)


def pg_connection(db):
    """
    连接pg数据库并处理异常事件
    :return:
    """
    try:
        conn = psycopg2.connect(dbname=db, **DSN)
        return conn

    except psycopg2.Error as e:
        print "Unable to connect to the database."
        print e.pgerror
        print e.diag.message_detail


def pg_query(db, query, arg=None):
    """
    postgresl query
    :param db:
    :param query:
    :param arg:
    :return:
    """

    with pg_connection(db) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, arg)
            rows = cursor.fetchall()

    return rows


def pg_write(db, query, arg=None):
    """
    postgresl query
    :param db:
    :param query:
    :param arg:
    :return:
    """

    with pg_connection(db) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, arg)


def my_connection():
    """
    mysql connection
    :return:
    """
    try:
        conn = MySQLdb.connect(**MYS)
        return conn
    except MySQLdb.Error as e:
        print 'Unable to connect to the database. %s' % e


def my_query(query, arg=None):
    """
    mysql query
    :param db:
    :param query:
    :param arg:
    :return:
    """

    with closing(my_connection()) as conn:  # ensure that the connection is closed
        with conn as cursor:  # cursor will now auto-commit
            cursor.execute(query, arg)
            ret = cursor.fetchall()
            return ret

def my_insert(query,arg=None):
    """
    mysql query
    :param db:
    :param query:
    :param arg:
    :return:
    """

    with closing(my_connection()) as conn:  # ensure that the connection is closed
        with conn as cursor:  # cursor will now auto-commit
            cursor.executemany(query, arg)

            return 'success'


if __name__ == '__main__':
    pass
