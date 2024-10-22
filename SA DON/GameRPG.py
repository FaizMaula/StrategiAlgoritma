import streamlit as st
import time
import Greedy
import img_output
import bruteforce

st.title("Game RPG")
st.text("Selamat datang di aplikasi untuk menentukan kartu pada game RPG")

Boss = st.number_input('Masukan Power Boss:', 0, 10000)
Koin = st.number_input('Masukan Koin awal:', 0, 10000)

class Fighter:
    def __init__(self, harga, power, img_url, nama, dens):
        self.harga = harga
        self.power = power
        self.img_url = img_url
        self.nama = nama
        self.dens = dens 

# Menampilkan gambar dan input di sebelahnya menggunakan kolom
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    image1 = st.image('https://raw.githubusercontent.com/sanfla/knapsack-game-rpg/main/Character/Arthur.png', width=90, use_column_width='always', caption="Claart")
    power1 = st.number_input("Power Fighter 1", 0, 10000, key='input1')
    Koin1 = st.number_input("Harga Fighter 1", 0, 10000, key='input2')

with col2:
    image2 = st.image('https://raw.githubusercontent.com/sanfla/knapsack-game-rpg/main/Character/Assassin%20(1).png', width=90, use_column_width='always', caption="Bumba")
    power2 = st.number_input("Power Fighter 2", 0, 10000, key='input3')
    Koin2 = st.number_input("Harga Fighter 2", 0, 10000, key='input4')

with col3:
    image3 = st.image('https://raw.githubusercontent.com/sanfla/knapsack-game-rpg/main/Character/Knight.png', width=90, use_column_width='always', caption="Peter")
    power3 = st.number_input("Power Fighter 3", 0, 10000, key='input5')
    Koin3 = st.number_input("Harga Fighter 3", 0, 10000, key='input6')

with col4:
    image4 = st.image('https://raw.githubusercontent.com/sanfla/knapsack-game-rpg/main/Character/Wizard.png', width=90, use_column_width='always', caption="James")
    power4 = st.number_input("Power Fighter 4", 0, 10000, key='input7')
    Koin4 = st.number_input("Harga Fighter 4", 0, 10000, key='input8')

with col5:
    image5 = st.image('https://raw.githubusercontent.com/sanfla/knapsack-game-rpg/main/Character/Wolf.png', width=90, use_column_width='always', caption="Wolf")
    power5 = st.number_input("Power Fighter 5", 0, 10000, key='input9')
    Koin5 = st.number_input("Harga Fighter 5", 0, 10000, key='input10')

# Array
img_urls = [
    'https://raw.githubusercontent.com/sanfla/knapsack-game-rpg/main/Character/Arthur.png',
    'https://raw.githubusercontent.com/sanfla/knapsack-game-rpg/main/Character/Assassin%20(1).png',
    'https://raw.githubusercontent.com/sanfla/knapsack-game-rpg/main/Character/Knight.png',
    'https://raw.githubusercontent.com/sanfla/knapsack-game-rpg/main/Character/Wizard.png',
    'https://raw.githubusercontent.com/sanfla/knapsack-game-rpg/main/Character/Wolf.png'
]
arrN = ["Claart", "Bumba", "Peter", "James", "Wolf"]
arrP = [power1, power2, power3, power4, power5]
arrK = [Koin1, Koin2, Koin3, Koin4, Koin5]

# Membuat objek Fighter dan memasukkannya ke dalam list
fighters = []
# Melakukan iterasi pada indeks dari arrK
for i in range(len(arrK)):
    # Mengambil harga dari arrK
    harga = arrK[i]  
    # Mengambil power dari arrP
    power = arrP[i]  
    # Mengambil URL gambar dari img_urls
    img_url = img_urls[i]  
    # Mengambil nama dari arrN
    nama = arrN[i]  
    #density
    if arrK[i] != 0:
        dens = arrP[i]/arrK[i]
    else:
        dens = 0
    # Membuat objek Fighter dan menambahkannya ke dalam list fighters
    fighter = Fighter(harga, power, img_url, nama, dens)
    fighters.append(fighter)



hasil = []
hfighter = []
tPower = []

