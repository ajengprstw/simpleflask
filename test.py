import requests, schedule

def indo():
    api_url="https://api.kawalcorona.com/indonesia/"
    rstl = requests.get(api_url).json()
    print(rstl)

def jkt():
    api_url="https://api.kawalcorona.com/indonesia/provinsi/"
    rstl = requests.get(api_url).json()
    cek=rstl[0]
    ambil_dic=cek["attributes"]
    a=[ambil_dic]
    print(a)

r_indo=schedule.every(2).seconds.do(indo)
r_jkt=schedule.every(2).seconds.do(jkt)


data_indo=indo()
data_jkt=jkt()