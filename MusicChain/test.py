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

    try:
        scope = ['https://spreadsheets.google.com/feeds']
        key = SAC.from_json_keyfile_name(GDriveJSON, scope)
        gc = gspread.authorize(key)
        worksheet = gc.open(GSpreadSheet).sheet1
        col = worksheet.col_values(1)
	val = worksheet.acell('C')
    except Exception as ex:
        print('無法連線Google試算表', ex)
        sys.exit(1)
    print(col)
    print(val)


#https://docs.google.com/spreadsheets/d/15Zvx7cXS3X34vDu808KLcnOBBe3fM8EKBXM5UbXZ87Y/edit




