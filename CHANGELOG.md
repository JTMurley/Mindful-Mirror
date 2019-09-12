# CHANGELOG
All notable changes to this project will be documented in this file.

## [0.2.1] - 2019-09-11
### Removed
- Today's min and max temperature
- weather location

## [0.2.0] - 2019-09-10
### Bug Fix
- Fix daily weather bug where it display 1 day later

## [0.2.0] - 2019-09-10
### Added
- Reminder module
- Daily weather (4 days ahead) on Weather module

### Changed
- Weather icon now display moon icon instead of sun icon when the weather is clear and when it is in between 8PM to 8AM

### Bug Fix
- Fixed type image bug where item was referenced before created
- Fixed bug where 12AM is shown as 0AM

## [0.1.3] - 2019-09-09
### Added
- Icons implementation in Weather module
- UpdateImageByTag() method in Standard module
- GetTextByTag() method in Standard module

### Changed
- Renamed some weather icon to make programming much easier
- Changed full month (September) to shorter month (Sep)

### Removed
- Placeholder test.gif

## [0.1.2] - 2019-09-05
### Added
- Time module
- RunSpecial runs every 10 seconds on a new thread for time sentsitive module
- Added Run and RunSpecial to every module

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
