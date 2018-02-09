#!/user/bin/env python
# -*- coding:utf-8 -*-
from multiprocessing import Pool
import time
from db import pg_query, my_query, pg_write, my_insert
from settings import auction_mapping
db = 'pyaution'


def get_info_antiques(auction_id, activity_id, prefix):
    """
    导入拍品信息
    :param auction_id:
    :param activity_id:
    :return:
    """
    query = (" SELECT a.name,a.name_en,a.lot,c.created_at,c.updated_at,c.num,c.dept_no,"  # 7
             "a.age,a.age_en,a.size,base_price,"  # 11
             " a.author, a.id"
             " from antiques as a left JOIN contracts as c "
             " on a.contract_id=c.id "
             "where a.activity_id=%s") % (activity_id)
    lots = pg_query(db, query)
    count = 0
    tmp_list = []
    for lot in lots:
        lot_name = lot[0] if "'" not in lot[0] else lot[0].replace(
            "'", "''")  # 拍品中文名字
        lot_no = lot[2]  # 图录号
        create_time = lot[3]  # 创建时间
        last_update_time = lot[4]  # 修改时间
        contract_id = lot[5]  # 合同关联id
        role_id = lot[6] or ''  # 部门
        age = lot[7] or ''  # 年代
        age_en = lot[8] or ''
        dimension = lot[9] or ''  # 尺寸

        bottom_price = lot[10] or 0  # 起步价
        author_zh = lot[11] or ''
        auction_id = auction_id
        ids = prefix + str(lot[12])
        status = 400
        tmp_list.append([lot_name,
                         lot_no,
                         create_time,
                         last_update_time,
                         contract_id,
                         role_id,
                         age,
                         age_en,
                         dimension,
                         bottom_price,
                         author_zh,
                         auction_id,
                         ids,
                         status])

        # query_insert = "insert into lot (lot_name,lot_no,create_time,last_update_time,contract_id,role_id," \
        #                "age,age_en, o_dimension,bottom_price,author_zh,auction_id,id, status) " \
        #                " VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" %  \
        #                (lot_name, lot_no, create_time, last_update_time, contract_id, role_id, age,
        # age_en,  dimension, bottom_price, author_zh, auction_id, ids, status)

    query_insert = "insert into lot (lot_name,lot_no,create_time,last_update_time,contract_id,role_id," \
        "age,age_en, o_dimension,bottom_price,author_zh,auction_id,id, status) " \
                   " VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    # print tmp_list
    my_insert(query_insert, tmp_list)
    tmp_list = []

    # count += 1
    # print u'[插入-图录号:%s]来自第-%s-场次,第-%s-次插入' % (lot_no, prefix, count)
    # print '--------------------------------------->'
    # print u'第[%s]届拍品总计完成%s' % (prefix, count)


def related_lot_id(auction_id):
    """
    合同id和拍品信息关联起来
    :param auction_id:
    :return:
    """
    query = (
        "select l.id, c.id,c.electronic_id from lot as l left join contract as c on c.electronic_id = l.contract_id "
        "where l.auction_id=%s" %
        auction_id)
    contract_ids = my_query(query)
    args = []
    for item in contract_ids:
        args.append([item['c.id'], item['id'], auction_id])
        print (item['c.id'], item['id'], auction_id)
    query_update = 'update lot set contract_id=%s where id=%s and auction_id=%s'
    my_insert(query_update, args)
    print '%关联成功'


if __name__ == '__main__':

    for activity_id, auction_id in auction_mapping.iteritems():

        get_info_antiques(auction_id[0], activity_id, auction_id[1])
        print '%s届拍品完成' % auction_id[1]
    print u'Done completely！'

    # 再次执行请再执行lot表的导入工作
    # t1 = time.time()
    # for activity_id, auction_id in auction_mapping.iteritems():
    #     related_lot_id(auction_id[0])
    # print(time.time()-t1)
    time.sleep(10)
    print u'开始关联......'
    t2 = time.time()
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
    pool.map(related_lot_id, kwags)
    pool.close()
    pool.join()
    print (time.time() - t2)  # 164.447
