import json

from streamlit_elements import nivo, mui
from .dashboard import Dashboard


class Pie(Dashboard.Item):

    DEFAULT_DATA = [
        { "id": "00:00 - 03:00", "label": "00:00 - 03:00", "value": 465, "color": "hsl(128, 70%, 50%)" },
        { "id": "04:00 - 07:00", "label": "04:00 - 07:00", "value": 140, "color": "hsl(178, 70%, 50%)" },
        { "id": "08:00 - 11:00", "label": "08:00 - 11:00", "value": 40, "color": "hsl(322, 70%, 50%)" },
        { "id": "12:00 - 15: 00", "label": "12:00 - 15:00", "value": 439, "color": "hsl(117, 70%, 50%)" },
        { "id": "16:00 - 19:00", "label": "16:00 - 19:00", "value": 366, "color": "hsl(286, 70%, 50%)" },
        { "id": "20:00 - 23:00", "label":  "20:00 - 23:00", "value": 200, "color": "hsl(186, 70%, 50%)"}]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._theme = {
            "dark": {
                "background": "#252526",
                "textColor": "#FAFAFA",
                "tooltip": {
                    "container": {
                        "background": "#3F3F3F",
                        "color": "FAFAFA",
                    }
                }
            },
            "light": {
                "background": "#FFFFFF",
                "textColor": "#31333F",
                "tooltip": {
                    "container": {
                        "background": "#FFFFFF",
                        "color": "#31333F",
                    }
                }
            }
        }

    def __call__(self):
        self.data = self.DEFAULT_DATA

        with mui.Paper(key=self._key, sx={"display": "flex", "flexDirection": "column", "borderRadius": 3, "overflow": "hidden"}, elevation=1):
            with self.title_bar():
                mui.icon.PieChart()
                mui.Typography("Complications by Hour Visitation", sx={"flex": 1})

            with mui.Box(sx={"flex": 1, "minHeight": 0}):
                nivo.Pie(
                    data=self.data,
                    theme=self._theme["dark" if self._dark_mode else "light"],
                    margin={ "top": 40, "right": 80, "bottom": 80, "left": 80 },
                    innerRadius=0.5,
                    padAngle=0.7,
                    cornerRadius=3,
                    activeOuterRadiusOffset=8,
                    borderWidth=1,
                    borderColor={
                        "from": "color",
                        "modifiers": [
                            [
                                "darker",
                                0.2,
                            ]
                        ]
                    },
                    arcLinkLabelsSkipAngle=10,
                    arcLinkLabelsTextColor="grey",
                    arcLinkLabelsThickness=2,
                    arcLinkLabelsColor={ "from": "color" },
                    arcLabelsSkipAngle=10,
                    arcLabelsTextColor={
                        "from": "color",
                        "modifiers": [
                            [
                                "darker",
                                2
                            ]
                        ]
                    },
                    defs=[
                        {
                            "id": "dots",
                            "type": "patternDots",
                            "background": "inherit",
                            "color": "rgba(255, 255, 255, 0.3)",
                            "size": 4,
                            "padding": 1,
                            "stagger": True
                        },
                        {
                            "id": "lines",
                            "type": "patternLines",
                            "background": "inherit",
                            "color": "rgba(255, 255, 255, 0.3)",
                            "rotation": -45,
                            "lineWidth": 6,
                            "spacing": 10
                        }
                    ],
                    fill=[
                        { "match": { "id": "00:00 - 03:00" }, "id": "dots" },
                        { "match": { "id": "04:00 - 07:00" }, "id": "dots" },
                        { "match": { "id": "08:00 - 11:00" }, "id": "dots" },
                        { "match": { "id": "12:00 - 15:00" }, "id": "dots" },
                        { "match": { "id": "16:00 - 19:00" }, "id": "lines" },
                        { "match": { "id": "20:00 - 23:00" }, "id": "lines" },
                    ],
                    legends=[
                        {
                            "anchor": "bottom",
                            "direction": "row",
                            "justify": False,
                            "translateX": 0,
                            "translateY": 56,
                            "itemsSpacing": 0,
                            "itemWidth": 100,
                            "itemHeight": 18,
                            "itemTextColor": "#999",
                            "itemDirection": "left-to-right",
                            "itemOpacity": 1,
                            "symbolSize": 18,
                            "symbolShape": "circle",
                            "effects": [
                                {
                                    "on": "hover",
                                    "style": {
                                        "itemTextColor": "#000"
                                    }
                                }
                            ]
                        }
                    ]
                )