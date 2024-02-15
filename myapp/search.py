# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 09:54:03 2024

@author: USER
"""

import threading
import store1



def search_products(product):
    results = []

    
    pc24_thread = threading.Thread(target=store1.store().PC,args = (product,results))
    cf_thread = threading.Thread(target=store1.store().Carrefour,args = (product,results))
    momo_thread = threading.Thread(target=store1.store().momo,args = (product,results))
    poya_thread = threading.Thread(target=store1.store().Poya,args = (product,results))

    pc24_thread.start()
    cf_thread.start()
    momo_thread.start()
    poya_thread.start()
    pc24_thread.join()
    cf_thread.join()
    momo_thread.join()
    poya_thread.join()



product = input("輸入搜尋關鍵字:")

search_results = search_products(product)



