# Purpose of the software

Compute error metrics in the logs of student compilation events.

# Repository structure

## Folders

* `data-snapshots`: Complete snapshots of all compilation events. *Author: Maciej Pankiewicz.*
* `data-snapshot-summary`: A summary of snapshots that shows the number of runtime errors *Author: Maciej Pankiewicz.*
* `data-compiler-errors`: All compilation errors. *Author: Maciej Pankiewicz.*
* `data-exceptions`: All runtime errors. *Author: Maciej Pankiewicz.*
* `data-repeated-error-density`: **TODO Maciek: Should this be a subfolder of results? I tried to keep the prefix 'data-' for input source files from which something is computed.**
* `grades`: Student grades from the [Fall 2020 GDrive](https://drive.google.com/drive/u/0/folders/1eh1Vf5ACLN-tuK9S20iOSHv9_PAN4MKX). *Author: ?*
* `results`: Output of `jadud.py`. *Author: Valdemar Švábenský.*

## Files

* `jadud.py`: Compute Jadud's EQ for each student using `data-snapshots` and either `data-compiler-errors` or `data-exceptions`. *Author: Valdemar Švábenský.*
* `learning outcomes RED.R`: Compute Repeated Error Density for each student using `data-snapshots` and `data-errors`. *Author: Maciej Pankiewicz.*
* `use error count to pred grades.Rmd`: SRL-use total error counts to predict learning outcomes. *Author: Joyce Zhang.*
