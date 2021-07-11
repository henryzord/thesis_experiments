# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| nbumps < 1.5 and gpuls < 1342.0 and genergy >= 16885.0 | 0 | 0.859347 |
| nbumps < 1.5 and gpuls < 1342.0 and genergy < 16885.0 and energy < 3500.0 and genergy >= 7295.0 | 0 | 0.741824 |
| nbumps < 1.5 and gpuls < 1342.0 and genergy < 16885.0 and energy < 3500.0 and genergy < 7295.0 | 0 | 0.678861 |
| nbumps >= 1.5 and gpuls < 749.0 and seismoacoustic != d | 0 | 0.578332 |
| nbumps >= 1.5 and gpuls >= 749.0 and nbumps2 >= 0.5 and gdenergy >= -29.5 | 0 | 0.340845 |
| nbumps < 1.5 and gpuls >= 1342.0 and nbumps3 < 0.5 | 0 | 0.252083 |
| nbumps >= 1.5 and gpuls >= 749.0 and nbumps2 < 0.5 | 0 | 0.200705 |
| nbumps < 1.5 and gpuls < 1342.0 and genergy < 16885.0 and energy >= 3500.0 | 0 | 0.154083 |
| nbumps > 1 and nbumps2 > 0 and seismic = b and genergy > 197620 and seismoacoustic = a and nbumps2 > 1 | 1 | 0.002453 |
| nbumps > 1 and nbumps2 > 0 and seismic = b and genergy > 197620 and seismoacoustic = a and nbumps2 <= 1 | 1 | 0.001843 |
| nbumps > 1 and nbumps2 > 0 and seismic = b and genergy <= 197620 and nbumps3 > 1 and seismoacoustic = b and nbumps4 <= 0 | 1 | 0.001613 |
| nbumps < 1.5 and gpuls >= 1342.0 and nbumps3 >= 0.5 | 1 | 0.002304 |
| nbumps >= 1.5 and gpuls >= 749.0 and nbumps2 >= 0.5 and gdenergy < -29.5 and gpuls >= 1201.0 | 1 | 0.003266 |
| nbumps > 1 and nbumps2 <= 0 and seismoacoustic = c | 1 | 0.000230 |
| nbumps <= 1 and gpuls > 1209 and nbumps3 > 0 and seismic = a | 0 | 0.052743 |
| nbumps >= 1.5 and gpuls >= 749.0 and nbumps2 >= 0.5 and gdenergy < -29.5 and gpuls < 1201.0 | 0 | 0.029115 |
| nbumps <= 1 and gpuls > 1209 and nbumps3 > 0 and seismic = b | 1 | 0.002661 |
| nbumps > 1 and nbumps2 > 0 and seismic = b and genergy > 197620 and seismoacoustic = b | 0 | 0.023684 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| nbumps <= 1 and gpuls <= 1209 and genergy <= 16840 and energy <= 3500 and genergy > 7290 | 0 | 0.741824 |
| nbumps <= 1 and gpuls <= 1332 and gdpuls > -75 and shift = N and gdpuls > -70 and genergy > 16940 | 0 | 0.595687 |
| nbumps <= 1 and gpuls <= 1332 and gpuls > 32 and gdpuls > -75 and gpuls > 812 and gpuls <= 1209 | 0 | 0.440299 |
| gpuls <= 749 and nbumps <= 1 and gpuls > 32 and gdpuls > -75 and gdenergy <= 88 and gdenergy <= 70 and energy <= 7500 and genergy <= 7240 and nbumps <= 0 and gdenergy <= -3 | 0 | 0.512987 |
| gpuls <= 749 and gpuls <= 59 and seismoacoustic = a | 0 | 0.486301 |
| gpuls <= 749 and genergy <= 128260 and nbumps <= 1 and gpuls > 89 and gdpuls > -53 and energy > 1500 | 0 | 0.367089 |
| energy <= 500 and gdpuls <= 101 and gdenergy <= 88 and shift = W and gpuls > 318 and gdenergy <= 70 and gdpuls > 20 and gdenergy <= 61 and genergy <= 43030 | 0 | 0.305556 |
| energy <= 700 and genergy <= 546980 and gpuls <= 768 and gdenergy > -54 and genergy <= 49520 and gdpuls > -37 and genergy <= 32690 and genergy > 21240 and gdpuls > -9 and gdenergy > -19 and gpuls > 270 and gdpuls <= 117 and gdpuls > -4 | 0 | 0.321267 |
| energy <= 500 and genergy <= 546980 and gdenergy <= 87 and gpuls <= 318 and genergy > 12220 | 0 | 0.282297 |
| energy <= 1800 and genergy <= 715540 and genergy <= 320150 and nbumps2 <= 1 and gdpuls <= -5 and gpuls > 87 and shift = W and gpuls > 317 and genergy > 18510 and genergy > 21240 and gdenergy > -41 and genergy > 25130 and genergy > 25760 and gdenergy <= 15 | 0 | 0.257426 |
| gdenergy > 182 and gdpuls <= 278 | 0 | 0.166667 |
| gpuls <= 749 and genergy <= 128260 and gdenergy <= 68 and gdenergy > 45 and gdpuls > -11 | 0 | 0.210526 |
| gdpuls <= 93 and maxenergy <= 3000 and gdenergy <= -57 and genergy <= 65150 | 0 | 0.162011 |
| gdenergy > -58 and gdpuls <= 93 and gpuls <= 802 and genergy > 128260 and genergy <= 316200 | 0 | 0.166667 |
| gdenergy > -56 and gdpuls <= 93 and genergy <= 95050 and maxenergy > 9000 and nbumps <= 6 | 0 | 0.175824 |
| gdenergy > -56 and nbumps <= 2 and genergy <= 1061760 and genergy <= 95050 and gdpuls <= -9 and genergy <= 41410 and genergy <= 36520 and energy <= 2300 and genergy > 18580 and genergy > 19040 and genergy > 20420 and genergy > 21220 and gdenergy > -46 and gdenergy <= 27 and nbumps3 <= 0 | 0 | 0.242424 |
| genergy > 1132810 and gpuls > 1545 | 0 | 0.137931 |
| gpuls <= 2205 and gdenergy > -56 and maxenergy <= 3000 and gpuls <= 155 and genergy > 6070 | 0 | 0.122807 |
| gpuls <= 2205 and gdenergy > -56 and gpuls > 1946 and gdpuls > -11 | 0 | 0.132948 |
| gpuls <= 1742 and gdenergy > -56 and nbumps <= 4 and genergy > 448900 and nbumps2 <= 1 and genergy <= 993080 | 0 | 0.137931 |
| genergy <= 77040 and energy <= 13500 and genergy > 16940 and gdpuls <= 93 and gpuls <= 802 and gpuls > 732 and gdenergy > -2 | 0 | 0.127907 |
| genergy <= 77040 and energy <= 13500 and genergy > 16940 and genergy <= 18540 and genergy <= 17620 | 0 | 0.096386 |
| genergy <= 77040 and energy <= 13500 and genergy > 17750 and gpuls <= 723 and ghazard = a and nbumps3 > 2 and gdenergy <= 25 | 0 | 0.122807 |
| nbumps3 <= 2 and gdenergy > -56 and genergy <= 76150 and genergy > 17750 and gpuls > 325 and genergy <= 20500 and gdenergy > -45 | 0 | 0.152542 |
| nbumps3 <= 2 and gpuls <= 1742 and genergy > 20550 and genergy <= 48530 and genergy <= 46740 and gdpuls > -49 and gdpuls <= 113 and gdpuls <= 79 and ghazard = a and gpuls <= 670 and genergy <= 42220 and genergy <= 25130 and gpuls > 326 | 0 | 0.132948 |
| nbumps3 <= 2 and genergy > 21780 and genergy <= 76150 and gpuls <= 258 and energy <= 10700 | 0 | 0.090909 |
| nbumps3 <= 2 and genergy > 21780 and genergy <= 76150 and gpuls > 1259 and genergy > 47370 | 0 | 0.074074 |
| nbumps3 <= 2 and genergy > 21780 and gpuls <= 723 and gdenergy > -53 and energy <= 9900 and gpuls <= 682 and genergy > 32960 and gpuls <= 646 and gpuls <= 608 and genergy > 34230 and gpuls > 301 and gpuls > 409 and gpuls <= 461 | 0 | 0.122807 |
| nbumps <= 4 and gdenergy > 8 and genergy > 20860 and gpuls <= 1828 and gpuls > 1525 | 0 | 0.068323 |
| nbumps <= 4 and gpuls <= 1325 and genergy > 21780 and genergy > 248900 and gpuls > 989 | 0 | 0.085366 |
| genergy <= 185910 and genergy > 21780 and gdpuls > -52 and shift = W and nbumps3 <= 2 and gpuls <= 723 and gdenergy > 8 and gdenergy > 14 and gpuls <= 682 and gpuls <= 646 and genergy > 30750 and genergy <= 68830 and gpuls > 540 | 0 | 0.137931 |
| ghazard = a and nbumps3 <= 2 and genergy <= 122030 and gdenergy > -63 and gdpuls <= 93 and gdpuls > 68 and gdenergy <= 147 | 0 | 0.056604 |
| gdenergy > -54 and genergy <= 185910 and genergy > 134890 and nbumps2 > 0 | 0 | 0.068323 |
| nbumps3 <= 2 and gdenergy > -54 and gpuls <= 999 and genergy > 21350 and gdenergy <= -21 and energy > 1200 | 0 | 0.132948 |
| nbumps3 <= 2 and energy > 40700 and energy <= 67700 | 0 | 0.056604 |
| energy <= 5700 and energy > 4800 and genergy > 55230 | 0 | 0.056604 |
| genergy <= 48440 and genergy <= 46640 and gdenergy > 8 and maxenergy <= 5000 and genergy > 20860 and genergy <= 45180 and energy > 900 | 0 | 0.085366 |
| nbumps3 > 2 and maxenergy <= 7000 and genergy > 50580 | 1 | 0.031746 |
| ghazard = a and energy <= 3500 and genergy <= 5940 and energy <= 100 | 0 | 0.012414 |
| ghazard = a and energy <= 3500 and gdpuls <= 48 and gdenergy > 34 and genergy > 61770 | 0 | 0.064935 |
| ghazard = a and genergy <= 48440 and genergy <= 46640 and nbumps <= 4 and gdpuls > -64 and gdpuls <= 113 and gpuls > 260 and gpuls <= 317 | 0 | 0.058824 |
| ghazard = a and energy <= 500 and genergy <= 734930 and genergy <= 48440 and gdpuls <= 113 and gdpuls <= -33 | 0 | 0.028153 |
| ghazard = b and nbumps2 <= 1 and gdenergy <= 140 and genergy > 26280 | 0 | 0.024295 |
| ghazard = b and gdenergy <= 121 and genergy <= 21070 | 1 | 0.014706 |
| ghazard = a and gdenergy <= -31 and gdenergy > -42 and gpuls > 209 and gpuls <= 1684 | 1 | 0.079268 |
| ghazard = a and gpuls > 1737 and gdpuls <= 68 and gdenergy <= 43 and nbumps2 > 0 and nbumps <= 3 and genergy <= 632800 | 1 | 0.050314 |
| ghazard = a and nbumps <= 2 and gdenergy <= -53 and gdpuls > -63 | 1 | 0.039013 |
| ghazard = a and nbumps <= 2 and energy > 22600 | 0 | 0.073770 |
| ghazard = a and energy > 32000 and gdenergy <= 17 | 1 | 0.010563 |
| energy > 21000 and energy > 27600 and energy > 34000 | 1 | 0.025000 |
| ghazard = a and gdenergy <= 87 and energy <= 500 and genergy > 28960 and genergy <= 225040 and genergy > 32210 and gpuls <= 668 and gdenergy > 16 and gdpuls > -18 | 0 | 0.118644 |
| ghazard = a and genergy > 836500 and nbumps3 <= 0 | 0 | 0.045872 |
| ghazard = b and gdenergy > 117 and genergy <= 62880 | 0 | 0.029907 |
| ghazard = b and gdenergy <= 117 | 1 | 0.033875 |
| ghazard = a and nbumps <= 0 and genergy <= 27630 | 1 | 0.062992 |
| ghazard = a and genergy <= 34230 and gdpuls > -69 and gpuls > 382 and gdpuls <= 103 and genergy <= 32430 | 0 | 0.116505 |
| ghazard = a and genergy <= 9590 and gdpuls <= -26 | 0 | 0.061856 |
| ghazard = a and energy > 10800 and gdpuls <= 36 and energy <= 12100 | 0 | 0.043860 |
| ghazard = a and energy > 14300 and energy > 18000 and genergy <= 122410 | 0 | 0.072562 |
| ghazard = a and gdpuls <= -52 and energy > 4400 | 1 | 0.073684 |
| ghazard = a and nbumps2 > 3 and gdenergy <= 19 | 1 | 0.011364 |
| ghazard = a and nbumps > 5 and gdenergy <= 22 | 1 | 0.009195 |
| ghazard = a and gpuls > 1828 and genergy <= 763520 and genergy > 415690 | 0 | 0.032520 |
| gpuls > 1828 and seismic = b | 1 | 0.078144 |
| ghazard = a and gdpuls <= -25 and genergy <= 240350 and nbumps2 <= 1 and gdenergy > -46 and energy > 2000 | 0 | 0.076923 |
| ghazard = a and genergy <= 28060 and gdenergy > -48 | 1 | 0.123596 |
| ghazard = a and genergy <= 28820 | 0 | 0.091418 |
| ghazard = a and gdpuls > 13 and gdpuls > 16 and nbumps <= 0 and seismic = b | 1 | 0.067669 |
| ghazard = a and gdpuls > 13 and gdpuls > 17 and nbumps <= 5 and genergy <= 59250 and gdenergy > 1 and genergy <= 39330 | 0 | 0.126984 |
| ghazard = a and genergy <= 40670 and gdenergy <= 10 | 1 | 0.112676 |
| ghazard = a and genergy <= 1096910 and genergy <= 768080 and gdpuls > 10 and gdpuls <= 18 | 0 | 0.129630 |
| ghazard = a and genergy <= 1096910 and genergy > 675030 | 1 | 0.069444 |
| ghazard = a and gdpuls > 62 | 0 | 0.109422 |
| ghazard = a and genergy > 390180 and gpuls <= 1504 | 0 | 0.106383 |
| ghazard = a and nbumps <= 4 and gdenergy > 89 and gpuls > 702 | 1 | 0.085034 |
| ghazard = a and nbumps <= 4 and gdpuls > 34 and gdenergy > 35 | 1 | 0.033333 |
| ghazard = a and gdpuls <= 38 and nbumps <= 4 and maxenergy > 2000 and seismic = b and genergy <= 199030 | 1 | 0.166667 |
| ghazard = a and gdpuls <= 38 and nbumps <= 3 and gpuls <= 1571 and genergy > 163510 | 1 | 0.085034 |
| gpuls > 465 and genergy > 39330 and genergy > 45020 and gdenergy <= 88 and gdenergy > -22 and gpuls > 702 | 0 | 0.413603 |
| ghazard = a and maxenergy <= 7000 and gpuls <= 627 and genergy <= 80210 and gpuls <= 465 and gdenergy <= 35 | 1 | 0.166667 |
| genergy > 39330 and genergy > 44800 and gpuls <= 675 and maxenergy > 1000 | 0 | 0.440000 |
| genergy <= 39330 | 0 | 0.338624 |
| genergy > 44800 and gpuls > 505 and seismoacoustic = a | 1 | 0.240385 |
| genergy <= 44800 | 1 | 0.277778 |
| genergy <= 75670 | 0 | 0.571429 |
|  | 1 | 0.444444 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| nbumps >= 2 and gpuls >= 751 and gdpuls <= 9 | 1 | 0.004831 |
|  | 0 | 0.948012 |


