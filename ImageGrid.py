import streamlit as st

st.title('Bard v Bot')

# to get different images in the rows and columns, have a systematic way to label your images. For mine, I have used row_{i}_col_{j}

cols = st.columns(3)

cols[0].image('images/row_0_col_0.png', caption='Search Plays', use_column_width=True)

cols[1].image('images/row_0_col_1.png', caption='Statistical Analysis', use_column_width=True)
cols[2].image('images/row_0_col_2.png', caption='Sentiment Analysis', use_column_width=True)

cols[0].image('images/row_1_col_0.png', caption='AI Play Writer', use_column_width=True)
cols[1].image('images/row_1_col_1.png', caption='Shakespeare', use_column_width=True)
cols[2].image('images/row_1_col_2.png', caption='Sonnet Clouds', use_column_width=True)

cols[0].image('images/row_2_col_0.png', caption='Infinite MonkRandom', use_column_width=True)
cols[1].image('images/row_2_col_1.png', caption='Random Insults & Quotes', use_column_width=True)
cols[2].image('images/row_2_col_2.png', caption='Text Summary', use_column_width=True)
cols[2].markdown("https://tulasi-agina-searchshakespeareplays-main-fpxl6w.streamlit.app/")
