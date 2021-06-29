# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Gammagt > 20.5 | 2 | 0.440276 |
| Gammagt <= 20.5 | 1 | 0.199462 |
| Gammagt < 20.5 and Sgpt < 19.5 and Alkphos < 77.0 and Sgot >= 14.5 and Alkphos < 67.5 and Sgot < 23.0 | 2 | 0.139073 |
| Gammagt >= 20.5 and Drinks >= 5.5 and Sgpt >= 35.5 and Sgot < 42.5 | 1 | 0.074380 |
| Gammagt >= 20.5 and Drinks < 5.5 and Gammagt < 35.5 and Alkphos >= 65.5 and Sgpt >= 29.0 | 1 | 0.047103 |
| Gammagt < 20.5 and Sgpt >= 19.5 and Mcv < 87.5 and Sgpt < 26.5 and Sgot >= 21.5 | 2 | 0.045037 |
| Gammagt >= 20.5 and Drinks >= 5.5 and Sgpt < 35.5 and Sgot < 22.5 | 1 | 0.021390 |
| Gammagt < 20.5 and Sgpt < 19.5 and Alkphos < 77.0 and Sgot >= 14.5 and Alkphos >= 67.5 | 2 | 0.033582 |
| Gammagt < 20.5 and Sgpt >= 19.5 and Mcv >= 87.5 and Alkphos < 59.5 and Sgpt < 25.0 | 2 | 0.024060 |
| Gammagt >= 20.5 and Drinks >= 5.5 and Sgpt < 35.5 and Sgot >= 22.5 and Alkphos >= 92.5 | 1 | 0.008152 |
| Gammagt < 20.5 and Sgpt < 19.5 and Alkphos < 77.0 and Sgot >= 14.5 and Alkphos < 67.5 and Sgot >= 23.0 | 2 | 0.024060 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Gammagt > 20 and Drinks <= 5 and Drinks > 3 and Drinks <= 4 and Mcv <= 90 | 2 | 0.103448 |
| Gammagt > 35 and Drinks <= 5 and Drinks > 2 | 2 | 0.127517 |
| Sgpt <= 21 and Alkphos <= 61 and Gammagt <= 14 | 2 | 0.103448 |
| Gammagt <= 20 and Sgpt > 24 | 1 | 0.180738 |
| Mcv > 87 and Sgot > 14 and Gammagt > 12 | 2 | 0.421970 |
| Mcv > 87 and Drinks <= 1 | 1 | 0.382003 |
| Mcv <= 87 | 2 | 0.343936 |
|  | 1 | 0.942857 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Gammagt <= 20 and Sgpt >= 20 | 1 | 0.184091 |
| Drinks >= 6 and Sgpt >= 37 | 1 | 0.068729 |
| Alkphos >= 66 and Gammagt <= 35 and Sgpt >= 30 | 1 | 0.053019 |
| Sgot <= 14 | 1 | 0.025755 |
|  | 2 | 0.840183 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

gammagt|selector
---|---
(20.5-inf)|2
(-inf-20.5]|1

## JRip

Decision list:

rules | predicted class
---|---
(Gammagt <= 20) and (Sgpt >= 20)|1 (72.0/18.0)
(Drinks >= 6) and (Sgpt >= 37)|1 (30.0/10.0)
(Alkphos >= 66) and (Gammagt <= 35) and (Sgpt >= 30)|1 (13.0/1.0)
(Sgot <= 14)|1 (15.0/6.0)
|2 (184.0/35.0)


## PART

Decision list:

rules | predicted class
---|---
Gammagt > 20 AND Drinks <= 5 AND Drinks > 3 AND Drinks <= 4 AND Mcv <= 90|2 (15.0)
Gammagt > 35 AND Drinks <= 5 AND Drinks > 2|2 (19.0)
Sgpt <= 21 AND Alkphos <= 61 AND Gammagt <= 14|2 (15.0)
Gammagt <= 20 AND Sgpt > 24|1 (39.0/5.0)
Mcv > 87 AND Sgot > 14 AND Gammagt > 12|2 (146.0/60.0)
Mcv > 87 AND Drinks <= 1|1 (17.0/1.0)
Mcv <= 87|2 (53.0/13.0)
|1 (10.0/3.0)


## SimpleCart Decision Tree

* Gammagt < 20.5
	* Sgpt < 19.5
		* Alkphos < 77.0
			* Sgot < 14.5: 1(4.0/2.0)
			* Sgot >= 14.5
				* Alkphos < 67.5
					* Sgot < 23.0: 2(21.0/0.0)
					* Sgot >= 23.0: 2(4.0/1.0)
				* Alkphos >= 67.5: 2(6.0/2.0)
		* Alkphos >= 77.0: 1(10.0/5.0)
	* Sgpt >= 19.5
		* Mcv < 87.5
			* Sgpt < 26.5
				* Sgot < 21.5: 1(4.0/3.0)
				* Sgot >= 21.5: 2(7.0/1.0)
			* Sgpt >= 26.5: 1(6.0/0.0)
		* Mcv >= 87.5
			* Alkphos < 59.5
				* Sgpt < 25.0: 2(4.0/1.0)
				* Sgpt >= 25.0: 1(7.0/1.0)
			* Alkphos >= 59.5: 1(35.0/3.0)
* Gammagt >= 20.5
	* Drinks < 5.5
		* Gammagt < 35.5
			* Alkphos < 65.5
				* Gammagt < 30.5: 2(22.0/1.0)
				* Gammagt >= 30.5: 2(4.0/3.0)
			* Alkphos >= 65.5
				* Sgpt < 29.0: 2(14.0/7.0)
				* Sgpt >= 29.0: 1(10.0/1.0)
		* Gammagt >= 35.5
			* Drinks < 2.5: 2(27.0/7.0)
			* Drinks >= 2.5: 2(26.0/0.0)
	* Drinks >= 5.5
		* Sgpt < 35.5
			* Sgot < 22.5: 1(6.0/3.0)
			* Sgot >= 22.5
				* Alkphos < 92.5: 2(17.0/1.0)
				* Alkphos >= 92.5: 1(3.0/3.0)
		* Sgpt >= 35.5
			* Sgot < 42.5: 1(18.0/4.0)
			* Sgot >= 42.5: 2(7.0/3.0)


