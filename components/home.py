# dash
import dash
from dash import html,dcc

import feffery_antd_components as fac
import feffery_leaflet_components as flc
from feffery_dash_utils.style_utils import style

from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# 配置
from server import app
from config import MapConfig

# 地图组件
from maps.legend import Legend
from maps.basemap import Basemap
from maps import tile_selector, symbol_style
import dash_bootstrap_components as dbc
import feffery_antd_charts as fact

# 数据
from models.gpd_data import cbsdata, arcgisdata
import random

# figs
from figs import home



def render():
    return dbc.Container([
        # fac.AntdDivider('基础信息'),
        # dbc.Row([
        #     ## 添加人体图片assets\human-body.svg
        #     # dbc.Col([
        #     #      html.Img(src='/assets/imgs/human-body.svg')
        #     #     ],
        #     #     # align="center",
        #     #     width=3
        #     # ),
        #     # # dbc.Col(html.Div("One of two columns"), width=4),
        #     # dbc.Col(html.Div("One of two columns"), width=4),
        #     dbc.Col([
        #         dbc.Card(
        #             [
        #                 dbc.Row(
        #                     [
        #                         dbc.Col(
        #                             dbc.CardImg(
        #                                 src="/assets/imgs/human-body.svg",
        #                                 # className="img-fluid rounded-start",
        #                             ),
        #                             # className="col-md-3",
        #                         ),
        #                         dbc.Col(
        #                             dbc.CardBody(
        #                                 [
        #                                     # html.H4("基础信息", className="card-title"),
        #                                     html.P("年龄: 30",className="card-text"),
        #                                     html.P("性别: 男",className="card-text"),
        #                                     html.P("体重: 65kg",className="card-text"),
        #                                     html.P("身高: 180cm",className="card-text"),
        #                                     html.Small(
        #                                         "Last updated 3 mins ago",
        #                                         className="card-text text-muted",
        #                                     ),
        #                                 ]
        #                             ),
        #                             # className="col-md-9",
        #                         ),
        #                     ],
        #                     align="center",
                            
        #                     # className="g-0 d-flex align-items-center",
        #                 )
        #             ],
        #             # className="mb-3",
        #             style={"maxWidth": "540px"},
        #             class_name="blur-box"
        #         )
        #         ],width="auto",
        #     )
        #     ],
        #     justify="center",
        # ),
        # dbc.Row([
        #     dbc.Col([
        #         fact.AntdLine(
        #             data=[
        #                 {
        #                     'date': f'2020-0{i}',
        #                     'y': random.randint(0, 100),
        #                     'type': f'item{j}',
        #                 }
        #                 for i in range(1, 10)
        #                 for j in range(1, 4)
        #             ],
        #             xField='date',
        #             yField='y',
        #             seriesField='type',
        #             color=['#ff4444', '#99bb33', '#ffbb55'],
                    
        #         )
        #         ],width="auto",style={"maxWidth": "540px"},
        #     ),
        #     ],
        #     justify="center",  
        # ),
        
        dbc.Row([
            dbc.Col([
                dcc.Graph(figure=home.render(),className="blur-box",style={"padding": "5px"}),
            ],
                width="auto",
                style={"maxWidth": "430px"},
            ),
            ],
            justify="center",  
        ),
            
    ], fluid=True,
    )


# 图层控制
@app.callback(
    Output("cbs_fire", "hidden"),
    Input("burned_area_check", "checked"),
)
def cbs_fire_check(checked):
    if checked:
        return False
    else:
        return True


@app.callback(
    Output("cbs_evac_order", "hidden"),
    Input("cbs_evac_order_check", "checked"),
)
def cbs_evac_order_check(checked):
    if checked:
        return False
    else:
        return True


@app.callback(
    Output("cbs_evac_warning", "hidden"),
    Input("cbs_evac_warning_check", "checked"),
)
def cbs_evac_warning_check(checked):
    if checked:
        return False
    else:
        return True
