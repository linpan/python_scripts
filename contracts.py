#!/user/bin/env python
# -*- coding:utf-8 -*-
# 3/2 2018


from db import pg_query, my_query, my_insert
from settings import auction_mapping

db = 'pyaution'


def handler_contracts(db, prefix, activity_id, auction_id):
    """
    created_at <---> created_at

    updated_at <---> last_updated_at

    num # 合同号 <---> electronic_id

    `seller_id` <---> customer_id

    activitiy_id <---> action_id

    seller.num   <---> identity_number
    :return:
    """
    query_contracts = (
        " SELECT c.created_at, c.updated_at, c.seller_id, b.identity_num, c.dept_no,c.num,c.id,b.name "
        " from contracts as c left join sellers as b "
        " on c.seller_id=b.id where c.activity_id=%s") % activity_id

    records = pg_query(db, query_contracts)
    args = []
    for record in records:
        count = 0
        create_time = record[0] or ' '
        last_update_time = record[1] or ' '
        electronic_id = record[5] or ' '
        role_id = record[4] or ' '
        identitiy_no = record[3] or ' '
        ids = prefix + str(record[6])
        count += 1
        name = record[7] if "'" not in record[7] else record[7].replace(
            "'", "''")

        args.append([ids, create_time, last_update_time, electronic_id, role_id, auction_id, identitiy_no, name])

    query_insert = "INSERT INTO contract (ID, create_time, last_update_time, electronic_id, role_id, auction_id,identity_number,customer_name)" \
                   " VALUES (%s, %s, %s,%s,%s,%s,%s,%s)"
    my_insert(query_insert, args)

    print '--------------------------------------->'
    print u'第[%s]届总计完成' %  auction_id


# def handler_customer_id_related(auction_id='-14'):
#     query = "SELECT id, identity_number FROM contract where identity_number <>'' and auction_id='%s' " % auction_id
#     records = my_query(query)
#     for record in records:
#         if record['identity_number']:
#             query_num = 'SELECT customer_id from customer_identity where number="%s"' % record[
#                 'identity_number']
#             customer_id = my_query(query_num)
#             print record['identity_number'], '对应用户编号：', customer_id
#             if customer_id:
#                 query_update = 'update contract set customer_id="%s" where id="%s"' % (
#                     customer_id[0]['customer_id'], record['id'])
#                 my_insert(query_update)


if __name__ == '__main__':

    for activity_id, auction_id in auction_mapping.iteritems():
        handler_contracts(
            db,
            prefix=auction_id[1],
            activity_id=activity_id,
            auction_id=auction_id[0])

        print '%s届完成Done!!' % auction_id[1]
    print u'Done completely！'
