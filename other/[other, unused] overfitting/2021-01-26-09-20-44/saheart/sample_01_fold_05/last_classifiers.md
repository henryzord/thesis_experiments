# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Age <= 31.0 | 0 | 0.387821 |
| Age > 31.0 and Tobacco <= 8.08 and Famhist != Present | 0 | 0.341274 |
| Age > 31.0 and Tobacco <= 8.08 and Famhist = Present and Ldl > 5.05 | 1 | 0.100852 |
| Age > 31.0 and Tobacco > 8.08 | 1 | 0.092987 |
| Age > 31.0 and Tobacco <= 8.08 and Famhist = Present and Ldl <= 5.05 and Adiposity > 24.06 | 0 | 0.140815 |
| Tobacco > 0.49 and Tobacco <= 8.04 and Famhist = Present and Age > 30.5 and Age <= 50.5 | 0 | 0.107456 |
| Age > 31.0 and Tobacco <= 8.08 and Famhist = Present and Ldl <= 5.05 and Adiposity <= 24.06 | 1 | 0.029805 |
| Tobacco <= 0.49 and Famhist = Present and Age > 30.5 and Age <= 50.5 | 0 | 0.059211 |
| Tobacco > 8.04 and Famhist = Present and Age > 30.5 and Age <= 50.5 | 0 | 0.008991 |
| Tobacco <= 0.49 and Famhist = Present and Age > 50.5 | 0 | 0.027968 |
| Tobacco > 0.49 and Tobacco <= 8.04 and Famhist = Present and Age > 50.5 | 1 | 0.084483 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Age <= 30.5 and Tobacco <= 0.51 | 0 | 0.333396 |
| Tobacco > 8.04 and Famhist = Present and Ldl > 5.06 | 1 | 0.057416 |
| Famhist = Absent and Tobacco <= 7.635 and Typea <= 65.5 | 0 | 0.403501 |
| Age > 50.5 and Ldl > 6.82 | 1 | 0.168692 |
| Typea > 68.5 | 1 | 0.092764 |
| Famhist = Present and Sbp > 155 and Ldl > 5.04 | 1 | 0.085911 |
| Famhist = Present | 0 | 0.373336 |
|  | 1 | 0.853211 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

tobacco|famhist|age|chd
---|---|---|---
(-inf-0.49]|absent|(50.5-inf)|0
(8.04-inf)|absent|(50.5-inf)|1
(0.49-8.04]|absent|(50.5-inf)|0
(8.04-inf)|present|(50.5-inf)|1
(0.49-8.04]|present|(50.5-inf)|1
(-inf-0.49]|present|(50.5-inf)|0
(8.04-inf)|absent|(30.5-50.5]|1
(-inf-0.49]|absent|(30.5-50.5]|0
(0.49-8.04]|absent|(30.5-50.5]|0
(8.04-inf)|present|(30.5-50.5]|0
(0.49-8.04]|present|(30.5-50.5]|0
(-inf-0.49]|present|(30.5-50.5]|0
(0.49-8.04]|absent|(-inf-30.5]|0
(-inf-0.49]|absent|(-inf-30.5]|0
(0.49-8.04]|present|(-inf-30.5]|0
(-inf-0.49]|present|(-inf-30.5]|0

## PART

Decision list:

rules | predicted class
---|---
Age <= 30.5 AND Tobacco <= 0.51|0 (74.0/1.0)
Tobacco > 8.04 AND Famhist = Present AND Ldl > 5.06|1 (12.0)
Famhist = Absent AND Tobacco <= 7.635 AND Typea <= 65.5|0 (136.0/28.0)
Age > 50.5 AND Ldl > 6.82|1 (19.0/1.0)
Typea > 68.5|1 (11.0/1.0)
Famhist = Present AND Sbp > 155 AND Ldl > 5.04|1 (10.0)
Famhist = Present|0 (115.0/44.0)
|1 (37.0/16.0)


## J48 Decision Tree

* Age <= 31.0: 0 (72.0/4.0)
* Age > 31.0
	* Tobacco <= 8.08
		* Famhist = Present
			* Ldl <= 5.05
				* Adiposity <= 24.06: 1 (14.0/6.0)
				* Adiposity > 24.06: 0 (21.0/1.0)
			* Ldl > 5.05: 1 (46.0/15.0)
		* Famhist != Present: 0 (89.0/25.0)
	* Tobacco > 8.08: 1 (34.0/7.0)


