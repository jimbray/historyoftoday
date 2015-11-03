#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: jimbray
@contact: jimbray16@gmail.com
@site:
@software: PyCharm
@file: getProvince.py
@time: 2015/10/23 16:58
"""

import requests
import json

class City:
    # def __init__(self, dict):
    #     self.__dict__ = dict

    def __init__(self, code, name):
        self.code = code
        self.name = name

    # def city2dict(self, city):
    #     return {
    #         'name':city.name,
    #         'code':city.code
    #     }

s = requests.session()

base_url = 'http://10.10.10.91/client/getProvincesCities?dom='

def object2dict(obj):
    d = {}
    d['__class__'] = obj.__class__.__name__
    d['__module__'] = obj.__module__
    d.update(obj.__dict__)
    return d

def dict2object(d):
    if '__class__' in d:
        class_name = d.pop('__class__')
        module_name = d.pop('__module__')
        module = __import__(module_name)
        class_ = getattr(module, class_name)
        args = dict((key.encode('ascii'), value) for key, value in d.items())
        inst = class_(**args)
    else:
        inst = d
    return inst

def get_city_by_code(code):
    data = {
         'login_type':'02',
        'province_code': code
    }
    res = s.get(base_url+str(data), headers={'content-type': 'application/json'})
    json_dict = json.loads(res.text.encode('utf-8'))

    citys = json_dict['provinces_cities_list']

    for city in citys:
        city['parent_code'] = code

    # print json.dumps(citys, ensure_ascii=False)
    return json.dumps(citys, ensure_ascii=False)


def get_all_province():
    data = {
        'login_type':'02',
        'province_code':''
    }

    res = s.get(base_url+str(data), headers={'content-type': 'application/json'})

    # print res.text

    province_dict =  json.loads(res.text.encode('utf-8'))

    province_list = province_dict['provinces_cities_list']

    all_list = []
    all_list.extend(province_list)

    for province in province_list:
        province['parent_code'] = '0'
        temp = get_city_by_code(province['code'].encode('utf-8'))
        jtemp = temp.encode('utf-8')
        jtemp_list = json.loads(jtemp)
        all_list.extend(jtemp_list)
        # all_list += get_city_by_code(province['code'].encode('utf-8'))
        # print get_city_by_code(province['code'].encode('utf-8'))
    print json.dumps(all_list, ensure_ascii=False)
    #print json.dumps(all_list, ensure_ascii=False)
    # encode_json_str = json.dumps(json_str, ensure_ascii=False)
    # print encode_json_str
    #
    # city = json.loads(encode_json_str, object_hook=dict2object)
    #
    # print type(city)

    # get_city_by_code(110)
    # get_city_by_code(120)
    # get_city_by_code(130)
    # get_city_by_code(140)
    # get_city_by_code(150)
    # get_city_by_code(210)
    # get_city_by_code(220)
    # get_city_by_code(230)
    # get_city_by_code(310)
    # get_city_by_code(320)
    # get_city_by_code(330)
    # get_city_by_code(340)
    # get_city_by_code(350)
    # get_city_by_code(360)
    # get_city_by_code(370)
    # get_city_by_code(410)
    # get_city_by_code(420)
    # get_city_by_code(430)
    # get_city_by_code(440)
    # get_city_by_code(450)
    # get_city_by_code(460)
    # get_city_by_code(500)
    # get_city_by_code(510)
    # get_city_by_code(520)
    # get_city_by_code(530)
    # get_city_by_code(540)
    # get_city_by_code(610)
    # get_city_by_code(620)
    # get_city_by_code(630)
    # get_city_by_code(640)
    # get_city_by_code(650)



if __name__ == '__main__':
    get_all_province()
