# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| StatusAccount != A11 | 1 | 0.620921 |
| StatusAccount != A12 | 1 | 0.613268 |
| StatusAccount = A12 and CreditHistory = A30 and CreditAmount > 7839.5 and InstallmentRate = all and Guarantors = A101 and ResidenceSince = all and NPeopleMain = all | 2 | 0.004219 |
| StatusAccount != A14 and DurationMonth <= 43.5 and CreditAmount > 8150.5 | 2 | 0.023040 |
| StatusAccount = A12 and DurationMonth < 22.5 and CreditHistory = A30 | 2 | 0.002381 |
| StatusAccount = A11 and CreditHistory = A33 and CreditAmount <= 7839.5 and InstallmentRate = all and Guarantors = A101 and ResidenceSince = all and NPeopleMain = all | 2 | 0.011560 |
| StatusAccount = A11 and CreditHistory = A31 and CreditAmount <= 7839.5 and InstallmentRate = all and Guarantors = A102 and ResidenceSince = all and NPeopleMain = all | 2 | 0.000794 |
| StatusAccount = A12 and DurationMonth < 22.5 and CreditHistory = A31 | 2 | 0.006572 |
| StatusAccount = A11 and CreditHistory = A31 and CreditAmount <= 7839.5 and InstallmentRate = all and Guarantors = A101 and ResidenceSince = all and NPeopleMain = all | 2 | 0.013547 |
| StatusAccount != A14 and DurationMonth <= 43.5 and CreditAmount <= 8150.5 and ForeignWorker = A201 and Purpose != A41 and Guarantors != A103 and SavingsAccount != A64 and DurationMonth > 11.5 and StatusAccount = A11 and DurationMonth > 22.5 | 2 | 0.049637 |
| StatusAccount = A11 and CreditHistory = A30 and CreditAmount <= 7839.5 and InstallmentRate = all and Guarantors = A101 and ResidenceSince = all and NPeopleMain = all | 2 | 0.011163 |
| StatusAccount = A12 and CreditHistory = A32 and CreditAmount > 7839.5 and InstallmentRate = all and Guarantors = A101 and ResidenceSince = all and NPeopleMain = all | 2 | 0.014566 |
| StatusAccount != A14 and DurationMonth <= 43.5 and CreditAmount <= 8150.5 and ForeignWorker = A201 and Purpose != A41 and Guarantors != A103 and SavingsAccount != A64 and DurationMonth > 11.5 and StatusAccount != A11 and CreditAmount <= 2878.0 and CreditAmount > 954.5 and EmploymentSince != A74 and Age <= 25.5 | 2 | 0.012664 |
| StatusAccount != A14 and DurationMonth <= 43.5 and CreditAmount <= 8150.5 and ForeignWorker = A201 and Purpose != A41 and Guarantors != A103 and SavingsAccount != A64 and DurationMonth > 11.5 and StatusAccount != A11 and CreditAmount <= 2878.0 and CreditAmount <= 954.5 | 2 | 0.013547 |
| StatusAccount = A11 and CreditHistory = A32 and CreditAmount > 7839.5 and InstallmentRate = all and Guarantors = A101 and ResidenceSince = all and NPeopleMain = all | 2 | 0.011163 |
| StatusAccount != A14 and DurationMonth <= 43.5 and CreditAmount <= 8150.5 and ForeignWorker = A201 and Purpose != A41 and Guarantors != A103 and SavingsAccount != A64 and DurationMonth > 11.5 and StatusAccount = A11 and DurationMonth <= 22.5 and InstallmentRate > 3.5 and Age <= 45.5 and Job = A173 and CreditAmount <= 1421.5 | 2 | 0.015023 |
| StatusAccount != A14 and DurationMonth <= 43.5 and CreditAmount <= 8150.5 and ForeignWorker = A201 and Purpose != A41 and Guarantors != A103 and SavingsAccount != A64 and DurationMonth > 11.5 and StatusAccount = A11 and DurationMonth <= 22.5 and InstallmentRate > 3.5 and Age > 45.5 | 2 | 0.008574 |
| StatusAccount = A14 and InstallmentPlans = A143 and Purpose != A41 and Age > 23.5 and CreditAmount > 4560.5 and EmploymentSince != A74 and EmploymentSince != A75 | 2 | 0.007777 |
| StatusAccount = A14 and CreditHistory = A33 and CreditAmount > 7839.5 and InstallmentRate = all and Guarantors = A101 and ResidenceSince = all and NPeopleMain = all | 2 | 0.002381 |
| StatusAccount = A12 and CreditHistory = A30 and CreditAmount <= 7839.5 and InstallmentRate = all and Guarantors = A101 and ResidenceSince = all and NPeopleMain = all | 2 | 0.008412 |
| StatusAccount != A14 and DurationMonth > 43.5 and SavingsAccount = A61 | 2 | 0.039837 |
| StatusAccount = A12 and CreditHistory = A32 and CreditAmount > 7839.5 and InstallmentRate = all and Guarantors = A102 and ResidenceSince = all and NPeopleMain = all | 2 | 0.004739 |
| StatusAccount = A11 and CreditHistory = A32 and CreditAmount <= 7839.5 and InstallmentRate = all and Guarantors = A101 and ResidenceSince = all and NPeopleMain = all | 2 | 0.048273 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| StatusAccount = A14 and InstallmentPlans = A143 and CreditHistory = A34 | 1 | 0.297070 |
| StatusAccount = A14 and NCredits <= 1 and InstallmentPlans = A143 and Purpose = A43 | 1 | 0.131908 |
| StatusAccount = A14 and ForeignWorker = A201 and NCredits <= 1 and CreditHistory = A32 and Purpose = A40 | 1 | 0.082119 |
| DurationMonth <= 15 and Guarantors = A101 and CreditHistory = A34 | 1 | 0.131959 |
| StatusAccount = A14 and ForeignWorker = A201 and Purpose = A41 | 1 | 0.088288 |
| DurationMonth <= 30 and Guarantors = A103 and InstallmentPlans = A143 | 1 | 0.084746 |
| StatusAccount = A13 and NPeopleMain <= 1 and SavingsAccount = A61 and Property = A123 | 1 | 0.031089 |
| StatusAccount = A13 and NPeopleMain <= 1 | 1 | 0.068651 |
| StatusAccount = A14 and ForeignWorker = A201 and Purpose = A43 and NCredits <= 1 | 1 | 0.023188 |
| StatusAccount = A14 and ForeignWorker = A201 and Purpose = A42 and StatusAndSex = A93 | 1 | 0.046172 |
| DurationMonth <= 11 and CreditHistory = A32 and Property = A121 | 1 | 0.085730 |
| SavingsAccount = A64 and Property = A121 | 1 | 0.014599 |
| SavingsAccount = A65 and Guarantors = A101 and StatusAccount = A12 and NCredits <= 1 and Property = A123 | 1 | 0.035714 |
| StatusAccount = A14 and ForeignWorker = A201 and EmploymentSince = A74 and Telephone = A192 | 1 | 0.035714 |
| SavingsAccount = A64 and Property = A123 | 1 | 0.014599 |
| SavingsAccount = A65 and Guarantors = A101 and CreditHistory = A33 | 1 | 0.032584 |
| DurationMonth > 42 and ResidenceSince > 1 | 2 | 0.122670 |
| ForeignWorker = A202 and StatusAccount = A11 and Age <= 31 | 1 | 0.025105 |
| Purpose = A41 and CreditAmount <= 8072 | 1 | 0.070560 |
| StatusAccount = A14 and ForeignWorker = A201 and Purpose = A40 and CreditAmount > 2284 | 2 | 0.035734 |
| StatusAccount = A14 and ForeignWorker = A201 and Property = A121 and Age > 23 | 1 | 0.034770 |
| StatusAccount = A11 and Purpose = A46 | 2 | 0.044092 |
| StatusAccount = A14 and ForeignWorker = A201 and ResidenceSince > 1 and SavingsAccount = A65 | 1 | 0.028959 |
| CreditHistory = A31 and Purpose = A40 | 2 | 0.028892 |
| StatusAccount = A11 and Job = A174 and InstallmentRate > 1 | 1 | 0.055411 |
| StatusAccount = A11 and Purpose = A49 | 1 | 0.016846 |
| StatusAccount = A11 and Purpose = A43 and SavingsAccount = A61 and NCredits > 1 | 2 | 0.037975 |
| StatusAccount = A11 and Purpose = A40 and SavingsAccount = A61 and InstallmentPlans = A143 and StatusAndSex = A92 and InstallmentRate > 2 | 2 | 0.044025 |
| StatusAccount = A11 and Purpose = A43 and SavingsAccount = A61 and CreditHistory = A32 and ResidenceSince > 1 and EmploymentSince = A73 and DurationMonth > 15 | 2 | 0.020645 |
| StatusAccount = A11 and Purpose = A40 and SavingsAccount = A61 and InstallmentPlans = A143 and StatusAndSex = A93 and DurationMonth > 22 | 2 | 0.044025 |
| StatusAccount = A11 and CreditHistory = A31 and InstallmentPlans = A141 | 2 | 0.032757 |
| CreditHistory = A30 and ResidenceSince > 2 | 2 | 0.067957 |
| Purpose = A41 | 2 | 0.062243 |
| StatusAccount = A12 and EmploymentSince = A74 | 1 | 0.091787 |
| NPeopleMain > 1 and InstallmentPlans = A143 and Housing = A152 | 1 | 0.033962 |
| NPeopleMain > 1 | 2 | 0.150970 |
| CreditHistory = A31 | 1 | 0.035766 |
| Purpose = A46 | 1 | 0.024423 |
| Purpose = A49 and StatusAndSex = A93 and CreditAmount <= 4473 | 1 | 0.032847 |
| CreditHistory = A30 and StatusAndSex = A93 | 1 | 0.016667 |
| Purpose = A40 and InstallmentPlans = A141 | 2 | 0.081900 |
| Guarantors = A102 and SavingsAccount = A61 | 1 | 0.028800 |
| Guarantors = A101 and EmploymentSince = A75 and StatusAndSex = A92 | 1 | 0.049612 |
| Guarantors = A101 and CreditHistory = A34 and Age > 34 | 1 | 0.055371 |
| Guarantors = A101 and Purpose = A40 and CreditHistory = A32 and EmploymentSince = A73 | 2 | 0.065041 |
| Guarantors = A101 and Purpose = A43 and Telephone = A192 | 2 | 0.133057 |
| Guarantors = A101 and Job = A174 | 2 | 0.141182 |
| Guarantors = A101 and Housing = A151 and InstallmentRate > 2 | 2 | 0.113953 |
| Guarantors = A101 and Housing = A151 and ResidenceSince > 1 | 1 | 0.183673 |
| Guarantors = A101 and Housing = A152 and NCredits > 1 and SavingsAccount = A61 and Property = A123 | 1 | 0.101215 |
| InstallmentPlans = A141 | 1 | 0.079256 |
| Housing = A152 and Property = A121 and InstallmentRate > 3 | 2 | 0.216667 |
| Housing = A152 and Age > 34 | 1 | 0.164835 |
| Guarantors = A101 and Housing = A152 and SavingsAccount = A61 and Property = A123 and InstallmentPlans = A143 | 2 | 0.320057 |
| Guarantors = A101 and Housing = A152 and Age <= 30 and Age > 23 | 1 | 0.214286 |
| Housing = A152 and SavingsAccount = A61 and InstallmentRate <= 2 | 2 | 0.427350 |
|  | 2 | 0.738095 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| StatusAccount = A11 and Job = A173 and DurationMonth >= 40 | 2 | 0.024768 |
| StatusAccount = A11 and DurationMonth >= 16 and CreditAmount <= 2462 and EmploymentSince = A73 and DurationMonth <= 24 | 2 | 0.020218 |
| StatusAccount = A11 and DurationMonth >= 24 and Purpose = A40 and DurationMonth <= 28 | 2 | 0.018692 |
| StatusAccount = A12 and SavingsAccount = A61 and DurationMonth >= 45 | 2 | 0.020218 |
| StatusAccount = A11 and Age <= 35 and CreditAmount <= 1366 | 2 | 0.020145 |
| StatusAccount = A12 and DurationMonth >= 24 and SavingsAccount = A61 | 2 | 0.022818 |
| StatusAccount = A11 and DurationMonth >= 33 | 2 | 0.016229 |
| EmploymentSince = A72 and DurationMonth >= 21 | 2 | 0.014216 |
| StatusAccount = A12 and SavingsAccount = A62 | 2 | 0.013127 |
| InstallmentPlans = A141 and Purpose = A40 and Job = A173 and DurationMonth >= 12 | 2 | 0.015755 |
| Age <= 30 and StatusAndSex = A92 and InstallmentRate >= 3 | 2 | 0.009086 |
|  | 1 | 0.879888 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

