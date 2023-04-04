# Purpose of the software

Compute error metrics in the logs of student compilation events.

# File structure

* `data-snapshots`: Complete snapshots of all compilation events. *Author: Maciej Pankiewicz.*
* `data-errors`: All compilation errors. *Author: Maciej Pankiewicz.*
* `results`: Output of `jadud.py`. *Author: Valdemar Švábenský.*
* `jadud.py`: Compute Jadud's EQ for each student using `data-snapshots` and `data-errors`. *Author: Valdemar Švábenský.*
* `use error count to pred grades.Rmd`: SRL-use total error counts to predict learning outcomes. *Author: Joyce Zhang.*
