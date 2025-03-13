# duplicate the template
before starting to write you code, please use this template as sketch.
```sh
# assure you have a shell at the root of the project
cd lib
cp template <module name>
```
then you can have a glances of the file structure:
## file structure
```{list-table}
:header-rows: 1

* - script name
  - purpose

* - 01-info.sh
  - defines the help messages

* - 10-function.sh
  - function implements

* - 90-actions.sh
  - defines action for getopt

* - 99-main.sh
  - the main function
  (also containning the defualt action)
```

## start editing
the file numbering is just as same as edit sequence.
