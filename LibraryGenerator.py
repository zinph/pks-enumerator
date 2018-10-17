#-------------------------------------------------------------------------------
# Name:        main
# Purpose:
#
# Author:      zinph
#
# Created:     01/11/2016
# Copyright:   (c) zinph 2016

'''
# LIMITED VERSION #
max library size is 1 million and RSMs aren't allowed.

'''
#-------------------------------------------------------------------------------
import os
import time
import tkinter as tk
from PKS_class import *
from GUI_class import *
import shutil
import tempfile

def CNVT(second):
    day = second/86400
    hour = (day - int(day))*24
    minute = (hour - int(hour))*60
    second = round((minute - int(minute))*60,4)
    return(str(int(day)) + ' DAYS: '+ str(int(hour)) + ' HOURS: '+ str(int(minute)) + ' MINUTES: ' + str(second) + ' SECONDS')

def CRD(name):
    ODD = os.getcwd()
    NDD = os.path.join(ODD, name)
    try:
        os.mkdir(NDD)
    except FileExistsError:
        print('Folder name exists. It will be replaced.')
        tmp = tempfile.mktemp(dir=os.path.dirname(name))
        shutil.move(name, tmp)
        shutil.rmtree(tmp)
        os.mkdir(NDD)
    return NDD

def generate(gui):

    SML, BLDR = gui.CLF()
    NDD = CRD(BLDR['filename'])
    os.chdir(NDD)
    start_time = time.time()
    sample = PKS_class(BLDR, SML)
    sample.GAL()
    duration = CNVT(time.time()-start_time)
    print('Time Elapsed for Enumeration: ' + str(duration))
    sample.CVSMITE()
    sample.csv_NFF()
    sample.NFFW(duration)
    print('End of Program.')
    gui.USB('Finished.')

def main():

    COMMON_SM_LIST = ['SM001','SM002','SM003','SM004','SM005','SM006','SM008','SM009','SM013'] #filnames of gif files. I am not including extension in case it needs to be different
    RARE_SM_LIST   = ['SM007','SM010','SM011','SM012','SM014','SM015','SM016']
    ext            = 'gif'
    root = tk.Tk()
    gui = GUI(root,COMMON_SM_LIST,RARE_SM_LIST,fileformat=ext)
    gui.start(lambda: generate(gui))
    root.mainloop()

if __name__.endswith('__main__'):
    main()