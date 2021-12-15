import streamlit as st
from PIL import Image

st.set_page_config(page_title="Home - Aplikasi Rekomendasi Skincare", page_icon=":blossom:")

# sidebar
sdbar = st.sidebar.radio('Menu', ['Home','About Us'])

st.sidebar.image('image2.jpg')

# showing pages berdasarkan pilihan
if sdbar == 'Home' or sdbar == '':

    # menampilkan halaman utama
    st.header("Capstone Project Team 096 - Aplikasi Rekomendasi Skincare :sparkles:")
    
    # header image
    image = st.image('image.jpg')

    st.markdown(
    "Aplikasi Rekomendasi Skincare merupakan sebuah implementasi dari projek Machine Learning yang dapat merekomendasikan pemilihan skincare sesuai dengan jenis dan juga permasalahan kulit Anda."
    + " Anda dapat memasukkan jenis kulit, keluhan, dan hal yang dibutuhkan kulit untuk mengetahui rekomendasi skincare yang Anda butuhkan "
    )

    # option
    # option 1 skintypes
    skintypes = st.selectbox(
     'Masukkan jenis kulit Anda : ',
     ('Normal', 'Oily', 'Dry', 'Combination', 'Sensitive'))


    # option 2 masalah kulit
    skin_problems = st.multiselect(
        'Masukkan masalah kulit yang Anda alami (boleh lebih dari 1) : ',
        ['Jerawat', 'Pori-pori besar', 'Flek hitam', 'Kerutan', 'Komedo', 'Warna kulit tidak merata', 'Milia'])

    # option 3 hasil produk yang dibutuhkan
    nottable_effects = st.multiselect(
        'Masukkan hasil dari skincare yang Anda inginkan (boleh lebih dari 1) : ',
        ['Brightening', 'Hydrating', 'Moisturizing', 'Soothing', 'Anti-aging', 'Firming', 'Exfoliating'])


    # pembatas
    st.write('---')

    # 1. rekomendasi facewash
    st.subheader('Rekomendasi Facewash untuk Anda!')

    # button submit 
    submit_fw = st.button('Klik disini untuk mengetahuinya', key="1")
    st.write(submit_fw)


    # pembatas
    st.write('---')

    # 2. rekomendasi toner
    st.subheader('Rekomendasi Toner untuk Anda!')

    # button submit 
    submit_toner = st.button('Klik disini untuk mengetahuinya', key="2")
    st.write(submit_toner)


    # pembatas
    st.write('---')

    # 3. rekomendasi serum
    st.subheader('Rekomendasi serum untuk Anda!')

    # button submit 
    submit_serum = st.button('Klik disini untuk mengetahuinya', key="3")
    st.write(submit_serum)


    # pembatas
    st.write('---')

    # 4. rekomendasi moisturizer
    st.subheader('Rekomendasi Moisturizer untuk Anda!')

    # button submit 
    submit_moist = st.button('Klik disini untuk mengetahuinya', key="4")
    st.write(submit_moist)


    # pembatas
    st.write('---')

    # 5. rekomendasi ss
    st.subheader('Rekomendasi Sunscreen untuk Anda!')

    # button submit 
    submit_ss = st.button('Klik disini untuk mengetahuinya', key="5")
    st.write(submit_ss)

elif sdbar == 'About Us':
    # menampilkan halaman about us
    st.title("About Us")

    st.markdown(
    "1. Dwi Ayu Nouvalina - M342V6359" 
    )
    st.markdown(
    "2. Gina Cahya Utami - M182V4139" 
    )
