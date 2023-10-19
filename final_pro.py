import streamlit as st
import streamlit as st
import pandas as pd
import numpy as num
from PIL import Image
import base64
import streamlit as st
import sklearn


st.title("Hotels in Rome")

st.write("""
### TripAdvisor Rating Impact on Hotel Popularity
""")
images = ['image.jpg']#, 'unnamed.png']
st.image(images, use_column_width=True, caption=["Rome"] * len(images))

st.write("""
### There are almost 4500 hotels in Rome
""")

images_2 = ['starss.jpg', 'stars.jpg']#, 'unnamed.png']
caption = ['which of 20% have 5.0 in BUBBLE RATTING', '50% have 4.5 or more in BUBBLE RATTING']
st.image(images_2, use_column_width=True, caption=caption * len(images))

st.write("""
### Here is the TOP10 hotels in Rome
""")

imagess = ['top_10.jpg']#, 'unnamed.png']
st.image(imagess, use_column_width=True, caption=["top_10"] * len(images))


images_3 = ['price.jpg']
caption_3 = ['Average price in TOP10 hotels and in general in the city is 95 euro']
st.image(images_3, use_column_width=True, caption=caption_3 * len(images))

st.write("""
### In this type of hotel are almost NO DISCOUNTS
(only about 3-6%)
""")


st.write("""
________________________________________________________________________________________
""")

st.write("""
### The most important features(VarianceThreshold):
:white_circle: Flatscreen TV(0.24)

:white_circle: Free breakfast(0.24)

:white_circle: Public wifi(0.23)

:white_circle: Safe(0.23)

:white_circle: Category(0.23)

:white_circle: Non-smoking hotel(0.22)

:white_circle: Housekeeping(0.22)

:white_circle: Refrigerator(0.22)

:white_circle: Class_3_4_5(0.22)

:white_circle: Complimentary toiletries(0.22)
""")

st.write("""
________________________________________________________________________________________
""")



st.write("""
### The 'bubble-ranking' which have TripAdvisor contains of 272 features.
To predict 'buble-ranking' or exactly price of the room in a hotel in Rome
have to included around 40 to get the great output.
If you would like to try my model go there ->https://github.com/Valeriiass/final_project/blob/main/ORIGINAL_final.ipynb
""")



