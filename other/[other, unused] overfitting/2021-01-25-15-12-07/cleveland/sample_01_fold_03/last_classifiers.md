# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Oldpeak <= 2.3 and Ca <= 0.0 | 0 | 0.426159 |
| Oldpeak <= 2.3 and Ca > 0.0 and Cp <= 3.0 | 0 | 0.134477 |
| Thal >= 4.5 and Cp >= 3.5 and Oldpeak >= 0.7 and Thalach >= 139.0 | 2 | 0.033622 |
| Oldpeak <= 2.3 and Ca > 0.0 and Cp > 3.0 and Sex > 0.0 and Trestbps <= 146.0 | 1 | 0.025323 |
| Thal < 4.5 and Age >= 55.5 and Thalach >= 108.5 and Oldpeak < 2.2 and Age < 65.5 and Chol < 337.5 and Chol >= 243.5 and Sex < 0.5 and Cp >= 3.5 | 1 | 0.013889 |
| Thal >= 4.5 and Cp >= 3.5 and Oldpeak >= 0.7 and Thalach < 139.0 and Oldpeak >= 2.9 | 3 | 0.016327 |
| Thal < 4.5 and Age >= 55.5 and Thalach >= 108.5 and Oldpeak < 2.2 and Age < 65.5 and Chol < 337.5 and Chol >= 243.5 and Sex >= 0.5 | 1 | 0.018355 |
| Thal >= 4.5 and Cp >= 3.5 and Oldpeak >= 0.7 and Thalach < 139.0 and Oldpeak < 2.9 and Trestbps >= 144.5 and Thalach >= 112.5 | 4 | 0.015843 |
| Age <= 54.5 and Cp > 3.5 and Ca > 0.5 | 3 | 0.010084 |
| Thal >= 4.5 and Cp < 3.5 and Ca >= 0.5 and Thalach < 144.0 | 2 | 0.011158 |
| Oldpeak > 2.3 and Thalach > 116.0 and Sex <= 0.0 | 3 | 0.010974 |
| Age > 54.5 and Cp > 3.5 and Ca > 0.5 | 2 | 0.027397 |
| Thal >= 4.5 and Cp >= 3.5 and Oldpeak >= 0.7 and Thalach < 139.0 and Oldpeak < 2.9 and Trestbps < 144.5 and Chol >= 274.5 | 2 | 0.006329 |
| Oldpeak > 2.3 and Thalach > 116.0 and Sex > 0.0 and Slope > 1.0 and Chol <= 232.0 and Age > 56.0 | 4 | 0.008791 |
| Thal < 4.5 and Age >= 55.5 and Thalach >= 108.5 and Oldpeak >= 2.2 | 1 | 0.003017 |
| Oldpeak <= 2.3 and Ca > 0.0 and Cp > 3.0 and Sex <= 0.0 | 0 | 0.004723 |
| Oldpeak > 2.3 and Thalach > 116.0 and Sex > 0.0 and Slope > 1.0 and Chol <= 232.0 and Age <= 56.0 | 1 | 0.003017 |
| Thal >= 4.5 and Cp >= 3.5 and Oldpeak >= 0.7 and Thalach < 139.0 and Oldpeak < 2.9 and Trestbps < 144.5 and Chol < 274.5 | 1 | 0.015695 |
| Thal < 4.5 and Age < 55.5 | 0 | 0.357279 |
| Age > 54.5 and Cp <= 3.5 and Ca <= 0.5 | 0 | 0.142606 |
| Thal >= 4.5 and Cp < 3.5 and Ca >= 0.5 and Thalach >= 144.0 and Restecg >= 1.0 | 1 | 0.001131 |
| Oldpeak > 2.3 and Thalach > 116.0 and Sex > 0.0 and Slope > 1.0 and Chol > 232.0 | 2 | 0.012658 |
| Thal >= 4.5 and Cp >= 3.5 and Oldpeak >= 0.7 and Thalach < 139.0 and Oldpeak < 2.9 and Trestbps >= 144.5 and Thalach < 112.5 | 1 | 0.004484 |
| Thal < 4.5 and Age >= 55.5 and Thalach < 108.5 | 2 | 0.007563 |
| Thal >= 4.5 and Cp >= 3.5 and Oldpeak < 0.7 and Chol >= 237.5 | 1 | 0.011211 |
| Thal >= 4.5 and Cp >= 3.5 and Oldpeak < 0.7 and Chol < 237.5 | 0 | 0.032407 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Ca <= 1.0 and Exang <= 0.0 | 0 | 0.434696 |
| Slope <= 1.0 | 0 | 0.063770 |
| Exang > 0.0 and Ca <= 1.0 and Thalach > 136.0 | 2 | 0.030000 |
|  | 3 | 0.236220 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Ca >= 2 and Age <= 59 | 3 | 0.024896 |
| Ca >= 1 and Thal >= 6 and Trestbps <= 148 | 2 | 0.041135 |
|  | 0 | 0.615063 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

