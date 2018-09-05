# -*- coding: utf-8 -*-

from tkinter import ttk
import tkinter as tk
import PIL
from PIL import ImageTk

#--------------------------------------------
def APDD(base,to_add):
    new_dic = {**base,**to_add}
    return new_dic

def _TIH(str_input):

    output = 0
    if len(str_input) < 1:
        output = 0
    else:
        try:
            output = int(str_input)
        except:
            raise ValueError('''Input "{}" cannot be converted into an integer'''.format(str_input))
    return output

def toint(str_input):
    _type = type(str_input)
    output = None
    if _type == str:
        output = _TIH(str_input)
    elif _type == tuple:
        output = tuple(_TIH(i) for i in str_input)
    elif _type == int:
        output = str_input
    else:
        print("Values entered must be integers")
        raise ValueError
    return output

class GUI(object):
    def __init__(self,root,CMN,RMN,window_width=1200,window_height=400,fileformat='gif',icon_filename="PKS_Enumerator.ico"):
        self.CFN = [motif+'.'+fileformat for motif in CMN]
        self.RFN = [motif+'.'+fileformat for motif in RMN]
        self.root  = root
        self.mainframe = tk.Frame(self.root)
        self.AF  = tk.Frame(self.root)
        winSZ = str(window_width) + 'x' + str(window_height)
        self.root.geometry(winSZ)
        self.root.title("PKS Enumerator - North Carolina State Unversity")
        self.root.iconbitmap(icon_filename)

    def CBT(self):
        self.GEBT = tk.Button(self.root,text="Generate")
        self.label  = tk.Label(self.root,text="THIS IS A LABEL")

    def _make_MN(self,img_width=100,img_height=100):
        self.MN = ttk.Notebook(self.mainframe)
        self.CP = MTFPG(self.MN,self.CFN,img_width=img_width,img_height=img_height)
        self.RP = MTFPG(self.MN,self.RFN,img_width=img_width,img_height=img_height,entry_state='disabled')
        self.MN.add(self.CP, text='CM Structural MTs')
        self.MN.add(self.RP,text='RR Structural MTs')
        self.MN.pack(side='left')

    def _MRF(self):
        self.RGTF = tk.Frame(self.mainframe,relief='sunken',bd=1)
        self.MCSA = MCSE(self.RGTF)
        self.LBSA = LBSS(self.RGTF)
        self.MCSA.pack(padx=10,pady=10,fill='x')
        self.LBSA.pack(padx=10,pady=10,fill='x')
        self.RGTF.pack(side='right',padx=10)

    def _MMF(self):
        self._make_MN()
        self._MRF()
        self.mainframe.pack(padx=10,pady=10)

    def _MAF(self,call_back):
        self.STV  = tk.StringVar(value='')
        self.STL = tk.Label(self.AF,textvariable=self.STV)
        self.GEBT = tk.Button(self.AF,text='Generate',command=call_back)
        self.STL.pack(side='left',padx=10,pady=10)
        self.GEBT.pack(padx=10,pady=10)
        self.AF.pack(padx=10,pady=10,side='right')

    def start(self,call_back):
        self._MMF()
        self._MAF(call_back)

    def CLF(self):
        self.STV.set('Program running')
        SM_dic = {}
        BR_dic = {}
        SM_dic = APDD(SM_dic,self.CP.getETRE())
        SM_dic = APDD(SM_dic,self.RP.getETRE())
        BR_dic = APDD(BR_dic,self.MCSA.GIP())
        BR_dic = APDD(BR_dic,self.LBSA.GIP())
        return (SM_dic, BR_dic)

    def USB(self,text=''):
        self.STV.set(text)

class GEB(tk.Button):
    def __init__(self,parent,text='Generate',**kwargs):
        tk.Button.__init__(self,parent,text=text,**kwargs)

