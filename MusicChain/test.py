import block
import blockchain

import sys
import time
import datetime

from oauth2client.service_account import ServiceAccountCredentials as SAC
import gspread


if __name__ == '__main__':
    GDriveJSON = 'auth.json'
    GSpreadSheet = 'blockchain'

    try:
        scope = ['https://spreadsheets.google.com/feeds']
        key = SAC.from_json_keyfile_name(GDriveJSON, scope)
        gc = gspread.authorize(key)
        worksheet = gc.open(GSpreadSheet).sheet1
        rows = worksheet.row_count
        col = worksheet.cell(rows,4).value
        #test = rowcol_to_a1(rows,4)
        #col = worksheet.cell(2,4)
    except Exception as ex:
        print('無法連線Google試算表', ex)
        sys.exit(1)
    print(col)
    print(rows)
    #print(test)


#https://docs.google.com/spreadsheets/d/15Zvx7cXS3X34vDu808KLcnOBBe3fM8EKBXM5UbXZ87Y/edit




