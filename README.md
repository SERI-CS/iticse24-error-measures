# Overview

This repository contains supplementary materials for the following conference paper:

[Anonymous authors]\
**Comparison of Three Programming Error Measures for Determining Grades in CS1**\
Submitted to ACM SIGCSE 2024 conference.

The software computes error measures in the logs of student compilation events and builds regression models to explain students' course grades.

## File structure

### Data

Folders:

* `compiler-errors`: All compilation errors. 
* `exceptions`: All runtime errors. 
* `grades`: Student grades.
* `snapshots`: List of snapshots (before autograder evaluation) collected during the study.
* `snapshots-summary`: For each snapshot (after autograder evaluation), indicates the number of compiler and runtime errors, as well as passed and failed test cases.

### Code

Files:

* `jadud.py`: Compute Jadud's EQ for each student using `data/snapshots` and either `data/compiler-errors` or `data/exceptions`.
* `EC jadud RED regression.Rmd`: SRL-use total error counts to predict learning outcomes. 

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
