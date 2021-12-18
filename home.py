import pickle
import streamlit as st
import pandas as pd

# Import the Dataset 
skincare = pd.read_csv("skincare.csv", encoding='utf-8', index_col=None)
# loading the trained model
pickle_in = open('Capstone_Project.pkl', 'rb') 
classifier = pickle.load(pickle_in)
# this is the main function in which we define our webpage
def main():
# Choose a product category
    category = st.selectbox(label='Select a product category', options= skincare['tipe_produk'].unique() )

    st.write(type(category))
    category_subset = skincare[skincare['tipe_produk'] == category]
    # Choose a skintype
    skin_type = st.selectbox(label='Select your skin type', options= ['Combination', 'Dry', 'Normal', 'Oily', 'Sensitive'] )
    st.write(type(skin_type))
    category_st_subset = category_subset[category_subset[skin_type] == 1]
    category_st_subset
    # Choose notable_effects
    options_a = category_st_subset['notable_effects'].unique().tolist()
    selected_options = st.multiselect('Which notable_effects do you want?',options_a)

    filtered_df = category_st_subset[category_st_subset["notable_effects"].isin(selected_options)]

    st.dataframe(filtered_df)

    options_b = filtered_df['product_name'].unique().tolist()
    product = st.selectbox(label='Select the product', options = sorted(options_b))

    product

    product_name = filtered_df[filtered_df["product_name"] == product]
    st.dataframe(product_name)
    # Reset index
    product_name = product_name.reset_index(drop=True)

    classifier.skincare_recommendations(product_name['product_name'])