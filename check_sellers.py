#!/user/bin/env python
# -*- coding:utf-8 -*-
import re

from db import pg_query, my_query, pg_write
from settings import  dept_mapping,dept_app

activity_id = 1
db='pyaution'


def get_sellers_name(db='pyaution'):
    query = 'select name from sellers where activity_id=1'
    records = pg_query(db, query)
    names =[]
    for name in records:
        names.append(name[0])
    return names


results = get_sellers_name()


def check_customer(name):
    query = "select name from customer where name like '%s' " % ('%%%s%%' % name)

    records = my_query(query)
    if not records:
        print name


def check_identity():
    query = "select  identity_num from sellers where identity_num <>'' "
    ids_from_pg = pg_query(db, query)
    ids_from_pg = [item[0] for item in ids_from_pg]
    for num in ids_from_pg:
        try:
            # print '->>',num
            match = re.search(r'[\w-]+', num).group()
            # print match
        except re.error as e:
            print e
        query = "select number from customer_identity where number LIKE '%s'" % ('%%%s%%' % match)
        records = my_query(query)
        if records:
            print match




def crm_client():
    query = "select  number from crms_paper where number <>'' "
    ids_from_pg = pg_query('CRM', query)
    ids_from_pg = [item[0] for item in ids_from_pg]
    for num in ids_from_pg:
        try:
            # print '->>',num
            match = re.search(r'[\w-]+', num).group()
            # print match
        except re.error as e:
            print e
        query = "select identity_number from contract where identity_number LIKE '%s'" % ('%%%s%%' % match)
        records = my_query(query)
        if records:
            print match

# 对contracts的基本操作，需增加一个dept_no字段

def append_dept_contract(db):
    query = "select id, num from contracts"
    id_num = pg_query(db, query)  # tuple in list
    for item in id_num:
        for dept in dept_mapping:
            if dept in item[1]:
                query = "update contracts set dept_no='%s' where id=%s" % (dept_mapping[dept], item[0])
                print query
                pg_write(db, query)


def append_seller_identity_contract(db):
    query = 'select id, seller_id from contracts '
    seller_id = pg_query(db, query)
    for item in seller_id:
        query ='select identity_num from sellers where id=%s'% (item[1])
        ids = pg_query(db, query)
        if ids[0][0]:
            match = re.search(r'[\w-]+', ids[0][0]).group()
            query2 = "update contracts set identity_num='%s' where id=%s" % (match, item[0])
            pg_write(db, query2)



if __name__ == '__main__':
    # check_identity()
    # crm_client()
    append_dept_contract(db)
    append_seller_identity_contract(db)