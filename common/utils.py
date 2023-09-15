import pandas as pd

def put_dataframe_to_database(conn, dataframe: pd.DataFrame, table_name: str):
    cursor = conn.cursor()
    
    sql = f"""
    INSERT OR REPLACE INTO {table_name} VALUES ({', '.join(['?' for _ in dataframe.columns])})
    """
    
    for idx, row in dataframe.iterrows():
        cursor.execute(sql, row)
    conn.commit()
    cursor.close()
