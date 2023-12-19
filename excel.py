import pandas as pd

def export(week_dict, week_breakdown, week_total):
    df_split = pd.DataFrame(week_dict)
    df_breakdown = pd.DataFrame(week_breakdown)
    df_total = pd.DataFrame(week_total, index=["Total"]).transpose()
    with pd.ExcelWriter("output.xlsx", engine="openpyxl") as writer:
        df_split.to_excel(writer, sheet_name="Sheet_1", startcol=1, index=False)
        df_breakdown.to_excel(writer, sheet_name="Sheet_1", startrow=10, startcol= 0)
        df_total.to_excel(writer,sheet_name = "Sheet_1", startrow = 10, startcol=7, index=True)