# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 1 | 0.700000 |
| StatusAccount = A11 and CreditHistory = A32 and SavingsAccount = A65 and ForeignWorker = A201 | 2 | 0.009858 |
| CreditHistory != A31 and StatusAccount != A14 and ForeignWorker = A201 and DurationMonth > 31.5 and Age <= 26.5 | 2 | 0.026256 |
| StatusAccount = A12 and CreditHistory = A30 and SavingsAccount = A61 and ForeignWorker = A201 | 2 | 0.007098 |
| CreditHistory != A31 and StatusAccount != A14 and ForeignWorker = A201 and DurationMonth <= 31.5 and Purpose != A49 and DurationMonth > 8.0 and Purpose != A41 and InstallmentPlans = A143 and EmploymentSince = A72 | 2 | 0.027894 |
| StatusAccount = A14 and CreditHistory = A30 and SavingsAccount = A65 and ForeignWorker = A201 | 2 | 0.000794 |
| CreditHistory != A31 and StatusAccount != A14 and ForeignWorker = A201 and DurationMonth > 31.5 and Age > 26.5 and StatusAccount = A11 | 2 | 0.022881 |
| StatusAccount = A11 and CreditHistory = A30 and SavingsAccount = A61 and ForeignWorker = A201 | 2 | 0.010063 |
| StatusAccount = A11 and CreditHistory = A31 and SavingsAccount = A61 and ForeignWorker = A201 | 2 | 0.018803 |
| StatusAccount = A11 and CreditHistory = A31 and SavingsAccount = A65 and ForeignWorker = A201 | 2 | 0.003165 |
| CreditHistory = A31 | 2 | 0.025888 |
| CreditHistory != A31 and StatusAccount != A14 and ForeignWorker = A201 and DurationMonth <= 31.5 and Purpose != A49 and DurationMonth > 8.0 and Purpose != A41 and InstallmentPlans != A143 and Purpose = A40 | 2 | 0.014107 |
| StatusAccount = A11 and CreditHistory = A33 and SavingsAccount = A61 and ForeignWorker = A201 | 2 | 0.010063 |
| StatusAccount = A11 and CreditHistory = A32 and SavingsAccount = A61 and ForeignWorker = A201 | 2 | 0.049652 |
| StatusAccount = A12 and CreditHistory = A34 and SavingsAccount = A63 and ForeignWorker = A201 | 2 | 0.000794 |
| StatusAccount = A12 and CreditHistory = A30 and SavingsAccount = A62 and ForeignWorker = A201 | 2 | 0.004739 |
| StatusAccount = A11 and CreditHistory = A32 and SavingsAccount = A62 and ForeignWorker = A201 | 2 | 0.003622 |
| StatusAccount = A12 and CreditHistory = A32 and SavingsAccount = A62 and ForeignWorker = A201 | 2 | 0.012116 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| CreditAmount <= 10918 and StatusAccount = A14 and InstallmentPlans = A143 | 1 | 0.477978 |
| DurationMonth <= 15.5 and Guarantors = A101 and CreditHistory = A34 | 1 | 0.122549 |
| CreditAmount <= 10841.5 and DurationMonth > 8.5 and SavingsAccount = A65 and CreditAmount > 1402.5 | 1 | 0.128487 |
| CreditAmount > 6686.5 and Age <= 29.5 | 2 | 0.070267 |
| DurationMonth <= 8.5 | 1 | 0.092976 |
| DurationMonth > 43.5 and ResidenceSince > 3.5 | 2 | 0.054111 |
| Purpose = A41 | 1 | 0.069087 |
| SavingsAccount = A62 and StatusAndSex = A93 | 1 | 0.064024 |
| SavingsAccount = A62 | 2 | 0.093006 |
| SavingsAccount = A63 | 1 | 0.038705 |
| SavingsAccount = A64 | 1 | 0.051843 |
| Purpose = A40 and InstallmentRate > 2.5 and InstallmentPlans = A143 and DurationMonth > 22.5 | 2 | 0.085452 |
| CreditAmount <= 1031 and Property = A121 | 1 | 0.023684 |
| CreditAmount > 1007 and DurationMonth <= 15.5 and CreditAmount > 1214.5 and CreditAmount > 1381.5 | 1 | 0.115365 |
| Age > 42.5 and CreditAmount > 1231 | 1 | 0.063932 |
| CreditAmount <= 2497.5 and Purpose = A40 | 2 | 0.251195 |
| Guarantors = A101 and NPeopleMain > 1.5 | 2 | 0.183908 |
| CreditAmount > 1211.5 and CreditAmount <= 3415 and Age <= 35.5 and ResidenceSince > 1.5 | 2 | 0.282981 |
| DurationMonth <= 33 and Age <= 28.5 | 1 | 0.255183 |
| Guarantors = A101 and NCredits > 1.5 | 1 | 0.072059 |
| Guarantors = A101 and StatusAndSex = A93 and ResidenceSince <= 2.5 | 1 | 0.041925 |
| Guarantors = A101 | 2 | 0.737445 |
|  | 1 | 0.722222 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| StatusAccount = A11 and DurationMonth >= 16 | 2 | 0.081318 |
| StatusAccount = A12 and DurationMonth >= 24 and Age <= 29 | 2 | 0.029206 |
| Purpose = A40 and InstallmentPlans = A141 | 2 | 0.015481 |
| StatusAccount = A12 and Property = A124 | 2 | 0.015867 |
|  | 1 | 0.846774 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

