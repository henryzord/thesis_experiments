# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Thal <= 3.0 | 0 | 0.446524 |
| Thal > 3.0 and Oldpeak <= 2.3 and Ca <= 0.0 | 0 | 0.109572 |
| Thal >= 4.5 and Ca >= 0.5 and Age >= 55.5 and Trestbps < 149.0 and Thalach >= 141.5 | 2 | 0.033255 |
| Cp > 3.5 and Trestbps = all and Chol = all and Fbs = all and Restecg = all and Ca > 0.5 and Thal > 4.5 | 3 | 0.021404 |
| Cp > 3.5 and Trestbps = all and Chol = all and Fbs = all and Restecg = all and Ca <= 0.5 and Thal > 4.5 | 1 | 0.012684 |
| Thal >= 4.5 and Ca >= 0.5 and Age >= 55.5 and Trestbps < 149.0 and Thalach < 141.5 | 1 | 0.014985 |
| Cp > 3.5 and Trestbps = all and Chol = all and Fbs = all and Restecg = all and Ca > 0.5 and Thal <= 4.5 | 1 | 0.006582 |
| Thal > 3.0 and Oldpeak <= 2.3 and Ca > 0.0 | 2 | 0.021404 |
| Thal > 3.0 and Oldpeak > 2.3 and Thalach <= 134.0 | 3 | 0.013751 |
| Thal > 3.0 and Oldpeak > 2.3 and Thalach > 134.0 | 2 | 0.010256 |
| Cp <= 3.5 and Trestbps = all and Chol = all and Fbs = all and Restecg = all and Ca = ? and Thal > 4.5 | 0 | 0.008264 |
| Thal >= 4.5 and Ca >= 0.5 and Age < 55.5 | 3 | 0.018987 |
| Cp <= 3.5 and Trestbps = all and Chol = all and Fbs = all and Restecg = all and Ca <= 0.5 and Thal > 4.5 | 0 | 0.098931 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Thal <= 3 and Ca <= 0 and Trestbps <= 146 and Age <= 59 and Sex <= 0 | 0 | 0.230769 |
| Cp <= 3 and Slope <= 1 and Sex > 0 and Ca <= 0 and Thalach > 155 | 0 | 0.183673 |
| Cp <= 3 and Thal <= 3 and Sex <= 0 and Trestbps > 136 | 0 | 0.090909 |
| Cp <= 3 and Thal <= 3 and Cp > 1 and Fbs <= 0 and Chol <= 244 | 0 | 0.050403 |
| Oldpeak <= 2.3 and Ca <= 0 and Thal <= 6 and Sex > 0 and Slope <= 1 | 0 | 0.072153 |
| Cp <= 3 and Oldpeak <= 1.9 and Sex > 0 and Exang <= 0 and Thal <= 6 | 0 | 0.050403 |
| Cp <= 3 and Thal <= 6 | 0 | 0.048403 |
| Oldpeak <= 2.3 and Ca <= 0 and Exang <= 0 and Slope > 1 and Cp <= 3 | 0 | 0.029508 |
| Oldpeak <= 0.7 and Slope > 1 | 1 | 0.043548 |
| Slope <= 1 and Ca <= 1 and Ca > 0 | 1 | 0.034752 |
| Oldpeak <= 0.7 | 0 | 0.057732 |
| Exang > 0 and Chol <= 309 and Thal > 6 and Thalach <= 130 and Chol <= 234 | 3 | 0.036765 |
| Oldpeak <= 1.1 | 3 | 0.040950 |
| Exang > 0 and Chol > 235 and Chol > 278 and Restecg <= 0 | 2 | 0.017045 |
| Fbs <= 0 and Oldpeak <= 2.3 and Thal > 6 | 2 | 0.055096 |
| Exang <= 0 | 0 | 0.024390 |
| Chol > 235 and Chol <= 271 | 1 | 0.094737 |
| Chol <= 252 | 2 | 0.045161 |
|  | 2 | 0.161290 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Thal >= 7 and Thalach <= 139 and Age <= 55 | 3 | 0.024510 |
| Cp >= 4 and Exang >= 1 and Chol <= 282 | 1 | 0.045157 |
|  | 0 | 0.620253 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

