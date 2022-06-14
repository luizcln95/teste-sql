f1_q1 = ('''
        SELECT AddressOrigin, SUM(TotalSent) AS TotalSentSum
        FROM raw_transactions_table
        WHERE Status = 'Confirmed'
        GROUP BY AddressOrigin
        ORDER BY TotalSentSum DESC
        LIMIT 1;
        ''')

f1_q2 = ('''
        SELECT DAYOFMONTH(SentDate) as MonthDay, SUM(TotalSent) AS TotalSentSum
        FROM raw_transactions_table
        WHERE Status = 'Confirmed'
        GROUP BY MonthDay
        ORDER BY TotalSentSum DESC
        LIMIT 1;
        ''')

f1_q3 = ('''
        SELECT CASE WHEN WEEKDAY(SentDate) = 0 THEN 'Monday'
                    WHEN WEEKDAY(SentDate) = 1 THEN 'Tuesday'
                    WHEN WEEKDAY(SentDate) = 2 THEN 'Wednesday'
                    WHEN WEEKDAY(SentDate) = 3 THEN 'Thursday'
                    WHEN WEEKDAY(SentDate) = 4 THEN 'Friday'
                    WHEN WEEKDAY(SentDate) = 5 THEN 'Saturday'
                    WHEN WEEKDAY(SentDate) = 6 THEN 'Sunday' END
                    AS WeekDay, COUNT(IdTransaction) AS TransactionsCount
        FROM raw_transactions_table
        WHERE Status = 'Confirmed'
        GROUP BY WeekDay
        ORDER BY TransactionsCount DESC
        LIMIT 1;
        ''')

f1_q4 = ('''
        SELECT * FROM raw_transactions_table
        WHERE AddressOrigin = AddressDestination;
        ''')

f1_q5 = ('''
        SELECT AddressOrigin, (TotalReceived - TotalSent) AS Balance
        FROM 
        (SELECT AddressOrigin, sum(TotalSent) AS TotalSent
        FROM raw_transactions_table
        WHERE Status = 'Confirmed'
        GROUP BY AddressOrigin) AS subquery1,
        (SELECT AddressDestination, sum(TotalSent) AS TotalReceived
        FROM raw_transactions_table
        WHERE Status = 'Confirmed'
        GROUP BY AddressDestination) AS subquery2
        WHERE subquery1.AddressOrigin = subquery2.AddressDestination
        ORDER BY Balance DESC;
        ''')
