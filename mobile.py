import dash
from dash import html

import feffery_antd_components as fac


from feffery_dash_utils.style_utils import style

from components import home, fire_maps, dashboard, timeline, about,sit_reach
import dash_bootstrap_components as dbc

def render():
    return html.Div(
        [
            html.Div(
                [
                    fac.AntdFlex(
                        fac.AntdTitle("个人健康数据中心v0.1.0", level=4, style={"margin": "0px"}),
                        justify="center",
                    ),
                    fac.AntdFlex(
                        fac.AntdTitle("self-health-data-center", level=4, style={"margin": "0px"}),
                        justify="center",
                    ),
                ],
                # style=style(height="15%"),
                className="header finisher-header",
            ),
            fac.AntdTabs(
                items=[
                    # {
                    #     "key": "base",
                    #     "label": "首页",
                    #     "children": home.render(),
                    # },
                    {
                        "key": "sit_reach",
                        "label": "坐位体前屈",
                        "children": sit_reach.render(),
                    },
                    {
                        "key": "medical",
                        "label": "医疗检测数据",
                        # "children": fire_maps.render(),
                    },
                    {
                        "key": "stats",
                        "label": "健康风险评估",
                        # "children": dashboard.render(),
                    },
                    {
                        "key": "about",
                        "label": "关于",
                        # "children": about.render(),
                    },
                ],
                # defaultActiveKey="sit_reach",
                tabPosition="top",
                centered=True,
                style=style(width="100%", overflowY="auto"),
                
                
            ),
            
        ],
        style=style(width="100%"),
        
    )
