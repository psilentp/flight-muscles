from IPython import display
print 'here'
class Genotype(dict):
    def __init__(self):
        self[0] = {'l':'wt','r':'wt'}
        self[1] = {'l':'wt','r':'wt'}
        self[2] = {'l':'wt','r':'wt'}
        self[3] = {'l':'wt','r':'wt'}
    
    def __str__(self):
        rstr = ''
        rstr += self[1]['l'] + '\t' + self[2]['l'] + '\t' + self[3]['l'] + '\n'
        rstr += '-'*len(self[1]['l']) + \
                    '\t' + '-'*len(self[2]['l']) + \
                    '\t' + '-'*len(self[3]['l']) + '\n'
        rstr += self[1]['l'] + '\t' + self[2]['l'] + '\t'+ self[3]['l'] + '\n'
        return rstr
        #print self
        
    def tbl(self):
        rstr = """<table border="1">"""
        rstr += """
                    <tr>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                    </tr>"""%(self[1]['l'],self[2]['l'],self[3]['l'])
        rstr += """
                    <tr>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                    </tr>"""%(self[1]['r'],self[2]['r'],self[3]['r'])
        rstr +=""" 
            </table>"""
        return rstr

strains = dict()
#################################
#################################
line = Genotype()
line[1] =   {'l':'HCS',
             'r':'HCS'}
line[2] = {'l':'P{Ubi-p63E(FRT.STOP)Stinger}9F6',
           'r':'P{y[+t7.7] w[+mC]=hs-FLPD5.fco}attP40'}
line[3] = {'l':'+',
           'r':'+'}
strains['objective 0: HS flipout of stop Stinger'] = display.HTML(line.tbl())
#################################
#################################
line = Genotype()
line[1] =   {'l':'HCS',
             'r':'HCS'}
line[2] = {'l':'P{y[+t7.7] w[+mC]=hs-FLPD5.fco}attP40',
           'r':'P{w[+mC]=tubP-GAL4}LL7'}
line[3] = {'l':'P{w[+mC]=alphaTub84B(FRT.GAL80)}',
           'r':'P{10XUAS-IVS-Syn21-GFP-p10}attP2'}
strains['objective 0: HS flipout of alphaTub Gal80'] = display.HTML(line.tbl())
#################################
#################################
line = Genotype()
line[1] =   {'l':'HCS',
             'r':'HCS'}
line[2] = {'l':'P{y[+t7.7] w[+mC]=hs-FLPD5.fco}attP40',
           'r':'P{w[+mC]=tubP(FRT.stop)GAL80}'}
line[3] = {'l':'P{10XUAS-IVS-Syn21-GFP-p10}attP2',
           'r':'P{w[+mC]=tubP-GAL4}LL7'}
strains['objective 0: HS flipout of tubP >stop> Gal80'] = display.HTML(line.tbl())
#################################
#################################
line = Genotype()
line[1] =   {'l':'HCS',
             'r':'HCS'}
line[2] = {'l':'P{y[+t7.7] w[+mC]=hs-FLPD5.fco}attP40',
           'r':'+'}
line[3] = {'l':'P{w[+mC]=UAS(FRT.stop)mCD8-GFP.H}14, P{w[+mC]=UAS(FRT.stop)mCD8-GFP.H}21B',
           'r':'P{w[+mC]=tubP-GAL4}LL7'}
strains['objective 0: HS flipout of UAS >stop> GFP'] = display.HTML(line.tbl())
#################################
#################################



