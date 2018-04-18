# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 13:58:34 2018

@author: WELCOME
"""

import numpy as np

import os
from sklearn.linear_model import LinearRegression

from sklearn import ensemble

import pickle

from flask import Flask
from flask import request
from sklearn.externals import joblib
app = Flask(__name__)

@app.route('/nch_bene_ip_ddctbl_amt_predictor',methods = ['POST'])
def postJsonHandler():
    content = request.get_json()
    CLM_ID = content["CLM_ID"]
    NCH_PRMRY_PYR_CLM_PD_AMT = content["NCH_PRMRY_PYR_CLM_PD_AMT"]
    CLM_PASS_THRU_PER_DIEM_AMT = content["CLM_PASS_THRU_PER_DIEM_AMT"]
    NCH_BENE_IP_DDCTBL_AMT = content["NCH_BENE_IP_DDCTBL_AMT"]
    NCH_BENE_PTA_COINSRNC_LBLTY_AM = content["NCH_BENE_PTA_COINSRNC_LBLTY_AM"]
    NCH_BENE_BLOOD_DDCTBL_LBLTY_AM = content["NCH_BENE_BLOOD_DDCTBL_LBLTY_AM"]
    CLM_UTLZTN_DAY_CNT = content["CLM_UTLZTN_DAY_CNT"]
    CLM_YEAR_MONTH_CLM_FROM_DT_CAT = content["CLM_YEAR_MONTH_CLM_FROM_DT_CAT"]
    CLM_YEAR_MONTH_CLM_THRU_DT_CAT = content["CLM_YEAR_MONTH_CLM_THRU_DT_CAT"]
    NCH_BENE_DSCHRG_DT_YEAR_MONTH_CAT = content["NCH_BENE_DSCHRG_DT_YEAR_MONTH_CAT"]
    ICD9_PRCDR_CD_1_CAT    = content["ICD9_PRCDR_CD_1_CAT"]
    ICD9_DGNS_CD_2_CAT = content["ICD9_DGNS_CD_2_CAT"]
    ICD9_DGNS_CD_3_CAT = content["ICD9_DGNS_CD_3_CAT"]
    DESYNPUF_ID_CAT = content["DESYNPUF_ID_CAT"]
    CLM_ADMSN_DT_CAT = content["CLM_ADMSN_DT_CAT"]
    nch_bene_ip_ddctbl_amt_predictor = joblib.load('CLM_PMT_AMT_Predictor.pkl')
    predictor = np.array([CLM_ID,NCH_PRMRY_PYR_CLM_PD_AMT,CLM_PASS_THRU_PER_DIEM_AMT,NCH_BENE_IP_DDCTBL_AMT,NCH_BENE_PTA_COINSRNC_LBLTY_AM,NCH_BENE_BLOOD_DDCTBL_LBLTY_AM,CLM_UTLZTN_DAY_CNT,CLM_YEAR_MONTH_CLM_FROM_DT_CAT,CLM_YEAR_MONTH_CLM_THRU_DT_CAT,NCH_BENE_DSCHRG_DT_YEAR_MONTH_CAT,ICD9_PRCDR_CD_1_CAT,ICD9_DGNS_CD_2_CAT,ICD9_DGNS_CD_3_CAT,DESYNPUF_ID_CAT,CLM_ADMSN_DT_CAT])
    result = nch_bene_ip_ddctbl_amt_predictor.predict(predictor)
    return result

if __name__ == '__main__':
    port = int(os.environ.get('PORT',5000))
    app.debug = True
    app.run(host = '192.168.0.102',port=port)
