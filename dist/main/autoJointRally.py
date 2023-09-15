from screeenshot import Auto
import time as tm

class AutoJointRally:
    def __init__(self,exit_flag,settingJoinRally,ip,port):
        self.settingJoinRally = settingJoinRally
        self.exit_flag = exit_flag
        self.ip = ip
        self.port = port
        self.sc = Auto(self.ip,self.port)
        # Image varibles
        self.imgLoggame = ".\images\loggin\\Evony.png"
        self.imggifloggin = ".\images\loggin\\gifloggin.png"
        self.imgdelay = ".\images\loggin\\delay.png"
        self.imgalliance = ".\images\\alliance.png"
        self.imglogagain = ".\images\loggin\\logagain.png"
        self.imginAlliance = ".\images\inAlliance\\inAlliance.png"
        self.imginWar = ".\images\inAlliance\\inWar.png"
        self.imginChamp = ".\images\inAlliance\\inChamp.png"
        self.imgWar = ".\images\inAlliance\\War.png"
        self.imgjointRally = ".\images\\Rally\\jointRally.png"
        self.imgjointRally2 = ".\images\\Rally\\jointRally2.png"
        self.imgselectArmy = ".\images\\Rally\\selectArmy.png"
        self.imgcheckChamp = ".\images\\Rally\\checkChamp.png"
        self.imgchamp1 = ".\images\\Rally\\champ1.png"
        self.imgchamp2 = ".\images\\Rally\\champ2.png"
        self.imgselectChamp = ".\images\\Rally\\selectChamp.png"
        self.imgerror1 = ".\images\\error\\1.png"
        self.imgerror2 = ".\images\\error\\2.png"
        self.imggetmeat = ".\images\\meat\\getmeat.png"
        self.imginmeat = ".\images\\meat\\inmeat.png"
        self.img200KC = ".\images\\meat\\200KC.png"
        self.imgtickmeat = ".\images\\meat\\tickmeat.png"
        
        # Check varibles
        self.checkInWar = 0
        self.checkAlliance = 0
        self.checkChamp = 0
        self.checkmeat = 0
        self.Run()
        
    def Run(self):
        while not self.exit_flag.is_set():
            
            if self.exit_flag.is_set():
                return
            if self.checkInWar == 0:
                self.Click()

            if self.checkInWar == 1:
                if self.settingJoinRally['filterBossVar'] == 0:
                    self.bosNFilter()
            
            if self.checkChamp == 1:
                self.chosechamp()
                
            if self.checkmeat == 1:
                self.eatmeat()
            tm.sleep(1)
    
    def Click(self):
        while 1:
            if self.exit_flag.is_set():
                return
            screenshot = self.sc.screen_capture()
            
            # Check đã vô lm chưa
            check = self.sc.find_img(self.imginAlliance,screenshot, 0.99, 1)
            if check != False:
                self.checkAlliance = 1
            else:
                self.checkAlliance = 0
            
            # Check đã vô chien tranh chưa
            check = self.sc.find_img(self.imginWar,screenshot, 0.9, 1)
            if check != False:
                self.checkInWar = 1
                self.checkAlliance = 1
            else:
                self.checkInWar = 0
            
            # vào chiến tranh
            if self.checkAlliance == 1:
                click = self.sc.find_img(self.imgWar,screenshot, 0.99, 1)
                if click != False:
                    self.sc.click(click[0][0], click[0][1])
                    tm.sleep(1)
                    return
            
            if self.checkAlliance == 0  and self.checkInWar == 0:
                # delay vào game 
                click = self.sc.find_img(self.imgdelay,screenshot, 0.9, 1)
                if click != False:
                    return
                
                # fix lỗi 
                # Log lại game
                click = self.sc.find_img(self.imgerror2,screenshot, 0.9, 1)
                if click != False:
                    self.sc.click(click[0][0], click[0][1])
                    tm.sleep(1)
                    return
                
                # Log lại game
                click = self.sc.find_img(self.imglogagain,screenshot, 0.9, 1)
                if click != False:
                    self.sc.click(click[0][0], click[0][1])
                    tm.sleep(5)
                    return
            
                # Vô game
                click = self.sc.find_img(self.imgLoggame,screenshot, 0.9, 1)
                if click != False:
                    self.sc.click(click[0][0], click[0][1])
                    tm.sleep(5)
                    return
            
                # Nhận quà đăng nhập
                click = self.sc.find_img(self.imggifloggin,screenshot, 0.9, 1)
                if click != False:
                    self.sc.click(click[0][0], click[0][1])
                    tm.sleep(2)
                    return
            
                # Tìm liên Minh
                click = self.sc.find_img(self.imgalliance,screenshot, 0.99, 1)
                if click != False:
                    self.sc.click(click[0][0], click[0][1])
                    tm.sleep(2)
                    return
                
                # Thoat nhanh
                self.sc.esc()

            if self.checkAlliance == 1  and self.checkInWar == 0:
                self.sc.esc()
            return
        
    def bosNFilter(self):
        while 1:
            if self.exit_flag.is_set():
                return
            screenshot = self.sc.screen_capture()
            
            # print(self.settingJoinRally)
            check = self.sc.find_img(self.imginWar,screenshot, 0.99, 1)
            if check != False:
                self.checkInWar = 1
                self.checkAlliance = 1
            else:
                self.checkInWar = 0
                return
            
            #check error
            check = self.sc.find_img(self.imgerror1,screenshot, 0.9, 1)
            if check != False:
                self.sc.esc()
            check = self.sc.find_img(self.imgjointRally2,screenshot, 0.9, 1)
            if check != False:
                self.sc.esc()
            # =====================================================================
            
            # Hết thịt============================================================
            
            # vào sử dụng thịt
            click = self.sc.find_img(self.imggetmeat,screenshot, 0.9, 1)
            if click != False:
                self.sc.click(click[0][0], click[0][1])
                self.checkmeat = 1
                tm.sleep(1)
                return
            # ========================================================================
            # run
            click = self.sc.find_img(self.imgjointRally,screenshot, 0.9, 1)
            if click != False:
                self.sc.click(click[0][0], click[0][1])
                tm.sleep(2)
                return
            
            click = self.sc.find_img(self.imgselectArmy,screenshot, 0.9, 1)
            if click != False:
                self.sc.click(click[0][0], click[0][1])
                tm.sleep(1)
                return
            
            click = self.sc.find_img(self.imgcheckChamp,screenshot, 0.9, 1)
            if click != False:
                if self.settingJoinRally['numberChamp'] == '0':
                    self.sc.click(400, 915)
                    tm.sleep(1)
                    return
                elif self.settingJoinRally['numberChamp'] == '1':
                    click = self.sc.find_img(self.imgchamp1,screenshot, 0.99, 1)
                    if click != False:
                        self.sc.click(click[0][0], click[0][1])
                        self.checkChamp = 1
                        self.checkInWar == 2
                        tm.sleep(1)
                        return
                    else:
                        self.sc.click(400, 915)
                elif self.settingJoinRally['numberChamp'] == '2' or int(self.settingJoinRally['numberChamp']) > 2:
                    click = self.sc.find_img(self.imgchamp1,screenshot, 0.99, 1)
                    if click != False:
                        self.sc.click(click[0][0], click[0][1])
                        self.checkChamp = 1
                        self.checkInWar == 2
                        tm.sleep(1)
                        return
                    click = self.sc.find_img(self.imgchamp2,screenshot, 0.99, 1)
                    if click != False:
                        self.sc.click(click[0][0], click[0][1])
                        self.checkChamp = 1
                        self.checkInWar == 2
                        tm.sleep(1)
                        return
                    else:
                        self.sc.click(400, 915)
                
            tm.sleep(1)
        
    def chosechamp(self):
        while 1:
            if self.exit_flag.is_set():
                return
            screenshot = self.sc.screen_capture()
            
            # Check đã vô chọn tướng chưa
            check = self.sc.find_img(self.imginChamp,screenshot, 0.9, 1)
            if check != False:
                self.checkChamp = 1
            else:
                self.checkInWar == 1
                self.checkChamp = 0
           
            if  self.checkChamp == 1:
                click = self.sc.find_img(self.imgselectChamp,screenshot, 0.9, 1)
                if click != False:
                    self.sc.click(click[0][0], click[0][1])
                    self.checkChamp = 0
                    tm.sleep(1)
                    return
            tm.sleep(1)
            return
        
    def eatmeat(self):
        nummeat = int(self.settingJoinRally['numberMeat'])
        if nummeat == 0 or nummeat < 3:
            nummeat = 5
        while 1:
            if self.exit_flag.is_set():
                return
            screenshot = self.sc.screen_capture()
            check = self.sc.find_img(self.imginmeat,screenshot, 0.9, 1)
            if check == False:
                self.checkmeat = 0
                return
            
            click = self.sc.find_img(self.imgtickmeat,screenshot, 0.9, 1)
            if click != False:
                for i in range(nummeat):
                    self.sc.click(click[0][0], click[0][1])
                self.sc.click(375, 685)
                tm.sleep(2)
                self.sc.esc()
                self.checkmeat = 0
                return
            
            click = self.sc.find_img(self.img200KC,screenshot, 0.9, 1)
            if click != False:
                if click[0][1] > 330 and click[0][1] < 450:
                    self.sc.click(443, 551)
                    tm.sleep(1)
                else:
                    self.sc.click(449, 393)
                    tm.sleep(1)
            else:
                self.sc.click(449, 393)
                tm.sleep(1)
                
            tm.sleep(1)