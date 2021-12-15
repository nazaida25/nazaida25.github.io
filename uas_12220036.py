#Ujian Akhir Semester Pemrograman Komputer
#Nama  : Naza Zaida Mustofa
#NIM   : 12220036
#Kelas : 02


from numpy import e
import pandas as pd
import streamlit as st

# Container declarations
header_container = st.container()
minyak_graph_container = st.container()
n_besar_negara = st.container()
n_terbesar = st.container()
informasi_negara = st.container()
negara_filtered = st.container()

# Data load
df = pd.read_csv('produksi_minyak_mentah.csv', index_col="kode_negara")
dfC = pd.read_json("kode_negara_lengkap.json")

# Data cleanup
for nCode in df.index.unique().tolist():
    if nCode not in dfC['alpha-3'].tolist():
        print('IS TRUE nCode:', nCode)
        df.drop([nCode], inplace=True)
df.reset_index(inplace=True)

with header_container:
    st.title("Data produksi minyak negara")
    st.markdown("***")

with minyak_graph_container:
    st.markdown("### Grafik jumlah produksi minyak mentah")

    def findNegara(nCode):
        return dfC[dfC["name"] == nCode]["alpha-3"].values[0]
    
    def listNegaraCreate():
        out = []
        listUsed = df['kode_negara'].unique().tolist()
        for ele in listUsed:
            try:
                out.append(dfC.loc[dfC['alpha-3'] == ele].values[0][0])
            except Exception:
                pass
        return out
    
    listNegara = listNegaraCreate()

    select_negara = st.selectbox("Pilih negara", listNegara)

    kodeNegara = findNegara(select_negara)
    st.write(f'Negara yang dipilih: {select_negara}. Kode: {kodeNegara}')
    display_data = df[df["kode_negara"] == kodeNegara][['tahun', 'produksi']]
    display_data = display_data.rename(columns={'tahun':'index'}).set_index('index')
    st.bar_chart(display_data)

with n_besar_negara:
    try:
        st.markdown("***")
        st.markdown('### Negara produksi minyak terbesar per tahun')
        userTahunInput = st.text_input('Tahun yang ingin dicek')
        userJumlahInput = st.text_input('Jumlah peringkat')
        minyakTahun = df.loc[df["tahun"] == int(userTahunInput)].sort_values(["produksi"], ascending=[0])
        minyakTahun = minyakTahun[:int(userJumlahInput)].reset_index(drop=True)
        minyakTahunOut = minyakTahun[['kode_negara', 'produksi']].rename(columns={'kode_negara':'index'}).set_index('index')
        st.write(minyakTahunOut)
        st.bar_chart(minyakTahunOut)
    except Exception:
        st.error('Pastikan anda memasukkan tahun dan jumlah negara yang valid. Apabila sudah, maka data dan grafik akan muncul.')

with n_terbesar:
    st.markdown('***')
    st.markdown('### Negara dengan produksi terbesar')
    userJmlInputRank = st.text_input('Jumlah negara')
    sumProduksi = (df[['kode_negara', 'produksi']].groupby('kode_negara', as_index=False).sum().sort_values(['produksi'], ascending=[0])).reset_index(drop=True)
    sumProduksi = sumProduksi[:int(userJmlInputRank)].reset_index(drop=True)
    sumProduksiOut = sumProduksi[['kode_negara', 'produksi']].rename(columns={'kode_negara':'index'}).set_index('index')
    st.write(sumProduksiOut)
    st.bar_chart(sumProduksiOut)
    
