# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Mcv = all | 2 | 0.580645 |
| Gammagt <= 20.5 and Sgpt > 24.5 | 1 | 0.141823 |
| Gammagt >= 20.5 and Drinks >= 5.5 and Sgpt < 36.5 and Sgot < 22.5 | 1 | 0.024342 |
| Gammagt <= 20.5 and Sgpt <= 24.5 and Mcv > 87.5 and Alkphos > 64.5 and Sgot > 14.5 and Mcv <= 91.5 and Sgpt > 15.5 | 1 | 0.028986 |
| Gammagt > 20.5 and Drinks <= 5.5 and Drinks <= 3.5 and Alkphos > 65.5 and Sgot <= 24.5 and Alkphos <= 71.5 | 1 | 0.047619 |
| Gammagt > 20.5 and Drinks > 5.5 and Sgpt > 36.5 and Sgot <= 32.5 | 1 | 0.052632 |
| Gammagt <= 20.5 and Sgpt <= 24.5 and Mcv > 87.5 and Alkphos > 64.5 and Sgot <= 14.5 | 1 | 0.032258 |
| Gammagt <= 20.5 and Sgpt <= 24.5 and Mcv > 87.5 and Alkphos > 64.5 and Sgot > 14.5 and Mcv > 91.5 | 1 | 0.034409 |
| Gammagt < 20.5 and Sgpt < 24.5 and Alkphos >= 64.5 and Mcv >= 87.5 | 1 | 0.081036 |
| Gammagt > 20.5 and Drinks > 5.5 and Sgpt > 36.5 and Sgot > 32.5 and Mcv > 93.5 | 1 | 0.029429 |
| Gammagt <= 20.5 and Sgpt <= 24.5 and Mcv <= 87.5 and Drinks <= 3.5 and Alkphos <= 63.5 | 1 | 0.008333 |
| Gammagt >= 20.5 and Drinks >= 5.5 and Sgpt >= 36.5 and Sgot < 42.5 | 1 | 0.079121 |
| Gammagt > 20.5 and Drinks <= 5.5 and Drinks <= 3.5 and Alkphos > 65.5 and Sgot <= 24.5 and Alkphos > 71.5 | 1 | 0.030525 |
| Gammagt <= 20.5 and Sgpt <= 24.5 and Mcv > 87.5 and Alkphos <= 64.5 and Sgpt > 19.5 | 1 | 0.018081 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Gammagt > 20.0 and Drinks <= 5.0 and Drinks <= 3.0 and Alkphos <= 65.0 | 2 | 0.186422 |
| Drinks > 3.0 and Drinks <= 5.0 and Mcv > 87.0 and Gammagt > 18.0 | 2 | 0.172796 |
| Mcv <= 87.0 and Drinks > 3.0 and Sgpt <= 31.0 | 2 | 0.139073 |
| Sgot <= 21.0 and Sgpt > 19.0 and Gammagt <= 51.0 and Mcv > 85.0 and Mcv <= 93.0 | 1 | 0.333333 |
| Sgpt <= 26.0 and Alkphos <= 59.0 and Alkphos > 53.0 | 2 | 0.154639 |
| Mcv <= 90.0 | 2 | 0.261527 |
| Sgpt > 14.0 and Sgot <= 45.0 and Sgpt <= 53.0 and Sgot > 22.0 | 2 | 0.145620 |
| Sgot <= 45.0 | 1 | 0.847237 |
|  | 2 | 0.933333 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Gammagt <= 21 and Sgpt >= 22 | 1 | 0.173651 |
| Alkphos >= 66 and Sgot <= 22 and Drinks <= 0.5 | 1 | 0.054400 |
| Drinks >= 6 and Sgpt >= 37 and Sgot <= 34 | 1 | 0.057994 |
| Alkphos >= 66 and Mcv >= 90 and Gammagt <= 35 and Mcv <= 93 | 1 | 0.049911 |
|  | 2 | 0.814480 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

mcv|selector
---|---
all|2

## JRip

Decision list:

rules | predicted class
---|---
(Gammagt <= 21) and (Sgpt >= 22)|1 (62.0/14.0)
(Alkphos >= 66) and (Sgot <= 22) and (Drinks <= 0.5)|1 (21.0/6.0)
(Drinks >= 6) and (Sgpt >= 37) and (Sgot <= 34)|1 (13.0/1.0)
(Alkphos >= 66) and (Mcv >= 90) and (Gammagt <= 35) and (Mcv <= 93)|1 (17.0/3.0)
|2 (197.0/41.0)


## PART

Decision list:

