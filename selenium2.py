from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import shutil
import pandas as pd 
import numpy as np
import os
"""
os.remove(r'C:\Users\USUARIO\Documents\python\comparacion.xlsx')
os.rename('Filtro_ListaUNICA.xlsx','comparacion.xlsx')

"""
"""
driver = webdriver.Chrome('./chromedriver')
driver.get("")
print(driver.title)
search_bar = driver.find_element_by_name("usuario")
search_bar.clear()
search_bar.send_keys("")
search_bar = driver.find_element_by_name("password")

search_bar.send_keys("")
search_bar.send_keys(Keys.RETURN)
print(driver.current_url)


try:
	element = WebDriverWait(driver, 60).until(
	EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div/div[3]/button'))
	)
	elem = driver.find_element_by_xpath( '/html/body/div[4]/div/div/div/div[3]/button')
	elem.click()
	time.sleep(5)
	elem2 = driver.find_element_by_xpath('//*[@id="sidebar-wrapper"]/ul/li[12]/div')
	elem2.click()
	time.sleep(2)
	elem3 = driver.find_element_by_xpath('//*[@id="sidebar-wrapper"]/ul/li[12]/ul/li[15]/div')
	elem3.click()
	time.sleep(2)
	elem4 = driver.find_element_by_xpath('//*[@id="collapseOne"]/div/lanzador-consulta-directive/form/div[1]/div[1]/div[1]/div[1]/select')
	elem4.click()
	time.sleep(2)
	elem5 = driver.find_element_by_xpath('//*[@id="collapseOne"]/div/lanzador-consulta-directive/form/div[1]/div[1]/div[1]/div[1]/select/option[6]')
	elem5.click()
	time.sleep(2)
	elem6 = driver.find_element_by_xpath('//*[@id="collapseOne"]/div/lanzador-consulta-directive/form/div[2]/div/button[2]/span')
	elem6.click()
	time.sleep(10)


	print("Descargando...")
	carpetadescargas = r'C:\Users\USUARIO\Downloads\Listado de Precios - Activos.csv'
	carpetaconsultador = r'C:\Users\USUARIO\Documents\python\listaprecios.csv'
	shutil.move(carpetadescargas,carpetaconsultador)
	print("Movido y reemplazado")
	
	print("Lista de precios actualizada")
finally:
	print("no entro")
	driver.quit()
time.sleep(3)

 
"""  
  
df_new = pd.read_csv('listaprecios.csv',sep=";") 
  
GFG = pd.ExcelWriter('Conversion.xlsx') 
df_new.to_excel(GFG, index = False) 
  
GFG.save()  
c=0
df_new=pd.read_excel('Conversion.xlsx')
for i in pd.unique(df_new['ColumnaTres']):
	print(i)
	c+=1
	if c==10:
		break
df=df_new['ColumnaOcho']=="Lista UNICA"
filter_df= df_new[df]
print(filter_df.head())
dfinal = filter_df.reindex(columns=['ColumnaTres','ColumnaCuatro','ColumnaSeis','columnaUno','columnaDos','ColumnaCinco'])
dfinal.columns = ['Codigo', 'Descripcion', 'Precios', 'Rubro', 'Subrubro', 'Presentacion']
dfinal['Descripcion'] = dfinal['Descripcion'].str.upper()
nuevo = pd.ExcelWriter('Filtro_ListaUNICA.xlsx') 
dfinal.to_excel(nuevo, index = False) 
  
nuevo.save()
print("Lista filtrada y actualizada")

