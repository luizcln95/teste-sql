drop_transactions_table = ('''
            DROP TEMPORARY TABLE IF EXISTS transactions_table;
            ''')

transactions_table = ('''
                    CREATE TEMPORARY TABLE transactions_table
                    SELECT DISTINCT IdTransaction, AddressOrigin, AddressDestination, 
                    CAST(REPLACE(TotalSent, ',', '') AS DECIMAL(10,2)) AS TotalSent, 
                    Status, 
                    CAST(SentDate AS DATETIME) AS SentDate
                    FROM raw_transactions_table
                    WHERE TotalSent <> 0.00;
                    ''')

drop_fees_table = ('''
            DROP TEMPORARY TABLE IF EXISTS fees_table;
            ''')

fees_table = ('''
            CREATE TEMPORARY TABLE fees_table
            SELECT IdTransaction, AddressOrigin, TotalSent, Status, SentDate, 
            MONTH(SentDate) AS TransactionMonth, YEAR(SentDate) AS TransactionYear,
            CASE 
                WHEN TotalSent > 833000.00 THEN 2.00
                WHEN TotalSent > 670000.00 THEN 4.00
                WHEN TotalSent > 500000.00 THEN 5.00
                WHEN TotalSent > 340000.00 THEN 6.00
                WHEN TotalSent > 160000.00 THEN 8.00
                ELSE 10.00 END 
                AS FeePercentage
            FROM transactions_table;
            ''')

f1_q1 = ('''
        SELECT AddressOrigin, SUM(TotalSent) AS TotalSentSum
        FROM transactions_table
        WHERE Status = 'Confirmed'
        GROUP BY AddressOrigin
        ORDER BY TotalSentSum DESC
        LIMIT 1;
        ''')

f1_q2 = ('''
        SELECT DAYOFMONTH(SentDate) as MonthDay, SUM(TotalSent) AS TotalSentSum
        FROM transactions_table
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
        FROM transactions_table
        WHERE Status = 'Confirmed'
        GROUP BY WeekDay
        ORDER BY TransactionsCount DESC
        LIMIT 1;
        ''')

f1_q4 = ('''
        SELECT * FROM transactions_table
        WHERE AddressOrigin = AddressDestination;
        ''')

f1_q5 = ('''
        WITH cte AS (SELECT IdTransaction, AddressOrigin, AddressDestination, 
        CAST(REPLACE(TotalSent, ',', '') AS DECIMAL(10,2)) AS TotalSent, 
        Status, CAST(SentDate AS DATETIME) AS SentDate
        FROM raw_transactions_table)
        SELECT AddressOrigin, (TotalReceived - TotalSent) AS Balance
        FROM 
        (SELECT AddressOrigin, sum(TotalSent) AS TotalSent
        FROM cte
        WHERE Status = 'Confirmed'
        GROUP BY AddressOrigin) AS subquery1,
        (SELECT AddressDestination, sum(TotalSent) AS TotalReceived
        FROM cte
        WHERE Status = 'Confirmed'
        GROUP BY AddressDestination) AS subquery2
        WHERE subquery1.AddressOrigin = subquery2.AddressDestination
        ORDER BY Balance DESC
        LIMIT 1;
        ''')

f2_q1 = ('''
        SELECT AddressOrigin, SUM(((TotalSent * FeePercentage) / 100)) AS FeeAmount
        FROM fees_table
        WHERE TransactionMonth = 1 AND TransactionYear = 2021
        GROUP BY AddressOrigin
        ORDER BY FeeAmount DESC
        LIMIT 1;
        ''')

f2_q2 = ('''
        SELECT AddressOrigin, SUM(((TotalSent * FeePercentage) / 100)) AS FeeAmount
        FROM fees_table
        WHERE TransactionMonth = 2 AND TransactionYear = 2021
        GROUP BY AddressOrigin
        ORDER BY FeeAmount DESC
        LIMIT 1;
        ''')

f2_q3 = ('''
        SELECT IdTransaction, ((TotalSent * FeePercentage) / 100) AS Fee
        FROM fees_table
        ORDER BY Fee DESC
        LIMIT 1;
        ''')

f2_q4 = ('''
        SELECT AVG((TotalSent * FeePercentage) / 100) AS AvgFee
        FROM fees_table;
        ''')
