def get_rank(df, area, feature):
    p_df = df.iloc[:,:]
    d_l = []
    if 2 == len(area.split()):
        d_n = area.split()[0]
        for i in range(len(p_df.index)):
            tmp = p_df['행정구역별'][i].split()
            if 2 == len(tmp) and tmp[0] == d_n:
                if tmp[1] not in ('읍부', '면부', '동부'):
                    d_l.append(i)
    else:
        for i in range(len(p_df.index)):
            tmp = p_df['행정구역별'][i].split()
            if 1 == len(tmp):
                if tmp[0] not in ('전국', '읍부', '면부', '동부'):
                    d_l.append(i)
    p_df = p_df.iloc[d_l,:]
    p_df = p_df.loc[:, ['행정구역별', feature]]
    p_df['rank_by_feature'] = p_df[feature].rank(method='min', ascending=False)
    return p_df.loc[p_df['행정구역별'] == area]['rank_by_feature'].values[0]


def get_num_of_districts(df, area = '전국'):
    a = df.iloc[:, [0]].to_numpy()
    cnt = 0
    if area == '전국':
        for i in range(len(a)):
            tmp = a[i][0].split()
            if 1 == len(tmp):
                if tmp[0] not in ('전국', '읍부', '면부', '동부'):
                    cnt+=1
    else:
        for i in range(len(a)):
            tmp = a[i][0].split()
            if 2 == len(tmp) and tmp[0] == area:
                if tmp[1] not in ('읍부', '면부', '동부'):
                    cnt+=1
    return cnt