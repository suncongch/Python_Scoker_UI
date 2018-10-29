#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *
import socket
import sys
import time
import str_handl
import check
from thread import *
import threading

import struct
import binascii
flag = 1

class frame():
    def __init__(self,obj,name):
        self.label = LabelFrame(obj.root,text = name,padx=5,pady=5)
        self.t1 = Text(self.label, height=1, width=5)
        self.t2 = Text(self.label, height=1, width=5)
        self.t3 = Text(self.label, height=1, width=5)
        self.t4 = Text(self.label, height=1, width=5)
        self.t5 = Text(self.label, height=1, width=5)
        self.t6 = Text(self.label, height=1, width=5)
        self.t7 = Text(self.label, height=1, width=5)
        label_wendu = Label(self.label, text = "温度", height = 1, fg = "black")
        label_shidu = Label(self.label, text = "湿度", height = 1, fg = "black")
        label_pm2 = Label(self.label, text = "PM2.5", height = 1, fg = "black")
        label_pm10 = Label(self.label, text = "PM10", height = 1, fg = "black")
        label_co = Label(self.label, text = "CO2", height = 1, fg = "black")
        label_tvoc = Label(self.label, text = "TVOCs", height = 1, fg = "black")
        label_jiaquan = Label(self.label, text = "甲醛", height = 1, fg = "black")
        label_wendu_1 = Label(self.label, text = "℃", height = 1, fg = "black")
        label_shidu_1 = Label(self.label, text = "%", height = 1, fg = "black")
        label_pm2_1 = Label(self.label, text = "ug/㎡", height = 1, fg = "black")
        label_pm10_1 = Label(self.label, text = "ug/㎡", height = 1, fg = "black")
        label_co_1 = Label(self.label, text = "ppm", height = 1, fg = "black")
        label_tvoc_1 = Label(self.label, text = "mg/㎡", height = 1, fg = "black")
        label_jiaquan_1 = Label(self.label, text = "mg/㎡", height = 1, fg = "black")
        def btnHelloClicked():
            labelHello.config(text = "Hello Tkinter!")
        btn_dancicaiji = Button(self.label, text = "单次采集", height =1 , width = 7,command = btnHelloClicked)
        label_wendu.grid(row=0,column=0)
        label_shidu.grid(row=1,column=0)        
        label_pm2.grid(row=2,column=0)
        label_pm10.grid(row=3,column=0)
        label_co.grid(row=4,column=0)
        label_tvoc.grid(row=5,column=0)
        label_jiaquan.grid(row=6,column=0)
        self.t1.grid(row=0,column=1)
        self.t2.grid(row=1,column=1)
        self.t3.grid(row=2,column=1)
        self.t4.grid(row=3,column=1)
        self.t5.grid(row=4,column=1)
        self.t6.grid(row=5,column=1)
        self.t7.grid(row=6,column=1)
        label_wendu_1.grid(row=0,column=2)
        label_shidu_1.grid(row=1,column=2)
        label_pm2_1.grid(row=2,column=2)
        label_pm10_1.grid(row=3,column=2)
        label_co_1.grid(row=4,column=2)
        label_tvoc_1.grid(row=5,column=2)
        label_jiaquan_1.grid(row=6,column=2)
        btn_dancicaiji.grid(row=7,column=1)
    

