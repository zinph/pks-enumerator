#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      zinph
#
# Created:     01/11/2016
# Copyright:   (c) zinph 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os
from random import shuffle
from rdkit import Chem
from rdkit.Chem import Descriptors
from rdkit.Chem import AllChem
from itertools import *

class PKS_class:

    def __init__(self, cmd, SMR):
        self.SMD = {'SM001':"C",'SM002':"C(C)",'SM003':"C(CC)",'SM004':"C(O)",'SM005':"C(OC)",'SM006':"C(O)(C)",'SM007':"C(OC)(C)",'SM008':"C(CC=O)",'SM009':"C(=O)",'SM010':"C(C)(F)",'SM011':"C(OC(=O)C)",'SM012':"C2(OC2)",'SM013':"C=C",'SM014':"C(OC(=O)CC)",'SM015':"N(C)",'SM016':"C3OC3"}
        self.inv_SMD = {v: k for k, v in self.SMD.items()}
        self.SMR = SMR
        self.cmd = cmd
        self.SMH()
        self.TLL = self.GMML(self.cmd['TE'][0],self.cmd['TE'][1])
        self.NFF = {}
        self.TNKPDs = 0
        self.CRL= []
        self.SMI = {}
        self.SMU()

    def IS1(self, chain, index):
        return chain[:index] + '1' + chain[index:]

    def SMU(self):
        for i in self.CEL:
            self.SMI.update({i:[0,{1:0}]})
        for i in self.REL:
            self.SMI.update({i:[0,{1:0}]})

    def DC(self, KPD):
        'Computes six molecular descriptors for the input compound via RDKit library: Molecular Weight - MW, Hydrophobicity - SlogP, Hydrogen Bond Acceptors - HBA, Hydrogen Bond Donors - HBD, Topological Polar Surface Area - TPSA, and Rotatable Bonds – NRB.'
        MW = Descriptors.MolWt(KPD)
        TPSA = Descriptors.TPSA(KPD)
        HBA = Descriptors.NumHAcceptors(KPD)
        HBD = Descriptors.NumHDonors(KPD)
        NRB = Descriptors.NumRotatableBonds(KPD)
        MolLogP = Descriptors.MolLogP(KPD)
        return [MW,TPSA,MolLogP,HBA,HBD,NRB]

    def SMH(self):
        CML = ['SM001','SM002','SM003','SM004','SM005','SM006','SM008','SM009','SM013']
        RML = ['SM007','SM010','SM011','SM012','SM014','SM015','SM016']
        self.CEL,self.REL = [],[]
        SMs = sorted(self.SMD)
        for i in SMs:
            if i in CML:
                self.CEL+=[self.SMD[i]]*self.SMR[i]
            elif i in RML:
                self.REL+=[self.SMD[i]]*self.SMR[i]
        shuffle(self.CEL)
        shuffle(self.REL)

    def CVSMITE(self):
        for i in range(len(self.CEL)):
            self.CEL[i]=self.inv_SMD[self.CEL[i]]
        for i in range(len(self.REL)):
            self.REL[i]=self.inv_SMD[self.REL[i]]
        SMIKY = list(self.SMI.keys())
        for each in SMIKY:
            self.SMI[self.inv_SMD[each]]=self.SMI.pop(each)

    def PC(self, SML, LGD):
        'Generates all different combinations of SMs per input length. '
        RQL = []
        for j in combinations(SML,LGD):
            list(j).sort()
            ITF = self.BS(RQL,list(j))
            if ITF == False:
                RQL.append(list(j))
        return RQL

    def BS(self, LGIV, TGR):
        'Searches target item in the given list. Implemented to ensure no duplicate macrocycles are generated.'
        LGIV.sort()
        L = 0
        H = len(LGIV)-1
        F = False
        while L<=H and not F:
            MP = (L+H)//2
            C =  LGIV[MP]
            if C == TGR:
                F = True
            else:
                if TGR < C:
                    H = MP -1
                else:
                    L = MP +1
        return F

    def DRSF(self):
        FL = os.listdir()
        for i in FL:
            if 'RS_' in i:
                os.remove(i)

    def GAL(self):
        '''
        Generate macrocycles for all total lengths.
        '''
        self.GLP()
        for j in self.TLL:
            if self.TNKPDs < self.cmd['LS']:
                KY = 'RS_'+str(j)
                self.csvFH = open(KY+'.csv', 'a+')
                self.csvFH.write("MW,TPSA,SlogP,HBA,HBD,RB\n")
                self.NFF[KY] = 0
                self.GM(j)
                self.csvFH.close()
                print('RS_'+ str(j) + ' file has been completed.')
                print(str(self.NFF[KY]) + ' compounds are in RS_'+ str(j) +'.sdf.\n')
            else:
                return

    def GM(self,total_length):
        '''
        Generate macrocycles.
        '''
        LFEL =[]
        for p in self.CRL:
            if p[0]+p[1] == total_length:
                file = 'RS_'+ str(total_length)
                temp_CML = self.PC(self.CEL,p[0])
                temp_RML = self.PC(self.REL,p[1])
                for r in product(temp_CML, temp_RML):
                    if self.TNKPDs < self.cmd['LS']:
                        MAIL = list(r[0] + r[1])
                        MAIL.sort()
                        TSTR = ''.join(MAIL)
                        ITF = self.BS(LFEL,TSTR)
                        if ITF == False:
                            self.USMI(MAIL)
                            LFEL.append(TSTR)
                            self.GC(MAIL,file)
                    else:
                        return

    def USMI(self,MAIL):
        '''
        Update structural motif info.
        '''
        for each in self.CEL:
            EAC = MAIL.count(each)
            if EAC not in self.SMI[each][1]:
                self.SMI[each][1].update({EAC:0})
        for each in self.REL:
            EAC = MAIL.count(each)
            if EAC not in self.SMI[each][1]:
                self.SMI[each][1].update({EAC:0})

    def GMML(self,mini,maxi):
        '''
        Generate a list from minimum to maximum. for example, if min is 2 and max is 5, generate [2,3,4,5].
        '''
        MML = []
        for i in range(maxi-mini+1):
            MML.append(mini)
            mini+=1
        return MML

    def RD(self, FN):
        lines_set = set([i.rstrip() for i in open(FN, 'r').readlines()])
        out  = open(FN, 'w')
        KY = FN[:5]
        self.NFF[KY]= 0
        for line in lines_set:
            out.write(line+'\n')
            self.NFF[KY]+=1
            self.TNKPDs+=1
        out.close()

    def GLP(self):
        '''
        Generates all possible common and rare SM length arrangements based on total number of SMs allowed in the program.
        '''
        CL = self.GMML(self.cmd['CE'][0],self.cmd['CE'][1])
        RL = self.GMML(self.cmd['RE'][0],self.cmd['RE'][1])
        for i in self.TLL:
            for j in CL:
                for k in RL:
                    if j+k == i:
                        ITF = self.BS(self.CRL,[j,k])
                        if ITF == False:
                            self.CRL.append([j,k])
                            self.CRL.sort()
        if self.cmd['AOB']==1:
            self.CRL.sort(reverse=True)
        elif self.cmd['AOB']==0:
            self.CRL.sort()

    def WDTF(self, FM, DSCL):
        '''
        Create SDF files.
        '''
        FM.write('> <MolecularWeight>\n'+str(DSCL[0])+'\n\n')
        FM.write('> <TPSA>\n'+str(DSCL[1])+'\n\n')
        FM.write('> <MolLogP>\n'+str(DSCL[2])+'\n\n')
        FM.write('> <NumHBA>\n'+str(DSCL[3])+'\n\n')
        FM.write('> <NumHBD>\n'+str(DSCL[4])+'\n\n')
        FM.write('> <NumRotatableBonds>\n'+str(DSCL[5])+'\n\n$$$$\n')

    def NFFW(self, time):
        '''
        Write info.txt file.
        '''
        if self.cmd['AOB'] ==1:
            C_or_R = 'common structural motifs'
        else:
            C_or_R = 'rare structural motifs'
        if self.cmd['EX']==1:
            AES = 'An ester was added to each macrocycle.'
        else:
            AES = 'No ester was added to macrocycle.'
        IFR = open('info.txt','w')
        IFR.write('Building Rules\nPer macrocycle:\n\nRange of common structural motifs per macrocycle - '+str(self.cmd['CE'][0])+' to '+str(self.cmd['CE'][1])+'\nRange of rare structural motifs per macrocycle - '+str(self.cmd['RE'][0])+' to '+str(self.cmd['CE'][1])+'\nRange of total structural motifs per macrocycle - '+str(self.cmd['TE'][0])+' to '+str(self.cmd['TE'][0])+'\nPrioritize - '+C_or_R+'\n'+AES+'\n\n')
        IFR.write('Library\nPermutations to skip - '+str(self.cmd['PS'])+'\nLibrary size - '+str(self.cmd['LS'])+' macrocycles.\n')
        for i in sorted(self.NFF):
            IFR.write(str(self.NFF[i])+' macrocycles has '+i[3:]+' structural motifs each.\n\n')
        IFR.write('common structural motifs and rare structural motifs were permuted in the following order:\ncommon structural motifs: '+str(self.CEL)+'\nrare structural motifs: '+str(self.REL)+'\n\n')
        IFR.write(('Time Elapsed for Enumeration: ' + str(time)) +'\n')
        IFR.close()

    def csv_NFF(self):
        FQR = [i+1 for i in range(max([max(self.SMI[i][1]) for i in self.SMI]))]
        FM = open('SM_distribution.csv','a+')
        FRH=','.join([str(i) + ' per macrocycle' for i in FQR])
        header = 'structural motifs, total structural motifs,'+FRH+'\n'
        FM.write(header)
        for i in sorted(self.SMI):
            TW=i+','+str(self.SMI[i][0])+','
            FM.write(TW)
            for j in FQR:
                if j in self.SMI[i][1]:
                    CUPMCC = str(self.SMI[i][1][j])+','
                    FM.write(CUPMCC)
                else:
                    FM.write('0,')
            FM.write('\n')
        FM.close()

    def GC(self,MAL,file):
        '''
        Permutate and generate a list of compounds stitched together from each list with proper format.
        Executes commands for ester chain & number of compounds generated.
        '''
        CPDC = 0
        CT = 0
        FT = file +'.sdf'
        SMFL = file + '.smi'
        SMFH = open(SMFL, 'a+')
        FH = open(FT,'a+')
        SN = self.cmd['PS']
        for i in permutations(MAL):
            if CT%SN == 0:
                if self.TNKPDs < self.cmd['LS']:
                    SML =  list([str(x) for x in i])
                    if len(SML) >= self.cmd['TE'][0] and len(SML) <=self.cmd['TE'][1]:
                        KPD = ''.join(SML)
                        if self.cmd['EX'] == 1:
                            smile = 'O1C(=O)' + KPD +'1'
                        elif self.cmd['EX'] ==0:
                            smile = self.IS1(''.join(SML)+'1',1)
                        SMFH.write(smile+'\n')
                        MCC = Chem.MolFromSmiles(smile)
                        if self.cmd['SKD'] != 1:
                            AllChem.Compute2DCoords(MCC)
                            AllChem.EmbedMolecule(MCC,AllChem.ETKDG())
                        FH.write(Chem.MolToMolBlock(MCC))
                        DESL = self.DC(MCC)
                        self.WDTF(FH,DESL)
                        CSVCP = ','.join(str(i) for i in DESL)+'\n'
                        self.csvFH.write(CSVCP)
                        CPDC+=1
                        self.TNKPDs+=1
                else:
                    break
            CT += 1
        SMFH.close()
        FH.close()
        self.NFF[file] += CPDC
        NDML = list(set(MAL))
        for each in NDML:
            FQ = MAL.count(each)
            self.SMI[each][1][FQ]+=CPDC
            self.SMI[each][0]+=CPDC*FQ