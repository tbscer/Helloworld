# -*-coding:utf-8-*-
# Created by makepy.py version 0.5.01
# By python version 3.6.7 (v3.6.7:6ec5cf24b7, Oct 20 2018, 12:45:02) [MSC v.1900 32 bit (Intel)]
# From type library 'fairsionCamera.dll'
# On Wed Dec 12 14:56:32 2018
'fairsionCamera 1.0'
makepy_version = '0.5.01'
python_version = 0x30607f0

import win32com.client.CLSIDToClass, pythoncom, pywintypes
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch

# The following 3 lines may need tweaking for the particular server
# Candidates are pythoncom.Missing, .Empty and .ArgNotFound
defaultNamedOptArg=pythoncom.Empty
defaultNamedNotOptArg=pythoncom.Empty
defaultUnnamedArg=pythoncom.Empty

CLSID = IID('{86134CBD-2C20-4B54-BC68-576155BC42A0}')
MajorVersion = 1
MinorVersion = 0
LibraryFlags = 8
LCID = 0x0

class constants:
	Camera_intfIBoolean           =3          # from enum _emCameraInterfaceType
	Camera_intfICategory          =8          # from enum _emCameraInterfaceType
	Camera_intfICommand           =4          # from enum _emCameraInterfaceType
	Camera_intfIEnumEntry         =10         # from enum _emCameraInterfaceType
	Camera_intfIEnumeration       =9          # from enum _emCameraInterfaceType
	Camera_intfIFloat             =5          # from enum _emCameraInterfaceType
	Camera_intfIInteger           =2          # from enum _emCameraInterfaceType
	Camera_intfIPort              =11         # from enum _emCameraInterfaceType
	Camera_intfIRegister          =7          # from enum _emCameraInterfaceType
	Camera_intfIString            =6          # from enum _emCameraInterfaceType
	Camera_intfIValue             =1          # from enum _emCameraInterfaceType
	Camera_intfUnknow             =0          # from enum _emCameraInterfaceType
	AM_CycleDetectAccesMode       =6          # from enum _emCameraParamAccessMode
	AM_NA                         =1          # from enum _emCameraParamAccessMode
	AM_NI                         =0          # from enum _emCameraParamAccessMode
	AM_RO                         =3          # from enum _emCameraParamAccessMode
	AM_RW                         =4          # from enum _emCameraParamAccessMode
	AM_UndefinedAccesMode         =5          # from enum _emCameraParamAccessMode
	AM_WO                         =2          # from enum _emCameraParamAccessMode
	V_Beginner                    =0          # from enum _emCameraParamVisibility
	V_Expert                      =1          # from enum _emCameraParamVisibility
	V_Guru                        =2          # from enum _emCameraParamVisibility
	V_Invisible                   =3          # from enum _emCameraParamVisibility
	V_UndefinedVisibility         =99         # from enum _emCameraParamVisibility
	Camera_1394                   =3          # from enum _emCameraType
	Camera_Any                    =0          # from enum _emCameraType
	Camera_CameraLink             =4          # from enum _emCameraType
	Camera_Gige                   =1          # from enum _emCameraType
	Camera_Usb                    =2          # from enum _emCameraType
	_AUTO_IP                      =4          # from enum _emGige_IPConfig_Options
	_DHCP_IP                      =6          # from enum _emGige_IPConfig_Options
	_STATIC_IP                    =5          # from enum _emGige_IPConfig_Options
	TRANS_Continuous              =2          # from enum _emTrans_Mode
	TRANS_MultiFrame              =1          # from enum _emTrans_Mode
	TRANS_SingleFrame             =0          # from enum _emTrans_Mode
	TRANS_TriggerHardware         =4          # from enum _emTrans_Mode
	TRANS_TriggerSoftware         =3          # from enum _emTrans_Mode
	Full_Speed                    =1          # from enum _emUsb_Trans_Speed
	High_Speed                    =2          # from enum _emUsb_Trans_Speed
	Low_Speed                     =0          # from enum _emUsb_Trans_Speed
	SuperSpeed                    =3          # from enum _emUsb_Trans_Speed