statusaccount|credithistory|creditamount|installmentrate|guarantors|residencesince|npeoplemain|customer
---|---|---|---|---|---|---|---
a12|a31|(7839.5-inf)|all|a102|all|all|1
a11|a31|(-inf-7839.5]|all|a102|all|all|2
a11|a32|(7839.5-inf)|all|a102|all|all|1
a12|a32|(7839.5-inf)|all|a102|all|all|2
a12|a34|(7839.5-inf)|all|a102|all|all|1
a12|a33|(-inf-7839.5]|all|a102|all|all|1
a13|a32|(-inf-7839.5]|all|a102|all|all|1
a14|a32|(-inf-7839.5]|all|a102|all|all|1
a11|a32|(-inf-7839.5]|all|a102|all|all|1
a12|a32|(-inf-7839.5]|all|a102|all|all|1
a13|a34|(-inf-7839.5]|all|a102|all|all|1
a11|a31|(-inf-7839.5]|all|a103|all|all|1
a14|a31|(-inf-7839.5]|all|a103|all|all|1
a14|a34|(-inf-7839.5]|all|a102|all|all|1
a11|a34|(-inf-7839.5]|all|a102|all|all|1
a11|a30|(-inf-7839.5]|all|a103|all|all|1
a12|a31|(7839.5-inf)|all|a101|all|all|1
a14|a30|(7839.5-inf)|all|a101|all|all|1
a14|a32|(-inf-7839.5]|all|a103|all|all|1
a13|a32|(-inf-7839.5]|all|a103|all|all|1
a11|a32|(-inf-7839.5]|all|a103|all|all|1
a12|a32|(-inf-7839.5]|all|a103|all|all|1
a12|a30|(7839.5-inf)|all|a101|all|all|2
a11|a30|(7839.5-inf)|all|a101|all|all|1
a11|a33|(7839.5-inf)|all|a101|all|all|1
a12|a33|(7839.5-inf)|all|a101|all|all|1
a12|a34|(-inf-7839.5]|all|a103|all|all|1
a13|a31|(-inf-7839.5]|all|a101|all|all|1
a14|a34|(-inf-7839.5]|all|a103|all|all|1
a14|a33|(7839.5-inf)|all|a101|all|all|2
a12|a31|(-inf-7839.5]|all|a101|all|all|2
a11|a34|(-inf-7839.5]|all|a103|all|all|1
a14|a31|(-inf-7839.5]|all|a101|all|all|1
a11|a31|(-inf-7839.5]|all|a101|all|all|2
a13|a30|(-inf-7839.5]|all|a101|all|all|1
a14|a32|(7839.5-inf)|all|a101|all|all|1
a12|a30|(-inf-7839.5]|all|a101|all|all|2
a14|a30|(-inf-7839.5]|all|a101|all|all|1
a11|a32|(7839.5-inf)|all|a101|all|all|2
a11|a30|(-inf-7839.5]|all|a101|all|all|2
a12|a32|(7839.5-inf)|all|a101|all|all|2
a14|a33|(-inf-7839.5]|all|a101|all|all|1
a13|a33|(-inf-7839.5]|all|a101|all|all|1
a11|a33|(-inf-7839.5]|all|a101|all|all|2
a12|a33|(-inf-7839.5]|all|a101|all|all|1
a14|a34|(7839.5-inf)|all|a101|all|all|1
a12|a34|(7839.5-inf)|all|a101|all|all|1
a11|a34|(7839.5-inf)|all|a101|all|all|1
a14|a32|(-inf-7839.5]|all|a101|all|all|1
a11|a32|(-inf-7839.5]|all|a101|all|all|2
a12|a32|(-inf-7839.5]|all|a101|all|all|1
a13|a32|(-inf-7839.5]|all|a101|all|all|1
a13|a34|(-inf-7839.5]|all|a101|all|all|1
a11|a34|(-inf-7839.5]|all|a101|all|all|1
a14|a34|(-inf-7839.5]|all|a101|all|all|1
a12|a34|(-inf-7839.5]|all|a101|all|all|1

