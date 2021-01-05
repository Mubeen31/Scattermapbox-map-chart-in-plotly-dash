import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import pathlib
from app import app

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()

covid = pd.read_csv(DATA_PATH.joinpath('Covid 19 data 2020-01-22 to 2020-12-25.csv'))

layout = html.Div([

html.Div([
        html.Div([


            html.P('All Countries: Covid - 19 data 2020-01-22 to 2020-12-25', className = 'fix_label', style = {'color': 'black', 'margin-top': '2px'}),
            html.P('Select Category', className = 'fix_label', style = {'color': 'black', 'margin-top': '2px'}),
            dcc.RadioItems(id = 'radio_items1',
                           labelStyle = {"display": "inline-block"},
                           options = [{'label': 'Confirmed', 'value': 'confirmed1'},
                                      {'label': 'Deaths', 'value': 'deaths1'},
                                      {'label': 'Recovered', 'value': 'recovered1'},
                                      {'label': 'Active', 'value': 'active1'}],
                           value = 'confirmed1',
                           style = {'text-align': 'center', 'color': 'black'}, className = 'dcc_compon'),

            ], className = "create_container2 four columns", style = {'margin-bottom': '20px', "margin-top": "20px"}),

    ], className = "row flex-display"),

            html.Div([
                html.Div([

                    dcc.Graph(id = 'map_3',
                              config = {'displayModeBar': 'hover'}),

                ], className = "create_container2 eight columns"),

            ], className = "row flex-display"),




], id="mainContainer", style={"display": "flex", "flex-direction": "column"})


@app.callback(Output('map_3', 'figure'),
              [Input('radio_items1', 'value')])
def update_graph(radio_items1):
    covid1 = covid.groupby(['Country/Region', 'Lat', 'Long'])[['confirmed', 'death', 'recovered', 'active']].max().reset_index()

    if radio_items1 == 'confirmed1':

        return {
            'data': [go.Scattermapbox(
                lon = covid1['Long'],
                lat = covid1['Lat'],
                mode = 'markers',
                marker = dict(
                    size = covid1['confirmed'] / 4000,
                    color = 'orange',
                    sizemode = 'area'),

                hoverinfo = 'text',
                hovertext =
                '<b>Country</b>: ' + covid1['Country/Region'].astype(str) + '<br>' +
                '<b>Lat</b>: ' + [f'{x:.4f}' for x in covid1['Lat']] + '<br>' +
                '<b>Long</b>: ' + [f'{x:.4f}' for x in covid1['Long']] + '<br>' +
                '<b>Confirmed</b>: ' + [f'{x:,.0f}' for x in covid1['confirmed']] + '<br>'

            )],

            'layout': go.Layout(
             margin={"r": 0, "t": 0, "l": 0, "b": 0},
             hovermode='closest',
             mapbox=dict(
                accesstoken='pk.eyJ1IjoicXM2MjcyNTI3IiwiYSI6ImNraGRuYTF1azAxZmIycWs0cDB1NmY1ZjYifQ.I1VJ3KjeM-S613FLv3mtkw',  # Create free account on Mapbox site and paste here access token
                center=go.layout.mapbox.Center(lat=36, lon=-5.4),
                style='open-street-map',
                # style='dark',
                zoom=1.2
             ),
             autosize=True,

        )

        }

    elif radio_items1 == 'deaths1':

        return {
            'data': [go.Scattermapbox(
                lon = covid1['Long'],
                lat = covid1['Lat'],
                mode = 'markers',
                marker = dict(
                    size = covid1['death'] / 500,
                    color = '#dd1e35',
                    sizemode = 'area'),

                hoverinfo = 'text',
                hovertext =
                '<b>Country</b>: ' + covid1['Country/Region'].astype(str) + '<br>' +
                '<b>Lat</b>: ' + [f'{x:.4f}' for x in covid1['Lat']] + '<br>' +
                '<b>Long</b>: ' + [f'{x:.4f}' for x in covid1['Long']] + '<br>' +
                '<b>Deaths</b>: ' + [f'{x:,.0f}' for x in covid1['death']] + '<br>'

            )],

             'layout': go.Layout(
             margin={"r": 0, "t": 0, "l": 0, "b": 0},
             hovermode='closest',
             mapbox=dict(
                accesstoken='pk.eyJ1IjoicXM2MjcyNTI3IiwiYSI6ImNraGRuYTF1azAxZmIycWs0cDB1NmY1ZjYifQ.I1VJ3KjeM-S613FLv3mtkw',  # Create free account on Mapbox site and paste here access token
                center=go.layout.mapbox.Center(lat=36, lon=-5.4),
                # style='open-street-map',
                style='dark',
                zoom=1.2
             ),
             autosize=True,

        )

        }

    elif radio_items1 == 'recovered1':

        return {
            'data': [go.Scattermapbox(
                lon = covid1['Long'],
                lat = covid1['Lat'],
                mode = 'markers',
                marker = dict(
                    size = covid1['recovered'] / 4000,
                    color = 'green',
                    sizemode = 'area'),

                hoverinfo = 'text',
                hovertext =
                '<b>Country</b>: ' + covid1['Country/Region'].astype(str) + '<br>' +
                '<b>Lat</b>: ' + [f'{x:.4f}' for x in covid1['Lat']] + '<br>' +
                '<b>Long</b>: ' + [f'{x:.4f}' for x in covid1['Long']] + '<br>' +
                '<b>Recovered</b>: ' + [f'{x:,.0f}' for x in covid1['recovered']] + '<br>'

            )],

            'layout': go.Layout(
             margin={"r": 0, "t": 0, "l": 0, "b": 0},
             hovermode='closest',
             mapbox=dict(
                accesstoken='pk.eyJ1IjoicXM2MjcyNTI3IiwiYSI6ImNraGRuYTF1azAxZmIycWs0cDB1NmY1ZjYifQ.I1VJ3KjeM-S613FLv3mtkw',  # Create free account on Mapbox site and paste here access token
                center=go.layout.mapbox.Center(lat=36, lon=-5.4),
                style='open-street-map',
                # style='dark',
                zoom=1.2
             ),
             autosize=True,

        )

        }

    elif radio_items1 == 'active1':

        return {
            'data': [go.Scattermapbox(
                lon = covid1['Long'],
                lat = covid1['Lat'],
                mode = 'markers',
                marker = dict(
                    size = covid1['active'] / 4000,
                    color = '#e55467',
                    sizemode = 'area'),

                hoverinfo = 'text',
                hovertext =
                '<b>Country</b>: ' + covid1['Country/Region'].astype(str) + '<br>' +
                '<b>Lat</b>: ' + [f'{x:.4f}' for x in covid1['Lat']] + '<br>' +
                '<b>Long</b>: ' + [f'{x:.4f}' for x in covid1['Long']] + '<br>' +
                '<b>Active</b>: ' + [f'{x:,.0f}' for x in covid1['active']] + '<br>'

            )],

            'layout': go.Layout(
             margin={"r": 0, "t": 0, "l": 0, "b": 0},
             hovermode='closest',
             mapbox=dict(
                accesstoken='pk.eyJ1IjoicXM2MjcyNTI3IiwiYSI6ImNraGRuYTF1azAxZmIycWs0cDB1NmY1ZjYifQ.I1VJ3KjeM-S613FLv3mtkw',  # Create free account on Mapbox site and paste here access token
                center=go.layout.mapbox.Center(lat=36, lon=-5.4),
                # style='open-street-map',
                style='dark',
                zoom=1.2
             ),
             autosize=True,

            )

        }
