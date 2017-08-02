def findLastRow():
    global spreadsheet
    global datastartrow
    global datastartcolumn

    t0 = time.time()

#    print 'starting count 1'
    colvals = worksheet.col_values(1)
    t1 = time.time()

#    print 'colvals: ', len(colvals)

#    print 'count 1 took: ', str(t1 - t0) + ' seconds'

    # return len(colvals)

    t0 = time.time()

#    print 'starting count 2'

    lastrow = datastartrow

    while(True):
        val = worksheet.cell(lastrow, datastartrow).value

        if val == '':
            lastrow -= 1

            break

        lastrow += 1

 #   print 'lastrow: ', lastrow

    t1 = time.time()

 #   print 'count 2 took: ', str(t1 - t0) + ' seconds'

    return lastrow
