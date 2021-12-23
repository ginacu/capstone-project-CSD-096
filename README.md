# capstone-project-CSD-096
Capstone Project : Aplikasi Rekomendasi Produk Skincare Sesuai Permasalahan Kulit Wajah
Proyek ini disusun oleh : 
1. M342V6359 – Dwi Ayu Nouvalina
2. M182V4139 – Gina Cahya Utami


Aplikasi rekomendasi skincare merupakan sebuah implementasi dari projek Machine Learning yang dapat merekomendasikan pemilihan skincare sesuai dengan jenis dan juga permasalahan kulit Anda. Anda dapat memasukkan jenis kulit, keluhan, dan hal yang dibutuhkan kulit untuk mengetahui rekomendasi skincare yang Anda butuhkan. 

Sistem rekomendasi ini merupakan content-based filtering yang dibuat di Google Colab menggunakan bahasa pemrograman Python dan framework Streamlit. Dataset yang digunakan berasal dari hasil Web Scrapping dari beberapa e-commerce yang menjual produk skincare. Lalu, pengolahan data nya dimulai dari Data Exploration sampai dengan Get Recommendation di Google Colab lalu menggunakan Streamlit untuk proses Deployment nya. Pada tahap Deployment kami menggunakan Streamlit sharing, sehingga demo aplikasi bisa dilihat padal link berikut : 
https://share.streamlit.io/ginacu/capstone-project-csd-096/main/home.py


Cara Penggunaan Aplikasi :

1. Pilih kategori produk skincare yang diinginkan : 
    a. Facewash
    b. Toner
    c. Serum
    d. Moisturizer
    e. Sunscreen
   
2. Pilih tipe kulit :
    a. Normal
    b. Dry
    c. Oily
    d. Combination
    e. Sensitive
    
3. Pilih jenis permasalahan kulit yang dialami 
    Misalnya seperti kulit kusam, jerawat, garis halus dan kerutan, dll
    
4. Pilih efek yang diinginkan dalam produk 
    Misalnya efek brightening, soothing, moisturizing, dll 
    
5. Setelah memilih kategori produk, tipe kulit, dan permasalahan serta efek yang ingin dihasilkan maka sistem akan memberikan beberapa rekomendasi sesuai apa yang diinginkan pengguna. Pengguna bisa memilih salah satu produk yang direkomendasikan.

6. Untuk mendapatkan rekomendasi produk serupa, pengguna bisa mengklik tombol 'Temukan rekomendasi produk lainnya'. Maka, sistem akan memunculkan produk-produk yang serupa dengan yang disukai pengguna. 
