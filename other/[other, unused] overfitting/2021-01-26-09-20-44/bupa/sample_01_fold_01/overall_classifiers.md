# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Sgpt <= 21.5 | 2 | 0.306122 |
| Sgpt > 21.5 and Gammagt > 28.5 | 2 | 0.305068 |
| Sgpt > 21.5 and Gammagt <= 28.5 and Sgot <= 22 | 1 | 0.176072 |
| Gammagt >= 20.5 and Drinks >= 5.5 and Sgpt >= 36.5 and Sgot < 42.5 | 1 | 0.079121 |
| Gammagt < 20.5 and Sgpt >= 24.5 | 1 | 0.141823 |
| Sgpt > 21.5 and Gammagt <= 28.5 and Sgot > 22 | 2 | 0.081284 |
| Gammagt >= 20.5 and Drinks < 5.5 and Alkphos >= 65.5 and Sgot < 24.5 and Drinks < 3.5 and Alkphos >= 71.5 | 1 | 0.030525 |
| Gammagt < 20.5 and Sgpt < 24.5 and Alkphos >= 64.5 and Mcv >= 87.5 and Sgot >= 14.5 and Sgpt < 19.5 and Alkphos >= 77.0 | 1 | 0.026630 |
| Gammagt < 20.5 and Sgpt < 24.5 and Alkphos >= 64.5 and Mcv >= 87.5 and Sgot < 14.5 | 1 | 0.032258 |
| Gammagt >= 20.5 and Drinks < 5.5 and Alkphos >= 65.5 and Sgot < 24.5 and Drinks < 3.5 and Alkphos < 71.5 | 1 | 0.047619 |
| Gammagt < 20.5 and Sgpt < 24.5 and Alkphos >= 64.5 and Mcv >= 87.5 and Sgot >= 14.5 and Sgpt >= 19.5 | 1 | 0.039378 |
| Gammagt >= 20.5 and Drinks >= 5.5 and Sgpt < 36.5 and Sgot < 22.5 | 1 | 0.024342 |
| Gammagt >= 20.5 and Drinks < 5.5 and Alkphos < 65.5 | 2 | 0.263900 |
| Gammagt < 20.5 and Sgpt < 24.5 and Alkphos < 64.5 | 2 | 0.157708 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Gammagt > 20 and Drinks <= 5 and Alkphos <= 65 and Gammagt > 26 and Gammagt > 35 | 2 | 0.145011 |
| Sgpt <= 21 and Gammagt > 11 and Alkphos <= 77 and Gammagt > 13 and Alkphos <= 71 and Gammagt <= 31 and Gammagt > 16 | 2 | 0.121959 |
| Sgot > 22 and Sgot <= 45 and Sgpt <= 68 and Gammagt > 21 and Sgpt <= 38 and Mcv <= 97 | 2 | 0.210782 |
| Sgot > 42 and Mcv <= 96 | 2 | 0.071429 |
| Sgpt > 19 and Mcv > 87 and Sgot > 15 and Sgpt <= 56 and Sgot <= 32 and Sgot <= 25 and Gammagt <= 26 and Sgot <= 21 | 1 | 0.199584 |
| Sgpt > 26 and Gammagt > 15 and Sgot > 17 and Drinks > 5 and Mcv <= 99 and Gammagt <= 66 | 1 | 0.152381 |
| Sgpt <= 19 and Gammagt > 7 and Alkphos <= 77 and Drinks <= 5 | 2 | 0.208107 |
| Sgot <= 17 and Mcv > 90 | 1 | 0.195569 |
| Mcv > 88 and Sgot > 25 and Sgot <= 64 and Alkphos <= 96 | 1 | 0.262401 |
| Drinks > 3 and Mcv <= 89 | 2 | 0.238806 |
| Sgpt <= 46 and Gammagt > 44 and Alkphos <= 102 | 2 | 0.160000 |
| Gammagt > 9 and Sgpt <= 46 and Gammagt <= 37 and Mcv > 83 and Sgpt > 27 | 1 | 0.285573 |
| Gammagt > 9 and Mcv > 83 and Mcv <= 85 | 2 | 0.192857 |
| Gammagt > 9 and Mcv <= 91 and Sgot <= 24 and Sgpt > 18 and Sgot <= 21 | 1 | 0.358974 |
| Gammagt > 9 and Mcv > 87 and Alkphos > 59 and Sgot > 16 and Gammagt <= 76 and Gammagt <= 39 | 2 | 0.234783 |
| Gammagt > 9 and Gammagt <= 39 | 2 | 0.319471 |
| Sgot <= 28 | 1 | 0.857143 |
|  | 2 | 0.600000 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Gammagt <= 20 and Sgpt >= 25 and Mcv >= 89 and Sgot <= 32 | 1 | 0.104478 |
| Alkphos >= 66 and Sgpt >= 22 and Gammagt <= 29 and Sgot <= 21 | 1 | 0.095477 |
| Drinks >= 6 and Sgpt >= 37 and Sgot <= 42 and Gammagt <= 89 | 1 | 0.067358 |
| Alkphos >= 66 and Gammagt <= 20 and Mcv >= 91 | 1 | 0.038402 |
| Gammagt <= 12 and Sgpt >= 17 and Sgot <= 21 and Drinks <= 4 | 1 | 0.057592 |
|  | 2 | 0.762712 |


