import numpy as np
import streamlit as st
import itertools

st.title("Click on an image to navigate to the App")

from itertools import cycle

WS_Images = [WS_Works.jpg, WS_Sonnet.jpg, WS_Insults.jpg, WS_Stats.jpg] # your images here
caption = ["Works", "Sonnets", "Insults", "Stats"] # your caption here
cols = cycle(st.columns(3)) # st.columns here 
for idx, ws_image in enumerate(WS_Images):
    next(cols).image(ws_image, width=150, caption=caption[idx])
