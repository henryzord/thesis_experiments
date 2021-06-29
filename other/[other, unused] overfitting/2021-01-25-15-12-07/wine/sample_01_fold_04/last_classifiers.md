# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Alcohol > 12.79 and Ash > 2.03 and AlcalinityOfAsh <= 17.45 and Magnesium > 88.5 and Magnesium <= 133 and OD280/OD315 > 2.475 | 1 | 0.231884 |
| Alcohol > 12.79 and Ash > 2.03 and AlcalinityOfAsh > 17.45 and Magnesium > 88.5 and Magnesium <= 133 and OD280/OD315 <= 2.005 | 3 | 0.164286 |
| Alcohol > 12.79 and Ash > 2.03 and AlcalinityOfAsh > 17.45 and Magnesium > 88.5 and Magnesium <= 133 and OD280/OD315 > 2.475 | 1 | 0.165354 |
| Alcohol <= 12.185 and Ash > 2.03 and AlcalinityOfAsh > 17.45 and Magnesium <= 88.5 and OD280/OD315 > 2.475 | 2 | 0.077670 |
| Alcohol > 12.185 and Alcohol <= 12.79 and Ash > 2.03 and AlcalinityOfAsh > 17.45 and Magnesium <= 88.5 and OD280/OD315 > 2.475 | 2 | 0.077670 |
| Alcohol <= 12.185 and Ash > 2.03 and AlcalinityOfAsh > 17.45 and Magnesium > 88.5 and Magnesium <= 133 and OD280/OD315 > 2.475 | 2 | 0.068627 |
| Alcohol > 12.185 and Alcohol <= 12.79 and Ash > 2.03 and AlcalinityOfAsh > 17.45 and Magnesium > 88.5 and Magnesium <= 133 and OD280/OD315 > 2.475 | 2 | 0.059406 |
| Alcohol > 12.185 and Alcohol <= 12.79 and Ash > 2.03 and AlcalinityOfAsh > 17.45 and Magnesium > 88.5 and Magnesium <= 133 and OD280/OD315 <= 2.005 | 3 | 0.056452 |
| Alcohol > 12.185 and Alcohol <= 12.79 and Ash <= 2.03 and AlcalinityOfAsh > 17.45 and Magnesium <= 88.5 and OD280/OD315 > 2.475 | 2 | 0.030612 |
| Alcohol <= 12.185 and Ash > 2.03 and AlcalinityOfAsh > 17.45 and Magnesium > 88.5 and Magnesium <= 133 and OD280/OD315 > 2.005 and OD280/OD315 <= 2.475 | 2 | 0.030612 |
| Alcohol > 12.79 and Ash > 2.03 and AlcalinityOfAsh > 17.45 and Magnesium <= 88.5 and OD280/OD315 > 2.475 | 2 | 0.030612 |
| Alcohol > 12.79 and Ash > 2.03 and AlcalinityOfAsh > 17.45 and Magnesium > 88.5 and Magnesium <= 133 and OD280/OD315 > 2.005 and OD280/OD315 <= 2.475 | 3 | 0.040984 |
| Alcohol <= 12.185 and Ash <= 2.03 and AlcalinityOfAsh > 17.45 and Magnesium > 88.5 and Magnesium <= 133 and OD280/OD315 > 2.475 | 2 | 0.020619 |
| Alcohol > 12.79 and Ash <= 2.03 and AlcalinityOfAsh <= 17.45 and Magnesium <= 88.5 and OD280/OD315 > 2.475 | 2 | 0.020619 |
| Alcohol > 12.185 and Alcohol <= 12.79 and Ash > 2.03 and AlcalinityOfAsh > 17.45 and Magnesium <= 88.5 and OD280/OD315 > 2.005 and OD280/OD315 <= 2.475 | 2 | 0.020619 |
| Alcohol <= 12.185 and Ash > 2.03 and AlcalinityOfAsh > 17.45 and Magnesium <= 88.5 and OD280/OD315 > 2.005 and OD280/OD315 <= 2.475 | 2 | 0.020619 |
| Alcohol <= 12.185 and Ash <= 2.03 and AlcalinityOfAsh > 17.45 and Magnesium <= 88.5 and OD280/OD315 > 2.475 | 2 | 0.020619 |
| Alcohol > 12.79 and Ash > 2.03 and AlcalinityOfAsh > 17.45 and Magnesium <= 88.5 and OD280/OD315 <= 2.005 | 3 | 0.033058 |
| Alcohol > 12.185 and Alcohol <= 12.79 and Ash > 2.03 and AlcalinityOfAsh > 17.45 and Magnesium <= 88.5 and OD280/OD315 <= 2.005 | 3 | 0.025000 |

## Ordered rules

### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| flavanoids <= 1.31 and ColorIntensity >= 3.85 | 3 | 0.254777 |
| Proline >= 780 and ColorIntensity >= 3.52 | 1 | 0.431034 |
|  | 2 | 0.927536 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

alcohol|ash|alcalinityofash|magnesium|od280/od315|class
---|---|---|---|---|---
(12.185-12.79]|(2.03-inf)|(17.45-inf)|(133-inf)|(2.475-inf)|1
(12.79-inf)|(2.03-inf)|(17.45-inf)|(133-inf)|(2.475-inf)|1
(12.185-12.79]|(-inf-2.03]|(-inf-17.45]|(133-inf)|(2.475-inf)|1
(-inf-12.185]|(2.03-inf)|(17.45-inf)|(88.5-133]|(2.475-inf)|2
(12.79-inf)|(2.03-inf)|(17.45-inf)|(88.5-133]|(2.475-inf)|1
(12.185-12.79]|(2.03-inf)|(17.45-inf)|(88.5-133]|(2.475-inf)|2
(12.185-12.79]|(-inf-2.03]|(17.45-inf)|(88.5-133]|(2.475-inf)|1
(-inf-12.185]|(-inf-2.03]|(17.45-inf)|(88.5-133]|(2.475-inf)|2
(-inf-12.185]|(2.03-inf)|(17.45-inf)|(133-inf)|(2.005-2.475]|1
(12.79-inf)|(2.03-inf)|(-inf-17.45]|(88.5-133]|(2.475-inf)|1
(12.79-inf)|(2.03-inf)|(17.45-inf)|(-inf-88.5]|(2.475-inf)|2
(12.185-12.79]|(2.03-inf)|(17.45-inf)|(-inf-88.5]|(2.475-inf)|2
(-inf-12.185]|(2.03-inf)|(17.45-inf)|(-inf-88.5]|(2.475-inf)|2
(12.185-12.79]|(-inf-2.03]|(-inf-17.45]|(133-inf)|(2.005-2.475]|1
(12.185-12.79]|(2.03-inf)|(17.45-inf)|(88.5-133]|(2.005-2.475]|1
(-inf-12.185]|(-inf-2.03]|(17.45-inf)|(-inf-88.5]|(2.475-inf)|2
(12.185-12.79]|(-inf-2.03]|(17.45-inf)|(-inf-88.5]|(2.475-inf)|2
(-inf-12.185]|(2.03-inf)|(17.45-inf)|(88.5-133]|(2.005-2.475]|2
(12.79-inf)|(2.03-inf)|(17.45-inf)|(88.5-133]|(2.005-2.475]|3
(12.79-inf)|(-inf-2.03]|(17.45-inf)|(88.5-133]|(2.005-2.475]|1
(12.79-inf)|(-inf-2.03]|(-inf-17.45]|(-inf-88.5]|(2.475-inf)|2
(-inf-12.185]|(-inf-2.03]|(-inf-17.45]|(88.5-133]|(2.005-2.475]|1
(-inf-12.185]|(2.03-inf)|(17.45-inf)|(-inf-88.5]|(2.005-2.475]|2
(12.79-inf)|(2.03-inf)|(17.45-inf)|(-inf-88.5]|(2.005-2.475]|1
(12.185-12.79]|(2.03-inf)|(17.45-inf)|(-inf-88.5]|(2.005-2.475]|2
(-inf-12.185]|(-inf-2.03]|(17.45-inf)|(-inf-88.5]|(2.005-2.475]|1
(12.79-inf)|(2.03-inf)|(17.45-inf)|(88.5-133]|(-inf-2.005]|3
(12.185-12.79]|(2.03-inf)|(17.45-inf)|(88.5-133]|(-inf-2.005]|3
(12.185-12.79]|(-inf-2.03]|(-inf-17.45]|(-inf-88.5]|(2.005-2.475]|1
(12.185-12.79]|(2.03-inf)|(-inf-17.45]|(88.5-133]|(-inf-2.005]|1
(12.79-inf)|(2.03-inf)|(-inf-17.45]|(88.5-133]|(-inf-2.005]|1
(12.79-inf)|(2.03-inf)|(17.45-inf)|(-inf-88.5]|(-inf-2.005]|3
(12.185-12.79]|(-inf-2.03]|(-inf-17.45]|(88.5-133]|(-inf-2.005]|1
(12.185-12.79]|(2.03-inf)|(17.45-inf)|(-inf-88.5]|(-inf-2.005]|3
(12.185-12.79]|(-inf-2.03]|(-inf-17.45]|(-inf-88.5]|(-inf-2.005]|1

## JRip

Decision list:

rules | predicted class
---|---
(flavanoids <= 1.31) and (ColorIntensity >= 3.85)|3 (40.0/0.0)
(Proline >= 780) and (ColorIntensity >= 3.52)|1 (50.0/0.0)
|2 (69.0/5.0)


