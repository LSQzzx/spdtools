import requests
import json
import re
import os
import sys
import webbrowser
import spd
import time

osxt = sys.platform
if 'win' in osxt:
    os.system("cls")
if 'linux' in osxt:
    os.system("clear")

print('               _ _              _     ')
print(' ___ _ __   __| | |_ ___   ___ | |___ ')
print('/ __| \'_ \\ / _` | __/ _ \ / _ \\| / __|')
print('\\__ \\ |_) | (_| | || (_) | (_) | \\__ \\')
print('|___/ .__/ \__,_|\__\___/ \___/|_|___/')
print('    |_|                               ')

print('[1] ip经纬度定位')
print('[2] 经纬度地图定位')
print('[3] 查看本机公网ip')
print('[4] 端口用途查询（第一次使用请先输入0）')
print('[spider]彩蛋')
print('[exit] 退出')
print()
while True:
    choice = input('spdtools > ')
    if choice == '1':
        ip = input('请输入ip地址：')
        url = 'https://restapi.amap.com/v3/ip?key=3e105e2105fafafb3c52d7fcf75ed5cf&ip=' + ip
        res = requests.get(url)
        json_data = json.loads(res.text)
        print('-----------------------------------------------')
        print('经纬度：',json_data["rectangle"])

        url2 = 'https://restapi.amap.com/v3/geocode/regeo?key=3e105e2105fafafb3c52d7fcf75ed5cf&location=' + json_data["rectangle"]
        res2 = requests.get(url2)
        json_data2 = json.loads(res2.text)
        title = str(json_data2)
        pattern = re.compile(r'[\u4e00-\u9fa5]+')
        result = pattern.findall(title)
        print()
        print("经纬度转地址：",result)
        print('-----------------------------------------------')
    elif choice == '2':
        result2 = input('请输入经纬度(只输入分号左边部分)：')
        url4 = 'https://restapi.amap.com/v3/staticmap?location=' + result2 + '&zoom=10&size=1200*550&markers=mid,,A:' + result2 + '&key=3e105e2105fafafb3c52d7fcf75ed5cf'
        webbrowser.open(url4, new=0, autoraise=True)
    elif choice == '3':
        url3 = 'http://ifconfig.co/json'
        res3 = requests.get(url3)
        json_data3 = json.loads(res3.text)
        print('-----------------------------------------------')
        print('本机公网ip：',json_data3["ip"])
    elif choice == '4':
        port = input('请输入端口：')
        dkcx = "whatportis " + port
        os.system(dkcx)
    elif choice == '0':
        os.system("pip install whatportis")
    elif choice == 'spider':
        os.system("mode con cols=120 lines=40")
        time.sleep(1)
        os.system("python spd.py")
        spd.spider()
    elif choice == 'exit':
        break
