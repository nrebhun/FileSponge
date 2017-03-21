# FileSponge
Extracts files duplicated across directories, to keep your projects DRY.

By automatically identifying common files and project structure, projects may be better managed or modularized.

## Installation

1. Clone this repo

## Usage

`$ ./filesponge "foo/" "bar/"`
  * for assistance, run with `-h` or flail helplessly

## Features

* compares **two** directories
* outputs identified duplicates to `STDOUT` or a directory specified with `-o`
* copied files maintain the organizational structure of the source directory

## System Requirements

* Unix-based OS
* Python >= 2.7

## Change Log

#### v0.2.0
* Add simpler CLI usage and a help menu (thanks, [argparse])
* Add directory minimum of two, with partial support for handling more
* Add support for optional output target, default is `STDOUT`
* Add caring about versioning, apparently

#### v0.1.0
* Initial functionality, accepting strictly two directories for comparison
* Admittedly terrible usage

## Planned Improvements

* Process more than two input directories
* Cleanup option, to remove original files after duplication to the "common" folder
* Allow for a range of acceptable similarity, where files which differ by less than `n`% are
identified and copied to a different output location for simple evaluation
* An "import" function for the "acceptable similarity range" feature. Once the user is satisfied
with any changes made to the files identified, this function can be run to first move those into the
"common" dir, then remove them from their original locations

<!--
## Fun Facts

* Name and core concept stem from an amazing friend, [Zach Bush], who first pun'd to me the term _"sponge"_ with the phrase _"keep your code DRY."_
-->

<!-- Links! -->
[argparse]: https://docs.python.org/2/library/argparse.html
[Zach Bush]: https://github.com/zmbush
