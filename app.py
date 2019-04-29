# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 12:56:10 2019

@author: elnura.arslan
"""

import numpy as np
import imutils
import cv2
import dlib
from flask import Flask
from flask import render_template
from flask import request, jsonify
import math
from imutils import face_utils
import logging
import json
from datetime import datetime
from enum import Enum

from logging.handlers import RotatingFileHandler

log_formatter = logging.Formatter('%(asctime)s %(levelname)s %(funcName)s(%(lineno)d) %(message)s')
my_handler = RotatingFileHandler('Facial_Landmarks_Logger.txt', mode='a', maxBytes=5 * 1024 * 1024,
                                 backupCount=2, encoding=None, delay=0)
my_handler.setFormatter(log_formatter)
my_handler.setLevel(logging.INFO)
app_log = logging.getLogger('root')
if not app_log.handlers:
    app_log.setLevel(logging.INFO)
    app_log.addHandler(my_handler)

app = Flask(__name__)
import base64
import os

# get fake parameters - image_base64, birth_date, gender = None, relation = False

birth_date_str = '2020-06-29 08:15:27.243860'
birth_date_time = datetime.strptime(birth_date_str, '%Y-%m-%d %H:%M:%S.%f')
gender = None
relation = False

birth_date_time = datetime(2020, 8, 2)  # year month day

with open('know_me_personality.json') as json_file:
    know_me_personality = json.load(json_file)

with open('know_me_zodiac.json') as json_file:
    know_me_zodiac = json.load(json_file)


@app.route('/')
def index():
    return "Successful."


face_landmarks_dat = "shape_predictor_68_face_landmarks.dat"  # C:/Users/elnura.arslan/.spyder-py3/face-landmarks/

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(face_landmarks_dat)


class Faces:
    def __init__(self, rects):
        self.rects = rects
        self.faces = []

    def assignFaceDistances(self, gray):
        for (i, rect) in enumerate(self.rects):
            face = Face()
            face.assignFaceDistance(gray, rect)
            self.faces.append(face)

        return self.faces


Cene = Enum('Cene', 'kare kisavedar yuvarlakcene uzun')
Kas = Enum('Kas', 'dogalduz yuksekkenar duzyukari kisa sivri')
KasKas = Enum('KasKas', 'buyukbosluk kucukbosluk normalbosluk')
Goz = Enum('Goz', 'kucuk genis badem yuvarlakgoz')
GozGoz = Enum('GozGoz', 'yakin uzak normal')
Dudak = Enum('Dudak',
             'buyukkabarik kucukkabarik ustkalinaltince ustincealtkalin ustsivri ustyuvarlak ustduz ince siradan')
Burun = Enum('Burun', 'genisburun sivriburun buyukburun kucukburun')

temp_image_file = 'test2.jpg'


class HumanDetectionJsonObject(object):
    def __init__(self, j):
        self.data = json.loads(j)


class Face:
    def __init__(self):
        self.distanceParameterHorizontal = 0
        self.distanceParameterVertical = 0

    def assignFaceDistance(self, gray, rect):
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)
        self.makeRelations(shape)

    def makeRelations(self, rect):
        self.relationFromCene(rect)
        self.relationFromGoz(rect)
        self.relationFromKas(rect)
        self.relationFromBurun(rect)
        self.relationFromDudak(rect)

    def relationFromCene(self, rect):
        ceneAltKasUstUzunluk = rect[8][1] - rect[19][1]  # rect[8][1] - rect[24][1]
        ceneAltCeneUstUzunluk = rect[8][1] - rect[0][1]  # rect[8][1] - rect[16][1]
        ceneUstSolSagFark = rect[16][0] - rect[0][0]
        ceneOrtaSolSagFark = rect[12][0] - rect[4][0]

        if ceneOrtaSolSagFark / ceneUstSolSagFark >= 0.8:
            self.cene = Cene.kare.name
        elif ceneOrtaSolSagFark / ceneUstSolSagFark <= 0.6:
            self.cene = Cene.yuvarlakcene.name
        elif ceneAltCeneUstUzunluk / ceneAltKasUstUzunluk > 0.7:
            self.cene = Cene.uzun.name
        else:
            self.cene = Cene.kisavedar.name

    def relationFromGoz(self, rect):
        sagSolGozUzaklik = rect[42][0] - rect[39][0]
        ceneUstSolSagFark = rect[16][0] - rect[0][0]

        if sagSolGozUzaklik / ceneUstSolSagFark >= 0.7:
            self.gozgoz = GozGoz.uzak.name
        elif sagSolGozUzaklik / ceneUstSolSagFark <= 0.3:
            self.gozgoz = GozGoz.yakin.name
        else:
            self.gozgoz = GozGoz.normal.name

        solGozGenislik = rect[39][0] - rect[36][0]
        solGozYukseklik = rect[41][1] - rect[37][1]

        if solGozYukseklik / solGozYukseklik >= 0.5:
            self.goz = Goz.yuvarlakgoz.name
        elif solGozYukseklik / solGozYukseklik < 0.3:
            self.goz = Goz.badem.name
        elif solGozGenislik / ceneUstSolSagFark >= 0.4:
            self.goz = Goz.buyuk.name
        else:
            self.goz = Goz.kucuk.name

    def relationFromKas(self, rect):
        ceneUstSolSagFark = rect[16][0] - rect[0][0]
        solKasGenislik = rect[21][0] - rect[17][0]
        solKasYukseklik = rect[17][1] - rect[19][1]
        kasArasiBosluk = rect[22][0] - rect[21][0]
        myradians = math.atan2(rect[17][1] - rect[18][1], rect[17][0] - rect[18][0])
        mydegrees = 180 - math.degrees(myradians)

        if kasArasiBosluk / ceneUstSolSagFark >= 0.4:
            self.kaskas = KasKas.buyukbosluk.name
        elif kasArasiBosluk / ceneUstSolSagFark < 0.2:
            self.kaskas = KasKas.kucukbosluk.name
        else:
            self.kaskas = KasKas.normalbosluk.name

        if rect[17][1] < rect[21][1]:
            self.kas = Kas.duzyukari.name
        elif solKasGenislik / ceneUstSolSagFark <= 0.2:
            self.kas = Kas.kisa.name
        elif mydegrees <= 45:
            self.kas = Kas.sivri.name
        elif mydegrees > 45:
            self.kas = Kas.yuksekkenar.name
        else:
            self.kas = Kas.duz.name

    def relationFromBurun(self, rect):
        ceneAltKasUstUzunluk = rect[8][1] - rect[19][1]  # rect[8][1] - rect[24][1]
        ceneUstSolSagFark = rect[16][0] - rect[0][0]
        burunUzunluk = rect[30][1] - rect[27][1]
        burunGenislik = rect[35][0] - rect[31][0]

        if burunUzunluk / ceneAltKasUstUzunluk >= 0.7 and burunGenislik / ceneUstSolSagFark >= 0.3:
            self.burun = Burun.buyukburun.name
        elif burunUzunluk / ceneAltKasUstUzunluk >= 0.7 and burunGenislik / ceneUstSolSagFark < 0.3:
            self.burun = Burun.sivriburun.name
        elif burunGenislik / ceneUstSolSagFark >= 0.3:
            self.burun = Burun.genisburun.name
        else:
            self.burun = Burun.kucukburun.name

    def relationFromDudak(self, rect):
        disDudakGenislik = rect[54][0] - rect[48][0]
        disDudakYukseklik = rect[57][1] - rect[51][1]
        ustDudakYukseklik = rect[61][1] - rect[50][1]
        altDudakYukseklik = rect[57][1] - rect[66][1]

        ceneAltKasUstUzunluk = rect[8][1] - rect[19][1]
        ceneUstSolSagFark = rect[16][0] - rect[0][0]

        myradians = math.atan2(rect[51][1] - rect[50][1], rect[51][0] - rect[50][0])
        mydegrees = math.degrees(myradians)

        if disDudakGenislik / ceneUstSolSagFark >= 0.4 and disDudakYukseklik / ceneAltKasUstUzunluk >= 0.1:
            self.dudak = Dudak.buyukkabarik.name
        elif disDudakYukseklik / ceneAltKasUstUzunluk >= 0.1:
            self.dudak = Dudak.kucukkabarik.name
        elif ustDudakYukseklik / altDudakYukseklik >= 1.2:
            self.dudak = Dudak.ustkalinaltince.name
        elif altDudakYukseklik / ustDudakYukseklik >= 1.2:
            self.dudak = Dudak.ustincealtkalin.name
        elif ustDudakYukseklik / ceneAltKasUstUzunluk <= 0.1:
            self.dudak = Dudak.ince.name
        elif mydegrees <= 15 and mydegrees > 0:
            self.dudak = Dudak.ustduz.name
        elif mydegrees <= 45 and mydegrees > 15:
            self.dudak = Dudak.ustsivri.name
        elif mydegrees > 45:
            self.dudak = Dudak.ustduz.name
        else:
            self.dudak = Dudak.siradan.name


def assign_zodiac_relations(birth_date):
    zod_comment = ''
    for i in range(len(know_me_zodiac)):
        zod = know_me_zodiac[i]
        date_time_start = datetime(birth_date.year, zod['start_month'], zod['start_day'])
        date_time_finish = datetime(birth_date.year, zod['finish_month'], zod['finish_day'])
        if birth_date >= date_time_start and birth_date <= date_time_finish:
            zod_comment = zod['comment']
            break

    return zod_comment


def assign_face_relations(faces):
    faces_relations_result = []
    for i in range(len(faces)):
        face_str = ''
        face = faces[i]

        face_str += know_me_personality[face.cene]
        face_str += know_me_personality[face.kas]
        face_str += know_me_personality[face.kaskas]
        face_str += know_me_personality[face.goz]
        face_str += know_me_personality[face.gozgoz]
        face_str += know_me_personality[face.burun]
        face_str += know_me_personality[face.dudak]

        faces_relations_result.append(face_str)

    return faces_relations_result


def assign_relations(faces, birth_date):
    faces_relations_result = assign_face_relations(faces)
    zodiac_relations_result = assign_zodiac_relations(birth_date)
    relations_result = {'zodiac': zodiac_relations_result, 'face': faces_relations_result}

    return relations_result


import io
from PIL import Image


def encode_image(image):
    image_buffer = io.BytesIO()
    image.save(image_buffer, format='PNG')
    # imgstr = 'data:image/png;base64,{}'.format(base64.b64encode(image_buffer.getvalue()))
    imgstr = '{}'.format(base64.b64encode(image_buffer.getvalue()))
    encoded_image = imgstr.replace("b'", "").replace("'", "")

    return encoded_image


@app.route('/getfaciallandmarks', methods=['GET', 'POST'])
def getfaciallandmarks():
    try:
        data = HumanDetectionJsonObject(request.args.get('JsonObject'))
        username = data.data.get('username')
        password = data.data.get('password')
        image_base64_ = data.data.get('image_base64')
        birth_day_ = data.data.get('birth_day')
        birth_month_ = data.data.get('birth_month')
        birth_year_ = data.data.get('birth_year')
        gender_ = data.data.get('gender')
        relation_ = data.data.get('relation')

        '''
        image_base64_ = request.args.get('image_base64')
        birth_day_ = request.args.get('birth_day')
        birth_month_ = request.args.get('birth_month')
        birth_year_ = request.args.get('birth_year')
        gender_ = request.args.get('gender')
        relation_ = request.args.get('relation')
        '''

        if username == 'moonai' and password == 'admn@1!':
            with open('image_base64.txt', 'r') as file:
                image_base64__ = file.read()
                # image_base64__.replace(" ", "")

            if image_base64_ != None and image_base64_ != '' and birth_day_ != None and birth_month_ != None and birth_year_ != None:
                try:
                    image_byte_ = base64.b64decode(image_base64__)
                    with open(temp_image_file, 'wb') as f_output:
                        f_output.write(image_byte_)

                    image = cv2.imread(temp_image_file)
                    os.remove(temp_image_file)
                    image = imutils.resize(image, width=500)
                    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                    rects = detector(gray, 1)
                    faces = Faces(rects)
                    faces_result = faces.assignFaceDistances(gray)
                    relations_result = assign_relations(faces_result, birth_date_time)

                    result = json.dumps(relations_result, ensure_ascii=False)
                except Exception as e:
                    app_log.info("Detection Error : {}", e)
                    result = {'face': '', 'zodiac': ''}
            else:
                app_log.info("Paramater Value Error")
                result = {'face': '', 'zodiac': ''}
        else:
            app_log.info("Authentication Error")
            result = {'face': '', 'zodiac': ''}
    except Exception as e:
        app_log.info(" Paramater Error : {}".format(e))
        result = {'face': '', 'zodiac': ''}

    return jsonify(result)


'''

image = Image.open(open('test.jpg', 'rb'))
      encoded_image = encode_image(image)
      image_read = image.read()
      image_64_encode = base64.encodebytes(image_read)

      decoded = base64.b64decode(image_64_encode)

      with open(temp_image_file, 'wb') as f_output:
          f_output.write(decoded)


jpg_original = base64.b64decode(image_base64)

try:
    with open(temp_image_file, 'wb') as f_output:
        f_output.write(jpg_original)

    image = cv2.imread(temp_image_file)
    os.remove(temp_image_file)
    image = imutils.resize(image, width=500)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    rects = detector(gray, 1)
    faces = Faces(rects)
    faces_result = faces.assignFaceDistances(gray)
    relations_result = assign_relations(faces_result, birth_date_time)

    json_result = json.dumps(relations_result, ensure_ascii=False)

except Exception as e:
    app_log.log("Hata : ", e)
'''
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)


# image = draw_image_landmarks(image, rects)

# cv2.imshow("Output1", image)

# cv2.waitKey(0)


def draw_image_landmarks(image, rects, gray):
    for (i, rect) in enumerate(rects):
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)
        (x, y, w, h) = face_utils.rect_to_bb(rect)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(image, "Face #{}".format(i + 1), (x - 10, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        for (x, y) in shape:
            cv2.circle(image, (x, y), 1, (0, 0, 255), -1)

    return image



