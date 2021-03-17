import sqlite3
import pymysql
from redis import StrictRedis

    
class Redis(StrictRedis):

    def __init__(self, host='localhost', port=6379, db=0, password=None, socket_timeout=None, socket_connect_timeout=None, socket_keepalive=None, socket_keepalive_options=None, connection_pool=None, unix_socket_path=None, encoding='utf-8', encoding_errors='strict', charset=None, errors=None, decode_responses=False, retry_on_timeout=False, ssl=False, ssl_keyfile=None, ssl_certfile=None, ssl_cert_reqs='required', ssl_ca_certs=None, ssl_check_hostname=False, max_connections=None, single_connection_client=False, health_check_interval=0, client_name=None, username=None):
        super().__init__(host=host, port=port, db=db, password=password, socket_timeout=socket_timeout, socket_connect_timeout=socket_connect_timeout, socket_keepalive=socket_keepalive, socket_keepalive_options=socket_keepalive_options, connection_pool=connection_pool, unix_socket_path=unix_socket_path, encoding=encoding, encoding_errors=encoding_errors, charset=charset, errors=errors, decode_responses=decode_responses, retry_on_timeout=retry_on_timeout, ssl=ssl, ssl_keyfile=ssl_keyfile, ssl_certfile=ssl_certfile, ssl_cert_reqs=ssl_cert_reqs, ssl_ca_certs=ssl_ca_certs, ssl_check_hostname=ssl_check_hostname, max_connections=max_connections, single_connection_client=single_connection_client, health_check_interval=health_check_interval, client_name=client_name, username=username)


class sqlite():
    def __init__(self,paths):
        self.path=paths
        self.connection=sqlite3.connect(database=paths)
        self.__cursor=self.connection.cursor()
    def createdbfile(self):
        with open(file=self.path,mode='w',encoding='utf-8') as f:
            f.close()
    def close(self):
        self.__cursor.close()
        self.connection.close()
    def execute(self, sql: str):
        """执行一条sql语句。"""
        self.__cursor.execute(sql)
    def executemany(self,sql):
        """执行多条sql语句。"""
        self.__cursor.executemany(sql)
    def fetchall(self):
        return self.__cursor.fetchall()
    def fetchmany(self,size:int):
        return self.__cursor.fetchmany(size)
    def fetchone(self):
        return self.__cursor.fetchone()


class mysql():
    def __init__(self,**kwargs):
        super().__init__()
        self.connection=pymysql.connect(**kwargs)
        self.__cursor=self.connection.cursor()
    def close(self):
        self.__cursor.close()
        self.connection.close()    
    def execute(self, sql: str):
        """执行一条sql语句。"""
        self.__cursor.execute(sql)
    def executemany(self,sql):
        """执行多条sql语句。"""
        self.__cursor.executemany(sql)
    def fetchall(self):
        return self.__cursor.fetchall()
    def fetchmany(self,size:int):
        return self.__cursor.fetchmany(size)
    def fetchone(self):
        return self.__cursor.fetchone()

class DbFactory():
    def __init__(self,dbtype,**kwargs):
        super().__init__()
        self.dbtype=dbtype
        self.connectionstring={}
        if self.dbtype=='redis':
            self.__db=Redis(**kwargs)
            self.connectionstring={'host':'localhost','port':6379,'db':0,'password':None,'socket_timeout':None,'socket_connect_timeout':None,'socket_keepalive':None,'socket_keepalive_options':None,'connection_pool':None,'unix_socket_path':None,'encoding':'utf-8','encoding_errors':'strict','charset':None,'errors':None,'decode_responses':False,'retry_on_timeout':False,'ssl':False,'ssl_keyfile':None,'ssl_certfile':None,'ssl_cert_reqs':'required','ssl_ca_certs':None,'ssl_check_hostname':False,'max_connections':None,'single_connection_client':False,'health_check_interval':0,'client_name':None,'username':None}
            for key,value in kwargs.items():
                self.connectionstring[key]=value
        if self.dbtype=='sqlite':
            self.__db=sqlite(**kwargs)
            for key,value in kwargs.items():
                self.connectionstring[key]=value
        if self.dbtype=='mysql':
            self.__db=mysql(**kwargs)
            for key,value in kwargs.items():
                self.connectionstring[key]=value
             
    def createdb(self):
        return self.__db


   


        



