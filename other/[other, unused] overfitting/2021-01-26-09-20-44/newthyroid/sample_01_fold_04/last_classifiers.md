# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| thyroidstimulating <= 4.2 and thyroxin <= 12.65 and thyroxin > 5.5 | 1 | 0.687191 |
| thyroxin > 12.65 and TSH_value <= 0.45 | 2 | 0.147368 |
| thyroidstimulating > 4.2 | 3 | 0.112903 |
| thyroxin > 12.65 and TSH_value > 0.45 and TSH_value <= 7.25 | 1 | 0.080645 |
| thyroidstimulating <= 4.2 and thyroxin <= 12.65 and thyroxin <= 5.5 | 3 | 0.021259 |
| thyroxin > 5.65 and thyroxin <= 12.65 and TSH_value > 7.25 | 3 | 0.010843 |

## Ordered rules

### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| thyroxin <= 5.6 | 3 | 0.118470 |
| TSH_value >= 11.5 | 3 | 0.013473 |
| TSH_value <= 0.4 and thyroxin >= 11.1 | 2 | 0.177026 |
|  | 1 | 1.000000 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

thyroxin|tsh_value|class
---|---|---
(5.65-12.65]|(7.25-inf)|3
(-inf-5.65]|(7.25-inf)|3
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
(TSH_value >= 11.5)|3 (4.0/1.0)
(TSH_value <= 0.4) and (thyroxin >= 11.1)|2 (31.0/1.0)
|1 (131.0/0.0)


## J48 Decision Tree

* thyroidstimulating <= 4.2
	* thyroxin <= 12.65
		* thyroxin <= 5.5: 3 (7.0/2.0)
		* thyroxin > 5.5: 1 (131.0/3.0)
	* thyroxin > 12.65
		* TSH_value <= 0.25: 2 (24.0)
		* TSH_value > 0.25: 1 (9.0/4.0)
* thyroidstimulating > 4.2: 3 (21.0)


