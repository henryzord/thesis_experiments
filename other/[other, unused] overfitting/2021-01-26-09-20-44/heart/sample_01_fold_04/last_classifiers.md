# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 1 | 0.555556 |
| ChestPainType > 3.5 and MajorVessels > 0.5 and Thal > 4.5 | 2 | 0.233087 |
| ChestPainType <= 3.5 and MajorVessels > 0.5 and Thal > 4.5 | 2 | 0.064637 |
| ChestPainType > 3.0 and MajorVessels > 0.0 | 2 | 0.293543 |
| ChestPainType > 3.5 and MajorVessels <= 0.5 and Thal > 4.5 | 2 | 0.097182 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| ChestPainType <= 3.5 and Thal <= 4.5 and Sex <= 0.5 and MajorVessels <= 0.5 | 1 | 0.223022 |
| ChestPainType <= 3.5 and Slope <= 1.5 and Thal <= 5.0 and MaxHeartRate > 158.5 | 1 | 0.205882 |
| MajorVessels > 0.5 and ChestPainType > 3.5 and Slope > 1.5 | 2 | 0.361345 |
| Thal <= 6.5 and MajorVessels <= 0.5 and SerumCholestoral <= 272.0 and ResElectrocardiographic > 1.0 and ChestPainType > 3.5 | 1 | 0.155844 |
| ChestPainType > 3.5 and ResElectrocardiographic > 0.5 and ExerciseInduced > 0.5 | 2 | 0.169697 |
| MajorVessels <= 0.5 and FastingBloodSugar <= 0.5 and ExerciseInduced <= 0.5 and ResElectrocardiographic <= 1.0 and SerumCholestoral > 215.0 | 1 | 0.091629 |
| MajorVessels <= 0.5 and FastingBloodSugar <= 0.5 and ExerciseInduced <= 0.5 and ResElectrocardiographic > 1.0 and RestBloodPressure <= 134.0 | 1 | 0.082492 |
| MajorVessels <= 0.5 and FastingBloodSugar <= 0.5 and Slope <= 1.5 | 1 | 0.160714 |
| FastingBloodSugar > 0.5 | 1 | 0.178506 |
| Thal > 6.5 and ChestPainType <= 3.5 | 2 | 0.375479 |
| Thal <= 6.5 and ChestPainType <= 3.5 | 1 | 0.135135 |
| Thal <= 6.5 | 2 | 0.666667 |
|  | 2 | 0.653846 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

chestpaintype|majorvessels|thal|class
---|---|---|---
(3.5-inf)|(0.5-inf)|(4.5-inf)|2
(-inf-3.5]|(0.5-inf)|(4.5-inf)|2
(-inf-3.5]|(-inf-0.5]|(4.5-inf)|1
(3.5-inf)|(-inf-0.5]|(4.5-inf)|2
(-inf-3.5]|(0.5-inf)|(-inf-4.5]|1
(3.5-inf)|(0.5-inf)|(-inf-4.5]|2
(-inf-3.5]|(-inf-0.5]|(-inf-4.5]|1
(3.5-inf)|(-inf-0.5]|(-inf-4.5]|1

## PART

Decision list:

rules | predicted class
---|---
ChestPainType <= 3.5 AND Thal <= 4.5 AND Sex <= 0.5 AND MajorVessels <= 0.5|1 (31.0)
ChestPainType <= 3.5 AND Slope <= 1.5 AND Thal <= 5.0 AND MaxHeartRate > 158.5|1 (28.0)
MajorVessels > 0.5 AND ChestPainType > 3.5 AND Slope > 1.5|2 (43.0)
Thal <= 6.5 AND MajorVessels <= 0.5 AND SerumCholestoral <= 272.0 AND ResElectrocardiographic > 1.0 AND ChestPainType > 3.5|1 (12.0)
ChestPainType > 3.5 AND ResElectrocardiographic > 0.5 AND ExerciseInduced > 0.5|2 (15.0/1.0)
MajorVessels <= 0.5 AND FastingBloodSugar <= 0.5 AND ExerciseInduced <= 0.5 AND ResElectrocardiographic <= 1.0 AND SerumCholestoral > 215.0|1 (17.0/8.0)
MajorVessels <= 0.5 AND FastingBloodSugar <= 0.5 AND ExerciseInduced <= 0.5 AND ResElectrocardiographic > 1.0 AND RestBloodPressure <= 134.0|1 (11.0/4.0)
MajorVessels <= 0.5 AND FastingBloodSugar <= 0.5 AND Slope <= 1.5|1 (17.0/3.0)
FastingBloodSugar > 0.5|1 (18.0/4.0)
Thal > 6.5 AND ChestPainType <= 3.5|2 (16.0/4.0)
Thal <= 6.5 AND ChestPainType <= 3.5|1 (13.0/3.0)
Thal <= 6.5|2 (12.0/5.0)
|2 (10.0)


## J48 Decision Tree

* ChestPainType <= 3.0
	* Thal <= 3.0: 1 (93.0/8.0)
	* Thal > 3.0
		* MajorVessels <= 0.0: 1 (22.0/5.0)
		* MajorVessels > 0.0: 2 (13.0/2.0)
* ChestPainType > 3.0
	* MajorVessels <= 0.0
		* Thal <= 6.0: 1 (31.0/7.0)
		* Thal > 6.0: 2 (24.0/5.0)
	* MajorVessels > 0.0: 2 (60.0/2.0)


