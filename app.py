import streamlit as st

from streamlit import session_state as state
from streamlit_elements import elements, mui
from types import SimpleNamespace

from dashboard.dashboard import Dashboard
from dashboard.datagrid import DataGrid
from dashboard.editor import Editor
from dashboard.radar import Radar
from dashboard.pie import Pie

def main():
    st.title("Orderli: Scheduler for Patient Safety, and Risk Management")
    col1, col2 = st.columns(2)

    with col1:
        st.image(image="images/logo.jpeg")

    with col2:
        st.write("""
        Orderli is a cutting-edge application designed for hospital risk managers. By leveraging machine learning, it predicts providers’ risk of complication and suggests optimal scheduling adjustments. This ensures that the right providers are assigned to the right procedures, maximizing patient safety and clinical efficacy.

        - **Optimized Scheduling:**  
        By aligning provider risk with procedure scheduling, the app ensures that patients receive care from providers best suited for the procedure. This optimization leads to higher treatment efficacy and a reduction in complications.

        - **Proactive Risk Identification:**  
        The machine learning model continuously assesses risk, identifying providers who may present a higher likelihood of complications. This allows for early intervention before risks translate into actual safety issues.

        - **Reduction of Complication Rates:**  
        By suggesting rescheduling of certain procedures based on risk prediction, Orderli directly contributes to minimizing complications. This systematic approach to risk management plays a key role in enhancing patient safety.

        - **Improved Resource Management:**  
        The app aids in allocating provider resources more effectively, ensuring that the most suitable staff are scheduled for procedures. This targeted approach helps mitigate risks and enhances operational efficiency.

        - **Streamlined Decision-Making:**  
        Orderli provides clear, actionable insights, allowing risk managers to make informed scheduling decisions without the need for extensive manual analysis.

        - **Transparency and Accountability:**  
        Detailed risk reports and scheduling recommendations give hospital administrators a transparent view of the decision-making process. This transparency supports better governance and adherence to safety protocols.

        - **Operational Efficiency:**  
        With automated risk assessments and scheduling suggestions, risk managers can focus on broader strategic initiatives rather than getting bogged down in day-to-day scheduling challenges.

        """)
    st.write("---")

    st.header("Hospital Risk Manager View:")
    
    col3, col4 = st.columns(2)

    with col3:
        st.write("""
            This app view is designed to provide risk managers with a clear, data-driven overview of both clinical performance and operational efficiency. It integrates multiple visual and data elements to support proactive decision-making and improved patient outcomes.

            - **Holistic Overview:**  
            Combining visual summaries, detailed reports, and granular data grids, the app view provides a comprehensive picture of both clinical outcomes and operational efficiency.
            
            - **Proactive Risk Mitigation:**  
            With clear visual indicators and actionable insights, hospital managers can quickly address high-risk periods and underperforming areas, thus reducing complications.
            
            - **Optimized Resource Allocation:**  
            The integrated view empowers managers to allocate staffing and other resources more effectively, aligning clinical expertise with patient needs.
            
            - **Data-Driven Strategy:**  
            By leveraging real-time data and predictive insights, hospital managers can formulate informed strategies to continually enhance patient safety and care quality.
        """)
        
    with col4:
        st.image("images/dr_chad.png", width=600)

    if "w" not in state:
        board = Dashboard()
        w = SimpleNamespace(
            dashboard=board,
            pie=Pie(board, 0, 0, 5, 7, minW=3, minH=4),
            radar=Radar(board, 5, 0, 7, 7, minW=3, minH=4),
            data_grid=DataGrid(board, 0, 4, 10, 7, minW=5, minH=4))

        state.w = w

    else:
        w = state.w

    with elements("demo"):
        with w.dashboard(rowHeight=57):
            w.pie()
            w.radar()
            w.data_grid()

if __name__ == "__main__":
    st.set_page_config(layout="wide")
    main()
