import requests
from bs4 import BeautifulSoup
def write(a):
    file='text.txt'
    with open(file,'a') as f:
        f.write(a)
def getAllLinks():
    links=[];
    req = requests.get("http://www.yunxs.com/longzu5/").text
    bf = BeautifulSoup(req, "html.parser")
    for i in str(bf.find(class_="Con jj_pl")).split("\n"):
        if(str(i).__contains__("href")):
            i=str(i)
            links.append((i[i.find("\"")+1:i.rfind("\"")]))
    return links
def getText(a):
    result=""
    link="http://www.yunxs.com/longzu5/"+a
    req = requests.get(link).text
    bf = BeautifulSoup(req, "html.parser")
    text=str(bf.find(class_="box_box")).split("\n")[4]
    for i in text.replace("<br/><br/>",'\n').split("\n"):
        if(i.__contains__("div")):
            continue
        result+=i.strip()+"\n"
    return result.replace('***','')

def getTitle(a):
    link = "http://www.yunxs.com/longzu5/" + a
    req = requests.get(link).text
    bf = BeautifulSoup(req, "html.parser")
    return str(bf.find(class_="Con box_con").text).split("\n")[1]

if __name__ == '__main__':
    for i in getAllLinks():
        a=getTitle(i)
        write(a+"\n")
        write(getText(i))
        write("\n\n")
        print(a+" finished")

