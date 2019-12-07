#-*- coding: utf-8 -*-

from fairsionCamera import *
import win32com.client
from ctypes import *

DeviceManager = win32com.client.DispatchEx('{939934F4-20DF-4866-A30D-0635F879725E}')

ImageDll = cdll.LoadLibrary("AuxiliaryCore_interface.dll")



class Camera:
    
    def __init__(self, index = 0):
        super().__init__()
        
        self.nWidth = 0
        self.nHeight = 0
        self.nBit = 8
        self.pImage = 0 # image data address
        self.nCount = 0
        self.bIsOpen = False
        self.nIndex = index
        self.raw_memory = None



    @classmethod
    def InitManager(cls):
        print("初始化设备管理对象，仅在程序入口处初始化一次即可")
        
        print("获取实例化对象")
        
        DeviceManager.Initialize()
        cameraCount = DeviceManager.GetCameraCount(2000)
        
        print("当前相机数目为：", cameraCount)
        return cameraCount

    @classmethod
    def ReleaseManager(cls):
        print("释放设备管理对象，仅在程序出口处调用一次即可，与Initialize对应")
        DeviceManager.Terminate()
    
    def OpenCamera(self):
        print("打开相机", self.nIndex + 1)
        self.Vendor = DeviceManager.GetCamera(self.nIndex).GetDeviceInfo().VendorName
        self.ModelName = DeviceManager.GetCamera(self.nIndex).GetDeviceInfo().ModelName
        self.SerialNumber = DeviceManager.GetCamera(self.nIndex).GetDeviceInfo().SerialNumber
        
        print("厂商名称", self.Vendor)
        print("设备名称", self.ModelName)
        print("设备序列号", self.SerialNumber)
        
        DeviceManager.GetCamera(self.nIndex).Open()
        
        self.bIsOpen = DeviceManager.GetCamera(self.nIndex).IsOpen()
        
        if self.bIsOpen:
            print("打开相机成功")
            self.nWidth = DeviceManager.GetCamera(self.nIndex).GetValue("Width")
            self.nHeight = DeviceManager.GetCamera(self.nIndex).GetValue("Height")
            nColor = DeviceManager.GetCamera(self.nIndex).GetValue("PixelColorFilter")
            if nColor != 0 :
                self.nBit = 24
            print("图像宽度", self.nWidth, "图像高度", self.nHeight, "像素位数", self.nBit)
        else:
            print("打开相机失败")
            
    def CloseCamera(self):
        print("关闭相机", self.nIndex + 1)
        DeviceManager.GetCamera(self.nIndex).StopCapture()
        DeviceManager.GetCamera(self.nIndex).Close()


    def SetExposure(self, nValue):
        print("设置相机", self.nIndex + 1, "曝光时间值为", nValue)
        self.bIsOpen = DeviceManager.GetCamera(self.nIndex).IsOpen()
        if self.bIsOpen:
            DeviceManager.GetCamera(self.nIndex).SetValue("ExposureTimeRaw", nValue)
            nShuter = DeviceManager.GetCamera(self.nIndex).GetValue("ExposureTimeRaw")
            print("当前相机曝光时间值为", nShuter)


    def SetGain(self, nValue):
        print("设置相机", self.nIndex + 1, "增益值为", nValue)
        self.bIsOpen = DeviceManager.GetCamera(self.nIndex).IsOpen()
        if self.bIsOpen:
            DeviceManager.GetCamera(self.nIndex).SetValue("GainRaw", nValue)
            nGain = DeviceManager.GetCamera(self.nIndex).GetValue("GainRaw")
            print("当前相机增益值为", nGain)

    def SendTrigger(self):
        print("相机", self.nIndex + 1, "发送软件触发指令，该指令只有SetTransMode为TRANS_TriggerSoftware时生效")
        DeviceManager.GetCamera(self.nIndex).SendTrigger()
    

    def StartCapture(self, transMode):
        print("设置相机", self.nIndex + 1, "传输模式为", transMode)
        self.bIsOpen = DeviceManager.GetCamera(self.nIndex).IsOpen()
        if self.bIsOpen:
            DeviceManager.GetCamera(self.nIndex).SetTransMode(transMode)
            DeviceManager.GetCamera(self.nIndex).StartCapture()
            bCapture = DeviceManager.GetCamera(self.nIndex).IsCapturing()
            if bCapture:
                print("启动相机传输成功")
            else:
                print("启动相机传输失败")
        else:
            print("打开相机失败")



    def GetImageBuffer(self, nWaitTime):
        print("相机", self.nIndex + 1, "获取图像时间超时时间(单位ms)为", nWaitTime, self.pImage)
        bSuccess = DeviceManager.GetCamera(self.nIndex).IsGrabSucceeded(nWaitTime)
        if bSuccess:
            DeviceManager.GetCamera(self.nIndex).GetRGB32Buffer(self.pImage, self.nWidth, self.nBit, 0)
        return bSuccess     

    def TestSoftWareTrigger(self):
        print("相机", self.nIndex, "开始软件触发测试")
        StartCapture(0, 3)
        for i in range(0, 10):
            SendTrigger(0)
            bSuccess = GetImageBuffer(0, 1000)
            i = i + 1
            if bSuccess:
                print("连续采集获取图像成功,当前图像ID为", i)
                DeviceManager.GetCamera(self.nIndex).SaveImage(pImage, ".\fairsion.bmp", self.nBit)
            else:
                print("连续采集获取图像超时,当前图像ID为", i)   
            
    def startCamera(self):
        if True:
            self.OpenCamera()
            self.SetExposure(3000)
            self.SetGain(32)
            
            Length = self.nWidth * self.nHeight
            self.raw_memory = bytearray(Length)
            ctypes_raw_type = (c_char * Length)
            ctypes_raw_memory = ctypes_raw_type.from_buffer(self.raw_memory)
            self.pImage = addressof(ctypes_raw_memory)
            
            # software trigger
            self.StartCapture(3)
            
    def grabImage(self):
        self.SendTrigger()
        bsuc = self.GetImageBuffer(1000)
        if bsuc :
            print("获取图片成功")
            # DeviceManager.GetCamera(self.nIndex).SaveImage(self.pImage, "fairsion.bmp", self.nBit)
        else :
            print("获取图片失败")