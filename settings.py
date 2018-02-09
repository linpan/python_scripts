#!/user/bin/env python
# -*- coding:utf-8 -*-

import datetime
"""
 - A 现当代艺术部
 - B 书画
 - C 瓷器
 - D 钱币油品
"""

dept_mapping = {
    'AA': 'a4336724851a4c4ba6e497a661e7dadf',
    'AB': '0d0898b051fd460cbad6b28f00ba857a',
    'AC': '04cb5d844aec43c98dde36d10369ea42',
    'AD': '70b51675410241e188c6548e510013db',
    'AE': '-10',
    'SA': 'a4336724851a4c4ba6e497a661e7dadf',
    'SB': '0d0898b051fd460cbad6b28f00ba857a',
    'SC': '04cb5d844aec43c98dde36d10369ea42',
    'SD': '70b51675410241e188c6548e510013db',
    'SE': '-10',
}

dept_app = ['AA', 'AB', 'AC', 'AD', 'SA', 'SB', 'SC', 'SD', 'SE']

# {activity_id: auction_id}
auction_mapping = {
    '2': ['-14', '20050001'],  # 2005a
    '3': ['-13', '20060000'],  # 2006s
    '4': ['-12', '20060001'],  # 2006a
    '5': ['-11', '20070000'],  # 2007s
    '6': ['-10', '20070001'],  # 2007a
    '7': ['-9', '20080000'],   # 2008s
    '8': ['-8', '20080001'],   # 2008a
    '9': ['-7', '20090000'],   # 2009s
    '10': ['-6', '20090001'],  # 2009a
    '11': ['-5', '20090000'],  # 2010s
    '12': ['-4', '20100000'],  # 2010a
    '13': ['-3', '20110000'],  # 2011s
    '14': ['-2', '20110001'],   # 2011a
    '15': ['-1', '20120000'],  # 2012a
    '1': ['-15', '20120001'],   # 2012s
}


TYPE_MAPPING = {'varchar': "''",
                'datetime': 'NULL',
                'int': '0',
                'tinyint': '0',
                'bigint': '0',
                'text': "''",
                'decimal': '0',
                'char': "''",

                }

TABLE_LISTS = ["auction",
               "auction_artist_info",
               "auction_associated_information",
               "auction_auctioneer",
               "auction_bid_no",
               "auction_bid_register",
               "auction_copy",
               "auction_lot_pigment",
               "auction_lot_situation",
               "auction_lot_texture",
               "auction_lot_texture2",
               "auth_token",
               "catalog",
               "china_area",
               "china_area_copy",
               "china_area_second",
               "company",
               "contract",
               "contract_copy",
               "contract_image",
               "contracts",
               "coulumn_role",
               "crms_client_no_contact",
               "customer",
               "customer_address",
               "customer_auction",
               "customer_copy",
               "customer_delivery",
               "customer_identity",
               "customer_phone",
               "customer_role",
               "customer_user",
               "data_authority",
               "delivery_catalog",
               "delivery_department",
               "delivery_history",
               "department",
               "department_catalog",
               "department_type",
               "extend_column_definition",
               "file_authority",
               "func_authority",
               "hm_user",
               "lot",
               "lot_book",
               "lot_category",
               "lot_copy",
               "lot_fee",
               "lot_image",
               "lot_info",
               "lot_status",
               "lot_subcategory",
               "menu",
               "message",
               "message_authority",
               "message_read_status",
               "note",
               "property",
               "record_export",
               "recycle_contract",
               "recycle_lot",
               "remit",
               "role",
               "role_catalog",
               "role_menu",
               "simple_data_authority",
               "special",
               "transaction",
               "user_preference",
               "user_preference_column",
               "z_antiques",
               "z_buyers",
               "z_customer_copy_copy",
               "z_customer_identity_copy",
               "z_test_customer",
               "ztest_seller"]
