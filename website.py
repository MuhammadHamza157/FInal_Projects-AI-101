# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt


# st.title("Simple Clothing website")

# upload_file = st.file_uploader("Choose a excel file", type="xlsx")
# if upload_file is not None:
#     df = pd.read_excel(upload_file)
#     st.subheader("Pakistan weather")
#     st.write(df.head())

#     st.subheader("summary")
#     st.write(df.describe())

#     st.subheader("filter data")
#     columns = df.columns.tolist()
#     select_column = st.selectbox("Select column to filter",columns)

#     unique_values = df[select_column].unique()
#     selected_value = st.selectbox ("select value",unique_values)

#     filterd_df = df[df[select_column] == selected_value ]
#     st.write(filterd_df)

#     st.subheader("PLOT DATA")
#     x_column = st.selectbox("Select x-axis column", columns)
#     y_column = st.selectbox("Select y-axis column", columns)

#     if st.button("Generate Plot"):
#         st.line_chart(filterd_df.set_index(x_column)[y_column])
#     else:
#         st.write("Waiting to file upload...")

# 
# ******************************************************************




import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt

st.title("Weather updates")

upload_file = st.file_uploader("Choose a excel file", type="xlsx")
if upload_file is not None:
    df = pd.read_excel(upload_file)
    st.subheader("Pakistan weather")
    st.write(df.head())

    st.subheader("summary")
    st.write(df.describe())

    st.subheader("filter data")
    columns = df.columns.tolist()
    select_column = st.selectbox("Select column to filter", columns)

    unique_values = df[select_column].unique()
    selected_value = st.selectbox("select value", unique_values)

    filtered_df = df[df[select_column] == selected_value]
    st.write(filtered_df)

    st.subheader("PLOT DATA")
    x_column = st.selectbox("Select x-axis column", columns)
    y_column = st.selectbox("Select y-axis column", columns)  # Changed to columns instead of unique_values

    if st.button("Generate Plot"):
        if x_column in filtered_df.columns and y_column in filtered_df.columns:
            st.line_chart(filtered_df.set_index(x_column)[y_column])  # Ensure valid columns for x and y
        else:
            st.write("Invalid column selection for plot.")
else:
    st.write("Waiting for file upload...")
