# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Native > 1.5 and Instructor = all and Course = all and Semester > 1.5 | 1 | 0.213474 |
| Course >= 5.5 | 2 | 0.180600 |
| Course < 5.5 and Native < 1.5 | 3 | 0.132353 |
| Native > 1.5 and Instructor = all and Course = all and Semester <= 1.5 | 3 | 0.063579 |
| Native <= 1.5 and Instructor = all and Course = all and Semester > 1.5 | 3 | 0.086022 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Semester <= 1.0 and Course <= 13.0 and Size > 10.0 and Size > 15.0 and Instructor > 22.0 | 3 | 0.049451 |
| Native <= 1.0 and Course <= 5.0 and Semester > 1.0 | 3 | 0.103093 |
| Semester <= 1.0 and Course <= 13.0 and Size > 10.0 and Size > 15.0 | 3 | 0.059179 |
| Course <= 10.0 and Instructor <= 23.0 and Native > 1.0 and Semester > 1.0 and Instructor > 9.0 | 1 | 0.212585 |
| Instructor <= 5.0 and Semester > 1.0 and Instructor > 2.0 | 1 | 0.080000 |
| Instructor > 19.0 | 2 | 0.256839 |
| Native > 1.0 and Semester <= 1.0 and Instructor > 7.0 | 2 | 0.037037 |
| Semester > 1.0 and Instructor <= 8.0 and Size > 30.0 and Size <= 49.0 and Size > 39.0 | 2 | 0.125000 |
| Semester > 1.0 and Size <= 25.0 and Instructor <= 8.0 | 2 | 0.166667 |
| Semester > 1.0 and Native > 1.0 and Size <= 38.0 and Size <= 25.0 and Course <= 22.0 and Course > 13.0 | 3 | 0.151261 |
| Semester > 1.0 and Size <= 25.0 and Native > 1.0 and Instructor <= 11.0 and Course <= 5.0 | 3 | 0.072581 |
| Semester <= 1.0 | 2 | 0.038462 |
| Size <= 24.0 and Native > 1.0 and Instructor <= 11.0 | 2 | 0.080357 |
| Size > 38.0 and Native > 1.0 | 3 | 0.200000 |
| Course <= 11.0 and Size <= 30.0 | 1 | 0.108225 |
| Instructor <= 12.0 and Instructor <= 4.0 | 2 | 0.083333 |
| Instructor > 12.0 and Size > 36.0 and Native > 1.0 | 2 | 0.112500 |
| Instructor <= 12.0 | 2 | 0.142857 |
| Size <= 18.0 | 2 | 0.057143 |
| Size <= 39.0 and Instructor > 15.0 and Native <= 1.0 | 3 | 0.200000 |
| Native <= 1.0 | 1 | 0.133333 |
|  | 3 | 0.538462 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Course <= 2 and Size >= 48 and Native >= 2 | 1 | 0.051546 |
| Course <= 10 and Semester >= 2 and Instructor >= 10 and Size <= 19 and Instructor <= 20 | 1 | 0.089109 |
| Size <= 38 and Native >= 2 and Course <= 11 and Instructor <= 22 and Instructor >= 3 and Size >= 31 | 1 | 0.061224 |
| Size >= 26 and Size <= 30 and Instructor <= 7 | 1 | 0.041667 |
| Instructor >= 13 and Size >= 28 and Size <= 29 and Course <= 18 | 1 | 0.041667 |
| Instructor >= 14 and Size <= 15 and Size >= 12 | 1 | 0.021277 |
| Size >= 21 and Size <= 21 and Native >= 2 | 1 | 0.021277 |
| Size >= 32 and Instructor <= 21 and Instructor >= 21 | 1 | 0.021277 |
| Instructor >= 13 and Instructor <= 14 and Size >= 32 | 1 | 0.014129 |
| Course >= 6 and Course <= 16 and Size <= 27 and Size >= 22 | 2 | 0.147541 |
| Course >= 8 and Instructor <= 9 and Size <= 18 | 2 | 0.087719 |
| Native >= 2 and Size <= 43 and Size >= 42 | 2 | 0.103448 |
| Native >= 2 and Size <= 16 and Course <= 2 | 2 | 0.037037 |
| Native >= 2 and Size <= 10 and Instructor >= 13 | 2 | 0.054545 |
| Course >= 23 | 2 | 0.037037 |
| Course >= 6 and Course <= 18 and Size <= 37 and Size >= 35 | 2 | 0.041667 |
| Instructor <= 2 and Instructor >= 2 | 2 | 0.037037 |
| Size <= 25 and Course <= 2 | 2 | 0.037037 |
| Instructor >= 17 and Size <= 18 and Instructor <= 20 | 2 | 0.037037 |
|  | 3 | 0.770492 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