statusaccount|credithistory|savingsaccount|foreignworker|customer
---|---|---|---|---
a14|a30|a62|a202|1
a14|a31|a62|a201|1
a12|a31|a62|a201|2
a14|a32|a62|a202|1
a11|a31|a62|a201|1
a12|a30|a62|a201|2
a11|a34|a62|a202|1
a12|a31|a64|a201|2
a13|a31|a64|a201|1
a13|a32|a64|a202|1
a12|a33|a62|a201|1
a14|a33|a62|a201|1
a14|a34|a64|a202|1
a11|a31|a61|a202|1
a11|a32|a62|a201|2
a14|a32|a62|a201|1
a13|a32|a62|a201|1
a12|a32|a62|a201|2
a12|a33|a64|a201|1
a13|a34|a62|a201|1
a14|a32|a63|a202|1
a11|a34|a62|a201|1
a14|a31|a63|a201|1
a14|a33|a64|a201|1
a14|a34|a62|a201|1
a12|a34|a62|a201|1
a11|a31|a63|a201|2
a12|a30|a63|a201|1
a11|a32|a64|a201|1
a12|a32|a64|a201|1
a14|a32|a64|a201|1
a13|a31|a61|a201|1
a11|a34|a64|a201|1
a12|a31|a61|a201|1
a12|a34|a64|a201|1
a14|a32|a61|a202|1
a11|a31|a61|a201|2
a14|a31|a61|a201|1
a14|a34|a64|a201|1
a12|a32|a61|a202|1
a11|a32|a61|a202|1
a14|a33|a63|a201|1
a14|a30|a61|a201|1
a13|a34|a61|a202|1
a11|a32|a63|a201|1
a11|a30|a61|a201|2
a12|a32|a63|a201|1
a12|a30|a61|a201|2
a13|a30|a61|a201|2
a13|a32|a63|a201|1
a14|a32|a63|a201|1
a11|a34|a61|a202|1
a13|a33|a61|a201|1
a13|a32|a65|a202|1
a14|a31|a65|a201|1
a13|a34|a63|a201|1
a14|a32|a65|a202|1
a12|a34|a63|a201|2
a11|a31|a65|a201|2
a11|a34|a63|a201|1
a11|a32|a65|a202|1
a14|a33|a61|a201|1
a13|a31|a65|a201|1
a12|a33|a61|a201|1
a11|a33|a61|a201|2
a14|a34|a63|a201|1
a12|a30|a65|a201|1
a11|a34|a65|a202|1
a14|a34|a65|a202|1
a11|a30|a65|a201|1
a14|a30|a65|a201|2
a14|a32|a61|a201|1
a13|a32|a61|a201|1
a11|a32|a61|a201|2
a12|a32|a61|a201|1
a11|a33|a65|a201|1
a13|a34|a61|a201|1
a12|a33|a65|a201|1
a14|a34|a61|a201|1
a11|a34|a61|a201|1
a14|a33|a65|a201|1
a12|a34|a61|a201|1
a13|a32|a65|a201|1
a11|a32|a65|a201|2
a14|a32|a65|a201|1
a12|a32|a65|a201|1
a11|a34|a65|a201|1
a13|a34|a65|a201|1
a14|a34|a65|a201|1
a12|a34|a65|a201|1

