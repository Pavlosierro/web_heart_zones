import pandas as pd


def read_hr_from_csv(path) -> list[int]:
    df = pd.read_csv(path)
    result = df['Date'][2:].tolist()
    res = []
    for i, x in enumerate(result):
        try:
            res.append(int(x))
        except:
            pass
    return res