native|instructor|course|semester|class
---|---|---|---|---
(-inf-1.5]|all|all|(1.5-inf)|3
(1.5-inf)|all|all|(1.5-inf)|1
(-inf-1.5]|all|all|(-inf-1.5]|3
(1.5-inf)|all|all|(-inf-1.5]|3

## JRip

Decision list:

rules | predicted class
---|---
(Course <= 2) and (Size >= 48) and (Native >= 2)|1 (5.0/0.0)
(Course <= 10) and (Semester >= 2) and (Instructor >= 10) and (Size <= 19) and (Instructor <= 20)|1 (9.0/0.0)
(Size <= 38) and (Native >= 2) and (Course <= 11) and (Instructor <= 22) and (Instructor >= 3) and (Size >= 31)|1 (6.0/0.0)
(Size >= 26) and (Size <= 30) and (Instructor <= 7)|1 (4.0/0.0)
(Instructor >= 13) and (Size >= 28) and (Size <= 29) and (Course <= 18)|1 (4.0/0.0)
(Instructor >= 14) and (Size <= 15) and (Size >= 12)|1 (2.0/0.0)
(Size >= 21) and (Size <= 21) and (Native >= 2)|1 (2.0/0.0)
(Size >= 32) and (Instructor <= 21) and (Instructor >= 21)|1 (2.0/0.0)
(Instructor >= 13) and (Instructor <= 14) and (Size >= 32)|1 (7.0/4.0)
(Course >= 6) and (Course <= 16) and (Size <= 27) and (Size >= 22)|2 (9.0/0.0)
(Course >= 8) and (Instructor <= 9) and (Size <= 18)|2 (5.0/0.0)
(Native >= 2) and (Size <= 43) and (Size >= 42)|2 (6.0/0.0)
(Native >= 2) and (Size <= 16) and (Course <= 2)|2 (2.0/0.0)
(Native >= 2) and (Size <= 10) and (Instructor >= 13)|2 (3.0/0.0)
(Course >= 23)|2 (2.0/0.0)
(Course >= 6) and (Course <= 18) and (Size <= 37) and (Size >= 35)|2 (3.0/0.0)
(Instructor <= 2) and (Instructor >= 2)|2 (2.0/0.0)
(Size <= 25) and (Course <= 2)|2 (2.0/0.0)
(Instructor >= 17) and (Size <= 18) and (Instructor <= 20)|2 (2.0/0.0)
|3 (57.0/12.0)


## PART

Decision list:

rules | predicted class
---|---
Semester <= 1.0 AND Course <= 13.0 AND Size > 10.0 AND Size > 15.0 AND Instructor > 22.0|3 (8.0/2.0)
Native <= 1.0 AND Course <= 5.0 AND Semester > 1.0|3 (10.0)
Semester <= 1.0 AND Course <= 13.0 AND Size > 10.0 AND Size > 15.0|3 (7.0)
Course <= 10.0 AND Instructor <= 23.0 AND Native > 1.0 AND Semester > 1.0 AND Instructor > 9.0|1 (35.0/10.0)
Instructor <= 5.0 AND Semester > 1.0 AND Instructor > 2.0|1 (6.0)
Instructor > 19.0|2 (6.0)
Native > 1.0 AND Semester <= 1.0 AND Instructor > 7.0|2 (3.0/1.0)
Semester > 1.0 AND Instructor <= 8.0 AND Size > 30.0 AND Size <= 49.0 AND Size > 39.0|2 (5.0)
Semester > 1.0 AND Size <= 25.0 AND Instructor <= 8.0|2 (7.0)
Semester > 1.0 AND Native > 1.0 AND Size <= 38.0 AND Size <= 25.0 AND Course <= 22.0 AND Course > 13.0|3 (7.0/1.0)
Semester > 1.0 AND Size <= 25.0 AND Native > 1.0 AND Instructor <= 11.0 AND Course <= 5.0|3 (4.0/1.0)
Semester <= 1.0|2 (3.0/1.0)
Size <= 24.0 AND Native > 1.0 AND Instructor <= 11.0|2 (3.0/1.0)
Size > 38.0 AND Native > 1.0|3 (5.0)
Course <= 11.0 AND Size <= 30.0|1 (4.0)
Instructor <= 12.0 AND Instructor <= 4.0|2 (3.0/1.0)
Instructor > 12.0 AND Size > 36.0 AND Native > 1.0|2 (5.0/2.0)
Instructor <= 12.0|2 (3.0)
Size <= 18.0|2 (2.0)
Size <= 39.0 AND Instructor > 15.0 AND Native <= 1.0|3 (2.0)
Native <= 1.0|1 (3.0/1.0)
|3 (3.0/1.0)


## SimpleCart Decision Tree

* Course < 5.5
	* Native < 1.5: 3(15.0/2.0)
	* Native >= 1.5
		* Semester < 1.5: 3(8.0/3.0)
		* Semester >= 1.5: 1(27.0/16.0)
* Course >= 5.5: 2(32.0/31.0)


