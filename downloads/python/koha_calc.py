import numpy as np
from io import BytesIO
from matplotlib.figure import Figure
import base64
from collections import Counter
# Luodaan erilaisia kuvaajia ja dataa ladatuista varaustiedoista.
# Datat:
# Nideluokka (kirja, cd, paikka (aikuiset nuoret), varauspaikka

def create_bar_chart(data, title, xlabel, ylabel):
    fig = Figure(figsize=(6,3))
    ax = fig.subplots()
    items = list(data.items())
    labels, values = zip(*items)
    ax.bar(labels, values, width=0.4)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.tick_params(axis='x', rotation=45)
    fig.tight_layout()
    buffer = BytesIO()
    with BytesIO() as buffer:
        fig.savefig(buffer, format="png", dpi=600)
        buffer.seek(0)
        img_base64 = base64.b64encode(buffer.read()).decode("utf-8")
    return img_base64
def calc_unique_count(excel_data):
    reservations_total = len(excel_data)
    # Counter on kätevä - laskee jokaisen uniikin arvon määrän mitä siihen tungetaan!
    reservations_by_lib = Counter(row["res"] for row in excel_data)
    reservations_by_type = Counter(row["type"] for row in excel_data)
    reservations_by_loc = Counter(row["loc"] for row in excel_data)
    reservations_by_signum = Counter(str(row["signum"]) for row in excel_data)
    graphs = {
        "reservations_by_lib": create_bar_chart(dict(reservations_by_lib),"Varaukset kirjastoittain", "Kirjasto", "Määrä"),
        "reservations_by_type": create_bar_chart(dict(reservations_by_type), "Varaukset nideluokittain", "Nideluokka", "Määrä"),
        "reservations_by_loc": create_bar_chart(dict(reservations_by_loc), "Varaukset sijainnittain", "Sijainti", "Määärä"),
        "reservations_by_signum": create_bar_chart(dict(reservations_by_signum), "Varaukset signumeittain", "Signum", "Määrä")
    }
    return {
        "total": reservations_total,
        "reservations_by_lib": dict(reservations_by_lib),
        "reservations_by_type": dict(reservations_by_type),
        "reservations_by_loc": dict(reservations_by_loc),
        "reservations_by_signum": dict(reservations_by_signum),
        "graphs": graphs
    }
