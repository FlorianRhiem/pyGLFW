from _typeshed import Incomplete
from collections.abc import Callable, Sequence
import ctypes
from typing import NamedTuple, Optional
from cffi import FFI

__version__: str
__license__: str
ERROR_REPORTING: str
NORMALIZE_GAMMA_RAMPS: bool
ffi: FFI
_PREVIEW: Optional[bool]

class GLFWError(UserWarning):
    error_code: int
    def __init__(self, message: str, error_code: int | None = None) -> None: ...

class _GLFWwindow(ctypes.Structure):
    dummy: ctypes.c_int

class _GLFWmonitor(ctypes.Structure):
    dummy: ctypes.c_int

class _GLFWvidmode(ctypes.Structure):
    class GLFWvidmode(NamedTuple):
        size: _GLFWvidmode.Size
        bits: _GLFWvidmode.Bits
        refresh_rate: int

    class Size(NamedTuple):
        width: int
        height: int

    class Bits(NamedTuple):
        red: int
        green: int
        blue: int

    width: ctypes.c_int
    height: ctypes.c_int
    red_bits: ctypes.c_int
    green_bits: ctypes.c_int
    blue_bits: ctypes.c_int
    refresh_rate: ctypes.c_uint

    def __init__(self) -> None: ...
    def wrap(self, video_mode: GLFWvidmode) -> None: ...
    def unwrap(self) -> GLFWvidmode: ...

class _GLFWgammaramp(ctypes.Structure):
    class GLFWgammaramp(NamedTuple):
        red: int
        green: int
        blue: int

    red: ctypes._Pointer[ctypes.c_ushort]
    green: ctypes._Pointer[ctypes.c_ushort]
    blue: ctypes._Pointer[ctypes.c_ushort]
    size: ctypes.c_uint

    def __init__(self) -> None: ...
    def wrap(self, gammaramp: GLFWgammaramp) -> None: ...
    def unwrap(self) -> GLFWgammaramp: ...

class _GLFWcursor(ctypes.Structure):
    dummy: ctypes.c_int

class _GLFWimage(ctypes.Structure):
    class GLFWimage(NamedTuple):
        width: int
        height: int
        pixels: Incomplete  # PIL image or nested sequence

    width: ctypes.c_int
    height: ctypes.c_int
    pixels: ctypes._Pointer[ctypes.c_ubyte]

    def __init__(self) -> None: ...
    def wrap(self, image: GLFWimage) -> None: ...
    def unwrap(self) -> GLFWimage: ...

class _GLFWgamepadstate(ctypes.Structure):
    class GLFWgamepadstate(NamedTuple):
        buttons: list[int]
        axes: list[float]

    buttons: ctypes.Array[ctypes.c_ubyte]
    axes: ctypes.Array[ctypes.c_float]

    def __init__(self) -> None: ...
    def wrap(self, gamepad_state: GLFWgamepadstate) -> None: ...
    def unwrap(self) -> GLFWgamepadstate: ...