## JRip

Decision list:

rules | predicted class
---|---
(StatusAccount = A11) and (Job = A173) and (DurationMonth >= 40)|2 (16.0/0.0)
(StatusAccount = A11) and (DurationMonth >= 16) and (CreditAmount <= 2462) and (EmploymentSince = A73) and (DurationMonth <= 24)|2 (13.0/0.0)
(StatusAccount = A11) and (DurationMonth >= 24) and (Purpose = A40) and (DurationMonth <= 28)|2 (12.0/0.0)
(StatusAccount = A12) and (SavingsAccount = A61) and (DurationMonth >= 45)|2 (13.0/0.0)
(StatusAccount = A11) and (Age <= 35) and (CreditAmount <= 1366)|2 (28.0/9.0)
(StatusAccount = A12) and (DurationMonth >= 24) and (SavingsAccount = A61)|2 (43.0/18.0)
(StatusAccount = A11) and (DurationMonth >= 33)|2 (28.0/11.0)
(EmploymentSince = A72) and (DurationMonth >= 21)|2 (47.0/25.0)
(StatusAccount = A12) and (SavingsAccount = A62)|2 (33.0/16.0)
(InstallmentPlans = A141) and (Purpose = A40) and (Job = A173) and (DurationMonth >= 12)|2 (11.0/0.0)
(Age <= 30) and (StatusAndSex = A92) and (InstallmentRate >= 3)|2 (52.0/33.0)
|1 (604.0/86.0)