class MCSE(tk.Frame):
    def __init__(self,parent,title='Per Macrocycle'):
        tk.Frame.__init__(self,parent,bd=1,relief='sunken')
        self.title = tk.Label(self,text=title)

        self._setup()

    def _setup(self):
        self.labelCMF = tk.Label(self,text="Range of CM SMs from ")
        self.DFCEMN  = tk.StringVar(value='12')
        self.RCSMF = tk.Entry(self,textvariable=self.DFCEMN)
        self.LCSMT = tk.Label(self,text=" to ")
        self.DFCEMX = tk.StringVar(value='12')
        self.RCSMTT = tk.Entry(self,textvariable=self.DFCEMX)
        self.LRRFR = tk.Label(self,text="Range of RR SMs from ")
        self.DFREMN = tk.StringVar(value='0')
        self.RRRSMF = tk.Entry(self, state='disabled')
        self.LRSMT = tk.Label(self,text=" to ")
        self.DFREMX  = tk.StringVar(value='0')
        self.RRSMTT = tk.Entry(self, state='disabled')
        self.LTF = tk.Label(self,text="Range of Total SMs from ")
        self.DFTEMN = tk.StringVar(value='12')
        self.RTTSMF = tk.Entry(self,textvariable=self.DFTEMN)
        self.LTLTO = tk.Label(self,text=" to ")
        self.DFTEMX = tk.StringVar(value='12')
        self.RTLSMT = tk.Entry(self,textvariable=self.DFTEMX)
        self.PRIORITYVR          = tk.IntVar()
        self.PRIORITYVR.set(1)
        self.Lrad  = tk.Label(self, text="Prioritize:")
        self.CMRD = tk.Radiobutton(self, text="CM SMs",variable=self.PRIORITYVR,value=1)
        self.RRRD = tk.Radiobutton(self, text="RR SMs",variable=self.PRIORITYVR,value=0)
        self.title.grid(row=0,column=1)   #subtitle for the area
        self.labelCMF.grid(row=1,column=0,sticky=tk.W)
        self.RCSMF.grid(row=1,column=1)
        self.LCSMT.grid(row=1,column=2)
        self.RCSMTT.grid(row=1,column=3)
        self.LRRFR.grid(row=2, column=0,sticky=tk.W)
        self.RRRSMF.grid(row=2,column=1)
        self.LRSMT.grid(row=2,column=2)
        self.RRSMTT.grid(row=2,column=3)
        self.LTF.grid(row=3,column=0,sticky=tk.W)
        self.RTTSMF.grid(row=3,column=1)
        self.LTLTO.grid(row=3,column=2)
        self.RTLSMT.grid(row=3,column=3)
        self.Lrad.grid(row=4,column=0,sticky=tk.W)
        self.CMRD.grid(row=4,column=1)
        self.RRRD.grid(row=4,column=3)

    def GIP(self):
        INPD = {}
        INPD['CE']  = toint((self.DFCEMN.get(),self.DFCEMX.get()))
        INPD['RE']   = toint((self.DFREMN.get(),self.DFREMX.get()))
        INPD['TE']   = toint((self.DFTEMN.get(),self.DFTEMX.get()))
        INPD['AOB'] = toint(self.PRIORITYVR.get())
        return INPD

