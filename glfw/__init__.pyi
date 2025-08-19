from collections.abc import Callable
import ctypes
from _typeshed import Incomplete
from typing import NamedTuple
from cffi import FFI

__version__: str
ERROR_REPORTING: str
NORMALIZE_GAMMA_RAMPS: bool
ffi: FFI

class GLFWError(UserWarning):
    error_code: int
    def __init__(self, message: str, error_code: int | None = None) -> None: ...

class _GLFWwindow(ctypes.Structure): ...
class _GLFWmonitor(ctypes.Structure): ...

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

    def __init__(self) -> None: ...
    def wrap(self, video_mode: GLFWvidmode) -> None: ...
    def unwrap(self) -> GLFWvidmode: ...

class _GLFWgammaramp(ctypes.Structure):
    class GLFWgammaramp(NamedTuple):
        red: int
        green: int
        blue: int

    def __init__(self) -> None: ...
    def wrap(self, gammaramp: GLFWgammaramp) -> None: ...
    def unwrap(self) -> GLFWgammaramp: ...

class _GLFWcursor(ctypes.Structure): ...

class _GLFWimage(ctypes.Structure):
    class GLFWimage(NamedTuple):
        width: Incomplete
        height: Incomplete
        pixels: Incomplete

    width: int
    height: int
    pixels: Incomplete
    pixels_array: Incomplete
    def __init__(self) -> None: ...
    def wrap(self, image) -> None: ...
    def unwrap(self): ...

class _GLFWgamepadstate(ctypes.Structure):
    class GLFWgamepadstate(NamedTuple):
        buttons: Incomplete
        axes: Incomplete

    buttons: Incomplete
    axes: Incomplete
    def __init__(self) -> None: ...
    def wrap(self, gamepad_state) -> None: ...
    def unwrap(self): ...

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
HAT_RIGHT_UP = HAT_RIGHT | HAT_UP
HAT_RIGHT_DOWN = HAT_RIGHT | HAT_DOWN
HAT_LEFT_UP = HAT_LEFT | HAT_UP
HAT_LEFT_DOWN = HAT_LEFT | HAT_DOWN
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

class _GLFWallocator(ctypes.Structure): ...

### Custom types used for type checking only
# Types copied to global namespace
type GLFWvidmode = _GLFWvidmode.GLFWvidmode
type GLFWgammaramp = _GLFWgammaramp.GLFWgammaramp

type GLFWmonitor_pointer = ctypes._Pointer[_GLFWmonitor]
type GLFWwindow_pointer = ctypes._Pointer[_GLFWwindow]

type GLFWerrorfun = Callable[[int, str], None]
type GLFWwindowposfun = Callable[[GLFWwindow_pointer, int, int], None]
type GLFWwindowsizefun = Callable[[GLFWwindow_pointer, int, int], None]
type GLFWwindowclosefun = Callable[[GLFWwindow_pointer], None]
type GLFWwindowrefreshfun = Callable[[GLFWwindow_pointer], None]
type GLFWwindowfocusfun = Callable[[GLFWwindow_pointer, int], None]
type GLFWwindowiconifyfun = Callable[[GLFWwindow_pointer, int], None]
type GLFWwindowmaximizefun = Callable[[GLFWwindow_pointer, int], None]
type GLFWframebuffersizefun = Callable[[GLFWwindow_pointer, int, int], None]
type GLFWwindowcontentscalefun = Callable[[GLFWwindow_pointer, float, float], None]

type GLFWmousebuttonfun = Callable[[GLFWwindow_pointer, int, int, int], None]
type GLFWcursorposfun = Callable[[GLFWwindow_pointer, float, float], None]
type GLFWcursorenterfun = Callable[[GLFWwindow_pointer, int], None]
type GLFWscrollfun = Callable[[GLFWwindow_pointer, float, float], None]
type GLFWkeyfun = Callable[[GLFWwindow_pointer, int, int, int, int], None]
type GLFWcharfun = Callable[[GLFWwindow_pointer, int], None]
type GLFWmonitorfun = Callable[[GLFWmonitor_pointer, int], None]
type GLFWdropfun = Callable[[GLFWwindow_pointer, int, str], None]
type GLFWcharmodsfun = Callable[[GLFWwindow_pointer, int, int], None]
type GLFWjoystickfun = Callable[[int, int], None]
### End of custom types