## PART

Decision list:

rules | predicted class
---|---
StatusAccount = A14 AND InstallmentPlans = A143 AND CreditHistory = A34|1 (120.0/3.0)
StatusAccount = A14 AND NCredits <= 1 AND InstallmentPlans = A143 AND Purpose = A43|1 (43.0/1.0)
StatusAccount = A14 AND ForeignWorker = A201 AND NCredits <= 1 AND CreditHistory = A32 AND Purpose = A40|1 (28.0/2.0)
DurationMonth <= 15 AND Guarantors = A101 AND CreditHistory = A34|1 (54.0/7.0)
StatusAccount = A14 AND ForeignWorker = A201 AND Purpose = A41|1 (30.0/2.0)
DurationMonth <= 30 AND Guarantors = A103 AND InstallmentPlans = A143|1 (25.0)
StatusAccount = A13 AND NPeopleMain <= 1 AND SavingsAccount = A61 AND Property = A123|1 (14.0/3.0)
StatusAccount = A13 AND NPeopleMain <= 1|1 (32.0/5.0)
StatusAccount = A14 AND ForeignWorker = A201 AND Purpose = A43 AND NCredits <= 1|1 (8.0)
StatusAccount = A14 AND ForeignWorker = A201 AND Purpose = A42 AND StatusAndSex = A93|1 (15.0/1.0)
DurationMonth <= 11 AND CreditHistory = A32 AND Property = A121|1 (29.0/1.0)
SavingsAccount = A64 AND Property = A121|1 (4.0)
SavingsAccount = A65 AND Guarantors = A101 AND StatusAccount = A12 AND NCredits <= 1 AND Property = A123|1 (10.0)
StatusAccount = A14 AND ForeignWorker = A201 AND EmploymentSince = A74 AND Telephone = A192|1 (10.0)
SavingsAccount = A64 AND Property = A123|1 (4.0)
SavingsAccount = A65 AND Guarantors = A101 AND CreditHistory = A33|1 (11.0/1.0)
DurationMonth > 42 AND ResidenceSince > 1|2 (44.0/8.0)
ForeignWorker = A202 AND StatusAccount = A11 AND Age <= 31|1 (6.0)
Purpose = A41 AND CreditAmount <= 8072|1 (23.0/3.0)
StatusAccount = A14 AND ForeignWorker = A201 AND Purpose = A40 AND CreditAmount > 2284|2 (6.0)
StatusAccount = A14 AND ForeignWorker = A201 AND Property = A121 AND Age > 23|1 (12.0/1.0)
StatusAccount = A11 AND Purpose = A46|2 (12.0/2.0)
StatusAccount = A14 AND ForeignWorker = A201 AND ResidenceSince > 1 AND SavingsAccount = A65|1 (6.0)
CreditHistory = A31 AND Purpose = A40|2 (6.0)
StatusAccount = A11 AND Job = A174 AND InstallmentRate > 1|1 (20.0/5.0)
StatusAccount = A11 AND Purpose = A49|1 (7.0/2.0)
StatusAccount = A11 AND Purpose = A43 AND SavingsAccount = A61 AND NCredits > 1|2 (6.0)
StatusAccount = A11 AND Purpose = A40 AND SavingsAccount = A61 AND InstallmentPlans = A143 AND StatusAndSex = A92 AND InstallmentRate > 2|2 (7.0)
StatusAccount = A11 AND Purpose = A43 AND SavingsAccount = A61 AND CreditHistory = A32 AND ResidenceSince > 1 AND EmploymentSince = A73 AND DurationMonth > 15|2 (5.0/1.0)
StatusAccount = A11 AND Purpose = A40 AND SavingsAccount = A61 AND InstallmentPlans = A143 AND StatusAndSex = A93 AND DurationMonth > 22|2 (7.0)
StatusAccount = A11 AND CreditHistory = A31 AND InstallmentPlans = A141|2 (7.0/1.0)
CreditHistory = A30 AND ResidenceSince > 2|2 (12.0/1.0)
Purpose = A41|2 (8.0/1.0)
StatusAccount = A12 AND EmploymentSince = A74|1 (22.0/4.0)
NPeopleMain > 1 AND InstallmentPlans = A143 AND Housing = A152|1 (15.0/6.0)
NPeopleMain > 1|2 (15.0/1.0)
CreditHistory = A31|1 (5.0/1.0)
Purpose = A46|1 (6.0/2.0)
Purpose = A49 AND StatusAndSex = A93 AND CreditAmount <= 4473|1 (6.0)
CreditHistory = A30 AND StatusAndSex = A93|1 (3.0)
Purpose = A40 AND InstallmentPlans = A141|2 (10.0/1.0)
Guarantors = A102 AND SavingsAccount = A61|1 (9.0/3.0)
Guarantors = A101 AND EmploymentSince = A75 AND StatusAndSex = A92|1 (9.0/1.0)
Guarantors = A101 AND CreditHistory = A34 AND Age > 34|1 (10.0)
Guarantors = A101 AND Purpose = A40 AND CreditHistory = A32 AND EmploymentSince = A73|2 (10.0/3.0)
Guarantors = A101 AND Purpose = A43 AND Telephone = A192|2 (16.0/4.0)
Guarantors = A101 AND Job = A174|2 (11.0/1.0)
Guarantors = A101 AND Housing = A151 AND InstallmentRate > 2|2 (17.0/4.0)
Guarantors = A101 AND Housing = A151 AND ResidenceSince > 1|1 (13.0/1.0)
Guarantors = A101 AND Housing = A152 AND NCredits > 1 AND SavingsAccount = A61 AND Property = A123|1 (11.0/2.0)
InstallmentPlans = A141|1 (6.0)
Housing = A152 AND Property = A121 AND InstallmentRate > 3|2 (10.0/1.0)
Housing = A152 AND Age > 34|1 (15.0/2.0)
Guarantors = A101 AND Housing = A152 AND SavingsAccount = A61 AND Property = A123 AND InstallmentPlans = A143|2 (11.0/2.0)
Guarantors = A101 AND Housing = A152 AND Age <= 30 AND Age > 23|1 (12.0/1.0)
Housing = A152 AND SavingsAccount = A61 AND InstallmentRate <= 2|2 (6.0/1.0)
|2 (21.0/5.0)


