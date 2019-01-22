# x-lines

So you want to keep track of how you set up a new system, but you *know* the `.*sh_history` file is already thousands of lines long. This script here will only copy the first x lines (you specify) from any file (you specify). Then, (***not implemented yet***) the script will save the lines to a new files called something like `*sh_history.<time_stamp>`.

_Where \* = your shell (bash, zsh, etc.)_ and `<time_stamp>` is in the format of `%Y-%m-%d-%H-%M-%S`.

Easy enough, right?

## Usage

It's pretty straightforward.

``` shell
$ python copy_x_files.py -h
usage: copy_x_lines.py [-h] [-d] filename lines

positional arguments:
  filename     the file to be copied from
  lines        the number of lines to copy from the beginning of the file

optional arguments:
  -h, --help   show this help message and exit
  -d, --debug  enables some (sparse) debugging features
```

So...

```shell
python copy_x_files.py ~/.zsh_history 50
```

...will copy the first 50 lines of `~/.zsh_history` to `~/zsh_history_<timestamp>`.

And...

```shell
python copy_x_files.py ~/example.txt 100
```

...will copy the first 100 lines of `~/example.txt` to `~/example_<timestamp>.txt`.