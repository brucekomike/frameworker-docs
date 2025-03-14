# duplicate the template
before starting to write you code, you can duplicate the template to a new module.
````{tab} sketcher
```sh
# assure you have a shell at the root of the project
./frameworker template sketch <name>
```
````
````{tab} manually
```sh
# assure you have a shell at the root of the project
cd lib
cp template <module name>
```
````

then you can have a glances of the file structure:
## file structure
```{list-table}
:header-rows: 1

* - script name
  - purpose

* - 01-info.sh
  - defines module info and help messages

* - 10-function.sh
  - function implements

* - 90-actions.sh
  - defines action for getopt

* - 95-default-action.sh
  - defines the default action

* - 99-main.sh
  - the main function

```

## start editing
the file numbering is just as same as edit sequence.