cp|trestbps|chol|fbs|restecg|ca|thal|num
---|---|---|---|---|---|---|---
(-inf-3.5]|all|all|all|all|?|(4.5-inf)|0
(3.5-inf)|all|all|all|all|?|(4.5-inf)|0
(3.5-inf)|all|all|all|all|(0.5-inf)|(4.5-inf)|3
(-inf-3.5]|all|all|all|all|(0.5-inf)|(4.5-inf)|2
(-inf-3.5]|all|all|all|all|(-inf-0.5]|?|0
(-inf-3.5]|all|all|all|all|?|(-inf-4.5]|0
(-inf-3.5]|all|all|all|all|(-inf-0.5]|(4.5-inf)|0
(3.5-inf)|all|all|all|all|(-inf-0.5]|(4.5-inf)|1
(3.5-inf)|all|all|all|all|(0.5-inf)|(-inf-4.5]|1
(-inf-3.5]|all|all|all|all|(0.5-inf)|(-inf-4.5]|0
(-inf-3.5]|all|all|all|all|(-inf-0.5]|(-inf-4.5]|0
(3.5-inf)|all|all|all|all|(-inf-0.5]|(-inf-4.5]|0

## JRip

Decision list:

rules | predicted class
---|---
(Thal >= 7) and (Thalach <= 139) and (Age <= 55)|3 (17.0/7.0)
(Cp >= 4) and (Exang >= 1) and (Chol <= 282)|1 (41.0/22.0)
|0 (209.0/69.0)


## PART

Decision list:

rules | predicted class
---|---
Thal <= 3 AND Ca <= 0 AND Trestbps <= 146 AND Age <= 59 AND Sex <= 0|0 (36.55)
Cp <= 3 AND Slope <= 1 AND Sex > 0 AND Ca <= 0 AND Thalach > 155|0 (27.74)
Cp <= 3 AND Thal <= 3 AND Sex <= 0 AND Trestbps > 136|0 (12.0)
Cp <= 3 AND Thal <= 3 AND Cp > 1 AND Fbs <= 0 AND Chol <= 244|0 (15.49/6.0)
Oldpeak <= 2.3 AND Ca <= 0 AND Thal <= 6 AND Sex > 0 AND Slope <= 1|0 (12.0/1.0)
Cp <= 3 AND Oldpeak <= 1.9 AND Sex > 0 AND Exang <= 0 AND Thal <= 6|0 (12.0/2.0)
Cp <= 3 AND Thal <= 6|0 (15.07/4.0)
Oldpeak <= 2.3 AND Ca <= 0 AND Exang <= 0 AND Slope > 1 AND Cp <= 3|0 (10.43/4.0)
Oldpeak <= 0.7 AND Slope > 1|1 (15.57/8.57)
Slope <= 1 AND Ca <= 1 AND Ca > 0|1 (14.0/8.0)
Oldpeak <= 0.7|0 (15.14/8.0)
Exang > 0 AND Chol <= 309 AND Thal > 6 AND Thalach <= 130 AND Chol <= 234|3 (8.0/3.0)
Oldpeak <= 1.1|3 (11.0/6.0)
Exang > 0 AND Chol > 235 AND Chol > 278 AND Restecg <= 0|2 (8.0/5.0)
Fbs <= 0 AND Oldpeak <= 2.3 AND Thal > 6|2 (14.0/7.0)
Exang <= 0|0 (14.0/9.0)
Chol > 235 AND Chol <= 271|1 (8.0/4.0)
Chol <= 252|2 (10.0/7.0)
|2 (8.0/2.0)


## J48 Decision Tree

* Thal <= 3.0: 0 (135.56/28.0)
* Thal > 3.0
	* Oldpeak <= 2.3
		* Ca <= 0.0: 0 (41.44/20.5)
		* Ca > 0.0: 2 (40.99/26.99)
	* Oldpeak > 2.3
		* Thalach <= 134.0: 3 (10.0/4.0)
		* Thalach > 134.0: 2 (13.0/8.0)


## SimpleCart Decision Tree

* Thal < 4.5: 0(116.55/31.0)
* Thal >= 4.5
	* Ca < 0.5: 0(25.91/30.47)
	* Ca >= 0.5
		* Age < 55.5: 3(9.0/8.52)
		* Age >= 55.5
			* Trestbps < 149.0
				* Thalach < 141.5: 1(7.0/8.0)
				* Thalach >= 141.5: 2(13.0/7.52)
			* Trestbps >= 149.0: 3(5.0/5.0)


