# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| StatusAccount != A12 and InstallmentPlans != A142 and CreditHistory != A31 | 1 | 0.595571 |
| StatusAccount = A12 and DurationMonth < 22.5 and CreditHistory != A30 and CreditAmount < 8724.5 and DurationMonth >= 8.5 and CreditAmount >= 979.5 and EmploymentSince != A72 | 1 | 0.150855 |
| StatusAccount != A14 and CreditAmount > 6681.0 and SavingsAccount != A65 | 2 | 0.043068 |
| StatusAccount != A14 and CreditAmount <= 6681.0 and ForeignWorker = A201 and DurationMonth <= 30.0 and CreditHistory != A30 and Purpose != A41 and Guarantors != A103 and CreditAmount <= 1366.0 and DurationMonth > 16.0 | 2 | 0.029273 |
| StatusAccount = A12 and DurationMonth >= 22.5 and SavingsAccount != A63 and StatusAccount!=(A11) | 1 | 0.090370 |
| StatusAccount = A11 and DurationMonth > 8.5 and DurationMonth <= 31.5 and CreditHistory = A32 and Age <= 25.5 | 2 | 0.017079 |
| StatusAccount != A14 and CreditAmount <= 6681.0 and ForeignWorker = A201 and DurationMonth > 30.0 and Age <= 26.0 | 2 | 0.017577 |
| StatusAccount != A14 and CreditAmount <= 6681.0 and ForeignWorker = A201 and DurationMonth <= 30.0 and CreditHistory = A30 | 2 | 0.013963 |
| StatusAccount = A11 and DurationMonth > 31.5 and CreditHistory = A32 and Age > 25.5 | 2 | 0.017419 |
| StatusAccount != A14 and CreditAmount <= 6681.0 and ForeignWorker = A201 and DurationMonth <= 30.0 and CreditHistory != A30 and Purpose != A41 and Guarantors != A103 and CreditAmount > 1366.0 and SavingsAccount != A63 and StatusAndSex = A91 | 2 | 0.007233 |
| StatusAccount != A12 and InstallmentPlans = A142 and Purpose != A46 | 1 | 0.046046 |
| StatusAccount = A12 and DurationMonth < 22.5 and CreditHistory != A30 and CreditAmount < 8724.5 and DurationMonth >= 8.5 and CreditAmount < 979.5 and Property = A123 | 2 | 0.010989 |
| StatusAccount != A14 and CreditAmount <= 6681.0 and ForeignWorker = A201 and DurationMonth > 30.0 and Age > 26.0 and CreditAmount > 3149.0 and Age > 41.0 | 2 | 0.009162 |
| StatusAccount != A14 and CreditAmount <= 6681.0 and ForeignWorker = A201 and DurationMonth > 30.0 and Age > 26.0 and CreditAmount <= 3149.0 | 2 | 0.012076 |
| StatusAccount != A12 and InstallmentPlans != A142 and CreditHistory = A33 and InstallmentRate >= 3.5 and Age < 31.0 | 2 | 0.007874 |
| StatusAccount = A12 and DurationMonth < 22.5 and CreditHistory != A30 and CreditAmount < 8724.5 and DurationMonth < 8.5 | 1 | 0.044326 |
| StatusAccount = A12 and DurationMonth < 22.5 and CreditHistory = A31 | 2 | 0.006572 |
| StatusAccount = A11 and DurationMonth > 8.5 and DurationMonth <= 31.5 and CreditHistory = A31 and Age > 25.5 | 2 | 0.011560 |
| StatusAccount = A14 and DurationMonth > 31.5 and CreditHistory = A34 and Age <= 25.5 | 2 | 0.004739 |
| StatusAccount = A12 and DurationMonth <= 8.5 and CreditHistory = A32 and Age <= 25.5 | 2 | 0.002113 |
| StatusAccount = A11 and DurationMonth > 8.5 and DurationMonth <= 31.5 and CreditHistory = A33 and Age > 25.5 | 2 | 0.005642 |
| StatusAccount = A12 and DurationMonth < 22.5 and CreditHistory != A30 and CreditAmount < 8724.5 and DurationMonth >= 8.5 and CreditAmount < 979.5 and Property != A123 and CreditAmount < 663.0 | 1 | 0.014599 |
| StatusAccount != A12 and InstallmentPlans = A142 and Purpose = A49 and DurationMonth >= 15.0 | 2 | 0.001272 |
| StatusAccount = A12 and DurationMonth > 31.5 and CreditHistory = A32 and Age > 25.5 | 2 | 0.012579 |
| StatusAccount = A13 and DurationMonth > 8.5 and DurationMonth <= 31.5 and CreditHistory = A33 and Age > 25.5 | 2 | 0.000794 |
| StatusAccount = A12 and DurationMonth < 22.5 and CreditHistory != A30 and CreditAmount < 8724.5 and DurationMonth >= 8.5 and CreditAmount >= 979.5 and EmploymentSince != A75 | 1 | 0.135681 |
| StatusAccount = A12 and DurationMonth < 22.5 and CreditHistory != A30 and CreditAmount < 8724.5 and DurationMonth >= 8.5 and CreditAmount < 979.5 and Property != A123 and CreditAmount >= 663.0 and EmploymentSince != A71 | 1 | 0.011489 |
| StatusAccount = A12 and DurationMonth > 31.5 and CreditHistory = A30 and Age > 25.5 | 2 | 0.005642 |
| StatusAccount != A12 and InstallmentPlans != A142 and CreditHistory != A33 | 1 | 0.583891 |
| StatusAccount != A14 and CreditAmount <= 6681.0 and ForeignWorker = A201 and DurationMonth <= 30.0 and CreditHistory != A30 and Purpose != A41 and Guarantors != A103 and CreditAmount > 1366.0 and SavingsAccount = A63 | 1 | 0.023188 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| StatusAccount = A14 and InstallmentPlans != A141 and CreditHistory != A33 and Purpose != A46 and StatusAndSex != A92 and Purpose != A49 and Property != A121 and SavingsAccount != A62 and Purpose != A40 and EmploymentSince != A74 | 1 | 0.212828 |
| CreditHistory != A30 and StatusAccount = A14 and InstallmentPlans != A141 and Purpose != A41 and CreditHistory != A33 and NPeopleMain <= 1.0 and Job != A174 and EmploymentSince != A72 and InstallmentPlans = A143 and Telephone = A192 | 1 | 0.131833 |
| CreditHistory = A30 and Housing != A152 and StatusAccount = A12 | 2 | 0.013384 |
| StatusAccount = A14 and ForeignWorker = A201 and InstallmentPlans != A141 and Purpose != A41 and Property != A123 and Purpose != A46 and Purpose = A43 | 1 | 0.111486 |
| ForeignWorker != A201 and StatusAndSex = A93 | 1 | 0.070671 |
| CreditHistory != A30 and StatusAccount = A14 and EmploymentSince = A74 and SavingsAccount != A61 | 1 | 0.067376 |
| CreditHistory != A30 and CreditHistory != A31 and CreditAmount <= 7721.0 and Purpose != A410 and DurationMonth <= 7.0 and EmploymentSince != A72 | 1 | 0.117450 |
| CreditHistory = A30 and Housing = A152 and InstallmentRate <= 2.0 and Telephone = A192 | 2 | 0.007603 |
| StatusAccount != A11 and CreditAmount > 9857.0 and DurationMonth <= 36.0 | 2 | 0.026190 |
| StatusAccount != A11 and Job = A171 and DurationMonth <= 14.0 | 1 | 0.016600 |
| StatusAccount != A11 and Job != A171 and Purpose = A41 and StatusAndSex = A93 | 1 | 0.091912 |
| StatusAccount != A11 and Job != A171 and SavingsAccount = A65 and Purpose != A46 and InstallmentPlans != A141 and EmploymentSince = A75 | 1 | 0.057252 |
| StatusAccount != A11 and Job != A171 and Purpose != A45 and StatusAccount != A12 and CreditHistory != A33 and InstallmentPlans = A143 and EmploymentSince = A75 and InstallmentRate > 2.0 | 1 | 0.053640 |
| CreditHistory = A30 and Housing = A152 and CreditAmount <= 4169.0 | 2 | 0.011331 |
| StatusAccount != A11 and Job != A171 and Guarantors = A103 and Job != A173 | 1 | 0.043651 |
| CreditHistory = A31 and Property != A121 and Property != A123 and Job != A173 | 2 | 0.014286 |
| Purpose = A410 | 1 | 0.025521 |
| DurationMonth <= 30.0 and Purpose = A41 and NCredits > 1.0 | 1 | 0.033058 |
| DurationMonth <= 30.0 and Purpose = A41 and EmploymentSince != A73 and InstallmentRate > 2.0 | 1 | 0.009726 |
| StatusAccount != A11 and Guarantors != A102 and Purpose != A45 and SavingsAccount = A64 and Property = A121 | 1 | 0.033058 |
| StatusAccount = A14 and CreditHistory != A33 and SavingsAccount != A63 and Property = A124 | 1 | 0.033471 |
| Property = A124 and InstallmentRate > 2.0 and Housing != A151 and SavingsAccount != A65 and CreditHistory != A34 and CreditHistory != A32 | 2 | 0.023754 |
| Property = A124 and InstallmentRate > 2.0 and Purpose != A40 and EmploymentSince = A75 | 2 | 0.029138 |
| DurationMonth <= 30.0 and Purpose != A41 and Purpose != A40 and Guarantors != A103 and Purpose != A45 and EmploymentSince = A74 and Age > 23.0 and Purpose != A42 | 1 | 0.100418 |
| Purpose = A41 and CreditAmount <= 7297.0 | 1 | 0.053178 |
| Purpose != A41 and Property = A124 and Housing = A152 and CreditAmount <= 6403.0 | 2 | 0.011660 |
| Purpose != A41 and StatusAccount != A11 and Guarantors != A102 and CreditHistory != A31 and StatusAndSex != A91 and Purpose != A40 and Job != A174 and Purpose != A45 and CreditHistory != A32 and InstallmentRate > 1.0 and EmploymentSince != A72 and NCredits > 1.0 and Property = A123 | 1 | 0.058296 |
| Purpose != A41 and DurationMonth <= 15.0 and Guarantors != A103 and Purpose != A49 and SavingsAccount != A62 and Purpose != A46 and CreditHistory != A33 and NPeopleMain > 1.0 and InstallmentRate <= 3.0 | 1 | 0.062500 |
| Purpose != A41 and StatusAccount != A11 and CreditHistory != A31 and Guarantors != A102 and NPeopleMain <= 1.0 and DurationMonth <= 24.0 and Housing != A153 and Purpose != A46 and StatusAccount = A13 and Property != A121 | 1 | 0.054054 |
| Purpose != A41 and StatusAccount = A14 and CreditHistory != A33 and Purpose != A46 and SavingsAccount != A62 and Housing != A151 and Job != A172 and EmploymentSince != A75 and CreditAmount <= 3758.0 and Property = A121 | 1 | 0.041511 |
| Purpose != A41 and Purpose = A40 and InstallmentPlans != A143 and Telephone != A192 | 2 | 0.056522 |
| Purpose != A41 and Guarantors = A103 and EmploymentSince != A74 and DurationMonth <= 15.0 | 1 | 0.034314 |
| Purpose != A41 and CreditHistory = A34 and Purpose != A49 and StatusAndSex != A94 and DurationMonth <= 24.0 and EmploymentSince != A74 and InstallmentPlans != A141 and Purpose != A46 and NCredits > 1.0 and StatusAccount != A12 and Purpose != A42 | 1 | 0.012690 |
| Purpose != A41 and CreditHistory = A34 and Purpose != A40 and InstallmentPlans = A143 and StatusAccount = A14 | 1 | 0.036096 |
| Purpose != A41 and SavingsAccount != A61 and CreditHistory != A32 and SavingsAccount = A62 | 1 | 0.044131 |
| Purpose != A41 and SavingsAccount = A65 and CreditHistory != A32 and StatusAccount = A12 | 1 | 0.048309 |
| Purpose != A41 and CreditHistory = A33 and InstallmentRate > 1.0 and EmploymentSince != A73 | 2 | 0.064210 |
| Purpose != A41 and SavingsAccount = A63 and NCredits <= 1.0 and DurationMonth > 13.0 | 1 | 0.041667 |
| Purpose != A41 and CreditHistory = A31 and ResidenceSince <= 3.0 | 2 | 0.023392 |
| CreditHistory != A31 and Purpose != A41 and ForeignWorker = A201 and Purpose != A44 and Housing = A151 and Job != A174 and Purpose != A42 and EmploymentSince = A72 | 2 | 0.046023 |
| CreditHistory != A31 and Purpose != A41 and Purpose != A44 and ForeignWorker = A201 and Property = A124 and Housing = A153 and EmploymentSince != A73 | 1 | 0.040816 |
| Property = A124 and Telephone = A192 | 2 | 0.057485 |
| CreditHistory != A31 and SavingsAccount != A64 and Purpose != A44 and Property != A124 and SavingsAccount = A63 | 2 | 0.032922 |
| CreditHistory != A31 and SavingsAccount != A64 and DurationMonth > 42.0 and EmploymentSince = A73 | 2 | 0.059524 |
| CreditHistory != A31 and SavingsAccount != A64 and ForeignWorker = A201 and StatusAccount != A11 and Guarantors = A101 and Job != A174 and NPeopleMain <= 1.0 and NCredits <= 1.0 and SavingsAccount = A62 | 1 | 0.042241 |
| CreditHistory != A31 and SavingsAccount = A62 and StatusAndSex != A93 | 2 | 0.073620 |
| CreditHistory != A31 and SavingsAccount != A64 and SavingsAccount != A62 and Purpose != A40 and Guarantors != A101 and ResidenceSince <= 2.0 | 1 | 0.021701 |
| CreditHistory != A31 and Guarantors = A102 | 1 | 0.025568 |
| CreditHistory != A31 and CreditHistory != A30 and SavingsAccount != A64 and SavingsAccount != A62 and StatusAccount != A11 and EmploymentSince = A74 and InstallmentRate > 2.0 | 1 | 0.024225 |
| CreditHistory != A31 and CreditHistory != A30 and SavingsAccount != A64 and SavingsAccount != A62 and NPeopleMain > 1.0 and CreditAmount > 1264.0 and ResidenceSince <= 2.0 | 2 | 0.022810 |
| CreditHistory != A31 and CreditHistory != A30 and Purpose = A46 and SavingsAccount = A61 | 2 | 0.043440 |
| CreditHistory = A31 | 2 | 0.024064 |
| Purpose = A46 | 1 | 0.045113 |
| SavingsAccount = A62 | 1 | 0.028153 |
| CreditHistory = A30 | 2 | 0.014453 |
| Purpose != A40 and CreditHistory != A33 and Property != A121 and Job = A172 and EmploymentSince = A73 | 1 | 0.054054 |
| Purpose != A40 and EmploymentSince = A75 and ResidenceSince > 3.0 and Property != A123 and Purpose = A42 | 1 | 0.055180 |
| StatusAndSex = A91 and EmploymentSince = A73 | 1 | 0.033069 |
| StatusAndSex != A91 and ResidenceSince <= 1.0 and Telephone != A192 and StatusAndSex = A92 | 1 | 0.060811 |
| StatusAndSex != A91 and StatusAndSex != A92 and StatusAccount != A13 and DurationMonth <= 9.0 | 1 | 0.073746 |
| StatusAndSex != A91 and CreditAmount <= 1042.0 and StatusAccount != A11 | 2 | 0.068817 |
| StatusAndSex != A91 and StatusAccount != A13 and Age <= 26.0 and InstallmentPlans = A143 and StatusAndSex != A93 and EmploymentSince = A73 and Age <= 24.0 | 2 | 0.075650 |
| StatusAndSex != A91 and StatusAccount = A13 | 1 | 0.034341 |
| StatusAndSex != A91 and Telephone != A192 and StatusAccount = A14 and StatusAndSex != A93 | 1 | 0.052688 |
| StatusAndSex != A91 and EmploymentSince = A75 and Property = A123 | 1 | 0.067368 |
| StatusAndSex != A91 and Property = A122 and EmploymentSince != A75 and Purpose = A42 | 1 | 0.080128 |
| StatusAndSex != A91 and NCredits > 1.0 and CreditAmount > 2080.0 | 2 | 0.221918 |
| StatusAndSex != A91 and Telephone = A192 and StatusAccount != A14 and Age <= 27.0 | 2 | 0.124615 |
| StatusAndSex != A91 and InstallmentRate <= 2.0 and Purpose = A40 and StatusAccount != A11 | 1 | 0.114286 |
| StatusAndSex != A91 and Housing = A151 and Property != A123 and Age <= 26.0 | 2 | 0.095238 |
| StatusAndSex != A91 and Telephone = A192 and Age > 34.0 | 1 | 0.070402 |
| StatusAndSex != A91 and Telephone = A192 | 2 | 0.152381 |
| StatusAndSex = A91 | 2 | 0.150278 |
| InstallmentPlans = A143 and Purpose = A43 and Property = A123 | 1 | 0.077160 |
| NCredits <= 1.0 and Housing = A152 and Property != A123 and ResidenceSince > 2.0 | 1 | 0.100000 |
| StatusAccount != A12 and Purpose != A40 and Property = A123 | 1 | 0.100000 |
| EmploymentSince != A73 and DurationMonth <= 21.0 | 2 | 0.347826 |
| StatusAndSex = A93 | 1 | 0.292271 |
|  | 1 | 0.387097 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| StatusAccount = A11 and DurationMonth >= 24 | 2 | 0.061200 |
| StatusAccount = A12 and DurationMonth >= 21 and SavingsAccount = A61 | 2 | 0.039722 |
| StatusAccount = A11 and InstallmentRate >= 4 and CreditAmount <= 1358 | 2 | 0.021563 |
|  | 1 | 0.817121 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

