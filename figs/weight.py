import plotly.express as px

def fig(title:str):
    df = px.data.stocks()
    fig = px.line(df, x='date', y="GOOG")
    fig.update_layout(
        # dragmode="zoom",
         title={
            "text": title,  # 标题内容
            "x": 0.5,              # 水平居中（0.5 表示中间）
            "xanchor": "center",   # 对齐方式为居中
            "yanchor": "top",      # 垂直方向顶部对齐（默认）
            "font": {"size": 14}   # 字体大小
        },
        hovermode="x",
        # legend=dict(traceorder="reversed"),
        height=200,
        # template="plotly_dark",
        template="plotly_white",
        margin=dict(
            t=30,
            b=0,
            l=0,
            r=0
        ),
        # 背景透明
        paper_bgcolor='rgba(0,0,0,0)',
        # 图形透明
        plot_bgcolor='rgba(0,0,0,0)',
         xaxis=dict(
            title=None,          # 隐藏 X 轴标题
            ticksuffix=" m",     # X 轴标签后添加 " m"
            tickformat=".1f"     # 可选：控制小数位数为 1 位
        ),
        yaxis=dict(
            title=None,          # 隐藏 Y 轴标题
            ticksuffix=" s"      # Y 轴标签后添加 " s"
        )
        
    )
        
        
        
    return fig