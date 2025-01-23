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
from figs import home,weight
from datetime import date


def render():
    return dbc.Container([
        
        dbc.Row([
            dbc.Col([
                dcc.Graph(figure=weight.fig(title="体重"),config={'displayModeBar': False},className="glass-box"),
                ],
                width="100%",
            ),
            ],
            justify="center",style={"marginBottom":10}
        ),
        # fac.AntdDivider(""),
        
        dbc.Row([
            dbc.Col([
                dcc.Graph(figure=weight.fig(title="深睡时长"),config={'displayModeBar': False},className="glass-box"),
                ],
                width="100%",
            ),
            ],
            justify="center", style={"marginBottom":10} 
        ),
        # fac.AntdDivider("深睡时长"),
        
        dbc.Row([
            dbc.Col([
                dcc.Graph(figure=weight.fig(title="血肌酐"),config={'displayModeBar': False},className="glass-box"),
                ],
                width="100%",
            ),
            ],
            justify="center",  style={"marginBottom":10}
        ),
        # fac.AntdDivider("体重"),
        #  dbc.Row([
        #     dbc.Col([
        #         dcc.Graph(figure=home.render(),config={'displayModeBar': False}),
        #         ],
        #         width="100%",
        #     ),
        #     ],
        #     justify="center",  
        # ),
        dbc.Row([
            dbc.Col([
                dbc.InputGroup([
                    dbc.Select(
                        id="select",
                        placeholder="选择指标",
                        options=[
                            {"label": "体重", "value": "1"},
                            {"label": "深睡时长", "value": "2"},
                            {"label": "血肌酐", "value": "3"},
                            {"label": "其他", "value": "3", "disabled": True},
                        ],
                    ),
                    dbc.Input(id="input-group-button-input", placeholder="输入数值"),
                    # dbc.Button("确认添加", color="outline-light"),
                    ]
                )
                ],
            ),
            ],
            justify="center",  
        ),
        dbc.Row([
            dbc.Col([
                dbc.Button("确认添加", color="light"),
                ],
                className="d-grid gap-2"
            ),
            ],
            justify="center",  
        ), 
    ], fluid=True,style={"maxWidth": "430px"}
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

@app.callback(
    Output("tab-content", "children"), [Input("tabs", "active_tab")]
)
def tab_content(active_tab):
    
    return "This is tab {}".format(active_tab)