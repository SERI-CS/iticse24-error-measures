library(dplyr)
library(Rfit)
# setwd("~/IdeaProjects/error-analysis") # set working directory

RED <- read.csv("./results/RED.csv", sep = ";")

courseGrades <- read.csv("./grades/CourseGrades.csv")
midterm1 <- read.csv("./grades/Midterm1_Fall_2020.csv")
midterm2 <- read.csv("./grades/Midterm2_Fall_2020.csv")

names(courseGrades) <- c("student", "grade")
names(midterm1) <- c("student", "midterm1")
names(midterm2) <- c("student", "midterm2")

courseGrades$grade <- as.numeric(as.character(courseGrades$grade))

f20_data <-
  inner_join(
    midterm1,
    midterm2,
    by = "student") %>%
    inner_join(courseGrades,by="student") %>%
    inner_join(RED, by="student")

f20_data <- na.omit(f20_data)

print("MIDTERM1 - RED runtime + compiler 03 04")

summary(
  rfit(
    f20_data$midterm1 ~
      f20_data$RED.compiler.hw03 +
        f20_data$RED.compiler.hw04 +
        f20_data$RED.exceptions.hw03 +
        f20_data$RED.exceptions.hw04
  ))

print("MIDTERM1 - AVG RED runtime + compiler 03 04")

summary(
  rfit(
    f20_data$midterm1 ~
      f20_data$AvgREDCompiler_HW04 +
        f20_data$AvgREDRuntime_HW04
  ))
print("MIDTERM1 - SUM RED runtime + compiler 03 04")

summary(
  rfit(
    f20_data$midterm1 ~
      f20_data$SumREDCompiler_HW04 +
        f20_data$SumREDRuntime_HW04
  ))

print("MIDTERM2 - RED runtime + compiler 03-08")

summary(
  rfit(
    f20_data$midterm2 ~
      f20_data$RED.compiler.hw03 +
        f20_data$RED.compiler.hw04 +
        f20_data$RED.compiler.hw05 +
        f20_data$RED.compiler.hw06 +
        f20_data$RED.compiler.hw07 +
        f20_data$RED.compiler.hw08 +
        f20_data$RED.exceptions.hw03 +
        f20_data$RED.exceptions.hw04 +
        f20_data$RED.exceptions.hw05 +
        f20_data$RED.exceptions.hw06 +
        f20_data$RED.exceptions.hw07 +
        f20_data$RED.exceptions.hw08
  ))

print("MIDTERM2 - AVG RED runtime + compiler 03-08")

summary(
  rfit(
    f20_data$midterm2 ~
      f20_data$AvgREDCompiler_HW08 +
        f20_data$AvgREDRuntime_HW08
  ))
print("MIDTERM2 - SUM RED runtime + compiler 03-08")

summary(
  rfit(
    f20_data$midterm2 ~
      f20_data$SumREDCompiler_HW08 +
        f20_data$SumREDRuntime_HW08
  ))

print("FINAL GRADE - RED runtime + compiler 03-08")

summary(
  rfit(
    f20_data$grade ~
      f20_data$RED.compiler.hw03 +
        f20_data$RED.compiler.hw04 +
        f20_data$RED.compiler.hw05 +
        f20_data$RED.compiler.hw06 +
        f20_data$RED.compiler.hw07 +
        f20_data$RED.compiler.hw08 +
        f20_data$RED.exceptions.hw03 +
        f20_data$RED.exceptions.hw04 +
        f20_data$RED.exceptions.hw05 +
        f20_data$RED.exceptions.hw06 +
        f20_data$RED.exceptions.hw07 +
        f20_data$RED.exceptions.hw08
  ))

print("FINAL GRADE - AVG RED runtime + compiler 03-08")

summary(
  rfit(
    f20_data$grade ~
      f20_data$AvgREDCompiler_HW08 +
        f20_data$AvgREDRuntime_HW08
  ))
print("FINAL GRADE - SUM RED runtime + compiler 03-08")

summary(
  rfit(
    f20_data$grade ~
      f20_data$SumREDCompiler_HW08 +
        f20_data$SumREDRuntime_HW08
  ))
