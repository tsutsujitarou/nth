#!/usr/bin/python3

# -*- coding:utf-8 -*- 
from datetime import datetime
 
def lambda_handler(event, context):
    input_date = datetime.today()
    yukari = '田村ゆかり'
    birth = datetime(1976, 2, 27)
    month_17 = ((input_date.year - birth.year) - 17) * 12 + (input_date.month - birth.month)
    if input_date.day < birth.day: month_17 -= 1
    return({
        "statusCode": "200",
        "headers" : {},
        "body" : f"{input_date.strftime('%Y年%m月%d日')}の{yukari}は17歳と{month_17}ヶ月"
    })