rules | predicted class
---|---
Gammagt > 20.0 AND Drinks <= 5.0 AND Drinks <= 3.0 AND Alkphos <= 65.0|2 (39.0/5.0)
Drinks > 3.0 AND Drinks <= 5.0 AND Mcv > 87.0 AND Gammagt > 18.0|2 (31.0/2.0)
Mcv <= 87.0 AND Drinks > 3.0 AND Sgpt <= 31.0|2 (21.0)
Sgot <= 21.0 AND Sgpt > 19.0 AND Gammagt <= 51.0 AND Mcv > 85.0 AND Mcv <= 93.0|1 (46.0)
Sgpt <= 26.0 AND Alkphos <= 59.0 AND Alkphos > 53.0|2 (15.0)
Mcv <= 90.0|2 (68.0/26.0)
Sgpt > 14.0 AND Sgot <= 45.0 AND Sgpt <= 53.0 AND Sgot > 22.0|2 (40.0/15.0)
Sgot <= 45.0|1 (42.0/7.0)
|2 (8.0/1.0)


## J48 Decision Tree

* Gammagt <= 20.5
	* Sgpt <= 24.5
		* Mcv <= 87.5
			* Drinks <= 3.5
				* Alkphos <= 63.5: 1 (6.0/3.0)
				* Alkphos > 63.5: 2 (6.0/1.0)
			* Drinks > 3.5: 2 (10.0)
		* Mcv > 87.5
			* Alkphos <= 64.5
				* Sgpt <= 19.5
					* Alkphos <= 53.5: 2 (6.0/2.0)
					* Alkphos > 53.5: 2 (13.0)
				* Sgpt > 19.5: 1 (11.0/5.0)
			* Alkphos > 64.5
				* Sgot <= 14.5: 1 (6.0)
				* Sgot > 14.5
					* Mcv <= 91.5
						* Sgpt <= 15.5: 2 (6.0/1.0)
						* Sgpt > 15.5: 1 (12.0/4.0)
					* Mcv > 91.5: 1 (10.0/2.0)
	* Sgpt > 24.5: 1 (39.0/5.0)
* Gammagt > 20.5
	* Drinks <= 5.5
		* Drinks <= 3.5
			* Alkphos <= 65.5
				* Drinks <= 0.75: 2 (18.0)
				* Drinks > 0.75
					* Drinks <= 2.5
						* Sgpt <= 31: 2 (6.0/2.0)
						* Sgpt > 31: 2 (7.0/2.0)
					* Drinks > 2.5: 2 (8.0/1.0)
			* Alkphos > 65.5
				* Sgot <= 24.5
					* Alkphos <= 71.5: 1 (9.0)
					* Alkphos > 71.5: 1 (18.0/8.0)
				* Sgot > 24.5
					* Sgpt <= 39: 2 (11.0)
					* Sgpt > 39: 2 (8.0/3.0)
		* Drinks > 3.5
			* Drinks <= 4.5: 2 (26.0/1.0)
			* Drinks > 4.5: 2 (11.0/1.0)
	* Drinks > 5.5
		* Sgpt <= 36.5
			* Sgot <= 22.5: 1 (11.0/4.0)
			* Sgot > 22.5
				* Alkphos <= 74.5: 2 (11.0)
				* Alkphos > 74.5: 2 (11.0/4.0)
		* Sgpt > 36.5
			* Sgot <= 32.5: 1 (10.0)
			* Sgot > 32.5
				* Mcv <= 93.5: 2 (11.0/4.0)
				* Mcv > 93.5: 1 (9.0/2.0)


## SimpleCart Decision Tree

* Gammagt < 20.5
	* Sgpt < 24.5
		* Alkphos < 64.5: 2(32.0/11.0)
		* Alkphos >= 64.5
			* Mcv < 87.5: 2(8.0/1.0)
			* Mcv >= 87.5: 1(23.0/11.0)
	* Sgpt >= 24.5: 1(34.0/5.0)
* Gammagt >= 20.5
	* Drinks < 5.5
		* Alkphos < 65.5: 2(51.0/5.0)
		* Alkphos >= 65.5
			* Sgot < 24.5
				* Drinks < 3.5: 1(19.0/8.0)
				* Drinks >= 3.5: 2(8.0/2.0)
			* Sgot >= 24.5: 2(26.0/3.0)
	* Drinks >= 5.5
		* Sgpt < 36.5
			* Sgot < 22.5: 1(7.0/4.0)
			* Sgot >= 22.5: 2(18.0/4.0)
		* Sgpt >= 36.5
			* Sgot < 42.5: 1(18.0/3.0)
			* Sgot >= 42.5: 2(6.0/3.0)


