# edit action list
now you can edit the action list according to the actions 
defined `01-info`

## example
```sh
function parse_action(){
    case "$1" in
        help)
            script_usage
            ;;
        list)
            shift
            LNMP_list $@
            ;;
        install)
            shift
            LNMP_install $@
            ;;
        *)
            script_exit "unknown action $1." 1
            ;;
    esac
}
```