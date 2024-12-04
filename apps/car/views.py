from django.shortcuts import render
from bs4 import BeautifulSoup
import requests



def current_date():
    try:
        res = requests.get("https://www.iranjib.ir/showgroup/45/%D9%82%DB%8C%D9%85%D8%AA-%D8%AE%D9%88%D8%AF%D8%B1%D9%88-%D8%AA%D9%88%D9%84%DB%8C%D8%AF-%D8%AF%D8%A7%D8%AE%D9%84/")
        soup = BeautifulSoup(res.content, "html.parser")
        current_date = soup.select('div.custom > span.group-refreshdate-wrapper')[0].text.strip()
        print(current_date)
        return current_date
    except:
        return False

def prices(request):
    try:
        file1=open('file1.txt', "r", encoding='utf-8')
        lines_for_template=[]
        for line in file1:
            parts = line.strip().split('*')
            lines_for_template.append(parts)
            
        if current_date():
            current = current_date()
        else:
            current = '  در دسترس نیست'
        file1.close()
        
        return render(request,'car_app/prices.html',{'lines_for_template' : lines_for_template, 'current' : current})
    except:
        prices('The file is not available')

