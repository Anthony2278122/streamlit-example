
import numpy as np
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit bread maker!

Use this app to cutomize your receipe for home made bread.
Ideally, use a bread floor with at least 12.5% protein (gluten).
Starter is made of half unbleached bread floor and half water. 
Hydration is set up at 72%.
"""

st.subheader("Make your own baguette: ")

starter_type = st.radio(
    "What kind of starter are you using:",
    ["dry yeast", "sourdough starter"],
    index=None,
)

floor_style = st.radio(
    "What kind of bread",
    ["white baguette", "whole wheat baguette"],
    index=None,
)

num_baguette = st.slider("Number of points in spiral", 1, 10, 3)

if starter_type == "dry yeast":
    floor_per_baguette = 173
    starter_per_baguette = 7
    wheight = 0
else:
    floor_per_baguette = 200
    starter_per_baguette = 50
    wheight = 0.5

if floor_style == "white baguette":
    hydration = 0.72
else:
    hydration = 0.72

receipe = {
    starter_type: np.round(num_baguette * starter_per_baguette),
    "total_floor [g]" : np.round(num_baguette * floor_per_baguette - wheight * num_baguette * starter_per_baguette),
    "total_water [g]" : np.round(num_baguette * floor_per_baguette * hydration - wheight * num_baguette * starter_per_baguette)
    }

st.subheader("needed ingredients:")

st.dataframe(pd.DataFrame.from_dict(receipe))

st.write("Job Done!")