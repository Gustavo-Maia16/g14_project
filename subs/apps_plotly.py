from flask import render_template, session
from classes.venue import Venue
from datafile import filename

import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px

def apps_plotly():
    # Conexão à base de dados SQLite
    engine = create_engine('sqlite:///' + filename + 'gestao_eventos.db')
    
    # Leitura da tabela Venue
    df_venue = pd.read_sql('Venue', con=engine)
    
    # Agrupamento por ID e soma das capacidades (caso existam repetidos)
    result = df_venue.groupby('id')['capacity'].sum()
    
    # Obtenção das localizações a partir do dicionário Venue.obj
    p_ids = result.index
    p_locations = []
    for p_id in p_ids:
        venue_obj = Venue.obj.get(p_id)
        p_locations.append(venue_obj.location if venue_obj else f"Local {p_id}")
    
    capacities = result.values

    # Criar gráfico de barras (sem legenda de cor)
    fig = px.bar(
        x=p_locations,
        y=capacities,
        labels={'x': 'Localização', 'y': 'Capacidade Máxima'},
        title='Capacidade Máxima por Localização de Evento'
    )

    # Estilo do gráfico
    fig.update_traces(marker_color='lightskyblue', marker_line_color='black', marker_line_width=1)

    # Layout personalizado
    fig.update_layout(
        coloraxis_showscale=False,  # Remove legenda de cor
        title_font_size=24,
        title_font_family='Arial',
        title_x=0.5,
        plot_bgcolor='white',
        paper_bgcolor='#f4f4f4',
        font=dict(
            family="Verdana",
            size=14,
            color="#222"
        ),
        xaxis=dict(
            tickangle=-45,
            title='Localização',
            title_font=dict(size=18),
            tickfont=dict(size=12),
        ),
        yaxis=dict(
            title='Capacidade Máxima',
            title_font=dict(size=18),
            tickfont=dict(size=12),
            gridcolor='lightgrey'
        ),
        margin=dict(l=40, r=30, t=80, b=150)
    )

    # Gerar HTML
    plot_div = fig.to_html(full_html=False, div_id='my-plot')

    # Renderizar página
    return render_template("plotly.html", plot_div=plot_div, ulogin=session.get("user"), group=session.get("group"))