statusaccount|durationmonth|credithistory|age|customer
---|---|---|---|---
a11|(31.5-inf)|a31|(25.5-inf)|2
a12|(31.5-inf)|a31|(25.5-inf)|1
a14|(31.5-inf)|a31|(25.5-inf)|1
a12|(8.5-31.5]|a31|(25.5-inf)|2
a11|(8.5-31.5]|a31|(25.5-inf)|2
a14|(8.5-31.5]|a31|(25.5-inf)|1
a13|(8.5-31.5]|a31|(25.5-inf)|1
a13|(31.5-inf)|a30|(25.5-inf)|1
a14|(-inf-8.5]|a31|(25.5-inf)|1
a11|(-inf-8.5]|a31|(25.5-inf)|1
a12|(-inf-8.5]|a31|(25.5-inf)|1
a11|(31.5-inf)|a30|(25.5-inf)|1
a14|(31.5-inf)|a30|(25.5-inf)|1
a12|(31.5-inf)|a30|(25.5-inf)|2
a13|(8.5-31.5]|a30|(25.5-inf)|1
a14|(8.5-31.5]|a30|(25.5-inf)|1
a11|(8.5-31.5]|a30|(25.5-inf)|2
a12|(8.5-31.5]|a30|(25.5-inf)|2
a11|(31.5-inf)|a33|(25.5-inf)|2
a11|(8.5-31.5]|a31|(-inf-25.5]|1
a14|(31.5-inf)|a33|(25.5-inf)|1
a12|(8.5-31.5]|a31|(-inf-25.5]|1
a14|(-inf-8.5]|a30|(25.5-inf)|1
a12|(31.5-inf)|a33|(25.5-inf)|1
a11|(31.5-inf)|a30|(-inf-25.5]|1
a12|(31.5-inf)|a30|(-inf-25.5]|1
a13|(8.5-31.5]|a33|(25.5-inf)|2
a12|(-inf-8.5]|a31|(-inf-25.5]|1
a11|(8.5-31.5]|a33|(25.5-inf)|2
a14|(8.5-31.5]|a33|(25.5-inf)|1
a12|(8.5-31.5]|a33|(25.5-inf)|1
a12|(-inf-8.5]|a33|(25.5-inf)|1
a12|(8.5-31.5]|a30|(-inf-25.5]|1
a11|(31.5-inf)|a32|(25.5-inf)|2
a13|(31.5-inf)|a32|(25.5-inf)|2
a14|(31.5-inf)|a32|(25.5-inf)|1
a14|(-inf-8.5]|a33|(25.5-inf)|1
a13|(-inf-8.5]|a33|(25.5-inf)|1
a11|(8.5-31.5]|a30|(-inf-25.5]|2
a12|(31.5-inf)|a32|(25.5-inf)|2
a11|(31.5-inf)|a33|(-inf-25.5]|1
a14|(31.5-inf)|a33|(-inf-25.5]|1
a11|(8.5-31.5]|a32|(25.5-inf)|1
a13|(8.5-31.5]|a32|(25.5-inf)|1
a12|(8.5-31.5]|a32|(25.5-inf)|1
a14|(8.5-31.5]|a32|(25.5-inf)|1
a11|(8.5-31.5]|a33|(-inf-25.5]|1
a14|(8.5-31.5]|a33|(-inf-25.5]|1
a12|(8.5-31.5]|a33|(-inf-25.5]|1
a13|(-inf-8.5]|a32|(25.5-inf)|1
a13|(31.5-inf)|a34|(25.5-inf)|1
a12|(31.5-inf)|a34|(25.5-inf)|1
a11|(31.5-inf)|a34|(25.5-inf)|1
a14|(-inf-8.5]|a32|(25.5-inf)|1
a14|(31.5-inf)|a34|(25.5-inf)|1
a12|(-inf-8.5]|a32|(25.5-inf)|1
a11|(-inf-8.5]|a32|(25.5-inf)|1
a14|(-inf-8.5]|a33|(-inf-25.5]|1
a11|(31.5-inf)|a32|(-inf-25.5]|2
a14|(31.5-inf)|a32|(-inf-25.5]|1
a12|(31.5-inf)|a32|(-inf-25.5]|2
a13|(8.5-31.5]|a34|(25.5-inf)|1
a13|(31.5-inf)|a32|(-inf-25.5]|1
a12|(8.5-31.5]|a34|(25.5-inf)|1
a11|(8.5-31.5]|a34|(25.5-inf)|1
a14|(8.5-31.5]|a34|(25.5-inf)|1
a12|(-inf-8.5]|a34|(25.5-inf)|1
a13|(-inf-8.5]|a34|(25.5-inf)|1
a14|(-inf-8.5]|a34|(25.5-inf)|1
a13|(8.5-31.5]|a32|(-inf-25.5]|1
a11|(8.5-31.5]|a32|(-inf-25.5]|2
a14|(8.5-31.5]|a32|(-inf-25.5]|1
a12|(8.5-31.5]|a32|(-inf-25.5]|1
a11|(-inf-8.5]|a34|(25.5-inf)|1
a11|(-inf-8.5]|a32|(-inf-25.5]|1
a14|(31.5-inf)|a34|(-inf-25.5]|2
a12|(31.5-inf)|a34|(-inf-25.5]|2
a11|(31.5-inf)|a34|(-inf-25.5]|2
a14|(-inf-8.5]|a32|(-inf-25.5]|1
a12|(-inf-8.5]|a32|(-inf-25.5]|2
a13|(8.5-31.5]|a34|(-inf-25.5]|1
a12|(8.5-31.5]|a34|(-inf-25.5]|1
a11|(8.5-31.5]|a34|(-inf-25.5]|1
a14|(8.5-31.5]|a34|(-inf-25.5]|1
a14|(-inf-8.5]|a34|(-inf-25.5]|1