#Metode = st.radio('Metode yang ingin dipakai', ['Greedy by Power', 'Greedy by Harga', 'Brute Force'])
if st.button('Hitung'):
    start = time.time()

    # Algoritma Knapsack menggunakan Brute Force
    st.write("Menggunakan Algoritma Brute Force")
    st.write("Hasil Bruteforce:")
    SisaKoin = bruteforce.bruteForce(fighters, hasil, hfighter, Koin, tPower)
    # Menampilkan output gambar
    img_output.output(hasil)
    stop = time.time()
    duration = float(stop - start)

    if tPower[0] < Boss :
        st.error(f'Total Power Kurang dari Power Boss: {tPower} vs {Boss} ')
    elif Boss == 0 :
        st.error(f'Output Tidak Valid')
    else     : 
        st.success(f'Fighter : {hfighter}')
        st.success(f'Best Power : {tPower}')
        st.success(f'Sisa Koin : {SisaKoin}')
        st.success(f"Running time: {duration} seconds")

    hasil = []
    hfighter = []
    tPower = []


    start = time.time()
    # Mengurutkan fighters berdasarkan power menggunakan insertionSort
    Greedy.insertionSortDesc(fighters, keyPower=lambda x: x.power) #lambda adalah fungsi sederhana satu baris
    st.write("Menggunakan Algoritma Greedy by Power")
    for i in range(len(arrK)):
        st.write(fighters[i].nama,fighters[i].power,fighters[i].harga,fighters[i].dens)
    # Algoritma Knapsack menggunakan Greedy
    SisaKoin = Greedy.greedyABC(fighters, hasil, hfighter, Koin, tPower)
    
    st.write("Hasil Greedy by Power:")
    # Menampilkan output gambar
    img_output.output(hasil)
    stop = time.time()
    duration = float(stop - start)

    if tPower[0] < Boss :
        st.error(f'Total Power Kurang dari Power Boss: {tPower} vs {Boss} ')
    elif Boss == 0 :
        st.error(f'Output Tidak Valid')
    else :
        st.success(f'Fighter : {hfighter}')
        st.success(f'Best Power : {tPower}')
        st.success(f'Sisa Koin : {SisaKoin}')
        st.success(f"Running time: {duration} seconds")
    
    hasil = []
    hfighter = []
    tPower = []


    start = time.time()
    # Algoritma Knapsack menggunakan Greedy
    Greedy.insertionSortAsc(fighters, keyPower=lambda x: x.harga)
    SisaKoin = Greedy.greedyABC(fighters, hasil, hfighter, Koin, tPower)
    st.write("Menggunakan Algoritma Greedy by Harga")
    for i in range(len(arrK)):
        st.write(fighters[i].nama,fighters[i].power,fighters[i].harga,fighters[i].dens)
    st.write("Hasil Greedy by Harga:")
    # Menampilkan output gambar
    img_output.output(hasil)
    stop = time.time()
    duration = float(stop - start)

    if tPower[0] < Boss :
        st.error(f'Total Power Kurang dari Power Boss: {tPower} vs {Boss} ')
    elif Boss == 0 :
        st.error(f'Output Tidak Valid')
    else :
        st.success(f'Fighter : {hfighter}')
        st.success(f'Best Power : {tPower}')
        st.success(f'Sisa Koin : {SisaKoin}')
        st.success(f"Running time: {duration} seconds")

    hasil = []
    hfighter = []
    tPower = []

    start = time.time()
    
    Greedy.insertionSortDesc(fighters, keyPower=lambda x: x.dens)
    st.write("Menggunakan Algoritma Greedy by Density")
    for i in range(len(arrK)):
        st.write(fighters[i].nama,fighters[i].power,fighters[i].harga,fighters[i].dens) 
    SisaKoin = Greedy.greedyABC(fighters, hasil, hfighter, Koin, tPower)
    
    st.write("Hasil Greedy by Density:")
    # Menampilkan output gambar
    img_output.output(hasil)
    stop = time.time()
    duration = float(stop - start)

    if tPower[0] < Boss :
        st.error(f'Total Power Kurang dari Power Boss: {tPower} vs {Boss} ')
    elif Boss == 0 :
        st.error(f'Output Tidak Valid')
    else :
        st.success(f'Fighter : {hfighter}')
        st.success(f'Best Power : {tPower}')
        st.success(f'Sisa Koin : {SisaKoin}')
        st.success(f"Running time: {duration} seconds")

