import streamlit as st

st.title('Table of images')

# to get different images in the rows and columns, have a systematic way to label your images. For mine, I have used row_{i}_col_{j}

cols = st.columns(3)

cols[0].image('images/row_0_col_0.png', use_column_width=True)
cols[1].image('images/row_0_col_1.png', use_column_width=True)
cols[2].image('images/row_0_col_2.png', use_column_width=True)

cols[0].image('images/row_1_col_0.png', use_column_width=True)
cols[1].image('images/row_1_col_1.png', use_column_width=True)
cols[2].image('images/row_1_col_2.png', use_column_width=True)

cols[0].image('images/row_2_col_0.png', use_column_width=True)
cols[1].image('images/row_2_col_1.png', use_column_width=True)
cols[2].image('images/row_2_col_2.png', use_column_width=True)
