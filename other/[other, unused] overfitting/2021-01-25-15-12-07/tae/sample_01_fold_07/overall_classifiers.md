# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Semester > 1.5 and Size = all | 2 | 0.250627 |
| Semester <= 1.5 and Size = all | 3 | 0.107656 |
| Semester > 1.5 and Size <= 47 and Course <= 5.5 and Instructor > 14 and Size <= 24.5 | 1 | 0.059981 |
| Semester > 1.5 and Size <= 47 and Course > 5.5 and Course > 20.5 | 3 | 0.049495 |
| Semester > 1.5 and Size <= 47 and Course > 5.5 and Course <= 20.5 and Course <= 13.5 and Size > 25.5 | 1 | 0.027174 |
| Semester > 1.5 and Size <= 47 and Course <= 5.5 and Instructor <= 14 and Size > 25 | 1 | 0.043440 |
| Semester > 1.5 and Size > 47 | 1 | 0.040529 |
| Semester > 1.5 and Size <= 47 and Course > 5.5 and Course <= 20.5 and Course > 13.5 and Size <= 36.5 | 3 | 0.018824 |
| Semester > 1.5 and Size <= 47 and Course <= 5.5 and Instructor > 14 and Size > 24.5 | 1 | 0.023148 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Semester <= 1.5 | 3 | 0.107656 |
| Native <= 1.5 | 3 | 0.059809 |
| Course <= 10.5 and Instructor > 21.5 | 2 | 0.109840 |
| Course <= 10.5 and Size > 32.5 | 1 | 0.203804 |
| Course > 20.5 and Course <= 23 | 3 | 0.090909 |
| Course > 7.5 | 2 | 0.307273 |
| Instructor <= 14 and Instructor > 9.5 | 1 | 0.198529 |
| Instructor <= 12 | 2 | 0.036364 |
|  | 1 | 0.486486 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

semester|size|class
---|---|---
(-inf-1.5]|all|3
(1.5-inf)|all|2

## PART

Decision list:

rules | predicted class
---|---
Semester <= 1.5|3 (22.0/7.0)
Native <= 1.5|3 (16.0/6.0)
Course <= 10.5 AND Instructor > 21.5|2 (15.0/6.0)
Course <= 10.5 AND Size > 32.5|1 (13.0/1.0)
Course > 20.5 AND Course <= 23|3 (6.0)
Course > 7.5|2 (35.0/14.0)
Instructor <= 14 AND Instructor > 9.5|1 (11.0/5.0)
Instructor <= 12|2 (10.0/6.0)
|1 (6.0/1.0)


## J48 Decision Tree

* Semester <= 1.5
	* Instructor <= 18.5: 3 (12.0/5.0)
	* Instructor > 18.5: 3 (10.0/2.0)
* Semester > 1.5
	* Size <= 47
		* Course <= 5.5
			* Instructor <= 14
				* Size <= 25: 2 (11.0/7.0)
				* Size > 25: 1 (12.0/5.0)
			* Instructor > 14
				* Size <= 24.5: 1 (11.0/3.0)
				* Size > 24.5: 1 (12.0/7.0)
		* Course > 5.5
			* Course <= 20.5
				* Course <= 13.5
					* Size <= 25.5: 2 (12.0/2.0)
					* Size > 25.5: 1 (10.0/5.0)
				* Course > 13.5
					* Size <= 36.5: 3 (10.0/6.0)
					* Size > 36.5: 2 (10.0/3.0)
			* Course > 20.5: 3 (11.0/4.0)
	* Size > 47: 1 (13.0/6.0)


