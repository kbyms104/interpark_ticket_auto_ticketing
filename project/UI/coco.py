import string, time, random, requests
from PyQt5 import QtCore, QtGui, QtWidgets
from project.bs import TK
from apscheduler.schedulers import background as b
from apscheduler.triggers.combining import OrTrigger
from apscheduler.triggers import interval as i
from apscheduler.triggers import cron as c

class Ui_Dialog(object):
    global tk, sched

    def __init__(self, dialog):
        self.label_17 = QtWidgets.QLabel(dialog)
        self.label_16 = QtWidgets.QLabel(dialog)
        self.label_15 = QtWidgets.QLabel(dialog)
        self.label_14 = QtWidgets.QLabel(dialog)
        self.label_13 = QtWidgets.QLabel(dialog)
        self.label_12 = QtWidgets.QLabel(dialog)
        self.label_11 = QtWidgets.QLabel(dialog)
        self.label_10 = QtWidgets.QLabel(dialog)
        self.label_9 = QtWidgets.QLabel(dialog)
        self.label_4 = QtWidgets.QLabel(dialog)
        self.label_8 = QtWidgets.QLabel(dialog)
        self.label_7 = QtWidgets.QLabel(dialog)
        self.label_6 = QtWidgets.QLabel(dialog)
        self.label_5 = QtWidgets.QLabel(dialog)
        self.label_3 = QtWidgets.QLabel(dialog)
        self.label_2 = QtWidgets.QLabel(dialog)
        self.label = QtWidgets.QLabel(dialog)
        self.interparkStart_btn = QtWidgets.QPushButton(dialog)
        self.pushButton_2 = QtWidgets.QPushButton(dialog)
        self.goodsCode_txt = QtWidgets.QLineEdit(dialog)
        self.yyyy_txt = QtWidgets.QLineEdit(dialog)
        self.MM_txt = QtWidgets.QLineEdit(dialog)
        self.dd_txt = QtWidgets.QLineEdit(dialog)
        self.hh_txt = QtWidgets.QLineEdit(dialog)
        self.mm_txt = QtWidgets.QLineEdit(dialog)
        self.zone_txt = QtWidgets.QLineEdit(dialog)
        self.seat_txt = QtWidgets.QLineEdit(dialog)
        self.ticketCount_txt = QtWidgets.QLineEdit(dialog)
        self.re_hh_txt = QtWidgets.QLineEdit(dialog)
        self.re_mm_txt = QtWidgets.QLineEdit(dialog)
        self.pw_txt = QtWidgets.QLineEdit(dialog)
        self.id_txt = QtWidgets.QLineEdit(dialog)
        self.tikecting_btn1 = QtWidgets.QPushButton(dialog)
        self.tikecting_btn2 = QtWidgets.QPushButton(dialog)
        self.reservationStart_btn = QtWidgets.QPushButton(dialog)
        self.reservatoin_stop_btn = QtWidgets.QPushButton(dialog)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(362, 440)
        self.label.setGeometry(QtCore.QRect(11, 56, 71, 21))
        self.label.setObjectName("label")
        self.goodsCode_txt.setGeometry(QtCore.QRect(90, 50, 81, 31))
        self.goodsCode_txt.setText("")
        self.goodsCode_txt.setAlignment(QtCore.Qt.AlignCenter)
        self.goodsCode_txt.setObjectName("goodsCode_txt")
        self.yyyy_txt.setGeometry(QtCore.QRect(60, 100, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.yyyy_txt.setFont(font)
        self.yyyy_txt.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.yyyy_txt.setText("")
        self.yyyy_txt.setAlignment(QtCore.Qt.AlignCenter)
        self.yyyy_txt.setObjectName("yyyy_txt")
        self.MM_txt.setGeometry(QtCore.QRect(132, 100, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.MM_txt.setFont(font)
        self.MM_txt.setText("")
        self.MM_txt.setAlignment(QtCore.Qt.AlignCenter)
        self.MM_txt.setObjectName("MM_txt")
        self.dd_txt.setGeometry(QtCore.QRect(184, 100, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.dd_txt.setFont(font)
        self.dd_txt.setText("")
        self.dd_txt.setAlignment(QtCore.Qt.AlignCenter)
        self.dd_txt.setObjectName("dd_txt")
        self.hh_txt.setGeometry(QtCore.QRect(240, 100, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.hh_txt.setFont(font)
        self.hh_txt.setText("")
        self.hh_txt.setAlignment(QtCore.Qt.AlignCenter)
        self.hh_txt.setObjectName("hh_txt")
        self.mm_txt.setGeometry(QtCore.QRect(290, 100, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.mm_txt.setFont(font)
        self.mm_txt.setText("")
        self.mm_txt.setAlignment(QtCore.Qt.AlignCenter)
        self.mm_txt.setObjectName("mm_txt")
        self.label_2.setGeometry(QtCore.QRect(11, 105, 41, 21))
        self.label_2.setObjectName("label_2")
        self.label_3.setGeometry(QtCore.QRect(114, 106, 16, 20))
        self.label_3.setObjectName("label_3")
        self.label_5.setGeometry(QtCore.QRect(168, 110, 16, 16))
        self.label_5.setObjectName("label_5")
        self.label_6.setGeometry(QtCore.QRect(222, 110, 16, 16))
        self.label_6.setObjectName("label_6")
        self.label_7.setGeometry(QtCore.QRect(274, 108, 16, 16))
        self.label_7.setObjectName("label_7")
        self.label_8.setGeometry(QtCore.QRect(330, 110, 16, 16))
        self.label_8.setObjectName("label_8")
        self.zone_txt.setGeometry(QtCore.QRect(60, 150, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.zone_txt.setFont(font)
        self.zone_txt.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.zone_txt.setText("")
        self.zone_txt.setAlignment(QtCore.Qt.AlignCenter)
        self.zone_txt.setObjectName("zone_txt")
        self.seat_txt.setGeometry(QtCore.QRect(150, 150, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.seat_txt.setFont(font)
        self.seat_txt.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.seat_txt.setText("")
        self.seat_txt.setAlignment(QtCore.Qt.AlignCenter)
        self.seat_txt.setObjectName("seat_txt")
        self.label_4.setGeometry(QtCore.QRect(117, 156, 31, 20))
        self.label_4.setObjectName("label_4")
        self.label_9.setGeometry(QtCore.QRect(210, 155, 21, 21))
        self.label_9.setObjectName("label_9")
        self.label_10.setGeometry(QtCore.QRect(14, 154, 41, 21))
        self.label_10.setObjectName("label_10")
        self.label_11.setGeometry(QtCore.QRect(6, 200, 56, 12))
        self.label_11.setObjectName("label_11")
        self.ticketCount_txt.setGeometry(QtCore.QRect(60, 190, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ticketCount_txt.setFont(font)
        self.ticketCount_txt.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ticketCount_txt.setText("")
        self.ticketCount_txt.setAlignment(QtCore.Qt.AlignCenter)
        self.ticketCount_txt.setObjectName("ticketCount_txt")
        self.label_12.setGeometry(QtCore.QRect(150, 250, 16, 16))
        self.label_12.setObjectName("label_12")
        self.label_13.setGeometry(QtCore.QRect(94, 248, 16, 16))
        self.label_13.setObjectName("label_13")
        self.re_hh_txt.setGeometry(QtCore.QRect(60, 240, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.re_hh_txt.setFont(font)
        self.re_hh_txt.setText("")
        self.re_hh_txt.setAlignment(QtCore.Qt.AlignCenter)
        self.re_hh_txt.setObjectName("re_hh_txt")
        self.re_mm_txt.setGeometry(QtCore.QRect(110, 240, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.re_mm_txt.setFont(font)
        self.re_mm_txt.setText("")
        self.re_mm_txt.setAlignment(QtCore.Qt.AlignCenter)
        self.re_mm_txt.setObjectName("re_mm_txt")
        self.label_14.setGeometry(QtCore.QRect(6, 230, 51, 51))
        self.label_14.setObjectName("label_14")
        self.interparkStart_btn.setGeometry(QtCore.QRect(20, 10, 81, 31))
        self.interparkStart_btn.setObjectName("interparkStart_btn")
        self.pushButton_2.setGeometry(QtCore.QRect(120, 10, 91, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tikecting_btn1.setGeometry(QtCore.QRect(20, 290, 75, 23))
        self.tikecting_btn1.setObjectName("tikecting_btn1")
        self.tikecting_btn2.setGeometry(QtCore.QRect(105, 290, 75, 23))
        self.tikecting_btn2.setObjectName("tikecting_btn2")
        self.reservationStart_btn.setGeometry(QtCore.QRect(200, 290, 75, 23))
        self.reservationStart_btn.setObjectName("reservationStart_btn")
        self.reservatoin_stop_btn.setGeometry(QtCore.QRect(280, 290, 75, 23))
        self.reservatoin_stop_btn.setObjectName("reservatoin_stop_btn")
        self.label_15.setGeometry(QtCore.QRect(10, 350, 411, 51))
        self.label_15.setObjectName("label_15")
        self.label_16.setGeometry(QtCore.QRect(200, 200, 21, 21))
        self.label_16.setObjectName("label_16")
        self.label_17.setGeometry(QtCore.QRect(200, 230, 21, 16))
        self.label_17.setObjectName("label_17")
        self.id_txt.setGeometry(QtCore.QRect(230, 200, 113, 20))
        self.id_txt.setObjectName("id_txt")
        self.pw_txt.setGeometry(QtCore.QRect(230, 230, 113, 20))
        self.pw_txt.setObjectName("pw_txt")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "음음"))
        self.label.setText(_translate("Dialog", "GoodsCode"))
        self.label_2.setText(_translate("Dialog", "예매일"))
        self.label_3.setText(_translate("Dialog", "년"))
        self.label_5.setText(_translate("Dialog", "월"))
        self.label_6.setText(_translate("Dialog", "일"))
        self.label_7.setText(_translate("Dialog", "시"))
        self.label_8.setText(_translate("Dialog", "분"))
        self.label_4.setText(_translate("Dialog", "구역"))
        self.label_9.setText(_translate("Dialog", "석"))
        self.label_10.setText(_translate("Dialog", "좌 석"))
        self.label_11.setText(_translate("Dialog", "티켓갯수"))
        self.label_12.setText(_translate("Dialog", "분"))
        self.label_13.setText(_translate("Dialog", "시"))
        self.label_14.setText(_translate("Dialog", "예약시간"))
        self.interparkStart_btn.setText(_translate("Dialog", "인터파크티켓"))
        self.interparkStart_btn.clicked.connect(self.open_nterpark)
        self.pushButton_2.setText(_translate("Dialog", "???????"))
        self.tikecting_btn1.setText(_translate("Dialog", "티케팅1"))
        self.tikecting_btn1.clicked.connect(self.start_Ticketing)
        self.tikecting_btn2.setText(_translate("Dialog", "티케팅2"))
        self.tikecting_btn2.clicked.connect(self.start_Ticketing_no)
        self.reservationStart_btn.setText(_translate("Dialog", "예약시작"))
        self.reservationStart_btn.clicked.connect(self.start_e_Ticketing)
        self.reservatoin_stop_btn.setText(_translate("Dialog", "예약중단"))
        self.reservatoin_stop_btn.clicked.connect(self.stop_e_Ticketing)
        self.label_15.setText(_translate("Dialog", ""))
        self.label_16.setText(_translate("Dialog", "ID"))
        self.label_17.setText(_translate("Dialog", "PW"))

    def open_nterpark(self):
        global tk
        try:
            tk = TK.TK()
            tk.open_window()
            tk.login(self.id_txt.text(), self.pw_txt.text())

        except Exception as e:  # 모든 예외의 에러 메시지를 출력할 때는 Exception을 사용
            print('예외가 발생했습니다.', e)

    def start_Ticketing(self):
        global tk
        try:
            tk.location_page2(self.goodsCode_txt.text())
            tk.location_page(self.goodsCode_txt.text(), self.yyyy_txt.text(), self.MM_txt.text(),
                             self.dd_txt.text(), self.hh_txt.text(), self.mm_txt.text(),
                             self.zone_txt.text(), self.seat_txt.text(), self.ticketCount_txt.text())

        except Exception as e:  # 모든 예외의 에러 메시지를 출력할 때는 Exception을 사용
            print('예외가 발생했습니다.', e)

    def start_Ticketing_no(self):
        global tk
        try:
            tk.location_page(self.goodsCode_txt.text(), self.yyyy_txt.text(), self.MM_txt.text(),
                             self.dd_txt.text(), self.hh_txt.text(), self.mm_txt.text(),
                             self.zone_txt.text(), self.seat_txt.text(), self.ticketCount_txt.text())

        except Exception as e:  # 모든 예외의 에러 메시지를 출력할 때는 Exception을 사용
            print('예외가 발생했습니다.', e)

    def start_Ticketing2(self):
        global while_check
        try:
            print("움직였다")
            while_check = True
            while while_check:
                random_string = "".join([random.choice(string.ascii_letters) for _ in range(10)])
                res = requests.get('https://ticket.interpark.com/' + random_string + 'asp')
                headers = res.headers.get('Date').split(' ')
                hmd = headers[4].split(':')
                h = int(hmd[0]) + 9
                if h > 24:
                    h = h - 24
                #print(str(h) + " " + self.re_hh_txt.text() + " " + hmd[1] + " " + self.re_mm_txt.text())
                if str(h) == self.re_hh_txt.text() and hmd[1] == self.re_mm_txt.text():
                    while_check = False
                    self.start_Ticketing()
                time.sleep(0.5)

        except Exception as e:  # 모든 예외의 에러 메시지를 출력할 때는 Exception을 사용
            print('예외가 발생했습니다.', e)
        finally:
            res.close()

    def start_e_Ticketing(self):
        global sched
        try:
            print("예약 시작")
            sched = b.BackgroundScheduler()
            trigger = OrTrigger([
                c.CronTrigger(hour=self.re_hh_txt.text(), minute=self.re_mm_txt.text())
                #i.IntervalTrigger(seconds=0.5)
            ])

            sched.add_job(self.start_Ticketing2, trigger)
            sched.start()
        except Exception as e:
            print('예외 맨', e)

    def stop_e_Ticketing(self):
        global while_check
        try:
            sched.shutdown()
            while_check = False
            print("예약중단")
        except Exception as e:
            print('예외 맨2', e)
