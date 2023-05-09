import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np
with st.sidebar :
    navbar = option_menu(menu_title=None,
             options=['Home', 'Asam Kuat oleh Basa Kuat', 'Basa Lemah oleh Asam Kuat', 'Basa Kuat oleh Asam Kuat', 'Asam Lemah oleh Basa Kuat'])
if navbar == 'Home':
    st.title('Aplikasi penghitung Kadar pH :red[Titrasi Asam Basa]')
    st.write('dibuat oleh: **kelompok 3**')
    st.write('**Annisa Nabillah** (2219035)')
    st.write('**Aulia Falina Putri** (2219042)')
    st.write('**Muhammad Ramlan Agustian** (2219117)')
    st.write('**Reisya Putri Apranti** (2219155)')

if navbar == 'Asam Kuat oleh Basa Kuat' :
    st.title('menghitung kadar pH titrasi :green[Asam Kuat oleh Basa Kuat]')
    M_titrat= st.number_input('masukkan :blue[Molaritas titran]',step = 0.0001, format = "%.4f", value = 0.1000)
    V_titrat= st.number_input('masukkan :blue[volume titran]',value = 25.00)
    M_titran= st.number_input('masukkan :red[Molaritas titrat]',step = 0.0001, format = "%.4f", value = 0.1000)
    V_titran= st.number_input('masukkan :red[volume titrat]',value = 25.00)

    mmol_titrat= M_titrat * V_titrat
    mmol_titran= M_titran * V_titran
    V_total= V_titrat + V_titran

    sisa_mol= abs(mmol_titran - mmol_titrat)
    Konsentrasi= sisa_mol/V_total

    pH = round(-(np.log10(Konsentrasi)),2)
    if st.button('tampilkan nilai ph') :
        if mmol_titran < mmol_titrat :
            st.write('nilai pH adalah :',14 - pH)
        elif mmol_titran == mmol_titrat :
            st.write('nilai pH adalah :' , 7)
        else :
            st.write('nilai pH adalah :' ,pH)
    else :
        st.write('tekan tombol untuk memunculkan nilai')

if navbar == 'Basa Lemah oleh Asam Kuat':
    st.title('menghitung kadar pH titrasi :green[Basa Lemah oleh Asam Kuat]')
    M_titran= st.number_input('masukkan :blue[Molaritas titran]',step = 0.0001, format = "%.4f", value = 0.1000)
    V_titran= st.number_input('masukkan :blue[volume titran]',value = 25.00)
    
    ka_titrat = st.number_input('masukkan :red[Kb titrat (10^5)]',value = 1.8)
    kb = ka_titrat * 10**(-5)
    
    M_titrat= st.number_input('masukkan :blue[Molaritas titrat]',step = 0.0001, format = "%.4f", value = 0.1000)
    V_titrat= st.number_input('masukkan :blue[volume titrat]',value = 25.00)

    mmol_titrat= round((M_titrat * V_titrat),2)
    mmol_titran= round((M_titran * V_titran),2)
    V_total= V_titrat + V_titran

    sisa_mol= abs(mmol_titran - mmol_titrat)
      
    if st.button('tampilkan nilai pH') :
        
        # Garam Terhodirolisis
        if mmol_titran == mmol_titrat :
            Cg = round((mmol_titran/V_total),3)
            konsentrasi = np.sqrt((10**(-14)/kb)*Cg)
            pH = round(-(np.log10(konsentrasi)),2)
            st.write('Nilai pH adalah ', pH,':green[[Garam Terhidrolisis]]')
         # Asam   
        elif mmol_titran > mmol_titrat  :
            konsentrasi = (sisa_mol/V_total)
            pH = round(-(np.log10(konsentrasi)),2)
            st.write('Nilai pH adalah', pH , ':green[[Asam]]')
        #Buffer    
        else :
            Cg = sisa_mol
            konsentrasi = (mmol_titrat/Cg) * ka
            ph = round(-(np.log10(konsentrasi)),2)
            st.write('Nilai pH adalah', ph, ':green[[Buffer]]')
    else :
        st.write('Tekan tombol untuk memunculukan nilah pH')
        
if navbar ==  'Basa Kuat oleh Asam Kuat':
    st.title('menghitung kadar pH titrasi :green[Basa Kuat oleh Asam Kuat]')
    M_titrat= st.number_input('masukkan :blue[Molaritas titran]',step = 0.0001, format = "%.4f", value = 0.1000)
    V_titrat= st.number_input('masukkan :blue[volume titran]',value = 25.00)
    M_titran= st.number_input('masukkan :red[Molaritas titrat]',step = 0.0001, format = "%.4f", value = 0.1000)
    V_titran= st.number_input('masukkan :red[volume titrat]',value = 25.00)

    mmol_titrat= M_titrat * V_titrat
    mmol_titran= M_titran * V_titran
    V_total= V_titrat + V_titran

    sisa_mol= abs(mmol_titran - mmol_titrat)
    Konsentrasi= sisa_mol/V_total

    pH = round(-(np.log10(Konsentrasi)),2)
    if st.button('tampilkan nilai ph') :
        if mmol_titran > mmol_titrat :
            st.write('nilai pH adalah :',14 - pH)
        elif mmol_titran == mmol_titrat :
            st.write('nilai pH adalah :' , 7)
        else :
            st.write('nilai pH adalah :' ,pH)
    else :
        st.write('tekan tombol untuk memunculkan nilai')
        
if navbar == 'Asam Lemah oleh Basa Kuat':
    st.title('menghitung kadar pH titrasi :green[Asam Lemah oleh Basa Kuat]')
    M_titran= st.number_input('masukkan :red[Molaritas titran]',step = 0.0001, format = "%.4f", value = 0.1000)
    V_titran= st.number_input('masukkan :red[volume titran]',value = 25.00)
    ka_titrat = st.number_input('masukkan :blue[Ka titrat (10^-5)]', value = 1.8)
    
    ka = ka_titrat * 10**(-5)
    M_titrat= st.number_input('masukkan :red[Molaritas titrat]',step = 0.0001, format = "%.4f", value = 0.1000)
    V_titrat= st.number_input('masukkan :red[volume titrat]',value = 25.00)

    mmol_titrat= round((M_titrat * V_titrat),2)
    mmol_titran= round((M_titran * V_titran),2)
    V_total= V_titrat + V_titran
    
    sisa_mol= abs(mmol_titran - mmol_titrat)
    
    if st.button('tampilkan nilai pH') :
        
        # Garam Terhodirolisis
        if mmol_titran == mmol_titrat :
            Cg = round((mmol_titran/V_total),3)
            konsentrasi = np.sqrt((10**(-14)/ka)*Cg)
            pH = round(-(np.log10(konsentrasi)),2)
            st.write('Nilai pH adalah ', round((14 - pH),2) ,':green[[Garam Terhidrolisis]]')
        # Basa    
        elif mmol_titran > mmol_titrat  :
            konsentrasi = (sisa_mol/V_total)
            pH = round(-(np.log10(konsentrasi)),2)
            st.write('Nilai pH adalah', round((14 - pH),2) , ':green[[Basa]]')
        # Buffer
        else :
            Cg = sisa_mol
            konsentrasi = (mmol_titrat/Cg) * ka
            ph = round(-(np.log10(konsentrasi)),2)
            st.write('Nilai pH adalah',round((14 - ph),2) , ':green[[Buffer]]')
    else :
        st.write('Tekan tombol untuk memunculukan nilah pH')
        
    
