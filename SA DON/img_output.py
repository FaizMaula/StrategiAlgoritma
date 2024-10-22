import streamlit as st

def output(hasil):
    col1, col2, col3, col4, col5 = st.columns(5)
    # Menampilkan gambar di setiap kolom
    for j in range(len(hasil)):
        if hasil[j]:  # Hanya menampilkan gambar jika URL tidak kosong
            if j == 0:
                with col1:
                    st.image(hasil[j], width=90)
            elif j == 1:
                with col2:
                    st.image(hasil[j], width=90)
            elif j == 2:
                with col3:
                    st.image(hasil[j], width=90)
            elif j == 3:
                with col4:
                    st.image(hasil[j], width=90)
            elif j == 4:
                with col5:
                    st.image(hasil[j], width=90)