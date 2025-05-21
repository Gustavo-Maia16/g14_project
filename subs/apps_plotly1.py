from flask import render_template, session
from classes.events import Events
from datafile import filename

import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px

def apps_plotly():
    # Creates a pandas dataframe with the orderproduct table data
    engine = create_engine('sqlite:///' + filename + 'gestao_eventos.db')
    df_registrations = pd.read_sql('Registrations', con=engine)
    # Uses groupby to obtain the total quantity order by product id
    result = df_registrations.groupby('events_id').size()
    # From the product class get the product id names
    p_ids = result.index
    p_names = []
    for p_id in p_ids:
        p_obj = Events.obj[p_id]
        p_names.append(p_obj.name)
    quantities = result.values

    # Create interactive plot with Plotly
    fig = px.bar(x=p_names, y=quantities, labels={'x': 'Product ID', 'y': 'Quantity'}, title='Total quantity ordered by product')

    plot_div = fig.to_html(full_html=False, div_id='my-plot')

    return render_template("plotly.html", plot_div=plot_div, ulogin=session.get("user"), group = session.get("group"))
