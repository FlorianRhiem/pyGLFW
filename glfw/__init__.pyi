import ctypes
from _typeshed import Incomplete
from typing import NamedTuple

__version__: str
ERROR_REPORTING: str
NORMALIZE_GAMMA_RAMPS: bool
ffi: Incomplete

class GLFWError(UserWarning):
    error_code: Incomplete
    def __init__(self, message, error_code=None) -> None: ...

class _GLFWwindow(ctypes.Structure): ...
class _GLFWmonitor(ctypes.Structure): ...

class _GLFWvidmode(ctypes.Structure):

    class GLFWvidmode(NamedTuple):
        size: Incomplete
        bits: Incomplete
        refresh_rate: Incomplete

    class Size(NamedTuple):
        width: Incomplete
        height: Incomplete

    class Bits(NamedTuple):
        red: Incomplete
        green: Incomplete
        blue: Incomplete
    width: int
    height: int
    red_bits: int
    green_bits: int
    blue_bits: int
    refresh_rate: int
    def __init__(self) -> None: ...
    def wrap(self, video_mode) -> None: ...
    def unwrap(self): ...

class _GLFWgammaramp(ctypes.Structure):

    class GLFWgammaramp(NamedTuple):
        red: Incomplete
        green: Incomplete
        blue: Incomplete
    red: Incomplete
    red_array: Incomplete
    green: Incomplete
    green_array: Incomplete
    blue: Incomplete
    blue_array: Incomplete
    size: int
    def __init__(self) -> None: ...
    def wrap(self, gammaramp) -> None: ...
    def unwrap(self): ...

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

def init() -> int: ...
def terminate() -> None: ...
def init_hint(hint: int, value: int) -> None: ...
def get_version() -> tuple[int, int, int]: ...
def get_version_string() -> str: ...
def get_error() -> tuple[int, str]: ...
def set_error_callback(cbfun): ...
def get_monitors(): ...
def get_primary_monitor(): ...
def get_monitor_pos(monitor): ...
def get_monitor_workarea(monitor): ...
def get_monitor_physical_size(monitor): ...
def get_monitor_content_scale(monitor): ...
def get_monitor_name(monitor): ...
def set_monitor_user_pointer(monitor, pointer) -> None: ...
def get_monitor_user_pointer(monitor): ...
def set_monitor_callback(cbfun): ...
def get_video_modes(monitor): ...
def get_video_mode(monitor): ...
def set_gamma(monitor, gamma) -> None: ...
def get_gamma_ramp(monitor): ...
def set_gamma_ramp(monitor, ramp) -> None: ...
def default_window_hints() -> None: ...
def window_hint(hint: int, value: int) -> None: ...
def window_hint_string(hint: int, value: str) -> None: ...
def create_window(width: int, height: int, title: str, monitor, share): ...
def destroy_window(window) -> None: ...
def window_should_close(window): ...
def set_window_should_close(window, value) -> None: ...
def set_window_title(window, title) -> None: ...
def get_window_pos(window): ...
def set_window_pos(window, xpos, ypos) -> None: ...
def get_window_size(window): ...
def set_window_size(window, width, height) -> None: ...
def get_framebuffer_size(window): ...
def get_window_content_scale(window): ...
def get_window_opacity(window): ...
def set_window_opacity(window, opacity) -> None: ...
def iconify_window(window) -> None: ...
def restore_window(window) -> None: ...
def show_window(window) -> None: ...
def hide_window(window) -> None: ...
def request_window_attention(window) -> None: ...
def get_window_monitor(window): ...
def get_window_attrib(window, attrib): ...
def set_window_attrib(window, attrib, value) -> None: ...
def set_window_user_pointer(window, pointer) -> None: ...
def get_window_user_pointer(window): ...
def set_window_pos_callback(window, cbfun): ...
def set_window_size_callback(window, cbfun): ...
def set_window_close_callback(window, cbfun): ...
def set_window_refresh_callback(window, cbfun): ...
def set_window_focus_callback(window, cbfun): ...
def set_window_iconify_callback(window, cbfun): ...
def set_window_maximize_callback(window, cbfun): ...
def set_framebuffer_size_callback(window, cbfun): ...
def set_window_content_scale_callback(window, cbfun): ...
def poll_events() -> None: ...
def wait_events() -> None: ...
def get_input_mode(window, mode): ...
def set_input_mode(window, mode, value) -> None: ...
def raw_mouse_motion_supported(): ...
def get_key(window, key): ...
def get_mouse_button(window, button): ...
def get_cursor_pos(window): ...
def set_cursor_pos(window, xpos, ypos) -> None: ...
def set_key_callback(window, cbfun): ...
def set_char_callback(window, cbfun): ...
def set_mouse_button_callback(window, cbfun): ...
def set_cursor_pos_callback(window, cbfun): ...
def set_cursor_enter_callback(window, cbfun): ...
def set_scroll_callback(window, cbfun): ...
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
def set_window_size_limits(window, minwidth, minheight, maxwidth, maxheight) -> None: ...
def set_window_aspect_ratio(window, numer, denom) -> None: ...
def get_window_frame_size(window): ...
def maximize_window(window) -> None: ...
def focus_window(window) -> None: ...
def set_window_monitor(window, monitor, xpos, ypos, width, height, refresh_rate) -> None: ...
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
