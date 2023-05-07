import streamlit as st

st.title('Table of images')

# to get different images in the rows and columns, have a systematic 
# way to label your images. For mine, I have used row_{i}_col_0/1/2

for i in range(1,3): # number of rows in your table! = 2
    cols = st.beta_columns(3) # number of columns in each row! = 3
    # first column of the ith row
    cols[0].image('images/row_%i_col_0.png' %i, use_column_width=True)
    cols[1].image('images/row_%i_col_1.png' %i, use_column_width=True)
    cols[2].image('images/row_%i_col_2.png' %i, use_column_width=True)
