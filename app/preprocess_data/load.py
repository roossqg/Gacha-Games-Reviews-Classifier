import pandas as pd

from paths import DATASETS_DIR


def load_data() -> pd.DataFrame:

    df1 = pd.read_csv(DATASETS_DIR / "wuwa_processed.csv")
    df2 = pd.read_csv(DATASETS_DIR / "zenless_processed.csv")
    df3 = pd.read_csv(DATASETS_DIR / "hsr_processed.csv")
    df4 = pd.read_csv(DATASETS_DIR / "genshin_processed.csv")
    df5 = pd.read_csv(DATASETS_DIR / "blue_processed.csv")

    df1['game'] = 'Wuthering Waves'
    df2['game'] = 'Zenless Zone Zero'
    df3['game'] = 'Honkai Star Rail'
    df4['game'] = 'Genshin Impact'
    df5['game'] = 'Blue Archive'

    df = pd.concat([df1,df2,df3,df4,df5])

    return df