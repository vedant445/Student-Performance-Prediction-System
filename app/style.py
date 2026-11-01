import streamlit as st


def load_css():

    st.markdown(
        """
        <style>

        .main{
            background-color:#f8f9fa;
        }

        h1,h2,h3{
            color:#0d6efd;
        }

        .prediction-box{
            padding:20px;
            border-radius:15px;
            background:#ffffff;
            box-shadow:0px 2px 8px rgba(0,0,0,0.15);
            text-align:center;
            margin-top:15px;
        }

        .metric-box{
            background:white;
            padding:15px;
            border-radius:12px;
            text-align:center;
            box-shadow:0px 2px 6px rgba(0,0,0,0.15);
        }

        .recommend-box{
            background:#eafaf1;
            border-left:6px solid green;
            padding:15px;
            border-radius:10px;
        }

        .warning-box{
            background:#fdecea;
            border-left:6px solid red;
            padding:15px;
            border-radius:10px;
        }

        footer{
            visibility:hidden;
        }

        </style>
        """,
        unsafe_allow_html=True
    )