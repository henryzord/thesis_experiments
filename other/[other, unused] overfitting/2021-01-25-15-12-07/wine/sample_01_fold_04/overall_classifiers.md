# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Alcohol > 12.79 and Ash > 2.03 and AlcalinityOfAsh <= 17.45 and Magnesium > 88.5 and Magnesium <= 133 and flavanoids > 2.31 and OD280/OD315 > 2.475 | 1 | 0.226277 |
| Alcohol > 12.79 and Ash > 2.03 and AlcalinityOfAsh > 17.45 and Magnesium > 88.5 and Magnesium <= 133 and flavanoids > 2.31 and OD280/OD315 > 2.475 | 1 | 0.165354 |
| Alcohol > 12.79 and Ash > 2.03 and AlcalinityOfAsh > 17.45 and Magnesium > 88.5 and Magnesium <= 133 and flavanoids <= 0.975 and OD280/OD315 <= 2.005 | 3 | 0.113636 |
| Alcohol <= 12.185 and Ash > 2.03 and AlcalinityOfAsh > 17.45 and Magnesium <= 88.5 and flavanoids > 1.575 and flavanoids <= 2.31 and OD280/OD315 > 2.475 | 2 | 0.050000 |
| Alcohol > 12.185 and Alcohol <= 12.79 and Ash > 2.03 and AlcalinityOfAsh > 17.45 and Magnesium > 88.5 and Magnesium <= 133 and flavanoids > 1.575 and flavanoids <= 2.31 and OD280/OD315 > 2.475 | 2 | 0.050000 |
| Alcohol > 12.185 and Alcohol <= 12.79 and Ash > 2.03 and AlcalinityOfAsh > 17.45 and Magnesium <= 88.5 and flavanoids > 2.31 and OD280/OD315 > 2.475 | 2 | 0.050000 |
| Alcohol > 12.79 and Ash > 2.03 and AlcalinityOfAsh > 17.45 and Magnesium > 88.5 and Magnesium <= 133 and flavanoids > 0.975 and flavanoids <= 1.575 and OD280/OD315 <= 2.005 | 3 | 0.064000 |
| Alcohol <= 12.185 and Ash > 2.03 and AlcalinityOfAsh > 17.45 and Magnesium > 88.5 and Magnesium <= 133 and flavanoids > 1.575 and flavanoids <= 2.31 and OD280/OD315 > 2.475 | 2 | 0.030612 |
| Alcohol <= 12.185 and Ash > 2.03 and AlcalinityOfAsh > 17.45 and Magnesium > 88.5 and Magnesium <= 133 and flavanoids > 1.575 and flavanoids <= 2.31 and OD280/OD315 > 2.005 and OD280/OD315 <= 2.475 | 2 | 0.030612 |
| Alcohol <= 12.185 and Ash > 2.03 and AlcalinityOfAsh > 17.45 and Magnesium > 88.5 and Magnesium <= 133 and flavanoids > 2.31 and OD280/OD315 > 2.475 | 2 | 0.030612 |
| Alcohol > 12.185 and Alcohol <= 12.79 and Ash > 2.03 and AlcalinityOfAsh > 17.45 and Magnesium <= 88.5 and flavanoids > 1.575 and flavanoids <= 2.31 and OD280/OD315 > 2.475 | 2 | 0.030612 |
| Alcohol > 12.185 and Alcohol <= 12.79 and Ash > 2.03 and AlcalinityOfAsh > 17.45 and Magnesium > 88.5 and Magnesium <= 133 and flavanoids <= 0.975 and OD280/OD315 <= 2.005 | 3 | 0.048780 |
| Alcohol > 12.79 and Ash > 2.03 and AlcalinityOfAsh > 17.45 and Magnesium <= 88.5 and flavanoids > 2.31 and OD280/OD315 > 2.475 | 2 | 0.020619 |
| Alcohol <= 12.185 and Ash <= 2.03 and AlcalinityOfAsh > 17.45 and Magnesium <= 88.5 and flavanoids > 1.575 and flavanoids <= 2.31 and OD280/OD315 > 2.475 | 2 | 0.020619 |
| Alcohol > 12.79 and Ash > 2.03 and AlcalinityOfAsh > 17.45 and Magnesium > 88.5 and Magnesium <= 133 and flavanoids <= 0.975 and OD280/OD315 > 2.005 and OD280/OD315 <= 2.475 | 3 | 0.040984 |
| Alcohol <= 12.185 and Ash > 2.03 and AlcalinityOfAsh > 17.45 and Magnesium <= 88.5 and flavanoids > 2.31 and OD280/OD315 > 2.475 | 2 | 0.020619 |
| Alcohol > 12.185 and Alcohol <= 12.79 and Ash <= 2.03 and AlcalinityOfAsh > 17.45 and Magnesium <= 88.5 and flavanoids > 1.575 and flavanoids <= 2.31 and OD280/OD315 > 2.475 | 2 | 0.020619 |
| Alcohol > 12.79 and Ash > 2.03 and AlcalinityOfAsh > 17.45 and Magnesium <= 88.5 and flavanoids <= 0.975 and OD280/OD315 <= 2.005 | 3 | 0.033058 |
| Alcohol > 12.185 and Alcohol <= 12.79 and Ash > 2.03 and AlcalinityOfAsh > 17.45 and Magnesium <= 88.5 and flavanoids <= 0.975 and OD280/OD315 <= 2.005 | 3 | 0.025000 |
| Alcohol > 12.79 and Ash > 2.03 and AlcalinityOfAsh <= 17.45 and Magnesium > 88.5 and Magnesium <= 133 and flavanoids > 1.575 and flavanoids <= 2.31 and OD280/OD315 > 2.475 | 1 | 0.009346 |

