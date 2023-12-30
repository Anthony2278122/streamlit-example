import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit bread maker!

Use this app to cutomize your receipe for home made bread.
Ideally, use a bread floor with at least 12.5% protein (gluten).
Hydration is set up at 72%.
"""

st.subheader("How many baguette?")

genre = st.radio(
    "What kind of bread",
    ["white baguette", "whole wheat baguette"],
    index=None,
)

num_baguette = st.slider("Number of points in spiral", 1, 1, 10)

floor_per_baguette = 200
starter_per_baguette = 60

total_floor = num_baguette * floor_per_baguette
total_starter = num_baguette * starter_per_baguette
total_water = total_floor * 0.72


st.subheader("needed ingredients:")

st.write("Floor: ")

st.write("Job Done!")