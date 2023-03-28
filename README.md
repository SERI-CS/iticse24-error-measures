# Application logic

The computation of error metrics looks at consecutive pairs of compilation events and errors in them.

The calculation of EQ is explained on page 6 in this paper:

https://dl.acm.org/doi/pdf/10.1145/1151588.1151600

# File structure

* `data-snapshots`: Complete snapshots of all compilation events. Author: Maciej Pankiewicz.
* `data-errors`: All compilation errors. Author: Maciej Pankiewicz.
* `main.py`: Compute Jadud's EQ for each student using the data about snapshots and errors. Author: Valdemar Švábenský
