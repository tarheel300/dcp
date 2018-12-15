from django.http import HttpResponse
from django.shortcuts import render
import db_conn as db
import pandas as pd
import json

def index(request):
    df = db.get_tbl_list()
    keys = range(df[list(df.columns.values)[0]].count())
    vals = list(df['disp_nm'])
    tbl_dict = dict(zip(keys,vals))
    return render(request, 'index.html', {'tbls':tbl_dict.items()})

def test(request):
    return render(request, 'test.html')

def grid(request):
    if request.method == 'GET' and 'disp_nm' in request.GET:
        tbl_nm = request.GET['disp_nm']
    else:
        tbl_nm = 'PlaceHolder Value'
    grid_data = db.get_tbl_data()
    grid_json_str = grid_data.to_json(orient='table')
    grid_json = json.loads(grid_json_str)
    col_nms = list(grid_data)
    print(grid_json)
    return render(request, 'grid.html', {
                                        'tbl_nm': tbl_nm,
                                        'col_nms': col_nms,
                                        'grid_json': grid_json_str,
                                        'row_data': grid_json['data']
                                        })
