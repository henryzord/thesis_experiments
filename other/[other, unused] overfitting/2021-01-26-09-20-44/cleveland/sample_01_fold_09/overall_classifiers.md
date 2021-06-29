# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 0 | 0.550562 |
| Thal >= 4.5 and Ca >= 0.5 and Age >= 55.5 and Trestbps < 149.0 and Thalach >= 141.5 and Trestbps >= 132.0 | 2 | 0.028689 |
| Thal >= 4.5 and Ca >= 0.5 and Age < 55.5 and Oldpeak >= 0.9 | 3 | 0.022498 |
| Thal >= 4.5 and Ca >= 0.5 and Age >= 55.5 and Trestbps < 149.0 and Thalach < 141.5 | 1 | 0.014985 |
| Thal < 4.5 and Ca >= 0.5 and Cp >= 3.5 and Age < 56.5 | 1 | 0.012066 |
| Thal >= 4.5 and Ca >= 0.5 and Age >= 55.5 and Trestbps < 149.0 and Thalach >= 141.5 and Trestbps < 132.0 | 2 | 0.010942 |
| Thal >= 4.5 and Ca >= 0.5 and Age < 55.5 and Oldpeak < 0.9 | 1 | 0.008155 |
| Thal >= 4.5 and Ca >= 0.5 and Age >= 55.5 and Trestbps >= 149.0 | 3 | 0.010549 |
| Thal >= 4.5 and Ca < 0.5 and Exang >= 0.5 and Chol >= 278.0 | 2 | 0.008439 |
| Thal >= 4.5 and Ca < 0.5 and Exang >= 0.5 and Chol < 278.0 and Oldpeak >= 1.55 | 3 | 0.007533 |
| Thal > 4.5 and Oldpeak <= 2.3499999999999996 and Trestbps > 119.0 and Ca > 0.5 | 2 | 0.015965 |
| Age = all and Sex = all and Cp > 3.5 and Trestbps = all and Chol = all and Restecg = all and Oldpeak > 1.95 and Ca > 0.5 and Thal <= 4.5 | 3 | 0.004219 |
| Age = all and Sex = all and Cp > 3.5 and Trestbps = all and Chol = all and Restecg = all and Oldpeak <= 1.95 and Ca > 0.5 and Thal <= 4.5 | 1 | 0.008306 |
| Age = all and Sex = all and Cp > 3.5 and Trestbps = all and Chol = all and Restecg = all and Oldpeak > 1.95 and Ca > 0.5 and Thal > 4.5 | 3 | 0.011116 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Oldpeak <= 2.4 and Cp <= 3.5 and Thal <= 4.5 | 0 | 0.408467 |
| Ca <= 0.5 and Slope <= 2.5 and Oldpeak <= 2.55 and Exang <= 0.5 | 0 | 0.182265 |
| Cp <= 1.5 | 0 | 0.012432 |
| Restecg <= 0.5 and Age > 66.5 and Trestbps <= 121.5 | 0 | 0.016393 |
| Ca <= 0.5 and Thal <= 4.5 | 0 | 0.019397 |
| Oldpeak > 2.35 and Sex > 0.5 and Thalach > 126.5 | 2 | 0.028064 |
| Oldpeak > 2.35 | 3 | 0.038352 |
| Sex <= 0.5 | 2 | 0.020654 |
| Chol > 287.5 and Exang > 0.5 | 3 | 0.018605 |
| Chol <= 284.5 and Trestbps > 109 and Age <= 52.5 | 1 | 0.145161 |
| Ca <= 0.5 | 0 | 0.014124 |
| Thalach <= 106.5 | 3 | 0.029412 |
| Trestbps <= 162.5 and Restecg > 1 and Chol <= 251.5 | 1 | 0.130909 |
|  | 2 | 0.246377 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

