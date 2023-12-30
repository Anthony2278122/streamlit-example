
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
    index=0,
)

floor_style = st.radio(
    "What kind of bread",
    ["white baguette", "whole wheat baguette"],
    index=0,
)

num_baguette = st.slider("Number of points in spiral", 1, 10, 3)

if starter_type == "dry yeast":
    floor_per_baguette = 173.33
    starter_per_baguette = 7
    wheight = 0
    salt_per_baguette = 3
else:
    floor_per_baguette = 200
    starter_per_baguette = 50
    wheight = 0.5
    salt_per_baguette = 4

if floor_style == "white baguette":
    hydration = 0.72
    total_floor = np.round(num_baguette * floor_per_baguette - wheight * num_baguette * starter_per_baguette)
    floor_ratio = 1
else:
    hydration = 0.72
    total_floor = np.round(num_baguette * floor_per_baguette - wheight * num_baguette * starter_per_baguette)
    floor_ratio = 0.8


receipe = {
    starter_type + " [g]" : int(np.round(num_baguette * starter_per_baguette)),
    "total white floor [g]" : int(np.round(total_floor * floor_ratio)),
    "total salt [g]": int(np.round(num_baguette * salt_per_baguette)),
    "total water [g]" : int(np.round(num_baguette * floor_per_baguette * hydration - wheight * num_baguette * starter_per_baguette))
    }
if floor_style == "whole wheat baguette":
    receipe["whole wheat floor [g]"] = int(np.round(total_floor * (1 - floor_ratio)))

st.subheader("needed ingredients:")
#st.write(receipe)
df = pd.DataFrame.from_records([receipe], index=None).transpose()
df = df.rename(index={0: "quantities"})

st.dataframe(df)
st.write("Job Done!")