# Text representation of classifiers as-is

## JRip

Decision list:

rules | predicted class
---|---
(Gammagt <= 20) and (Sgpt >= 25) and (Mcv >= 89) and (Sgot <= 32)|1 (21.0/0.0)
(Alkphos >= 66) and (Sgpt >= 22) and (Gammagt <= 29) and (Sgot <= 21)|1 (19.0/0.0)
(Drinks >= 6) and (Sgpt >= 37) and (Sgot <= 42) and (Gammagt <= 89)|1 (13.0/0.0)
(Alkphos >= 66) and (Gammagt <= 20) and (Mcv >= 91)|1 (14.0/4.0)
(Gammagt <= 12) and (Sgpt >= 17) and (Sgot <= 21) and (Drinks <= 4)|1 (11.0/0.0)
|2 (232.0/56.0)


## PART

Decision list:

rules | predicted class
---|---
Gammagt > 20 AND Drinks <= 5 AND Alkphos <= 65 AND Gammagt > 26 AND Gammagt > 35|2 (24.0/1.0)
Sgpt <= 21 AND Gammagt > 11 AND Alkphos <= 77 AND Gammagt > 13 AND Alkphos <= 71 AND Gammagt <= 31 AND Gammagt > 16|2 (20.0/1.0)
Sgot > 22 AND Sgot <= 45 AND Sgpt <= 68 AND Gammagt > 21 AND Sgpt <= 38 AND Mcv <= 97|2 (43.0/4.0)
Sgot > 42 AND Mcv <= 96|2 (10.0)
Sgpt > 19 AND Mcv > 87 AND Sgot > 15 AND Sgpt <= 56 AND Sgot <= 32 AND Sgot <= 25 AND Gammagt <= 26 AND Sgot <= 21|1 (26.0/2.0)
Sgpt > 26 AND Gammagt > 15 AND Sgot > 17 AND Drinks > 5 AND Mcv <= 99 AND Gammagt <= 66|1 (16.0)
Sgpt <= 19 AND Gammagt > 7 AND Alkphos <= 77 AND Drinks <= 5|2 (30.0/3.0)
Sgot <= 17 AND Mcv > 90|1 (16.0)
Mcv > 88 AND Sgot > 25 AND Sgot <= 64 AND Alkphos <= 96|1 (22.0/1.0)
Drinks > 3 AND Mcv <= 89|2 (16.0)
Sgpt <= 46 AND Gammagt > 44 AND Alkphos <= 102|2 (13.0/2.0)
Gammagt > 9 AND Sgpt <= 46 AND Gammagt <= 37 AND Mcv > 83 AND Sgpt > 27|1 (21.0/5.0)
Gammagt > 9 AND Mcv > 83 AND Mcv <= 85|2 (9.0/1.0)
Gammagt > 9 AND Mcv <= 91 AND Sgot <= 24 AND Sgpt > 18 AND Sgot <= 21|1 (13.0)
Gammagt > 9 AND Mcv > 87 AND Alkphos > 59 AND Sgot > 16 AND Gammagt <= 76 AND Gammagt <= 39|2 (12.0/5.0)
Gammagt > 9 AND Gammagt <= 39|2 (9.0)
Sgot <= 28|1 (7.0)
|2 (3.0)


## J48 Decision Tree

* Sgpt <= 21.5: 2 (56.0/12.0)
* Sgpt > 21.5
	* Gammagt <= 28.5
		* Sgot <= 22: 1 (24.0)
		* Sgot > 22: 2 (17.0/8.0)
	* Gammagt > 28.5: 2 (58.0/21.0)


## SimpleCart Decision Tree

* Gammagt < 20.5
	* Sgpt < 24.5
		* Alkphos < 64.5: 2(32.0/11.0)
		* Alkphos >= 64.5
			* Mcv < 87.5: 2(8.0/1.0)
			* Mcv >= 87.5
				* Sgot < 14.5: 1(6.0/0.0)
				* Sgot >= 14.5
					* Sgpt < 19.5
						* Alkphos < 77.0: 2(6.0/1.0)
						* Alkphos >= 77.0: 1(7.0/3.0)
					* Sgpt >= 19.5: 1(9.0/2.0)
	* Sgpt >= 24.5: 1(34.0/5.0)
* Gammagt >= 20.5
	* Drinks < 5.5
		* Alkphos < 65.5: 2(51.0/5.0)
		* Alkphos >= 65.5
			* Sgot < 24.5
				* Drinks < 3.5
					* Alkphos < 71.5: 1(9.0/0.0)
					* Alkphos >= 71.5: 1(10.0/8.0)
				* Drinks >= 3.5: 2(8.0/2.0)
			* Sgot >= 24.5: 2(26.0/3.0)
	* Drinks >= 5.5
		* Sgpt < 36.5
			* Sgot < 22.5: 1(7.0/4.0)
			* Sgot >= 22.5: 2(18.0/4.0)
		* Sgpt >= 36.5
			* Sgot < 42.5: 1(18.0/3.0)
			* Sgot >= 42.5: 2(6.0/3.0)


