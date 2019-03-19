# file clubbing
import pandas as pd
import os
import re
for i in range(208):
    fin_txt=[]
    fin_txt_str=''
    flag=1
    page=0
    while(flag==1):
        f1=open('../nlp_text_files/Bi2i_'+str(i).zfill(4)+'-'+str(page)+'.txt','r',encoding='utf-8')
        doc=f1.readlines()
        fin_txt+=doc
        if not os.path.isfile('../nlp_text_files/Bi2i_'+str(i).zfill(4)+'-'+str(page+1)+'.txt'):
            flag=0
        page=page+1
    f2=open('../nlp_concat_files/Bi2i_'+str(i).zfill(4)+'.txt','w')
    f2.write(re.sub(r'[^\x00-\x7F]+',' ', fin_txt_str.join(fin_txt)))
    f2.close()
# basis point
import pandas as pd
basis_df=pd.DataFrame(columns=['fee_schedule_no','basis_point'])
for i in range(208):
    file_pointer=open('../nlp_concat_files/Bi2i_'+str(i).zfill(4)+'.txt','r',encoding='utf-8')
    temp_str=file_pointer.readlines()
    basis_lis=[]
    for line_ind in range(len(temp_str)):
        try: 
            if 'basis point fee' in temp_str[line_ind].lower() or 'basis point'  in temp_str[line_ind].lower() or 'basis points fee' in temp_str[line_ind].lower() or 'bps' in temp_str[line_ind]:
                for tmp_i in range(10):
                    tmp_lis=re.findall(r'[^$]\s+\d{1}\.\d{1,2}',temp_str[line_ind+tmp_i])
                    if(len(tmp_lis)>0):
                        basis_lis.append(temp_str[line_ind+tmp_i])
        except:
            continue;
    basis_df=basis_df.append({'fee_schedule_no':i,'basis_point':list(set(basis_lis))},ignore_index=True)
    file_pointer.close()
basis_df.to_csv('./basis_file_out.csv')