## J48 Decision Tree

* StatusAccount = A14
	* InstallmentPlans = A143
		* Purpose = A41: 1 (37.0)
		* Purpose != A41
			* Age <= 23.5: 1 (17.0/6.0)
			* Age > 23.5
				* CreditAmount <= 4560.5: 1 (172.0/7.0)
				* CreditAmount > 4560.5
					* EmploymentSince = A74: 1 (8.0)
					* EmploymentSince != A74
						* EmploymentSince = A75: 1 (10.0/1.0)
						* EmploymentSince != A75: 2 (12.0/5.0)
	* InstallmentPlans != A143: 1 (44.0/12.0)
* StatusAccount != A14
	* DurationMonth <= 43.5
		* CreditAmount <= 8150.5
			* ForeignWorker = A201
				* Purpose = A41: 1 (26.0/3.0)
				* Purpose != A41
					* Guarantors = A103: 1 (25.0/3.0)
					* Guarantors != A103
						* SavingsAccount = A64: 1 (15.0/2.0)
						* SavingsAccount != A64
							* DurationMonth <= 11.5: 1 (58.0/13.0)
							* DurationMonth > 11.5
								* StatusAccount = A11
									* DurationMonth <= 22.5
										* InstallmentRate <= 3.5: 1 (29.0/10.0)
										* InstallmentRate > 3.5
											* Age <= 45.5
												* Job = A173
													* CreditAmount <= 1421.5: 2 (13.0/3.0)
													* CreditAmount > 1421.5: 1 (10.0/5.0)
												* Job != A173: 1 (11.0/4.0)
											* Age > 45.5: 2 (9.0/2.0)
									* DurationMonth > 22.5: 2 (52.0/11.0)
								* StatusAccount != A11
									* CreditAmount <= 2878.0
										* CreditAmount <= 954.5: 2 (12.0/2.0)
										* CreditAmount > 954.5
											* EmploymentSince = A74: 1 (10.0/1.0)
											* EmploymentSince != A74
												* Age <= 25.5: 2 (14.0/4.0)
												* Age > 25.5: 1 (45.0/18.0)
									* CreditAmount > 2878.0: 1 (56.0/10.0)
			* ForeignWorker != A201: 1 (19.0/1.0)
		* CreditAmount > 8150.5: 2 (25.0/7.0)
	* DurationMonth > 43.5
		* SavingsAccount = A61: 2 (27.0/1.0)
		* SavingsAccount != A61: 1 (16.0/7.0)


## SimpleCart Decision Tree

	* StatusAccount=(A11)|(A12)
	* DurationMonth < 22.5
			* CreditHistory=(A31)|(A30): 2(19.0/7.0)
			* CreditHistory!=(A31)|(A30): 1(174.0/74.0)
	* DurationMonth >= 22.5
				* SavingsAccount=(A61)|(A62)|(A63)
			* DurationMonth < 47.5
												* Purpose=(A40)|(A45)|(A43)|(A46)|(A42)|(A49)|(A410)|(A44)|(A48): 2(75.0/47.0)
												* Purpose!=(A40)|(A45)|(A43)|(A46)|(A42)|(A49)|(A410)|(A44)|(A48)
					* CreditAmount < 8097.5: 1(15.0/1.0)
					* CreditAmount >= 8097.5: 2(5.0/2.0)
			* DurationMonth >= 47.5: 2(30.0/4.0)
				* SavingsAccount!=(A61)|(A62)|(A63): 1(27.0/11.0)
	* StatusAccount!=(A11)|(A12): 1(354.0/55.0)


