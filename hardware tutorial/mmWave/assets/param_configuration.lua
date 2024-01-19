---------------------------------- STARTUP -------------------------------------
------------------------ DO NOT MODIFY THIS SECTION ----------------------------

-- mmwavestudio installation path
RSTD_PATH = RSTD.GetRstdPath()

------------------------------ CONFIGURATIONS ----------------------------------
-- Use "DCA1000" for working with DCA1000
capture_device  = "DCA1000"

-- SOP mode
SOP_mode        = 2

-- RS232 connection baud rate
baudrate        = 921600
-- RS232 COM Port number
uart_com_port   = 8     -- your com port number
-- Timeout in ms
timeout         = 1000

-- BSS firmware
bss_path        = "~\\mmwave_studio_02_01_01_00\\rf_eval_firmware\\radarss\\xwr68xx_radarss.bin"
-- MSS firmware
mss_path        = "~\\mmwave_studio_02_01_01_00\\rf_eval_firmware\\masterss\\xwr68xx_masterss.bin"

adc_data_path = "~\\mmwave_studio_02_01_01_00\\mmWaveStudio\\PostProc\\adc_data.bin"

------------------------- Connect Tab settings ---------------------------------

ar1.FullReset()

-- Select Capture device
ret=ar1.SelectCaptureDevice(capture_device)
if(ret~=0)
then
    print("******* Wrong Capture device *******")
    return
end

-- SOP mode
ret=ar1.SOPControl(SOP_mode)
RSTD.Sleep(timeout)
if(ret~=0)
then
    print("******* SOP FAIL *******")
    return
end

-- RS232 Connect
ret=ar1.Connect(uart_com_port,baudrate,timeout)
RSTD.Sleep(timeout)
if(ret~=0)
then
    print("******* Connect FAIL *******")
    return
end

-- Operating Frequency & Device Variant
ar1.frequencyBandSelection("60G")
ar1.deviceVariantSelection("XWR6843")

-- Download BSS Firmware
ret=ar1.DownloadBSSFw(bss_path)
RSTD.Sleep(2*timeout)
if(ret~=0)
then
    print("******* BSS Load FAIL *******")
    return
end

-- Download MSS Firmware
ret=ar1.DownloadMSSFw(mss_path)
RSTD.Sleep(2*timeout)
if(ret~=0)
then
    print("******* MSS Load FAIL *******")
    return
end

-- SPI Connect
ar1.PowerOn(0, 1000, 0, 0)

-- RF Power UP
ar1.RfEnable()

------------------------- Other Device Configuration ---------------------------

-- ADD Device Configuration here

-- StaticConfig
ar1.ChanNAdcConfig(1, 1, 1, 1, 1, 1, 1, 2, 2, 0)
ar1.LPModConfig(0, 0)
ar1.RfInit()
RSTD.Sleep(1000)

-- DataConfig
ar1.DataPathConfig(513, 1216644097, 0)
ar1.LvdsClkConfig(1, 1)
ar1.LVDSLaneConfig(0, 1, 1, 0, 0, 1, 0, 0)


--SensorConfig
ar1.ProfileConfig(0, 60, 7, 5, 140, 0, 0, 0, 0, 0, 0, 27.013, 0, 256, 3000, 0, 131072, 30)

ar1.ChirpConfig(0, 0, 0, 0, 0, 0, 0, 1, 1, 1)
ar1.FrameConfig(0, 0, 1000, 192, 50, 0, 0, 1)

ar1.SelectCaptureDevice("DCA1000")
ar1.CaptureCardConfig_EthInit("192.168.33.30", "192.168.33.180", "12:34:56:78:90:12", 4096, 4098)