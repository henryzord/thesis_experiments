# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| ChestPainType < 3.5 and Thal < 4.5 | 1 | 0.419936 |
| ChestPainType >= 3.5 and MajorVessels >= 0.5 | 2 | 0.293543 |
| ChestPainType >= 3.5 and MajorVessels < 0.5 and Thal < 6.5 | 1 | 0.148645 |
| ChestPainType >= 3.5 and MajorVessels < 0.5 and Thal >= 6.5 | 2 | 0.100951 |
| ChestPainType < 3.5 and Thal >= 4.5 and MajorVessels < 0.5 | 1 | 0.109470 |
| ChestPainType < 3.5 and Thal >= 4.5 and MajorVessels >= 0.5 | 2 | 0.064637 |
| ChestPainType <= 3.0 and Thal > 3.0 and MajorVessels <= 0.0 and FastingBloodSugar <= 0.0 and ResElectrocardiographic <= 1.0 and Slope > 1.0 | 2 | 0.016423 |
| Age > 54.5 and ChestPainType > 3.5 and MajorVessels <= 0.5 and Thal > 4.5 | 1 | 0.030025 |
| Age <= 54.5 and ChestPainType > 3.5 and MajorVessels <= 0.5 and Thal > 4.5 | 2 | 0.089428 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| ChestPainType <= 3 and Thal <= 3 and Sex <= 0 and MajorVessels <= 0 | 1 | 0.223022 |
| ChestPainType <= 3 and Slope <= 1 and Thal <= 3 and MaxHeartRate > 158 | 1 | 0.205882 |
| MajorVessels > 0 and ChestPainType > 3 and Slope > 1 | 2 | 0.361345 |
| Thal <= 6 and MajorVessels <= 0 and SerumCholestoral <= 271 and ResElectrocardiographic > 1 and ChestPainType > 3 | 1 | 0.155844 |
| ChestPainType > 3 and ResElectrocardiographic > 0 and ExerciseInduced > 0 | 2 | 0.169697 |
| MajorVessels <= 0 and FastingBloodSugar <= 0 and ExerciseInduced <= 0 and ResElectrocardiographic <= 1 and SerumCholestoral > 215 | 1 | 0.091629 |
| MajorVessels <= 0 and FastingBloodSugar <= 0 and ExerciseInduced <= 0 and ResElectrocardiographic > 1 and RestBloodPressure <= 134 | 1 | 0.082492 |
| MajorVessels <= 0 and FastingBloodSugar <= 0 and Slope <= 1 | 1 | 0.160714 |
| FastingBloodSugar > 0 | 1 | 0.178506 |
| Thal > 6 and ChestPainType <= 3 | 2 | 0.375479 |
| Thal <= 6 and ChestPainType <= 3 | 1 | 0.135135 |
| Thal <= 6 | 2 | 0.666667 |
|  | 2 | 0.653846 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| ChestPainType >= 4 and MajorVessels >= 1 | 2 | 0.293543 |
| Thal >= 7 and ChestPainType >= 4 | 2 | 0.097568 |
| Thal >= 6 and MajorVessels >= 1 | 2 | 0.060440 |
| SerumCholestoral >= 229 and MaxHeartRate <= 147 and ResElectrocardiographic <= 1 | 2 | 0.038369 |
|  | 1 | 0.918367 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

age|chestpaintype|majorvessels|thal|class
---|---|---|---|---
(-inf-54.5]|(3.5-inf)|(0.5-inf)|(4.5-inf)|2
(54.5-inf)|(3.5-inf)|(0.5-inf)|(4.5-inf)|2
(-inf-54.5]|(-inf-3.5]|(0.5-inf)|(4.5-inf)|2
(54.5-inf)|(-inf-3.5]|(0.5-inf)|(4.5-inf)|2
(-inf-54.5]|(3.5-inf)|(-inf-0.5]|(4.5-inf)|2
(54.5-inf)|(3.5-inf)|(-inf-0.5]|(4.5-inf)|1
(-inf-54.5]|(3.5-inf)|(0.5-inf)|(-inf-4.5]|2
(-inf-54.5]|(-inf-3.5]|(-inf-0.5]|(4.5-inf)|1
(54.5-inf)|(-inf-3.5]|(-inf-0.5]|(4.5-inf)|1
(54.5-inf)|(3.5-inf)|(0.5-inf)|(-inf-4.5]|2
(-inf-54.5]|(-inf-3.5]|(0.5-inf)|(-inf-4.5]|1
(54.5-inf)|(-inf-3.5]|(0.5-inf)|(-inf-4.5]|1
(-inf-54.5]|(3.5-inf)|(-inf-0.5]|(-inf-4.5]|1
(54.5-inf)|(3.5-inf)|(-inf-0.5]|(-inf-4.5]|1
(-inf-54.5]|(-inf-3.5]|(-inf-0.5]|(-inf-4.5]|1
(54.5-inf)|(-inf-3.5]|(-inf-0.5]|(-inf-4.5]|1

