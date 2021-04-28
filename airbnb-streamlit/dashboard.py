import streamlit as st
import pandas as pd
import altair as alt

@st.cache
def get_airbnb_data():
    df = pd.read_csv('http://data.insideairbnb.com/germany/be/berlin/2021-02-20/data/listings.csv.gz')
    df['price'] = df['price'].replace('[\$,)]','', regex=True).replace('[(]','-', regex=True).astype(float)
    return df # .set_index("Region")

try:
    df = get_airbnb_data()
except urllib.error.URLError as e:
    st.error(
        '''
        **This demo requires internet access.**

        Connection error: %s
        ''' % e.reason
    )
    # return

price_to_filter = st.slider('price', int(df.price.min()), int(df.price.max()), int(df.price.median()))  # min: 0h, max: 23h, default: 17h

# st.write(df.price)

st.write(price_to_filter)

# # st.table(df)
#

st.map(df[['latitude', 'longitude']])

#

st.bar_chart(df.neighbourhood_cleansed.value_counts())


# st.table(df_tweets[['created_at', 'harmonized_text']]) # , width='1200', height='100%')



# countries = st.multiselect(
#     "Choose countries", list(df.index), ["China", "United States of America"]
# )
# if not countries:
#     st.error("Please select at least one country.")
#     # return

# data = df.loc[countries]
# data /= 1000000.0
# st.write("### Gross Agricultural Production ($B)", data.sort_index())

# data = data.T.reset_index()
# data = pd.melt(data, id_vars=["index"]).rename(
#     columns={"index": "year", "value": "Gross Agricultural Product ($B)"}
# )
# chart = (
#     alt.Chart(data)
#     .mark_area(opacity=0.3)
#     .encode(
#         x="year:T",
#         y=alt.Y("Gross Agricultural Product ($B):Q", stack=None),
#         color="Region:N",
#     )
# )
# st.altair_chart(chart, use_container_width=True)