## JRip

Decision list:

rules | predicted class
---|---
(StatusAccount = A11) and (DurationMonth >= 16)|2 (155.0/64.0)
(StatusAccount = A12) and (DurationMonth >= 24) and (Age <= 29)|2 (48.0/18.0)
(Purpose = A40) and (InstallmentPlans = A141)|2 (24.0/8.0)
(StatusAccount = A12) and (Property = A124)|2 (31.0/12.0)
|1 (642.0/114.0)


## PART

Decision list:

rules | predicted class
---|---
CreditAmount <= 10918 AND StatusAccount = A14 AND InstallmentPlans = A143|1 (288.0/22.0)
DurationMonth <= 15.5 AND Guarantors = A101 AND CreditHistory = A34|1 (54.0/9.0)
CreditAmount <= 10841.5 AND DurationMonth > 8.5 AND SavingsAccount = A65 AND CreditAmount > 1402.5|1 (66.0/14.0)
CreditAmount > 6686.5 AND Age <= 29.5|2 (22.0/2.0)
DurationMonth <= 8.5|1 (36.0/5.0)
DurationMonth > 43.5 AND ResidenceSince > 3.5|2 (18.0/2.0)
Purpose = A41|1 (26.0/5.0)
SavingsAccount = A62 AND StatusAndSex = A93|1 (26.0/6.0)
SavingsAccount = A62|2 (23.0/7.0)
SavingsAccount = A63|1 (20.0/6.0)
SavingsAccount = A64|1 (16.0/1.0)
Purpose = A40 AND InstallmentRate > 2.5 AND InstallmentPlans = A143 AND DurationMonth > 22.5|2 (16.0/1.0)
CreditAmount <= 1031 AND Property = A121|1 (15.0/7.0)
CreditAmount > 1007 AND DurationMonth <= 15.5 AND CreditAmount > 1214.5 AND CreditAmount > 1381.5|1 (53.0/14.0)
Age > 42.5 AND CreditAmount > 1231|1 (33.0/9.0)
CreditAmount <= 2497.5 AND Purpose = A40|2 (28.0/4.0)
Guarantors = A101 AND NPeopleMain > 1.5|2 (20.0/5.0)
CreditAmount > 1211.5 AND CreditAmount <= 3415 AND Age <= 35.5 AND ResidenceSince > 1.5|2 (36.0/8.0)
DurationMonth <= 33 AND Age <= 28.5|1 (34.0/5.0)
Guarantors = A101 AND NCredits > 1.5|1 (15.0/5.0)
Guarantors = A101 AND StatusAndSex = A93 AND ResidenceSince <= 2.5|1 (13.0/5.0)
Guarantors = A101|2 (26.0/9.0)
|1 (16.0/6.0)


## J48 Decision Tree

* CreditHistory = A31: 2 (20.0/5.0)
* CreditHistory != A31
	* StatusAccount = A14: 1 (179.0/20.0)
	* StatusAccount != A14
		* ForeignWorker = A201
			* DurationMonth <= 31.5
				* Purpose = A49: 1 (12.0/1.0)
				* Purpose != A49
					* DurationMonth <= 8.0: 1 (20.0/1.0)
					* DurationMonth > 8.0
						* Purpose = A41: 1 (16.0/2.0)
						* Purpose != A41
							* InstallmentPlans = A143
								* EmploymentSince = A72: 2 (21.0/9.0)
								* EmploymentSince != A72: 1 (96.0/33.0)
							* InstallmentPlans != A143
								* Purpose = A40: 2 (11.0/2.0)
								* Purpose != A40: 1 (17.0/8.0)
			* DurationMonth > 31.5
				* Age <= 26.5: 2 (11.0)
				* Age > 26.5
					* StatusAccount = A11: 2 (15.0/3.0)
					* StatusAccount != A11: 1 (22.0/10.0)
		* ForeignWorker != A201: 1 (10.0/1.0)


