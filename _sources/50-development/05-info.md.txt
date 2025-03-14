# write down descriptions
```{note}
WIP
```
descriptions located in 01-info.sh.
most part of the descriptions are help messages.

for example:
```sh
export MODULE_NAME="template"
export DESCRIPTION="this is the $MODULE_NAME app, \
manager for apps"
export DESCRIPTION_verbose="\
you see this line since you have verbose mode enabled"
function script_usage() {
cat << EOF 
$MODULE_NAME application
Action list:
    help             - show this help
    install <URL> <name> - install content from given url
    update <name> - update content by name
Default:
    help
EOF
}
```