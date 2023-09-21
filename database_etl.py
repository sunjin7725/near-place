import pandas as pd

from common.database_connection import SQLitePlaceDB, PostgresPlaceDB
from common.utils import put_dataframe_to_postgres, put_dataframe_to_sqlite


data_dir = 'data'

conn = PostgresPlaceDB().conn

df = pd.read_csv(data_dir + '/전국업종별_사업체정보_2021년_12월.csv', dtype=str)
df = df.loc[:, ['bizrno', 'bsnm_nm', 'bsns_detail_road_addr', 'induty_cd', 
                'dta_creat_ym', 'bsnm_tpcd', 'induty_nm', 'bplc_zip', 
                'bsns_detail_gibun_addr', 'web_fax_no', 'web_ceo_nm',
                'web_addr', 'web_tel_no', 'web_emp_co']]

put_dataframe_to_postgres(conn=conn, dataframe=df, table_name='TB_PLACE')