VERSION_MAJOR: int
VERSION_MINOR: int
VERSION_REVISION: int
TRUE: int
FALSE: int
RELEASE: int
PRESS: int
REPEAT: int
HAT_CENTERED: int
HAT_UP: int
HAT_RIGHT: int
HAT_DOWN: int
HAT_LEFT: int
HAT_RIGHT_UP: int
HAT_RIGHT_DOWN: int
HAT_LEFT_UP: int
HAT_LEFT_DOWN: int
KEY_UNKNOWN: int
KEY_SPACE: int
KEY_APOSTROPHE: int
KEY_COMMA: int
KEY_MINUS: int
KEY_PERIOD: int
KEY_SLASH: int
KEY_0: int
KEY_1: int
KEY_2: int
KEY_3: int
KEY_4: int
KEY_5: int
KEY_6: int
KEY_7: int
KEY_8: int
KEY_9: int
KEY_SEMICOLON: int
KEY_EQUAL: int
KEY_A: int
KEY_B: int
KEY_C: int
KEY_D: int
KEY_E: int
KEY_F: int
KEY_G: int
KEY_H: int
KEY_I: int
KEY_J: int
KEY_K: int
KEY_L: int
KEY_M: int
KEY_N: int
KEY_O: int
KEY_P: int
KEY_Q: int
KEY_R: int
KEY_S: int
KEY_T: int
KEY_U: int
KEY_V: int
KEY_W: int
KEY_X: int
KEY_Y: int
KEY_Z: int
KEY_LEFT_BRACKET: int
KEY_BACKSLASH: int
KEY_RIGHT_BRACKET: int
KEY_GRAVE_ACCENT: int
KEY_WORLD_1: int
KEY_WORLD_2: int
KEY_ESCAPE: int
KEY_ENTER: int
KEY_TAB: int
KEY_BACKSPACE: int
KEY_INSERT: int
KEY_DELETE: int
KEY_RIGHT: int
KEY_LEFT: int
KEY_DOWN: int
KEY_UP: int
KEY_PAGE_UP: int
KEY_PAGE_DOWN: int
KEY_HOME: int
KEY_END: int
KEY_CAPS_LOCK: int
KEY_SCROLL_LOCK: int
KEY_NUM_LOCK: int
KEY_PRINT_SCREEN: int
KEY_PAUSE: int
KEY_F1: int
KEY_F2: int
KEY_F3: int
KEY_F4: int
KEY_F5: int
KEY_F6: int
KEY_F7: int
KEY_F8: int
KEY_F9: int
KEY_F10: int
KEY_F11: int
KEY_F12: int
KEY_F13: int
KEY_F14: int
KEY_F15: int
KEY_F16: int
KEY_F17: int
KEY_F18: int
KEY_F19: int
KEY_F20: int
KEY_F21: int
KEY_F22: int
KEY_F23: int
KEY_F24: int
KEY_F25: int
KEY_KP_0: int
KEY_KP_1: int
KEY_KP_2: int
KEY_KP_3: int
KEY_KP_4: int
KEY_KP_5: int
KEY_KP_6: int
KEY_KP_7: int
KEY_KP_8: int
KEY_KP_9: int
KEY_KP_DECIMAL: int
KEY_KP_DIVIDE: int
KEY_KP_MULTIPLY: int
KEY_KP_SUBTRACT: int
KEY_KP_ADD: int
KEY_KP_ENTER: int
KEY_KP_EQUAL: int
KEY_LEFT_SHIFT: int
KEY_LEFT_CONTROL: int
KEY_LEFT_ALT: int
KEY_LEFT_SUPER: int
KEY_RIGHT_SHIFT: int
KEY_RIGHT_CONTROL: int
KEY_RIGHT_ALT: int
KEY_RIGHT_SUPER: int
KEY_MENU: int
KEY_LAST = KEY_MENU
MOD_SHIFT: int
MOD_CONTROL: int
MOD_ALT: int
MOD_SUPER: int
MOD_CAPS_LOCK: int
MOD_NUM_LOCK: int
MOUSE_BUTTON_1: int
MOUSE_BUTTON_2: int
MOUSE_BUTTON_3: int
MOUSE_BUTTON_4: int
MOUSE_BUTTON_5: int
MOUSE_BUTTON_6: int
MOUSE_BUTTON_7: int
MOUSE_BUTTON_8: int
MOUSE_BUTTON_LAST = MOUSE_BUTTON_8
MOUSE_BUTTON_LEFT = MOUSE_BUTTON_1
MOUSE_BUTTON_RIGHT = MOUSE_BUTTON_2
MOUSE_BUTTON_MIDDLE = MOUSE_BUTTON_3
JOYSTICK_1: int
JOYSTICK_2: int
JOYSTICK_3: int
JOYSTICK_4: int
JOYSTICK_5: int
JOYSTICK_6: int
JOYSTICK_7: int
JOYSTICK_8: int
JOYSTICK_9: int
JOYSTICK_10: int
JOYSTICK_11: int
JOYSTICK_12: int
JOYSTICK_13: int
JOYSTICK_14: int
JOYSTICK_15: int
JOYSTICK_16: int
JOYSTICK_LAST = JOYSTICK_16
GAMEPAD_BUTTON_A: int
GAMEPAD_BUTTON_B: int
GAMEPAD_BUTTON_X: int
GAMEPAD_BUTTON_Y: int
GAMEPAD_BUTTON_LEFT_BUMPER: int
GAMEPAD_BUTTON_RIGHT_BUMPER: int
GAMEPAD_BUTTON_BACK: int
GAMEPAD_BUTTON_START: int
GAMEPAD_BUTTON_GUIDE: int
GAMEPAD_BUTTON_LEFT_THUMB: int
GAMEPAD_BUTTON_RIGHT_THUMB: int
GAMEPAD_BUTTON_DPAD_UP: int
GAMEPAD_BUTTON_DPAD_RIGHT: int
GAMEPAD_BUTTON_DPAD_DOWN: int
GAMEPAD_BUTTON_DPAD_LEFT: int
GAMEPAD_BUTTON_LAST = GAMEPAD_BUTTON_DPAD_LEFT
GAMEPAD_BUTTON_CROSS = GAMEPAD_BUTTON_A
GAMEPAD_BUTTON_CIRCLE = GAMEPAD_BUTTON_B
GAMEPAD_BUTTON_SQUARE = GAMEPAD_BUTTON_X
GAMEPAD_BUTTON_TRIANGLE = GAMEPAD_BUTTON_Y
GAMEPAD_AXIS_LEFT_X: int
GAMEPAD_AXIS_LEFT_Y: int
GAMEPAD_AXIS_RIGHT_X: int
GAMEPAD_AXIS_RIGHT_Y: int
GAMEPAD_AXIS_LEFT_TRIGGER: int
GAMEPAD_AXIS_RIGHT_TRIGGER: int
GAMEPAD_AXIS_LAST = GAMEPAD_AXIS_RIGHT_TRIGGER
NO_ERROR: int
NOT_INITIALIZED: int
NO_CURRENT_CONTEXT: int
INVALID_ENUM: int
INVALID_VALUE: int
OUT_OF_MEMORY: int
API_UNAVAILABLE: int
VERSION_UNAVAILABLE: int
PLATFORM_ERROR: int
FORMAT_UNAVAILABLE: int
NO_WINDOW_CONTEXT: int
CURSOR_UNAVAILABLE: int
FEATURE_UNAVAILABLE: int
FEATURE_UNIMPLEMENTED: int
PLATFORM_UNAVAILABLE: int
FOCUSED: int
ICONIFIED: int
RESIZABLE: int
VISIBLE: int
DECORATED: int
AUTO_ICONIFY: int
FLOATING: int
MAXIMIZED: int
CENTER_CURSOR: int
TRANSPARENT_FRAMEBUFFER: int
HOVERED: int
FOCUS_ON_SHOW: int
MOUSE_PASSTHROUGH: int
POSITION_X: int
POSITION_Y: int
RED_BITS: int
GREEN_BITS: int
BLUE_BITS: int
ALPHA_BITS: int
DEPTH_BITS: int
STENCIL_BITS: int
ACCUM_RED_BITS: int
ACCUM_GREEN_BITS: int
ACCUM_BLUE_BITS: int
ACCUM_ALPHA_BITS: int
AUX_BUFFERS: int
STEREO: int
SAMPLES: int
SRGB_CAPABLE: int
REFRESH_RATE: int
DOUBLEBUFFER: int
CLIENT_API: int
CONTEXT_VERSION_MAJOR: int
CONTEXT_VERSION_MINOR: int
CONTEXT_REVISION: int
CONTEXT_ROBUSTNESS: int
OPENGL_FORWARD_COMPAT: int
OPENGL_DEBUG_CONTEXT: int
CONTEXT_DEBUG: int
OPENGL_PROFILE: int
CONTEXT_RELEASE_BEHAVIOR: int
CONTEXT_NO_ERROR: int
CONTEXT_CREATION_API: int
SCALE_TO_MONITOR: int
SCALE_FRAMEBUFFER: int
COCOA_RETINA_FRAMEBUFFER: int
COCOA_FRAME_NAME: int
COCOA_GRAPHICS_SWITCHING: int
X11_CLASS_NAME: int
X11_INSTANCE_NAME: int
WIN32_KEYBOARD_MENU: int
WIN32_SHOWDEFAULT: int
WAYLAND_APP_ID: int
NO_API: int
OPENGL_API: int
OPENGL_ES_API: int
NO_ROBUSTNESS: int
NO_RESET_NOTIFICATION: int
LOSE_CONTEXT_ON_RESET: int
OPENGL_ANY_PROFILE: int
OPENGL_CORE_PROFILE: int
OPENGL_COMPAT_PROFILE: int
CURSOR: int
STICKY_KEYS: int
STICKY_MOUSE_BUTTONS: int
LOCK_KEY_MODS: int
RAW_MOUSE_MOTION: int
CURSOR_NORMAL: int
CURSOR_HIDDEN: int
CURSOR_DISABLED: int
CURSOR_CAPTURED: int
ANY_RELEASE_BEHAVIOR: int
RELEASE_BEHAVIOR_FLUSH: int
RELEASE_BEHAVIOR_NONE: int
NATIVE_CONTEXT_API: int
EGL_CONTEXT_API: int
OSMESA_CONTEXT_API: int
ARROW_CURSOR: int
IBEAM_CURSOR: int
CROSSHAIR_CURSOR: int
HAND_CURSOR: int
POINTING_HAND_CURSOR: int
HRESIZE_CURSOR: int
RESIZE_EW_CURSOR: int
VRESIZE_CURSOR: int
RESIZE_NS_CURSOR: int
RESIZE_NWSE_CURSOR: int
RESIZE_NESW_CURSOR: int
RESIZE_ALL_CURSOR: int
NOT_ALLOWED_CURSOR: int
ANGLE_PLATFORM_TYPE_NONE: int
ANGLE_PLATFORM_TYPE_OPENGL: int
ANGLE_PLATFORM_TYPE_OPENGLES: int
ANGLE_PLATFORM_TYPE_D3D9: int
ANGLE_PLATFORM_TYPE_D3D11: int
ANGLE_PLATFORM_TYPE_VULKAN: int
ANGLE_PLATFORM_TYPE_METAL: int
WAYLAND_PREFER_LIBDECOR: int
WAYLAND_DISABLE_LIBDECOR: int
CONNECTED: int
DISCONNECTED: int
JOYSTICK_HAT_BUTTONS: int
ANGLE_PLATFORM_TYPE: int
PLATFORM: int
COCOA_CHDIR_RESOURCES: int
COCOA_MENUBAR: int
X11_XCB_VULKAN_SURFACE: int
WAYLAND_LIBDECOR: int
ANY_PLATFORM: int
PLATFORM_WIN32: int
PLATFORM_COCOA: int
PLATFORM_WAYLAND: int
PLATFORM_X11: int
PLATFORM_NULL: int
ANY_POSITION: int
DONT_CARE: int
UNLIMITED_MOUSE_BUTTONS: int


