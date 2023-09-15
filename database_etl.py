import pandas as pd

from common.database_connection import PlaceDB
from common.utils import put_dataframe_to_database


data_dir = 'data'

conn = PlaceDB().conn

df = pd.read_csv(data_dir + '/전국업종별_사업체정보_2021년_12월.csv')
df = df.loc[:, ['bizrno', 'bsnm_nm', 'bsns_detail_road_addr', 'induty_cd', 
                'dta_creat_ym', 'bsnm_tpcd', 'induty_nm', 'bplc_zip', 
                'bsns_detail_gibun_addr', 'web_fax_no', 'web_ceo_nm',
                'web_addr', 'web_tel_no', 'web_emp_co']]

put_dataframe_to_database(conn=conn, dataframe=df, table_name='TB_PLACE')