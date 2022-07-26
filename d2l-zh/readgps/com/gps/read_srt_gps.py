#!/usr/bin/python3
# -*- coding:utf-8 -*-
import os
# 读取srt文件中的字幕信息并写入txt中
i = 4 # 从0开始 4代表第五行
with open(r"D:\11d2LDemo\d2l-zh\readgps\srt\DJI_0036.SRT",'r',encoding='utf-8') as reader , open('SubtitleInfo.txt','w',encoding='utf-8') as writer:
    for index,line in enumerate(reader):
        if index == i:
            print(line)
            writer.write(line)
            i+=6 #每6行是一帧视频的字幕信息
reader.close()
writer.close()

fileName = 'SubtitleInfo.txt'
'''以下为一行数据的示例
[iso : 570] [shutter : 1/25.0] [fnum : 280] [ev : 0] [ct : 5899] [color_md : default] 
[focal_len : 240] [latitude: 0.000000] [longitude: 0.000000] [altitude: 0.000000] </font>
'''
latitude_value_float =0
longitude_value_float =0
altitude_value_float=0
with open(fileName) as file:
     content=file.readlines()
# 逐行读取数据
with open('GPSInfo.txt','w',encoding='utf-8') as writer:
    for line in content:
        line = line.rstrip()#去掉尾部空白
        line_split = line.split('] [') # [iso : 570       shutter : 1/25.0        fnum : 280  ...
        for line_split_content in line_split:
            name = line_split_content.split(':')[0].strip() # 取到所有的参数名称
            if name == 'latitude':
                latitude_value = line_split_content.split(':')[1].strip() # 分割取出latitude后的数值
                # print(latitude_value)
                latitude_value_float=float(latitude_value)
                writer.write(latitude_value)#写入的时候只能写入str 不能写入float
                writer.write(' ')
            if name == 'longitude':
                longitude_value = line_split_content.split(':')[1].strip()
                # print(longitude_value)
                longitude_value_float=float(longitude_value)
                writer.write(longitude_value)
                writer.write(' ')
            if name == 'altitude':
                altitude_value_bug=line_split_content.split('] </font>') #分割 altitude: 0.000000] </font>
                for altitude_value_bug_content in altitude_value_bug:
                    if altitude_value_bug_content != '':
                        altitude_value = altitude_value_bug_content.split(':')[1]
                # print(altitude_value)
                        altitude_value_float=float(altitude_value)
                        writer.write(altitude_value)
                        writer.write('\n')
print('done')











