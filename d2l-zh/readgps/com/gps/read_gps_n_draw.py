
import exifread
import re
import json
import requests
import os
from scipy.io import loadmat  #导入 loadmat, 用于对 mat 格式文件进行操作
import numpy as np
import matplotlib.pyplot as plt  #导入绘图操作用到的库

def latitude_and_longitude_convert_to_decimal_system(*arg):
    """
    经纬度转为小数, param arg:
    :return: 十进制小数
    """
    return float(arg[0]) + ((float(arg[1]) + (float(arg[2].split('/')[0]) / float(arg[2].split('/')[-1]) / 60)) / 60)

def find_GPS_image(pic_path):
    GPS = {}
    date = ''
    with open(pic_path, 'rb') as f:
        tags = exifread.process_file(f)
        for tag, value in tags.items():
            if re.match('GPS GPSLatitudeRef', tag):
                GPS['GPSLatitudeRef'] = str(value)
            elif re.match('GPS GPSLongitudeRef', tag):
                GPS['GPSLongitudeRef'] = str(value)
            elif re.match('GPS GPSAltitudeRef', tag):
                GPS['GPSAltitudeRef'] = str(value)
            elif re.match('GPS GPSLatitude', tag):
                try:
                    match_result = re.match('\[(\w*),(\w*),(\w.*)/(\w.*)\]', str(value)).groups()
                    GPS['GPSLatitude'] = int(match_result[0]), int(match_result[1]), int(match_result[2])
                except:
                    deg, min, sec = [x.replace(' ', '') for x in str(value)[1:-1].split(',')]
                    GPS['GPSLatitude'] = latitude_and_longitude_convert_to_decimal_system(deg, min, sec)
            elif re.match('GPS GPSLongitude', tag):
                try:
                    match_result = re.match('\[(\w*),(\w*),(\w.*)/(\w.*)\]', str(value)).groups()
                    GPS['GPSLongitude'] = int(match_result[0]), int(match_result[1]), int(match_result[2])
                except:
                    deg, min, sec = [x.replace(' ', '') for x in str(value)[1:-1].split(',')]
                    GPS['GPSLongitude'] = latitude_and_longitude_convert_to_decimal_system(deg, min, sec)
            elif re.match('GPS GPSAltitude', tag):
                GPS['GPSAltitude'] = str(value)
            elif re.match('.*Date.*', tag):
                date = str(value)
    return {'GPS_information': GPS, 'date_information': date}

def find_address_from_GPS(GPS):
    """
    使用Geocoding API把经纬度坐标转换为结构化地址。
    :param GPS:
    :return:
    """
    secret_key = 'zbLsuDDL4CS2U0M4KezOZZbGUY9iWtVf'
    if not GPS['GPS_information']:
        return '该照片无GPS信息'
    lat, lng = GPS['GPS_information']['GPSLatitude'], GPS['GPS_information']['GPSLongitude']
    baidu_map_api = "http://api.map.baidu.com/geocoder/v2/?ak={0}&callback=renderReverse&location={1},{2}s&output=json&pois=0".format(
        secret_key, lat, lng)
    response = requests.get(baidu_map_api)
    content = response.text.replace("renderReverse&&renderReverse(", "")[:-1]
    baidu_map_address = json.loads(content)
    formatted_address = baidu_map_address["result"]["formatted_address"]
    province = baidu_map_address["result"]["addressComponent"]["province"]
    city = baidu_map_address["result"]["addressComponent"]["city"]
    district = baidu_map_address["result"]["addressComponent"]["district"]
    return formatted_address,province,city,district

path = r"D:\11d2LDemo\d2l-zh\readgps\pic"  # 待读取的文件夹
path_list = os.listdir(path)
path_list.sort()  # 对读取的路径进行排序

dict_y = {}
N = []  # N
E = []  # E
for filename in path_list:
    file_path = os.path.join(path, filename)
    # print(file_path)
    pic_path = file_path

    GPS_info = find_GPS_image(pic_path)
    address = find_address_from_GPS(GPS=GPS_info)
    #print(GPS_info)
    #print(address)

    x = list(GPS_info.values())
    #print(x)
    time = x[1]
    gps_dict_formate = x[0]
    y = list(gps_dict_formate.values())
    information = '拍照时间：'+time+'，拍照地点：'+str(address[0])+'（经度:'+str(y[2])+' '+str(y[3])+'，纬度：'+str(y[0])+' '+str(y[1])+'，高度：'+str(y[5])+'米）'


    for i in range(len(y)):
        if i == 1:
            N.append(y[i])
        elif i == 3:
            # 奇数位置作值
            E.append(y[i])
        else:
            a=2
    # 用zip将两个列表中对应的元素打包成一个个元组，后转为字典

    #
    # print(pic_path)
    # print(information)
# dict_y=dict(zip(key_y_N_E, value_y_N_E))
plt.subplot(221)
# plt.xlim(xmax=4,xmin=0)
# plt.ylim(ymax=4,ymin=0)
plt.xlabel("E")
plt.ylabel("N")
print(N)
print(E)
plt.plot(N,E,'ro')

plt.show()






