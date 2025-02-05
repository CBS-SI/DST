import pandas as  pd

URL = "https://www.cbs.dk/en/research/departments-and-centres/department-of-strategy-and-innovation/staff"


def get_cbs_staff_table(url=URL):
    try:
        tables = pd.read_html(url)
        table_1 = pd.DataFrame({
                        'First name': tables[0][1],
                        'Last name': tables[0][2],
                        'mail': tables[0][5]
                    })

        table_2 = tables[1][["First name", "Last name", "mail"]]

        return pd.concat([table_1,table_2])

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

if __name__=="__main__":
    get_cbs_staff_table()
