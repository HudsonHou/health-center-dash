from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
from feffery_dash_utils.style_utils import style

from dash.dependencies import Input, Output

from server import app
from config import AppConfig
import dash_bootstrap_components as dbc

import mobile


app.layout = html.Div(
    [
        fuc.FefferyDeviceDetect(id="device-detect"),
        html.Div(id="page-render", style=style(padding="5px 10px 10px 5px")),  # 上右下左 # 页面渲染
        html.Div(  # 背景图片
            style={
                "position": "fixed",
                "top": "0",
                "left": "0",
                "width": "100%",
                "height": "100%",
                # "backgroundImage": "url('/assets/imgs/image.png')",
                # 'backgroundColor': 'black',
                "backgroundSize": "cover",  # 调整背景图片的大小
                "backgroundRepeat": "no-repeat",  # 防止图片重复
                "backgroundPosition": "center",  # 居中背景图片
                # "opacity": "0.4",
                "zIndex": "-1",
            },
            # className="bg-cosmos"
        ),
    ],
    style={"width": "100%"}
)

color_mode_switch =  html.Span(
    [
        dbc.Label(className="fa fa-moon", html_for="color-mode-switch"),
        dbc.Switch( id="color-mode-switch", value=False, className="d-inline-block ms-1", persistence=True),
        dbc.Label(className="fa fa-sun", html_for="color-mode-switch"),
    ]
)



# 回调
# 移动端
@app.callback(Output("page-render", "children"), Input("device-detect", "deviceInfo"))
def device_detect_demo(deviceInfo):
    if deviceInfo is None or deviceInfo["isMobile"] is True:
        return mobile.render()
    else:
        # return [
        #     fac.AntdFlex(
        #         [
        #             fac.AntdResult(
        #                 title="非移动端",
        #                 subTitle="请切换为移动端访问",
        #                 style=style(marginTop="10vh"),
        #             )
        #         ],
        #         justify="center",
        #         align="center",
        #     )
        # ]
        return mobile.render()
    
    

server=app.server

if __name__ == "__main__":

    app.run(port=AppConfig.debug_port, debug=True)  # 调试模式
    # app.run(host="0.0.0.0", debug=False) # 生产模式
