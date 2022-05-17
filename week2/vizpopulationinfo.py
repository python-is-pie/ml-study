import pandas as pd
import matplotlib.pyplot as plt
from popdataload import load_data
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/gulim.ttc"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

def top5graph(df, feature):
    df = df.nlargest(5, feature)
    print(df)
    df.plot.bar(x="행정구역별", y= feature, rot=0, title = "상위 5개의 지역")
    plt.show()

def circlegraph(df, feature):
    df = df.nlargest(5, feature)
    df = df.plot.pie(figsize=(9,8), y = feature, labels = df["행정구역별"], title = "상위 5개의 지역")
    return df