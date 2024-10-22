import streamlit as st
import pandas as pd
import PyPDF2

# Judul aplikasi
st.title('Aplikasi Upload dan Baca File')

# Membuat widget untuk upload file
uploaded_file = st.file_uploader("Pilih file", type=["csv", "xlsx", "txt", "pdf"])

# Menampilkan isi file yang diupload
if uploaded_file is not None:
    file_details = {"Filename": uploaded_file.name, "FileType": uploaded_file.type, "FileSize": uploaded_file.size}
    st.write(file_details)

    # Membaca dan menampilkan file teks
    if uploaded_file.type == "text/plain":
        content = uploaded_file.read().decode("utf-8")
        st.text(content)

    # Membaca dan menampilkan file CSV
    elif uploaded_file.type == "text/csv":
        df = pd.read_csv(uploaded_file)
        st.write(df)

    # Membaca dan menampilkan file Excel
    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
        df = pd.read_excel(uploaded_file)
        st.write(df)

    # Membaca dan menampilkan file PDF
    elif uploaded_file.type == "application/pdf":
        pdf_reader = PyPDF2.PdfFileReader(uploaded_file)
        num_pages = pdf_reader.numPages
        for page_num in range(num_pages):
            page = pdf_reader.getPage(page_num)
            st.write(page.extractText())

    # Pesan jika jenis file tidak dikenali
    else:
        st.write("File tidak dikenali atau belum didukung.")
else:
    st.write("Silakan unggah file untuk melihat kontennya.")