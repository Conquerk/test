import mysqlpython

sqlh=mysqlpython.mysqlpython("db5")
dele="delete from t1 where name='小姐'"
sqlh.zhixing(dele)