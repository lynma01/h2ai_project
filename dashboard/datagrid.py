import json

from streamlit_elements import mui
from .dashboard import Dashboard


class DataGrid(Dashboard.Item):

    DEFAULT_COLUMNS = [
        { "field": 'id', "headerName": 'ID', "width": 90},
        { "field": 'provider', "headerName": "Provider name", "width": 200, "editable": True},
        { "field": 'pname', "headerName": 'Patient name', "width": 150, "editable": True},
        { "field": 'slot', "headerName": 'slot', "width": 110, "editable": True},
        { "field": 'risk', "headerName": 'Risk Score', "width": 150, "Editable": True},
        { "field": 'recommendation', "headerName": 'Recommendation', "width": 200, "Editable": True}
    ]

    DEFAULT_ROWS = [
        { "id": 1, "provider": "Dr. Michael Brattslavsky", "pname": 'Jon Snow',  "slot": "12:00 - 02:30", "risk": "High!", "recommendation": "Change Recommended!"},
        { "id": 2, "provider": "Dr. Naroa Gimenez", "pname": 'Cersei Lannister', "slot": "12:00 - 12:30", "risk": "Low", "recommendation": "No Change"},
        { "id": 3, "provider": "Dr. Adesh Suchit", "pname": 'Jaime Lannister', "slot": "08:00 - 08:30", "risk": "Medium", "recommendation": "Potential Change"},
        { "id": 4, "provider": "Dr. Matthew Lyn", "pname": 'Arya Stark', "slot": "14:00 - 15:00", "risk": "High!", "recommendation": "Change Recommended!"},
        { "id": 5, "provider": "Dr. Naroa Gimenez", "pname": 'Daenerys Targaryen', "slot": "02:00 - 02:30", "risk": "Medium", "recommendation": "Potential Change"},
        { "id": 6, "provider": "Dr. Adesh Suchit", "pname": 'Melisandre', "slot": "08:00 - 10:30", "risk": "Low", "recommendation": "No Change"},
        { "id": 7, "provider": "Dr. Sophia Levit", "pname": 'Clifford Ferrara', "slot": "02:00 - 02:30", "risk": "High!", "recommendation": "Change Recommended!"},
        { "id": 8, "provider": "Dr. Sophia Levit", "pname": 'Rossini Frances', "slot": "02:00 - 02:30", "risk": "Low", "recommendation": "No Change"},
        { "id": 9, "provider": "Dr. Michael Brattslavsky", "pname": 'Harvey Roxie', "slot": "02:00 - 02:30", "risk": "Medium", "recommendation": "Potential Change"},
    ]

    def _handle_edit(self, params):
        print(params)

    def __call__(self):
        data = self.DEFAULT_ROWS

        with mui.Paper(key=self._key, sx={"display": "flex", "flexDirection": "column", "borderRadius": 3, "overflow": "hidden"}, elevation=1):
            with self.title_bar(padding="10px 15px 10px 15px", dark_switcher=False):
                mui.icon.ViewCompact()
                mui.Typography("Patient Schedule")

            with mui.Box(sx={"flex": 1, "minHeight": 0}):
                mui.DataGrid(
                    columns=self.DEFAULT_COLUMNS,
                    rows=data,
                    pageSize=5,
                    rowsPerPageOptions=[5],
                    checkboxSelection=True,
                    disableSelectionOnClick=True,
                    onCellEditCommit=self._handle_edit)