# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 1 | 0.555556 |
| ChestPainType > 3.5 and SerumCholestoral = all and Oldpeak > 17 and MajorVessels > 0.5 and Thal <= 4.5 | 2 | 0.049296 |
| ChestPainType > 3.5 and SerumCholestoral = all and Oldpeak > 17 and MajorVessels > 0.5 and Thal > 4.5 | 2 | 0.105960 |
| ChestPainType > 3.5 and SerumCholestoral = all and Oldpeak <= 17 and MajorVessels > 0.5 and Thal > 4.5 | 2 | 0.157112 |
| ChestPainType > 3.5 and SerumCholestoral = all and Oldpeak > 17 and MajorVessels <= 0.5 and Thal > 4.5 | 2 | 0.029976 |
| ChestPainType > 3.5 and SerumCholestoral = all and Oldpeak <= 17 and MajorVessels > 0.5 and Thal <= 4.5 | 2 | 0.041558 |
| Thal <= 3.0 and Oldpeak > 16.0 | 2 | 0.050840 |
| ChestPainType <= 3.5 and SerumCholestoral = all and Oldpeak > 17 and MajorVessels > 0.5 and Thal > 4.5 | 2 | 0.023188 |
| ChestPainType <= 3.5 and SerumCholestoral = all and Oldpeak <= 17 and MajorVessels > 0.5 and Thal > 4.5 | 2 | 0.041558 |
| ChestPainType > 3.5 and SerumCholestoral = all and Oldpeak <= 17 and MajorVessels <= 0.5 and Thal > 4.5 | 2 | 0.071637 |
| Thal > 3.0 | 2 | 0.319457 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Thal <= 4.5 and Oldpeak <= 17.0 and MajorVessels <= 0.5 and Age <= 58.5 | 1 | 0.382857 |
| ChestPainType > 3.5 and MajorVessels > 0.5 and Sex > 0.5 | 2 | 0.404211 |
| Slope <= 1.5 and ResElectrocardiographic <= 1.0 and Sex <= 0.5 | 1 | 0.178082 |
| ChestPainType > 3.5 and Slope <= 2.5 and Age <= 52.0 | 2 | 0.180171 |
| Slope <= 1.5 and FastingBloodSugar > 0.5 | 1 | 0.176901 |
| MajorVessels > 1.5 | 2 | 0.249138 |
| Slope <= 1.5 and MajorVessels <= 0.5 and SerumCholestoral > 246.5 | 2 | 0.085106 |
| Slope > 1.5 and MajorVessels <= 0.5 and ExerciseInduced <= 0.5 | 1 | 0.364899 |
| Slope > 1.5 and RestBloodPressure > 119.0 | 2 | 0.407407 |
|  | 1 | 0.931034 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Thal >= 6 and MajorVessels >= 1 | 2 | 0.269512 |
| ChestPainType >= 4 and ExerciseInduced >= 1 and Oldpeak >= 8 | 2 | 0.117974 |
| Thal >= 7 and Age <= 48 | 2 | 0.047872 |
| Age >= 57 and SerumCholestoral >= 273 and Sex >= 1 | 2 | 0.051857 |
| MajorVessels >= 1 and ChestPainType >= 4 | 2 | 0.029805 |
|  | 1 | 0.937500 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

chestpaintype|serumcholestoral|oldpeak|majorvessels|thal|class
---|---|---|---|---|---
(-inf-3.5]|all|(17-inf)|(0.5-inf)|(4.5-inf)|2
(3.5-inf)|all|(17-inf)|(0.5-inf)|(4.5-inf)|2
(-inf-3.5]|all|(-inf-17]|(0.5-inf)|(4.5-inf)|2
(3.5-inf)|all|(-inf-17]|(0.5-inf)|(4.5-inf)|2
(3.5-inf)|all|(17-inf)|(-inf-0.5]|(4.5-inf)|2
(-inf-3.5]|all|(17-inf)|(-inf-0.5]|(4.5-inf)|1
(-inf-3.5]|all|(17-inf)|(0.5-inf)|(-inf-4.5]|1
(3.5-inf)|all|(17-inf)|(0.5-inf)|(-inf-4.5]|2
(3.5-inf)|all|(-inf-17]|(-inf-0.5]|(4.5-inf)|2
(-inf-3.5]|all|(-inf-17]|(-inf-0.5]|(4.5-inf)|1
(-inf-3.5]|all|(-inf-17]|(0.5-inf)|(-inf-4.5]|1
(3.5-inf)|all|(-inf-17]|(0.5-inf)|(-inf-4.5]|2
(3.5-inf)|all|(17-inf)|(-inf-0.5]|(-inf-4.5]|1
(-inf-3.5]|all|(17-inf)|(-inf-0.5]|(-inf-4.5]|1
(3.5-inf)|all|(-inf-17]|(-inf-0.5]|(-inf-4.5]|1
(-inf-3.5]|all|(-inf-17]|(-inf-0.5]|(-inf-4.5]|1

## JRip

Decision list:

rules | predicted class
---|---
(Thal >= 6) and (MajorVessels >= 1)|2 (61.0/6.0)
(ChestPainType >= 4) and (ExerciseInduced >= 1) and (Oldpeak >= 8)|2 (20.0/1.0)
(Thal >= 7) and (Age <= 48)|2 (12.0/3.0)
(Age >= 57) and (SerumCholestoral >= 273) and (Sex >= 1)|2 (10.0/1.0)
(MajorVessels >= 1) and (ChestPainType >= 4)|2 (10.0/3.0)
|1 (130.0/9.0)


## PART

Decision list:

rules | predicted class
---|---
Thal <= 4.5 AND Oldpeak <= 17.0 AND MajorVessels <= 0.5 AND Age <= 58.5|1 (67.0)
ChestPainType > 3.5 AND MajorVessels > 0.5 AND Sex > 0.5|2 (50.0/2.0)
Slope <= 1.5 AND ResElectrocardiographic <= 1.0 AND Sex <= 0.5|1 (13.0)
ChestPainType > 3.5 AND Slope <= 2.5 AND Age <= 52.0|2 (13.0)
Slope <= 1.5 AND FastingBloodSugar > 0.5|1 (11.0/1.0)
MajorVessels > 1.5|2 (19.0/3.0)
Slope <= 1.5 AND MajorVessels <= 0.5 AND SerumCholestoral > 246.5|2 (9.0/3.0)
Slope > 1.5 AND MajorVessels <= 0.5 AND ExerciseInduced <= 0.5|1 (22.0/5.0)
Slope > 1.5 AND RestBloodPressure > 119.0|2 (20.0/2.0)
|1 (19.0/1.0)


## J48 Decision Tree

* Thal <= 3.0
	* Oldpeak <= 16.0: 1 (59.0/7.0)
	* Oldpeak > 16.0: 2 (8.0/2.0)
* Thal > 3.0: 2 (55.0/14.0)