## JRip

Decision list:

rules | predicted class
---|---
(StatusAccount = A11) and (DurationMonth >= 24)|2 (109.0/43.0)
(StatusAccount = A12) and (DurationMonth >= 21) and (SavingsAccount = A61)|2 (59.0/20.0)
(StatusAccount = A11) and (InstallmentRate >= 4) and (CreditAmount <= 1358)|2 (41.0/17.0)
|1 (691.0/141.0)


## PART

Decision list:

rules | predicted class
---|---
StatusAccount = A14 AND InstallmentPlans != A141 AND CreditHistory != A33 AND Purpose != A46 AND StatusAndSex != A92 AND Purpose != A49 AND Property != A121 AND SavingsAccount != A62 AND Purpose != A40 AND EmploymentSince != A74|1 (73.0)
CreditHistory != A30 AND StatusAccount = A14 AND InstallmentPlans != A141 AND Purpose != A41 AND CreditHistory != A33 AND NPeopleMain <= 1.0 AND Job != A174 AND EmploymentSince != A72 AND InstallmentPlans = A143 AND Telephone = A192|1 (41.0)
CreditHistory = A30 AND Housing != A152 AND StatusAccount = A12|2 (7.0)
StatusAccount = A14 AND ForeignWorker = A201 AND InstallmentPlans != A141 AND Purpose != A41 AND Property != A123 AND Purpose != A46 AND Purpose = A43|1 (33.0)
ForeignWorker != A201 AND StatusAndSex = A93|1 (20.0)
CreditHistory != A30 AND StatusAccount = A14 AND EmploymentSince = A74 AND SavingsAccount != A61|1 (19.0)
CreditHistory != A30 AND CreditHistory != A31 AND CreditAmount <= 7721.0 AND Purpose != A410 AND DurationMonth <= 7.0 AND EmploymentSince != A72|1 (35.0)
CreditHistory = A30 AND Housing = A152 AND InstallmentRate <= 2.0 AND Telephone = A192|2 (8.0/3.0)
StatusAccount != A11 AND CreditAmount > 9857.0 AND DurationMonth <= 36.0|2 (11.0)
StatusAccount != A11 AND Job = A171 AND DurationMonth <= 14.0|1 (6.0/1.0)
StatusAccount != A11 AND Job != A171 AND Purpose = A41 AND StatusAndSex = A93|1 (25.0)
StatusAccount != A11 AND Job != A171 AND SavingsAccount = A65 AND Purpose != A46 AND InstallmentPlans != A141 AND EmploymentSince = A75|1 (15.0)
StatusAccount != A11 AND Job != A171 AND Purpose != A45 AND StatusAccount != A12 AND CreditHistory != A33 AND InstallmentPlans = A143 AND EmploymentSince = A75 AND InstallmentRate > 2.0|1 (14.0)
CreditHistory = A30 AND Housing = A152 AND CreditAmount <= 4169.0|2 (7.0/1.0)
StatusAccount != A11 AND Job != A171 AND Guarantors = A103 AND Job != A173|1 (11.0)
CreditHistory = A31 AND Property != A121 AND Property != A123 AND Job != A173|2 (10.0/3.0)
Purpose = A410|1 (8.0/1.0)
DurationMonth <= 30.0 AND Purpose = A41 AND NCredits > 1.0|1 (8.0)
DurationMonth <= 30.0 AND Purpose = A41 AND EmploymentSince != A73 AND InstallmentRate > 2.0|1 (7.0/3.0)
StatusAccount != A11 AND Guarantors != A102 AND Purpose != A45 AND SavingsAccount = A64 AND Property = A121|1 (8.0)
StatusAccount = A14 AND CreditHistory != A33 AND SavingsAccount != A63 AND Property = A124|1 (10.0/1.0)
Property = A124 AND InstallmentRate > 2.0 AND Housing != A151 AND SavingsAccount != A65 AND CreditHistory != A34 AND CreditHistory != A32|2 (10.0/1.0)
Property = A124 AND InstallmentRate > 2.0 AND Purpose != A40 AND EmploymentSince = A75|2 (10.0/1.0)
DurationMonth <= 30.0 AND Purpose != A41 AND Purpose != A40 AND Guarantors != A103 AND Purpose != A45 AND EmploymentSince = A74 AND Age > 23.0 AND Purpose != A42|1 (23.0)
Purpose = A41 AND CreditAmount <= 7297.0|1 (13.0)
Purpose != A41 AND Property = A124 AND Housing = A152 AND CreditAmount <= 6403.0|2 (7.0/2.0)
Purpose != A41 AND StatusAccount != A11 AND Guarantors != A102 AND CreditHistory != A31 AND StatusAndSex != A91 AND Purpose != A40 AND Job != A174 AND Purpose != A45 AND CreditHistory != A32 AND InstallmentRate > 1.0 AND EmploymentSince != A72 AND NCredits > 1.0 AND Property = A123|1 (13.0)
Purpose != A41 AND DurationMonth <= 15.0 AND Guarantors != A103 AND Purpose != A49 AND SavingsAccount != A62 AND Purpose != A46 AND CreditHistory != A33 AND NPeopleMain > 1.0 AND InstallmentRate <= 3.0|1 (14.0)
Purpose != A41 AND StatusAccount != A11 AND CreditHistory != A31 AND Guarantors != A102 AND NPeopleMain <= 1.0 AND DurationMonth <= 24.0 AND Housing != A153 AND Purpose != A46 AND StatusAccount = A13 AND Property != A121|1 (12.0)
Purpose != A41 AND StatusAccount = A14 AND CreditHistory != A33 AND Purpose != A46 AND SavingsAccount != A62 AND Housing != A151 AND Job != A172 AND EmploymentSince != A75 AND CreditAmount <= 3758.0 AND Property = A121|1 (11.0/1.0)
Purpose != A41 AND Purpose = A40 AND InstallmentPlans != A143 AND Telephone != A192|2 (13.0)
Purpose != A41 AND Guarantors = A103 AND EmploymentSince != A74 AND DurationMonth <= 15.0|1 (7.0)
Purpose != A41 AND CreditHistory = A34 AND Purpose != A49 AND StatusAndSex != A94 AND DurationMonth <= 24.0 AND EmploymentSince != A74 AND InstallmentPlans != A141 AND Purpose != A46 AND NCredits > 1.0 AND StatusAccount != A12 AND Purpose != A42|1 (10.0/5.0)
Purpose != A41 AND CreditHistory = A34 AND Purpose != A40 AND InstallmentPlans = A143 AND StatusAccount = A14|1 (11.0/2.0)
Purpose != A41 AND SavingsAccount != A61 AND CreditHistory != A32 AND SavingsAccount = A62|1 (10.0)
Purpose != A41 AND SavingsAccount = A65 AND CreditHistory != A32 AND StatusAccount = A12|1 (7.0)
Purpose != A41 AND CreditHistory = A33 AND InstallmentRate > 1.0 AND EmploymentSince != A73|2 (13.0)
Purpose != A41 AND SavingsAccount = A63 AND NCredits <= 1.0 AND DurationMonth > 13.0|1 (8.0)
Purpose != A41 AND CreditHistory = A31 AND ResidenceSince <= 3.0|2 (7.0/3.0)
CreditHistory != A31 AND Purpose != A41 AND ForeignWorker = A201 AND Purpose != A44 AND Housing = A151 AND Job != A174 AND Purpose != A42 AND EmploymentSince = A72|2 (10.0/1.0)
CreditHistory != A31 AND Purpose != A41 AND Purpose != A44 AND ForeignWorker = A201 AND Property = A124 AND Housing = A153 AND EmploymentSince != A73|1 (11.0/3.0)
Property = A124 AND Telephone = A192|2 (9.0)
CreditHistory != A31 AND SavingsAccount != A64 AND Purpose != A44 AND Property != A124 AND SavingsAccount = A63|2 (11.0/4.0)
CreditHistory != A31 AND SavingsAccount != A64 AND DurationMonth > 42.0 AND EmploymentSince = A73|2 (10.0)
CreditHistory != A31 AND SavingsAccount != A64 AND ForeignWorker = A201 AND StatusAccount != A11 AND Guarantors = A101 AND Job != A174 AND NPeopleMain <= 1.0 AND NCredits <= 1.0 AND SavingsAccount = A62|1 (8.0/1.0)
CreditHistory != A31 AND SavingsAccount = A62 AND StatusAndSex != A93|2 (10.0)
CreditHistory != A31 AND SavingsAccount != A64 AND SavingsAccount != A62 AND Purpose != A40 AND Guarantors != A101 AND ResidenceSince <= 2.0|1 (9.0/4.0)
CreditHistory != A31 AND Guarantors = A102|1 (8.0/2.0)
CreditHistory != A31 AND CreditHistory != A30 AND SavingsAccount != A64 AND SavingsAccount != A62 AND StatusAccount != A11 AND EmploymentSince = A74 AND InstallmentRate > 2.0|1 (8.0/3.0)
CreditHistory != A31 AND CreditHistory != A30 AND SavingsAccount != A64 AND SavingsAccount != A62 AND NPeopleMain > 1.0 AND CreditAmount > 1264.0 AND ResidenceSince <= 2.0|2 (8.0/3.0)
CreditHistory != A31 AND CreditHistory != A30 AND Purpose = A46 AND SavingsAccount = A61|2 (7.0)
CreditHistory = A31|2 (6.0/1.0)
Purpose = A46|1 (6.0/1.0)
SavingsAccount = A62|1 (6.0/1.0)
CreditHistory = A30|2 (6.0/2.0)
Purpose != A40 AND CreditHistory != A33 AND Property != A121 AND Job = A172 AND EmploymentSince = A73|1 (6.0)
Purpose != A40 AND EmploymentSince = A75 AND ResidenceSince > 3.0 AND Property != A123 AND Purpose = A42|1 (8.0/1.0)
StatusAndSex = A91 AND EmploymentSince = A73|1 (7.0/2.0)
StatusAndSex != A91 AND ResidenceSince <= 1.0 AND Telephone != A192 AND StatusAndSex = A92|1 (11.0/3.0)
StatusAndSex != A91 AND StatusAndSex != A92 AND StatusAccount != A13 AND DurationMonth <= 9.0|1 (11.0/1.0)
StatusAndSex != A91 AND CreditAmount <= 1042.0 AND StatusAccount != A11|2 (7.0)
StatusAndSex != A91 AND StatusAccount != A13 AND Age <= 26.0 AND InstallmentPlans = A143 AND StatusAndSex != A93 AND EmploymentSince = A73 AND Age <= 24.0|2 (9.0/1.0)
StatusAndSex != A91 AND StatusAccount = A13|1 (7.0/2.0)
StatusAndSex != A91 AND Telephone != A192 AND StatusAccount = A14 AND StatusAndSex != A93|1 (7.0/1.0)
StatusAndSex != A91 AND EmploymentSince = A75 AND Property = A123|1 (7.0)
StatusAndSex != A91 AND Property = A122 AND EmploymentSince != A75 AND Purpose = A42|1 (11.0/1.0)
StatusAndSex != A91 AND NCredits > 1.0 AND CreditAmount > 2080.0|2 (12.0)
StatusAndSex != A91 AND Telephone = A192 AND StatusAccount != A14 AND Age <= 27.0|2 (9.0)
StatusAndSex != A91 AND InstallmentRate <= 2.0 AND Purpose = A40 AND StatusAccount != A11|1 (8.0)
StatusAndSex != A91 AND Housing = A151 AND Property != A123 AND Age <= 26.0|2 (7.0/1.0)
StatusAndSex != A91 AND Telephone = A192 AND Age > 34.0|1 (9.0/4.0)
StatusAndSex != A91 AND Telephone = A192|2 (7.0/1.0)
StatusAndSex = A91|2 (6.0)
InstallmentPlans = A143 AND Purpose = A43 AND Property = A123|1 (6.0/2.0)
NCredits <= 1.0 AND Housing = A152 AND Property != A123 AND ResidenceSince > 2.0|1 (8.0/3.0)
StatusAccount != A12 AND Purpose != A40 AND Property = A123|1 (8.0/3.0)
EmploymentSince != A73 AND DurationMonth <= 21.0|2 (8.0/3.0)
StatusAndSex = A93|1 (7.0/1.0)
|1 (6.0/3.0)


