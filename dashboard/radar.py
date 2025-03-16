import json

from streamlit_elements import mui, nivo
from .dashboard import Dashboard


class Radar(Dashboard.Item):

    DEFAULT_DATA = [
    { "kpi": 'Satisfaction', "Dr. Adesh Suchit": 93, "Dr. Michael Brattslavsky": 61, "Dr. Naroa Gimenez": 114, "Dr. Sophia Levit": 30, "Dr. Matthew Lyn": 64},
    { "kpi": 'Risk', "Dr. Sophia Levit": 91, "Dr. Adesh Suchit": 37, "Dr. Naroa Gimenez": 72, "Dr. Michael Brattslavsky": 30, "Dr. Matthew Lyn": 88},
    { "kpi": 'Timeliness', "Dr. Michael Brattslavsky": 56, "Dr. Adesh Suchit": 95, "Dr. Sophia Levit": 99, "Dr. Matthew Lyn": 64, "Dr. Naroa Gimenez": 119},
    { "kpi": 'Peers', "Dr. Matthew Lyn": 64, "Dr. Adesh Suchit": 90, "Dr. Sophia Levit": 30, "Dr. Naroa Gimenez": 100, "Dr. Michael Brattslavsky": 56},
    { "kpi": 'Complications', "Dr. Naroa Gimenez": 119, "Dr. Matthew Lyn": 94, "Dr. Sophia Levit": 103, "Dr. Michael Brattslavsky": 56, "Dr. Adesh Suchit": 95}]

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
                mui.icon.Radar()
                mui.Typography("Provider Performance Review", sx={"flex": 1})

            with mui.Box(sx={"flex": 1, "minHeight": 0}):
                nivo.Radar(
                    data=self.data,
                    theme=self._theme["dark" if self._dark_mode else "light"],
                    keys=["Dr. Michael Brattslavsky", "Dr. Naroa Gimenez", "Dr. Sophia Levit", "Dr. Adesh Suchit", "Dr. Matthew Lyn"],
                    indexBy="kpi",
                    valueFormat=">-.2f",
                    margin={ "top": 70, "right": 80, "bottom": 40, "left": 80 },
                    borderColor={ "from": "color" },
                    gridLabelOffset=36,
                    dotSize=10,
                    dotColor={ "theme": "background" },
                    dotBorderWidth=2,
                    motionConfig="wobbly",
                    legends=[
                        {
                            "anchor": "top-left",
                            "direction": "column",
                            "translateX": -50,
                            "translateY": -40,
                            "itemWidth": 80,
                            "itemHeight": 20,
                            "itemTextColor": "#999",
                            "symbolSize": 12,
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