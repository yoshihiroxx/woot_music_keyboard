import ctypes
import os

base = os.path.dirname(os.path.abspath(__file__))
print( os.path.join(base, 'wooting-analog-sdk\\windows\\x64\\Release\\wooting-analog-sdk.dll'))
libc = ctypes.cdll.LoadLibrary(os.path.join(base, 'wooting-analog-sdk\\windows\\Release\\wooting-analog-sdk.dll'))

print('hello')

print(libc.wooting_kbd_connected())

# analogBuffer = ctypes.c_ubyte * 32
# print(analogBuffer)
# print(libc.wooting_read_full_buffer(analogBuffer, ctypes.c_uint(32)))

libc.wooting_read_analog.restype = ctypes.c_uint8
libc.wooting_read_analog.argtypes = [ctypes.c_uint8, ctypes.c_uint8]

print(libc.wooting_read_analog( 2, 0))