class frame_heat():
    def __init__(self,obj,name):
        self.label = LabelFrame(obj.root,text = name,padx=5,pady=5)
        label_biaohao = Label(self.label, text = "表号", height = 1, fg = "black")
        label_leijilengliang = Label(self.label, text = "累计冷量", height = 1, fg = "black")
        label_leijireliang = Label(self.label, text = "累计热量", height = 1, fg = "black")
        label_gonglv = Label(self.label, text = "功率", height = 1, fg = "black")
        label_shunshiliuliang = Label(self.label, text = "瞬时流量", height = 1, fg = "black")
        label_leijiliuliang = Label(self.label, text = "累计流量", height = 1, fg = "black")
        label_jinshuwendu = Label(self.label, text = "进水温度", height = 1, fg = "black")
        label_huishuiwendu = Label(self.label, text = "回水温度", height = 1, fg = "black")
        label_gongzuoshijian = Label(self.label, text = "工作时间", height = 1, fg = "black")
        label_shizhong = Label(self.label, text = "时  钟", height = 1, fg = "black")
        label_zhuangtai = Label(self.label, text = "状  态", height = 1, fg = "black")
        

        label_leijilengliang_1 = Label(self.label, text = "KW*h  ", height = 1, fg = "black")
        label_leijireliang_1 = Label(self.label, text = "KW*h  ", height = 1, fg = "black")
        label_gonglv_1 = Label(self.label, text = "W    ", height = 1, fg = "black")
        label_shunshiliuliang_1 = Label(self.label, text = "㎡/h", height = 1, fg = "black")
        label_leijiliuliang_1 = Label(self.label, text = "m³ ", height = 1, fg = "black")
        label_jinshuwendu_1 = Label(self.label, text = "℃ ", height = 1, fg = "black")
        label_huishuiwendu_1 = Label(self.label, text = "℃ ", height = 1, fg = "black")
        label_gongzuoshijian_1 = Label(self.label, text = "h", height = 1, fg = "black")

        self.t1 = Text(self.label, height=1, width=10)
        self.t2 = Text(self.label, height=1, width=10)
        self.t3 = Text(self.label, height=1, width=10)
        self.t4 = Text(self.label, height=1, width=10)
        self.t5 = Text(self.label, height=1, width=10)
        self.t6 = Text(self.label, height=1, width=10)
        self.t7 = Text(self.label, height=1, width=10)
        self.t8 = Text(self.label, height=1, width=10)
        self.t9 = Text(self.label, height=1, width=10)
        self.t10 = Text(self.label, height=1, width=10)
        self.t11 = Text(self.label, height=1, width=10)
        def btnHelloClicked():
            labelHello.config(text = "Hello Tkinter!")
        btn_dancicaiji = Button(self.label, text = "单次采集 Meter", height =1 , width = 13)

        label_biaohao.grid(row=0,column=0)
        self.t1.grid(row=0,column=1)
        label_leijilengliang.grid(row=1,column=0)
        self.t2.grid(row=1,column=1)
        label_leijilengliang_1.grid(row=1,column=2)
        label_leijireliang.grid(row=2,column=0)
        self.t3.grid(row=2,column=1)
        label_leijireliang_1.grid(row=2,column=2)
        label_gonglv.grid(row=3,column=0)
        self.t4.grid(row=3,column=1)
        label_gonglv_1.grid(row=3,column=2)
        label_shunshiliuliang.grid(row=0,column=3)
        self.t5.grid(row=0,column=4)
        label_shunshiliuliang_1.grid(row=0,column=5)
        label_leijiliuliang.grid(row=1,column=3)
        self.t6.grid(row=1,column=4)
        label_leijiliuliang_1.grid(row=1,column=5)
        label_jinshuwendu.grid(row=2,column=3)
        self.t7.grid(row=2,column=4)
        label_jinshuwendu_1.grid(row=2,column=5)
        label_huishuiwendu.grid(row=3,column=3)
        self.t8.grid(row=3,column=4)
        label_huishuiwendu_1.grid(row=3,column=5)
        '''label_gongzuoshijian.grid(row=0,column=6)
        self.t9.grid(row=0,column=7)
        label_gongzuoshijian_1.grid(row=0,column=8)
        label_shizhong.grid(row=1,column=6)
        self.t10.grid(row=1,column=7)'''
        label_zhuangtai.grid(row=0,column=6)  
        self.t11.grid(row=1,column=6)
        btn_dancicaiji.grid(row=2,column=6)
class frame_gprs():
    def __init__(self,obj,name):
        self.label = LabelFrame(obj.root,width=610, height=160,text = name,padx=5,pady=5)    

        #标签控件:可以显示文本和位图
        label_IP = Label(self.label, text = "IP与PORT", height = 1, width = 10, fg = "black")
        label_socket = Label(self.label, text = "socket", height = 1, width = 10, fg = "black")
        label_GPRS = Label(self.label, text = "GPRS在线状态", height = 1, fg = "black")
        label_GPRS1 = Label(self.label, text = "在线个数：", height = 1, fg = "black")
        label_GPRS2 = Label(self.label, text = "下拉在线状态：", height = 1, fg = "black")
        def btnHelloClicked():
            labelHello.config(text = "Hello Tkinter!")
        btn_closelisten = Button(self.label, text = "关闭监听", height =1 , command = btnHelloClicked)

        

        
        #文本框
        self.t1 = Text(self.label, height=8, width=70, state=DISABLED)
        self.t2 = Text(self.label, height=2, width=10)
        self.t3 = Text(self.label, height=4, width=10)
        label_IP.place(x = 0, y = 5, anchor = NW)
        label_socket.place(x = 250, y = 5)
        btn_closelisten.place(x = 430, y = 0 , anchor = NW)
        label_GPRS.place(x = 500, y = 0, anchor = NW)
        label_GPRS1.place(x = 500, y = 50, anchor = NW)
        label_GPRS2.place(x = 500, y = 70, anchor = NW)
        self.t1.place(x = 0, y = 35, anchor = NW)
        self.t2.place(x = 505, y = 20, anchor = NW)
        self.t3.place(x = 505, y = 90, anchor = NW)