type _GLFWallocatefunT = Callable[[ctypes.c_size_t, ctypes.c_void_p], ctypes.c_void_p]
type _GLFWreallocatefunT = Callable[[ctypes.c_void_p, ctypes.c_size_t, ctypes.c_void_p], ctypes.c_void_p]
type _GLFWdeallocatefunT = Callable[[None, ctypes.c_void_p, ctypes.c_void_p], ctypes.c_void_p]

class _GLFWallocator(ctypes.Structure):
    allocate: _GLFWallocatefunT
    reallocate: _GLFWreallocatefunT
    deallocate: _GLFWdeallocatefunT

### Custom types used for type checking only
# Types copied to global namespace
type _GLFWvidmodeT = _GLFWvidmode.GLFWvidmode
type _GLFWgammarampT = _GLFWgammaramp.GLFWgammaramp
type _GLFWimageT = _GLFWimage.GLFWimage
type _GLFWgamepadstateT = _GLFWgamepadstate.GLFWgamepadstate

type _GLFWmonitorPointerT = ctypes._Pointer[_GLFWmonitor]
type _GLFWwindowPointerT = ctypes._Pointer[_GLFWwindow]
type _GLFWcursorPointerT = ctypes._Pointer[_GLFWcursor]

type _GLFWglprocT = ctypes.c_void_p

