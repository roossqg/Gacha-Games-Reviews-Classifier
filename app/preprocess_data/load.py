import pandas as pd


def load_data() -> pd.DataFrame:

    df1 = pd.read_csv('Gacha_Reviews/Datasets/wuwa_processed.csv')
    df2 = pd.read_csv('Gacha_Reviews/Datasets/zenless_processed.csv')
    df3 = pd.read_csv('Gacha_Reviews/Datasets/hsr_processed.csv')
    df4 = pd.read_csv('Gacha_Reviews/Datasets/genshin_processed.csv')
    df5 = pd.read_csv('Gacha_Reviews/Datasets/blue_processed.csv')

    df1['game'] = 'Wuthering Waves'
    df2['game'] = 'Zenless Zone Zero'
    df3['game'] = 'Honkai Star Rail'
    df4['game'] = 'Genshin Impact'
    df5['game'] = 'Blue Archive'

    df = pd.concat([df1,df2,df3,df4,df5])

    return df

print(load_data().index)