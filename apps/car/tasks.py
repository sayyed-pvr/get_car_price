from celery import shared_task
import requests
from bs4 import BeautifulSoup


# ----------------------------------------------------------------

@shared_task
def get_care_price():
    try:
        res = requests.get("https://www.iranjib.ir/showgroup/45/%D9%82%DB%8C%D9%85%D8%AA-%D8%AE%D9%88%D8%AF%D8%B1%D9%88-%D8%AA%D9%88%D9%84%DB%8C%D8%AF-%D8%AF%D8%A7%D8%AE%D9%84/")
        soup = BeautifulSoup(res.content, "html.parser")
        care_p = soup.select('tr:not([class])')[1:-1]
        f1 = open('file1.txt', 'w', encoding='utf-8')
        for tr in care_p:
            t1 = tr.select('td')[0].text.strip()
            t2 = tr.select('td')[1].text.strip()
            t3 = tr.select('td')[2].text.strip()
            f1.write(f'{t1}*{t2}*{t3}\n')
        f1.close()
        print('f1 closed...')
    except:
        print('Connection Error..............')






# ----------------------------------------------------------------