from win32com.client import DispatchBaseClass
class ICamera(DispatchBaseClass):
	'ICamera �ӿ�'
	CLSID = IID('{58B62995-823D-4AC8-9A04-5A839BA64D52}')
	coclass_clsid = IID('{1DD5D781-3E0C-4477-90C3-392A682B6452}')

	def AutoBalance(self):
		'ʹ���Զ���ƽ���㷨'
		return self._oleobj_.InvokeTypes(25, LCID, 1, (24, 0), (),)

	def Close(self):
		'�ر����'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (24, 0), (),)

	def CopyImageBuffer(self, pDestBuffer=defaultNamedNotOptArg, nLength=defaultNamedNotOptArg):
		'������ǰͼ�񻺳���'
		return self._oleobj_.InvokeTypes(35, LCID, 1, (11, 0), ((3, 1), (3, 1)),pDestBuffer
			, nLength)

	def Destory(self):
		'����������Դ'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (24, 0), (),)

	def DisplayPropertiesWnd(self):
		'��ʾ������Դ���'
		return self._oleobj_.InvokeTypes(64, LCID, 1, (24, 0), (),)

	def EnableDenoising(self, bEnable=defaultNamedNotOptArg):
		'ͼ����ʹ��'
		return self._oleobj_.InvokeTypes(37, LCID, 1, (24, 0), ((11, 1),),bEnable
			)

	def GetAccessMode(self, strName=defaultNamedNotOptArg):
		'��ȡ��ǰ�����ķ���ģʽ'
		return self._oleobj_.InvokeTypes(60, LCID, 1, (3, 0), ((8, 1),),strName
			)

	def GetBuffer(self):
		'��ȡ��ǰ��Чͼ�����ݵ�ַ'
		return self._ApplyTypes_(11, 1, (16401, 0), (), 'GetBuffer', None,)

	def GetChildCount(self, strName=defaultNamedNotOptArg):
		'��ȡ��ǰ������������Ŀ'
		return self._oleobj_.InvokeTypes(51, LCID, 1, (3, 0), ((8, 1),),strName
			)

	def GetChildName(self, strName=defaultNamedNotOptArg, nIndex=defaultNamedNotOptArg):
		'��ȡ��ǰ������Ӧ�����������������'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(52, LCID, 1, (8, 0), ((8, 1), (3, 1)),strName
			, nIndex)

	# Result is of type IDebugInfo
	def GetDebugInfo(self):
		'��ȡ������Ϣ'
		ret = self._oleobj_.InvokeTypes(36, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetDebugInfo', '{F79A0746-83FD-4A37-A47F-B5E14B2D4915}')
		return ret

	def GetDescription(self, strName=defaultNamedNotOptArg):
		'��ȡ��ǰ������������Ϣ'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(55, LCID, 1, (8, 0), ((8, 1),),strName
			)

	# Result is of type IDeviceInfo
	def GetDeviceInfo(self):
		'��ȡ�豸��Ϣ'
		ret = self._oleobj_.InvokeTypes(24, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetDeviceInfo', '{3D3A2E09-310D-45CA-A4DD-97EDFD156E6D}')
		return ret

	def GetDeviceName(self, strName=defaultNamedNotOptArg):
		'��ȡ��ǰ�������豸����'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(57, LCID, 1, (8, 0), ((8, 1),),strName
			)

	def GetDisplayName(self, strName=defaultNamedNotOptArg):
		'��ȡ��ǰ��������ʾ����'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(56, LCID, 1, (8, 0), ((8, 1),),strName
			)

	def GetErrorImage(self):
		'��ȡ����ͼ��ָ��'
		return self._ApplyTypes_(38, 1, (16401, 0), (), 'GetErrorImage', None,)

	def GetFInc(self, strName=defaultNamedNotOptArg):
		'��ȡ�����Ͳ�����Ԫ'
		return self._oleobj_.InvokeTypes(46, LCID, 1, (4, 0), ((8, 1),),strName
			)

	def GetFMax(self, strName=defaultNamedNotOptArg):
		'��ȡ�����Ͳ������ֵ'
		return self._oleobj_.InvokeTypes(45, LCID, 1, (4, 0), ((8, 1),),strName
			)

	def GetFMin(self, strName=defaultNamedNotOptArg):
		'��ȡ�����Ͳ�����Сֵ'
		return self._oleobj_.InvokeTypes(44, LCID, 1, (4, 0), ((8, 1),),strName
			)

	def GetFValue(self, strName=defaultNamedNotOptArg):
		'��ȡ�����Ͳ���ֵ'
		return self._oleobj_.InvokeTypes(42, LCID, 1, (4, 0), ((8, 1),),strName
			)

	def GetGenICamObj(self):
		'��ȡGenICam����'
		return self._ApplyTypes_(61, 1, (16387, 0), (), 'GetGenICamObj', None,)

	def GetInc(self, szValue=defaultNamedNotOptArg):
		'��ȡָ������������Ԫ'
		return self._oleobj_.InvokeTypes(20, LCID, 1, (3, 0), ((8, 1),),szValue
			)

	def GetInterfaceType(self, strName=defaultNamedNotOptArg):
		'��ȡ�����ӿ����ͣ��ɷ����û������жϲ�ѡ����Ӧ���͵ĺ���'
		return self._oleobj_.InvokeTypes(62, LCID, 1, (3, 0), ((8, 1),),strName
			)

	def GetInterfaceTypeName(self, strName=defaultNamedNotOptArg):
		'��ȡ�����������ı�'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(63, LCID, 1, (8, 0), ((8, 1),),strName
			)

	def GetMax(self, szValue=defaultNamedNotOptArg):
		'��ȡָ���������ֵ'
		return self._oleobj_.InvokeTypes(19, LCID, 1, (3, 0), ((8, 1),),szValue
			)

	def GetMin(self, szValue=defaultNamedNotOptArg):
		'��ȡָ��������Сֵ'
		return self._oleobj_.InvokeTypes(18, LCID, 1, (3, 0), ((8, 1),),szValue
			)

	def GetParentName(self, strName=defaultNamedNotOptArg):
		'��ȡ��ǰ�����ĸ�������'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(53, LCID, 1, (8, 0), ((8, 1),),strName
			)

	def GetRGB32Buffer(self, LVImagePtr=defaultNamedNotOptArg, LVLineWidth=defaultNamedNotOptArg, LVPixelSize=defaultNamedNotOptArg, AlgorithmType=defaultNamedNotOptArg):
		'��ȡRGB32ͼ�񻺳���'
		return self._oleobj_.InvokeTypes(33, LCID, 1, (3, 0), ((3, 1), (3, 1), (3, 0), (3, 1)),LVImagePtr
			, LVLineWidth, LVPixelSize, AlgorithmType)

	def GetRGB32BufferEx(self, LVImagePtr=defaultNamedNotOptArg, LVLineWidth=defaultNamedNotOptArg, LVPixelSize=defaultNamedNotOptArg, AlgorithmType=defaultNamedNotOptArg):
		'64λ��ַ�����ȡ���ͼ������'
		return self._oleobj_.InvokeTypes(65, LCID, 1, (3, 0), ((21, 1), (3, 1), (3, 1), (3, 1)),LVImagePtr
			, LVLineWidth, LVPixelSize, AlgorithmType)

	def GetRGBBuffer(self, usPixelSize=defaultNamedNotOptArg, AlgorithmType=defaultNamedNotOptArg):
		'��ȡRGBͼ�񻺳���'
		return self._ApplyTypes_(34, 1, (16401, 0), ((3, 1), (3, 1)), 'GetRGBBuffer', None,usPixelSize
			, AlgorithmType)

	def GetSelector(self, szValue=defaultNamedNotOptArg):
		'��ȡѡ������ֵ'
		return self._oleobj_.InvokeTypes(27, LCID, 1, (3, 0), ((8, 1),),szValue
			)

	def GetSelectorStr(self, strName=defaultNamedNotOptArg):
		'��ȡѡ������ѡֵ���ַ�����'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(50, LCID, 1, (8, 0), ((8, 1),),strName
			)

	def GetStrValue(self, strName=defaultNamedNotOptArg):
		'��ȡ�ַ��Ͳ���ֵ'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(47, LCID, 1, (8, 0), ((8, 1),),strName
			)

	def GetToolTip(self, strName=defaultNamedNotOptArg):
		'��ȡ��ǰ��������ʾ�ı�'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(54, LCID, 1, (8, 0), ((8, 1),),strName
			)

	def GetTransMode(self):
		'��ȡ��ǰ����ģʽ'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (3, 0), (),)

	def GetUnit(self, strName=defaultNamedNotOptArg):
		'��ȡ��ǰ�����ĵ�λ����'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(58, LCID, 1, (8, 0), ((8, 1),),strName
			)

	def GetUserContext(self):
		'��ȡ�û�������ָ��'
		return self._ApplyTypes_(28, 1, (16401, 0), (), 'GetUserContext', None,)

	def GetValue(self, szValue=defaultNamedNotOptArg):
		'��ȡָ��������ֵ'
		return self._oleobj_.InvokeTypes(15, LCID, 1, (3, 0), ((8, 1),),szValue
			)

	def GetVisibility(self, strName=defaultNamedNotOptArg):
		'��ȡ��ǰ�����Ŀɼ���'
		return self._oleobj_.InvokeTypes(59, LCID, 1, (3, 0), ((8, 1),),strName
			)

	def GrapOne(self):
		'��֡�ɼ�'
		return self._oleobj_.InvokeTypes(41, LCID, 1, (24, 0), (),)

	def IsAvailable(self, szValue=defaultNamedNotOptArg):
		'ָ�������Ƿ���Ч'
		return self._oleobj_.InvokeTypes(17, LCID, 1, (11, 0), ((8, 1),),szValue
			)

	def IsCapturing(self):
		'�Ƿ����ڲɼ�'
		return self._oleobj_.InvokeTypes(30, LCID, 1, (11, 0), (),)

	def IsGrabSucceeded(self, nWaitTime=defaultNamedNotOptArg):
		'�ɼ��Ƿ�ɹ�'
		return self._oleobj_.InvokeTypes(31, LCID, 1, (11, 0), ((3, 0),),nWaitTime
			)

	def IsOnline(self):
		'����Ƿ�����'
		return self._oleobj_.InvokeTypes(29, LCID, 1, (11, 0), (),)

	def IsOpen(self):
		'����Ƿ��'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (11, 0), (),)

	def LoadConfigure(self, szFileName=defaultNamedNotOptArg):
		'���������ļ�'
		return self._oleobj_.InvokeTypes(23, LCID, 1, (24, 0), ((8, 1),),szFileName
			)

	def Open(self):
		'�����'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (24, 0), (),)

	def ReadMemory(self, ulAddress=defaultNamedNotOptArg, ulLength=defaultNamedNotOptArg):
		'������ڴ�'
		return self._ApplyTypes_(39, 1, (16401, 0), ((21, 1), (19, 1)), 'ReadMemory', None,ulAddress
			, ulLength)

	def ReadRegister(self, ulAddress=defaultNamedNotOptArg, ulLength=defaultNamedNotOptArg):
		'���Ĵ���'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(13, LCID, 1, (8, 0), ((21, 1), (19, 1)),ulAddress
			, ulLength)

	def SaveConfigure(self, szFileName=defaultNamedNotOptArg):
		'���������ļ�'
		return self._oleobj_.InvokeTypes(22, LCID, 1, (24, 0), ((8, 1),),szFileName
			)

	def SaveImage(self, ImageAddress=defaultNamedNotOptArg, strImageName=defaultNamedNotOptArg, nPixelSize=defaultNamedNotOptArg):
		'����ͼ��'
		return self._oleobj_.InvokeTypes(66, LCID, 1, (24, 0), ((20, 1), (8, 1), (3, 1)),ImageAddress
			, strImageName, nPixelSize)

	def SendTrigger(self):
		'���ʹ����ź�'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (24, 0), (),)

	def SetBufferCount(self, nCount=defaultNamedNotOptArg):
		'���û���ش�С'
		return self._oleobj_.InvokeTypes(21, LCID, 1, (24, 0), ((3, 1),),nCount
			)

	def SetFValue(self, strName=defaultNamedNotOptArg, fValue=defaultNamedNotOptArg):
		'���ø����Ͳ���ֵ'
		return self._oleobj_.InvokeTypes(43, LCID, 1, (24, 0), ((8, 1), (4, 1)),strName
			, fValue)

	def SetSelector(self, szValue=defaultNamedNotOptArg, nValue=defaultNamedNotOptArg):
		'����ѡ����'
		return self._oleobj_.InvokeTypes(26, LCID, 1, (24, 0), ((8, 1), (3, 1)),szValue
			, nValue)

	def SetSelectorStr(self, strName=defaultNamedNotOptArg, strValue=defaultNamedNotOptArg):
		'ͨ���ַ�����ʽ����ѡ������ֵ'
		return self._oleobj_.InvokeTypes(49, LCID, 1, (24, 0), ((8, 1), (8, 1)),strName
			, strValue)

	def SetStrValue(self, strName=defaultNamedNotOptArg, strValue=defaultNamedNotOptArg):
		'�����ַ��Ͳ���ֵ'
		return self._oleobj_.InvokeTypes(48, LCID, 1, (24, 0), ((8, 1), (8, 1)),strName
			, strValue)

	def SetTransMode(self, TransMode=defaultNamedNotOptArg):
		'���ô���ģʽ'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (24, 0), ((3, 1),),TransMode
			)

	def SetUserContext(self, pUserContext=defaultNamedNotOptArg):
		'�����û�������'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (24, 0), ((16401, 1),),pUserContext
			)

	def SetValue(self, szValue=defaultNamedNotOptArg, nValue=defaultNamedNotOptArg):
		'����ָ��������ֵ'
		return self._oleobj_.InvokeTypes(16, LCID, 1, (24, 0), ((8, 1), (3, 1)),szValue
			, nValue)

	def StartCapture(self):
		'��ʼ���ݲɼ�'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (24, 0), (),)

	def StopCapture(self):
		'ֹͣ���ݲɼ�'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (24, 0), (),)

	def WriteMemroy(self, ulAddress=defaultNamedNotOptArg, ulLength=defaultNamedNotOptArg, pData=defaultNamedNotOptArg):
		'д����ڴ�'
		return self._oleobj_.InvokeTypes(40, LCID, 1, (24, 0), ((21, 1), (19, 1), (16401, 1)),ulAddress
			, ulLength, pData)

	def WriteRegister(self, ulAddress=defaultNamedNotOptArg, ulLength=defaultNamedNotOptArg, pData=defaultNamedNotOptArg):
		'д�Ĵ���'
		return self._oleobj_.InvokeTypes(14, LCID, 1, (24, 0), ((21, 1), (19, 0), (8, 1)),ulAddress
			, ulLength, pData)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ICameraLinkDeviceInfo(DispatchBaseClass):
	'ICameraLinkDeviceInfo �ӿ�'
	CLSID = IID('{C4D650B1-73A1-41D8-813B-FD34F624CCB2}')
	coclass_clsid = IID('{A1587EFE-6BB9-4E01-8BEC-F287654B6D5E}')

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IDebugInfo(DispatchBaseClass):
	'IDebugInfo �ӿ�'
	CLSID = IID('{F79A0746-83FD-4A37-A47F-B5E14B2D4915}')
	coclass_clsid = IID('{D59898B1-79CD-45A0-9115-14DFB35F658C}')

	def GetCurrentBufferCount(self):
		'��ȡ��ǰ����������'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (19, 0), (),)

	def GetCurrentCallBackEnterNumber(self):
		'��ȡ��ǰ�ص�����ִ�д���'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (19, 0), (),)

	def GetCurrentCoverImageNumber(self):
		'��ȡ��ǰ�Ѹ���ͼ����Ŀ'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (19, 0), (),)

	def GetCurrentDeviceImageNumber(self):
		'��ȡ��ǰ�豸ͼ����'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (19, 0), (),)

	def GetCurrentDropImageNumber(self):
		'��ȡ��ǰ�쳣ͼ����Ŀ'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (19, 0), (),)

	def GetCurrentDropPacketNumber(self):
		'��ȡ��ǰ���䶪����Ŀ'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (19, 0), (),)

	def GetCurrentEmptylistSize(self):
		'��ȡ��ǰ�ն��л�������Ŀ'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (19, 0), (),)

	def GetCurrentFulllistSize(self):
		'��ȡ��ǰ�����л�������Ŀ'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (19, 0), (),)

	def GetCurrentImageNumber(self):
		'��ȡ��ǰͼ����Ŀ'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (19, 0), (),)

	def GetCurrentImagelistSize(self):
		'��ȡ��ǰͼ����л�������Ŀ'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (19, 0), (),)

	def GetCurrentResendCount(self):
		'��ȡ��ǰ�ط�����Ŀ'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (19, 0), (),)

	def GetCurrentUserlistSize(self):
		'��ȡ��ǰ�û����л�������Ŀ'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (19, 0), (),)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IDeviceInfo(DispatchBaseClass):
	'IDeviceInfo �ӿ�'
	CLSID = IID('{3D3A2E09-310D-45CA-A4DD-97EDFD156E6D}')
	coclass_clsid = IID('{6B883B26-98C5-4E69-A0D2-37A55D6FA1FB}')

	# Result is of type ICameraLinkDeviceInfo
	def GetCameraLinkInfo(self):
		'��ȡCameraLink��Ϣ�ӿڶ���'
		ret = self._oleobj_.InvokeTypes(20, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetCameraLinkInfo', '{C4D650B1-73A1-41D8-813B-FD34F624CCB2}')
		return ret

	def GetCameraType(self):
		'��ȡ�������'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (3, 0), (),)

	# Result is of type IGigeDeviceInfo
	def GetGigeInfo(self):
		'��ȡGige��Ϣ�ӿڶ���'
		ret = self._oleobj_.InvokeTypes(17, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetGigeInfo', '{D4904E55-39D2-490D-A5DF-ADE372FBCE55}')
		return ret

	# Result is of type IIEEEDeviceInfo
	def GetIEEEInfo(self):
		'��ȡIEEE��Ϣ�ӿڶ���'
		ret = self._oleobj_.InvokeTypes(19, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetIEEEInfo', '{D9172DBC-6D72-46B4-BDD9-218D69D255E0}')
		return ret

	# Result is of type IUsbDeviceInfo
	def GetUsbInfo(self):
		'��ȡusb��Ϣ�ӿڶ���'
		ret = self._oleobj_.InvokeTypes(18, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetUsbInfo', '{039F2506-34D0-49DE-AEFE-E6F0485455A0}')
		return ret

	def IsModelNameAvailable(self):
		'�ͺ������Ƿ���Ч'
		return self._oleobj_.InvokeTypes(13, LCID, 1, (11, 0), (),)

	def IsSerialNumberAvailable(self):
		'������к��Ƿ���Ч'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (11, 0), (),)

	def IsUserIDAvailable(self):
		'�û�ID�Ƿ���Ч'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (11, 0), (),)

	def IsVendorNameAvailable(self):
		'���������Ƿ���Ч'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (11, 0), (),)

	def IsVersionAvailable(self):
		'�豸�汾�Ƿ���Ч'
		return self._oleobj_.InvokeTypes(16, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"ManufactureInfo": (27, 2, (8, 0), (), "ManufactureInfo", None),
		"ModelName": (25, 2, (8, 0), (), "ModelName", None),
		"SerialNumber": (22, 2, (8, 0), (), "SerialNumber", None),
		"UserID": (23, 2, (8, 0), (), "UserID", None),
		"VendorName": (24, 2, (8, 0), (), "VendorName", None),
		"Version": (26, 2, (8, 0), (), "Version", None),
	}
	_prop_map_put_ = {
		"ManufactureInfo": ((27, LCID, 4, 0),()),
		"ModelName": ((25, LCID, 4, 0),()),
		"SerialNumber": ((22, LCID, 4, 0),()),
		"UserID": ((23, LCID, 4, 0),()),
		"VendorName": ((24, LCID, 4, 0),()),
		"Version": ((26, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IDeviceManager(DispatchBaseClass):
	'IDeviceManager �ӿ�'
	CLSID = IID('{D6AE9517-8BE3-4C9A-A45D-435BF9603263}')
	coclass_clsid = IID('{939934F4-20DF-4866-A30D-0635F879725E}')

	# Result is of type ICamera
	def GetCamera(self, nIndex=defaultNamedNotOptArg):
		'ͨ��������ȡ�������'
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), ((3, 1),),nIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetCamera', '{58B62995-823D-4AC8-9A04-5A839BA64D52}')
		return ret

	# Result is of type ICamera
	def GetCameraByName(self, szCameraName=defaultNamedNotOptArg):
		'ͨ��������кŻ��û��Զ������ƴ����'
		ret = self._oleobj_.InvokeTypes(5, LCID, 1, (9, 0), ((8, 1),),szCameraName
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetCameraByName', '{58B62995-823D-4AC8-9A04-5A839BA64D52}')
		return ret

	def GetCameraCount(self, nWaitTime=defaultNamedNotOptArg):
		'��ȡ��ǰ�����Ŀ'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (3, 0), ((3, 1),),nWaitTime
			)

	def GetError(self, nError=defaultNamedNotOptArg):
		'��ȡָ����������Ϣ'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(7, LCID, 1, (8, 0), ((3, 1),),nError
			)

	def Initialize(self):
		'��ʼ�����������Դ'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (24, 0), (),)

	def ReleaseCamera(self, pCamera=defaultNamedNotOptArg):
		'�黹���ͷ������Դ'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (24, 0), ((9, 1),),pCamera
			)

	def Terminate(self):
		'�������������Դ'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IGigeDeviceInfo(DispatchBaseClass):
	'IGigeDeviceInfo �ӿ�'
	CLSID = IID('{D4904E55-39D2-490D-A5DF-ADE372FBCE55}')
	coclass_clsid = IID('{A2CA86D9-92BC-460C-838F-BB3FF699E2BB}')

	def AutoSetIP(self):
		'�Զ�����IP'
		return self._oleobj_.InvokeTypes(23, LCID, 1, (24, 0), (),)

	def GetDeviceMode(self):
		'��ȡ�豸ģʽ'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (3, 0), (),)

	def GetIPConfigOptions(self):
		'��ȡIP����ѡ��'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (19, 0), (),)

	def GetMacHigh(self):
		'��ȡMAC��ַ��λ'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (18, 0), (),)

	def GetMacLow(self):
		'��ȡMAC��ַ��λ'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (19, 0), (),)

	def GetNICLocalName(self):
		'��ȡ������������'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(21, LCID, 1, (8, 0), (),)

	def GetNetIP(self):
		'��ȡ��������IP'
		return self._oleobj_.InvokeTypes(15, LCID, 1, (19, 0), (),)

	def GetNetMask(self):
		'��ȡ����������������'
		return self._oleobj_.InvokeTypes(16, LCID, 1, (19, 0), (),)

	def GetSpecVerMajor(self):
		'��ȡЭ�����汾��'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (3, 0), (),)

	def GetSpecVerMinor(self):
		'��ȡЭ���Ӱ汾��'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (3, 0), (),)

	def IsCurrentIPValid(self, ulAddress=defaultNamedNotOptArg):
		'������IP�Ƿ���Ч'
		return self._oleobj_.InvokeTypes(22, LCID, 1, (11, 0), ((19, 1),),ulAddress
			)

	_prop_map_get_ = {
		"DefaultGateway": (20, 2, (19, 0), (), "DefaultGateway", None),
		"IP": (18, 2, (19, 0), (), "IP", None),
		"IPConfigCurrent": (17, 2, (3, 0), (), "IPConfigCurrent", None),
		"SubnetMask": (19, 2, (19, 0), (), "SubnetMask", None),
	}
	_prop_map_put_ = {
		"DefaultGateway": ((20, LCID, 4, 0),()),
		"IP": ((18, LCID, 4, 0),()),
		"IPConfigCurrent": ((17, LCID, 4, 0),()),
		"SubnetMask": ((19, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IIEEEDeviceInfo(DispatchBaseClass):
	'IIEEEDeviceInfo �ӿ�'
	CLSID = IID('{D9172DBC-6D72-46B4-BDD9-218D69D255E0}')
	coclass_clsid = IID('{05B1890F-898B-4BF1-9FDB-9F82E8684776}')

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMsgNotice(DispatchBaseClass):
	'IMsgNotice �ӿ�'
	CLSID = IID('{1FB878F5-4C89-43DA-A438-EE3AF0D2B344}')
	coclass_clsid = IID('{8F116AA1-F23A-4B62-A344-9B463C0BDE2F}')

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IUsbDeviceInfo(DispatchBaseClass):
	'IUsbDeviceInfo �ӿ�'
	CLSID = IID('{039F2506-34D0-49DE-AEFE-E6F0485455A0}')
	coclass_clsid = IID('{31751075-AB5B-4A29-8331-4E9672F98641}')

	def IsUsb3(self):
		'�Ƿ���usb3�豸'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (11, 0), (),)

	_prop_map_get_ = {
		"Speed": (1, 2, (3, 0), (), "Speed", None),
	}
	_prop_map_put_ = {
		"Speed": ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _IMsgNoticeEvents:
	'_IMsgNoticeEvents �ӿ�'
	CLSID = CLSID_Sink = IID('{2DBD29C5-42BE-4886-B8CF-682DC7B18EE1}')
	coclass_clsid = IID('{8F116AA1-F23A-4B62-A344-9B463C0BDE2F}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnImageSuccess",
		        2 : "OnCameraOnline",
		        3 : "OnCameraDrop",
		        4 : "OnCameraDestory",
		        5 : "OnAutoBalanceEnd",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnImageSuccess(self, pCamera=defaultNamedNotOptArg):
#		'ͼ��ɹ�ʱ��'
#	def OnCameraOnline(self, pCamera=defaultNamedNotOptArg):
#		'�������'
#	def OnCameraDrop(self, pCamera=defaultNamedNotOptArg):
#		'�������'
#	def OnCameraDestory(self, pCamera=defaultNamedNotOptArg):
#		'�����Դ����'
#	def OnAutoBalanceEnd(self, pCamera=defaultNamedNotOptArg):
#		'�Զ���ƽ����ڽ���'


from win32com.client import CoClassBaseClass
# This CoClass is known by the name 'fairsionCamera.Camera.1'
class Camera(CoClassBaseClass): # A CoClass
	# Camera Class
	CLSID = IID('{1DD5D781-3E0C-4477-90C3-392A682B6452}')
	coclass_sources = [
		_IMsgNoticeEvents,
	]
	default_source = _IMsgNoticeEvents
	coclass_interfaces = [
		ICamera,
	]
	default_interface = ICamera

# This CoClass is known by the name 'fairsionCamera.CameraLinkDeviceInfo.1'
class CameraLinkDeviceInfo(CoClassBaseClass): # A CoClass
	# CameraLinkDeviceInfo Class
	CLSID = IID('{A1587EFE-6BB9-4E01-8BEC-F287654B6D5E}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ICameraLinkDeviceInfo,
	]
	default_interface = ICameraLinkDeviceInfo

# This CoClass is known by the name 'fairsionCamera.DebugInfo.1'
class DebugInfo(CoClassBaseClass): # A CoClass
	# DebugInfo Class
	CLSID = IID('{D59898B1-79CD-45A0-9115-14DFB35F658C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IDebugInfo,
	]
	default_interface = IDebugInfo

# This CoClass is known by the name 'fairsionCamera.DeviceInfo.1'
class DeviceInfo(CoClassBaseClass): # A CoClass
	# DeviceInfo Class
	CLSID = IID('{6B883B26-98C5-4E69-A0D2-37A55D6FA1FB}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IDeviceInfo,
	]
	default_interface = IDeviceInfo

# This CoClass is known by the name 'fairsionCamera.DeviceManager.1'
class DeviceManager(CoClassBaseClass): # A CoClass
	# DeviceManager Class
	CLSID = IID('{939934F4-20DF-4866-A30D-0635F879725E}')
	coclass_sources = [
		_IMsgNoticeEvents,
	]
	default_source = _IMsgNoticeEvents
	coclass_interfaces = [
		IDeviceManager,
	]
	default_interface = IDeviceManager

# This CoClass is known by the name 'fairsionCamera.GigeDeviceInfo.1'
class GigeDeviceInfo(CoClassBaseClass): # A CoClass
	# GigeDeviceInfo Class
	CLSID = IID('{A2CA86D9-92BC-460C-838F-BB3FF699E2BB}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IGigeDeviceInfo,
	]
	default_interface = IGigeDeviceInfo

# This CoClass is known by the name 'fairsionCamera.IEEEDeviceInfo.1'
class IEEEDeviceInfo(CoClassBaseClass): # A CoClass
	# IEEEDeviceInfo Class
	CLSID = IID('{05B1890F-898B-4BF1-9FDB-9F82E8684776}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IIEEEDeviceInfo,
	]
	default_interface = IIEEEDeviceInfo

# This CoClass is known by the name 'fairsionCamera.MsgNotice.1'
class MsgNotice(CoClassBaseClass): # A CoClass
	# MsgNotice Class
	CLSID = IID('{8F116AA1-F23A-4B62-A344-9B463C0BDE2F}')
	coclass_sources = [
		_IMsgNoticeEvents,
	]
	default_source = _IMsgNoticeEvents
	coclass_interfaces = [
		IMsgNotice,
	]
	default_interface = IMsgNotice

# This CoClass is known by the name 'fairsionCamera.UsbDeviceInfo.1'
class UsbDeviceInfo(CoClassBaseClass): # A CoClass
	# UsbDeviceInfo Class
	CLSID = IID('{31751075-AB5B-4A29-8331-4E9672F98641}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IUsbDeviceInfo,
	]
	default_interface = IUsbDeviceInfo

ICamera_vtables_dispatch_ = 1
ICamera_vtables_ = [
	(( 'Open' , ), 1, (1, (), [ ], 1 , 1 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Close' , ), 2, (2, (), [ ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'SetUserContext' , 'pUserContext' , ), 4, (4, (), [ (16401, 1, None, None) , ], 1 , 1 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'IsOpen' , 'bOpen' , ), 5, (5, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'SetTransMode' , 'TransMode' , ), 6, (6, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'GetTransMode' , 'pTransMode' , ), 7, (7, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'StartCapture' , ), 8, (8, (), [ ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'StopCapture' , ), 9, (9, (), [ ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'SendTrigger' , ), 10, (10, (), [ ], 1 , 1 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'GetBuffer' , 'pImageBuffer' , ), 11, (11, (), [ (16401, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Destory' , ), 12, (12, (), [ ], 1 , 1 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( 'ReadRegister' , 'ulAddress' , 'ulLength' , 'pData' , ), 13, (13, (), [ 
			 (21, 1, None, None) , (19, 1, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'WriteRegister' , 'ulAddress' , 'ulLength' , 'pData' , ), 14, (14, (), [ 
			 (21, 1, None, None) , (19, 0, None, None) , (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( 'GetValue' , 'szValue' , 'nValue' , ), 15, (15, (), [ (8, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'SetValue' , 'szValue' , 'nValue' , ), 16, (16, (), [ (8, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( 'IsAvailable' , 'szValue' , 'bIsAvailable' , ), 17, (17, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'GetMin' , 'szValue' , 'nValue' , ), 18, (18, (), [ (8, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( 'GetMax' , 'szValue' , 'nValue' , ), 19, (19, (), [ (8, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'GetInc' , 'szValue' , 'nValue' , ), 20, (20, (), [ (8, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( 'SetBufferCount' , 'nCount' , ), 21, (21, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'SaveConfigure' , 'szFileName' , ), 22, (22, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( 'LoadConfigure' , 'szFileName' , ), 23, (23, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'GetDeviceInfo' , 'pDeviceInfo' , ), 24, (24, (), [ (16393, 10, None, "IID('{3D3A2E09-310D-45CA-A4DD-97EDFD156E6D}')") , ], 1 , 1 , 4 , 0 , 116 , (3, 0, None, None) , 0 , )),
	(( 'AutoBalance' , ), 25, (25, (), [ ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'SetSelector' , 'szValue' , 'nValue' , ), 26, (26, (), [ (8, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 124 , (3, 0, None, None) , 0 , )),
	(( 'GetSelector' , 'szValue' , 'nValue' , ), 27, (27, (), [ (8, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'GetUserContext' , 'pUserContext' , ), 28, (28, (), [ (16401, 10, None, None) , ], 1 , 1 , 4 , 0 , 132 , (3, 0, None, None) , 0 , )),
	(( 'IsOnline' , 'bIsOnline' , ), 29, (29, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'IsCapturing' , 'bIsCapturing' , ), 30, (30, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 140 , (3, 0, None, None) , 0 , )),
	(( 'IsGrabSucceeded' , 'nWaitTime' , 'bIsSucceed' , ), 31, (31, (), [ (3, 0, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'GetRGB32Buffer' , 'LVImagePtr' , 'LVLineWidth' , 'LVPixelSize' , 'AlgorithmType' , 
			 'nRel' , ), 33, (33, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 0, None, None) , 
			 (3, 1, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 148 , (3, 0, None, None) , 0 , )),
	(( 'GetRGBBuffer' , 'usPixelSize' , 'AlgorithmType' , 'pImageBuffer' , ), 34, (34, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (16401, 10, None, None) , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'CopyImageBuffer' , 'pDestBuffer' , 'nLength' , 'bRel' , ), 35, (35, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 156 , (3, 0, None, None) , 0 , )),
	(( 'GetDebugInfo' , 'pDebugInfo' , ), 36, (36, (), [ (16393, 10, None, "IID('{F79A0746-83FD-4A37-A47F-B5E14B2D4915}')") , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'EnableDenoising' , 'bEnable' , ), 37, (37, (), [ (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 164 , (3, 0, None, None) , 0 , )),
	(( 'GetErrorImage' , 'pErrorImage' , ), 38, (38, (), [ (16401, 10, None, None) , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'ReadMemory' , 'ulAddress' , 'ulLength' , 'pData' , ), 39, (39, (), [ 
			 (21, 1, None, None) , (19, 1, None, None) , (16401, 10, None, None) , ], 1 , 1 , 4 , 0 , 172 , (3, 0, None, None) , 0 , )),
	(( 'WriteMemroy' , 'ulAddress' , 'ulLength' , 'pData' , ), 40, (40, (), [ 
			 (21, 1, None, None) , (19, 1, None, None) , (16401, 1, None, None) , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'GrapOne' , ), 41, (41, (), [ ], 1 , 1 , 4 , 0 , 180 , (3, 0, None, None) , 0 , )),
	(( 'GetFValue' , 'strName' , 'fValue' , ), 42, (42, (), [ (8, 1, None, None) , 
			 (16388, 10, None, None) , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'SetFValue' , 'strName' , 'fValue' , ), 43, (43, (), [ (8, 1, None, None) , 
			 (4, 1, None, None) , ], 1 , 1 , 4 , 0 , 188 , (3, 0, None, None) , 0 , )),
	(( 'GetFMin' , 'strName' , 'fValue' , ), 44, (44, (), [ (8, 1, None, None) , 
			 (16388, 10, None, None) , ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'GetFMax' , 'strName' , 'fValue' , ), 45, (45, (), [ (8, 1, None, None) , 
			 (16388, 10, None, None) , ], 1 , 1 , 4 , 0 , 196 , (3, 0, None, None) , 0 , )),
	(( 'GetFInc' , 'strName' , 'fValue' , ), 46, (46, (), [ (8, 1, None, None) , 
			 (16388, 10, None, None) , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'GetStrValue' , 'strName' , 'strValue' , ), 47, (47, (), [ (8, 1, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 204 , (3, 0, None, None) , 0 , )),
	(( 'SetStrValue' , 'strName' , 'strValue' , ), 48, (48, (), [ (8, 1, None, None) , 
			 (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'SetSelectorStr' , 'strName' , 'strValue' , ), 49, (49, (), [ (8, 1, None, None) , 
			 (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 212 , (3, 0, None, None) , 0 , )),
	(( 'GetSelectorStr' , 'strName' , 'strValue' , ), 50, (50, (), [ (8, 1, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'GetChildCount' , 'strName' , 'nCount' , ), 51, (51, (), [ (8, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 220 , (3, 0, None, None) , 0 , )),
	(( 'GetChildName' , 'strName' , 'nIndex' , 'strValue' , ), 52, (52, (), [ 
			 (8, 1, None, None) , (3, 1, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'GetParentName' , 'strName' , 'strValue' , ), 53, (53, (), [ (8, 1, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 228 , (3, 0, None, None) , 0 , )),
	(( 'GetToolTip' , 'strName' , 'strValue' , ), 54, (54, (), [ (8, 1, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'GetDescription' , 'strName' , 'strValue' , ), 55, (55, (), [ (8, 1, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 236 , (3, 0, None, None) , 0 , )),
	(( 'GetDisplayName' , 'strName' , 'strValue' , ), 56, (56, (), [ (8, 1, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'GetDeviceName' , 'strName' , 'strValue' , ), 57, (57, (), [ (8, 1, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 244 , (3, 0, None, None) , 0 , )),
	(( 'GetUnit' , 'strName' , 'strValue' , ), 58, (58, (), [ (8, 1, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'GetVisibility' , 'strName' , 'nValue' , ), 59, (59, (), [ (8, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 252 , (3, 0, None, None) , 0 , )),
	(( 'GetAccessMode' , 'strName' , 'nAccessMode' , ), 60, (60, (), [ (8, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'GetGenICamObj' , 'pHandle' , ), 61, (61, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 260 , (3, 0, None, None) , 0 , )),
	(( 'GetInterfaceType' , 'strName' , 'nInterfaceType' , ), 62, (62, (), [ (8, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'GetInterfaceTypeName' , 'strName' , 'strValue' , ), 63, (63, (), [ (8, 1, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 268 , (3, 0, None, None) , 0 , )),
	(( 'DisplayPropertiesWnd' , ), 64, (64, (), [ ], 1 , 1 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'GetRGB32BufferEx' , 'LVImagePtr' , 'LVLineWidth' , 'LVPixelSize' , 'AlgorithmType' , 
			 'nRel' , ), 65, (65, (), [ (21, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , 
			 (3, 1, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 276 , (3, 0, None, None) , 0 , )),
	(( 'SaveImage' , 'ImageAddress' , 'strImageName' , 'nPixelSize' , ), 66, (66, (), [ 
			 (20, 1, None, None) , (8, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
]

ICameraLinkDeviceInfo_vtables_dispatch_ = 1
ICameraLinkDeviceInfo_vtables_ = [
]

IDebugInfo_vtables_dispatch_ = 1
IDebugInfo_vtables_ = [
	(( 'GetCurrentImageNumber' , 'ulCurrentImageNumber' , ), 1, (1, (), [ (16403, 10, None, None) , ], 1 , 1 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'GetCurrentDropImageNumber' , 'ulCurrentDropImageNumber' , ), 2, (2, (), [ (16403, 10, None, None) , ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'GetCurrentDropPacketNumber' , 'ulCurrentDropPacketNumber' , ), 3, (3, (), [ (16403, 10, None, None) , ], 1 , 1 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'GetCurrentResendCount' , 'ulCurrentResendCount' , ), 4, (4, (), [ (16403, 10, None, None) , ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'GetCurrentBufferCount' , 'ulCurrentBufferCount' , ), 5, (5, (), [ (16403, 10, None, None) , ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'GetCurrentFulllistSize' , 'ulCurrentFulllistSize' , ), 6, (6, (), [ (16403, 10, None, None) , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'GetCurrentEmptylistSize' , 'ulCurrentEmptylistSize' , ), 7, (7, (), [ (16403, 10, None, None) , ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'GetCurrentImagelistSize' , 'ulCurrentImagelistSize' , ), 8, (8, (), [ (16403, 10, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'GetCurrentUserlistSize' , 'ulCurrentUserlistSize' , ), 9, (9, (), [ (16403, 10, None, None) , ], 1 , 1 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'GetCurrentCallBackEnterNumber' , 'ulCurrentCallBackEnterNumber' , ), 10, (10, (), [ (16403, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'GetCurrentCoverImageNumber' , 'ulCurrentCoverImageNumber' , ), 11, (11, (), [ (16403, 10, None, None) , ], 1 , 1 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( 'GetCurrentDeviceImageNumber' , 'ulCurrentDeviceImageNumber' , ), 12, (12, (), [ (16403, 10, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IDeviceInfo_vtables_dispatch_ = 1
IDeviceInfo_vtables_ = [
	(( 'IsSerialNumberAvailable' , 'bIsAvailable' , ), 3, (3, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'GetCameraType' , 'Cameratype' , ), 4, (4, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'IsUserIDAvailable' , 'bIsAvailable' , ), 7, (7, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'IsVendorNameAvailable' , 'bIsAvailable' , ), 10, (10, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'IsModelNameAvailable' , 'bIsAvailable' , ), 13, (13, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'IsVersionAvailable' , 'bIsAvailable' , ), 16, (16, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'GetGigeInfo' , 'pGigeInfo' , ), 17, (17, (), [ (16393, 10, None, "IID('{D4904E55-39D2-490D-A5DF-ADE372FBCE55}')") , ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'GetUsbInfo' , 'pUsbInfo' , ), 18, (18, (), [ (16393, 10, None, "IID('{039F2506-34D0-49DE-AEFE-E6F0485455A0}')") , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'GetIEEEInfo' , 'pIEEEInfo' , ), 19, (19, (), [ (16393, 10, None, "IID('{D9172DBC-6D72-46B4-BDD9-218D69D255E0}')") , ], 1 , 1 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'GetCameraLinkInfo' , 'pCameraLinkInfo' , ), 20, (20, (), [ (16393, 10, None, "IID('{C4D650B1-73A1-41D8-813B-FD34F624CCB2}')") , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'SerialNumber' , 'pVal' , ), 22, (22, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( 'SerialNumber' , 'pVal' , ), 22, (22, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'UserID' , 'pVal' , ), 23, (23, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( 'UserID' , 'pVal' , ), 23, (23, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'VendorName' , 'pVal' , ), 24, (24, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( 'VendorName' , 'pVal' , ), 24, (24, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'ModelName' , 'pVal' , ), 25, (25, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( 'ModelName' , 'pVal' , ), 25, (25, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Version' , 'pVal' , ), 26, (26, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
	(( 'Version' , 'pVal' , ), 26, (26, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'ManufactureInfo' , 'pVal' , ), 27, (27, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 108 , (3, 0, None, None) , 0 , )),
	(( 'ManufactureInfo' , 'pVal' , ), 27, (27, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
]

IDeviceManager_vtables_dispatch_ = 1
IDeviceManager_vtables_ = [
	(( 'Initialize' , ), 1, (1, (), [ ], 1 , 1 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Terminate' , ), 2, (2, (), [ ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'GetCameraCount' , 'nWaitTime' , 'nCount' , ), 3, (3, (), [ (3, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'GetCamera' , 'nIndex' , 'pCamera' , ), 4, (4, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{58B62995-823D-4AC8-9A04-5A839BA64D52}')") , ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'GetCameraByName' , 'szCameraName' , 'pCamera' , ), 5, (5, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{58B62995-823D-4AC8-9A04-5A839BA64D52}')") , ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'ReleaseCamera' , 'pCamera' , ), 6, (6, (), [ (9, 1, None, "IID('{58B62995-823D-4AC8-9A04-5A839BA64D52}')") , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'GetError' , 'nError' , 'szErrorInfo' , ), 7, (7, (), [ (3, 1, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
]

IGigeDeviceInfo_vtables_dispatch_ = 1
IGigeDeviceInfo_vtables_ = [
	(( 'GetSpecVerMajor' , 'nMajor' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'GetSpecVerMinor' , 'nMinor' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'GetDeviceMode' , 'nDeviceMode' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
	(( 'GetMacHigh' , 'usMacHigh' , ), 4, (4, (), [ (16402, 10, None, None) , ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( 'GetMacLow' , 'ulMacLow' , ), 5, (5, (), [ (16403, 10, None, None) , ], 1 , 1 , 4 , 0 , 44 , (3, 0, None, None) , 0 , )),
	(( 'GetIPConfigOptions' , 'ulIPConfigOptions' , ), 6, (6, (), [ (16403, 10, None, None) , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( 'GetNetIP' , 'ulNetIP' , ), 15, (15, (), [ (16403, 10, None, None) , ], 1 , 1 , 4 , 0 , 52 , (3, 0, None, None) , 0 , )),
	(( 'GetNetMask' , 'ulNetMask' , ), 16, (16, (), [ (16403, 10, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'IPConfigCurrent' , 'pVal' , ), 17, (17, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 60 , (3, 0, None, None) , 0 , )),
	(( 'IPConfigCurrent' , 'pVal' , ), 17, (17, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'IP' , 'pVal' , ), 18, (18, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 68 , (3, 0, None, None) , 0 , )),
	(( 'IP' , 'pVal' , ), 18, (18, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'SubnetMask' , 'pVal' , ), 19, (19, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 76 , (3, 0, None, None) , 0 , )),
	(( 'SubnetMask' , 'pVal' , ), 19, (19, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'DefaultGateway' , 'pVal' , ), 20, (20, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 84 , (3, 0, None, None) , 0 , )),
	(( 'DefaultGateway' , 'pVal' , ), 20, (20, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'GetNICLocalName' , 'strNICName' , ), 21, (21, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 92 , (3, 0, None, None) , 0 , )),
	(( 'IsCurrentIPValid' , 'ulAddress' , 'bIsValid' , ), 22, (22, (), [ (19, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'AutoSetIP' , ), 23, (23, (), [ ], 1 , 1 , 4 , 0 , 100 , (3, 0, None, None) , 0 , )),
]

IIEEEDeviceInfo_vtables_dispatch_ = 1
IIEEEDeviceInfo_vtables_ = [
]

IMsgNotice_vtables_dispatch_ = 1
IMsgNotice_vtables_ = [
]

IUsbDeviceInfo_vtables_dispatch_ = 1
IUsbDeviceInfo_vtables_ = [
	(( 'Speed' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
	(( 'Speed' , 'pVal' , ), 1, (1, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( 'IsUsb3' , 'bIsUsb3' , ), 2, (2, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 36 , (3, 0, None, None) , 0 , )),
]

RecordMap = {
}

CLSIDToClassMap = {
	'{3D3A2E09-310D-45CA-A4DD-97EDFD156E6D}' : IDeviceInfo,
	'{6B883B26-98C5-4E69-A0D2-37A55D6FA1FB}' : DeviceInfo,
	'{D4904E55-39D2-490D-A5DF-ADE372FBCE55}' : IGigeDeviceInfo,
	'{039F2506-34D0-49DE-AEFE-E6F0485455A0}' : IUsbDeviceInfo,
	'{D9172DBC-6D72-46B4-BDD9-218D69D255E0}' : IIEEEDeviceInfo,
	'{C4D650B1-73A1-41D8-813B-FD34F624CCB2}' : ICameraLinkDeviceInfo,
	'{A2CA86D9-92BC-460C-838F-BB3FF699E2BB}' : GigeDeviceInfo,
	'{31751075-AB5B-4A29-8331-4E9672F98641}' : UsbDeviceInfo,
	'{05B1890F-898B-4BF1-9FDB-9F82E8684776}' : IEEEDeviceInfo,
	'{A1587EFE-6BB9-4E01-8BEC-F287654B6D5E}' : CameraLinkDeviceInfo,
	'{2DBD29C5-42BE-4886-B8CF-682DC7B18EE1}' : _IMsgNoticeEvents,
	'{58B62995-823D-4AC8-9A04-5A839BA64D52}' : ICamera,
	'{F79A0746-83FD-4A37-A47F-B5E14B2D4915}' : IDebugInfo,
	'{1DD5D781-3E0C-4477-90C3-392A682B6452}' : Camera,
	'{D6AE9517-8BE3-4C9A-A45D-435BF9603263}' : IDeviceManager,
	'{939934F4-20DF-4866-A30D-0635F879725E}' : DeviceManager,
	'{1FB878F5-4C89-43DA-A438-EE3AF0D2B344}' : IMsgNotice,
	'{8F116AA1-F23A-4B62-A344-9B463C0BDE2F}' : MsgNotice,
	'{D59898B1-79CD-45A0-9115-14DFB35F658C}' : DebugInfo,
}
CLSIDToPackageMap = {}
win32com.client.CLSIDToClass.RegisterCLSIDsFromDict( CLSIDToClassMap )
VTablesToPackageMap = {}
VTablesToClassMap = {
	'{3D3A2E09-310D-45CA-A4DD-97EDFD156E6D}' : 'IDeviceInfo',
	'{D4904E55-39D2-490D-A5DF-ADE372FBCE55}' : 'IGigeDeviceInfo',
	'{039F2506-34D0-49DE-AEFE-E6F0485455A0}' : 'IUsbDeviceInfo',
	'{D9172DBC-6D72-46B4-BDD9-218D69D255E0}' : 'IIEEEDeviceInfo',
	'{C4D650B1-73A1-41D8-813B-FD34F624CCB2}' : 'ICameraLinkDeviceInfo',
	'{58B62995-823D-4AC8-9A04-5A839BA64D52}' : 'ICamera',
	'{F79A0746-83FD-4A37-A47F-B5E14B2D4915}' : 'IDebugInfo',
	'{D6AE9517-8BE3-4C9A-A45D-435BF9603263}' : 'IDeviceManager',
	'{1FB878F5-4C89-43DA-A438-EE3AF0D2B344}' : 'IMsgNotice',
}


NamesToIIDMap = {
	'IDeviceInfo' : '{3D3A2E09-310D-45CA-A4DD-97EDFD156E6D}',
	'IGigeDeviceInfo' : '{D4904E55-39D2-490D-A5DF-ADE372FBCE55}',
	'IUsbDeviceInfo' : '{039F2506-34D0-49DE-AEFE-E6F0485455A0}',
	'IIEEEDeviceInfo' : '{D9172DBC-6D72-46B4-BDD9-218D69D255E0}',
	'ICameraLinkDeviceInfo' : '{C4D650B1-73A1-41D8-813B-FD34F624CCB2}',
	'_IMsgNoticeEvents' : '{2DBD29C5-42BE-4886-B8CF-682DC7B18EE1}',
	'ICamera' : '{58B62995-823D-4AC8-9A04-5A839BA64D52}',
	'IDebugInfo' : '{F79A0746-83FD-4A37-A47F-B5E14B2D4915}',
	'IDeviceManager' : '{D6AE9517-8BE3-4C9A-A45D-435BF9603263}',
	'IMsgNotice' : '{1FB878F5-4C89-43DA-A438-EE3AF0D2B344}',
}

win32com.client.constants.__dicts__.append(constants.__dict__)

