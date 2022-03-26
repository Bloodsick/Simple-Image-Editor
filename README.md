# Simple Image Editor

The program is written in *Python* and it's a simple project to study image processing with *multithreading*.

## Excecution

To run this program there are two ways.

### With .json:
The first one is to provide a .json list which will contain the following:
1. The path of the file with a key named *File*.
2. The operation you want to run with a key named *Operation*. The operations supported by the program are:
   - rotate-90
   - rotate-180
   - rotate-270
   - mirror
   - flip
   - brightness (The *brightness* operation will need an extra key named *Factor*. If the Factor is 0 the image will be black and 1 is the default brightness.)

Here is an *example* of the .json file:

``` json
[
    {
      "File":"A:/ImageFolder/Image1.jpeg",
      "Operation":"rotate-90"
    },
    {
        "File":"A:/ImageFolder/Image2.png",
        "Operation":"mirror"
    },
    {
        "File":"A:/ImageFolder/Image3.png",
        "Operation":"brightness",
        "Factor":0.6
    }
  ]
  ```

### With Terminal Arguments:

Under normal and not buggy windows circumstances you can type:
`imageeditor.py Path\to\Image operation`

If you want to use the operation *brightness*:
`imageeditor.py Path\to\Image brightness:factor`