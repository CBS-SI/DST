import json
import pandas as pd


STAFF_URL = "https://www.cbs.dk/en/research/departments-and-centres/department-of-strategy-and-innovation/staff"
DST_JSON_PATH="/Users/pipegalera/Documents/dev/DST/Active User Access Tracking/src/dst_users.json"

def get_dst_users(json_path=DST_JSON_PATH):

    with open(json_path, 'r') as file:
        data = json.load(file)

    return data.get('mail')


def get_si_staff_table(url=STAFF_URL):
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

staff = get_si_staff_table()
dst_users = get_dst_users()


known = [email for email in dst_users if email in staff['mail'].values]
unknown = [email for email in dst_users if email not in staff['mail'].values]

print("Found emails:", known)
print("Not found emails:", unknown)