# Text representation of classifiers as-is

## JRip

Decision list:

rules | predicted class
---|---
(nbumps >= 2) and (gpuls >= 751) and (gdpuls <= 9)|1 (93.0/62.0)
|0 (2227.0/119.0)


## PART

Decision list:

rules | predicted class
---|---
nbumps <= 1 AND gpuls <= 1209 AND genergy <= 16840 AND energy <= 3500 AND genergy > 7290|0 (431.0)
nbumps <= 1 AND gpuls <= 1332 AND gdpuls > -75 AND shift = N AND gdpuls > -70 AND genergy > 16940|0 (221.0)
nbumps <= 1 AND gpuls <= 1332 AND gpuls > 32 AND gdpuls > -75 AND gpuls > 812 AND gpuls <= 1209|0 (118.0)
gpuls <= 749 AND nbumps <= 1 AND gpuls > 32 AND gdpuls > -75 AND gdenergy <= 88 AND gdenergy <= 70 AND energy <= 7500 AND genergy <= 7240 AND nbumps <= 0 AND gdenergy <= -3|0 (158.0)
gpuls <= 749 AND gpuls <= 59 AND seismoacoustic = a|0 (142.0)
gpuls <= 749 AND genergy <= 128260 AND nbumps <= 1 AND gpuls > 89 AND gdpuls > -53 AND energy > 1500|0 (87.0)
energy <= 500 AND gdpuls <= 101 AND gdenergy <= 88 AND shift = W AND gpuls > 318 AND gdenergy <= 70 AND gdpuls > 20 AND gdenergy <= 61 AND genergy <= 43030|0 (66.0)
energy <= 700 AND genergy <= 546980 AND gpuls <= 768 AND gdenergy > -54 AND genergy <= 49520 AND gdpuls > -37 AND genergy <= 32690 AND genergy > 21240 AND gdpuls > -9 AND gdenergy > -19 AND gpuls > 270 AND gdpuls <= 117 AND gdpuls > -4|0 (71.0)
energy <= 500 AND genergy <= 546980 AND gdenergy <= 87 AND gpuls <= 318 AND genergy > 12220|0 (59.0)
energy <= 1800 AND genergy <= 715540 AND genergy <= 320150 AND nbumps2 <= 1 AND gdpuls <= -5 AND gpuls > 87 AND shift = W AND gpuls > 317 AND genergy > 18510 AND genergy > 21240 AND gdenergy > -41 AND genergy > 25130 AND genergy > 25760 AND gdenergy <= 15|0 (52.0)
gdenergy > 182 AND gdpuls <= 278|0 (30.0)
gpuls <= 749 AND genergy <= 128260 AND gdenergy <= 68 AND gdenergy > 45 AND gdpuls > -11|0 (40.0)
gdpuls <= 93 AND maxenergy <= 3000 AND gdenergy <= -57 AND genergy <= 65150|0 (29.0)
gdenergy > -58 AND gdpuls <= 93 AND gpuls <= 802 AND genergy > 128260 AND genergy <= 316200|0 (30.0)
gdenergy > -56 AND gdpuls <= 93 AND genergy <= 95050 AND maxenergy > 9000 AND nbumps <= 6|0 (32.0)
gdenergy > -56 AND nbumps <= 2 AND genergy <= 1061760 AND genergy <= 95050 AND gdpuls <= -9 AND genergy <= 41410 AND genergy <= 36520 AND energy <= 2300 AND genergy > 18580 AND genergy > 19040 AND genergy > 20420 AND genergy > 21220 AND gdenergy > -46 AND gdenergy <= 27 AND nbumps3 <= 0|0 (48.0)
genergy > 1132810 AND gpuls > 1545|0 (24.0)
gpuls <= 2205 AND gdenergy > -56 AND maxenergy <= 3000 AND gpuls <= 155 AND genergy > 6070|0 (21.0)
gpuls <= 2205 AND gdenergy > -56 AND gpuls > 1946 AND gdpuls > -11|0 (23.0)
gpuls <= 1742 AND gdenergy > -56 AND nbumps <= 4 AND genergy > 448900 AND nbumps2 <= 1 AND genergy <= 993080|0 (24.0)
genergy <= 77040 AND energy <= 13500 AND genergy > 16940 AND gdpuls <= 93 AND gpuls <= 802 AND gpuls > 732 AND gdenergy > -2|0 (22.0)
genergy <= 77040 AND energy <= 13500 AND genergy > 16940 AND genergy <= 18540 AND genergy <= 17620|0 (16.0)
genergy <= 77040 AND energy <= 13500 AND genergy > 17750 AND gpuls <= 723 AND ghazard = a AND nbumps3 > 2 AND gdenergy <= 25|0 (21.0)
nbumps3 <= 2 AND gdenergy > -56 AND genergy <= 76150 AND genergy > 17750 AND gpuls > 325 AND genergy <= 20500 AND gdenergy > -45|0 (27.0)
nbumps3 <= 2 AND gpuls <= 1742 AND genergy > 20550 AND genergy <= 48530 AND genergy <= 46740 AND gdpuls > -49 AND gdpuls <= 113 AND gdpuls <= 79 AND ghazard = a AND gpuls <= 670 AND genergy <= 42220 AND genergy <= 25130 AND gpuls > 326|0 (23.0)
nbumps3 <= 2 AND genergy > 21780 AND genergy <= 76150 AND gpuls <= 258 AND energy <= 10700|0 (15.0)
nbumps3 <= 2 AND genergy > 21780 AND genergy <= 76150 AND gpuls > 1259 AND genergy > 47370|0 (12.0)
nbumps3 <= 2 AND genergy > 21780 AND gpuls <= 723 AND gdenergy > -53 AND energy <= 9900 AND gpuls <= 682 AND genergy > 32960 AND gpuls <= 646 AND gpuls <= 608 AND genergy > 34230 AND gpuls > 301 AND gpuls > 409 AND gpuls <= 461|0 (21.0)
nbumps <= 4 AND gdenergy > 8 AND genergy > 20860 AND gpuls <= 1828 AND gpuls > 1525|0 (11.0)
nbumps <= 4 AND gpuls <= 1325 AND genergy > 21780 AND genergy > 248900 AND gpuls > 989|0 (14.0)
genergy <= 185910 AND genergy > 21780 AND gdpuls > -52 AND shift = W AND nbumps3 <= 2 AND gpuls <= 723 AND gdenergy > 8 AND gdenergy > 14 AND gpuls <= 682 AND gpuls <= 646 AND genergy > 30750 AND genergy <= 68830 AND gpuls > 540|0 (24.0)
ghazard = a AND nbumps3 <= 2 AND genergy <= 122030 AND gdenergy > -63 AND gdpuls <= 93 AND gdpuls > 68 AND gdenergy <= 147|0 (9.0)
gdenergy > -54 AND genergy <= 185910 AND genergy > 134890 AND nbumps2 > 0|0 (11.0)
nbumps3 <= 2 AND gdenergy > -54 AND gpuls <= 999 AND genergy > 21350 AND gdenergy <= -21 AND energy > 1200|0 (23.0)
nbumps3 <= 2 AND energy > 40700 AND energy <= 67700|0 (9.0)
energy <= 5700 AND energy > 4800 AND genergy > 55230|0 (9.0)
genergy <= 48440 AND genergy <= 46640 AND gdenergy > 8 AND maxenergy <= 5000 AND genergy > 20860 AND genergy <= 45180 AND energy > 900|0 (14.0)
nbumps3 > 2 AND maxenergy <= 7000 AND genergy > 50580|1 (6.0)
ghazard = a AND energy <= 3500 AND genergy <= 5940 AND energy <= 100|0 (5.0/2.0)
ghazard = a AND energy <= 3500 AND gdpuls <= 48 AND gdenergy > 34 AND genergy > 61770|0 (10.0)
ghazard = a AND genergy <= 48440 AND genergy <= 46640 AND nbumps <= 4 AND gdpuls > -64 AND gdpuls <= 113 AND gpuls > 260 AND gpuls <= 317|0 (9.0)
ghazard = a AND energy <= 500 AND genergy <= 734930 AND genergy <= 48440 AND gdpuls <= 113 AND gdpuls <= -33|0 (5.0)
ghazard = b AND nbumps2 <= 1 AND gdenergy <= 140 AND genergy > 26280|0 (7.0/2.0)
ghazard = b AND gdenergy <= 121 AND genergy <= 21070|1 (4.0/1.0)
ghazard = a AND gdenergy <= -31 AND gdenergy > -42 AND gpuls > 209 AND gpuls <= 1684|1 (13.0)
ghazard = a AND gpuls > 1737 AND gdpuls <= 68 AND gdenergy <= 43 AND nbumps2 > 0 AND nbumps <= 3 AND genergy <= 632800|1 (8.0)
ghazard = a AND nbumps <= 2 AND gdenergy <= -53 AND gdpuls > -63|1 (7.0/1.0)
ghazard = a AND nbumps <= 2 AND energy > 22600|0 (9.0)
ghazard = a AND energy > 32000 AND gdenergy <= 17|1 (6.0/3.0)
energy > 21000 AND energy > 27600 AND energy > 34000|1 (7.0/1.0)
ghazard = a AND gdenergy <= 87 AND energy <= 500 AND genergy > 28960 AND genergy <= 225040 AND genergy > 32210 AND gpuls <= 668 AND gdenergy > 16 AND gdpuls > -18|0 (14.0)
ghazard = a AND genergy > 836500 AND nbumps3 <= 0|0 (5.0)
ghazard = b AND gdenergy > 117 AND genergy <= 62880|0 (5.0/1.0)
ghazard = b AND gdenergy <= 117|1 (4.0)
ghazard = a AND nbumps <= 0 AND genergy <= 27630|1 (7.0)
ghazard = a AND genergy <= 34230 AND gdpuls > -69 AND gpuls > 382 AND gdpuls <= 103 AND genergy <= 32430|0 (12.0)
ghazard = a AND genergy <= 9590 AND gdpuls <= -26|0 (6.0)
ghazard = a AND energy > 10800 AND gdpuls <= 36 AND energy <= 12100|0 (6.0/1.0)
ghazard = a AND energy > 14300 AND energy > 18000 AND genergy <= 122410|0 (6.0/1.0)
ghazard = a AND gdpuls <= -52 AND energy > 4400|1 (6.0)
ghazard = a AND nbumps2 > 3 AND gdenergy <= 19|1 (4.0/2.0)
ghazard = a AND nbumps > 5 AND gdenergy <= 22|1 (4.0/2.0)
ghazard = a AND gpuls > 1828 AND genergy <= 763520 AND genergy > 415690|0 (5.0/2.0)
gpuls > 1828 AND seismic = b|1 (6.0)
ghazard = a AND gdpuls <= -25 AND genergy <= 240350 AND nbumps2 <= 1 AND gdenergy > -46 AND energy > 2000|0 (6.0)
ghazard = a AND genergy <= 28060 AND gdenergy > -48|1 (11.0)
ghazard = a AND genergy <= 28820|0 (7.0/1.0)
ghazard = a AND gdpuls > 13 AND gdpuls > 16 AND nbumps <= 0 AND seismic = b|1 (7.0/1.0)
ghazard = a AND gdpuls > 13 AND gdpuls > 17 AND nbumps <= 5 AND genergy <= 59250 AND gdenergy > 1 AND genergy <= 39330|0 (8.0)
ghazard = a AND genergy <= 40670 AND gdenergy <= 10|1 (6.0)
ghazard = a AND genergy <= 1096910 AND genergy <= 768080 AND gdpuls > 10 AND gdpuls <= 18|0 (7.0)
ghazard = a AND genergy <= 1096910 AND genergy > 675030|1 (6.0/1.0)
ghazard = a AND gdpuls > 62|0 (7.0/1.0)
ghazard = a AND genergy > 390180 AND gpuls <= 1504|0 (5.0)
ghazard = a AND nbumps <= 4 AND gdenergy > 89 AND gpuls > 702|1 (5.0)
ghazard = a AND nbumps <= 4 AND gdpuls > 34 AND gdenergy > 35|1 (5.0/2.0)
ghazard = a AND gdpuls <= 38 AND nbumps <= 4 AND maxenergy > 2000 AND seismic = b AND genergy <= 199030|1 (9.0)
ghazard = a AND gdpuls <= 38 AND nbumps <= 3 AND gpuls <= 1571 AND genergy > 163510|1 (6.0/1.0)
gpuls > 465 AND genergy > 39330 AND genergy > 45020 AND gdenergy <= 88 AND gdenergy > -22 AND gpuls > 702|0 (12.0)
ghazard = a AND maxenergy <= 7000 AND gpuls <= 627 AND genergy <= 80210 AND gpuls <= 465 AND gdenergy <= 35|1 (6.0)
genergy > 39330 AND genergy > 44800 AND gpuls <= 675 AND maxenergy > 1000|0 (10.0)
genergy <= 39330|0 (7.0)
genergy > 44800 AND gpuls > 505 AND seismoacoustic = a|1 (5.0/1.0)
genergy <= 44800|1 (4.0)
genergy <= 75670|0 (4.0/1.0)
|1 (4.0/2.0)


