# file_clubbing
import pandas as pd
import os
import re
for i in range(710):
    fin_txt=[]
    fin_txt_str=''
    flag=1
    page=0
    while(flag==1):
        f1=open('./img/Bi2i_'+str(i).zfill(4)+'/Bi2i_'+str(i).zfill(4)+'-'+str(page).zfill(2)+'.txt','r',encoding='utf-8')
        doc=f1.readlines()
        fin_txt+=doc
        if not os.path.isfile('./img/Bi2i_'+str(i).zfill(4)+'/Bi2i_'+str(i).zfill(4)+'-'+str(page+1).zfill(2)+'.txt'):
            flag=0
        page=page+1
    f1.close()
    f2=open('./nlp_concat_files/Bi2i_'+str(i).zfill(4)+'.txt','w')
    f2.write(re.sub(r'[^\x00-\x7F]+',' ', fin_txt_str.join(fin_txt)))
    f2.close()
