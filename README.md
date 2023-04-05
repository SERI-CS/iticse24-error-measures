# Purpose of the software

Compute error metrics in the logs of student compilation events.

# File structure

* `data-snapshots`: Complete snapshots of all compilation events. *Author: Maciej Pankiewicz.*
* `data-errors`: All compilation errors. *Author: Maciej Pankiewicz.*
* `grades`: Student grades from the [Fall 2020 GDrive](https://drive.google.com/drive/u/0/folders/1eh1Vf5ACLN-tuK9S20iOSHv9_PAN4MKX). *Author: ?*
* `results`: Output of `jadud.py`. *Author: Valdemar Švábenský.*
* `jadud.py`: Compute Jadud's EQ for each student using `data-snapshots` and `data-errors`. *Author: Valdemar Švábenský.*
* `use error count to pred grades.Rmd`: SRL-use total error counts to predict learning outcomes. *Author: Joyce Zhang.*