## J48 Decision Tree

* nbumps <= 1
	* gpuls <= 1209
		* nbumps4 <= 0
			* shift = W
				* genergy <= 17660: 0 (247.0)
				* genergy > 17660
					* ghazard = a
						* nbumps3 <= 0
							* seismic = a
								* nbumps <= 0
									* seismoacoustic = a: 0 (131.0/6.0)
									* seismoacoustic = b: 0 (79.0/5.0)
									* seismoacoustic = c: 0 (0.0)
									* seismoacoustic = d: 0 (0.0)
								* nbumps > 0
									* seismoacoustic = a: 0 (41.0/4.0)
									* seismoacoustic = b: 0 (20.0)
									* seismoacoustic = c: 0 (0.0)
									* seismoacoustic = d: 0 (0.0)
							* seismic = b
								* nbumps <= 0
									* seismoacoustic = a: 0 (113.0/6.0)
									* seismoacoustic = b: 0 (68.0/4.0)
									* seismoacoustic = c: 0 (0.0)
									* seismoacoustic = d: 0 (0.0)
								* nbumps > 0
									* seismoacoustic = a
										* energy <= 500: 0 (15.0)
										* energy > 500: 0 (10.0/1.0)
									* seismoacoustic = b: 0 (16.0)
									* seismoacoustic = c: 0 (0.0)
									* seismoacoustic = d: 0 (0.0)
							* seismic = c: 0 (0.0)
							* seismic = d: 0 (0.0)
						* nbumps3 > 0
							* seismic = a
								* energy <= 2500: 0 (17.0/2.0)
								* energy > 2500: 0 (34.0)
							* seismic = b
								* seismoacoustic = a
									* energy <= 3500: 0 (13.0)
									* energy > 3500: 0 (10.0/1.0)
								* seismoacoustic = b: 0 (13.0)
								* seismoacoustic = c: 0 (0.0)
								* seismoacoustic = d: 0 (0.0)
							* seismic = c: 0 (0.0)
							* seismic = d: 0 (0.0)
					* ghazard = b
						* nbumps <= 0
							* seismic = a
								* gpuls <= 634: 0 (12.0)
								* gpuls > 634: 0 (10.0/1.0)
							* seismic = b
								* genergy <= 22220: 0 (10.0/3.0)
								* genergy > 22220: 0 (22.0)
							* seismic = c: 0 (0.0)
							* seismic = d: 0 (0.0)
						* nbumps > 0: 0 (27.0)
					* ghazard = c: 0 (16.0)
					* ghazard = d: 0 (0.0)
			* shift = N
				* nbumps <= 0
					* seismoacoustic = a
						* seismic = a: 0 (362.0/3.0)
						* seismic = b: 0 (53.0)
						* seismic = c: 0 (0.0)
						* seismic = d: 0 (0.0)
					* seismoacoustic = b: 0 (202.0)
					* seismoacoustic = c: 0 (2.0)
					* seismoacoustic = d: 0 (0.0)
				* nbumps > 0
					* seismoacoustic = a
						* nbumps2 <= 0: 0 (77.0/2.0)
						* nbumps2 > 0: 0 (33.0)
					* seismoacoustic = b
						* seismic = a
							* nbumps2 <= 0: 0 (30.0/1.0)
							* nbumps2 > 0: 0 (14.0)
						* seismic = b: 0 (12.0/1.0)
						* seismic = c: 0 (0.0)
						* seismic = d: 0 (0.0)
					* seismoacoustic = c: 0 (5.0)
					* seismoacoustic = d: 0 (0.0)
		* nbumps4 > 0
			* energy <= 34400
				* gpuls <= 459: 0 (10.0/2.0)
				* gpuls > 459: 0 (10.0)
			* energy > 34400: 0 (11.0)
	* gpuls > 1209
		* nbumps3 <= 0
			* nbumps4 <= 0
				* nbumps <= 0
					* seismic = a: 0 (24.0)
					* seismic = b: 0 (23.0/3.0)
					* seismic = c: 0 (0.0)
					* seismic = d: 0 (0.0)
				* nbumps > 0
					* gdenergy <= 5: 0 (10.0/3.0)
					* gdenergy > 5: 0 (11.0)
			* nbumps4 > 0: 0 (10.0)
		* nbumps3 > 0
			* seismic = a: 0 (12.0/2.0)
			* seismic = b: 1 (14.0/5.0)
			* seismic = c: 0 (0.0)
			* seismic = d: 0 (0.0)
