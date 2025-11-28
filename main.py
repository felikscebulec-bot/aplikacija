import streamlit as st
import izracun_kolicine
import izracun_sestavin
import kalkulator_kolicine
import kalkulator_viskoznosti_kolicine
import pandas as pd

excel=st.sidebar.file_uploader("VSTAVITE EXCEL DATOTEKO",type=["xlsx"])
if excel is not None:
 st.session_state["excel"]=excel
 st.success("Datoteka je naložena")

st.sidebar.title("Izberite program, ki ga želite uporabiti")
choice=st.sidebar.radio ( " ",["Izračun količin","Izračun sestavin","Kalkulator količin","Kalkulator viskoznosti in količin"])
if choice=="Izračun količin":
    izracun_kolicine.run()
elif choice=="Izračun sestavin":
    izracun_sestavin.run()
elif choice=="Kalkulator količin":
    kalkulator_kolicine.run() 
elif choice=="Kalkulator viskoznosti in količin":
    kalkulator_viskoznosti_kolicine.run()

st.sidebar.write(" ")
st.sidebar.write(" ")
st.sidebar.write(" ")
st.sidebar.write(" ")
st.sidebar.image("vizitka3.png",use_container_width=True)