age|sex|cp|trestbps|chol|restecg|oldpeak|ca|thal|num
---|---|---|---|---|---|---|---|---|---
all|all|(-inf-3.5]|all|all|all|(-inf-1.95]|?|(4.5-inf)|0
all|all|(3.5-inf)|all|all|all|(-inf-1.95]|(0.5-inf)|(4.5-inf)|2
all|all|(3.5-inf)|all|all|all|(1.95-inf)|(-inf-0.5]|(4.5-inf)|3
all|all|(3.5-inf)|all|all|all|(1.95-inf)|(0.5-inf)|(-inf-4.5]|3
all|all|(-inf-3.5]|all|all|all|(-inf-1.95]|(0.5-inf)|(4.5-inf)|0
all|all|(-inf-3.5]|all|all|all|(1.95-inf)|(-inf-0.5]|(4.5-inf)|0
all|all|(-inf-3.5]|all|all|all|(1.95-inf)|(0.5-inf)|(-inf-4.5]|0
all|all|(-inf-3.5]|all|all|all|(-inf-1.95]|(-inf-0.5]|?|0
all|all|(-inf-3.5]|all|all|all|(-inf-1.95]|?|(-inf-4.5]|0
all|all|(3.5-inf)|all|all|all|(-inf-1.95]|(-inf-0.5]|(4.5-inf)|0
all|all|(3.5-inf)|all|all|all|(-inf-1.95]|(0.5-inf)|(-inf-4.5]|1
all|all|(3.5-inf)|all|all|all|(1.95-inf)|(-inf-0.5]|(-inf-4.5]|0
all|all|(-inf-3.5]|all|all|all|(-inf-1.95]|(-inf-0.5]|(4.5-inf)|0
all|all|(-inf-3.5]|all|all|all|(-inf-1.95]|(0.5-inf)|(-inf-4.5]|0
all|all|(-inf-3.5]|all|all|all|(1.95-inf)|(-inf-0.5]|(-inf-4.5]|0
all|all|(3.5-inf)|all|all|all|(-inf-1.95]|(-inf-0.5]|(-inf-4.5]|0
all|all|(-inf-3.5]|all|all|all|(-inf-1.95]|(-inf-0.5]|(-inf-4.5]|0
all|all|(3.5-inf)|all|all|all|(1.95-inf)|(0.5-inf)|(4.5-inf)|3
all|all|(3.5-inf)|all|all|all|(-inf-1.95]|?|(4.5-inf)|0
all|all|(-inf-3.5]|all|all|all|(1.95-inf)|(0.5-inf)|(4.5-inf)|2

## PART

Decision list:

rules | predicted class
---|---
Oldpeak <= 2.4 AND Cp <= 3.5 AND Thal <= 4.5|0 (78.7/5.0)
Ca <= 0.5 AND Slope <= 2.5 AND Oldpeak <= 2.55 AND Exang <= 0.5|0 (38.83/9.0)
Cp <= 1.5|0 (5.0/2.0)
Restecg <= 0.5 AND Age > 66.5 AND Trestbps <= 121.5|0 (2.0)
Ca <= 0.5 AND Thal <= 4.5|0 (11.0/5.0)
Oldpeak > 2.35 AND Sex > 0.5 AND Thalach > 126.5|2 (9.0/4.0)
Oldpeak > 2.35|3 (10.0/3.0)
Sex <= 0.5|2 (8.0/4.0)
Chol > 287.5 AND Exang > 0.5|3 (6.0/3.0)
Chol <= 284.5 AND Trestbps > 109 AND Age <= 52.5|1 (14.0/5.0)
Ca <= 0.5|0 (7.08/3.0)
Thalach <= 106.5|3 (7.0/3.0)
Trestbps <= 162.5 AND Restecg > 1 AND Chol <= 251.5|1 (7.0/3.0)
|2 (19.39/7.39)


## J48 Decision Tree

* Thal <= 4.5: 0 (115.58/23.0)
* Thal > 4.5
	* Oldpeak <= 2.3499999999999996
		* Trestbps <= 119.0: 0 (13.0/4.0)
		* Trestbps > 119.0
			* Ca <= 0.5: 0 (21.83/13.41)
			* Ca > 0.5: 2 (31.59/21.59)
	* Oldpeak > 2.3499999999999996: 3 (19.0/12.0)


## SimpleCart Decision Tree

* Thal < 4.5
	* Ca < 0.5: 0(92.24/10.0)
	* Ca >= 0.5
		* Cp < 3.5: 0(21.3/6.0)
		* Cp >= 3.5
			* Age < 56.5: 1(4.0/2.0)
			* Age >= 56.5: 0(3.0/9.0)
* Thal >= 4.5
	* Ca < 0.5
		* Exang < 0.5
			* Age < 51.0: 0(5.0/8.0)
			* Age >= 51.0
				* Trestbps < 151.0: 0(11.91/0.0)
				* Trestbps >= 151.0: 0(4.0/2.0)
		* Exang >= 0.5
			* Chol < 278.0
				* Oldpeak < 1.55: 0(5.0/3.47)
				* Oldpeak >= 1.55: 3(4.0/5.0)
			* Chol >= 278.0: 2(4.0/4.0)
	* Ca >= 0.5
		* Age < 55.5
			* Oldpeak < 0.9: 1(3.52/5.0)
			* Oldpeak >= 0.9: 3(7.0/2.0)
		* Age >= 55.5
			* Trestbps < 149.0
				* Thalach < 141.5: 1(7.0/8.0)
				* Thalach >= 141.5
					* Trestbps < 132.0: 2(6.0/7.52)
					* Trestbps >= 132.0: 2(7.0/0.0)
			* Trestbps >= 149.0: 3(5.0/5.0)