with informasi_negara:
    st.markdown('***')
    st.markdown('### Informasi negara')
    userInputNegara = st.selectbox("Pilih negara yang ingin dicek", listNegara)

    namaNegara = userInputNegara
    kodeNegara = dfC[dfC["name"] == namaNegara]["alpha-3"].values[0]
    regionNegara = dfC[dfC["name"] == namaNegara]["region"].values[0]
    subregionNegara = dfC[dfC["name"] == namaNegara]["sub-region"].values[0]
    tertinggiProduksi = df.loc[df['kode_negara'] == kodeNegara]
    tertinggiProduksiIndex = tertinggiProduksi[['tahun', 'produksi']]['produksi'].idxmax()
    tertinggiProduksi = df[tertinggiProduksiIndex:tertinggiProduksiIndex+1]
    tertinggiProduksiJml = tertinggiProduksi['produksi'].values[0]
    tertinggiProduksiTahun = tertinggiProduksi['tahun'].values[0]
    ProduksiTotal = df[['kode_negara', 'produksi']].groupby('kode_negara', as_index=False).sum()
    ProduksiTotal = ProduksiTotal[ProduksiTotal['kode_negara'] == kodeNegara]['produksi'].values[0]
    st.markdown(f'#### Data negara {namaNegara}')
    st.markdown(f'Nama: **{namaNegara}**')
    st.markdown(f'Kode: **{kodeNegara}**')
    st.markdown(f'Region: **{regionNegara}**')
    st.markdown(f'Subregion: **{subregionNegara}**')
    st.markdown(f'#### Data produksi {namaNegara}')
    st.markdown(f'Produksi tertinggi sebanyak **{tertinggiProduksiJml}** pada tahun **{tertinggiProduksiTahun}**')
    st.markdown(f'Selama ini telah memproduksi sebanyak **{ProduksiTotal}**')

