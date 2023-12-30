import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit bread maker!

Use this app to cutomize your receipe for home made bread.
"""

st.subheader("my subs")
num_baguette = st.slider("Number of points in spiral", 1, 1, 10)
num_turns = st.slider("Number of turns in spiral",0, 300, 31)

indices = np.linspace(0, 1, num_baguette)
theta = 2 * np.pi * num_turns * indices
radius = indices

x = radius * np.cos(theta)
y = radius * np.sin(theta)

df = pd.DataFrame({
    "x": x,
    "y": y,
    "idx": indices,
    "rand": np.random.randn(num_baguette),
})

st.altair_chart(alt.Chart(df, height=700, width=700)
    .mark_point(filled=True)
    .encode(
        x=alt.X("x", axis=None),
        y=alt.Y("y", axis=None),
        color=alt.Color("idx", legend=None, scale=alt.Scale()),
        size=alt.Size("rand", legend=None, scale=alt.Scale(range=[1, 150])),
    ))

st.write("Job Done!")