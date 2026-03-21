import usb.device
from usb.device.hid import HIDInterface
import time

_CONSUMER_DESC = bytes([
    0x05, 0x0C,        # Usage Page (Consumer)
    0x09, 0x01,        # Usage (Consumer Control)
    0xA1, 0x01,        # Collection (Application)
    0x15, 0x00,        #   Logical Minimum (0)
    0x26, 0xFF, 0x03,  #   Logical Maximum (1023)
    0x19, 0x00,        #   Usage Minimum (0)
    0x2A, 0xFF, 0x03,  #   Usage Maximum (1023)
    0x75, 0x10,        #   Report Size (16)
    0x95, 0x01,        #   Report Count (1)
    0x81, 0x00,        #   Input (Data, Array)
    0xC0,              # End Collection
])

class ConsumerCode:
    MUTE          = 0x00E2
    VOLUME_UP     = 0x00E9
    VOLUME_DOWN   = 0x00EA
    PLAY_PAUSE    = 0x00CD
    NEXT_TRACK    = 0x00B5
    PREV_TRACK    = 0x00B6
    
class ConsumerInterface(HIDInterface):
    def __init__(self):
        super().__init__(_CONSUMER_DESC, interface_str="Macro Pad")
        
    def send_code(self, code):
        self.send_report(bytes([code & 0xFF, (code >> 8) & 0xFF]))
        time.sleep_ms(50)
        self.send_report(bytes([0x00, 0x00]))