#!/user/bin/env python
# -*- coding:utf-8 -*-

import re
import time
import MySQLdb
import MySQLdb.cursors as mc
import multiprocessing
from db import my_query

from settings import TYPE_MAPPING, TABLE_LISTS

DictCursor = mc.DictCursor
Cursor = mc.DictCursor

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


reg = r'\w+'
pattern = re.compile(reg)


def get_fileds_type(tablename):
    query = "SHOW FIELDS FROM %s " % tablename
    filed_type = my_query(query)
    # 对外键不能设空值，排除带有id的字段
    filed_to_datatype = {filed['Field']: re.search(pattern, filed['Type']).group() for filed in filed_type if not filed['Field'].endswith('_id')}
    return filed_to_datatype


def handle_fileds(tablename, conn):
    """
    set specail filed(Null,NONE) to a defualt value
    :return:
    """
    cursor = conn.cursor()
    filed_to_datatype = get_fileds_type(tablename)

    fileds = [filed for filed in filed_to_datatype.keys()]

    query = "SELECT * FROM %s " % tablename
    records = my_query(query)
    null_filed = []

    for record in records:
        flag = False
        for fd in fileds:
            if record[fd] in [None, 'NULL']:  # 如果该字段为空的处理 fd 为字段
                null_filed.append(fd)
                flag = True
                if filed_to_datatype[fd] in TYPE_MAPPING:
                    default_values = TYPE_MAPPING[filed_to_datatype[fd]]  # 获得字段的类型及对应的默认值
                    record[fd] = default_values

                else:
                    print u'请把%s加入映射表' % filed_to_datatype[fd]
            else:
                pass

        if flag:
           filed_id = record.get('id') if record.get('id') else record.get('ID')
        # 代码片段：更新数据库
           query = update_table(tablename, record, null_filed, filed_id)
           cursor.execute(query)

        # 清空列表内容
           null_filed = []
    # 一次性提交，效率较高
    conn.commit()
    cursor.close()


def update_table(tablename, record, null_filed, field_id):
    query = "UPDATE %s SET " % tablename
    end_index = len(null_filed)-1
    for index, filed in enumerate(null_filed):
        if index != end_index:
            query = query + "`" + filed + "`" + " =%s , "
        else:
            query = query + "`" + filed + "`" + " =%s "
    values = [record[value] for value in null_filed]
    query = query + " WHERE id='%s' " % field_id
    query_all = query % tuple(values)
    return query_all


if __name__ == '__main__':
    conn = MySQLdb.connect(**MYS)

    ts = time.time()
    for tb in TABLE_LISTS:
        print u'%s准备处理中...' % tb
        handle_fileds(tb, conn)
        print (time.time()-ts)
        print u'%s表处理完毕'% tb
    else:
        print '任务完成，关闭数据库 '
        conn.close()

    # handle_fileds('user_preference', conn)
    # conn.close()