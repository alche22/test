import streamlit as st
import pandas as pd
import numpy as np

data = chart_data = pd.DataFrame(
    {
        'kia' : [6, 9, 5, 6, 1],
        'sam' : [8, 3, 7, 8, 2],
        'lg' : [4, 4, 3, 1, 3],
        'doo' : [2, 2, 9, 5, 4],
        'kt' : [3, 1, 4, 2, 5],
        'ssg' : [9, 6, 1, 3, 6],
        'lot' : [7, 8, 8, 7, 7],
        'han' : [10, 10, 10, 9, 8],
        'nc' : [1, 7, 6, 4, 9],
        'kh' : [5, 5, 2, 10, 10]
        
    }
)
st.dataframe(data, use_container_width=True)


