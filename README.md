# Purpose of the software

Compute error metrics in the logs of student compilation events.

# Repository structure

## Folders

### Data

* `compiler-errors`: All compilation errors. *Author: Maciej Pankiewicz.*
* `exceptions`: All runtime errors. *Author: Maciej Pankiewicz.*
* `grades`: Student grades from the [Fall 2020 GDrive](https://drive.google.com/drive/u/0/folders/1eh1Vf5ACLN-tuK9S20iOSHv9_PAN4MKX). *Author: Eric Fouh?*
* `snapshots`: Complete snapshots of all compilation events. *Author: Maciej Pankiewicz.*

### Results

* `error-count`: Contains files with computed number of compiler and runtime errors (exceptions) for each student snapshot *Author: Maciej Pankiewicz.*
* `jadud`: Output of `jadud.py`. Contains files with computed *Jadud's error quotient* (EQ) values for compiler and runtime errors (exceptions) *Author: Valdemar Švábenský.*
* `repeated-error-density`: Contains files with computed *repeated error density* (RED) values for compiler and runtime errors (exceptions) *Author: Maciej Pankiewicz.*

## Files

* `jadud.py`: Compute Jadud's EQ for each student using `data/snapshots` and either `data/compiler-errors` or `data/exceptions`. *Author: Valdemar Švábenský.*
* `learning outcomes RED.R`: Rank-based regression analysis with RED values as predictors of the midterm1, midterm2 and final grade. *Author: Maciej Pankiewicz.*
* `use error count to pred grades.Rmd`: SRL-use total error counts to predict learning outcomes. *Author: Joyce Zhang.*