* nbumps > 1
	* nbumps2 <= 0
		* seismoacoustic = a
			* seismic = a: 0 (24.0)
			* seismic = b
				* nbumps3 <= 1: 0 (10.0)
				* nbumps3 > 1: 0 (15.0/3.0)
			* seismic = c: 0 (0.0)
			* seismic = d: 0 (0.0)
		* seismoacoustic = b
			* seismic = a: 0 (18.0/2.0)
			* seismic = b: 0 (13.0)
			* seismic = c: 0 (0.0)
			* seismic = d: 0 (0.0)
		* seismoacoustic = c: 1 (2.0/1.0)
		* seismoacoustic = d: 0 (0.0)
	* nbumps2 > 0
		* seismic = a
			* ghazard = a
				* shift = W
					* seismoacoustic = a: 0 (120.0/20.0)
					* seismoacoustic = b: 0 (64.0/12.0)
					* seismoacoustic = c: 0 (1.0)
					* seismoacoustic = d: 0 (0.0)
				* shift = N: 0 (16.0/2.0)
			* ghazard = b: 0 (14.0/3.0)
			* ghazard = c: 0 (1.0)
			* ghazard = d: 0 (0.0)
		* seismic = b
			* genergy <= 197620
				* nbumps3 <= 1
					* nbumps3 <= 0
						* seismoacoustic = a: 0 (15.0/1.0)
						* seismoacoustic = b: 0 (15.0/2.0)
						* seismoacoustic = c: 0 (0.0)
						* seismoacoustic = d: 0 (0.0)
					* nbumps3 > 0
						* nbumps2 <= 1
							* seismoacoustic = a
								* genergy <= 46400: 0 (10.0/1.0)
								* genergy > 46400: 0 (10.0/2.0)
							* seismoacoustic = b: 0 (10.0/1.0)
							* seismoacoustic = c: 0 (0.0)
							* seismoacoustic = d: 0 (0.0)
						* nbumps2 > 1: 0 (18.0/4.0)
				* nbumps3 > 1
					* seismoacoustic = a: 0 (27.0/5.0)
					* seismoacoustic = b
						* nbumps4 <= 0: 1 (14.0/7.0)
						* nbumps4 > 0: 0 (14.0/5.0)
					* seismoacoustic = c: 0 (0.0)
					* seismoacoustic = d: 0 (0.0)
			* genergy > 197620
				* seismoacoustic = a
					* nbumps2 <= 1: 1 (16.0/8.0)
					* nbumps2 > 1: 1 (12.0/4.0)
				* seismoacoustic = b: 0 (10.0/4.0)
				* seismoacoustic = c: 0 (2.0)
				* seismoacoustic = d: 1 (0.0)
		* seismic = c: 0 (0.0)
		* seismic = d: 0 (0.0)


## SimpleCart Decision Tree

* nbumps < 1.5
	* gpuls < 1342.0
		* genergy < 16885.0
			* energy < 3500.0
				* genergy < 7295.0: 0(320.0/3.0)
				* genergy >= 7295.0: 0(431.0/0.0)
			* energy >= 3500.0: 0(30.0/3.0)
		* genergy >= 16885.0: 0(944.0/38.0)
	* gpuls >= 1342.0
		* nbumps3 < 0.5: 0(55.0/5.0)
		* nbumps3 >= 0.5: 1(10.0/10.0)
* nbumps >= 1.5
	* gpuls < 749.0
				* seismoacoustic=(c)|(a)|(d): 0(150.0/16.0)
				* seismoacoustic!=(c)|(a)|(d): 0(81.0/22.0)
	* gpuls >= 749.0
		* nbumps2 < 0.5: 0(42.0/5.0)
		* nbumps2 >= 0.5
			* gdenergy < -29.5
				* gpuls < 1201.0: 0(7.0/4.0)
				* gpuls >= 1201.0: 1(8.0/1.0)
			* gdenergy >= -29.5: 0(99.0/36.0)


