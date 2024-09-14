
import numpy as np
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit bread maker!

Use this app to cutomize your receipe for home made bread.
Ideally, use a bread floor with 12.7% protein (gluten).
Starter is made of half unbleached bread floor and half water.
Hydration is set up at 72% for sourdough and 86% for dry yeast.
"""

st.subheader("Make your own baguette: ")

starter_type = st.radio(
    "What kind of starter are you using:",
    ["dry yeast", "sourdough starter"],
    index=0,
)

floor_style = st.radio(
    "What kind of bread",
    ["white floor", "whole wheat floor"],
    index=0,
)

num_baguette = st.slider("Number of points in spiral", 1, 10, 3)

if starter_type == "dry yeast":
    floor_per_baguette = 173.33
    starter_per_baguette = 4.67
    wheight = 0
    salt_per_baguette = 3
    # hydration = 0.8654
    hydration = 0.75
else:
    floor_per_baguette = 200
    starter_per_baguette = 50
    wheight = 0.5
    salt_per_baguette = 4
    hydration = 0.72

if floor_style == "white floor":
    total_floor = np.round(num_baguette * floor_per_baguette - wheight * num_baguette * starter_per_baguette)
    floor_ratio = 1
else:
    total_floor = np.round(num_baguette * floor_per_baguette - wheight * num_baguette * starter_per_baguette)
    floor_ratio = 0.8


receipe = {
    starter_type + " [g]" : int(np.round(num_baguette * starter_per_baguette)),
    "salt [g]": int(np.round(num_baguette * salt_per_baguette)),
    "water [g]" : int(np.round(total_floor * hydration)),
    "white floor [g]" : int(np.round(total_floor * floor_ratio)),
    }
if floor_style == "whole wheat floor":
    receipe["whole wheat floor [g]"] = int(np.round(total_floor * (1 - floor_ratio)))

st.subheader("needed ingredients:")
#st.write(receipe)
df = pd.DataFrame.from_records([receipe], index=None).transpose()
df = df.rename(columns={0: "quantities"})

st.dataframe(df)

expander = st.expander("Sourdough preparation")
expander.write('''
    Take your sourdough out of the fridge. Let it rest on your counter to warm-up a little.
    Then feed it with half water and floor. 50g each if you need 100g starter for instance.
    Let it raise for a couple of hours.
    ''')
expander.image("https://www.theperfectloaf.com/wp-content/uploads/2020/08/theperfectloaf-whats-the-difference-between-starter-levain-1-2-1080x720.jpg")
expander.write('''
    When the sourdough has doubled (at least), it's ready to use!
    Take out the quantity you need and put the remaining sourdough back in your fridge.
    ''')


expander = st.expander("Step-by-step tutorial")
expander.write('''
    If you're using dry yeast. Mix the dry yeast with a part of the water. Water must be between 20°C and 25°C. Let it sit on the counter for 20 minutes.
    ''')
expander.write('''
    In a large bowl, combine the starter ingredients (dry yeast and water or sourdough starter), the flour, the salt and the water. Again, water must be between 20°C and 25°C. 
    ''')
expander.image("https://www.kingarthurbaking.com/sites/default/files/2022-09/step-3.gif")
expander.write('''
    To make the dough: Mix and knead everything together — by hand, mixer or bread machine set on the dough cycle — to make a soft, somewhat smooth dough;
    it should be cohesive, but the surface may still be a bit rough.
    If you're using a stand mixer, knead for about 4 minutes on medium-low speed (speed 2 on a KitchenAid);
    the finished dough should stick a bit at the bottom of the bowl.
    ''')
expander.image("https://www.kingarthurbaking.com/sites/default/files/2022-08/step-6_1.gif")
expander.write('''
    Optionally, stretch and fold 3 times the dough separeted by 15 to 20 minutes. See: 
    ''')
expander.video("https://www.youtube.com/watch?v=KcS58OzfTcM")
expander.write('''
    After 2 hour (dry yeast) or 3 to 4 hour (sourdough), the dough is ready to form and cook!.
    ''')
expander.image("https://www.kingarthurbaking.com/sites/default/files/2022-09/step-9.gif")
expander.write('''
    Place the logs seam-side down onto a lightly greased or parchment-lined sheet pan or pans; or into the folds of a heavily floured cotton dish towel (or couche).
    Cover them with lightly greased plastic wrap, and allow the loaves to rise until they're slightly puffy.
    The loaves should certainly look lighter and less dense than when you first shaped them, but won't be anywhere near doubled in bulk.
    This should take about 45 minutes to an hour at room temperature (about 68°F).
    ''')
expander.image("https://www.kingarthurbaking.com/sites/default/files/2022-08/step-13.gif")
expander.write('''
    Load the baguettes into the oven pre-heated at 265°C (510°F). If you’re baking on a stone, use a baker’s peel to transfer the baguettes, parchment and all, onto the hot stone.
    Carefully pour a glass of water into the cast iron pan, and quickly shut the oven door.
    The billowing steam created by the boiling water will help the baguettes rise, and give them a shiny thin crust.
    Cook them for about 20min, depending on the crust you like.
    ''')
expender.image("https://www.google.com/url?sa=i&url=https%3A%2F%2Ftasteofartisan.com%2Ffrench-baguette-recipe%2F&psig=AOvVaw3iajSNnL028izyCtfY43az&ust=1726413347277000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCOjnz4bdwogDFQAAAAAdAAAAABAE")
expander.write('''
    Job Done! Congratulations!
    ''')

# Webapp link :
# https://anthony2278122-streamlit-example-streamlit-app-kwicbv.streamlit.app/
