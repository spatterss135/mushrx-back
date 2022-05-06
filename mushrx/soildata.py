
import pandas as pd

def getHelp(facts):
    data = [list(x.values()) for x in facts]
    for i in range(len(data)):
        for j in range(len(data[i])):
            if type(data[i][j]) is dict:
                data[i][j] = data[i][j]['noaa']
    df = pd.DataFrame(data, columns=["soilMoisture", "soilMoisture10cm", "soilTemperature", "soilTemperature10cm", "time"])
    df = df[df['time'].str.contains('12:')].to_csv()
    print(df)
    return df