type _GLFWerrorfunT = Callable[[int, str], None]
type _GLFWwindowposfunT = Callable[[_GLFWwindowPointerT, int, int], None]
type _GLFWwindowsizefunT = Callable[[_GLFWwindowPointerT, int, int], None]
type _GLFWwindowclosefunT = Callable[[_GLFWwindowPointerT], None]
type _GLFWwindowrefreshfunT = Callable[[_GLFWwindowPointerT], None]
type _GLFWwindowfocusfunT = Callable[[_GLFWwindowPointerT, int], None]
type _GLFWwindowiconifyfunT = Callable[[_GLFWwindowPointerT, int], None]
type _GLFWwindowmaximizefunT = Callable[[_GLFWwindowPointerT, int], None]
type _GLFWframebuffersizefunT = Callable[[_GLFWwindowPointerT, int, int], None]
type _GLFWwindowcontentscalefunT = Callable[[_GLFWwindowPointerT, float, float], None]

type _GLFWmousebuttonfunT = Callable[[_GLFWwindowPointerT, int, int, int], None]
type _GLFWcursorposfunT = Callable[[_GLFWwindowPointerT, float, float], None]
type _GLFWcursorenterfunT = Callable[[_GLFWwindowPointerT, int], None]
type _GLFWscrollfunT = Callable[[_GLFWwindowPointerT, float, float], None]
type _GLFWkeyfunT = Callable[[_GLFWwindowPointerT, int, int, int, int], None]
type _GLFWcharfunT = Callable[[_GLFWwindowPointerT, int], None]
type _GLFWmonitorfunT = Callable[[_GLFWmonitorPointerT, int], None]
type _GLFWdropfunT = Callable[[_GLFWwindowPointerT, int, str], None]
type _GLFWcharmodsfunT = Callable[[_GLFWwindowPointerT, int, int], None]
type _GLFWjoystickfunT = Callable[[int, int], None]
### End of custom types

