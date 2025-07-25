import conf # config-tiedosto
import pandas as pd
filters = conf.filters
home = conf.settings["HOME"]
signum_id = conf.settings["signum_id"]
available_index = conf.settings["available_index"]
reservation_index = conf.settings["reservation_index"]
signum_index = conf.settings["signum_index"]
name_index = conf.settings["name_index"]
type_index = conf.settings["type_index"]
loc_index = conf.settings["loc_index"]
class ConfigurationError(Exception):
    def __init__(self, message):
        super().__init__(message)
def parse_signum(parsable_data: str):
    #if conf.settings["parse_signum"].lower() == "true":
    #    return parsable_data
    print(parsable_data)
    indexes = []
    temp = []
    pairs = []
    track = False
    if parsable_data[-1] != " ":
        parsable_data = parsable_data + " "
        
    if parsable_data[0] != " ":
        parsable_data = " " + parsable_data
    for i, char in enumerate(parsable_data):
        if char == " ":
            indexes.append(i)
    for i in range(0,len(indexes)-1):
        element = parsable_data[indexes[i]:indexes[i+1]]
        temp.append(element.replace(" ", ""))
    for k in range(0, len(temp)-1):
        if temp[k] == signum_id or temp[k+1] == signum_id:
            if temp[k].isnumeric():
                return temp[k]
            else: return temp[k+1]
    return parsable_data # Jos paria ei löydy, tulostetaan kaikki.

def process_excel(file_path: str):
    pickup_rows = []
    df = pd.read_excel(file_path, keep_default_na=False, na_values=['jokuarvo123'])
    # pandas-kirjasto luulee että luokka NA (nuoret aikuiset) on nan-datatyyppi.
    for index, row in df.iterrows():
        delete = None 
        available = row.iloc[available_index]
        reservation = row.iloc[reservation_index]
        if reservation == home:
            delete = False
        elif reservation in available:
            delete = False
        else:
            if reservation in filters and len(filters[reservation]) > 0:
                for k in filters[reservation]:
                    if k in available:
                        delete = True
                        break
        if not delete:
            pickup_rows.append({
                "res": reservation,
                "signum": parse_signum(row.iloc[signum_index]),
                "type": row.iloc[type_index],
                "name": row.iloc[name_index],
                "loc": row.iloc[loc_index]
            })
    return pickup_rows