# MicroPython USB Mouse module
#
# MIT license; Copyright (c) 2023-2024 Angus Gratton
from micropython import const
import struct
import machine

from usb.device.hid import HIDInterface

_INTERFACE_PROTOCOL_MOUSE = const(0x02)


class MouseInterface(HIDInterface):
    # A basic three button USB mouse HID interface
    def __init__(self, interface_str="Macro Pad Mouse"):
        super().__init__(
            _MOUSE_REPORT_DESC,
            protocol=_INTERFACE_PROTOCOL_MOUSE,
            interface_str=interface_str,
        )
        self._l = False  # Left button
        self._m = False  # Middle button
        self._r = False  # Right button
        self._buf = bytearray(4)

    def send_report(self, dx=0, dy=0, wheel=0):
        b = 0
        if self._l:
            b |= 1 << 0
        if self._r:
            b |= 1 << 1
        if self._m:
            b |= 1 << 2

        # Wait for any pending report to be sent to the host
        # before updating contents of _buf.
        #
        # This loop can be removed if you don't care about possibly missing a
        # transient report, the final report buffer contents will always be the
        # last one sent to the host (it just might lose one of the ones in the
        # middle).
        while self.busy():
            machine.idle()

        struct.pack_into("Bbbb", self._buf, 0, b, dx, dy, wheel)

        return super().send_report(self._buf)

    def click_left(self, down=True):
        self._l = down
        return self.send_report()

    def click_middle(self, down=True):
        self._m = down
        return self.send_report()

    def click_right(self, down=True):
        self._r = down
        return self.send_report()

    def move_by(self, dx, dy):
        if not -127 <= dx <= 127:
            raise ValueError("dx")
        if not -127 <= dy <= 127:
            raise ValueError("dy")
        return self.send_report(dx, dy)
    
    def scroll(self, amount):
        if not -127 <= amount <= 127:
            raise ValueError("amount")
        return self.send_report(wheel=amount)


# Basic 3-button mouse HID Report Descriptor.
# This is based on Appendix E.10 of the HID v1.11 document.
# fmt: off
_MOUSE_REPORT_DESC = (
    b'\x05\x01'  # Usage Page (Generic Desktop)
        b'\x09\x02'  # Usage (Mouse)
    b'\xA1\x01'  # Collection (Application)
        b'\x09\x01'  # Usage (Pointer)
        b'\xA1\x00'  # Collection (Physical)
            b'\x05\x09'  # Usage Page (Buttons)
                b'\x19\x01'  # Usage Minimum (01),
                b'\x29\x03'  # Usage Maximun (03),
                b'\x15\x00'  # Logical Minimum (0),
                b'\x25\x01'  # Logical Maximum (1),
                b'\x95\x03'  # Report Count (3),
                b'\x75\x01'  # Report Size (1),
                b'\x81\x02'  # Input (Data, Variable, Absolute), ;3 button bits
                b'\x95\x01'  # Report Count (1),
                b'\x75\x05'  # Report Size (5),
                b'\x81\x01'  # Input (Constant), ;5 bit padding
            b'\x05\x01'  # Usage Page (Generic Desktop),
                b'\x09\x30'  # Usage (X),
                b'\x09\x31'  # Usage (Y),
                b'\x09\x38'  # Usage (Wheel),
                b'\x15\x81'  # Logical Minimum (-127),
                b'\x25\x7F'  # Logical Maximum (127),
                b'\x75\x08'  # Report Size (8),
                b'\x95\x03'  # Report Count (3),
                b'\x81\x06'  # Input (Data, Variable, Relative), ;2 position bytes (X & Y)
        b'\xC0'  # End Collection
    b'\xC0'  # End Collection
)
# fmt: on


__version__ = '0.1.0'