age|cp|ca|num
---|---|---|---
(-inf-54.5]|(3.5-inf)|?|0
(-inf-54.5]|(-inf-3.5]|?|0
(54.5-inf)|(3.5-inf)|(0.5-inf)|2
(-inf-54.5]|(3.5-inf)|(0.5-inf)|3
(54.5-inf)|(-inf-3.5]|(0.5-inf)|0
(-inf-54.5]|(-inf-3.5]|(0.5-inf)|0
(-inf-54.5]|(3.5-inf)|(-inf-0.5]|0
(54.5-inf)|(3.5-inf)|(-inf-0.5]|0
(54.5-inf)|(-inf-3.5]|(-inf-0.5]|0
(-inf-54.5]|(-inf-3.5]|(-inf-0.5]|0

## JRip

Decision list:

rules | predicted class
---|---
(Ca >= 2) and (Age <= 59)|3 (24.0/12.0)
(Ca >= 1) and (Thal >= 6) and (Trestbps <= 148)|2 (38.0/20.0)
|0 (209.0/69.0)


## PART

Decision list:

rules | predicted class
---|---
Ca <= 1.0 AND Exang <= 0.0|0 (95.53/18.0)
Slope <= 1.0|0 (29.47/12.0)
Exang > 0.0 AND Ca <= 1.0 AND Thalach > 136.0|2 (16.0/9.0)
|3 (40.0/24.0)


## J48 Decision Tree

* Oldpeak <= 2.3
	* Ca <= 0.0: 0 (75.26/14.63)
	* Ca > 0.0
		* Cp <= 3.0: 0 (18.37/7.0)
		* Cp > 3.0
			* Sex <= 0.0: 0 (3.0/2.0)
			* Sex > 0.0
				* Trestbps <= 146.0: 1 (19.37/12.0)
				* Trestbps > 146.0: 2 (3.0/1.0)
* Oldpeak > 2.3
	* Thalach <= 116.0: 0 (2.0/1.0)
	* Thalach > 116.0
		* Sex <= 0.0: 3 (4.0/1.0)
		* Sex > 0.0
			* Slope <= 1.0: 2 (2.0/1.0)
			* Slope > 1.0
				* Chol <= 232.0
					* Age <= 56.0: 1 (3.0/1.0)
					* Age > 56.0: 4 (3.0/1.0)
				* Chol > 232.0: 2 (3.0/1.0)


## SimpleCart Decision Tree

* Thal < 4.5
	* Age < 55.5: 0(75.54/7.54)
	* Age >= 55.5
		* Thalach < 108.5: 2(3.0/2.0)
		* Thalach >= 108.5
			* Oldpeak < 2.2
				* Age < 65.5
					* Chol < 337.5
						* Chol < 243.5: 0(11.0/3.0)
						* Chol >= 243.5
							* Sex < 0.5
								* Cp < 3.5: 0(5.0/1.0)
								* Cp >= 3.5: 1(5.0/3.0)
							* Sex >= 0.5: 1(5.0/1.0)
					* Chol >= 337.5: 0(5.0/0.0)
				* Age >= 65.5: 0(12.0/2.0)
			* Oldpeak >= 2.2: 1(2.0/4.0)
* Thal >= 4.5
	* Cp < 3.5
		* Ca < 0.5: 0(18.45/8.0)
		* Ca >= 0.5
			* Thalach < 144.0: 2(4.0/2.0)
			* Thalach >= 144.0
				* Restecg < 1.0: 0(4.0/0.0)
				* Restecg >= 1.0: 1(1.0/3.0)
	* Cp >= 3.5
		* Oldpeak < 0.7
			* Chol < 237.5: 0(7.0/5.0)
			* Chol >= 237.5: 1(5.0/5.0)
		* Oldpeak >= 0.7
			* Thalach < 139.0
				* Oldpeak < 2.9
					* Trestbps < 144.5
						* Chol < 274.5: 1(7.0/7.0)
						* Chol >= 274.5: 2(3.0/3.0)
					* Trestbps >= 144.5
						* Thalach < 112.5: 1(2.0/2.0)
						* Thalach >= 112.5: 4(5.0/1.0)
				* Oldpeak >= 2.9: 3(4.0/0.0)
			* Thalach >= 139.0: 2(14.45/13.0)