def init() -> int: ...
def terminate() -> None: ...
def init_hint(hint: int, value: int) -> None: ...
def get_version() -> tuple[int, int, int]: ...
def get_version_string() -> str: ...
def get_error() -> tuple[int, str]: ...
def set_error_callback(cbfun: GLFWerrorfun) -> GLFWerrorfun | None: ...
def get_monitors() -> list[GLFWmonitor_pointer]: ...
def get_primary_monitor() -> GLFWmonitor_pointer: ...
def get_monitor_pos(monitor: GLFWmonitor_pointer) -> tuple[int, int]: ...
def get_monitor_workarea(monitor: GLFWmonitor_pointer) -> tuple[int, int, int, int]: ...
def get_monitor_physical_size(monitor: GLFWmonitor_pointer) -> tuple[int, int]: ...
def get_monitor_content_scale(monitor: GLFWmonitor_pointer) -> tuple[float, float]: ...
def get_monitor_name(monitor: GLFWmonitor_pointer) -> str: ...
def set_monitor_user_pointer(monitor: GLFWmonitor_pointer, pointer: object) -> None: ...
def get_monitor_user_pointer(monitor: GLFWmonitor_pointer) -> object: ...
def set_monitor_callback(cbfun: GLFWmonitorfun) -> GLFWmonitorfun | None: ...
def get_video_modes(monitor: GLFWmonitor_pointer) -> list[GLFWvidmode]: ...
def get_video_mode(monitor: GLFWmonitor_pointer) -> GLFWvidmode: ...
def set_gamma(monitor: GLFWmonitor_pointer, gamma: float) -> None: ...
def get_gamma_ramp(monitor: GLFWmonitor_pointer) -> GLFWgammaramp: ...
def set_gamma_ramp(monitor: GLFWmonitor_pointer, ramp: GLFWgammaramp) -> None: ...
def default_window_hints() -> None: ...
def window_hint(hint: int, value: int) -> None: ...
def window_hint_string(hint: int, value: str) -> None: ...
def create_window(
    width: int,
    height: int,
    title: str,
    monitor: GLFWmonitor_pointer | None,
    share: GLFWwindow_pointer | None,
) -> GLFWwindow_pointer: ...
def destroy_window(window: GLFWwindow_pointer) -> None: ...
def window_should_close(window: GLFWwindow_pointer) -> int: ...
def set_window_should_close(window: GLFWwindow_pointer, value: int) -> None: ...
def set_window_title(window: GLFWwindow_pointer, title: str) -> None: ...
def get_window_pos(window: GLFWwindow_pointer) -> tuple[int, int]: ...
def set_window_pos(window: GLFWwindow_pointer, xpos: int, ypos: int) -> None: ...
def get_window_size(window: GLFWwindow_pointer) -> tuple[int, int]: ...
def set_window_size(window: GLFWwindow_pointer, width: int, height: int) -> None: ...
def get_framebuffer_size(window: GLFWwindow_pointer) -> tuple[int, int]: ...
def get_window_content_scale(window: GLFWwindow_pointer) -> tuple[float, float]: ...
def get_window_opacity(window: GLFWwindow_pointer) -> float: ...
def set_window_opacity(window: GLFWwindow_pointer, opacity: float) -> None: ...
def iconify_window(window: GLFWwindow_pointer) -> None: ...
def restore_window(window: GLFWwindow_pointer) -> None: ...
def show_window(window: GLFWwindow_pointer) -> None: ...
def hide_window(window: GLFWwindow_pointer) -> None: ...
def request_window_attention(window: GLFWwindow_pointer) -> None: ...
def get_window_monitor(window: GLFWwindow_pointer) -> GLFWmonitor_pointer: ...
def get_window_attrib(window: GLFWwindow_pointer, attrib: int) -> int: ...
def set_window_attrib(window: GLFWwindow_pointer, attrib: int, value: int) -> None: ...
def set_window_user_pointer(window: GLFWwindow_pointer, pointer: object) -> None: ...
def get_window_user_pointer(window: GLFWwindow_pointer) -> object: ...
def set_window_pos_callback(
    window: GLFWwindow_pointer, cbfun: GLFWwindowposfun
) -> GLFWwindowposfun | None: ...
def set_window_size_callback(
    window: GLFWwindow_pointer, cbfun: GLFWwindowsizefun
) -> GLFWwindowsizefun | None: ...
def set_window_close_callback(
    window: GLFWwindow_pointer, cbfun: GLFWwindowclosefun
) -> GLFWwindowclosefun | None: ...
def set_window_refresh_callback(
    window: GLFWwindow_pointer, cbfun: GLFWwindowrefreshfun
) -> GLFWwindowrefreshfun | None: ...
def set_window_focus_callback(
    window: GLFWwindow_pointer, cbfun: GLFWwindowfocusfun
) -> GLFWwindowfocusfun | None: ...
def set_window_iconify_callback(
    window: GLFWwindow_pointer, cbfun: GLFWwindowiconifyfun
) -> GLFWwindowiconifyfun | None: ...
def set_window_maximize_callback(
    window: GLFWwindow_pointer, cbfun: GLFWwindowmaximizefun
) -> GLFWwindowmaximizefun | None: ...
def set_framebuffer_size_callback(
    window: GLFWwindow_pointer, cbfun: GLFWframebuffersizefun
) -> GLFWframebuffersizefun | None: ...
def set_window_content_scale_callback(
    window: GLFWwindow_pointer, cbfun: GLFWwindowcontentscalefun
) -> GLFWwindowcontentscalefun | None: ...
def poll_events() -> None: ...
def wait_events() -> None: ...
def get_input_mode(window: GLFWwindow_pointer, mode: int) -> int: ...
def set_input_mode(window: GLFWwindow_pointer, mode: int, value: int) -> None: ...
def raw_mouse_motion_supported() -> bool: ...
def get_key(window: GLFWwindow_pointer, key: int) -> int: ...
def get_mouse_button(window: GLFWwindow_pointer, button: int) -> int: ...
def get_cursor_pos(window: GLFWwindow_pointer) -> tuple[float, float]: ...
def set_cursor_pos(window: GLFWwindow_pointer, xpos: float, ypos: float) -> None: ...
def set_key_callback(
    window: GLFWwindow_pointer, cbfun: GLFWkeyfun
) -> GLFWkeyfun | None: ...
def set_char_callback(
    window: GLFWwindow_pointer, cbfun: GLFWcharfun
) -> GLFWcharfun | None: ...
def set_mouse_button_callback(
    window: GLFWwindow_pointer, cbfun: GLFWmousebuttonfun
) -> GLFWmousebuttonfun | None: ...
def set_cursor_pos_callback(
    window: GLFWwindow_pointer, cbfun: GLFWcursorposfun
) -> GLFWcursorposfun | None: ...
def set_cursor_enter_callback(
    window: GLFWwindow_pointer, cbfun: GLFWcursorenterfun
) -> GLFWcursorenterfun | None: ...
def set_scroll_callback(
    window: GLFWwindow_pointer, cbfun: GLFWscrollfun
) -> GLFWscrollfun | None: ...
def joystick_present(joy): ...
def get_joystick_axes(joy): ...
def get_joystick_buttons(joy): ...
def get_joystick_hats(joystick_id): ...
def get_joystick_name(joy): ...
def get_joystick_guid(joystick_id): ...
def set_joystick_user_pointer(joystick_id, pointer) -> None: ...
def get_joystick_user_pointer(joystick_id): ...
def joystick_is_gamepad(joystick_id): ...
def get_gamepad_state(joystick_id): ...
def set_clipboard_string(window, string) -> None: ...
def get_clipboard_string(window): ...
def get_time(): ...
def set_time(time) -> None: ...
def make_context_current(window) -> None: ...
def get_current_context(): ...
def swap_buffers(window) -> None: ...
def swap_interval(interval) -> None: ...
def extension_supported(extension): ...
def get_proc_address(procname): ...
def set_drop_callback(window, cbfun): ...
def set_char_mods_callback(window, cbfun): ...
def vulkan_supported(): ...
def get_required_instance_extensions(): ...
def get_timer_value(): ...
def get_timer_frequency(): ...
def set_joystick_callback(cbfun): ...
def update_gamepad_mappings(string): ...
def get_gamepad_name(joystick_id): ...
def get_key_name(key, scancode): ...
def get_key_scancode(key): ...
def create_cursor(image, xhot, yhot): ...
def create_standard_cursor(shape): ...
def destroy_cursor(cursor) -> None: ...
def set_cursor(window, cursor) -> None: ...
def create_window_surface(instance, window, allocator, surface): ...
def get_physical_device_presentation_support(instance, device, queuefamily): ...
def get_instance_proc_address(instance, procname): ...
def set_window_icon(window, count, images) -> None: ...
def set_window_size_limits(
    window, minwidth, minheight, maxwidth, maxheight
) -> None: ...
def set_window_aspect_ratio(window, numer, denom) -> None: ...
def get_window_frame_size(window): ...
def maximize_window(window) -> None: ...
def focus_window(window) -> None: ...
def set_window_monitor(
    window, monitor, xpos, ypos, width, height, refresh_rate
) -> None: ...
def wait_events_timeout(timeout) -> None: ...
def post_empty_event() -> None: ...
def get_win32_adapter(monitor): ...
def get_win32_monitor(monitor): ...
def get_win32_window(window): ...
def get_wgl_context(window): ...
def get_cocoa_monitor(monitor): ...
def get_cocoa_window(window): ...
def get_nsgl_context(window): ...
def get_x11_display(): ...
def get_x11_adapter(monitor): ...
def get_x11_monitor(monitor): ...
def get_x11_window(window): ...
def set_x11_selection_string(string) -> None: ...
def get_x11_selection_string(): ...
def get_glx_context(window): ...
def get_glx_window(window): ...
def get_wayland_display(): ...
def get_wayland_monitor(monitor): ...
def get_wayland_window(window): ...
def get_egl_display(): ...
def get_egl_context(window): ...
def get_egl_surface(window): ...
def get_os_mesa_color_buffer(window): ...
def get_os_mesa_depth_buffer(window): ...
def get_os_mesa_context(window): ...
def init_allocator(allocate, reallocate, deallocate) -> None: ...
def init_vulkan_loader(loader) -> None: ...
def get_platform(): ...
def platform_supported(platform): ...
def get_window_title(window): ...
