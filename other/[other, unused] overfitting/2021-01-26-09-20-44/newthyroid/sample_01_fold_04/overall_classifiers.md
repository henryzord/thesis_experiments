# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 1 | 0.703125 |
| thyroxin > 11.9 and TSH_value <= 0.4 | 2 | 0.151832 |
| thyroxin <= 11.9 and thyroidstimulating > 3.7 | 3 | 0.112903 |
| thyroxin <= 5.65 and TSH_value > 0.45 and TSH_value <= 7.25 | 3 | 0.037427 |
| thyroxin > 5.65 and thyroxin <= 12.65 and TSH_value > 7.25 | 3 | 0.010843 |
| thyroxin <= 5.65 and TSH_value > 7.25 | 3 | 0.088398 |

## Ordered rules

### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| thyroxin <= 5.6 | 3 | 0.118470 |
| thyroxin >= 12.9 and TSH_value <= 0.4 | 2 | 0.168675 |
|  | 1 | 0.964286 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

thyroxin|tsh_value|class
---|---|---
(-inf-5.65]|(7.25-inf)|3
(5.65-12.65]|(7.25-inf)|3
(12.65-inf)|(0.45-7.25]|1
(-inf-5.65]|(0.45-7.25]|3
(5.65-12.65]|(0.45-7.25]|1
(12.65-inf)|(-inf-0.45]|2
(5.65-12.65]|(-inf-0.45]|1

## JRip

Decision list:

rules | predicted class
---|---
(thyroxin <= 5.6)|3 (26.0/2.0)
(thyroxin >= 12.9) and (TSH_value <= 0.4)|2 (28.0/0.0)
|1 (138.0/5.0)


## J48 Decision Tree

* thyroxin <= 11.9
	* thyroidstimulating <= 3.7: 1 (88.0/5.0)
	* thyroidstimulating > 3.7: 3 (13.0)
* thyroxin > 11.9
	* TSH_value <= 0.4: 2 (20.0)
	* TSH_value > 0.4: 1 (7.0)


