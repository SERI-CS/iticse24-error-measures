# Overview

This repository contains supplementary materials for the following conference paper:

Valdemar Švábenský, Maciej Pankiewicz, Jiayi Zhang, Elizabeth B. Cloude, Ryan S. Baker, and Eric Fouh.\
**Comparison of Three Programming Error Measures for Explaining Variability in CS1 Grades**\
In Proceedings of the 29th Conference on Innovation and Technology in Computer Science Education (ITiCSE 2024).\
https://doi.org/10.1145/3649217.3653563

Preprint available at: https://arxiv.org/abs/2404.05988

# Contents of the repository

The software computes error measures in the logs of student compilation events and builds regression models to explain students' course grades.

## File structure

### Data

Folders:

* `compiler-errors`: All compilation errors. Also includes a test file used by `jadud.py` that can be ignored.
* `exceptions`: All runtime errors. 
* `grades`: Student grades.
* `snapshots`: List of snapshots (before autograder evaluation) collected during the study. Also includes a test file used by `jadud.py` that can be ignored.
* `snapshots-summary`: For each snapshot (after autograder evaluation), indicates the number of compiler and runtime errors, as well as passed and failed test cases.

### Code

Files:

* `jadud.py`: Compute Jadud's EQ for each student using `data/snapshots` and either `data/compiler-errors` or `data/exceptions`.
* `repeated-error-density-process-errors.xml`: Compute RED for each student using `data/snapshots` and either `data/compiler-errors` or `data/exceptions`.
* `EC jadud RED regression.Rmd`: Use error metrics to predict learning outcomes. 

### Results

Folders:

* `error-count`: Computed number of compiler and runtime errors (exceptions) for each student snapshot.
* `jadud`: Output of `jadud.py`. Computed *Jadud's error quotient* (EQ) values for compiler and runtime errors (exceptions).
* `repeated-error-density`: Computed *repeated error density* (RED) values for compiler and runtime errors (exceptions).

Files:

* `descriptive stats.pdf`: Descriptive statistics of all variables used in the regression models.
* `correlation between error measures.pdf`: Correlations of the feature variables used in the regression models.
* `EC-jadud-RED-regression.pdf`: Full regression modeling results.
* `BIC.xlsx`: Computation of the BIC' for the regression models.

# How to cite

If you use or build upon the materials, please use the BibTeX entry below to cite the original paper (not only this web link).

```bibtex
@inproceedings{Svabensky2024comparison,
    author    = {\v{S}v\'{a}bensk\'{y}, Valdemar and Pankiewicz, Maciej and Zhang, Jiayi and Cloude, Elizabeth B. and Baker, Ryan S. and Fouh, Eric},
    title     = {{Comparison of Three Programming Error Measures for Explaining Variability in CS1 Grades}},
    booktitle = {Proceedings of the 29th Conference on Innovation and Technology in Computer Science Education},
    series    = {ITiCSE '24},
    publisher = {Association for Computing Machinery},
    address   = {New York, NY, USA},
    year      = {2024},
    numpages  = {7},
    isbn      = {979-8-4007-0600-4/24/07},
    url       = {https://doi.org/10.1145/3649217.3653563},
    doi       = {10.1145/3649217.3653563},
}
```
