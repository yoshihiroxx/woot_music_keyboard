import ctypes
import os

base = os.path.dirname(os.path.abspath(__file__))
libc = ctypes.cdll.LoadLibrary(os.path.join(base, '..\\wooting-analog-sdk.dll'))


print(libc.wooting_kbd_connected())

# analogBuffer = ctypes.c_ubyte * 32
# print(analogBuffer)
# print(libc.wooting_read_full_buffer(analogBuffer, ctypes.c_uint(32)))
