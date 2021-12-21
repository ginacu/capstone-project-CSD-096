from os import write
from numpy.core.fromnumeric import prod
import tensorflow as tf
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

# Import the Dataset 
skincare = pd.read_csv("skincare.csv", encoding='utf-8', index_col=None)

# Header
st.set_page_config(page_title="Home - Aplikasi Rekomendasi Skincare", page_icon=":blossom:")

# Sidebar
sdbar = st.sidebar.radio('Menu', ['Home','About Us'])
# Gambar header
st.sidebar.image('image2.jpg')

# showing pages berdasarkan pilihan
if sdbar == 'Home' or sdbar == '':
    # Choose a product product type category
    # pt = product type
    category = st.selectbox(label='Pilih kategori produk kamu : ', options= skincare['tipe_produk'].unique() )
    category_pt = skincare[skincare['tipe_produk'] == category]

    # Choose a skintype
    # st = skin type
    skin_type = st.selectbox(label='Pilih tipe kulit kamu : ', options= ['Combination', 'Dry', 'Normal', 'Oily', 'Sensitive'] )
    category_st_pt = category_pt[category_pt[skin_type] == 1]

    # Choose notable_effects
    # dari produk yg sudah di filter berdasarkan product type dan skin type(category_st_pt), kita akan ambil nilai yang unik di kolom notable_effects
    opsi_ne = category_st_pt['notable_effects'].unique().tolist()
    # notable_effects-notable_effects yang unik maka dimasukkan ke dalam variabel opsi_ne dan digunakan untuk value dalam multiselect yg dibungkus variabel selected_options di bawah ini
    selected_options = st.multiselect('Pilih efek yang kamu inginkan di dalam produk kamu : ',opsi_ne)
    # hasil dari selected_options kita masukan ke dalam var category_ne_st_pt
    category_ne_st_pt = category_st_pt[category_st_pt["notable_effects"].isin(selected_options)]

    # Choose product
    # produk2 yang sudah di filter dan ada di var filtered_df kemudian kita saring dan ambil yang unik2 saja berdasarkan product_name dan di masukkan ke var opsi_pn
    opsi_pn = category_ne_st_pt['product_name'].unique().tolist()
    # buat sebuah selectbox yang berisi pilihan produk yg sudah di filter di atas
    product = st.selectbox(label='Select the product', options = sorted(opsi_pn))
    # variabel product di atas akan menampung sebuah produk yang akan memunculkan rekomendasi produk lain

    ## MODELLING with Content Based Filtering
    # Inisialisasi TfidfVectorizer
    tf = TfidfVectorizer()
    
    # Melakukan perhitungan idf pada data 'notable_effects'
    tf.fit(skincare['notable_effects']) 
    
    # Mapping array dari fitur index integer ke fitur nama
    tf.get_feature_names()

    # Melakukan fit lalu ditransformasikan ke bentuk matrix
    tfidf_matrix = tf.fit_transform(skincare['notable_effects']) 
    
    # Melihat ukuran matrix tfidf
    shape = tfidf_matrix.shape

    # Mengubah vektor tf-idf dalam bentuk matriks dengan fungsi todense()
    tfidf_matrix.todense()

    # Membuat dataframe untuk melihat tf-idf matrix
    # Kolom diisi dengan efek-efek yang diinginkan
    # Baris diisi dengan nama produk
    pd.DataFrame(
        tfidf_matrix.todense(), 
        columns=tf.get_feature_names(),
        index=skincare.product_name
    ).sample(shape[1], axis=1).sample(10, axis=0)

    # Menghitung cosine similarity pada matrix tf-idf
    cosine_sim = cosine_similarity(tfidf_matrix) 

    # Membuat dataframe dari variabel cosine_sim dengan baris dan kolom berupa nama produk
    cosine_sim_df = pd.DataFrame(cosine_sim, index=skincare['product_name'], columns=skincare['product_name'])
    
    # Melihat similarity matrix pada setiap nama produk
    cosine_sim_df.sample(7, axis=1).sample(10, axis=0)

    # Membuat fungsi untuk mendapatkan rekomendasi
    def skincare_recommendations(nama_produk, similarity_data=cosine_sim_df, items=skincare[['product_name', 'picture_src','price', 'description', 'notable_effects']], k=5):
        
        # Mengambil data dengan menggunakan argpartition untuk melakukan partisi secara tidak langsung sepanjang sumbu yang diberikan    
        # Dataframe diubah menjadi numpy
        # Range(start, stop, step)
        index = similarity_data.loc[:,nama_produk].to_numpy().argpartition(range(-1, -k, -1))
        
        # Mengambil data dengan similarity terbesar dari index yang ada
        closest = similarity_data.columns[index[-1:-(k+2):-1]]
        
        # Drop nama_produk agar nama produk yang dicari tidak muncul dalam daftar rekomendasi
        closest = closest.drop(nama_produk, errors='ignore')
        df = pd.DataFrame(closest).merge(items).head(k)
        return df

    # Membuat button untuk menampilkan rekomendasi
    model_run = st.button('Find similar products!')
    # Mendapatkan rekomendasi
    if model_run:
        st.write('Berikut rekomendasi pilihan skincare yang kamu butuhkan sesuai efek yang kamu inginkan')
        st.write(skincare_recommendations(product))

elif sdbar == 'About Us':
    # menampilkan halaman about us
    st.title("About Us")

    st.markdown(
    "1. Dwi Ayu Nouvalina - M342V6359" 
    )
    st.markdown(
    "2. Gina Cahya Utami - M182V4139" 
    )