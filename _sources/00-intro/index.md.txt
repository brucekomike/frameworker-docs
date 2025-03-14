# introduction
this project is a set of bash scripts that containning various functions 
intended to be used performing common tasks, as the ultimate solution
created by myself to solve repeating tasks in an extreamlly familiar way.

domain specific codes can be places into the `lib` folder and share 
a common function base with all other tools.
## quick start
clone this repo
```
git clone https://github.com/brucekomike/frameworker 
cd frameworker
```
run the main script (make sure you have bash)
```
./frameworker --help
```
list actions
```
./frameworker list
```
## usage
command struction is as below:
```
./frameworker [options] <action> [action options]
```
to show help for the frameworker itself:
```
./frameworker help # or --help
```
```{note}
therefore the action name help is reserved by frameworker
```
to show help for an action:
```
./frameworker <action> 
```