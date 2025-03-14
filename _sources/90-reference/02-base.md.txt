# base module

the base module is always the first module loaded when running frameworker,
it contains fundemental functions and variables for other modules to work.

first part of options is also processed here.

## functions for other modules

### logging
- info_echo()
- verb_echo()
- red_echo()
- error_echo()

### text file utils

- config_check()
- detect_section()
- write_section()
- read_section()

### load additional code
- load_folder()

### permission related
- check_superuser()
- run_as_root()
- 
## function list
### exit handling
- script_trap_err()
- script_trap_exit()
- script_exit()

### init handling
- script_init()
- colour_init()
- cron_init()
- lock_init()
- journal_init()
- parse_params() (overrided)

### logging utils
- pretty_print()
- info_echo()
- verb_echo()
- red_echo()

### checking utils
- build_path()
- check_binary()
- config_check()
- check_superuser()
- run_as_root()

### interactive utils
- ask_yes_no()
- load_folder()