"""Check the installed Windows ARM64 wheel, not a DLL from PATH."""
import ctypes
from pathlib import Path
import struct
import sys

import glfw


def pe_machine(path):
    data = Path(path).read_bytes()
    assert data[:2] == b"MZ", path
    pe_offset = struct.unpack_from("<I", data, 0x3C)[0]
    assert data[pe_offset:pe_offset + 4] == b"PE\0\0", path
    return struct.unpack_from("<H", data, pe_offset + 4)[0]


assert pe_machine(sys.executable) == 0xAA64, "Python must be native ARM64"
dll = Path(glfw.__file__).with_name("glfw3.dll")
assert pe_machine(dll) == 0xAA64, "Bundled GLFW must be native ARM64"
ctypes.CDLL(str(dll))
assert glfw.get_version() == (3, 4, 0)
# The null platform exercises initialization without requiring a desktop/driver.
glfw.init_hint(glfw.PLATFORM, glfw.PLATFORM_NULL)
assert glfw.init(), glfw.get_error()
glfw.terminate()
print("Native ARM64 DLL load, GLFW 3.4 API and null-platform initialization passed")
