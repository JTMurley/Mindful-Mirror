# CHANGELOG
All notable changes to this project will be documented in this file.

## [0.1.1] - 2019-09-01
### Added
- SentenceFormat for Standard module. This automatically adds a new line and "-" for long sentences
- News tab in client GUI, it gets the title of the latest article
- Added configuration.ini for API key change
- Added the option to change DEBUG = True to display logs

### Changed
- Made all text in tkinter label left align instead of middle align
- Weather and News module reads API key from configuration.ini instead of the one in the module

## [0.1.1] - 2019-08-25
### Added
- Shebang line for linux (Python 3)
- Basic functionality for gesture sensor (swipe up to remove, swipe down to show)

### Changed
- Changed to fullscreen instead of overridedirect to allow ALT+F4 to close
- Changed cursor remove method for use in linux system
- Updated README.md

### Removed
- Print statement on code

## [0.1.0] - 2019-08-23
### Added
- Added README.md
- Added CHANGELOG file
- Added Standard module for use with custom modules
- Weather and News now have a .Run() function
- client.py now runs .Run() function of modules located in components/

### Changed
- Changed contents in .gitignore to ignore Python and VS Code
