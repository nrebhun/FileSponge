# FileSponge [![Build Status](https://travis-ci.org/nrebhun/FileSponge.svg?branch=master)](https://travis-ci.org/nrebhun/FileSponge)
Extracts files duplicated across directories, to keep your projects DRY.

By automatically identifying common files and project structure, projects may be better managed or modularized.

## Installation

1. Clone this repo

## Usage

1. Navigate to project root
2. Modify FileSponge.py, passing in two directories to the `fileSponge` function
3. Run the script:

  `$ python FileSponge.py`

## Features

* compares **two** directories
* compiles a text list of duplicate files found
* copies identified duplicates to a `common` directory
* copied files maintain the organizational structure of the source directory

## System Requirements

* Unix-based OS
* Python >= 2.7

## Planned Improvements

* Accept more than two target directories as input
* Simpler interface (perhaps via [Fabric])
* Optional argument specifying output location (default would be "common" in current dir)
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
[Fabric]: https://get.fabric.io/
[Zach Bush]: https://github.com/zmbush