## J48 Decision Tree

* StatusAccount = A14: 1 (266.0/36.0)
* StatusAccount != A14
	* CreditAmount <= 6681.0
		* ForeignWorker = A201
			* DurationMonth <= 30.0
				* CreditHistory = A30: 2 (14.0/5.0)
				* CreditHistory != A30
					* Purpose = A41: 1 (20.0/2.0)
					* Purpose != A41
						* Guarantors = A103: 1 (24.0/3.0)
						* Guarantors != A103
							* CreditAmount <= 1366.0
								* DurationMonth <= 16.0: 1 (67.0/27.0)
								* DurationMonth > 16.0: 2 (21.0/3.0)
							* CreditAmount > 1366.0
								* SavingsAccount = A63: 1 (8.0)
								* SavingsAccount != A63
									* StatusAndSex = A91: 2 (9.0/4.0)
									* StatusAndSex != A91: 1 (133.0/37.0)
			* DurationMonth > 30.0
				* Age <= 26.0: 2 (12.0/1.0)
				* Age > 26.0
					* CreditAmount <= 3149.0: 2 (10.0/2.0)
					* CreditAmount > 3149.0
						* Age <= 41.0: 1 (17.0/4.0)
						* Age > 41.0: 2 (8.0/2.0)
		* ForeignWorker != A201: 1 (16.0/1.0)
	* CreditAmount > 6681.0
		* SavingsAccount = A65: 1 (8.0/3.0)
		* SavingsAccount != A65: 2 (42.0/10.0)


