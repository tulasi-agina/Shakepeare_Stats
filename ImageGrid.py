import numpy as np
import streamlit as st

st.title("Click on an image to navigate to the App")

WS_Images = [WS_Works.jpg, WS_Sonnet.jpg, WS_Play.jpg, WS_Sonnet.jpg]
n_rows = 2
n_cols = 2

for image_index, ws_image in enumerate(WS_Images):
  cols[image_index].image(ws_image)
