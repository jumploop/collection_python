#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import json
import pymysql
from sqlalchemy import create_engine

# 打开数据库连接
conn = pymysql.connect(host='localhost',
                       port=3306,
                       user='root',
                       passwd='xxxx',
                       charset='utf8'
                       )
engine = create_engine('mysql+pymysql://root:xxxx@localhost/mysql?charset=utf8')


def read_excel(file):
    return pd.read_excel(file)


def read_json(file):
    with open(file, 'r') as json_f:
        return pd.read_json(json_f)


def read_sql(table):
    sql_cmd = f'SELECT * FROM {table}'
    return pd.read_sql(sql_cmd, engine)


def read_csv(file):
    return pd.read_csv(file)
