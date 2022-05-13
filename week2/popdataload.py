#!/usr/bin/env python
# coding: utf-8

# In[302]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def load_data():
    df = pd.read_excel("2020_인구조사.xlsx", engine = "openpyxl")

    # In[303]:


    df_columns = df.loc[0]
    new_columns = ['행정구역별', '총인구', '남자', '여자', '내국인-계', '내국인-남자', '내국인-여자', '외국인-계', '외국인-남자', '외국인-여자', '가구-계', '일반가구', '집단가구', '외국인가구', '주택-계', '단독주택', '아파트', '연립주택', '다세대주택', '비거주용 건물내 주택', '주택이외의 거처']


    # In[304]:


    df.columns = new_columns
    new_df = df.drop([0], axis = 0)
    new_df.reset_index(inplace=True, drop=True)


    # In[306]:


    UpRegion = ['서울특별시', '부산광역시', '대구광역시', '인천광역시', '광주광역시', '대전광역시', '울산광역시', '세종특별자치시', '경기도', '강원도', '충청북도', '충청남도', '전라북도', '전라남도', '경상북도', '경상남도', '제주특별자치도']


    # In[307]:


    Up_Index_list=[]
    for i in UpRegion:
        Up_Index_list.append(new_df.index[(new_df['행정구역별'] == i)].tolist())
    Up_Index_list.append([len(new_df['행정구역별'])])


    # In[308]:


    Update_df = new_df

    for i in range(len(Up_Index_list)-1):
        start = Up_Index_list[i][0]
        end = Up_Index_list[i+1][0]
        for j in range(start, end):
            if Update_df['행정구역별'][j] != Update_df['행정구역별'][start]:
                Update_df['행정구역별'][j] = Update_df['행정구역별'][start] + " " + Update_df['행정구역별'][j].strip()

    # In[309]:


    ch_columns = new_columns[1:]

    # In[310]:


    #print(Update_df.dtypes)
    Update_df['비거주용 건물내 주택'][100] = Update_df['비거주용 건물내 주택'][100].replace('X', '0')
    Update_df['비거주용 건물내 주택'][100] = float(Update_df['비거주용 건물내 주택'][100])

    for i in ch_columns:
        Update_df[i] = Update_df[i].astype(int)


    df = Update_df
    return df
