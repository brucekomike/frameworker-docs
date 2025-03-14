# basic loader

the basic loader (i.e. `frameworker`), have several code structure for loading modules.
## structure

- macos tweak
- action_loader definition
- load base module
- load given action

## action_loader
the function action_loader will load all `.sh` scripts in a given folder.
## macos tweak
the script will detect system name(darwin), and use the homebrew gnu-getopt.