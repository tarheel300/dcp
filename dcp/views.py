from django.http import HttpResponse
from django.shortcuts import render
import db_conn as db
import pandas as pd

def index(request):
    df = db.get_tbl_list()
    keys = range(df[list(df.columns.values)[0]].count())
    vals = list(df['disp_nm'])
    tbl_dict = dict(zip(keys,vals))
    return render(request, 'index.html', {'tbls':tbl_dict.items()})