with negara_filtered:
    st.markdown('***')
    st.markdown('### Filter negara berdasar kategori')
    userPilihFilter1 = st.selectbox('Filter', ['Tertinggi', 'Terendah (bukan nol)', 'Nol'])
    userPilihFilter2 = st.selectbox('Cakupan', ['Semua waktu', 'Tahun tertentu'])
    if userPilihFilter1 == 'Tertinggi':
        if userPilihFilter2 == 'Tahun tertentu':
            try:
                userTahunInput = st.text_input('Tahun yang akan dicek untuk maksimum')
                dfMaxID = df[df['tahun'] == int(userTahunInput)]['produksi'].idxmax()
                negaraTahunMax = df[dfMaxID:dfMaxID+1]
                negaraTahunMaxKode = negaraTahunMax['kode_negara'].values[0]
                negaraTahunMaxNama = dfC[dfC["alpha-3"] == negaraTahunMaxKode]["name"].values[0]
                negaraTahunMaxRegion = dfC[dfC["name"] == negaraTahunMaxNama]["region"].values[0]
                negaraTahunMaxSubregion = dfC[dfC["name"] == negaraTahunMaxNama]["sub-region"].values[0]
                negaraTahunMaxProduksi = negaraTahunMax['produksi'].values[0]
                st.markdown(f'#### Negara produksi paling tinggi pada tahun {userTahunInput}')
                st.markdown(f'Nama: **{negaraTahunMaxNama}**')
                st.markdown(f'Kode: **{negaraTahunMaxKode}**')
                st.markdown(f'Region: **{negaraTahunMaxRegion}**')
                st.markdown(f'Subregion: **{negaraTahunMaxSubregion}**')
                st.markdown(f'Jumlah produksi: **{negaraTahunMaxProduksi}**')
            except Exception:
                st.error('Pastikan anda memasukkan tahun yang valid. Apabila sudah, maka data akan dimunculkan.')
        elif userPilihFilter2 == 'Semua waktu':
            dfMaxID = df['produksi'].idxmax()
            negaraMax = df[dfMaxID:dfMaxID+1]
            negaraMaxKode = negaraMax['kode_negara'].values[0]
            negaraMaxNama = dfC[dfC["alpha-3"] == negaraMaxKode]["name"].values[0]
            negaraMaxRegion = dfC[dfC["name"] == negaraMaxNama]["region"].values[0]
            negaraMaxSubregion = dfC[dfC["name"] == negaraMaxNama]["sub-region"].values[0]
            negaraMaxProduksi = negaraMax['produksi'].values[0]
            st.markdown(f'#### Negara produksi paling tinggi di semua waktu')
            st.markdown(f'Nama: **{negaraMaxNama}**')
            st.markdown(f'Kode: **{negaraMaxKode}**')
            st.markdown(f'Region: **{negaraMaxRegion}**')
            st.markdown(f'Subregion: **{negaraMaxSubregion}**')
            st.markdown(f'Jumlah produksi: **{negaraMaxProduksi}**')
    elif userPilihFilter1 == 'Terendah (bukan nol)':
        if userPilihFilter2 == 'Tahun tertentu':
            try:
                userTahunInputMin = st.text_input('Tahun yang akan dicek untuk minimum')
                dfMinF = df[df['tahun'] == int(userTahunInputMin)]
                dfMinF = dfMinF[dfMinF['produksi'] != 0]
                dfMinID = dfMinF['produksi'].idxmin()
                negaraTahunMin = df[dfMinID:dfMinID+1]
                negaraTahunMinKode = negaraTahunMin['kode_negara'].values[0]
                negaraTahunMinNama = dfC[dfC["alpha-3"] == negaraTahunMinKode]["name"].values[0]
                negaraTahunMinRegion = dfC[dfC["name"] == negaraTahunMinNama]["region"].values[0]
                negaraTahunMinSubregion = dfC[dfC["name"] == negaraTahunMinNama]["sub-region"].values[0]
                negaraTahunMinProduksi = negaraTahunMin['produksi'].values[0]
                st.markdown(f'#### Negara produksi paling rendah pada tahun {userTahunInput}')
                st.markdown(f'Nama: **{negaraTahunMinNama}**')
                st.markdown(f'Kode: **{negaraTahunMinKode}**')
                st.markdown(f'Region: **{negaraTahunMinRegion}**')
                st.markdown(f'Subregion: **{negaraTahunMinSubregion}**')
                st.markdown(f'Jumlah produksi: **{negaraTahunMinProduksi}**')
            except Exception:
                st.error('Pastikan anda memasukkan tahun yang valid. Apabila sudah, maka data akan dimunculkan.')
        elif userPilihFilter2 == 'Semua waktu':
            dfMinF = df[df['produksi'] > 0]
            dfMinF.reset_index(inplace=True)
            dfMinID = dfMinF['produksi'].idxmin()
            negaraMin = dfMinF[dfMinID:dfMinID+1]
            negaraMinKode = negaraMin['kode_negara'].values[0]
            negaraMinNama = dfC[dfC["alpha-3"] == negaraMinKode]["name"].values[0]
            negaraMinRegion = dfC[dfC["name"] == negaraMinNama]["region"].values[0]
            negaraMinSubregion = dfC[dfC["name"] == negaraMinNama]["sub-region"].values[0]
            negaraMinProduksi = negaraMin['produksi'].values[0]
            st.markdown(f'#### Negara produksi paling rendah di semua waktu')
            st.markdown(f'Nama: **{negaraMinNama}**')
            st.markdown(f'Kode: **{negaraMinKode}**')
            st.markdown(f'Region: **{negaraMinRegion}**')
            st.markdown(f'Subregion: **{negaraMinSubregion}**')
            st.markdown(f'Jumlah produksi: **{negaraMinProduksi}**')
    elif userPilihFilter1 == 'Nol':
        dfNolF = df[df['produksi'] == 0]
        dfNolF.reset_index(inplace=True)
        df0 = dfNolF['kode_negara'].unique()
        dfNolFNew = pd.DataFrame()
        dfNolFNew['nama_negara'] = [dfC[dfC['alpha-3'] == x]['name'].values[0] for x in df0]
        dfNolFNew['kode_negara'] = [ct for ct in df0]
        dfNolFNew['region'] = [dfC[dfC['alpha-3'] == x]['region'].values[0] for x in df0]
        dfNolFNew['subregion'] = [dfC[dfC['alpha-3'] == x]['sub-region'].values[0] for x in df0]
        dfNolFNew['Tahun'] = [df[df['kode_negara'] == x]['tahun'].values[0] for x in df0]
        dfNolFNew['produksi'] = [df[df['kode_negara'] == x]['produksi'].values[0] for x in df0]
        if userPilihFilter2 == 'Tahun tertentu':
            try:
                userInputTahunNol = st.text_input('Tahun yang akan dicek untuk produksi kosong')
                dfNolFNewF = dfNolFNew[dfNolFNew['Tahun'] == int(userInputTahunNol)]
                st.write(dfNolFNewF)
            except Exception:
                st.error('Pastikan anda memasukkan tahun yang valid. Apabila sudah, maka data akan dimunculkan.')
        elif userPilihFilter2 == 'Semua waktu':
            st.write(dfNolFNew)
            
            
            


    
    





