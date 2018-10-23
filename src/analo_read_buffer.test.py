import ctypes
import os

base = os.path.dirname(os.path.abspath(__file__))
print( os.path.join(base, '..\\wooting-analog-sdk.dll'))
libc = ctypes.cdll.LoadLibrary(os.path.join(base, '..\\wooting-analog-sdk.dll'))


print(libc.wooting_kbd_connected())

analogBuffer = ctypes.c_uint8 * 32
buffer_size = ctypes.c_uint(32)
print(list(analogBuffer()))
# print(libc.wooting_read_full_buffer(analogBuffer, ctypes.c_uint(32)))

# libc.wooting_read_analog.restype = ctypes.c_uint8
# libc.wooting_read_analog.argtypes = [ctypes.c_uint8, ctypes.c_uint]
buffer_arr = analogBuffer()
active_keys_count = libc.wooting_read_full_buffer(ctypes.byref(buffer_arr), buffer_size)


while (1):

    active_keys_count = libc.wooting_read_full_buffer(ctypes.byref(buffer_arr), buffer_size)
    active_keys_status = []
    for i in range(active_keys_count):
            active_keys_status.append( buffer_arr[i*2] )
            active_keys_status.append( buffer_arr[i*2 +1] )
    print(list(active_keys_status))
    # print (list(buffer_arr))
    # print (active_keys_count)