def init() -> int: ...
def terminate() -> None: ...
def init_hint(hint: int, value: int) -> None: ...
def get_version() -> tuple[int, int, int]: ...
def get_version_string() -> str: ...
def get_error() -> tuple[int, str]: ...
def set_error_callback(cbfun: _GLFWerrorfunT) -> _GLFWerrorfunT | None: ...
def get_monitors() -> list[_GLFWmonitorPointerT]: ...
def get_primary_monitor() -> _GLFWmonitorPointerT: ...
def get_monitor_pos(monitor: _GLFWmonitorPointerT) -> tuple[int, int]: ...
def get_monitor_workarea(monitor: _GLFWmonitorPointerT) -> tuple[int, int, int, int]: ...
def get_monitor_physical_size(monitor: _GLFWmonitorPointerT) -> tuple[int, int]: ...
def get_monitor_content_scale(monitor: _GLFWmonitorPointerT) -> tuple[float, float]: ...
def get_monitor_name(monitor: _GLFWmonitorPointerT) -> str: ...
def set_monitor_user_pointer(monitor: _GLFWmonitorPointerT, pointer: object) -> None: ...
def get_monitor_user_pointer(monitor: _GLFWmonitorPointerT) -> object: ...
def set_monitor_callback(cbfun: _GLFWmonitorfunT) -> _GLFWmonitorfunT | None: ...
def get_video_modes(monitor: _GLFWmonitorPointerT) -> list[_GLFWvidmodeT]: ...
def get_video_mode(monitor: _GLFWmonitorPointerT) -> _GLFWvidmodeT: ...
def set_gamma(monitor: _GLFWmonitorPointerT, gamma: float) -> None: ...
def get_gamma_ramp(monitor: _GLFWmonitorPointerT) -> _GLFWgammarampT: ...
def set_gamma_ramp(monitor: _GLFWmonitorPointerT, ramp: _GLFWgammarampT) -> None: ...
def default_window_hints() -> None: ...
def window_hint(hint: int, value: int) -> None: ...
def window_hint_string(hint: int, value: str) -> None: ...
def create_window(
    width: int,
    height: int,
    title: str,
    monitor: _GLFWmonitorPointerT | None,
    share: _GLFWwindowPointerT | None,
) -> _GLFWwindowPointerT: ...
def destroy_window(window: _GLFWwindowPointerT) -> None: ...
def window_should_close(window: _GLFWwindowPointerT) -> int: ...
def set_window_should_close(window: _GLFWwindowPointerT, value: int) -> None: ...
def set_window_title(window: _GLFWwindowPointerT, title: str) -> None: ...
def get_window_pos(window: _GLFWwindowPointerT) -> tuple[int, int]: ...
def set_window_pos(window: _GLFWwindowPointerT, xpos: int, ypos: int) -> None: ...
def get_window_size(window: _GLFWwindowPointerT) -> tuple[int, int]: ...
def set_window_size(window: _GLFWwindowPointerT, width: int, height: int) -> None: ...
def get_framebuffer_size(window: _GLFWwindowPointerT) -> tuple[int, int]: ...
def get_window_content_scale(window: _GLFWwindowPointerT) -> tuple[float, float]: ...
def get_window_opacity(window: _GLFWwindowPointerT) -> float: ...
def set_window_opacity(window: _GLFWwindowPointerT, opacity: float) -> None: ...
def iconify_window(window: _GLFWwindowPointerT) -> None: ...
def restore_window(window: _GLFWwindowPointerT) -> None: ...
def show_window(window: _GLFWwindowPointerT) -> None: ...
def hide_window(window: _GLFWwindowPointerT) -> None: ...
def request_window_attention(window: _GLFWwindowPointerT) -> None: ...
def get_window_monitor(window: _GLFWwindowPointerT) -> _GLFWmonitorPointerT: ...
def get_window_attrib(window: _GLFWwindowPointerT, attrib: int) -> int: ...
def set_window_attrib(window: _GLFWwindowPointerT, attrib: int, value: int) -> None: ...
def set_window_user_pointer(window: _GLFWwindowPointerT, pointer: object) -> None: ...
def get_window_user_pointer(window: _GLFWwindowPointerT) -> object: ...
def set_window_pos_callback(
    window: _GLFWwindowPointerT, cbfun: _GLFWwindowposfunT
) -> _GLFWwindowposfunT | None: ...
def set_window_size_callback(
    window: _GLFWwindowPointerT, cbfun: _GLFWwindowsizefunT
) -> _GLFWwindowsizefunT | None: ...
def set_window_close_callback(
    window: _GLFWwindowPointerT, cbfun: _GLFWwindowclosefunT
) -> _GLFWwindowclosefunT | None: ...
def set_window_refresh_callback(
    window: _GLFWwindowPointerT, cbfun: _GLFWwindowrefreshfunT
) -> _GLFWwindowrefreshfunT | None: ...
def set_window_focus_callback(
    window: _GLFWwindowPointerT, cbfun: _GLFWwindowfocusfunT
) -> _GLFWwindowfocusfunT | None: ...
def set_window_iconify_callback(
    window: _GLFWwindowPointerT, cbfun: _GLFWwindowiconifyfunT
) -> _GLFWwindowiconifyfunT | None: ...
def set_window_maximize_callback(
    window: _GLFWwindowPointerT, cbfun: _GLFWwindowmaximizefunT
) -> _GLFWwindowmaximizefunT | None: ...
def set_framebuffer_size_callback(
    window: _GLFWwindowPointerT, cbfun: _GLFWframebuffersizefunT
) -> _GLFWframebuffersizefunT | None: ...
def set_window_content_scale_callback(
    window: _GLFWwindowPointerT, cbfun: _GLFWwindowcontentscalefunT
) -> _GLFWwindowcontentscalefunT | None: ...
def poll_events() -> None: ...
def wait_events() -> None: ...
def get_input_mode(window: _GLFWwindowPointerT, mode: int) -> int: ...
def set_input_mode(window: _GLFWwindowPointerT, mode: int, value: int) -> None: ...
def raw_mouse_motion_supported() -> bool: ...
def get_key(window: _GLFWwindowPointerT, key: int) -> int: ...
def get_mouse_button(window: _GLFWwindowPointerT, button: int) -> int: ...
def get_cursor_pos(window: _GLFWwindowPointerT) -> tuple[float, float]: ...
def set_cursor_pos(window: _GLFWwindowPointerT, xpos: float, ypos: float) -> None: ...
def set_key_callback(
    window: _GLFWwindowPointerT, cbfun: _GLFWkeyfunT
) -> _GLFWkeyfunT | None: ...
def set_char_callback(
    window: _GLFWwindowPointerT, cbfun: _GLFWcharfunT
) -> _GLFWcharfunT | None: ...
def set_mouse_button_callback(
    window: _GLFWwindowPointerT, cbfun: _GLFWmousebuttonfunT
) -> _GLFWmousebuttonfunT | None: ...
def set_cursor_pos_callback(
    window: _GLFWwindowPointerT, cbfun: _GLFWcursorposfunT
) -> _GLFWcursorposfunT | None: ...
def set_cursor_enter_callback(
    window: _GLFWwindowPointerT, cbfun: _GLFWcursorenterfunT
) -> _GLFWcursorenterfunT | None: ...
def set_scroll_callback(
    window: _GLFWwindowPointerT, cbfun: _GLFWscrollfunT
) -> _GLFWscrollfunT | None: ...
def joystick_present(joy: int) -> int: ...
def get_joystick_axes(joy: int) -> tuple[Sequence[float], int]: ...
def get_joystick_buttons(joy: int) -> tuple[Sequence[int], int]: ...
def get_joystick_hats(joystick_id: int) -> tuple[Sequence[int], int]: ...
def get_joystick_name(joy: int) -> str: ...
def get_joystick_guid(joystick_id: int) -> str: ...
def set_joystick_user_pointer(joystick_id: int, pointer: object) -> None: ...
def get_joystick_user_pointer(joystick_id: int) -> object: ...
def joystick_is_gamepad(joystick_id: int) -> bool: ...
def get_gamepad_state(joystick_id: int) -> _GLFWgamepadstateT: ...
def set_clipboard_string(window: _GLFWwindowPointerT, string: str) -> None: ...
def get_clipboard_string(window: _GLFWwindowPointerT) -> str: ...
def get_time() -> float: ...
def set_time(time: float) -> None: ...
def make_context_current(window: _GLFWwindowPointerT) -> None: ...
def get_current_context() -> _GLFWwindowPointerT: ...
def swap_buffers(window: _GLFWwindowPointerT) -> None: ...
def swap_interval(interval: int) -> None: ...
def extension_supported(extension: str) -> int: ...
def get_proc_address(procname: str) -> _GLFWglprocT: ...
def set_drop_callback(
    window: _GLFWwindowPointerT, cbfun: _GLFWdropfunT
) -> _GLFWdropfunT | None: ...
def set_char_mods_callback(
    window: _GLFWwindowPointerT, cbfun: _GLFWcharmodsfunT
) -> _GLFWcharmodsfunT | None: ...
def vulkan_supported() -> bool: ...
def get_required_instance_extensions() -> list[str]: ...
def get_timer_value() -> int: ...
def get_timer_frequency() -> int: ...
def set_joystick_callback(cbfun: _GLFWjoystickfunT) -> _GLFWjoystickfunT | None: ...
def update_gamepad_mappings(string: str) -> int: ...
def get_gamepad_name(joystick_id: int) -> str | None: ...
def get_key_name(key: int, scancode: int) -> str | None: ...
def get_key_scancode(key: int) -> int: ...
def create_cursor(image: _GLFWimageT, xhot: int, yhot: int) -> _GLFWcursorPointerT: ...
def create_standard_cursor(shape: int) -> _GLFWcursorPointerT: ...
def destroy_cursor(cursor: _GLFWcursorPointerT) -> None: ...
def set_cursor(window: _GLFWwindowPointerT, cursor: _GLFWcursorPointerT) -> None: ...
def create_window_surface(instance, window: _GLFWwindowPointerT, allocator, surface): ...
def get_physical_device_presentation_support(instance, device, queuefamily: int): ...
def get_instance_proc_address(instance, procname: str): ...
def set_window_icon(
    window: _GLFWwindowPointerT, count: int, images: Sequence[_GLFWimageT]
) -> None: ...
def set_window_size_limits(
    window: _GLFWwindowPointerT,
    minwidth: int,
    minheight: int,
    maxwidth: int,
    maxheight: int,
) -> None: ...
def set_window_aspect_ratio(
    window: _GLFWwindowPointerT, numer: int, denom: int
) -> None: ...
def get_window_frame_size(window: _GLFWwindowPointerT) -> tuple[int, int, int, int]: ...
def maximize_window(window: _GLFWwindowPointerT) -> None: ...
def focus_window(window: _GLFWwindowPointerT) -> None: ...
def set_window_monitor(
    window: _GLFWwindowPointerT,
    monitor: _GLFWmonitorPointerT,
    xpos: int,
    ypos: int,
    width: int,
    height: int,
    refresh_rate: int,
) -> None: ...
def wait_events_timeout(timeout: float) -> None: ...
def post_empty_event() -> None: ...
def get_win32_adapter(monitor: _GLFWmonitorPointerT): ...
def get_win32_monitor(monitor: _GLFWmonitorPointerT): ...
def get_win32_window(window: _GLFWwindowPointerT): ...
def get_wgl_context(window: _GLFWwindowPointerT): ...
def get_cocoa_monitor(monitor: _GLFWmonitorPointerT): ...
def get_cocoa_window(window: _GLFWwindowPointerT): ...
def get_nsgl_context(window: _GLFWwindowPointerT): ...
def get_x11_display(): ...
def get_x11_adapter(monitor: _GLFWmonitorPointerT): ...
def get_x11_monitor(monitor: _GLFWmonitorPointerT): ...
def get_x11_window(window: _GLFWwindowPointerT): ...
def set_x11_selection_string(string: str) -> None: ...
def get_x11_selection_string() -> str | None: ...
def get_glx_context(window: _GLFWwindowPointerT): ...
def get_glx_window(window: _GLFWwindowPointerT): ...
def get_wayland_display(): ...
def get_wayland_monitor(monitor: _GLFWmonitorPointerT): ...
def get_wayland_window(window: _GLFWwindowPointerT): ...
def get_egl_display(): ...
def get_egl_context(window: _GLFWwindowPointerT): ...
def get_egl_surface(window: _GLFWwindowPointerT): ...
def get_os_mesa_color_buffer(window: _GLFWwindowPointerT) -> tuple[int, int, int, Incomplete]: ...
def get_os_mesa_depth_buffer(window: _GLFWwindowPointerT) -> tuple[int, int, int, Incomplete]: ...
def get_os_mesa_context(window: _GLFWwindowPointerT): ...
def init_allocator(allocate, reallocate, deallocate) -> None: ...
def init_vulkan_loader(loader) -> None: ...
def get_platform() -> int: ...
def platform_supported(platform: int) -> int: ...
def get_window_title(window: _GLFWwindowPointerT) -> str: ...
