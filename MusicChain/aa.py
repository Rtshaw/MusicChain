GDriveJSON = 'auth.json'
GSpreadSheet = 'blockchain'
WaitSecond = 60
# print('將資料記錄在試算表' ,GSpreadSheet , '每' ,WaitSecond ,'秒')
# print('按下 Ctrl-C中斷執行')
count = 1
while True:
    try:
        scope = ['https://spreadsheets.google.com/feeds']
        key = SAC.from_json_keyfile_name(GDriveJSON, scope)
        gc = gspread.authorize(key)
        worksheet = gc.open(GSpreadSheet).sheet1
    except Exception as ex:
        print('無法連線Google試算表', ex)
        sys.exit(1)
    worksheet.append_row((datetime.datetime.now(), count, my_block.previous_hashvalue, my_block.hashvalue(),
                          my_block.nonce, my_block.data))
    count = count + 1
    print('新增一列資料到試算表', GSpreadSheet)
    # time.sleep(WaitSecond)
