import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from typing import Dict

from ..data.loader import DataSchema
from . import ids


def render(app: Dash, data_dict: Dict[str,pd.DataFrame]) -> html.Div:
    @app.callback(
        Output(ids.TIMESERIES_CHAT, "children"),
        [
            Input(ids.ZONE_DROPDOWN, "value"),
            
        ],
    )
    def update_timeseries_chart(
        zone: str
    ) -> html.Div:
        #print(data_dict.keys())
        #print(zone in data_dict)
        filtered_data = pd.DataFrame()
        if zone in data_dict:
            filtered_data = data_dict[zone]
        #print(filtered_data)
        if filtered_data.shape[0] == 0:
            return html.Div("No data selected.", id=ids.TIMESERIES_CHAT), 

        # pie = go.Pie(
        #     labels=filtered_data[DataSchema.CATEGORY].tolist(),
        #     values=filtered_data[DataSchema.AMOUNT].tolist(),
        #     hole=0.5,
        # )


        # fig = px.bar(
        #     create_pivot_table(),
        #     x=DataSchema.CATEGORY,
        #     y=DataSchema.AMOUNT,
        #     color=DataSchema.CATEGORY,
        # )
        fig = px.line(
            filtered_data,
            x=DataSchema.DAY,
            y=[DataSchema.USAGE, DataSchema.LIMIT, DataSchema.RESTRICTION]
        )
            
        specific_dates = filtered_data[~(filtered_data[DataSchema.RESTRICTION].isnull())]['Day '].tolist()
        specific_dates_values = filtered_data[~(filtered_data[DataSchema.RESTRICTION].isnull())][DataSchema.RESTRICTION].tolist()
        for date,value in zip(specific_dates,specific_dates_values):
            #print(value)
            fig.add_shape(type='line', x0=date, x1=date, y0=0, y1=value, yref='y',
                        line={'color': '#00CC96', 'width': 1, 'dash': 'dot'},#dict(color='#00CC96', width=1, dash='dot'),
                        name= DataSchema.RESTRICTION)#"Restriction On")
        fig.update_layout(
            title=f"{zone} Daily Water Usage :month year format to be integrated later",#"User Input for title",
            xaxis_title="",
            yaxis_title= DataSchema.USAGE ,#"Usage (m3/day)",
            legend_title="",
            font=dict(
                family="Courier New, monospace",
                size=18,
                color="RebeccaPurple"
            )
        )
        #fig.show()
        # fig = go.Figure(data=[pie])
        # fig.update_layout(margin={"t": 40, "b": 0, "l": 0, "r": 0})
        #fig.update_traces(hovertemplate="%{label}<br>$%{value:.2f}<extra></extra>")

        return html.Div(dcc.Graph(figure=fig), id=ids.TIMESERIES_CHAT) 

    return html.Div(id=ids.TIMESERIES_CHAT)