## JRip

Decision list:

rules | predicted class
---|---
(ChestPainType >= 4) and (MajorVessels >= 1)|2 (60.0/2.0)
(Thal >= 7) and (ChestPainType >= 4)|2 (24.0/5.0)
(Thal >= 6) and (MajorVessels >= 1)|2 (13.0/2.0)
(SerumCholestoral >= 229) and (MaxHeartRate <= 147) and (ResElectrocardiographic <= 1)|2 (10.0/2.0)
|1 (136.0/12.0)


## PART

Decision list:

rules | predicted class
---|---
ChestPainType <= 3 AND Thal <= 3 AND Sex <= 0 AND MajorVessels <= 0|1 (31.0)
ChestPainType <= 3 AND Slope <= 1 AND Thal <= 3 AND MaxHeartRate > 158|1 (28.0)
MajorVessels > 0 AND ChestPainType > 3 AND Slope > 1|2 (43.0)
Thal <= 6 AND MajorVessels <= 0 AND SerumCholestoral <= 271 AND ResElectrocardiographic > 1 AND ChestPainType > 3|1 (12.0)
ChestPainType > 3 AND ResElectrocardiographic > 0 AND ExerciseInduced > 0|2 (15.0/1.0)
MajorVessels <= 0 AND FastingBloodSugar <= 0 AND ExerciseInduced <= 0 AND ResElectrocardiographic <= 1 AND SerumCholestoral > 215|1 (17.0/8.0)
MajorVessels <= 0 AND FastingBloodSugar <= 0 AND ExerciseInduced <= 0 AND ResElectrocardiographic > 1 AND RestBloodPressure <= 134|1 (11.0/4.0)
MajorVessels <= 0 AND FastingBloodSugar <= 0 AND Slope <= 1|1 (17.0/3.0)
FastingBloodSugar > 0|1 (18.0/4.0)
Thal > 6 AND ChestPainType <= 3|2 (16.0/4.0)
Thal <= 6 AND ChestPainType <= 3|1 (13.0/3.0)
Thal <= 6|2 (12.0/5.0)
|2 (10.0)


## J48 Decision Tree

* ChestPainType <= 3.0
	* Thal <= 3.0: 1 (85.0/8.0)
	* Thal > 3.0
		* MajorVessels <= 0.0
			* FastingBloodSugar <= 0.0
				* ResElectrocardiographic <= 1.0
					* Slope <= 1.0: 1 (5.0/1.0)
					* Slope > 1.0: 2 (3.0/1.0)
				* ResElectrocardiographic > 1.0: 1 (6.0/1.0)
			* FastingBloodSugar > 0.0: 1 (3.0)
		* MajorVessels > 0.0: 2 (11.0/2.0)
* ChestPainType > 3.0
	* MajorVessels <= 0.0
		* Thal <= 6.0: 1 (28.0/6.0)
		* Thal > 6.0: 2 (23.0/5.0)
	* MajorVessels > 0.0: 2 (55.0/2.0)


## SimpleCart Decision Tree

* ChestPainType < 3.5
	* Thal < 4.5: 1(85.0/8.0)
	* Thal >= 4.5
		* MajorVessels < 0.5: 1(17.0/5.0)
		* MajorVessels >= 0.5: 2(11.0/2.0)
* ChestPainType >= 3.5
	* MajorVessels < 0.5
		* Thal < 6.5: 1(24.0/7.0)
		* Thal >= 6.5: 2(19.0/5.0)
	* MajorVessels >= 0.5: 2(58.0/2.0)


