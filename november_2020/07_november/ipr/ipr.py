import sqlite3
import pandas as pd

def connect():
    conn=sqlite3.connect("timesheet.db")  # Database Creation
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tax_flow(id INTEGER PRIMARY KEY, Date_on Date, Employee_ID text, Hours_in_VDI float, PNASD int, ANASD int, PNASE int, ANASE int, NASM int,PNMSD int, ANMSD int, PNMSE int, ANMSE int, Remarks text, UNIQUE(Date_on, Employee_ID))")
    conn.commit()
    conn.close()

def insert(Date_on_var, Employee_ID_var, Hours_in_VDI_var, PNASD_var, ANASD_var, PNASE_var, ANASE_var, NASM_var, PNMSD_var, ANMSD_var, PNMSE_var, ANMSE_var, Remarks_var):
    conn=sqlite3.connect("timesheet.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO work_productivity2 VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?)  ",(Date_on_var, Employee_ID_var, Hours_in_VDI_var, PNASD_var, ANASD_var, PNASE_var, ANASE_var, NASM_var, PNMSD_var, ANMSD_var, PNMSE_var, ANMSE_var, Remarks_var))
    #cur.execute("INSERT INTO work_productivity1 VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?)",(Date_on_var, Employee_ID_var, Hours_in_VDI_var, PNASD_var, ANASD_var, PNASE_var, ANASE_var, NASM_var, PNMSD_var, ANMSD_var, PNMSE_var, ANMSE_var, Remarks_var))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("timesheet.db")
    df = pd.read_sql_query("SELECT * FROM work_productivity2", conn)
    return df
