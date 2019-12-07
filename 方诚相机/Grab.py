print("fairsion单相机测试例程：")

from fairsionCamera import *
import win32com.client
from ctypes import *

print("获取实例化对象")
DeviceManager = win32com.client.DispatchEx('{939934F4-20DF-4866-A30D-0635F879725E}')

ImageDll = cdll.LoadLibrary("AuxiliaryCore_interface.dll")

nWidth = 0
nHeight = 0
nBit = 8

def InitManager():
    print("初始化设备管理对象，仅在程序入口处初始化一次即可")
    DeviceManager.Initialize()
    nCount = DeviceManager.GetCameraCount(2000)
    return nCount


def ReleaseManager():
    print("释放设备管理对象，仅在程序出口处调用一次即可，与Initialize对应")
    DeviceManager.Terminate()


def OpenCamera(nIndex):
    global nWidth
    global nHeight
    global nBit
    global pImage

    print("打开相机", nIndex + 1)
    Vendor = DeviceManager.GetCamera(nIndex).GetDeviceInfo().VendorName
    ModelName = DeviceManager.GetCamera(nIndex).GetDeviceInfo().ModelName
    SerialNumber = DeviceManager.GetCamera(nIndex).GetDeviceInfo().SerialNumber
    print("厂商名称", Vendor)
    print("设备名称", ModelName)
    print("设备序列号", SerialNumber)
    DeviceManager.GetCamera(nIndex).Open()
    bIsOpen = DeviceManager.GetCamera(nIndex).IsOpen()
    if bIsOpen:
        print("打开相机成功")
        nWidth = DeviceManager.GetCamera(nIndex).GetValue("Width")
        nHeight = DeviceManager.GetCamera(nIndex).GetValue("Height")
        nColor = DeviceManager.GetCamera(nIndex).GetValue("PixelColorFilter")
        if nColor != 0 :
            nBit = 24
        print("图像宽度", nWidth, "图像高度", nHeight, "像素位数", nBit)
    else:
        print("打开相机失败")


def SetExposure(nIndex, nValue):
    print("设置相机", nIndex + 1, "曝光时间值为", nValue)
    bIsOpen = DeviceManager.GetCamera(nIndex).IsOpen()
    if bIsOpen:
        DeviceManager.GetCamera(nIndex).SetValue("ExposureTimeRaw", nValue)
        nShuter = DeviceManager.GetCamera(nIndex).GetValue("ExposureTimeRaw")
        print("当前相机曝光时间值为", nShuter)


def SetGain(nIndex, nValue):
    print("设置相机", nIndex + 1, "增益值为", nValue)
    bIsOpen = DeviceManager.GetCamera(nIndex).IsOpen()
    if bIsOpen:
        DeviceManager.GetCamera(nIndex).SetValue("GainRaw", nValue)
        nGain = DeviceManager.GetCamera(nIndex).GetValue("GainRaw")
        print("当前相机增益值为", nGain)


def StartCapture(nIndex, transMode):
    print("设置相机", nIndex + 1, "传输模式为", transMode)
    bIsOpen = DeviceManager.GetCamera(nIndex).IsOpen()
    if bIsOpen:
        DeviceManager.GetCamera(nIndex).SetTransMode(transMode)
        DeviceManager.GetCamera(nIndex).StartCapture()
        bCapture = DeviceManager.GetCamera(nIndex).IsCapturing()
        if bCapture:
            print("启动相机传输成功")
        else:
            print("启动相机传输失败")


def SendTrigger(nIndex):
    print("相机", nIndex + 1, "发送软件触发指令，该指令只有SetTransMode为TRANS_TriggerSoftware时生效")
    DeviceManager.GetCamera(nIndex).SendTrigger()


def GetImageBuffer(nIndex, nWaitTime):
    global nWidth
    global nHeight
    global nBit
    global pImage

    print("相机", nIndex + 1, "获取图像时间超时时间(单位ms)为", nWaitTime, pImage)
    bSuccess = DeviceManager.GetCamera(nIndex).IsGrabSucceeded(nWaitTime)
    if bSuccess:
        DeviceManager.GetCamera(nIndex).GetRGB32Buffer(pImage, nWidth, nBit, 0)
    return bSuccess


def TestContinuoutAcq(nIndex):
    print("相机", nIndex, "开始连续采集测试")
    global nWidth
    global nHeight
    global nBit
    global pImage

    StartCapture(0, 2)
    for i in range(0, 10):
        bSuccess = GetImageBuffer(0, 1000)
        i = i + 1
        if bSuccess:
            print("连续采集获取图像成功,当前图像ID为", i)
            DeviceManager.GetCamera(nIndex).SaveImage(pImage, "fairsion.bmp", nBit)
        else:
            print("连续采集获取图像超时,当前图像ID为", i)


def TestSoftWareTrigger(nIndex):
    print("相机", nIndex, "开始软件触发测试")
    StartCapture(0, 3)
    for i in range(0, 10):
        SendTrigger(0)
        bSuccess = GetImageBuffer(0, 1000)
        i = i + 1
        if bSuccess:
            print("连续采集获取图像成功,当前图像ID为", i)
            DeviceManager.GetCamera(nIndex).SaveImage(pImage, ".\fairsion.bmp", nBit)
        else:
            print("连续采集获取图像超时,当前图像ID为", i)


def CloseCamera(nIndex):
    print("关闭相机", nIndex + 1)
    DeviceManager.GetCamera(nIndex).StopCapture()
    DeviceManager.GetCamera(nIndex).Close()


nCameraCount = InitManager()
print("当前相机数目为：", nCameraCount)

if nCameraCount > 0:
    OpenCamera(0)
    SetExposure(0, 3000)
    SetGain(0, 32)

    print("width", nWidth, "height", nHeight, "bit", nBit)
    if nBit == 24 :
        Length = nWidth * nHeight * 3
    else:
        Length = nWidth * nHeight

    raw_memory = bytearray(Length)
    ctypes_raw_type = (c_char * Length)
    ctypes_raw_memory = ctypes_raw_type.from_buffer(raw_memory)
    pImage = addressof(ctypes_raw_memory)

    TestContinuoutAcq(0)
    TestSoftWareTrigger(0)
    CloseCamera(0)

ReleaseManager()
