
import numpy as np
import pandas as pd
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('f1',help="f1")
    parser.add_argument('f2',help="f2")
    parser.add_argument('f3',help="f3")
    parser.add_argument('f4',help="f4")
    parser.add_argument('out',help="out")

    args = parser.parse_args()
    
    header_img = args.f1
    header_lbl = args.f2
    data_img= args.f3
    data_lbl= args.f4
    out= args.out

    df_header = pd.read_excel(header_img,sheet_name='IMG')
    df_header_lbl = pd.read_excel(header_lbl,sheet_name='Feuille 1')


    df_header = df_header.iloc[:,[1]]
    df_header_lbl = df_header_lbl.iloc[:,[1]]


    columns = list(df_header.squeeze().values)
    columns_lbl = list(df_header_lbl.squeeze().values)


    df_data= pd.read_csv(data_img,skiprows=1,skipfooter=1,engine='python',sep=';')
    df_data_lbl= pd.read_csv(data_lbl,skiprows=1,skipfooter=1,engine='python',sep=';')


    df_data.columns=columns
    df_data_lbl.columns = columns_lbl


    new_df = pd.merge(df_data,df_data_lbl,on=['ID_PRET'],how='inner')


    new_df['TAUX'] = new_df['TAUX_SANS_MARGE']+new_df['MARGE']




    df_data['TAUX'] = df_data['TAUX_SANS_MARGE']+df_data['MARGE']




    df_data['TEST_TAUX'] = df_data['TAUX']>2
    # df_data['TEST_TAUX'] = np.where(df_data['TAUX'] > 2, "TOTO", "TITI")



    nb_true = (df_data['TEST_TAUX']==True).sum()

    df_data[df_data['TEST_TAUX']==True]

    df_data.to_excel(out, index=False, engine='openpyxl')



if __name__=='__main__':
    main()




