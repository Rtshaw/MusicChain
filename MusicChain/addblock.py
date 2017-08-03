import block
import blockchain

import sys
import time
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials as SAC

if __name__ == '__main__':
    GDriveJSON = 'auth.json'
    GSpreadSheet = 'blockchain'
#    chain = blockchain.Blockchain()
    scope = ['https://spreadsheets.google.com/feeds']
    key = SAC.from_json_keyfile_name(GDriveJSON, scope)
    gc = gspread.authorize(key)
    worksheet = gc.open(GSpreadSheet).sheet1
    rows = worksheet.row_count
    x = input('要加在區塊鍊中的文字 :')
    my_block = block.Block(x)
    pre = worksheet.cell(rows,4)
    my_block.update_previous_hash(pre)
    my_block.mine()
#    chain.add_block(my_block)
    count = 1
    try:
        scope = ['https://spreadsheets.google.com/feeds']
        key = SAC.from_json_keyfile_name(GDriveJSON, scope)
        gc = gspread.authorize(key)
        worksheet = gc.open(GSpreadSheet).sheet1
        #row = worksheet.row_values(1)
    except Exception as ex:
        print('無法連線Google試算表', ex)
        sys.exit(1)
    worksheet.append_row((datetime.datetime.now(), count,my_block.previous_hashvalue(),my_block.hashvalue(),my_block.nonce,my_block.data))
    count = count+1
    print('新增一列資料到試算表' ,GSpreadSheet)
#    print(chain.blocks)


#https://docs.google.com/spreadsheets/d/15Zvx7cXS3X34vDu808KLcnOBBe3fM8EKBXM5UbXZ87Y/edit




