import numpy as np
import pandas as pd

from tqdm import tqdm


def put_dataframe_to_postgres(conn, dataframe: pd.DataFrame, table_name: str):
    cursor = conn.cursor()
    
    sql = f"""
    WITH upsert AS (
        update {table_name} set
              DTA_CHNG_YYYYMM = %s
            , BSNS_TPCD = %s
            , BSNS_INDUTY_NM = %s
            , BPLC_ZIP = %s 
            , BSNS_DETAIL_GIBUN_ADDR = %s
            , WEB_FAX_NO = %s
            , WEB_CEO_NM = %s
            , WEB_ADDR = %s
            , WEB_TEL_NO = %s
            , WEB_EMP_CO = %s
        where
              BSNS_NO = %s
          and BSNS_NM = %s
          and BSNS_DETAIL_ROAD_ADDR = %s
          and BSNS_INDUTY_CD = %s
        returning *
    )
    insert into {table_name}
    select 
         %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
    where not exists(select * from upsert);
    """
    dataframe = dataframe.replace([np.nan], [None])
    for idx, row in tqdm(dataframe.iterrows(), total=dataframe.shape[0]):
        cursor.execute(sql, (row.dta_creat_ym, row.bsnm_tpcd, row.induty_nm, row.bplc_zip, row.bsns_detail_gibun_addr,
                             row.web_fax_no, row.web_ceo_nm, row.web_addr, row.web_tel_no, row.web_emp_co,
                             row.bizrno, row.bsnm_nm, row.bsns_detail_road_addr, row.induty_cd, *row))
    conn.commit()
    cursor.close()


def put_dataframe_to_sqlite(conn, dataframe: pd.DataFrame, table_name: str):
    cursor = conn.cursor()
    
    sql = f"""
    INSERT OR REPLACE INTO {table_name} VALUES ({', '.join(['?' for _ in dataframe.columns])})
    """
    
    for idx, row in dataframe.iterrows():
        cursor.execute(sql, row)
    conn.commit()
    cursor.close()

