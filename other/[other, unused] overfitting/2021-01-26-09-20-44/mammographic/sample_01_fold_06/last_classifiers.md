# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 0 | 0.535342 |
| BI-RADS <= 4.5 and Shape > 3.5 | 1 | 0.076110 |
| BI-RADS > 4.5 and Shape <= 2.5 | 1 | 0.055789 |
| BI-RADS > 4.5 and Shape = ? | 1 | 0.008941 |
| BI-RADS > 4.5 and Shape > 2.5 and Shape <= 3.5 | 1 | 0.054540 |
| BI-RADS <= 4 and Shape <= 3 and Age > 63 and Margin > 3 | 1 | 0.010515 |
| BI-RADS > 4 | 1 | 0.356229 |
| BI-RADS <= 4 and Shape <= 3 and Age > 63 and Margin <= 3 and Shape <= 2 and Age > 67 and Age <= 71 | 1 | 0.008141 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| BI-RADS > 4.0 | 1 | 0.356229 |
| Shape <= 3.0 and Age > 41.0 and Age <= 67.0 and Age > 45.0 and Age > 49.0 and BI-RADS > 3.0 and Shape <= 2.0 | 0 | 0.486405 |
| Age <= 49.0 | 0 | 0.638895 |
| Margin > 4.0 | 1 | 0.100000 |
| Age <= 53.0 | 0 | 0.108423 |
| Density <= 2.0 | 0 | 0.093785 |
| Age <= 76.0 and Shape <= 1.0 | 1 | 0.135110 |
| Age <= 76.0 and BI-RADS > 3.0 and Margin > 2.0 and Age > 56.0 and Age > 57.0 and Age > 58.0 and Age > 59.0 and Age > 65.0 and Age > 66.0 | 1 | 0.072222 |
| Age <= 75.0 and Age <= 65.0 and BI-RADS > 3.0 and Age <= 63.0 and Age > 59.0 | 0 | 0.146453 |
| Age <= 75.0 and Age <= 65.0 and BI-RADS > 3.0 and Age > 58.0 | 1 | 0.206045 |
|  | 0 | 0.594595 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| BI-RADS >= 5 and Margin >= 2 | 1 | 0.349553 |
| Shape >= 4 and Age >= 62 | 1 | 0.046244 |
|  | 0 | 0.833935 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

bi-rads|shape|severity
---|---|---
?|(3.5-inf)|0
(-inf-4.5]|(3.5-inf)|1
(4.5-inf)|(3.5-inf)|1
?|?|0
(4.5-inf)|?|1
(-inf-4.5]|?|0
(4.5-inf)|(2.5-3.5]|1
(-inf-4.5]|(2.5-3.5]|0
(4.5-inf)|(-inf-2.5]|1
(-inf-4.5]|(-inf-2.5]|0

## JRip

Decision list:

rules | predicted class
---|---
(BI-RADS >= 5) and (Margin >= 2)|1 (291.0/22.0)
(Shape >= 4) and (Age >= 62)|1 (53.0/17.0)
|0 (519.0/96.0)


## PART

Decision list:

rules | predicted class
---|---
BI-RADS > 4.0|1 (158.37/18.37)
Shape <= 3.0 AND Age > 41.0 AND Age <= 67.0 AND Age > 45.0 AND Age > 49.0 AND BI-RADS > 3.0 AND Shape <= 2.0|0 (67.06/7.0)
Age <= 49.0|0 (120.58/11.58)
Margin > 4.0|1 (14.68/3.58)
Age <= 53.0|0 (9.63/1.83)
Density <= 2.0|0 (7.21/1.58)
Age <= 76.0 AND Shape <= 1.0|1 (6.89/2.01)
Age <= 76.0 AND BI-RADS > 3.0 AND Margin > 2.0 AND Age > 56.0 AND Age > 57.0 AND Age > 58.0 AND Age > 59.0 AND Age > 65.0 AND Age > 66.0|1 (6.88/3.0)
Age <= 75.0 AND Age <= 65.0 AND BI-RADS > 3.0 AND Age <= 63.0 AND Age > 59.0|0 (12.49/4.66)
Age <= 75.0 AND Age <= 65.0 AND BI-RADS > 3.0 AND Age > 58.0|1 (5.77/1.0)
|0 (22.45/9.71)


## J48 Decision Tree

* BI-RADS <= 4
	* Shape <= 3
		* Age <= 63: 0 (349.08/28.08)
		* Age > 63
			* Margin <= 3
				* Shape <= 2
					* Age <= 67: 0 (22.5/2.33)
					* Age > 67
						* Age <= 71: 1 (13.9/6.9)
						* Age > 71: 0 (12.63/1.0)
				* Shape > 2: 0 (11.3/5.08)
			* Margin > 3: 1 (11.01/4.16)
	* Shape > 3
		* Age <= 47: 0 (19.07/4.38)
		* Age > 47
			* Age <= 69
				* Margin <= 3: 0 (14.36/4.55)
				* Margin > 3
					* Margin <= 4
						* Age <= 56
							* Age <= 50: 1 (9.14/4.0)
							* Age > 50: 0 (10.6/4.0)
						* Age > 56
							* Age <= 65: 1 (23.72/7.69)
							* Age > 65: 0 (9.23/4.09)
					* Margin > 4: 1 (20.9/7.16)
			* Age > 69: 1 (18.84/3.46)
* BI-RADS > 4: 1 (316.73/33.37)


## SimpleCart Decision Tree

* BI-RADS < 4.5
	* Shape < 3.5: 0(370.08/50.33)
	* Shape >= 3.5
		* Age < 47.5: 0(14.69/4.38)
		* Age >= 47.5
			* Age < 69.5
				* Margin < 3.5: 0(9.8/4.55)
				* Margin >= 3.5: 1(42.98/30.59)
			* Age >= 69.5: 1(15.38/3.46)
* BI-RADS >= 4.5: 1(283.36/33.36)


