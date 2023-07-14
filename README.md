# Overview

This repository contains supplementary materials for the following conference paper:

[Anonymous authors]
**Evaluation and Comparison of Three Programming Error Measures for Explaining Course Grades.**
Submitted to ACM SIGCSE 2024 conference.

The software computes error measures in the logs of student compilation events and builds regression models to explain students' course grades.

## File structure

### Data

* `compiler-errors`: All compilation errors. 
* `exceptions`: All runtime errors. 
* `grades`: Student grades from the [Fall 2020 GDrive](https://drive.google.com/drive/u/0/folders/1eh1Vf5ACLN-tuK9S20iOSHv9_PAN4MKX).
* `snapshots`: Complete snapshots of all compilation events.
* `snapshots-summary`: For each snapshot, indicates the number of compiler and runtime errors, as well as passed and failed test cases.

### Code

* `jadud.py`: Compute Jadud's EQ for each student using `data/snapshots` and either `data/compiler-errors` or `data/exceptions`.
* `red.R`: Rank-based regression analysis with RED values as predictors of the exam 1 and exam 2 grades. 
* `EC jadud RED regression.Rmd`: SRL-use total error counts to predict learning outcomes. 

### Results

* `error-count`: Computed number of compiler and runtime errors (exceptions) for each student snapshot.
* `jadud`: Output of `jadud.py`. Computed *Jadud's error quotient* (EQ) values for compiler and runtime errors (exceptions).
* `repeated-error-density`: Computed *repeated error density* (RED) values for compiler and runtime errors (exceptions).
* `descriptive stats.pdf`: Descriptive statistics of the variables used in the regression models.
* `EC-jadud-RED-regression.pdf`: Full regression modeling results.
