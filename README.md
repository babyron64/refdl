# refdl

Build a reference tree in your environment. You can build up a directory tree by specifying it in conf.yaml file.

## Usage
Prepare the conf.yaml file and just execute refdl.py in the same directory.
```
./refdl.py
```

## Prerequisit
- Python version 3 or higher
- PyYaml (https://github.com/yaml/pyyaml)

## conf.yaml syntax
The directory where references to be installed is specified by the key of mappings, whose value is also mappings. When the value is a string, refdl recognize it as url to a reference and try 'wget' to download it into the file, named as the key. Empty directories are not created.

```
dir name:
  [mappings]
file name: [string]
```
where \[mappings\] includes no or more entries shown above.

### Example
```conf.yaml
root:
  sub1:
    ref1: "https://..../sample1.pdf"
    ref2: "http://..../sample2.html"
  sub2:
root2:
  ref3: "https://....../sample3.jpg"
```
will build a directory tree below on the current directory
```
./ 
  |- root
     |- sub1
        |- ref1
        |- ref2
  |- root2
     |- ref3
```
ref1 : sample1.pdf

ref2 : sample2.html

ref3 : sample3.jpg
