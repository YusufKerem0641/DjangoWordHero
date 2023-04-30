from selenium import webdriver
from selenium.webdriver.common.by import By
from time import time, sleep

import customtkinter as ctk
import threading

class Browser():
    def __init__(self,setting):
        self.setting = setting

    def browserStart(self):
        self.browser = self.setting.browser
        self.browser.get(self.setting.link)

    def start(self):
        self.browser = webdriver.Chrome()
        self.setting.browser = self.browser

    def pageControl(self,url):
        for i in range(len(self.browser.window_handles)):
            self.browser.switch_to.window(self.browser.window_handles[i])
            if self.browser.current_url == url:
                break

    def save(self):
        html_source = self.browser.page_source
        with open(self.setting.filePath+"\\"+str(time())+".html", "w",encoding='utf-8') as dosya:
            dosya.write(html_source)

    def tusControl(self):
        return self.browser.find_elements(By.XPATH, self.setting.tusXpath)

    def tusTekrar(self):
        while True:
            if self.setting.tusControlTime == 0:
                print("Durdurlurdu")
                break
            elif len(self.tusControl()) != 0 :
                print("Basıldı")
                self.tusClick()
                self.setting.basilmaSayisi += 1
            sleep(self.setting.tusControlTime)

    def tusClick(self):
        try:
            sleep(self.setting.kacSaniyeBas)
            self.browser.find_elements(By.XPATH,self.setting.tusXpath)[0].click()
        except:
            print(self.browser.find_elements(By.XPATH,self.setting.tusXpath))

class Setting():
    filePath = ""#"G:\\Files"
    kacSaniyeBas = 2
    tusControlTime = 2
    tusXpath = '//*[@id="perculus-container"]/div[4]/div[6]/div/div/div[3]/button'
    link = "https://google.com/"
    browser = None
    basilmaSayisi = 0

class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Ders Yoklama")
        self.geometry("180x50")
        self.attributes('-topmost', True)
        self.startButton = ctk.CTkButton(self,text="Chrome başlat",command=self.browserStart)
        self.startButton.grid(row=0, column=0,
                                        columnspan=2,
                                        padx=20, pady=10,
                                        sticky="ew")
    def browserStart(self):

        self.browser = Browser(Setting())
        self.browser.start()
        self.browser.browserStart()

        self.startButton.configure(width=100)
        self.startButton.grid(row=5, column=1,
                                        padx=10, pady=10,
                                        sticky="ew")
        self.saveButton = ctk.CTkButton(self, text="Kaydet", command=self.save,width=100)
        self.saveButton.grid(row=5, column=0,
                                        padx=10, pady=10,
                                        sticky="ew")


        ctk.CTkLabel(self,text="Url:").grid(row=0, column=0,
                           padx=10, pady=10,
                           sticky="ew")


        self.url = ctk.CTkEntry(self)
        self.url.grid(row=0, column=1,
                            columnspan=2, padx=10,
                            pady=10, sticky="ew")

        ctk.CTkLabel(self, text="Basma süresi:").grid(row=1, column=0,
                                             padx=10, pady=10,
                                             sticky="ew")

        self.kacSaniyeBas = ctk.CTkEntry(self)
        self.kacSaniyeBas.grid(row=1, column=1,
                      columnspan=3, padx=10,
                      pady=10, sticky="ew")

        ctk.CTkLabel(self, text="Kontrol Süresi").grid(row=2, column=0,
                                                      padx=10, pady=10,
                                                      sticky="ew")

        self.tusControlTime = ctk.CTkEntry(self)
        self.tusControlTime.grid(row=2, column=1,
                               columnspan=3, padx=10,
                               pady=10, sticky="ew")
        ctk.CTkLabel(self, text="Path:").grid(row=3, column=0,
                                                      padx=10, pady=10,
                                                      sticky="ew")

        self.filePath = ctk.CTkEntry(self)
        self.filePath.grid(row=3, column=1,
                               columnspan=3, padx=10,
                               pady=10, sticky="ew")

        ctk.CTkLabel(self, text="Xpath:").grid(row=4, column=0,
                                                      padx=10, pady=10,
                                                      sticky="ew")

        self.tusXpath = ctk.CTkEntry(self)
        self.tusXpath.grid(row=4, column=1,
                               columnspan=3, padx=10,
                               pady=10, sticky="ew")

        self.kacSaniyeBas.insert(0, "2")
        self.tusControlTime.insert(0, "2")
        self.tusXpath.insert(0, self.browser.setting.tusXpath)
        self.filePath.insert(0, self.browser.setting.filePath)

        self.geometry("280x300")
        self.start()

    def start(self):
        self.browser.setting.tusControlTime = 0
        self.startButton.configure(
            text="Çalıştır",
            command=self.driverStart
        )

    def driverStart(self):
        self.browser.setting.filePath = self.filePath.get()
        self.browser.setting.kacSaniyeBas = int(self.kacSaniyeBas.get())
        self.browser.setting.tusControlTime = int(self.tusControlTime.get())
        self.browser.setting.tusXpath = self.tusXpath.get()
        self.browser.pageControl(self.url.get())
        x = threading.Thread(target=self.browser.tusTekrar,daemon=True)
        x.start()
        threading.Thread(target=self.basilma, daemon=True).start()

        self.startButton.configure(
            text="Durdur",
            command=self.start
        )

    def save(self):
        self.browser.pageControl(self.url.get())
        self.browser.save()

    def basilma(self):
        while True:
            if 0 == self.browser.setting.tusControlTime:
                break
            self.title(f"Yoklama Basilma: {self.browser.setting.basilmaSayisi}")
            sleep(self.browser.setting.tusControlTime)

class GuiMain():
    def __init__(self):
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("green")
        app = App()
        app.mainloop()

if __name__ == "__main__":
    GuiMain()