class frame_comm():
    def __init__(self,obj,name):
        self.label = LabelFrame(obj.root,width=80, height=160,text = name,padx=5,pady=5)
        self.v=IntVar()
        Radiobutton(self.label,variable = self.v,text = '485',value = 1).place(x = 0, y = 20, anchor = NW)
        Radiobutton(self.label,variable = self.v,text = '无线',value = 0).place(x = 0, y = 70, anchor = NW)
        #485 or zigbee
        self.flag = 0
class UI():

    def __init__(self):


        # 创建窗口对象的背景色
        self.root = Tk()

        # 窗口大小可调性
        self.root.resizable(0,0)

        # 窗口大小
        self.root.geometry('1170x450')

        # 创建窗口标签
        self.root.title('hello')
        
        #框架
        self.frame_9 = frame_comm(self,'通信方式')
        self.frame_0 = frame_gprs(self,'')
        self.frame_1 = frame_heat(self,'热量表')
        self.frame_2 = frame(self,'主机')
        self.frame_3 = frame(self,'#1从机')
        self.frame_4 = frame(self,'#2从机')
        self.frame_5 = frame(self,'#3从机')
        self.frame_6 = frame(self,'#4从机')
        self.frame_7 = frame(self,'#5从机')
        self.frame_8 = frame(self,'#6从机')

        # 连接动作函数
        btn_kaishicaiji = Button(self.root, text = "开始采集", height =1 , width = 7,command = self.printhello)
        btn_tingzhicaiji = Button(self.root, text = "停止采集", height =1 , width = 7)
        btn_kaishiruku = Button(self.root, text = "开始入库", height =1 , width = 7)
        btn_tingzhiruku = Button(self.root, text = "停止入库", height =1 , width = 7)
        btn_qingkong = Button(self.root, text = " 清空 ", height =1 , width = 7)

        self.frame_0.label.place(x = 10, y = 10 )
        self.frame_9.label.place(x = 625, y = 10 )
        self.frame_1.label.place(x = 713, y = 20 )
        self.frame_2.label.place(x = 10, y = 170 ) 
        self.frame_3.label.place(x = 175, y = 170 )
        self.frame_4.label.place(x = 340, y = 170 )
        self.frame_5.label.place(x = 505, y = 170 )
        self.frame_6.label.place(x = 670, y = 170 )
        self.frame_7.label.place(x = 835, y = 170 )
        self.frame_8.label.place(x = 1000, y = 170 )

        btn_kaishicaiji.place(x = 80, y = 410, anchor = NW)
        btn_tingzhicaiji.place(x = 240, y = 410, anchor = NW)
        btn_kaishiruku.place(x = 420, y = 410, anchor = NW)
        btn_qingkong.place(x = 580, y = 410, anchor = NW)

    def init(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print '\n     ------Socket创建成功-------'.decode('UTF-8').encode('GBK')
        HOST = ''   # Symbolic name meaning all available interfaces
        PORT = 8080 # Arbitrary non-privileged port
 
        
 
        #Bind socket to local host and port
        try:
            self.s.bind((HOST, PORT))
        except socket.error , msg:
            print '     ------Socket绑定失败-------\n   错误类型 : '.decode('UTF-8').encode('GBK')+ str(msg[0]).decode('UTF-8').encode('GBK') + ' 错误信息 '.decode('UTF-8').encode('GBK') + msg[1].decode('UTF-8').encode('GBK')
            sys.exit()
     
        print '     ------Socket绑定成功-------'.decode('UTF-8').encode('GBK')
        #Start listening on socket
        self.s.listen(10)
        print '     ------Socket开始监听-------'.decode('UTF-8').encode('GBK')
 
        #Function for handling connections. This will be used to create threads
        def clientthread(conn):
            #Sending message to connected client
            #infinite loop so that function do not terminate and thread do not end.
            while True:
                #Receiving from client
                data_str = conn.recv(1024)
                #str_handl.setup(time.strftime("%H%M%S",time.localtime()),check.check(),8,data_str)
                #self.display(data_str)
                try:
                    if len(self.str_list(data_str))>100:
                        self.show(self.frame_1,self.decode_R(self.list_X(self.str_list(data_str),0)),9)
                        self.show(self.frame_2,self.decode_r(self.list_x(self.str_list(data_str),0)),7)
                        self.show(self.frame_3,self.decode_r(self.list_x(self.str_list(data_str),1)),7)
                        self.show(self.frame_4,self.decode_r(self.list_x(self.str_list(data_str),2)),7)
                        self.show(self.frame_5,self.decode_r(self.list_x(self.str_list(data_str),3)),7)
                        self.show(self.frame_6,self.decode_r(self.list_x(self.str_list(data_str),4)),7)
                        self.show(self.frame_7,self.decode_r(self.list_x(self.str_list(data_str),5)),7)
                        self.show(self.frame_8,self.decode_r(self.list_x(self.str_list(data_str),6)),7)
                except:
                    self.frame_0.t1.config(state=NORMAL)
                    self.frame_0.t1.insert(END,'\n     ------Socket连接终止-------')
                    self.frame_0.t1.config(state=DISABLED)
                    break
        #now keep talking with the client
        while 1:
            #wait to accept a connection - blocking call
            self.conn, self.addr = self.s.accept()
            print 'Connected with ' + self.addr[0] + ':' + str(self.addr[1])
     
            #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
            start_new_thread(clientthread ,(self.conn,)) 
        self.s.close()
    def startNewThread(self):
        #启动一个新线程来接收服务器端的消息
        #thread.start_new_thread(function,args[,kwargs])函数原型，
        #其中function参数是将要调用的线程函数，args是传递给线程函数的参数，它必须是个元组类型，而kwargs是可选的参数
        #receiveMessage函数不需要参数，就传一个空元组
        start_new_thread(self.init,())
    def printhello(self):
        try:
            self.R(self.frame_9)
            print self.frame_9.flag
            ss="\x21\x24\x00\x01\x01\xff"+self.frame_9.flag
            ss=ss+str(self.sum_add(ss))+'\x23'
            self.conn.send(ss)
            print "              发送成功".decode('UTF-8').encode('GBK')
            self.frame_0.t1.config(state=NORMAL)
            self.frame_0.t1.insert(END,'             发送成功              ')
            self.frame_0.t1.config(state=DISABLED)
            self.frame_0.t1.see(END)
        except:
            print "          发送失败          ".decode('UTF-8').encode('GBK')
            self.frame_0.t1.config(state=NORMAL)
            self.frame_0.t1.insert(END,'               发送失败           ')
            self.frame_0.t1.config(state=DISABLED)
            self.frame_0.t1.see(END)
    def sum_add(self,s):
        sum_add=0
        j=0
        while j<len(s):
            sum_add=int(struct.unpack('B', bytes(s[j]))[0])+sum_add
            j=j+1
        return struct.pack('B', sum_add%255)

    def display(self,s):
        self.frame_0.label.place(x = 10, y = 10 )
        self.frame_0.t1.config(state=NORMAL)
        self.frame_0.t1.insert(END,)
        self.frame_0.t1.config(state=DISABLED)
        self.frame_1.label.place(x = 630, y = 20 )
        self.frame_2.label.place(x = 10, y = 170 ) 
        self.frame_3.label.place(x = 175, y = 170 )
        self.frame_4.label.place(x = 340, y = 170 )
        self.frame_5.label.place(x = 505, y = 170 )
        self.frame_6.label.place(x = 670, y = 170 )
        self.frame_7.label.place(x = 835, y = 170 )
        self.frame_8.label
    def str_list(self,s):
        if(str(binascii.b2a_hex(s))[:4]=='2124'):
            if(str(binascii.b2a_hex(s))[-4:-2]=='23'):
                ss=str(binascii.b2a_hex(s))[2:-4]
                j=len(ss)/2
                i=0
                list = []
                while (i<j):
                    list.append(ss[:2])
                    ss = ss[2:]
                    i=i+1
                return list
    def strconvert(self,s):  
        s=str(s).strip().split(' ')  
        my=r'\x'  
        fin=''  
        for i in range(len(s)):  
            fin=fin+struct.pack('B',int(s[i],16))  
        return fin
    def normal(self,list,head,end):
        ss=''
        i=0
        while(i<end-head+1):
            ss=ss+list[head+i]
            i=i+1
        return ss
    def back(self,list,head,end):
        ss=''
        i=0
        while(i<end-head+1):
            ss=ss+list[end-i]
            i=i+1
        return ss
    def state(self,list,pos):
        if(list[pos]=='00'):
            return '正常'
        else:
            ss=''
            s=int(list[pos],16)
            if(s/32>0):
                s=s%32
                ss=ss+'低压'
            if(s/16>0):
                s=s%16
                ss=ss+'过流'
            if(s/8>0):
                s=s%8
                ss=ss+'损坏'
            if(s/4>0):
                s=s%4
                ss=ss+'无水'
            if(s/2>0):
                s=s%2
                ss=ss+'断路'
            if(s/1>0):
                ss=ss+'短路'
        return ss
        
    def h256l(self,list,head):
        s=int(list[head], 16)*256+int(list[head+1],16)
        return s
    def h256l_10(self,list,head):
        s=int(list[head], 16)*256+int(list[head+1],16)
        return float(s)/10
    def h256l_125(self,list,head):
        s=int(list[head], 16)*256+int(list[head+1],16)
        return round(-6+125*float(s)/2**16,2)
    def h256l_175(self,list,head):
        s=int(list[head], 16)*256+int(list[head+1],16)
        return round(-46.85+175.72*float(s)/2**16,2)
    def show(self,obj,list_r,x):
        obj.t1.config(state=NORMAL)
        obj.t1.delete('0.0',END)
        obj.t1.insert(END,list_r[0])
        obj.t1.config(state=DISABLED)
        obj.t2.config(state=NORMAL)
        obj.t2.delete('0.0',END)
        obj.t2.insert(END,list_r[1])
        obj.t2.config(state=DISABLED)
        obj.t3.config(state=NORMAL)
        obj.t3.delete('0.0',END) 
        obj.t3.insert(END,list_r[2])
        obj.t3.config(state=DISABLED)
        obj.t4.config(state=NORMAL)
        obj.t4.delete('0.0',END) 
        obj.t4.insert(END,list_r[3])
        obj.t4.config(state=DISABLED)
        obj.t5.config(state=NORMAL)
        obj.t5.delete('0.0',END)
        obj.t5.insert(END,list_r[4])
        obj.t5.config(state=DISABLED)
        obj.t6.config(state=NORMAL)
        obj.t6.delete('0.0',END)
        obj.t6.insert(END,list_r[5])
        obj.t6.config(state=DISABLED)
        obj.t7.config(state=NORMAL)
        obj.t7.delete('0.0',END)
        obj.t7.insert(END,list_r[6])
        obj.t7.config(state=DISABLED)
        if x==9:
            obj.t8.config(state=NORMAL)
            obj.t8.delete('0.0',END)
            obj.t8.insert(END,list_r[7])
            obj.t8.config(state=DISABLED)
            obj.t11.config(state=NORMAL)
            obj.t11.delete('0.0',END)
            obj.t11.insert(END,list_r[8])
            obj.t11.config(state=DISABLED)
    def list_x(self,list_s,x):
        list_r=[]
        i=0
        while i<14:
            list_r.append(list_s[i+14*x+7])
            i=i+1
        return list_r
    def decode_r(self,list_r):
        list=[]
        list.append(self.h256l_175(list_r,10))
        list.append(self.h256l_125(list_r,8))
        list.append(self.h256l(list_r,6))
        list.append(self.h256l(list_r,12))
        list.append(self.h256l(list_r,0))
        list.append(self.h256l_10(list_r,2))
        list.append(self.h256l_10(list_r,4))
        return list
    def decode_R(self,list_r):
        list=[]
        list.append(self.normal(list_r,0,3))
        list.append(int(self.back(list_r,4,7)))
        list.append(float(self.back(list_r,8,12))/100)
        list.append(int(self.back(list_r,14,17)))
        list.append(int(self.back(list_r,19,22)))
        list.append(int(self.back(list_r,24,27)))
        list.append(float(self.back(list_r,29,31))/100)
        list.append(float(self.back(list_r,32,34))/100)
        list.append(self.state(list_r,35))
        return list
    def list_X(self,list_s,x):
        list_r=[]
        i=0
        while i<36:
            list_r.append(list_s[i+105])
            i=i+1
        return list_r
    def R(self,s):
        if(s.v.get()==1):
            s.flag='\x00'
        if(s.v.get()==0):
            s.flag='\xff'
def main():
    ui = UI()
    ui.startNewThread()
    ui.root.mainloop()
    
    
if __name__=='__main__':
    main()
        # 进入消息循环
