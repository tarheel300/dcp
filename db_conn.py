import pypyodbc as db
import pandas as pd
import cn_str

#getting connection string specific to local path / servers in cn_str lib.
cn_str = cn_str.get_cn_str()

def get_tbl_list():
    qry = 'select * from ad_hoc.dcp.lkup_tbls'
    cn = db.connect(cn_str)
    df = pd.io.sql.read_sql(qry, con=cn)
    cn.close()
    return df
