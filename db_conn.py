import pypyodbc as db
import pandas as pd
import cn_str
import src_qry

cn_str = cn_str.get_cn_str()

def get_tbl_list():
    qry = src_qry.get_tbl_list_qry()
    cn = db.connect(cn_str)
    df = pd.io.sql.read_sql(qry, con=cn)
    cn.close()
    return df

def get_tbl_data():
    qry = src_qry.get_tbl_data_qry()
    cn = db.connect(cn_str)
    df = pd.io.sql.read_sql(qry, con=cn)
    cn.close()
    return df