class LBSS(tk.Frame):
    def __init__(self,parent,title='Library'):
        tk.Frame.__init__(self,parent,bd=1,relief='sunken')
        self.title = tk.Label(self,text=title)
        self._setup()

    def _setup(self):
        self.LPRM   = tk.Label(self,text="Permutations to Skip ")
        self.PRMVR = tk.StringVar(value='1000')
        self.PRMTO_skip  = tk.Entry(self,textvariable=self.PRMVR)
        self.LLBSZ = tk.Label(self,text="Library Size ")
        self.LBVR = tk.StringVar(value='100')
        self.LBSZ  = tk.Entry(self,textvariable=self.LBVR)
        self.LADEX  = tk.Label(self,text="Add additional EX to each macrocycle")
        self.LOUP = tk.Label(self,text="Output as:")
        self.EXTEX  = tk.IntVar(value=1)
        self.CSVO = tk.IntVar(value=1)
        self.SDFO= tk.IntVar(value=1)
        self.EXBTN = tk.Checkbutton(self,variable=self.EXTEX)
        self.LFLN = tk.Label(self, text="Output file name:")
        self.FLNVR = tk.StringVar(value='MacrocycleLibrary')
        self.ENTFLN = tk.Entry(self,textvariable=self.FLNVR)
        self.title.grid(row=0,column=1)      #Subbtitle for the area
        self.LPRM.grid(row=1,column=0,sticky=tk.W)
        self.PRMTO_skip.grid(row=1,column=1)
        self.LLBSZ.grid(row=2,column=0,sticky=tk.W)
        self.LBSZ.grid(row=2,column=1)
        self.LADEX.grid(row=3,column=0)
        self.EXBTN.grid(row=3,column=1)
        self.LFLN.grid(row=4,column=0)
        self.ENTFLN.grid(row=4,column=1)

    def GIP(self):
        INPD = {}
        INPD['PS'] = toint(self.PRMVR.get())
        INPD['LS']= toint(self.LBVR.get())
        INPD['EX'] = toint(self.EXTEX.get())
        INPD['filename'] = self.FLNVR.get()
        if INPD['LS']> 1000000:
            INPD['LS'] = 1000000
        return INPD

class MTNTBK(ttk.Notebook):
    def __init__(self,parent,num_pages):
        ''''''

class MTFPG(ttk.Frame):
    def __init__(self,parent, MTFFLNMES,num_rows=3,num_cols=6,img_width=100,img_height=100,entry_state='normal'):
        ttk.Frame.__init__(self,parent)
        self.parent = parent
        self.FLNMES = MTFFLNMES
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.entry_state = entry_state
        self.CTPG(img_width,img_height)

    def CTPG(self,img_width,img_height):
        self.blocks = []
        MTFcount = 0
        for motif in self.FLNMES:
            r,c = divmod(MTFcount,self.num_cols)
            text = motif.split('.')[0]
            block = MTBLK(self,motif,text,img_width,img_height,self.entry_state)
            block.grid(row=r,column=c,padx=1,pady=1)
            self.blocks.append(block)
            MTFcount += 1
    def getETRE(self):
        entries_dic = {}
        for block in self.blocks:
            motif,value = block.GE()
            entries_dic[motif] = value
        return entries_dic

class MTBLK(tk.Frame):
    def __init__(self,parent,img_file, text_label,img_width=100,img_height=100, entry_state ='normal'):
        tk.Frame.__init__(self,parent,width=img_width,height=img_height,bg="#d3d3d3",relief='sunken')
        self.parent = parent
        self.imfile = img_file
        self.text = text_label
        self.img_width = img_width
        self.img_height = img_height
        self.entry_state = entry_state
        self._CBL()

    def _CBL(self):
        self.UPPFR = tk.Frame(self)
        self.IMGFRM = tk.Frame(self)
        self.PLIM= PIL.Image.open(self.imfile)
        self.PLIM = self.PLIM.resize((self.img_width, self.img_height), PIL.Image.ANTIALIAS)
        self.PLIM  = PIL.ImageTk.PhotoImage(self.PLIM,master=self)
        self.img = tk.Label(self, image=self.PLIM)
        self.img.image = self.PLIM
        self.label = tk.Label(self.UPPFR,text=self.text+' x ', bg='black',fg='white',anchor=tk.W)
        self.DFvalues = tk.StringVar(value='0')
        self.entry = tk.Entry(self,textvariable=self.DFvalues, state=self.entry_state)
        self.UPPFR.pack(fill='x')
        self.img.pack(fill='both')
        self.label.pack(side='left',fill='x',expand=1)
        self.entry.place(relx=1.8,x=2,y=-2,anchor=tk.N+tk.E)

    def GE(self):
        return (self.text,toint(self.DFvalues.get()))


class MainFrame(tk.Frame):
    def __init__(self,parent):
        ''''''