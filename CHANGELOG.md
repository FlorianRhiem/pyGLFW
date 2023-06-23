# Changelog

All notable changes to this project will be documented in this file.

For information on changes in GLFW itself, see the [GLFW version history](https://www.glfw.org/changelog.html).

## [2.6.0] - 2023-06-23
- Use multiprocessing for library version detection on non-Windows systems

## [2.5.9] - 2023-04-01
- Fixed package version in CHANGELOG.md and glfw/__init__.py

## [2.5.8] - 2023-04-01
- Added more wrappers for unreleased macros

## [2.5.7] - 2023-03-15
- Added support for PYGLFW_LIBRARY_VARIANT

## [2.5.6] - 2023-02-01
- Added warnings for deprecated functions

## [2.5.5] - 2022-09-07
- Added wrappers for unreleased macros
- Fixed set_monitor_user_pointer and get_monitor_user_pointer

## [2.5.4] - 2022-07-23
- Updated to GLFW 3.3.8

## [2.5.3] - 2022-04-09
- Updated to GLFW 3.3.7

## [2.5.2] - 2022-04-01
- Fixed swapped HAT_DOWN and HAT_RIGHT constants

## [2.5.1] - 2022-02-27
- Updated to GLFW 3.3.6

## [2.5.0] - 2021-12-18
- Added /usr/lib/arm-linux-gnueabihf to library search paths

## [2.4.0] - 2021-11-07
- Added macOS wheels for arm64
- Added wrappers for unreleased macros and functions
- Updated to GLFW 3.3.5

## [2.3.0] - 2021-10-01
- Added /opt/homebrew/lib to library search paths

## [2.2.0] - 2021-09-09
- Added Linux wheels for aarch64
- Updated to GLFW 3.3.4

## [2.1.0] - 2021-02-28
- Updated to GLFW 3.3.3

## [2.0.0] - 2020-10-04
- Changed default error reporting method to warn
- Allow dict for ERROR_REPORTING

## [1.12.0] - 2020-07-10
- Added support for CFFI pointers for Vulkan objects

## [1.11.2] - 2020-06-03
- Fixed missing parameter in set_window_opacity
- Replaced non-ASCII whitespace

## [1.11.1] - 2020-05-15
- Fixed a TypeError in _GLFWgamepadstate

## [1.11.0] - 2020-02-21
- Updated to GLFW 3.3.2
- Include support for both X11 and Wayland libraries in the wheel

## [1.10.1] - 2020-01-21
- Fixed default error callback name

## [1.10.0] - 2020-01-19
- Added more options to error reporting

## [1.9.1] - 2020-01-08
- Added conda search path for Windows

## [1.9.0] - 2019-12-30
- Added wrappers for native functions

## [1.8.7] - 2019-12-10
- Fixed glfwGetMonitorContentScale

## [1.8.6] - 2019-12-09
- Added macOS wheels
- Added Microsoft Visual C++ runtime libraries to Windows wheels

## [1.8.5] - 2019-11-28
- Added /usr/lib/aarch64-linux-gnu/ to library search paths

## [1.8.4] - 2019-11-04
- Fix pointer types in get_window_content_scale

## [1.8.3] - 2019-08-22
- Updated the GLFW version in the wheels to 3.3

## [1.8.2] - 2019-07-06
- Added the sys.prefix/lib to the search path

## [1.8.1] - 2019-05-21
- Added the changelog back to the source distribution

## [1.8.0] - 2019-05-11
- Update for GLFW 3.3
- Fixed typo `set_get_window_frame_size`

## [1.7.1] - 2019-02-02
- Fixed exception re-raising for Python 2

## [1.7.0] - 2018-07-09
- Added glfw.GLFW for the naming convention used by the GLFW C API

## [1.6.0] - 2018-03-30
- Added NORMALIZE_GAMMA_RAMPS
- Use namedtuples for structs
- Moved library loading to glfw.library

## [1.5.1] - 2018-01-24
- Improved packaging

## [1.5.0] - 2018-01-09
- Fixed a bug in set_window_icon
- Added support for PIL/pillow Image objects

## [1.4.0] - 2017-02-22
- Improved library search paths

## [1.3.0] - 2016-07-28
- Improved error and exception handling

## [1.2.0] - 2016-06-17
- Update for GLFW 3.2

## [1.0.0] - 2014-03-23
- Initial release.
