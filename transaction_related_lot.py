#!/user/bin/env python
# -*- coding:utf-8 -*-
from multiprocessing import Pool
from db import pg_query, my_query, pg_write, my_insert
from settings import auction_mapping
import time


def related_lot_id(auction_id):
    query = "select t.id as t_id,t.lot, l.lot_no,l.id as l_id from  transaction as t  " \
            "left join lot as l on t.lot= l.lot_no where l.auction_id='%s' and t.auction_id=%s" % (auction_id,auction_id)
    count = 0
    lots = my_query(query)
    args = []
    for lot in lots:
        args.append([lot['l_id'], lot['t_id'], auction_id])

    query_update = "UPDATE transaction set lot_id=%s where id=%s and auction_id=%s"
    my_insert(query_update, args)
    print '-------------------------------------------------'
    print u'<总结>第%s届拍卖会关联' % (auction_id)
    print '--------------------------------------------------'


if __name__ == '__main__':
    pool = Pool(4)
    kwags = [
        '-14',
        '-13',
        '-12',
        '-11',
        '-10',
        '-9',
        '-8',
        '-7',
        '-6',
        '-5',
        '-4',
        '-3',
        '-2',
        '-1',
        '-15']
    t1 = time.time()
    pool.map(related_lot_id, kwags)
    pool.close()
    pool.join()
    print (time.time()-t1)