## SimpleCart Decision Tree

	* StatusAccount=(A11)|(A12)
	* DurationMonth < 22.5
			* CreditHistory=(A31)|(A30): 2(19.0/7.0)
			* CreditHistory!=(A31)|(A30)
			* CreditAmount < 8724.5
				* DurationMonth < 8.5: 1(34.0/2.0)
				* DurationMonth >= 8.5
					* CreditAmount < 979.5
							* Property=(A124)|(A123): 2(12.0/0.0)
							* Property!=(A124)|(A123)
							* CreditAmount < 663.0: 1(7.0/0.0)
							* CreditAmount >= 663.0
											* EmploymentSince=(A71)|(A74)|(A75)|(A72)
											* StatusAccount=(A11)|(A14)|(A13): 2(8.0/0.0)
											* StatusAccount!=(A11)|(A14)|(A13): 1(3.0/1.0)
											* EmploymentSince!=(A71)|(A74)|(A75)|(A72): 1(6.0/2.0)
					* CreditAmount >= 979.5
									* EmploymentSince=(A72)|(A75)|(A73)|(A71)
								* Job=(A173)|(A174)
												* Purpose=(A44)|(A43)|(A46)|(A40)|(A48)
											* SavingsAccount=(A61)|(A62)|(A65)
										* NPeopleMain < 1.5
											* ResidenceSince < 3.5
												* CreditAmount < 1491.0: 2(11.0/1.0)
												* CreditAmount >= 1491.0
															* Property=(A124)|(A121)|(A122): 2(7.0/2.0)
															* Property!=(A124)|(A121)|(A122): 1(6.0/2.0)
											* ResidenceSince >= 3.5
												* Housing=(A151)
													* CreditAmount < 2615.5: 1(4.0/2.0)
													* CreditAmount >= 2615.5: 2(4.0/0.0)
												* Housing!=(A151): 1(9.0/1.0)
										* NPeopleMain >= 1.5: 1(4.0/0.0)
											* SavingsAccount!=(A61)|(A62)|(A65): 1(7.0/1.0)
												* Purpose!=(A44)|(A43)|(A46)|(A40)|(A48): 1(35.0/11.0)
								* Job!=(A173)|(A174)
								* DurationMonth < 17.0: 1(25.0/1.0)
								* DurationMonth >= 17.0: 1(6.0/4.0)
									* EmploymentSince!=(A72)|(A75)|(A73)|(A71): 1(25.0/1.0)
			* CreditAmount >= 8724.5: 2(4.0/0.0)
	* DurationMonth >= 22.5
				* SavingsAccount=(A61)|(A62)|(A63)
			* DurationMonth < 47.5
												* Purpose=(A40)|(A45)|(A43)|(A46)|(A42)|(A49)|(A410)|(A44)|(A48)
					* CreditAmount < 1368.5: 2(9.0/1.0)
					* CreditAmount >= 1368.5: 2(66.0/46.0)
												* Purpose!=(A40)|(A45)|(A43)|(A46)|(A42)|(A49)|(A410)|(A44)|(A48)
					* CreditAmount < 8097.5: 1(15.0/1.0)
					* CreditAmount >= 8097.5: 2(5.0/2.0)
			* DurationMonth >= 47.5: 2(30.0/4.0)
				* SavingsAccount!=(A61)|(A62)|(A63)
			* StatusAccount=(A11)
				* NCredits < 1.5
												* Purpose=(A43)|(A46)|(A40)|(A410)|(A49)|(A44)|(A45)|(A48): 2(6.0/0.0)
												* Purpose!=(A43)|(A46)|(A40)|(A410)|(A49)|(A44)|(A45)|(A48): 1(3.0/3.0)
				* NCredits >= 1.5: 1(4.0/0.0)
			* StatusAccount!=(A11): 1(20.0/2.0)
	* StatusAccount!=(A11)|(A12)
		* InstallmentPlans=(A141)|(A142)
				* Purpose=(A46)|(A40)|(A49)
			* DurationMonth < 15.0: 1(6.0/1.0)
			* DurationMonth >= 15.0: 2(13.0/8.0)
				* Purpose!=(A46)|(A40)|(A49): 1(33.0/6.0)
		* InstallmentPlans!=(A141)|(A142)
			* CreditHistory=(A31)|(A33)
			* InstallmentRate < 3.5: 1(15.0/1.0)
			* InstallmentRate >= 3.5
				* Age < 31.0: 2(5.0/0.0)
				* Age >= 31.0
					* EmploymentSince=(A75): 2(3.0/2.0)
					* EmploymentSince!=(A75): 1(6.0/0.0)
			* CreditHistory!=(A31)|(A33): 1(284.0/26.0)


