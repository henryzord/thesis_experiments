# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 1 | 0.703125 |
| thyroxin > 14 and TSH_value <= 0.45 | 2 | 0.129032 |
| thyroidstimulating > 2.8 | 3 | 0.108354 |
| thyroxin > 11 and thyroxin <= 14 and TSH_value <= 0.45 | 2 | 0.021645 |
| thyroxin <= 5.65 and TSH_value > 0.45 and TSH_value <= 7.25 | 3 | 0.042812 |
| thyroxin > 5.65 and thyroxin <= 11 and TSH_value > 7.25 | 3 | 0.010843 |
| thyroxin > 14 and TSH_value > 0.45 and TSH_value <= 7.25 | 2 | 0.002070 |
| thyroxin <= 5.65 and TSH_value > 7.25 | 3 | 0.083333 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| thyroidstimulating > 4 | 3 | 0.112903 |
| thyroxin > 14 and T3resin <= 102 | 2 | 0.113208 |
| thyroxin <= 12.65 and thyroxin > 6.55 and T3resin > 99 | 1 | 0.856000 |
| TSH_value > 0.45 and thyroxin > 5.8 and T3resin <= 111 | 1 | 0.470588 |
| TSH_value <= 0.45 | 2 | 0.379310 |
| thyroxin > 5.8 | 1 | 0.492308 |
|  | 3 | 0.545455 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| thyroxin <= 5.6 and TSH_value >= 2.2 | 3 | 0.122340 |
| thyroxin >= 12.9 and TSH_value <= 0.4 | 2 | 0.162651 |
|  | 1 | 0.950704 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

thyroxin|tsh_value|class
---|---|---
(5.65-11]|(7.25-inf)|3
(-inf-5.65]|(7.25-inf)|3
(-inf-5.65]|(0.45-7.25]|3
(14-inf)|(0.45-7.25]|2
(5.65-11]|(0.45-7.25]|1
(11-14]|(0.45-7.25]|1
(14-inf)|(-inf-0.45]|2
(11-14]|(-inf-0.45]|2
(5.65-11]|(-inf-0.45]|1

## JRip

Decision list:

rules | predicted class
---|---
(thyroxin <= 5.6) and (TSH_value >= 2.2)|3 (23.0/0.0)
(thyroxin >= 12.9) and (TSH_value <= 0.4)|2 (27.0/0.0)
|1 (142.0/7.0)


## PART

Decision list:

rules | predicted class
---|---
thyroidstimulating > 4|3 (21.0)
thyroxin > 14 AND T3resin <= 102|2 (18.0)
thyroxin <= 12.65 AND thyroxin > 6.55 AND T3resin > 99|1 (107.0)
TSH_value > 0.45 AND thyroxin > 5.8 AND T3resin <= 111|1 (16.0)
TSH_value <= 0.45|2 (11.0)
thyroxin > 5.8|1 (10.0/2.0)
|3 (9.0/4.0)


## J48 Decision Tree

* thyroidstimulating <= 2.8
	* triiodothyronine <= 2.9: 1 (134.0/15.0)
	* triiodothyronine > 2.9: 2 (19.0/1.0)
* thyroidstimulating > 2.8: 3 (18.0)


