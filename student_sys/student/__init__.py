import pymysql

#因为操作msq数据库默认是用Mysqldb，现在就是手动指定用pymsql来操作数据库：
pymysql.install_as_MySQLdb()