## Ordered rules

### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| flavanoids <= 1.39 and ColorIntensity >= 4.1 | 3 | 0.250000 |
| Proline >= 760 and Alcohol >= 13.05 | 1 | 0.422583 |
|  | 2 | 0.914286 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

alcohol|ash|alcalinityofash|magnesium|flavanoids|od280/od315|class
---|---|---|---|---|---|---
(12.185-12.79]|(-inf-2.03]|(17.45-inf)|(-inf-88.5]|(0.975-1.575]|(2.475-inf)|1
(12.79-inf)|(2.03-inf)|(17.45-inf)|(-inf-88.5]|(1.575-2.31]|(2.005-2.475]|1
(-inf-12.185]|(2.03-inf)|(17.45-inf)|(-inf-88.5]|(1.575-2.31]|(2.005-2.475]|1
(12.185-12.79]|(2.03-inf)|(17.45-inf)|(-inf-88.5]|(1.575-2.31]|(2.005-2.475]|1
(-inf-12.185]|(-inf-2.03]|(17.45-inf)|(-inf-88.5]|(1.575-2.31]|(2.005-2.475]|1
(12.185-12.79]|(2.03-inf)|(17.45-inf)|(-inf-88.5]|(0.975-1.575]|(2.005-2.475]|1
(-inf-12.185]|(-inf-2.03]|(-inf-17.45]|(88.5-133]|(0.975-1.575]|(2.005-2.475]|1
(-inf-12.185]|(2.03-inf)|(17.45-inf)|(-inf-88.5]|(0.975-1.575]|(2.005-2.475]|1
(12.79-inf)|(2.03-inf)|(17.45-inf)|(88.5-133]|(-inf-0.975]|(2.005-2.475]|3
(12.185-12.79]|(2.03-inf)|(17.45-inf)|(88.5-133]|(0.975-1.575]|(-inf-2.005]|1
(12.79-inf)|(2.03-inf)|(17.45-inf)|(88.5-133]|(0.975-1.575]|(-inf-2.005]|3
(12.185-12.79]|(-inf-2.03]|(-inf-17.45]|(-inf-88.5]|(0.975-1.575]|(2.005-2.475]|1
(12.79-inf)|(2.03-inf)|(-inf-17.45]|(88.5-133]|(0.975-1.575]|(-inf-2.005]|1
(12.185-12.79]|(2.03-inf)|(-inf-17.45]|(88.5-133]|(0.975-1.575]|(-inf-2.005]|1
(12.185-12.79]|(-inf-2.03]|(-inf-17.45]|(88.5-133]|(0.975-1.575]|(-inf-2.005]|1
(12.185-12.79]|(2.03-inf)|(17.45-inf)|(88.5-133]|(-inf-0.975]|(-inf-2.005]|3
(12.79-inf)|(2.03-inf)|(17.45-inf)|(88.5-133]|(-inf-0.975]|(-inf-2.005]|3
(12.185-12.79]|(2.03-inf)|(17.45-inf)|(-inf-88.5]|(-inf-0.975]|(-inf-2.005]|3
(12.79-inf)|(2.03-inf)|(17.45-inf)|(-inf-88.5]|(-inf-0.975]|(-inf-2.005]|3
(12.185-12.79]|(-inf-2.03]|(-inf-17.45]|(-inf-88.5]|(-inf-0.975]|(-inf-2.005]|1
(12.79-inf)|(2.03-inf)|(17.45-inf)|(133-inf)|(2.31-inf)|(2.475-inf)|1
(12.185-12.79]|(2.03-inf)|(17.45-inf)|(88.5-133]|(2.31-inf)|(2.475-inf)|1
(-inf-12.185]|(2.03-inf)|(17.45-inf)|(88.5-133]|(2.31-inf)|(2.475-inf)|2
(12.79-inf)|(2.03-inf)|(17.45-inf)|(88.5-133]|(2.31-inf)|(2.475-inf)|1
(12.185-12.79]|(2.03-inf)|(17.45-inf)|(133-inf)|(1.575-2.31]|(2.475-inf)|1
(-inf-12.185]|(-inf-2.03]|(17.45-inf)|(88.5-133]|(2.31-inf)|(2.475-inf)|1
(12.79-inf)|(2.03-inf)|(-inf-17.45]|(88.5-133]|(2.31-inf)|(2.475-inf)|1
(-inf-12.185]|(2.03-inf)|(17.45-inf)|(-inf-88.5]|(2.31-inf)|(2.475-inf)|2
(12.79-inf)|(2.03-inf)|(17.45-inf)|(-inf-88.5]|(2.31-inf)|(2.475-inf)|2
(12.185-12.79]|(2.03-inf)|(17.45-inf)|(-inf-88.5]|(2.31-inf)|(2.475-inf)|2
(12.185-12.79]|(2.03-inf)|(17.45-inf)|(88.5-133]|(1.575-2.31]|(2.475-inf)|2
(-inf-12.185]|(2.03-inf)|(17.45-inf)|(88.5-133]|(1.575-2.31]|(2.475-inf)|2
(12.185-12.79]|(2.03-inf)|(17.45-inf)|(88.5-133]|(2.31-inf)|(2.005-2.475]|1
(-inf-12.185]|(-inf-2.03]|(17.45-inf)|(88.5-133]|(1.575-2.31]|(2.475-inf)|1
(12.185-12.79]|(-inf-2.03]|(17.45-inf)|(88.5-133]|(1.575-2.31]|(2.475-inf)|1
(12.79-inf)|(2.03-inf)|(-inf-17.45]|(88.5-133]|(1.575-2.31]|(2.475-inf)|1
(12.79-inf)|(-inf-2.03]|(-inf-17.45]|(-inf-88.5]|(2.31-inf)|(2.475-inf)|1
(12.79-inf)|(2.03-inf)|(17.45-inf)|(-inf-88.5]|(1.575-2.31]|(2.475-inf)|1
(12.185-12.79]|(2.03-inf)|(17.45-inf)|(-inf-88.5]|(1.575-2.31]|(2.475-inf)|2
(-inf-12.185]|(2.03-inf)|(17.45-inf)|(-inf-88.5]|(1.575-2.31]|(2.475-inf)|2
(-inf-12.185]|(-inf-2.03]|(17.45-inf)|(-inf-88.5]|(1.575-2.31]|(2.475-inf)|2
(-inf-12.185]|(2.03-inf)|(17.45-inf)|(88.5-133]|(0.975-1.575]|(2.475-inf)|1
(12.185-12.79]|(-inf-2.03]|(-inf-17.45]|(133-inf)|(0.975-1.575]|(2.475-inf)|1
(12.185-12.79]|(-inf-2.03]|(17.45-inf)|(-inf-88.5]|(1.575-2.31]|(2.475-inf)|2
(12.185-12.79]|(-inf-2.03]|(-inf-17.45]|(133-inf)|(1.575-2.31]|(2.005-2.475]|1
(-inf-12.185]|(2.03-inf)|(17.45-inf)|(88.5-133]|(1.575-2.31]|(2.005-2.475]|2
(-inf-12.185]|(2.03-inf)|(17.45-inf)|(133-inf)|(0.975-1.575]|(2.005-2.475]|1
(12.79-inf)|(-inf-2.03]|(-inf-17.45]|(-inf-88.5]|(1.575-2.31]|(2.475-inf)|1
(12.79-inf)|(-inf-2.03]|(17.45-inf)|(88.5-133]|(1.575-2.31]|(2.005-2.475]|1
(-inf-12.185]|(2.03-inf)|(17.45-inf)|(-inf-88.5]|(0.975-1.575]|(2.475-inf)|1

## JRip

Decision list:

rules | predicted class
---|---
(flavanoids <= 1.39) and (ColorIntensity >= 4.1)|3 (39.0/0.0)
(Proline >= 760) and (Alcohol >= 13.05)|1 (51.0/1.0)
|2 (69.0/5.0)


