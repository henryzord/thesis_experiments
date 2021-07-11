# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| POS30 != G and POS35 != G | N | 0.377270 |
| POS30 = G and POS32 = T and POS31 = G and POS35 = G | EI | 0.173422 |
| POS30 = G and POS32 != T and POS29 = A and POS28 != G and POS28 != A and POS25 != G | IE | 0.155026 |
| POS30 = G and POS32 != T and POS29 != A | N | 0.134808 |
| POS30 != G and POS35 = G and POS31 != G | N | 0.120462 |
| POS30 = G and POS32 = T and POS31 != G and POS29 = A and POS26 != G | IE | 0.049841 |
| POS30 != G and POS35 = G and POS31 = G and POS32 = T and POS34 = A | EI | 0.047640 |
| POS30 != G and POS35 = G and POS31 = G and POS32 != T | N | 0.038328 |
| POS30 = G and POS32 = T and POS31 = G and POS35 != G and POS29 = A and POS33 != A and POS28 != A and POS23 != A and POS26 != A | IE | 0.024733 |
| POS30 = G and POS32 = T and POS31 != G and POS29 != A | N | 0.030899 |
| POS30 = G and POS32 = T and POS31 = G and POS35 != G and POS29 = A and POS33 = A | EI | 0.018655 |
| POS30 = G and POS32 != T and POS29 = A and POS28 != G and POS28 = A and POS48 != G | N | 0.017121 |
| POS30 = G and POS32 != T and POS29 = A and POS28 = G | N | 0.016615 |
| POS30 != A and POS32 != A and POS31 != A and POS35 != T | EI | 0.133367 |
| POS30 = G and POS32 = T and POS31 = G and POS35 != G and POS29 != A and POS3 != A | N | 0.007368 |
| POS30 = G and POS32 != T and POS29 = A and POS28 != G and POS28 != A and POS25 = G and POS57 != T and POS38 != A and POS55 != C | IE | 0.004825 |
| POS30 != G and POS35 = G and POS31 = G and POS32 = T and POS34 != A and POS29 != A | N | 0.005127 |
| POS30 = G and POS32 != T and POS29 = A and POS28 != G and POS28 != A and POS25 = G and POS57 != T and POS38 = A | IE | 0.003658 |
| POS30 = G and POS32 != T and POS29 = A and POS28 != G and POS28 != A and POS25 = G and POS57 = T | N | 0.005047 |
| POS30 = G and POS32 = T and POS31 != G and POS29 = A and POS26 = G and POS9 = T | IE | 0.003202 |
| POS30 = G and POS32 = T and POS31 = G and POS35 != G and POS29 = A and POS33 != A and POS28 != A and POS23 != A and POS26 = A and POS23 = T | IE | 0.002803 |
| POS30 = G and POS32 != T and POS29 = A and POS28 != G and POS28 = A and POS48 = G | IE | 0.002650 |
| POS30 = G and POS32 = T and POS31 != G and POS29 = A and POS26 = G and POS9 != T | N | 0.003713 |
| POS30 = A and POS35 != R and POS31 != N and POS32 != G | EI | 0.004373 |
| POS30 = G and POS32 != T and POS29 = A and POS28 != G and POS28 != A and POS25 = G and POS57 != T and POS38 != A and POS55 = C | N | 0.002582 |
| POS30 != A and POS32 != A and POS31 != A and POS35 != C | EI | 0.133313 |
| POS1 = C and POS2 = A and POS3 = G and POS4 = C and POS5 = T and POS6 = G and POS7 = A and POS8 = C and POS9 = T and POS10 = C and POS11 = C and POS12 = C and POS13 = A and POS14 = G and POS15 = A and POS16 = G and POS17 = T and POS18 = C and POS19 = C and POS20 = A and POS21 = C and POS22 = T and POS23 = C and POS25 = C and POS27 = G and POS28 = T and POS29 = A and POS30 = G and POS31 = G and POS32 = T and POS33 = C and POS34 = G and POS35 = G and POS36 = G and POS37 = C and POS38 = A and POS39 = G and POS40 = C and POS41 = A and POS42 = G and POS43 = G and POS44 = C and POS45 = C and POS46 = G and POS47 = T and POS48 = A and POS49 = G and POS50 = A and POS51 = A and POS52 = G and POS53 = T and POS54 = C and POS55 = T and POS56 = G and POS57 = G and POS58 = C and POS59 = A and POS60 = G | IE | 0.000917 |
| POS30 != A and POS32 = A and POS29 != C and POS28 = A | N | 0.040379 |
| POS30 != A and POS32 != A and POS31 = A and POS29 != G | IE | 0.032785 |
| POS30 != A and POS32 = A and POS29 != C and POS28 != A | IE | 0.038514 |
| POS30 != A and POS32 = A and POS29 != C and POS28 != G | IE | 0.038847 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| POS30 = C and POS31 = T | N | 0.080000 |
| POS30 = C and POS31 = C | N | 0.069454 |
| POS30 = T and POS35 = T | N | 0.067568 |
| POS30 = A and POS32 = C | N | 0.063136 |
| POS30 = C and POS31 = A and POS49 = G | N | 0.024045 |
| POS30 = T and POS35 = A | N | 0.063772 |
| POS32 = A and POS29 = G | N | 0.047619 |
| POS30 = A and POS35 = C | N | 0.045643 |
| POS32 = G and POS29 = T | N | 0.038997 |
| POS32 = A and POS29 = C | N | 0.039666 |
| POS31 = T and POS29 = T | N | 0.026798 |
| POS32 = A and POS29 = T and POS31 = A | N | 0.015692 |
| POS32 = A and POS29 = T and POS49 = A | N | 0.007908 |
| POS32 = A and POS30 = A and POS29 = A | N | 0.019190 |
| POS32 = A and POS29 = T and POS33 = G | N | 0.005764 |
| POS32 = A and POS29 = T and POS31 = G | N | 0.005047 |
| POS32 = A and POS29 = A and POS28 = G and POS31 = G | N | 0.005047 |
| POS32 = A and POS29 = A and POS28 = C and POS18 = C | IE | 0.040878 |
| POS31 = T and POS29 = G | N | 0.019956 |
| POS31 = C and POS29 = C | N | 0.025716 |
| POS32 = A and POS29 = A and POS28 = T and POS23 = T | IE | 0.025869 |
| POS31 = T and POS30 = T | N | 0.013720 |
| POS31 = T and POS30 = A and POS43 = A | N | 0.007669 |
| POS31 = T and POS30 = A and POS32 = T | N | 0.005380 |
| POS31 = T and POS29 = A and POS28 = C and POS19 = C | IE | 0.015980 |
| POS32 = A and POS29 = A and POS28 = G | N | 0.005547 |
| POS32 = A and POS29 = A and POS28 = A and POS19 = T | N | 0.004684 |
| POS32 = A and POS29 = A and POS18 = T and POS28 = C and POS25 = C | IE | 0.015332 |
| POS32 = A and POS29 = A and POS24 = T and POS23 = C | IE | 0.011966 |
| POS32 = G and POS29 = G and POS10 = G | N | 0.013492 |
| POS31 = T and POS29 = C | N | 0.006475 |
| POS31 = T and POS28 = T and POS11 = T | IE | 0.007030 |
| POS31 = T and POS28 = C and POS42 = C | IE | 0.007902 |
| POS31 = T and POS28 = C and POS42 = G | IE | 0.006157 |
| POS31 = A and POS29 = C | N | 0.028685 |
| POS32 = G and POS29 = C | N | 0.016971 |
| POS31 = A and POS29 = G | N | 0.028685 |
| POS31 = A and POS29 = T | N | 0.018519 |
| POS31 = A and POS30 = A | N | 0.008137 |
| POS31 = A and POS30 = C and POS54 = C | N | 0.006520 |
| POS31 = A and POS30 = G and POS28 = C and POS25 = C | IE | 0.055081 |
| POS32 = G and POS29 = A and POS30 = G and POS28 = C and POS21 = C and POS24 = T | IE | 0.021632 |
| POS32 = G and POS29 = A and POS30 = G and POS28 = C and POS21 = T and POS31 = G | IE | 0.021632 |
| POS32 = A and POS29 = A and POS18 = T and POS19 = C | IE | 0.014851 |
| POS32 = G and POS29 = A and POS30 = G and POS28 = C and POS24 = C | IE | 0.030214 |
| POS32 = G and POS29 = G | N | 0.011146 |
| POS31 = A and POS30 = C | N | 0.008418 |
| POS32 = G and POS30 = G and POS28 = T and POS36 = T | IE | 0.013198 |
| POS32 = G and POS30 = A | N | 0.010362 |
| POS31 = A and POS30 = G and POS28 = T and POS43 = A | IE | 0.006341 |
| POS31 = A and POS30 = G and POS28 = C and POS18 = T | IE | 0.027356 |
| POS32 = G and POS28 = G | N | 0.010702 |
| POS32 = G and POS34 = T | IE | 0.004727 |
| POS32 = G and POS34 = A and POS40 = G | IE | 0.005396 |
| POS32 = G and POS34 = A | IE | 0.004727 |
| POS32 = G and POS28 = A | N | 0.009925 |
| POS32 = G and POS42 = C | IE | 0.005207 |
| POS32 = C and POS29 = C | N | 0.018664 |
| POS31 = A and POS25 = T and POS23 = T | IE | 0.020463 |
| POS31 = A and POS19 = T | IE | 0.004969 |
| POS31 = A and POS24 = C | N | 0.007165 |
| POS31 = A and POS44 = C | N | 0.003671 |
| POS31 = A | N | 0.010154 |
| POS31 = T and POS28 = C | IE | 0.005017 |
| POS31 = C and POS29 = G and POS28 = G | N | 0.014315 |
| POS31 = C and POS29 = T and POS30 = G | N | 0.020325 |
| POS31 = C and POS30 = T | N | 0.015322 |
| POS32 = G | N | 0.007364 |
| POS32 = C and POS29 = G and POS41 = G | N | 0.007209 |
| POS32 = C and POS29 = G and POS41 = C | N | 0.006186 |
| POS32 = C and POS29 = A and POS28 = C and POS25 = T and POS24 = C | IE | 0.021454 |
| POS31 = T | N | 0.004307 |
| POS31 = C and POS30 = A and POS54 = A | N | 0.007345 |
| POS31 = C and POS30 = G and POS29 = A and POS43 = G and POS40 = A | IE | 0.019441 |
| POS31 = C and POS30 = G and POS29 = A and POS16 = T and POS24 = C | IE | 0.011029 |
| POS32 = T and POS31 = G and POS35 = G and POS34 = A and POS33 = A | EI | 0.350746 |
| POS32 = C and POS29 = G | N | 0.008288 |
| POS32 = C and POS28 = C and POS25 = C and POS16 = C | IE | 0.039246 |
| POS31 = C and POS30 = G and POS16 = T and POS24 = T | IE | 0.014493 |
| POS31 = C and POS30 = G and POS16 = C and POS12 = G | N | 0.004675 |
| POS31 = C and POS30 = G and POS16 = C | IE | 0.033493 |
| POS31 = C and POS30 = G and POS53 = C | N | 0.013974 |
| POS32 = T and POS31 = G and POS35 = G and POS30 = G and POS28 = A | EI | 0.303896 |
| POS32 = C and POS28 = C and POS44 = C | IE | 0.028513 |
| POS32 = A and POS24 = C | IE | 0.016701 |
| POS32 = T and POS31 = G and POS30 = A and POS35 = G and POS34 = A | EI | 0.085821 |
| POS32 = T and POS31 = C | IE | 0.010025 |
| POS32 = T and POS30 = A and POS29 = A | EI | 0.009630 |
| POS32 = T and POS30 = C and POS36 = T | EI | 0.052000 |
| POS30 = A | N | 0.033973 |
| POS32 = A and POS25 = T | IE | 0.012902 |
| POS32 = T and POS30 = C | N | 0.015731 |
| POS32 = A | N | 0.017638 |
| POS32 = T and POS30 = T and POS35 = G and POS1 = A | EI | 0.026374 |
| POS32 = T and POS30 = T and POS35 = G | EI | 0.018750 |
| POS30 = G and POS32 = T and POS35 = G and POS25 = G | EI | 0.260757 |
| POS30 = G and POS32 = T and POS29 = C and POS33 = G | EI | 0.128440 |
| POS30 = G and POS32 = T and POS29 = G and POS35 = G | EI | 0.112150 |
| POS30 = T | N | 0.033346 |
| POS32 = T and POS29 = T and POS36 = T | EI | 0.078125 |
| POS32 = C and POS53 = A and POS18 = C | IE | 0.032787 |
| POS32 = T and POS29 = C | EI | 0.036571 |
| POS29 = T and POS20 = C | EI | 0.024085 |
| POS29 = T | N | 0.022940 |
| POS29 = G and POS3 = C | N | 0.007256 |
| POS32 = T and POS29 = A and POS28 = G and POS35 = G | EI | 0.142857 |
| POS32 = T and POS29 = G | EI | 0.044092 |
| POS32 = T and POS28 = T and POS38 = T | IE | 0.059459 |
| POS32 = T and POS28 = G | EI | 0.056489 |
| POS32 = T and POS28 = T and POS53 = C | IE | 0.041176 |
| POS32 = T and POS28 = T | IE | 0.026835 |
| POS32 = T and POS28 = A and POS27 = C and POS3 = C | EI | 0.050725 |
| POS32 = T and POS28 = C and POS35 = G and POS24 = G | EI | 0.149351 |
| POS32 = T and POS28 = C and POS21 = T and POS35 = C | IE | 0.101351 |
| POS32 = T and POS28 = C and POS34 = A and POS21 = A and POS1 = G | EI | 0.056911 |
| POS32 = T and POS28 = C and POS34 = A and POS21 = G and POS37 = C | EI | 0.072000 |
| POS32 = T and POS28 = C and POS35 = G and POS36 = T | EI | 0.114504 |
| POS28 = C and POS32 = T and POS33 = T | IE | 0.067556 |
| POS32 = T and POS28 = C and POS23 = A | EI | 0.100840 |
| POS28 = T | IE | 0.079778 |
| POS28 = C and POS32 = T and POS33 = C and POS57 = G | IE | 0.090909 |
| POS28 = C and POS32 = T and POS17 = G and POS7 = A | EI | 0.076464 |
| POS28 = C and POS33 = G and POS24 = T | IE | 0.082737 |
| POS28 = C and POS33 = G and POS24 = A | EI | 0.084656 |
| POS28 = C and POS33 = G and POS16 = C | IE | 0.108434 |
| POS28 = C and POS32 = C and POS15 = T | IE | 0.075000 |
| POS32 = T and POS28 = C and POS33 = G and POS19 = T | IE | 0.097561 |
| POS32 = T and POS33 = A and POS55 = T | EI | 0.120715 |
| POS32 = T and POS28 = C and POS12 = C | IE | 0.058824 |
| POS32 = T and POS28 = C and POS12 = T | IE | 0.102273 |
| POS33 = A and POS14 = A | EI | 0.220000 |
| POS32 = C | N | 0.154731 |
| POS56 = A | EI | 0.113426 |
| POS33 = G | EI | 0.205433 |
|  | EI | 0.263158 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| POS29 = A and POS28 = C and POS30 = G and POS20 = T and POS24 = T and POS54 = G | IE | 0.023746 |
| POS29 = A and POS28 = C and POS24 = C and POS23 = T and POS30 = G and POS9 = C | IE | 0.021993 |
| POS29 = A and POS28 = C and POS30 = G and POS19 = T and POS26 = T and POS24 = T | IE | 0.017583 |
| POS29 = A and POS28 = C and POS24 = C and POS30 = G and POS19 = T and POS26 = C | IE | 0.018910 |
| POS29 = A and POS30 = G and POS21 = T and POS17 = T and POS28 = C and POS25 = T | IE | 0.018910 |
| POS29 = A and POS30 = G and POS21 = T and POS28 = T and POS26 = T | IE | 0.021114 |
| POS29 = A and POS28 = C and POS30 = G and POS20 = T and POS16 = T and POS18 = T | IE | 0.014473 |
| POS29 = A and POS28 = C and POS30 = G and POS31 = A and POS25 = C | IE | 0.019793 |
| POS29 = A and POS28 = C and POS30 = G and POS17 = C and POS60 = G and POS48 = G | IE | 0.011791 |
| POS29 = A and POS30 = G and POS22 = T and POS20 = T and POS21 = C | IE | 0.011343 |
| POS29 = A and POS30 = G and POS28 = C and POS34 = C and POS35 = T and POS25 = C | IE | 0.008644 |
| POS29 = A and POS30 = G and POS28 = T and POS24 = C and POS23 = T | IE | 0.011343 |
| POS29 = A and POS28 = C and POS30 = G and POS32 = G and POS24 = C | IE | 0.007289 |
| POS29 = A and POS28 = C and POS30 = G and POS33 = T and POS5 = C | IE | 0.008193 |
| POS29 = A and POS30 = G and POS28 = C and POS33 = C and POS18 = C and POS49 = C | IE | 0.007289 |
| POS29 = A and POS30 = G and POS18 = T and POS24 = T and POS28 = C and POS40 = G | IE | 0.005931 |
| POS29 = A and POS30 = G and POS28 = T and POS25 = C | IE | 0.007741 |
| POS29 = A and POS30 = G and POS28 = C and POS21 = T and POS35 = C and POS22 = C | IE | 0.004568 |
| POS29 = A and POS30 = G and POS28 = C and POS19 = C and POS6 = T and POS1 = T | IE | 0.005477 |
| POS29 = A and POS30 = G and POS22 = T and POS44 = T and POS26 = T | IE | 0.006837 |
| POS29 = A and POS30 = G and POS25 = T and POS28 = T and POS27 = C | IE | 0.004568 |
| POS29 = A and POS28 = C and POS30 = G and POS35 = A and POS1 = C and POS2 = C | IE | 0.004113 |
| POS29 = A and POS30 = G and POS28 = C and POS25 = T and POS26 = T and POS22 = C | IE | 0.004568 |
| POS29 = A and POS30 = G and POS18 = T and POS21 = T and POS17 = T and POS27 = A | IE | 0.005023 |
| POS29 = A and POS28 = C and POS30 = G and POS32 = A and POS16 = T and POS20 = C | IE | 0.003202 |
| POS29 = A and POS28 = C and POS30 = G and POS32 = C and POS31 = G and POS44 = C | IE | 0.002746 |
| POS29 = A and POS30 = G and POS26 = C and POS24 = T and POS6 = C | IE | 0.003658 |
| POS29 = A and POS30 = G and POS33 = T and POS25 = T and POS19 = C | IE | 0.002746 |
| POS29 = A and POS30 = G and POS28 = C and POS35 = A and POS21 = C and POS5 = T | IE | 0.002289 |
| POS29 = A and POS30 = G and POS22 = T and POS4 = T and POS41 = A and POS49 = A | IE | 0.002746 |
| POS29 = A and POS30 = G and POS19 = T and POS34 = G and POS43 = A | IE | 0.002289 |
| POS29 = A and POS30 = G and POS26 = C and POS24 = T and POS11 = A and POS1 = T | IE | 0.002289 |
| POS29 = A and POS28 = C and POS34 = C and POS12 = C and POS45 = A | IE | 0.001832 |
| POS29 = A and POS30 = G and POS21 = T and POS11 = T and POS48 = G | IE | 0.002289 |
| POS29 = A and POS26 = C and POS32 = G and POS13 = C and POS17 = T | IE | 0.002289 |
| POS29 = A and POS30 = G and POS31 = T and POS48 = G and POS39 = G | IE | 0.001375 |
| POS29 = A and POS28 = C and POS48 = T and POS51 = A and POS47 = G | IE | 0.002289 |
| POS29 = A and POS18 = T and POS45 = G and POS11 = C and POS33 = C | IE | 0.001832 |
| POS29 = A and POS19 = C and POS46 = C and POS23 = C and POS27 = C and POS8 = G | IE | 0.001375 |
| POS29 = A and POS28 = C and POS46 = C and POS57 = C and POS3 = C and POS51 = A | IE | 0.001375 |
| POS29 = A and POS5 = G and POS57 = A and POS38 = T and POS8 = T | IE | 0.001375 |
| POS45 = G and POS14 = C and POS29 = A and POS10 = A | IE | 0.000460 |
| POS40 = G and POS9 = T and POS8 = G and POS46 = T and POS13 = G | IE | 0.001375 |
| POS32 = T and POS31 = G and POS35 = G and POS34 = A | EI | 0.231563 |
| POS32 = T and POS31 = G and POS30 = G and POS35 = G and POS29 = A | EI | 0.061122 |
| POS31 = G and POS32 = T and POS30 = G and POS33 = A and POS34 = A | EI | 0.023591 |
| POS31 = G and POS32 = T and POS30 = G and POS35 = G and POS33 = A | EI | 0.017798 |
| POS31 = G and POS32 = T and POS30 = G and POS4 = G and POS29 = A | EI | 0.012591 |
| POS31 = G and POS32 = T and POS30 = G and POS35 = G and POS1 = A | EI | 0.006004 |
| POS31 = G and POS32 = T and POS30 = G and POS28 = C and POS35 = C | EI | 0.006667 |
| POS31 = G and POS32 = T and POS30 = G and POS7 = C and POS11 = C | EI | 0.005340 |
| POS31 = G and POS32 = T and POS29 = A and POS18 = C and POS10 = A | EI | 0.004676 |
| POS31 = G and POS32 = T and POS30 = G and POS10 = G and POS55 = A | EI | 0.003344 |
| POS31 = G and POS32 = T and POS44 = C and POS4 = C and POS30 = G | EI | 0.003344 |
| POS31 = G and POS32 = T and POS33 = A and POS42 = G and POS29 = A | EI | 0.003344 |
| POS31 = G and POS32 = T and POS40 = T and POS29 = A and POS28 = C | EI | 0.002009 |
| POS31 = G and POS41 = G and POS16 = T and POS9 = G and POS1 = G | EI | 0.002009 |
| POS31 = G and POS9 = C and POS42 = A and POS8 = G and POS3 = C | EI | 0.002009 |
|  | N | 0.996653 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

pos1|pos2|pos3|pos4|pos5|pos6|pos7|pos8|pos9|pos10|pos11|pos12|pos13|pos14|pos15|pos16|pos17|pos18|pos19|pos20|pos21|pos22|pos23|pos25|pos27|pos28|pos29|pos30|pos31|pos32|pos33|pos34|pos35|pos36|pos37|pos38|pos39|pos40|pos41|pos42|pos43|pos44|pos45|pos46|pos47|pos48|pos49|pos50|pos51|pos52|pos53|pos54|pos55|pos56|pos57|pos58|pos59|pos60|class
---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---
a|t|g|a|c|t|c|c|c|a|g|a|c|c|t|c|c|t|t|c|t|g|c|t|t|c|a|g|a|c|t|c|t|a|t|t|c|c|g|a|c|a|t|c|c|t|c|c|a|a|c|a|t|g|g|a|g|g|ei
g|g|a|g|c|c|t|t|g|g|g|a|g|g|g|g|c|a|a|t|g|g|a|c|g|t|c|a|c|t|a|t|t|c|a|t|t|c|t|a|g|t|t|c|a|g|c|a|c|t|c|t|g|g|g|a|c|t|ei
c|a|a|a|a|a|g|a|g|c|t|t|t|c|c|t|t|c|t|c|c|a|g|a|t|a|c|t|g|a|a|c|a|t|g|g|g|a|g|c|t|c|t|t|g|a|a|a|t|a|t|g|t|a|g|t|a|t|ei
t|a|c|t|g|a|t|t|t|t|c|a|t|t|t|c|t|c|t|t|t|t|t|t|c|t|a|g|a|a|t|g|t|c|t|t|g|a|t|t|g|t|g|g|a|a|g|t|a|a|g|t|t|c|a|c|a|t|ei
c|c|c|a|c|g|g|g|g|g|c|c|g|c|a|t|c|g|a|c|t|a|c|t|g|c|a|g|g|c|g|a|g|t|g|c|c|a|g|t|g|g|c|c|g|c|a|t|c|t|a|g|g|g|c|g|c|t|ei
a|t|g|g|c|c|c|c|t|t|c|c|t|c|c|t|t|t|g|c|t|g|t|c|c|c|a|g|g|a|g|a|c|a|g|t|g|t|t|g|g|a|c|a|t|g|c|t|c|c|g|g|g|a|t|g|c|c|ei
c|c|c|c|a|a|a|g|c|a|a|g|t|g|t|c|a|g|a|a|a|g|a|g|a|a|c|c|c|a|g|g|a|c|c|a|g|g|a|c|c|a|a|g|c|a|c|g|g|t|c|c|c|c|a|g|g|c|ei
g|g|a|a|t|t|g|t|c|t|c|a|g|g|g|g|a|g|c|g|g|c|c|c|t|c|c|a|g|a|g|g|t|t|a|g|a|g|c|a|c|a|g|g|c|c|c|a|g|c|t|a|a|t|a|g|g|a|ei
a|t|c|c|g|a|g|g|a|c|c|t|t|t|g|g|c|t|c|g|g|g|a|a|g|c|a|g|g|t|g|a|g|g|t|a|g|t|g|g|g|c|a|t|c|c|g|a|g|g|g|g|a|t|g|c|g|g|ei
g|c|a|a|a|c|t|c|t|c|t|g|g|c|t|t|c|t|c|t|c|t|c|t|g|c|a|g|a|t|g|a|c|g|g|c|t|g|c|c|c|g|a|a|g|c|c|c|c|c|c|g|a|g|a|t|t|g|ie
g|c|t|g|g|g|c|c|t|g|g|g|g|a|a|c|c|a|c|a|a|c|t|c|g|c|a|g|g|t|g|a|g|g|g|c|a|c|a|t|c|c|c|c|a|a|g|g|a|g|g|g|a|t|t|c|c|c|ei
g|c|t|a|c|a|c|c|t|t|g|c|g|a|g|g|g|a|g|c|t|c|c|t|t|t|c|g|g|t|a|g|g|c|c|t|g|g|g|g|a|g|a|g|t|g|g|c|a|g|g|t|g|c|t|g|c|t|ei
a|g|a|g|c|a|c|t|a|t|t|t|g|c|t|a|g|g|t|g|c|t|g|g|g|a|g|a|g|a|a|g|c|a|g|g|t|g|g|c|t|t|t|c|a|c|a|c|c|c|c|a|c|a|t|t|a|c|ei
c|c|t|g|t|c|a|t|c|t|a|t|a|t|c|a|t|g|a|t|g|a|a|a|g|c|a|g|g|t|g|c|c|t|a|c|t|g|c|g|g|g|t|g|g|g|a|g|g|g|c|c|c|c|a|g|t|g|ei
c|a|c|a|g|g|c|a|t|t|c|c|a|t|c|a|c|a|a|a|t|c|c|t|g|g|c|t|g|t|g|c|t|t|t|g|t|g|a|g|t|t|t|a|t|c|a|g|t|c|a|g|a|g|c|a|t|c|ei
t|g|a|a|g|t|g|t|c|t|a|a|t|g|c|a|t|t|a|a|c|t|t|t|t|a|a|g|g|t|a|c|t|g|a|a|t|a|c|t|t|a|a|t|a|t|g|t|g|g|g|a|a|a|c|c|c|t|ei
a|t|c|t|a|a|a|t|g|a|t|g|a|a|t|t|a|t|g|a|t|t|c|t|t|t|a|g|t|t|g|t|t|g|g|a|t|t|t|g|a|a|a|t|t|c|c|a|g|a|c|a|a|g|t|t|t|g|ei
g|g|g|g|t|g|a|a|a|g|g|g|a|c|t|c|t|c|t|g|g|c|c|a|g|t|c|a|g|g|g|g|a|g|g|g|a|a|a|g|a|c|a|t|c|c|c|c|g|a|g|a|a|g|a|t|t|c|ei
c|a|g|c|t|g|g|c|c|t|t|t|g|a|c|a|c|c|t|a|c|c|a|g|g|t|t|t|g|t|a|a|g|c|t|c|t|t|g|g|g|g|a|a|t|g|g|g|t|g|c|g|c|a|t|c|a|g|ei
g|a|c|c|t|c|t|c|c|t|t|c|t|c|t|t|c|c|t|t|c|a|c|t|g|c|a|g|a|g|g|c|t|g|g|a|a|g|a|c|g|g|c|a|g|c|c|g|c|c|g|g|a|c|t|g|g|g|ei
a|g|g|t|t|a|c|t|a|a|t|t|t|t|t|c|t|t|c|t|a|t|t|t|c|t|a|g|t|g|c|c|a|t|t|t|c|c|a|t|g|t|g|g|a|a|g|a|g|t|t|t|c|t|g|t|t|t|ei
c|a|t|g|a|a|g|c|t|t|t|g|a|g|t|g|a|a|g|c|t|c|t|c|t|g|g|g|g|a|c|a|a|t|g|t|g|g|g|c|t|t|c|a|a|t|g|t|c|a|a|g|a|a|t|g|t|g|ei
c|c|t|t|t|c|t|c|c|t|a|c|c|c|a|c|t|g|g|g|g|c|t|a|g|c|a|g|g|t|g|a|g|t|g|a|c|c|a|t|c|c|c|c|a|c|c|c|t|c|a|g|a|g|g|c|c|t|ei
g|g|c|c|t|c|t|c|c|t|t|c|t|c|t|t|c|c|t|t|c|a|c|t|g|c|a|g|a|g|g|c|t|g|g|a|a|g|a|c|g|g|c|a|g|c|c|g|c|c|g|g|a|c|t|g|g|g|ie
g|a|c|a|c|g|c|t|g|c|t|g|g|g|c|c|g|c|a|t|g|c|t|c|c|c|a|g|c|t|g|g|t|c|t|g|c|c|g|c|c|t|c|g|t|c|c|t|c|c|g|g|t|g|c|t|c|c|ei
c|t|t|g|c|c|c|c|a|c|c|g|c|a|c|c|a|c|a|c|g|g|c|c|g|c|a|g|g|t|g|a|c|t|c|c|c|g|a|g|g|g|t|t|g|g|g|g|a|t|g|a|g|t|g|a|g|g|ei
c|t|a|t|g|a|c|a|a|g|a|a|c|a|t|c|a|t|g|a|c|c|a|g|t|c|c|a|t|g|g|g|a|a|g|c|g|c|t|a|c|g|c|c|t|a|c|a|a|g|t|t|c|g|a|c|t|t|ei
g|a|t|c|c|c|c|g|g|c|c|t|g|c|c|t|g|g|g|c|c|t|g|g|c|t|t|g|g|t|g|g|g|t|t|t|g|g|t|t|t|t|g|g|t|t|t|c|c|t|t|c|t|c|t|g|t|c|ei
g|g|a|t|g|c|t|t|c|c|a|a|t|c|t|g|g|a|t|t|c|a|a|g|g|g|a|g|a|c|t|t|g|c|c|t|g|g|t|g|a|a|a|a|t|c|a|t|c|a|c|t|g|g|t|c|t|t|ei
c|c|a|a|c|t|a|g|t|t|t|t|g|a|t|t|t|t|a|c|a|t|g|t|a|t|a|g|g|c|t|g|a|a|g|g|g|a|c|t|t|g|c|c|t|t|g|t|c|t|c|a|g|a|t|g|a|g|ei
g|a|a|t|c|a|t|g|c|a|a|g|c|t|t|c|c|t|c|c|c|t|c|g|c|a|t|t|g|a|t|g|g|a|a|a|g|t|t|c|a|g|c|a|a|g|a|t|c|a|g|c|a|a|c|a|a|a|ei
c|a|g|c|t|g|a|c|t|c|c|c|a|g|a|g|t|c|c|a|c|t|c|c|g|t|a|g|g|t|c|g|g|g|c|a|g|c|a|g|g|c|c|g|t|a|g|a|a|g|t|c|t|g|g|c|a|g|ie
t|g|a|a|a|t|g|t|t|t|t|t|c|c|t|t|g|t|g|t|a|t|t|t|a|c|a|g|g|g|c|t|g|a|a|g|a|c|a|t|t|a|t|g|g|a|g|a|a|a|g|a|c|t|g|g|a|a|ei
t|g|g|c|c|c|c|t|g|a|g|t|a|t|g|c|c|a|a|a|g|c|c|c|g|g|g|a|a|g|c|t|g|a|a|g|g|c|a|g|a|a|g|g|t|t|c|c|g|a|g|a|t|c|a|g|g|t|ei
g|t|g|g|c|c|t|g|a|c|c|c|g|g|a|c|t|c|c|t|c|t|g|t|t|c|a|g|c|c|c|t|c|a|g|t|c|t|g|c|a|g|g|g|c|t|c|c|a|t|a|a|t|g|a|c|a|g|ei
t|a|g|c|t|c|c|c|t|a|t|g|c|c|a|a|g|g|g|t|g|g|c|a|a|t|t|g|g|t|a|t|g|t|t|a|t|t|a|a|g|g|g|g|t|a|c|a|t|a|t|t|t|t|c|c|a|a|ei
g|g|a|g|g|c|c|a|c|g|g|a|g|g|g|g|a|a|g|a|t|t|c|g|a|a|t|t|c|c|t|c|t|c|t|g|g|g|c|t|g|c|c|g|g|a|a|g|a|c|a|c|c|g|t|g|t|t|ei
a|g|g|c|c|t|c|a|g|g|a|t|a|a|t|c|a|t|t|t|c|t|c|c|a|c|a|g|a|c|a|t|t|c|c|c|c|a|g|c|c|t|c|a|t|g|c|a|g|a|g|c|c|c|t|g|g|g|ei
a|t|t|g|t|t|t|t|a|t|t|a|g|g|g|c|a|a|t|t|t|g|t|t|a|a|t|a|a|a|a|g|c|c|c|a|g|g|a|a|g|a|a|g|a|c|g|a|g|g|a|t|g|a|a|g|g|a|ei
t|a|t|t|c|t|g|c|c|c|a|t|t|t|g|g|g|g|a|c|a|c|t|c|c|c|g|c|c|g|c|t|g|c|c|a|g|g|a|c|c|c|g|c|t|t|c|t|c|t|g|a|a|a|g|g|c|t|ei
t|a|c|c|t|g|g|g|a|c|t|a|c|a|g|t|c|a|t|g|c|a|c|a|c|a|c|a|t|c|c|a|g|c|t|a|a|t|t|t|t|t|t|a|t|a|c|a|g|a|t|g|g|g|g|t|t|t|ei
c|c|c|c|a|g|g|c|a|a|a|c|t|t|g|c|a|c|g|a|c|g|c|t|c|c|a|g|g|t|a|a|c|c|a|g|g|a|g|t|g|g|c|g|g|c|c|c|a|t|g|c|t|g|g|g|c|a|ei
g|a|c|c|g|c|t|t|c|c|c|g|t|a|c|g|t|g|g|c|t|c|t|t|c|a|a|g|g|t|a|a|g|t|g|c|t|g|g|g|c|t|a|c|c|t|t|a|g|a|g|t|c|c|t|c|c|a|ei
a|g|c|c|a|c|t|c|a|c|t|c|t|c|t|c|c|c|g|c|g|c|g|g|a|c|a|g|g|c|a|t|c|g|t|g|c|t|g|g|a|c|t|c|c|g|g|c|g|a|c|g|g|c|g|t|c|a|ei
t|g|c|c|t|t|g|c|t|g|a|c|g|c|c|c|t|c|c|c|g|t|c|c|g|c|a|g|g|c|g|g|c|a|a|g|t|a|c|g|t|g|c|c|c|c|g|c|g|c|c|g|t|g|c|t|c|g|ei
t|c|a|c|a|g|c|c|a|c|t|c|a|g|a|t|g|c|t|t|c|c|t|c|c|c|c|c|a|g|t|g|c|c|c|a|t|t|c|c|a|g|g|t|c|a|c|c|a|g|a|t|c|c|a|a|g|g|ei
g|g|a|t|g|g|a|a|a|c|g|g|c|t|t|t|a|c|c|g|g|g|a|t|a|c|a|c|a|g|g|g|g|c|c|g|g|c|c|g|g|c|g|g|g|g|g|c|g|a|a|g|g|a|c|t|c|g|ei
a|t|t|c|a|a|a|c|a|g|c|g|c|c|t|c|a|g|a|c|t|a|c|t|a|t|t|t|g|g|t|a|c|a|a|a|c|a|a|g|a|a|t|c|t|g|g|a|a|a|a|g|g|t|c|c|t|c|ei
a|a|a|a|t|g|t|c|t|g|c|t|c|a|g|t|t|a|a|a|a|a|a|a|a|a|a|a|g|t|a|g|t|a|g|t|g|c|c|a|c|c|c|a|g|t|t|t|c|a|g|g|c|a|g|a|a|a|ei
g|t|c|t|t|g|a|g|a|c|t|g|a|a|a|g|a|t|t|t|a|g|c|a|a|a|t|g|t|a|a|a|c|t|g|c|c|t|c|a|a|a|t|t|g|g|a|c|t|t|t|g|g|g|c|a|t|a|ei
g|c|c|t|g|c|t|g|a|g|c|c|c|t|g|t|t|t|c|t|g|t|g|a|t|g|g|a|g|t|g|a|g|a|a|t|t|a|g|t|t|t|c|t|a|g|t|a|c|t|c|t|c|t|g|g|g|c|ei
t|t|g|t|a|a|c|t|t|g|a|c|a|a|g|a|a|g|t|t|a|t|c|g|t|t|c|c|a|a|a|g|t|a|c|a|a|t|g|a|t|g|g|g|g|c|a|g|g|c|a|t|a|g|g|a|t|g|ei
g|a|g|a|t|t|t|g|a|t|g|c|c|a|a|g|c|t|g|g|c|c|a|c|t|g|g|g|c|a|t|t|g|c|c|t|t|c|t|c|c|t|g|g|a|t|c|t|g|g|g|t|a|a|g|g|g|t|ei
a|c|g|c|a|g|c|t|c|a|t|c|t|c|c|a|a|c|a|t|g|g|a|a|t|g|a|t|g|t|g|c|g|a|c|c|c|c|c|g|g|g|c|c|a|a|g|g|g|t|g|g|g|g|c|t|g|g|ei
g|g|a|a|g|a|g|g|c|t|g|g|a|g|g|a|g|a|a|g|c|c|c|g|g|a|a|g|g|t|a|c|g|c|t|c|t|g|g|g|g|g|c|c|a|g|g|a|c|a|a|g|g|g|a|g|g|g|ei
c|c|a|a|a|t|g|g|t|g|a|c|t|a|c|t|c|a|c|c|t|t|t|a|g|a|t|t|a|a|a|c|a|c|a|g|a|a|c|t|g|g|a|g|a|t|g|a|a|a|t|c|a|c|g|t|a|c|ei
g|c|c|t|c|g|g|a|c|t|t|g|g|a|a|a|c|g|t|c|c|g|g|t|a|c|a|g|g|t|g|a|g|a|g|c|g|g|a|g|g|g|c|a|g|c|t|c|a|g|g|g|g|g|a|t|t|g|ei
a|a|g|c|a|a|a|g|t|g|a|t|a|t|a|t|a|t|t|t|g|t|t|a|g|a|a|a|t|g|t|t|a|c|a|t|g|t|a|g|a|a|a|a|a|t|a|c|t|g|a|t|t|t|t|a|a|a|ei
a|a|c|c|t|c|c|a|c|t|c|c|c|a|a|c|c|c|t|a|c|c|c|a|g|t|c|t|c|c|t|a|a|t|t|t|c|a|a|t|g|g|g|a|a|g|a|c|c|a|t|a|a|t|t|c|a|c|ei
t|a|c|t|a|c|a|t|t|t|t|t|c|t|a|c|a|t|c|c|t|t|t|t|t|c|a|g|g|g|t|g|t|t|g|a|t|t|g|c|c|t|t|t|g|c|t|c|a|g|t|a|t|c|t|t|c|a|ei
t|g|a|c|c|a|g|g|t|c|c|t|g|t|t|t|t|t|g|t|t|c|t|c|c|c|a|g|g|c|a|g|c|g|a|c|a|g|t|g|c|c|c|a|g|g|g|c|t|c|t|g|a|t|g|t|g|t|ei
g|c|c|a|a|t|t|c|a|a|t|t|t|c|t|t|a|a|c|c|t|a|t|t|a|a|a|g|a|t|g|g|a|g|a|t|c|a|g|t|g|t|g|a|g|t|c|c|a|a|t|c|c|a|t|g|t|t|ei
a|t|c|t|c|a|c|a|g|a|t|c|c|c|c|t|a|t|c|t|t|a|a|g|g|a|c|c|c|t|a|a|t|t|t|g|g|g|t|t|c|a|c|c|t|c|a|g|t|c|t|c|t|a|t|a|a|t|ei
a|a|a|g|a|a|a|t|c|t|t|a|g|a|t|a|a|g|a|a|g|g|t|g|g|a|a|g|g|t|a|a|g|c|c|a|t|t|c|t|g|g|g|g|c|t|a|g|g|a|t|a|t|a|t|t|t|t|ei
a|g|c|g|c|c|c|t|c|t|g|t|c|t|t|t|c|c|a|t|g|g|g|g|a|c|a|g|c|c|a|t|t|t|g|g|g|g|c|c|a|t|c|c|t|g|a|a|c|c|t|g|g|t|g|c|c|g|ei
a|c|a|t|c|c|c|a|a|c|g|c|a|t|g|c|t|c|c|t|g|g|a|c|c|a|c|a|g|c|c|t|t|c|t|g|t|g|g|t|g|t|c|a|t|t|t|c|t|g|a|a|a|c|a|a|g|g|ei
t|c|t|t|c|c|a|g|a|g|g|c|a|a|g|a|c|c|a|a|c|c|a|g|t|g|a|g|g|t|g|g|g|t|c|c|a|c|a|g|c|t|t|t|c|c|c|t|c|c|t|g|c|c|t|t|t|c|ei
g|c|g|a|g|c|c|c|g|t|g|g|t|g|a|c|c|t|g|g|g|t|g|c|c|a|g|c|t|g|t|t|c|c|t|g|g|a|c|a|t|g|a|c|t|g|a|a|g|t|c|c|t|g|c|c|c|t|ei
c|t|a|a|g|g|a|c|t|t|g|g|g|c|a|g|t|g|g|t|g|g|c|g|g|g|c|c|a|t|t|t|t|t|t|c|t|c|t|c|c|c|t|c|a|g|a|g|g|t|g|g|t|t|t|t|g|a|ei
g|a|a|t|c|c|c|a|g|c|a|g|t|t|t|c|t|t|t|c|t|g|t|t|t|g|c|g|a|g|g|a|c|a|c|a|g|a|t|t|a|t|c|c|t|t|a|t|t|t|g|g|g|t|a|c|c|a|ei
a|a|a|a|g|t|g|c|t|a|t|c|t|t|a|g|t|g|t|g|t|a|a|a|g|t|c|a|t|t|c|a|g|t|g|g|c|a|t|g|a|c|t|t|a|g|a|g|g|g|a|t|t|a|g|a|g|t|ei
a|a|t|g|t|a|c|c|a|c|t|t|a|t|t|t|t|t|g|g|t|t|t|t|t|c|a|g|c|a|c|t|t|t|t|c|t|g|t|a|g|a|a|g|g|t|c|a|g|t|t|g|g|a|a|t|t|c|ei
c|a|t|c|t|g|t|g|c|c|g|g|c|t|a|c|t|g|c|c|c|c|a|c|t|g|a|c|c|c|g|c|g|t|g|c|t|g|c|a|g|g|g|g|g|t|c|c|t|g|c|c|g|g|c|c|c|t|ei
c|a|c|t|g|g|a|g|t|g|c|t|c|a|c|a|g|t|c|t|c|c|t|g|a|g|a|g|g|a|g|c|a|c|c|a|c|c|c|c|a|g|a|c|a|t|t|a|c|t|g|g|t|t|a|t|a|g|ei
t|t|a|g|a|c|a|t|c|a|a|a|t|c|c|t|g|c|a|g|a|c|a|g|g|g|a|g|g|t|a|a|g|g|g|g|a|c|c|c|c|c|t|g|g|g|c|t|c|a|c|g|g|g|g|t|a|g|ei
c|t|g|a|c|a|t|g|c|t|t|t|c|a|t|c|t|a|g|t|t|t|c|t|g|c|t|t|c|c|t|t|c|c|t|t|t|t|c|t|g|c|a|g|t|t|t|t|c|g|c|t|t|c|a|c|a|g|ei
t|t|c|a|g|t|g|g|c|a|g|t|g|g|g|t|c|t|g|g|g|a|c|g|c|t|t|c|a|c|t|c|t|c|a|c|c|a|t|c|a|g|c|a|g|a|c|t|g|g|a|g|c|c|t|g|a|a|ei
a|t|g|g|a|c|a|g|a|c|c|c|t|t|c|c|t|c|t|t|t|g|t|g|c|c|g|g|c|a|c|a|a|c|c|c|c|a|c|a|g|g|a|a|c|a|g|t|c|c|t|t|t|t|c|a|t|g|ei
g|g|t|a|a|g|a|g|a|a|a|t|a|g|t|g|t|t|g|a|t|t|t|a|g|g|a|g|a|a|t|a|a|c|t|c|a|g|c|a|a|t|t|g|g|a|t|c|t|g|g|t|a|t|g|t|g|t|ei
c|a|t|g|c|c|t|t|g|a|a|t|t|t|c|t|t|t|t|c|t|g|c|c|a|c|a|g|g|t|c|t|g|c|c|a|g|c|t|t|a|c|a|t|t|t|a|c|c|c|a|a|a|c|t|g|t|c|ei
c|a|a|t|g|g|a|c|c|c|c|a|a|c|t|g|c|t|c|c|t|g|c|c|g|c|t|g|g|t|a|a|g|g|a|a|c|g|c|c|g|g|g|t|t|c|c|g|t|g|c|c|t|g|g|g|g|a|ei
t|t|g|g|a|a|t|c|c|a|c|c|a|g|c|t|a|c|a|t|c|c|a|c|c|c|c|t|g|a|g|g|c|a|g|g|t|a|a|t|c|c|a|t|g|a|t|g|t|t|t|t|a|c|a|t|c|c|ei
a|c|c|c|t|g|c|c|c|c|t|c|c|t|c|t|c|t|g|t|g|c|c|c|g|c|a|g|a|a|g|g|c|c|a|g|c|t|t|g|g|a|g|a|a|c|a|g|c|c|t|g|a|g|g|g|a|g|ei
t|c|c|c|c|g|t|a|t|c|t|t|a|t|c|t|c|t|g|t|c|a|c|c|c|c|a|g|c|t|g|g|t|t|c|c|t|g|c|c|c|t|g|g|a|t|g|g|c|t|g|c|c|t|g|c|g|c|ei
g|c|t|a|c|c|c|c|c|t|g|c|g|a|g|g|g|a|g|c|t|c|c|t|t|t|c|g|g|t|a|g|g|c|c|t|g|g|g|g|a|g|a|g|t|g|g|c|a|g|g|t|g|c|t|g|c|t|ei
t|a|a|t|a|g|a|a|g|a|a|c|a|t|c|c|a|a|g|g|a|g|a|a|a|g|a|g|a|c|a|g|g|c|c|c|a|a|g|a|g|a|t|g|a|a|g|a|g|t|g|a|g|a|g|g|g|c|ei
g|g|c|t|t|a|a|a|c|t|c|c|a|a|c|t|g|g|g|a|a|c|c|a|a|a|c|a|t|t|c|a|t|t|t|g|c|t|a|a|g|a|g|t|c|t|g|g|t|g|t|t|c|t|a|c|c|a|ei
t|a|a|t|c|t|t|c|c|t|t|g|t|t|t|g|c|t|t|g|t|c|t|t|t|c|a|g|g|a|a|g|t|g|a|a|t|a|a|g|a|a|g|a|t|a|a|c|a|g|t|g|t|t|t|c|a|a|ei
a|t|t|t|t|t|c|a|g|a|t|a|c|a|a|t|g|t|g|a|a|g|a|a|t|g|a|a|g|a|t|a|t|g|t|g|g|t|c|c|t|c|c|t|g|a|a|a|g|t|c|a|c|t|g|g|c|t|ei
t|g|t|c|t|c|t|a|c|a|g|a|g|a|g|c|t|t|c|a|g|g|a|a|t|t|c|c|a|g|a|c|g|a|c|a|a|a|g|c|t|g|a|a|t|g|g|a|t|t|t|g|a|g|g|t|c|t|ei
a|t|g|a|c|c|a|g|g|c|g|g|g|g|a|g|a|c|a|g|c|c|c|t|g|c|a|g|g|t|g|g|g|a|g|g|c|g|a|g|g|c|a|g|c|a|c|c|g|g|c|t|c|g|t|c|a|c|ei
a|g|g|t|g|t|a|t|g|g|g|a|c|c|c|g|c|c|a|g|c|t|g|g|a|g|g|c|c|a|a|a|g|c|g|a|t|g|t|c|c|a|a|g|g|a|g|c|t|g|t|g|a|a|a|t|a|a|ei
g|c|c|t|g|c|c|t|c|t|g|c|c|g|g|g|a|a|c|a|c|c|c|g|c|t|t|c|c|c|t|g|c|c|t|g|c|c|c|a|c|t|c|c|t|g|g|t|t|a|t|c|t|a|a|g|g|c|ei
c|a|g|c|t|g|t|c|t|c|t|g|t|c|c|c|c|a|c|c|c|a|c|c|c|c|a|g|a|g|a|a|g|c|c|a|a|g|g|c|a|t|g|c|g|t|g|g|t|g|c|a|c|g|g|c|t|c|ei
c|a|t|a|c|a|c|c|a|g|a|a|t|t|c|a|g|a|t|c|a|t|g|a|g|a|c|t|g|a|c|a|g|a|a|t|a|t|t|c|t|g|t|t|g|g|g|c|a|g|t|c|c|t|g|a|c|t|ei
g|a|c|c|c|g|c|a|g|c|t|c|a|g|c|t|a|c|a|g|c|a|c|g|t|c|a|g|g|t|g|a|g|g|a|g|c|a|c|a|c|a|a|g|g|a|g|t|g|a|t|t|t|t|t|a|a|a|ei
g|t|c|c|a|c|t|g|t|g|a|c|c|c|c|t|g|t|t|c|c|c|a|g|t|g|a|c|c|t|g|t|g|t|t|t|c|c|t|c|c|c|c|a|g|t|c|a|t|c|t|t|t|c|t|t|g|t|ei
a|a|g|a|t|a|c|c|c|a|c|a|c|a|t|t|c|c|c|g|g|g|a|a|c|a|t|g|g|t|g|a|g|t|t|t|c|t|g|c|c|c|g|g|a|g|c|c|c|c|c|g|g|a|g|c|g|g|ei
t|g|a|g|c|c|c|t|g|c|t|c|c|c|c|t|t|t|t|c|t|c|t|c|g|c|a|g|a|g|a|a|g|c|t|g|a|a|g|a|a|a|a|c|c|a|a|g|a|t|c|a|t|c|t|t|t|g|ei
g|g|g|g|c|t|t|t|c|t|c|a|t|g|g|c|t|g|t|c|c|t|t|a|g|g|t|c|t|t|c|c|t|g|a|a|a|t|g|c|a|g|t|g|g|t|g|c|t|t|a|c|g|c|t|c|c|a|ei
a|a|c|t|t|g|g|a|c|a|c|c|t|g|t|g|c|c|t|t|c|c|a|g|a|c|a|g|c|c|a|g|a|a|c|t|g|c|a|g|a|a|g|a|a|a|c|a|g|t|t|g|t|g|c|t|c|t|ei
a|c|a|g|c|t|t|a|a|a|a|g|c|c|a|t|c|c|t|t|c|c|c|a|g|c|c|t|t|g|c|c|t|c|t|g|t|c|t|g|g|a|c|a|c|c|c|a|g|g|t|c|c|a|t|a|t|c|ei
g|g|g|c|g|g|g|t|c|t|c|a|g|c|c|c|c|t|c|c|t|c|g|c|c|c|a|g|g|c|t|c|c|c|a|c|t|c|c|a|t|g|a|a|g|t|a|t|t|t|c|t|t|c|a|c|a|t|ei
c|c|c|a|g|c|a|g|c|t|g|t|c|t|g|g|c|a|t|c|a|a|c|c|g|t|c|t|t|c|t|a|t|t|a|c|t|c|c|a|c|g|a|g|c|a|t|c|t|t|c|g|a|g|a|a|g|g|ei
g|g|t|g|c|g|c|a|t|t|g|g|c|a|a|g|c|a|c|t|c|c|c|c|c|a|a|g|g|t|a|c|a|g|a|a|c|t|g|g|t|g|g|c|c|c|g|t|g|g|g|t|g|t|c|t|g|g|ei
a|g|a|c|g|a|t|g|a|c|g|a|c|g|a|t|g|g|c|t|c|t|g|g|g|g|a|c|c|t|c|a|g|g|g|g|c|t|g|c|c|g|a|g|c|t|g|g|g|g|g|g|g|c|g|c|t|c|ei
t|c|c|t|a|a|c|a|t|c|t|g|t|c|a|t|g|t|c|t|t|t|g|g|t|c|a|g|g|g|t|a|a|a|a|a|a|c|t|t|g|t|t|g|c|t|g|c|a|a|g|t|c|a|a|g|c|t|ei
g|g|g|c|c|t|g|g|c|c|c|c|c|c|c|a|t|c|t|c|t|g|t|t|g|c|a|g|g|a|c|a|a|t|g|c|c|g|t|c|t|t|c|t|g|t|c|t|c|g|t|g|g|g|g|c|a|t|ei
t|c|t|c|c|c|c|a|t|a|t|g|c|a|a|t|t|t|g|c|t|t|a|t|t|a|a|c|c|t|c|t|t|c|t|t|t|t|g|c|c|a|t|g|t|t|t|c|c|a|t|t|c|t|g|c|c|a|ei
t|c|a|a|g|g|a|c|a|c|c|g|t|c|t|a|c|a|c|g|g|a|c|t|g|a|t|g|g|t|g|a|g|c|c|a|g|g|c|c|c|g|g|g|a|g|g|g|a|g|c|t|g|c|c|c|a|g|ei
t|c|c|c|a|a|c|c|a|a|g|c|c|c|t|c|c|a|g|c|a|a|g|a|t|c|a|g|g|t|t|g|g|t|g|c|t|g|a|g|t|g|c|c|t|g|g|g|a|g|g|g|a|c|a|c|c|c|ei
g|g|g|a|c|a|g|c|c|t|c|a|c|c|c|t|t|a|a|g|c|t|a|t|c|c|t|t|c|t|c|c|c|c|t|t|t|g|c|a|g|a|c|g|a|g|a|t|g|c|a|g|c|g|a|c|t|a|ei
t|t|a|t|c|t|t|t|c|t|g|a|c|t|c|t|a|a|g|t|g|g|c|t|c|a|a|g|g|t|a|a|g|g|a|a|c|a|t|c|a|a|a|g|g|a|t|a|c|t|t|a|a|t|t|t|g|t|ei
g|g|g|c|t|g|c|g|t|t|g|c|t|g|g|t|c|a|c|a|t|t|c|t|g|c|a|g|g|t|a|t|g|g|g|g|c|g|g|g|g|c|t|t|g|c|t|c|g|g|t|t|t|t|c|c|c|c|ei
t|g|a|t|g|g|t|g|t|t|g|g|a|a|g|a|t|g|t|g|t|t|g|t|a|c|t|a|t|g|a|t|a|a|t|c|g|t|g|g|g|a|g|t|t|t|c|g|g|c|g|a|a|c|t|g|g|c|ei
c|t|g|c|a|a|a|a|g|c|t|g|g|a|a|g|a|a|g|c|a|g|a|a|a|g|c|t|g|c|t|g|g|t|g|a|g|a|g|t|g|a|g|a|g|a|g|g|t|a|t|g|a|a|g|g|t|t|ei
g|c|g|g|c|c|t|g|a|c|g|c|t|g|a|g|t|a|c|t|g|g|a|c|g|c|c|a|g|a|a|g|g|a|c|c|t|c|c|t|g|g|a|g|c|g|g|a|g|g|c|g|g|g|c|c|g|a|ei
a|g|g|a|t|g|g|c|g|a|t|c|a|g|a|a|g|c|t|g|g|a|g|a|a|t|c|a|g|t|g|a|g|t|g|c|c|a|g|g|c|t|g|g|c|c|c|c|t|g|g|g|g|c|t|g|g|g|ei
c|c|c|t|g|a|a|t|c|t|t|c|c|t|g|c|c|c|t|t|c|t|c|c|c|c|a|g|g|a|t|t|a|c|g|a|g|a|g|g|t|c|c|c|t|g|a|g|t|c|g|c|c|t|g|a|c|g|ei
a|c|c|t|t|g|g|c|c|g|t|g|c|t|c|t|t|c|c|t|g|a|c|g|t|a|g|g|t|g|t|c|c|c|c|t|a|a|c|c|t|a|g|g|a|g|c|c|a|a|c|c|a|t|c|g|g|g|ei
g|c|c|t|c|t|a|t|t|c|g|t|g|c|g|t|c|t|c|c|g|t|c|c|g|c|a|g|g|t|c|a|g|c|t|c|c|g|c|c|g|a|a|g|g|c|g|c|c|g|c|c|a|a|g|g|a|a|ei
g|g|c|t|g|g|a|c|a|g|t|g|a|a|a|t|a|t|t|a|t|g|a|c|t|g|a|a|g|a|a|a|a|g|a|t|a|g|t|c|a|g|t|c|t|g|a|t|c|a|a|g|a|a|c|c|t|g|ei
a|g|g|g|g|g|a|g|c|c|t|g|g|c|g|a|g|a|g|g|g|g|c|c|c|c|a|g|g|t|g|a|g|c|a|g|g|g|t|g|g|g|g|c|a|g|g|t|g|g|g|c|a|g|t|g|g|a|ei
c|g|t|t|a|a|t|t|t|g|t|c|t|t|c|t|t|t|t|a|t|t|c|t|a|t|a|g|a|c|t|g|a|a|t|t|t|t|g|g|a|a|g|c|a|g|t|a|t|g|t|t|g|g|t|a|a|g|ei
c|c|a|g|a|a|t|g|c|c|t|c|a|c|g|t|g|c|t|t|g|g|g|a|a|a|a|g|c|a|c|c|c|c|t|c|t|t|g|c|c|a|a|c|a|a|g|c|c|t|g|g|a|a|a|g|c|a|ei
a|c|g|t|t|t|c|a|t|g|a|a|g|t|t|t|a|t|t|t|t|g|c|t|c|c|a|g|c|t|t|c|c|a|t|a|t|t|g|g|a|t|t|c|t|t|a|c|c|a|a|t|g|t|a|c|t|g|ei
t|t|a|t|g|t|t|t|c|t|t|c|c|t|t|c|t|t|t|t|c|t|t|c|t|t|a|g|c|a|c|t|a|a|g|t|c|a|g|g|a|g|a|t|t|g|g|a|a|a|a|g|c|a|a|a|t|g|ei
t|a|c|c|a|c|t|g|c|t|g|g|t|g|a|g|c|t|g|a|a|a|g|t|c|a|t|a|t|t|c|a|t|a|a|a|t|g|t|c|a|c|a|g|t|g|t|a|g|t|g|g|t|t|a|a|g|g|ei
t|t|t|c|t|t|t|t|t|t|t|c|a|g|c|a|a|c|c|a|t|g|t|c|a|g|g|g|a|c|c|t|g|c|a|g|t|t|g|g|t|a|t|t|g|a|t|c|t|t|g|g|c|a|c|c|a|c|ei
c|c|a|g|c|t|t|c|c|a|a|g|t|g|c|c|a|c|t|g|c|a|g|g|t|a|a|t|g|t|g|a|g|t|g|a|a|t|g|c|t|c|t|t|t|a|a|g|a|a|c|t|t|t|c|c|a|a|ei
g|t|g|t|c|t|g|a|a|t|t|t|t|c|t|g|a|c|t|c|t|t|c|c|t|c|a|g|a|a|c|a|c|c|c|a|a|a|g|a|c|a|c|a|c|g|t|g|a|c|c|c|a|c|c|a|t|c|ei
g|g|c|t|g|c|c|g|g|a|g|c|c|c|c|t|c|a|c|c|c|t|g|g|t|g|g|g|g|t|a|a|g|g|a|g|g|g|g|g|a|t|g|a|g|g|g|g|t|a|c|t|g|t|g|t|c|t|ei
c|a|a|c|a|t|g|c|c|a|c|c|t|g|g|c|a|t|t|g|a|g|g|c|g|t|c|c|t|g|a|c|a|a|a|a|t|g|c|t|t|c|a|g|g|g|c|c|g|c|c|t|t|t|t|t|g|c|ei
a|a|g|a|c|t|t|c|t|g|a|g|a|a|g|t|g|g|t|t|c|a|g|a|g|g|g|t|t|t|c|a|g|a|a|c|t|c|t|g|a|g|t|a|a|a|g|t|a|a|g|g|t|c|g|g|a|c|ei
g|t|c|t|g|c|c|c|t|c|c|g|a|t|a|c|c|c|g|c|c|t|t|t|c|t|c|c|t|c|a|a|t|g|c|t|a|t|c|t|a|c|c|t|g|a|g|t|g|c|c|a|a|g|t|g|g|a|ei
c|g|t|g|g|g|a|g|t|a|c|t|g|t|g|a|t|g|t|g|c|c|c|c|t|g|c|t|g|t|a|a|g|g|g|c|t|g|g|g|c|c|c|c|g|g|c|t|g|c|c|t|c|c|c|t|g|c|ei
c|c|t|g|c|t|c|a|c|g|c|t|c|t|g|g|c|t|t|t|c|t|c|t|c|c|a|g|g|a|a|c|a|c|c|a|t|g|g|a|g|g|c|g|c|t|g|c|c|c|g|c|c|t|g|c|c|t|ei
c|a|g|c|a|a|a|a|a|g|c|t|c|c|g|c|a|a|c|a|a|g|a|a|c|a|g|g|g|t|g|a|g|t|c|g|g|g|c|c|t|t|c|c|t|c|g|g|c|c|t|c|c|g|g|g|c|g|ei
t|g|c|t|a|c|t|t|a|a|a|t|c|g|t|a|c|t|t|c|t|c|t|a|g|a|a|g|g|t|g|a|g|g|a|g|g|a|a|g|g|g|g|a|c|a|a|g|a|t|g|a|c|a|t|a|g|a|ei
t|t|c|g|a|g|g|c|t|c|t|g|g|a|g|t|c|c|t|c|c|a|c|g|t|a|c|g|g|t|g|a|g|c|c|t|g|g|g|c|t|g|c|t|c|g|g|a|c|g|g|t|g|c|c|g|g|g|ei
a|t|t|a|a|t|t|t|c|t|a|a|t|t|t|c|t|t|t|t|t|t|t|c|c|t|a|g|a|a|c|t|g|t|t|a|c|t|a|a|a|c|t|g|a|g|t|c|a|g|a|a|g|t|t|t|a|c|ei
a|t|a|c|c|t|g|t|a|g|t|g|t|t|c|a|t|t|g|g|c|a|t|g|g|t|t|g|t|t|g|a|c|t|c|t|t|t|g|g|c|c|a|a|t|a|t|g|g|c|g|t|t|t|a|t|a|t|ei
g|g|g|t|a|c|c|g|g|t|t|g|c|c|c|c|c|t|c|c|t|g|t|g|c|t|g|c|c|c|t|g|c|c|c|c|t|c|t|g|t|a|t|g|a|g|c|t|c|a|t|g|a|a|g|a|a|c|ei
a|c|c|t|t|c|t|c|t|g|c|t|g|t|t|c|c|t|c|t|t|t|t|c|a|c|a|g|g|a|g|t|a|c|c|t|c|t|c|t|c|t|a|g|a|a|c|t|g|t|a|c|g|c|t|g|t|a|ei
g|c|a|t|c|a|a|c|g|t|g|t|a|c|t|a|c|a|a|t|g|a|g|c|a|c|c|g|g|t|g|a|g|g|c|c|c|c|g|g|c|c|c|c|t|t|c|c|c|c|g|a|c|c|g|c|c|t|ei
c|t|g|a|t|g|a|g|g|c|t|g|g|c|c|t|g|t|c|t|t|t|t|t|a|t|a|g|t|g|a|t|c|t|g|c|a|g|a|g|a|t|g|a|a|a|a|a|a|c|g|c|a|g|a|t|g|a|ei
g|t|g|c|c|t|g|a|a|t|t|t|t|c|t|g|a|c|t|c|t|t|c|c|t|c|a|g|a|g|c|c|c|c|c|a|a|a|g|a|c|a|c|a|c|g|t|g|a|c|t|c|a|c|c|a|c|c|ei
g|d|g|a|c|g|g|g|g|c|t|g|a|c|c|g|c|g|g|g|g|g|c|g|t|c|c|a|g|g|g|t|c|t|c|a|c|a|c|c|c|t|c|c|a|g|a|a|t|a|t|g|t|a|t|g|g|c|ei
c|a|c|a|a|c|t|t|g|t|t|t|g|a|c|g|a|c|g|a|a|a|a|a|a|g|c|c|c|a|g|t|t|t|g|t|t|c|a|t|g|t|c|a|g|t|g|a|g|a|g|c|t|t|c|c|c|a|ei
c|c|a|c|c|c|t|c|c|a|g|c|c|c|c|c|a|g|c|t|c|c|t|c|g|c|a|g|a|c|a|a|g|c|t|g|g|t|g|t|c|t|a|g|g|a|a|c|t|a|c|c|c|g|g|a|c|c|ei
g|g|g|t|c|t|t|c|g|c|c|c|a|g|g|t|g|g|c|c|g|g|c|c|t|c|a|g|g|t|g|a|g|t|g|g|c|a|c|c|a|g|c|c|c|c|t|g|g|a|a|g|c|c|c|g|g|g|ei
g|t|g|t|a|g|c|c|g|c|t|t|c|t|c|t|a|t|a|c|g|g|g|t|c|c|a|g|g|t|a|a|g|g|a|g|a|g|a|g|c|a|g|g|g|a|t|t|g|g|g|g|g|c|c|t|g|g|ei
t|t|c|t|c|c|a|t|t|t|c|t|t|t|c|t|t|g|g|g|g|t|c|c|g|c|a|g|g|t|a|c|g|a|g|c|g|a|a|a|c|a|t|t|g|a|a|a|a|g|a|t|a|t|c|c|a|t|ei
t|g|g|g|c|c|t|c|c|t|a|t|t|c|c|c|t|g|g|a|g|t|a|g|g|a|a|g|g|t|a|a|g|a|g|g|g|c|t|g|g|g|g|t|g|g|c|c|g|g|a|g|g|a|a|g|g|g|ei
c|c|c|c|t|c|t|t|t|c|a|a|t|g|t|c|a|g|c|c|t|t|c|g|c|a|a|g|t|g|g|g|g|a|a|a|g|a|g|c|a|t|t|g|c|t|t|g|g|c|t|c|c|a|t|t|g|c|ei
g|c|a|c|c|a|g|c|t|g|t|t|g|t|g|g|g|c|t|g|g|c|c|t|t|c|c|c|c|t|t|c|t|c|a|c|c|c|t|g|t|g|t|g|g|g|t|c|t|t|g|a|c|a|c|c|t|t|ei
g|g|g|c|a|g|t|g|g|c|c|c|t|g|a|c|c|g|a|g|a|c|c|g|g|c|t|g|g|t|g|a|g|t|g|c|g|g|g|g|t|c|a|g|g|c|a|g|g|g|a|a|a|t|g|g|c|c|ei
a|g|g|a|c|a|g|c|a|a|t|g|g|t|t|g|t|a|t|c|a|a|c|a|g|a|a|g|g|t|a|a|g|a|g|g|t|g|a|a|c|t|g|c|g|c|t|t|t|c|t|c|a|g|a|g|a|a|ei
a|g|c|c|g|c|t|a|a|t|c|c|a|g|g|a|g|a|g|g|g|g|a|g|t|g|g|a|c|a|g|g|a|g|a|c|a|c|t|t|t|g|g|a|t|t|g|g|g|a|c|t|g|c|a|g|g|g|ei
c|c|c|g|g|c|c|g|g|a|t|g|t|t|a|c|c|g|a|g|a|g|c|a|a|g|c|g|g|t|g|a|g|t|g|c|c|g|c|g|g|g|g|t|g|g|c|c|c|c|c|t|g|a|g|g|g|g|ei
t|g|c|t|g|a|a|a|a|c|a|c|a|t|g|a|c|t|t|c|t|t|t|t|t|c|a|g|g|c|t|a|t|t|a|g|t|t|c|g|t|t|a|c|a|c|c|a|a|g|a|a|a|g|t|a|c|c|ei
t|c|a|t|a|a|a|a|c|t|a|t|a|a|c|t|c|t|t|t|a|t|c|t|a|a|t|t|a|g|a|a|a|t|g|t|t|t|t|t|t|t|t|t|t|t|g|a|g|a|c|a|a|g|g|t|c|t|ei
c|t|t|c|a|a|a|g|c|t|g|a|g|a|a|g|a|a|a|t|c|t|g|a|a|a|c|a|a|t|g|c|t|g|a|g|t|g|g|g|t|t|t|a|t|c|a|a|g|g|g|g|c|c|a|t|t|a|ei
g|g|a|a|c|c|c|c|a|c|a|g|t|g|g|a|g|g|t|g|g|a|t|t|t|a|t|a|c|t|g|c|c|a|a|a|g|g|t|c|t|t|t|t|c|c|g|g|g|c|t|g|c|a|g|t|g|c|ei
t|t|c|a|g|g|g|g|a|a|a|a|a|a|a|t|a|t|c|t|t|c|t|g|c|a|a|g|g|t|a|a|c|a|c|a|c|t|c|t|g|t|a|a|a|t|g|c|a|t|g|t|t|c|a|t|g|c|ei
t|t|t|t|t|t|g|a|c|a|g|g|g|c|c|t|g|g|c|t|c|t|g|t|c|t|c|a|g|g|c|t|g|g|a|g|t|c|a|g|t|g|g|c|a|t|g|a|t|c|t|c|t|g|c|t|c|a|ei
g|a|g|a|t|t|g|a|g|c|t|g|c|a|g|t|c|c|c|a|g|c|t|a|c|a|t|g|g|t|a|g|g|a|a|t|a|g|t|g|c|c|a|g|g|a|a|g|g|g|t|g|g|t|g|c|a|c|ei
c|t|c|t|c|t|t|c|t|a|c|c|t|t|a|a|a|a|t|g|t|a|a|a|a|a|a|a|a|t|g|t|a|a|t|g|a|t|c|a|t|a|a|g|t|c|t|a|a|a|t|a|a|a|t|g|a|a|ei
a|a|a|g|a|a|g|a|g|a|g|a|t|a|a|g|t|c|c|a|g|c|t|a|g|a|g|t|c|t|g|t|g|t|t|a|t|g|g|g|a|t|a|a|t|c|g|g|a|a|t|t|t|g|t|a|c|a|ei
t|g|a|c|a|a|a|a|t|t|g|g|a|a|t|g|t|t|c|t|t|t|c|g|c|a|a|t|g|g|c|a|a|c|a|t|t|t|t|t|c|a|c|t|g|g|g|t|t|t|a|t|a|g|t|a|g|g|ei
a|a|g|c|t|g|c|a|c|g|t|g|g|a|t|c|c|t|g|a|g|a|a|t|c|a|g|g|g|t|g|a|g|t|c|c|a|g|g|a|g|a|t|g|c|t|t|c|a|c|t|t|t|t|c|t|c|t|ei
c|a|g|a|a|g|g|g|c|g|t|g|a|a|g|a|a|c|c|g|g|g|a|c|c|a|t|c|c|a|c|a|t|c|t|c|t|g|a|c|t|g|g|c|t|g|c|c|a|a|c|a|c|t|c|g|t|g|ei
g|t|a|c|c|g|c|a|t|g|c|a|c|a|a|g|t|c|c|c|g|g|a|g|a|c|a|g|c|c|a|g|t|g|t|g|t|c|c|g|a|a|t|g|a|g|g|c|a|c|c|t|c|t|c|t|c|a|ei
a|a|a|g|t|c|g|g|a|g|c|t|g|t|t|t|a|c|c|c|c|c|a|t|t|a|a|t|a|g|g|g|g|t|t|c|a|a|t|a|t|a|a|a|a|a|g|c|c|g|g|c|a|g|a|g|a|g|ei
a|t|g|c|c|a|c|g|t|g|c|t|c|c|a|c|g|a|t|c|g|g|c|t|g|c|c|c|a|c|t|a|c|c|t|c|a|c|c|t|t|c|g|a|c|g|g|g|c|t|c|a|a|a|t|a|c|c|ei
a|a|g|c|t|g|a|c|a|g|t|g|g|a|c|c|c|g|g|t|c|a|a|t|c|a|a|g|g|t|g|a|g|c|c|a|g|g|a|g|t|c|g|g|g|t|g|g|g|a|g|g|g|t|g|a|g|a|ei
a|a|g|c|a|c|a|c|c|a|c|g|g|a|t|c|t|a|g|a|t|g|c|a|t|a|a|a|g|t|g|a|g|t|t|c|a|a|a|t|a|t|c|c|c|a|c|t|t|c|t|g|a|t|t|t|g|c|ei
c|c|t|a|a|t|a|a|a|t|a|c|a|a|a|g|g|g|c|t|g|t|a|a|g|c|t|c|a|g|g|g|c|c|c|t|t|g|t|t|c|c|c|t|a|g|a|a|g|a|a|a|g|g|a|g|c|c|ei
g|g|c|t|c|t|c|a|g|c|c|c|t|t|c|t|g|t|t|t|t|c|a|g|c|c|a|t|c|a|t|g|g|a|g|a|a|a|c|t|g|g|a|g|a|t|g|t|c|c|a|a|g|t|t|c|c|a|ei
g|c|t|g|t|g|a|t|g|a|g|t|t|g|a|t|a|c|c|a|g|a|g|a|c|t|c|a|g|t|g|a|g|t|a|t|c|t|c|c|t|t|g|g|c|c|t|a|a|t|t|t|a|g|t|t|g|g|ei
g|c|a|g|a|g|g|a|g|c|t|g|a|a|g|a|a|g|g|a|g|c|a|g|c|a|c|c|a|g|c|g|c|c|c|a|c|c|t|g|g|a|g|c|g|c|a|t|g|a|a|g|a|a|g|a|a|c|ei
a|c|a|c|c|t|t|c|a|a|c|a|g|c|t|a|c|t|a|t|a|t|g|a|t|g|g|g|t|g|c|g|a|c|a|g|g|c|c|c|c|t|g|g|a|c|a|a|g|g|g|c|t|t|g|a|g|t|ei
c|g|c|t|t|c|c|t|c|g|t|c|c|g|c|c|c|c|t|a|a|g|t|g|g|a|a|g|g|t|t|c|c|t|t|g|c|g|g|t|t|c|g|c|g|g|c|g|t|g|c|c|g|g|a|c|g|t|ei
g|a|g|t|g|a|a|a|a|t|a|a|t|a|t|t|c|a|g|a|c|a|a|t|t|t|g|c|a|g|t|t|a|c|t|g|a|a|g|a|a|t|t|t|c|a|g|c|c|t|g|t|t|t|a|c|a|a|ei
g|g|c|a|g|t|g|g|c|g|g|c|g|g|c|g|a|a|g|g|t|g|g|g|c|g|g|c|t|c|g|g|c|c|a|g|t|a|c|t|c|c|c|g|g|c|c|c|c|c|g|c|c|a|t|t|t|c|ei
c|t|g|g|t|g|t|g|c|t|c|t|c|t|g|g|t|g|a|t|c|a|a|a|a|c|a|g|g|t|a|g|g|t|c|a|t|c|a|t|c|g|c|a|g|c|a|t|c|t|t|t|c|t|t|a|g|t|ei
t|a|c|a|a|t|g|c|t|c|a|t|a|a|c|a|t|a|a|a|a|a|a|c|a|a|c|a|t|a|a|c|a|t|c|a|a|a|t|a|a|a|a|t|a|t|a|t|g|a|t|t|c|t|g|a|t|a|ei
t|c|a|g|c|t|t|c|t|t|t|g|a|a|a|t|t|g|g|g|c|c|a|g|c|c|g|a|t|c|c|c|c|t|g|g|t|t|c|a|t|g|g|t|g|g|c|t|g|a|g|t|t|t|t|t|c|a|ei
c|a|a|c|c|c|a|g|c|t|a|t|g|g|t|t|c|t|c|t|c|g|c|a|g|g|a|a|g|t|c|c|t|t|g|c|a|a|g|c|t|a|a|t|t|c|t|t|t|g|a|c|c|t|g|t|t|g|ei
a|a|g|g|a|a|c|t|g|t|g|t|t|t|g|a|t|g|c|c|t|t|c|c|g|a|t|c|a|g|g|t|g|g|c|c|a|t|c|c|a|g|c|t|g|a|a|t|g|a|t|a|c|t|c|a|c|c|ei
a|a|c|t|a|t|a|t|t|g|c|g|g|a|c|a|t|t|g|a|g|g|t|g|c|g|g|c|a|a|g|c|a|g|g|t|g|g|a|g|c|t|g|g|c|t|c|t|g|t|g|g|g|a|c|a|c|a|ei
c|t|g|c|c|t|t|c|g|a|g|g|g|c|c|g|g|a|a|c|t|g|t|a|a|c|g|c|g|t|a|a|g|g|c|c|c|c|a|c|t|t|t|g|g|g|t|c|c|c|a|t|a|t|t|t|g|c|ei
c|c|a|c|c|c|t|c|c|a|g|c|c|c|c|c|a|c|c|t|c|c|t|c|g|c|a|g|a|c|a|a|g|c|t|g|g|t|g|t|c|t|a|g|g|a|a|c|t|a|c|c|c|g|g|a|c|c|ei
t|c|t|t|c|c|t|c|a|c|c|c|t|g|t|c|c|g|t|g|a|c|g|g|a|t|t|g|g|t|g|a|g|a|g|g|g|g|c|c|a|t|g|g|t|t|g|g|g|g|g|g|a|t|g|c|a|g|ei
c|t|g|a|g|g|c|a|c|t|c|t|t|c|c|a|g|c|c|t|t|c|c|t|c|t|g|g|g|t|g|a|g|t|g|g|a|g|a|c|t|g|t|c|t|c|c|c|g|g|c|t|c|t|g|c|c|t|ei
g|g|a|c|c|c|t|a|a|g|c|t|c|c|a|g|a|t|g|g|g|c|a|g|a|g|c|t|c|c|c|g|c|t|c|c|a|c|c|t|c|a|c|c|c|t|g|c|c|c|c|a|g|g|c|c|t|t|ei
g|c|c|a|g|a|g|a|c|c|a|g|g|a|t|t|t|g|g|c|t|a|c|g|g|g|c|a|g|a|g|c|g|t|c|c|g|a|c|t|a|t|a|a|a|t|c|g|g|c|t|c|a|c|a|a|g|g|ei
a|g|g|a|a|a|a|a|g|a|g|g|a|a|g|g|g|a|g|g|g|a|g|g|g|g|a|a|g|g|a|a|g|g|a|a|a|g|a|a|g|g|a|a|g|g|a|a|g|g|g|a|g|a|g|a|g|a|ei
a|g|a|t|c|t|t|c|c|g|g|c|c|g|g|a|c|a|a|c|t|t|c|t|t|t|c|g|g|t|g|a|g|c|c|g|t|g|g|c|t|g|g|g|g|a|c|t|g|g|g|c|g|g|c|g|g|c|ei
t|g|t|c|c|c|t|c|t|a|c|g|c|c|t|c|c|g|g|a|a|g|g|c|a|c|c|g|g|t|g|a|g|t|g|c|c|c|g|c|t|g|g|c|c|c|c|c|a|g|t|c|c|c|c|t|c|g|ei
g|g|t|a|t|t|t|g|t|g|t|a|t|c|t|a|a|a|c|a|t|a|g|a|a|g|g|t|a|c|a|g|t|g|a|a|a|a|t|a|c|a|g|t|a|t|t|a|t|a|a|c|c|t|t|a|t|g|ei
g|a|g|a|g|a|g|c|c|c|c|a|g|a|c|t|g|a|g|g|g|a|a|c|t|g|g|a|t|g|g|a|t|g|g|a|g|a|a|g|g|a|t|g|c|c|t|c|g|c|t|g|g|g|g|a|c|t|ei
t|c|t|c|a|t|t|t|t|c|g|t|t|t|c|a|t|c|t|c|t|c|a|c|a|c|t|c|t|g|g|g|g|t|g|g|c|a|t|t|a|t|t|a|t|t|c|c|c|a|c|t|t|t|t|c|a|g|ei
a|c|c|a|a|g|a|a|g|g|g|a|t|c|t|a|t|c|a|c|c|t|c|g|a|c|a|g|g|t|a|a|g|a|a|a|a|a|t|t|a|c|a|t|a|g|a|t|g|a|a|g|a|t|c|t|g|a|ei
t|c|c|c|c|g|c|g|t|t|c|c|a|t|g|c|g|c|a|c|a|g|g|a|a|g|g|g|g|t|g|a|g|t|c|c|g|c|g|t|c|c|c|t|g|g|c|a|c|g|g|a|g|c|g|g|g|g|ei
c|c|c|t|c|g|t|g|c|g|c|t|c|c|a|c|g|a|c|c|a|a|g|c|a|g|c|g|g|t|g|a|g|c|c|a|c|g|g|g|c|a|g|g|c|t|g|g|g|g|t|c|g|t|g|g|g|g|ei
g|g|g|g|g|a|g|t|t|c|c|g|g|g|c|g|g|t|g|a|c|g|g|g|t|g|g|g|g|c|g|g|c|c|t|g|a|t|g|a|g|g|a|c|t|a|c|t|g|g|a|a|c|a|g|c|c|a|ei
a|g|g|a|a|c|a|a|a|g|a|a|g|t|g|a|c|t|t|g|g|g|a|g|a|c|t|a|g|a|a|g|g|a|g|a|g|g|t|g|g|a|a|a|a|a|g|a|a|g|c|a|c|t|g|a|a|g|ei
c|t|t|t|g|g|c|a|c|c|g|g|c|g|a|c|g|g|c|c|t|t|g|g|c|c|g|t|g|a|c|t|t|t|t|c|c|t|c|t|c|a|g|g|c|c|t|t|g|t|t|c|t|c|t|g|c|t|ei
a|c|c|t|g|c|g|a|g|a|t|t|g|a|c|g|c|c|c|t|c|a|a|g|c|a|c|t|g|t|g|a|g|t|c|c|c|t|g|c|c|c|a|c|c|t|g|g|g|c|c|a|g|g|c|c|c|t|ei
a|a|c|c|a|a|c|t|g|t|t|a|c|a|a|t|c|a|a|g|g|t|c|a|g|a|a|g|g|t|a|a|t|t|a|c|c|t|t|a|a|g|t|t|t|g|g|t|t|a|a|t|a|t|c|a|t|g|ei
t|g|g|g|g|g|t|g|t|c|t|g|g|g|c|t|a|c|a|g|a|a|g|g|t|c|a|g|g|t|a|a|t|g|c|a|c|a|t|t|c|c|t|g|a|t|g|t|t|g|c|c|a|g|g|a|a|t|ei
c|t|g|c|c|c|t|c|a|t|g|c|c|c|t|c|g|c|g|t|c|t|t|c|c|c|a|g|g|a|g|t|g|c|a|t|c|c|g|g|g|c|c|t|g|c|a|a|g|c|c|c|g|a|c|c|t|c|ei
a|c|a|a|a|g|a|a|t|g|g|a|a|a|a|g|t|c|a|g|a|g|g|a|g|a|a|c|t|t|g|a|c|a|g|t|t|t|t|t|g|g|t|g|g|c|a|c|g|g|t|a|a|c|a|g|c|c|ei
a|c|t|c|a|t|c|g|a|a|c|t|c|t|g|c|t|g|a|t|a|g|c|a|t|g|a|g|g|t|a|a|t|t|t|t|c|t|t|t|a|t|g|a|t|t|c|c|t|a|c|a|g|t|c|t|g|t|ei
c|t|a|c|a|g|c|a|g|c|a|g|c|t|t|c|t|g|c|a|c|a|c|t|a|c|c|g|g|t|c|a|g|t|c|c|c|t|g|c|c|c|c|c|t|g|c|a|g|t|c|c|t|g|t|c|c|a|ei
a|a|t|t|a|t|c|g|g|a|a|g|c|a|g|t|g|c|c|t|t|c|c|t|a|t|t|a|t|g|a|c|a|g|t|t|a|t|a|c|t|g|t|c|g|g|t|t|t|t|t|t|t|t|a|a|a|t|ei
a|g|c|a|g|c|a|g|g|g|c|a|c|t|c|a|g|c|g|a|g|g|g|a|a|t|c|t|t|g|c|c|c|a|g|t|g|c|t|g|a|t|g|g|g|a|c|a|t|g|g|t|a|t|c|t|c|c|ei
c|a|c|t|a|g|a|a|a|g|a|t|a|g|g|a|c|a|c|t|g|g|a|g|t|g|g|g|a|a|g|c|c|c|t|a|g|c|a|g|t|t|t|c|t|t|c|c|a|g|g|g|t|g|g|g|c|t|ei
c|a|c|t|c|c|a|c|c|t|c|c|c|c|t|c|t|g|c|t|t|g|c|c|t|c|a|g|a|t|g|g|c|t|g|c|c|g|c|a|c|g|c|c|t|c|t|g|c|c|t|c|t|c|c|c|t|g|ei
c|g|c|c|c|t|c|c|t|c|c|c|t|t|g|t|t|t|a|g|a|a|t|g|c|t|t|c|g|t|c|g|t|c|a|t|g|a|t|a|a|a|c|c|c|g|t|t|c|t|g|t|g|t|c|c|c|c|ei
a|g|a|c|c|c|c|a|t|c|t|c|t|t|a|a|a|a|a|a|t|g|a|t|t|g|g|c|c|a|g|a|c|a|c|a|g|g|t|g|c|c|t|c|a|c|g|c|c|t|g|t|a|a|t|c|c|c|ei
a|a|t|g|t|c|g|g|t|c|t|t|t|t|t|t|t|g|t|g|a|t|t|t|c|t|a|g|t|t|a|t|c|t|c|c|a|g|a|a|g|a|a|g|a|a|g|a|g|a|a|a|a|g|g|a|g|a|ei
c|a|a|c|c|t|a|g|a|a|a|t|c|a|c|a|g|a|a|g|g|c|g|c|c|t|g|a|c|c|t|t|c|a|g|t|g|c|c|t|c|a|g|c|t|c|c|a|g|c|g|c|c|a|t|g|g|c|ei
t|t|t|c|c|a|c|c|c|t|c|a|t|g|c|c|c|c|c|t|c|t|c|c|t|c|a|g|t|t|t|g|t|c|a|g|g|a|a|a|t|c|a|g|t|a|c|a|t|t|g|t|g|t|g|a|t|a|ei
a|c|a|t|a|a|c|a|g|g|g|a|a|a|g|c|t|g|g|a|g|c|c|c|c|t|g|g|a|c|c|t|t|c|t|g|g|t|a|g|a|g|a|a|c|a|t|g|g|g|a|c|g|t|g|t|g|a|ei
t|a|a|g|a|g|t|a|a|a|a|c|t|c|a|g|c|a|g|g|g|a|c|c|t|g|c|c|c|c|a|c|a|c|t|c|a|g|g|a|a|t|g|g|a|a|g|a|g|g|c|a|a|t|g|c|c|t|ei
a|t|a|a|g|c|a|t|t|g|c|c|t|g|g|t|t|a|c|t|g|t|g|a|a|a|g|g|g|c|t|c|c|t|a|c|t|a|t|c|c|t|g|g|t|t|c|t|g|g|a|a|t|t|g|c|t|c|ei
g|a|g|a|a|a|g|g|a|t|t|c|c|a|g|a|g|g|c|t|a|g|c|c|a|a|a|a|c|c|a|t|c|c|c|a|g|g|t|c|a|t|t|c|t|t|c|a|t|c|c|t|c|a|c|c|c|a|ei
c|t|c|c|a|t|g|g|t|t|a|c|t|g|g|g|t|a|c|c|c|c|c|c|c|c|a|g|c|g|c|t|g|a|g|t|a|c|c|c|a|g|a|c|c|t|c|c|g|a|a|a|g|c|a|c|a|a|ei
g|c|g|g|c|g|c|a|g|a|a|c|c|c|t|g|a|g|g|a|g|g|t|g|g|g|a|g|g|t|g|a|g|c|g|c|c|g|g|g|c|t|g|g|a|c|t|c|c|a|g|g|a|g|t|g|g|g|ei
g|g|a|c|a|t|t|c|g|a|a|c|a|g|a|g|t|t|c|a|a|g|a|g|a|t|t|a|t|g|g|c|t|a|t|t|c|c|c|t|a|t|a|t|t|c|a|g|c|a|a|t|t|a|a|a|t|c|ei
g|g|t|c|t|a|g|t|g|c|c|c|a|t|t|t|a|c|t|c|t|g|g|c|c|c|g|g|g|t|a|a|g|t|g|g|g|c|t|c|a|c|g|c|c|t|g|c|c|t|g|g|g|g|c|t|c|t|ei
g|c|c|a|t|t|g|c|a|c|t|t|t|a|t|a|g|t|c|t|g|a|t|a|a|a|a|a|c|g|t|g|c|a|a|t|t|c|a|g|g|a|g|c|c|c|a|g|c|a|g|t|g|a|c|a|c|a|ei
c|t|g|g|c|t|c|c|c|c|t|c|c|t|g|c|c|t|c|g|a|g|a|g|g|c|a|g|g|g|c|t|t|c|t|c|a|g|a|g|g|c|t|t|g|g|c|g|g|g|a|a|a|a|a|g|a|a|ei
g|c|g|g|c|t|g|g|g|a|g|g|g|c|c|g|c|t|t|c|t|g|c|a|c|g|c|g|g|t|g|a|g|g|g|g|g|a|g|a|g|g|t|g|g|a|t|g|c|t|g|g|c|g|g|g|c|g|ei
a|g|t|a|t|g|t|t|c|t|g|c|a|t|g|c|t|t|c|c|c|a|a|g|c|a|g|c|t|c|c|g|a|g|c|c|t|g|g|c|t|g|t|c|t|g|t|c|c|c|a|c|a|t|t|c|c|t|ei
t|c|t|a|c|c|g|c|a|t|c|g|a|c|c|a|c|t|a|c|c|t|g|g|a|a|g|g|a|g|a|t|g|g|t|g|c|a|g|a|a|c|c|t|c|a|t|g|g|t|g|c|t|g|a|g|a|t|ei
t|a|c|c|a|a|c|t|g|c|a|g|a|g|c|c|a|g|g|a|a|a|a|t|t|g|a|a|g|c|c|t|t|c|a|t|g|a|a|g|g|c|a|a|t|c|g|g|t|c|t|g|c|c|g|g|a|a|ei
t|t|a|t|a|a|c|t|t|g|g|g|c|t|t|g|g|t|c|t|t|c|t|t|a|c|a|g|t|c|t|t|g|g|t|g|a|t|g|c|c|t|t|g|g|a|c|a|g|c|a|g|c|a|a|c|t|c|ei
t|t|c|a|g|c|a|c|a|t|c|t|g|g|a|c|t|c|t|t|t|a|a|t|c|t|t|a|a|a|g|a|t|c|a|g|g|t|t|c|t|g|a|a|g|g|g|t|g|a|t|g|g|a|a|a|t|t|ei
g|c|c|c|a|g|c|t|a|a|t|t|t|t|t|g|a|a|a|a|c|a|g|g|c|t|t|t|c|t|a|t|g|t|t|g|c|c|c|a|g|g|c|t|g|g|t|c|t|c|a|a|a|c|t|c|c|t|ei
g|c|c|a|t|g|g|a|a|a|a|g|c|a|c|c|a|g|a|a|g|c|g|g|c|a|a|a|g|a|t|g|a|a|a|a|t|g|g|a|g|c|t|g|t|t|t|g|t|g|c|a|a|c|a|g|a|c|ei
t|g|g|g|a|a|g|a|a|t|g|t|t|t|c|c|a|g|c|t|c|c|a|a|t|g|c|t|a|a|a|t|c|t|c|t|a|a|g|t|c|t|g|t|g|g|t|t|g|g|c|a|g|c|c|a|c|t|ei
g|a|a|g|c|a|a|a|t|c|c|c|c|g|g|a|g|a|g|g|c|a|a|a|g|a|g|g|t|t|c|a|g|a|a|g|g|a|a|t|g|c|g|g|c|t|t|c|c|t|t|c|c|c|t|g|g|g|ei
c|t|c|g|a|g|a|t|a|a|g|c|t|t|g|c|t|g|c|a|t|g|t|t|g|a|a|g|g|t|g|a|g|c|a|a|c|t|g|a|c|a|c|g|g|g|t|t|t|g|g|g|g|a|g|c|a|g|ei
t|t|a|g|t|t|c|a|c|t|c|a|a|c|t|t|a|t|g|g|a|g|t|g|a|t|g|a|a|a|a|a|a|a|c|t|g|t|a|a|a|g|c|c|a|a|t|t|t|t|c|a|t|t|a|c|t|a|ei
c|c|a|c|c|a|c|a|c|t|g|c|a|t|g|t|g|g|c|t|c|c|c|a|g|g|c|a|c|a|g|c|c|a|t|g|g|c|t|g|t|c|a|g|t|a|c|c|t|t|c|c|g|a|a|a|g|c|ei
a|g|a|t|g|a|a|t|t|a|a|g|a|a|c|t|c|t|a|t|c|t|t|t|a|c|a|g|a|a|a|a|c|a|g|c|c|a|a|a|a|c|a|a|a|c|a|c|t|a|a|t|g|a|g|t|t|t|ei
g|a|g|g|g|g|t|t|c|c|t|t|c|c|a|c|t|t|c|t|g|g|g|c|a|c|c|t|c|t|g|g|a|t|c|c|c|g|t|t|c|a|g|a|a|a|a|c|c|a|c|t|t|t|a|t|t|g|ei
g|a|c|t|g|g|t|a|a|a|g|t|c|t|t|t|g|a|a|a|a|t|a|g|g|t|a|a|t|a|t|g|t|a|a|a|a|c|a|t|t|t|t|g|a|c|a|c|c|c|c|c|a|t|a|a|t|a|ei
t|c|a|g|a|a|t|c|t|g|a|a|a|c|t|t|t|g|t|a|g|c|t|c|t|c|t|c|c|t|c|t|a|t|c|t|t|c|t|c|a|g|g|g|g|t|a|t|g|a|g|t|c|c|a|a|c|g|ei
c|c|a|g|c|t|g|a|c|t|g|t|c|t|a|c|t|g|t|c|a|c|c|t|t|t|t|c|t|a|c|c|t|c|a|g|a|t|c|a|c|c|t|t|c|t|a|c|g|a|g|g|a|c|c|g|a|g|ei
c|g|g|t|g|t|g|c|c|g|g|g|c|t|c|c|t|g|a|t|g|a|c|c|c|a|a|g|g|g|a|c|t|t|c|c|c|a|g|c|a|c|c|t|a|c|a|a|c|a|a|a|g|a|c|t|t|a|ei
g|a|t|g|c|c|a|a|a|c|c|a|g|g|t|c|a|a|t|t|c|c|c|t|g|c|a|g|g|t|a|c|t|t|t|a|t|a|c|t|g|a|t|g|g|t|g|t|g|t|c|a|a|a|a|c|t|g|ei
g|a|c|c|a|a|c|a|t|a|t|c|c|a|g|g|t|t|t|t|a|a|t|g|t|a|a|a|t|t|a|g|t|a|g|a|g|t|t|g|g|c|c|c|a|c|c|a|a|t|a|c|a|a|g|t|t|g|ei
a|a|a|c|a|t|c|a|a|c|t|c|c|t|g|a|c|c|t|a|a|c|c|c|t|g|t|g|g|a|t|t|c|c|a|g|a|c|a|t|t|g|t|a|t|g|a|g|g|a|a|g|a|c|t|t|c|t|ei
a|a|g|g|a|c|a|c|g|g|g|c|a|g|c|a|g|a|c|a|g|t|g|t|a|g|t|c|c|t|t|t|c|t|t|g|g|c|t|c|t|g|c|t|g|a|c|a|c|t|c|g|a|g|c|c|c|a|ei
t|g|c|t|c|t|a|t|g|g|c|c|c|t|t|c|c|t|c|a|t|c|a|g|g|a|c|c|g|t|t|t|c|c|c|c|c|c|t|c|t|t|c|c|t|t|c|a|c|a|g|t|a|t|t|t|a|a|ei
c|c|t|a|a|g|a|a|a|a|a|t|g|t|g|t|t|t|t|c|a|t|g|a|a|g|t|a|a|g|t|c|a|t|t|g|t|c|t|t|c|a|c|t|t|g|g|c|t|g|c|c|a|c|c|t|c|c|ei
g|a|g|g|t|t|c|c|t|t|c|a|c|t|g|t|g|c|g|t|g|c|t|a|c|a|t|g|g|t|a|a|g|t|t|a|g|c|t|t|t|t|c|t|g|t|t|a|c|a|a|g|g|t|a|g|t|t|ei
a|a|a|t|t|g|c|a|c|g|t|g|g|a|t|c|c|t|g|a|g|a|a|t|c|a|g|g|g|t|a|a|g|t|c|t|a|t|g|g|a|a|t|c|t|t|t|g|a|t|g|t|t|t|t|c|c|t|ei
g|c|g|c|c|a|a|a|g|c|a|a|a|g|g|g|g|a|c|a|t|a|a|c|c|c|a|g|g|a|a|c|a|a|c|g|g|g|g|a|g|a|g|a|g|c|c|t|c|c|t|g|t|g|a|a|a|g|ei
a|c|a|a|a|a|c|t|t|t|t|c|c|c|t|t|t|t|t|c|a|a|t|t|a|t|a|g|t|a|c|g|g|c|a|g|c|t|g|c|t|a|t|t|g|c|t|t|a|t|g|g|c|c|t|g|g|a|ei
a|a|c|g|t|g|g|c|c|t|c|c|t|t|g|t|g|c|c|c|t|t|c|c|a|c|a|g|t|g|c|c|c|t|c|t|t|c|c|a|g|g|a|c|a|a|a|c|t|t|g|g|a|g|a|a|g|t|ei
a|c|c|c|c|c|g|c|g|g|c|t|t|c|t|a|c|c|t|c|t|t|t|t|g|a|g|g|g|t|g|c|g|t|g|g|t|g|g|c|c|c|c|t|g|g|g|g|a|g|t|g|g|a|g|g|a|a|ei
a|c|c|c|t|t|a|a|g|t|g|g|t|g|g|t|t|g|a|a|a|a|g|a|a|a|t|a|c|c|a|g|t|t|c|c|t|t|t|t|t|a|a|a|a|a|t|t|c|t|g|a|c|c|a|a|a|a|ei
c|t|g|a|a|c|t|t|c|a|t|c|t|g|c|a|g|c|t|g|g|a|a|g|c|t|g|g|a|g|t|c|t|t|g|c|t|t|a|g|g|g|c|a|g|a|c|a|a|a|a|a|g|a|g|a|g|g|ei
a|t|g|c|a|g|c|a|c|c|t|t|c|a|g|g|t|c|t|t|g|a|g|t|t|a|t|g|c|a|g|g|g|a|g|g|t|a|a|g|c|c|a|c|g|g|a|a|g|t|c|a|c|a|a|g|c|a|ei
g|t|a|t|c|c|t|c|c|c|c|a|t|t|c|t|a|a|c|c|a|c|a|g|t|c|c|c|c|a|a|g|g|a|t|c|t|c|c|t|t|a|t|c|t|a|t|c|c|c|c|g|g|g|a|t|c|c|ei
c|g|c|t|g|g|a|c|a|g|g|g|g|g|c|a|a|a|a|g|c|a|c|t|c|t|c|g|g|t|g|a|g|t|c|a|t|c|c|c|t|a|c|t|c|c|c|a|a|g|a|t|c|t|t|g|a|g|ei
c|t|a|g|c|c|t|a|g|a|a|c|a|t|c|c|c|a|c|c|a|a|t|t|t|c|c|a|c|c|c|a|c|t|t|a|a|g|g|a|g|a|a|a|a|g|g|c|t|a|t|c|a|a|g|g|g|t|ei
c|t|g|t|c|t|c|t|a|c|t|a|a|a|a|g|t|a|c|a|a|a|a|t|a|g|c|c|g|g|g|c|a|t|g|g|t|g|g|t|g|g|g|c|g|c|c|t|g|t|a|a|t|c|c|c|a|g|ei
g|c|t|c|a|g|c|t|c|t|t|c|t|t|g|t|t|t|c|a|a|c|t|a|a|c|a|g|a|t|g|g|a|g|g|a|g|a|c|t|c|t|g|a|g|c|a|g|t|t|c|a|t|a|g|a|t|g|ie
a|c|a|a|g|t|c|a|t|c|t|c|t|c|t|g|a|a|t|t|t|t|t|g|a|c|t|t|t|g|a|g|a|g|t|a|t|t|t|g|t|t|a|t|a|t|t|t|g|c|a|a|g|a|t|g|a|a|ei
c|a|g|a|g|g|t|g|g|g|c|t|t|c|g|g|g|c|a|g|a|a|c|a|c|c|g|t|g|c|t|g|a|g|c|t|a|g|g|a|c|c|a|g|g|a|g|t|g|c|t|a|g|t|g|c|c|a|ei
t|c|g|c|t|t|t|t|a|c|a|c|c|c|t|g|a|t|c|c|c|c|c|c|a|c|t|t|t|g|g|g|a|t|g|a|a|g|a|a|g|c|c|t|c|c|g|c|t|c|c|t|g|a|a|c|a|a|ei
g|a|t|g|a|c|c|a|t|t|c|a|g|a|a|a|t|a|a|a|g|c|a|a|a|g|c|a|g|g|c|c|a|c|a|t|a|c|c|t|t|a|a|c|c|a|a|c|a|c|c|a|a|a|g|a|a|a|ei
a|t|c|c|t|g|t|g|t|t|g|a|c|a|t|t|c|a|t|c|t|g|a|t|c|t|a|g|a|g|t|t|c|a|a|g|g|a|g|g|c|c|t|t|c|c|a|g|c|t|g|t|t|t|g|a|c|c|ie
c|g|g|g|c|a|a|g|t|c|a|c|t|g|c|g|c|t|c|c|c|t|g|g|a|c|a|g|c|c|c|t|a|t|g|a|a|t|a|a|a|g|g|g|g|a|t|a|c|c|g|a|g|g|t|g|a|t|ei
c|t|g|a|c|c|t|t|a|a|g|t|c|a|t|c|t|g|c|c|t|g|c|t|g|g|c|c|t|c|c|c|a|a|a|g|t|g|c|t|a|g|g|a|t|t|a|c|a|g|g|t|g|t|g|a|g|c|ei
a|g|c|g|a|g|a|t|g|a|a|g|a|t|a|a|g|g|a|t|a|a|a|t|g|g|a|a|a|t|g|t|g|g|a|g|t|a|t|t|t|t|g|g|a|c|t|g|g|g|c|a|a|c|t|c|c|c|ei
t|t|g|a|a|g|a|a|t|a|t|t|c|c|c|a|a|g|t|c|c|t|t|a|c|c|g|g|g|t|a|a|g|a|g|a|a|a|t|a|g|t|g|t|t|g|a|t|t|t|t|a|g|g|g|a|g|a|ei
c|c|t|t|c|a|g|c|t|c|a|g|c|t|c|a|g|g|a|t|t|t|a|a|g|a|a|g|g|t|a|a|g|a|t|g|a|a|t|t|g|g|g|g|g|a|a|g|a|t|a|t|t|g|t|g|a|c|ei
t|t|g|g|g|t|a|a|t|a|a|t|t|a|a|c|t|t|t|t|t|t|t|t|a|t|a|g|g|t|c|g|c|t|t|t|g|c|t|g|t|t|c|g|t|g|a|t|a|t|g|a|g|a|c|a|g|a|ei
g|a|a|t|g|c|t|t|a|g|t|g|c|c|c|t|c|a|c|t|t|c|t|c|c|t|c|t|c|t|c|t|c|t|a|t|a|c|c|a|t|c|t|g|a|g|c|a|c|c|c|a|t|t|g|c|t|c|ei
c|t|g|g|t|g|c|a|g|g|a|a|t|g|g|c|t|g|g|c|g|a|a|c|c|c|a|g|g|t|g|a|t|g|g|g|g|g|c|t|g|g|t|g|g|g|t|g|t|g|c|t|g|g|g|c|a|c|ei
c|a|g|g|a|c|t|t|a|g|t|t|a|a|a|a|a|a|t|g|c|t|t|t|t|c|a|g|g|t|t|t|c|t|c|g|t|t|g|c|t|t|a|c|a|c|a|a|a|g|a|a|a|g|c|c|c|c|ei
c|c|a|a|g|a|a|c|c|t|c|a|t|c|a|t|c|t|t|c|c|t|g|g|g|a|c|g|g|t|g|a|g|t|g|a|g|c|c|a|g|g|c|c|t|t|c|c|a|g|c|c|c|c|g|c|a|g|ei
t|g|a|c|c|a|g|g|t|c|t|t|g|t|t|t|t|t|g|t|t|c|t|c|c|c|a|g|g|g|a|g|c|g|a|c|a|g|t|g|c|c|c|a|g|g|g|g|t|c|t|g|a|g|t|c|t|c|ei
t|t|g|c|a|t|t|g|t|g|g|t|c|t|c|c|c|a|t|c|a|a|g|c|c|a|g|c|g|g|c|a|c|t|c|g|a|t|c|t|g|g|g|a|c|a|g|a|c|c|t|c|a|c|t|c|t|c|ei
c|t|g|g|t|t|g|a|g|a|a|a|c|a|g|a|g|a|c|t|g|t|a|c|a|c|t|c|t|g|g|c|a|g|g|g|a|g|a|a|g|c|t|g|t|c|t|c|t|g|a|t|g|g|c|c|t|g|ei
a|a|t|a|a|c|a|c|c|c|t|a|t|t|g|t|g|g|g|c|t|t|g|g|a|g|a|a|t|g|g|g|g|g|a|c|t|t|c|a|a|g|g|c|g|t|g|t|c|a|g|t|t|t|c|a|g|g|ei
a|a|c|t|a|a|a|t|c|a|a|g|a|a|g|a|a|a|t|c|t|c|t|t|a|a|t|g|g|a|a|g|a|a|a|t|t|a|a|g|t|t|t|g|t|a|a|t|t|t|t|a|a|a|a|a|t|c|ei
c|t|t|t|t|c|c|a|g|a|g|c|c|t|t|a|t|a|t|c|t|t|g|t|t|a|t|g|c|c|a|a|t|g|a|t|g|c|c|g|c|c|a|t|t|t|c|t|g|a|g|c|c|a|g|a|a|a|ei
c|a|t|g|g|c|t|g|a|a|g|g|g|g|a|a|a|t|c|a|c|c|a|c|t|c|a|c|a|g|c|c|c|t|g|a|c|c|g|a|g|a|a|g|t|t|t|a|a|t|c|t|g|c|c|t|c|c|ei
a|a|g|g|a|c|a|a|g|c|a|g|g|t|c|t|a|c|c|g|g|g|c|a|g|c|a|c|c|g|c|c|t|g|c|t|g|c|t|g|c|t|g|g|g|t|g|c|t|g|g|a|g|a|a|t|c|t|ei
c|t|t|t|g|g|c|t|c|a|t|t|t|c|t|t|g|c|c|t|t|t|t|t|t|c|a|g|g|a|g|t|a|t|a|c|a|c|c|t|t|a|a|a|t|g|a|t|a|a|g|a|a|g|c|a|g|t|ei
g|t|g|a|a|c|t|c|t|g|g|a|c|t|g|g|a|a|g|g|a|c|c|a|t|t|a|g|g|g|g|g|t|g|c|a|a|a|a|a|g|c|a|g|g|a|g|g|c|a|g|g|t|c|a|g|g|t|ei
c|c|c|g|g|c|c|g|g|a|t|g|t|t|a|c|g|g|a|g|a|g|c|a|a|g|c|g|g|t|g|a|g|t|g|c|c|g|t|g|g|g|g|t|g|g|c|c|t|g|a|g|g|g|g|g|a|c|ei
a|c|c|t|c|c|g|a|g|g|g|g|t|a|a|a|c|a|g|t|t|g|g|t|a|a|c|a|g|t|c|t|c|t|g|a|a|g|t|c|a|g|c|t|c|t|g|c|c|a|t|t|t|t|c|t|a|g|ei
a|g|c|t|c|t|g|c|c|a|g|t|a|a|g|a|a|g|t|t|g|c|a|c|c|c|c|a|g|t|g|a|a|a|t|g|c|t|g|c|t|g|c|t|g|c|c|a|t|t|t|c|a|a|c|t|g|t|ei
c|c|t|g|a|c|a|c|t|a|a|g|g|a|a|a|t|g|c|t|g|a|a|c|t|t|t|g|g|t|a|a|g|t|g|t|t|t|g|c|t|g|g|a|t|t|c|c|t|a|a|a|g|t|g|g|t|a|ei
c|t|g|t|g|g|t|a|t|g|a|a|g|c|c|a|g|a|c|c|t|c|c|c|g|c|g|g|g|c|c|t|c|a|g|g|g|a|a|c|a|g|a|a|t|g|a|t|c|a|g|a|c|c|t|t|t|g|ei
t|t|t|c|t|t|c|t|c|t|t|g|a|t|c|t|c|t|t|t|t|c|t|g|a|c|a|g|a|g|a|a|t|g|a|a|g|a|a|a|t|t|g|a|t|g|t|t|g|t|g|a|c|a|g|t|a|g|ie
c|t|g|g|g|c|a|g|g|g|g|g|a|g|t|t|c|a|g|g|g|c|c|t|a|a|t|g|c|t|c|g|c|c|t|g|c|c|c|c|t|g|a|a|c|a|c|t|g|a|t|g|c|c|t|a|c|t|ei
a|t|t|a|t|t|g|g|g|a|c|c|a|t|c|t|t|c|a|t|c|a|t|a|g|g|g|a|g|t|g|c|g|c|a|a|a|a|g|c|a|a|t|g|c|a|g|c|a|g|a|a|c|g|c|a|g|g|ei
a|c|c|t|t|t|g|t|t|g|g|t|t|g|t|a|a|a|t|c|t|g|t|t|a|c|c|a|a|t|g|g|t|g|g|t|t|t|g|t|t|c|c|c|t|c|c|t|g|a|a|c|a|g|t|t|t|t|ei
a|c|t|t|g|a|a|a|t|a|t|t|t|t|t|c|t|c|c|a|c|a|t|t|t|c|a|g|t|t|t|t|g|t|t|c|a|t|g|a|a|t|a|t|t|c|a|a|g|a|a|g|a|c|a|t|c|c|ei
c|a|g|a|t|t|g|t|g|t|g|g|a|a|t|g|g|t|c|c|t|g|t|g|g|g|t|a|t|t|t|g|a|a|t|g|g|g|a|a|g|c|t|t|t|t|g|c|c|c|g|g|g|g|a|a|c|c|ei
a|g|t|g|t|t|c|g|t|t|g|t|g|c|c|a|g|c|g|a|c|t|a|a|a|g|a|g|g|t|g|a|g|a|g|c|g|g|g|t|c|g|c|g|g|a|g|g|c|c|g|c|a|c|c|t|g|g|ei
a|c|a|a|g|a|a|g|g|a|t|g|g|a|g|c|t|g|a|c|t|t|c|c|a|a|g|t|g|g|c|a|t|t|g|t|g|t|t|c|t|g|a|a|g|a|t|t|g|g|g|g|a|a|c|a|c|a|ei
t|t|t|g|c|a|c|t|g|a|a|t|g|c|a|a|a|t|c|t|t|t|t|t|c|a|a|g|g|t|g|a|t|t|a|t|c|c|t|g|a|a|c|c|a|t|c|c|a|g|g|c|c|a|a|a|t|a|ei
a|c|t|t|t|g|c|t|g|g|c|a|g|a|c|c|t|g|a|g|c|c|a|t|a|c|c|t|g|t|a|a|g|g|g|c|t|g|g|g|g|g|c|a|t|t|t|t|t|t|c|t|t|t|c|t|t|a|ei
t|t|a|t|t|t|c|t|g|t|a|g|c|t|g|a|a|c|g|t|g|a|a|t|g|t|c|c|g|t|g|a|c|a|t|t|a|a|a|g|a|g|a|a|g|c|t|g|t|g|c|t|a|t|g|t|c|g|ei
g|t|g|c|t|g|c|t|t|t|g|g|g|a|g|t|t|t|a|a|a|t|t|c|t|c|a|g|g|t|a|a|c|a|a|a|a|c|a|t|t|c|a|g|a|c|a|a|g|c|c|t|g|a|a|t|a|c|ei
a|a|g|t|g|a|c|t|g|t|t|t|t|t|c|t|t|t|t|t|c|a|a|a|t|t|a|g|a|t|a|c|t|t|a|t|a|t|g|a|a|a|t|t|g|c|c|a|g|a|a|g|a|c|a|t|c|c|ei
a|c|t|g|c|g|a|g|g|c|c|t|g|a|t|g|c|t|a|t|c|a|g|c|t|g|c|t|g|g|c|c|t|c|c|c|t|c|a|t|g|a|g|c|t|c|c|c|t|g|a|c|c|t|c|c|a|t|ei
g|a|a|a|a|c|c|c|t|c|t|t|g|a|a|t|g|c|c|a|a|g|a|a|a|g|g|a|g|t|a|a|g|t|t|g|c|t|c|t|a|g|a|a|t|t|t|t|a|g|g|g|g|a|g|t|a|t|ei
c|a|a|a|a|a|a|a|g|g|c|a|g|g|g|g|t|t|g|c|a|a|t|c|a|g|t|c|t|c|t|g|a|t|a|a|a|a|c|a|g|a|c|t|t|t|a|a|a|c|c|a|a|c|a|a|a|g|ei
t|g|c|t|c|c|a|g|g|g|a|g|c|t|g|a|g|g|c|c|c|t|t|a|a|g|c|c|c|a|g|t|a|c|a|t|g|c|t|g|g|t|g|g|t|t|c|a|c|a|t|g|c|g|c|a|g|a|ei
c|c|c|t|t|g|g|a|g|c|c|t|c|t|g|c|c|c|t|c|c|t|c|a|c|c|c|g|g|a|t|g|g|c|c|t|c|t|c|c|t|t|c|a|t|t|t|t|g|g|t|t|t|g|t|t|t|c|ei
g|g|g|a|g|c|a|c|a|g|t|g|g|a|c|c|a|t|c|a|g|g|g|g|g|a|g|c|t|g|g|t|a|c|c|a|c|t|g|g|a|a|g|g|g|c|t|t|c|g|a|g|t|t|c|t|c|g|ei
c|t|g|g|a|c|a|c|a|c|g|c|c|c|a|g|g|t|t|g|t|a|g|t|a|a|c|g|c|t|a|t|g|g|c|t|c|c|a|a|g|a|a|g|a|g|c|a|t|g|g|t|c|a|t|t|c|t|ei
g|a|c|a|a|g|t|a|c|a|t|g|a|c|t|a|t|a|t|c|a|g|g|t|t|c|a|a|a|t|t|g|a|g|g|a|a|a|c|c|a|t|t|g|a|c|c|g|c|g|a|g|a|c|t|t|c|t|ei
t|t|c|g|c|t|t|t|c|c|t|c|t|g|g|t|t|t|g|a|a|a|g|c|c|t|g|g|a|a|a|a|c|t|c|a|g|g|a|t|t|c|t|c|a|c|g|a|c|t|c|t|a|c|c|a|t|g|ei
g|a|a|a|g|a|a|a|c|g|a|g|g|a|a|g|a|c|g|g|g|t|t|t|g|t|c|t|a|t|a|g|t|t|g|a|a|g|c|t|t|t|t|a|c|t|a|g|g|a|t|c|t|t|g|c|c|t|ei
t|g|t|t|g|t|t|g|g|t|g|a|a|t|g|g|a|g|c|t|c|a|g|t|t|g|t|g|g|g|g|g|g|a|c|c|c|t|g|a|t|c|a|a|c|a|c|c|a|t|c|t|g|g|g|t|g|g|ei
t|t|t|a|c|c|a|g|a|g|g|g|a|g|c|c|a|g|g|g|c|t|g|a|c|t|c|a|t|c|t|g|t|t|t|g|c|g|g|a|t|c|a|a|g|a|a|c|c|c|g|a|g|c|t|g|t|g|ei
a|t|c|a|t|g|g|a|g|a|a|g|g|g|g|c|a|g|c|t|g|g|t|c|a|c|t|g|g|t|g|a|g|t|g|g|g|c|c|c|t|g|g|t|g|g|g|g|t|g|a|g|a|g|g|c|a|g|ei
t|t|t|c|c|t|g|t|g|t|g|t|t|c|c|a|t|g|c|a|g|t|a|t|t|a|t|c|c|t|c|t|g|t|t|c|c|t|t|t|c|a|g|c|c|t|c|c|t|t|g|g|a|a|g|g|g|c|ei
t|g|c|t|g|t|g|c|t|t|t|a|t|g|g|a|t|a|g|t|a|a|g|a|g|g|c|c|c|t|a|g|a|g|t|g|g|g|a|g|t|c|c|t|g|a|t|a|a|c|c|c|a|g|g|c|c|t|ei
t|g|t|c|a|a|t|g|g|g|a|a|t|a|t|g|g|a|a|a|a|t|g|t|t|g|g|g|g|a|g|g|c|t|t|t|a|t|g|t|g|g|a|a|g|c|a|g|c|a|t|t|t|g|c|t|g|g|ei
g|a|a|g|g|c|t|t|a|t|g|t|g|g|a|t|g|a|t|a|c|t|c|t|c|t|g|a|a|c|a|g|a|t|g|a|a|a|g|c|a|g|a|a|c|g|t|g|a|g|c|a|g|a|g|g|a|t|ei
g|g|a|a|g|a|g|g|g|a|a|t|c|c|c|a|t|c|a|a|a|g|t|a|c|c|g|t|g|t|g|g|g|g|t|c|t|g|c|a|a|t|g|g|t|g|a|a|t|g|c|c|a|a|a|g|a|t|ei
c|t|t|g|c|c|t|a|t|a|a|t|c|t|t|c|c|t|t|g|t|c|t|t|t|c|a|g|g|a|a|g|t|g|a|a|t|a|a|g|a|a|g|a|t|g|a|c|a|g|t|g|t|t|t|c|a|a|ei
c|t|a|a|t|t|t|a|a|a|a|a|t|t|t|t|a|a|a|a|t|t|t|a|t|c|c|a|t|t|a|g|a|a|a|a|c|a|a|a|a|c|t|g|a|c|t|t|t|t|a|a|g|a|a|c|a|a|ei
t|g|a|t|g|a|g|c|t|c|t|g|c|a|t|c|c|c|a|t|t|t|g|g|t|c|a|t|t|c|c|t|g|c|t|a|c|a|g|t|c|t|c|c|a|a|c|a|a|t|g|t|c|c|c|t|g|g|ei
c|t|g|a|t|t|g|g|c|c|c|t|c|t|c|t|c|t|t|c|c|c|t|t|a|c|a|g|a|a|a|c|a|g|t|t|g|t|g|c|t|c|t|t|t|c|g|a|g|a|t|c|t|a|c|g|a|a|ei
c|t|g|g|a|t|t|t|t|t|t|t|c|g|g|g|t|a|g|t|g|g|a|a|c|c|a|g|g|t|a|a|g|c|a|c|c|g|a|a|g|t|c|c|a|c|t|t|g|c|c|t|t|t|t|a|a|t|ei
t|g|t|g|g|a|g|a|c|a|t|g|g|c|t|g|g|a|t|t|c|c|g|c|a|a|g|a|a|a|t|a|a|a|a|a|a|g|c|a|g|g|t|t|c|g|t|g|g|t|g|t|c|c|c|t|t|g|ei
a|g|a|t|t|t|g|g|g|a|g|a|a|g|a|a|a|a|t|t|t|c|a|a|c|c|t|t|g|t|a|a|g|t|t|a|a|a|a|t|a|t|t|g|a|t|g|a|a|t|c|a|a|a|t|t|t|a|ei
t|g|t|t|c|a|g|c|a|t|c|t|a|t|g|a|t|g|t|a|c|c|a|g|a|g|g|c|a|a|g|t|t|c|c|g|t|t|a|t|c|g|g|c|g|c|g|t|g|g|c|t|g|a|a|g|g|c|ei
t|g|g|t|c|a|a|t|t|c|t|g|a|a|t|t|c|t|c|t|c|c|a|a|t|a|t|t|a|t|t|a|t|t|a|t|t|t|t|t|t|g|a|g|a|c|a|g|t|c|t|t|g|c|t|c|t|g|ei
t|c|c|g|g|t|g|t|g|g|a|g|t|c|t|g|g|a|g|a|c|g|a|g|g|c|a|g|g|t|a|g|g|a|g|c|c|c|g|g|g|c|g|c|g|a|c|a|a|t|c|g|g|g|g|g|g|c|ei
c|g|a|g|a|g|t|a|g|c|a|g|t|t|g|t|a|g|c|t|a|c|c|g|c|c|a|g|g|t|a|g|g|g|c|a|g|g|a|g|t|t|g|g|g|a|g|g|g|g|a|c|a|g|g|g|g|g|ei
t|g|t|t|t|c|t|t|g|t|c|c|t|c|c|t|g|g|t|a|t|t|g|g|t|t|t|g|g|t|g|a|g|t|g|t|g|g|g|c|t|t|c|c|g|g|g|g|a|g|g|g|a|a|g|c|c|t|ei
t|c|t|t|g|a|t|c|a|c|t|g|t|c|c|c|t|c|t|c|c|g|g|c|t|c|a|g|g|c|a|c|a|a|c|a|a|t|g|a|g|a|a|g|a|g|c|t|t|c|c|t|g|a|t|c|t|g|ei
t|t|t|t|t|t|t|c|t|t|t|t|g|c|t|g|t|t|t|t|t|c|t|t|t|t|t|t|t|g|a|g|a|c|a|g|g|g|c|t|t|g|c|t|c|t|g|t|g|c|c|a|c|c|c|a|g|g|ei
c|c|c|c|a|g|c|t|t|a|c|c|g|c|c|c|a|g|t|a|c|g|c|g|c|t|c|t|g|a|a|g|c|t|t|a|t|t|g|a|g|a|c|t|c|a|c|c|t|g|a|g|a|a|c|t|a|t|ei
a|c|t|a|c|t|c|g|g|a|a|c|a|a|a|a|g|a|g|a|a|a|a|g|a|g|a|a|a|a|t|t|c|c|c|a|t|c|a|c|t|c|t|g|t|g|a|g|t|a|g|g|a|g|g|t|g|t|ei
c|c|g|c|t|c|c|a|g|g|t|g|g|c|g|g|g|c|g|g|c|t|g|a|c|g|a|g|g|t|g|a|g|g|c|t|g|c|g|g|g|t|g|g|c|c|a|g|g|g|c|a|c|g|g|g|c|g|ei
g|a|t|c|t|g|g|c|t|g|a|c|t|t|a|t|t|t|t|c|t|t|g|t|c|t|a|g|g|c|t|g|a|g|g|t|t|g|g|t|t|t|c|a|g|c|a|t|g|t|a|t|c|t|g|c|t|t|ei
c|c|t|g|g|t|g|c|g|a|g|a|a|g|a|c|t|t|t|g|t|g|c|g|c|a|g|c|a|g|c|t|c|a|t|t|g|c|t|g|g|g|g|a|a|g|g|t|g|a|g|g|a|g|c|t|a|a|ei
a|a|g|g|g|c|c|t|g|a|g|g|g|g|g|g|c|t|t|c|t|t|c|t|c|c|a|g|g|c|g|a|g|c|a|c|g|a|c|c|t|c|a|g|c|g|a|g|c|a|c|g|a|c|g|g|g|g|ei
a|g|g|t|t|t|g|t|c|t|t|t|g|g|a|a|c|c|a|c|a|c|c|g|a|g|a|c|a|t|c|c|t|c|a|g|g|a|a|c|a|a|a|g|g|c|t|g|c|t|c|c|a|g|c|t|c|t|ei
g|g|t|c|t|c|t|g|c|t|g|g|t|t|c|t|a|g|c|t|t|c|c|c|t|c|c|c|a|t|t|t|c|t|g|a|c|t|c|c|t|g|g|c|t|t|t|a|g|c|t|c|t|c|t|g|g|a|ei
g|g|a|g|a|t|a|a|g|g|g|g|a|c|t|c|a|g|c|t|c|t|c|g|a|g|g|t|c|a|a|a|a|a|c|a|g|a|g|g|a|t|t|g|c|t|a|t|t|g|c|c|c|g|a|g|c|c|ei
g|a|a|g|c|a|g|t|t|g|c|t|a|a|t|g|a|a|g|t|a|t|t|a|a|a|t|g|g|a|g|a|t|g|c|c|t|a|g|c|a|c|c|c|c|a|c|a|g|c|a|g|t|t|a|c|a|g|ei
g|c|t|c|a|g|g|t|g|c|c|c|g|g|g|t|g|c|c|c|g|c|c|t|t|a|g|g|g|g|g|a|t|c|a|g|a|g|c|a|t|c|c|t|g|g|g|g|g|a|g|g|g|c|c|c|a|g|ei
a|a|c|t|t|g|g|c|t|t|g|g|g|a|g|t|c|t|g|c|a|t|c|a|c|a|c|t|t|t|c|t|g|g|c|t|g|t|g|t|g|a|c|c|t|t|g|g|g|c|a|a|g|t|t|a|c|t|ei
g|c|t|g|t|c|a|t|a|g|g|c|a|t|c|g|a|c|g|a|g|g|g|c|g|t|t|t|g|t|a|a|g|t|t|g|g|c|t|t|g|t|c|t|t|g|g|c|a|t|c|a|c|t|c|t|t|c|ei
g|c|t|a|t|t|a|c|t|a|c|c|a|a|g|c|c|t|g|t|t|a|g|t|a|g|g|g|c|a|a|a|g|g|c|a|a|g|a|a|a|t|t|g|t|a|a|t|t|t|g|g|g|g|c|t|g|t|ei
t|g|g|c|c|c|g|g|g|c|c|t|c|g|g|c|t|c|c|g|a|g|a|g|a|g|a|g|g|a|g|c|c|c|g|c|c|t|g|g|g|c|g|c|c|g|a|g|g|a|g|a|g|c|g|g|g|c|ei
a|g|t|g|g|a|g|c|c|a|a|t|c|c|c|c|t|g|g|a|a|c|c|g|c|t|g|a|g|t|g|a|g|t|g|a|t|g|g|g|c|c|t|g|g|a|a|g|g|g|g|c|c|a|t|g|c|t|ei
a|t|a|c|c|c|c|t|t|t|t|c|a|c|t|t|t|c|c|c|c|a|c|t|t|t|a|g|g|g|t|a|r|t|c|a|g|t|a|c|t|g|g|c|g|c|t|t|t|g|a|g|g|a|t|g|g|t|ei
a|c|t|c|a|c|c|t|t|g|t|c|c|c|c|c|t|t|c|t|c|c|a|t|t|c|a|g|g|t|t|g|g|c|c|c|a|t|a|a|a|g|c|c|c|t|c|t|g|c|a|c|t|g|a|g|a|a|ei
t|t|t|t|a|g|a|g|a|g|a|g|t|t|t|g|g|a|a|g|g|a|a|t|t|t|a|t|c|a|g|a|a|t|g|a|t|t|a|g|g|g|g|a|g|a|g|c|a|a|g|a|g|a|t|c|a|g|ei
c|c|g|c|c|c|t|c|a|g|a|g|a|g|c|a|g|c|c|t|c|c|c|a|a|c|a|g|g|t|a|a|g|g|g|c|g|c|a|g|c|g|t|g|g|g|g|g|a|c|c|c|g|t|g|c|t|c|ei
g|t|c|c|t|g|t|g|c|c|t|g|t|g|t|t|a|c|t|t|g|c|t|c|g|t|t|a|g|a|a|a|c|a|a|a|c|t|t|c|a|t|g|c|c|c|a|a|a|c|c|a|a|g|g|a|a|c|ei
t|t|c|t|g|g|c|a|g|a|a|c|c|c|c|c|g|c|a|a|c|c|a|t|c|c|g|c|t|g|t|c|a|a|g|t|c|c|a|g|t|t|c|t|a|c|g|g|g|c|t|c|t|c|g|g|a|g|ei
t|a|t|a|a|t|c|c|c|a|g|c|t|a|c|t|t|g|a|g|a|g|g|t|a|g|g|c|a|g|g|a|g|a|a|t|c|a|c|t|t|g|a|a|c|c|a|g|g|g|a|g|g|t|g|a|a|g|ei
c|c|c|t|g|a|c|c|t|c|a|g|c|t|a|c|a|t|c|g|t|g|c|a|c|t|a|g|g|t|a|c|a|c|g|g|g|c|t|g|c|c|c|a|t|g|g|g|g|t|g|g|t|g|c|t|g|g|ei
t|t|t|t|c|c|c|a|t|c|a|t|c|c|t|g|t|a|c|t|t|c|t|t|c|t|a|g|a|t|g|t|c|a|g|c|c|a|a|g|a|a|g|a|c|g|t|t|c|c|c|t|t|g|g|t|a|a|ei
c|t|g|g|t|g|c|a|g|g|a|a|t|g|g|c|t|g|g|c|a|a|a|c|c|c|a|g|g|t|g|a|t|g|g|g|g|g|c|t|g|g|t|g|g|g|t|g|t|g|g|g|a|g|g|c|a|c|ei
a|c|t|a|g|g|a|a|g|a|c|g|c|g|c|g|a|a|c|g|g|g|g|t|g|c|c|g|g|c|c|g|g|c|g|g|g|t|g|g|g|g|g|a|g|g|g|g|a|g|g|c|g|g|g|g|g|a|ei
a|g|g|g|g|t|g|c|t|c|c|t|g|g|c|a|a|t|c|g|t|g|g|t|t|c|c|a|g|g|c|t|c|t|g|a|t|g|g|t|t|t|a|c|c|t|g|g|g|c|c|a|a|a|g|g|g|t|ei
g|g|g|a|g|c|a|g|g|g|a|g|a|t|g|g|a|t|t|g|g|t|a|t|g|t|a|t|g|g|t|c|a|c|a|c|c|t|g|a|g|g|g|t|c|c|t|g|c|a|c|c|t|g|c|t|a|g|ei
c|a|g|c|t|c|c|t|t|c|c|a|a|t|a|t|c|t|t|t|t|g|t|t|t|t|a|g|t|c|a|g|g|g|a|c|t|a|t|g|c|g|g|c|g|c|a|a|a|c|a|t|c|t|c|c|t|t|ei
g|a|c|t|g|g|c|c|a|t|g|g|g|a|g|c|a|c|a|g|c|t|t|c|g|c|a|c|t|a|c|t|c|c|t|t|t|t|a|g|g|c|c|t|g|a|t|g|g|c|c|t|c|t|g|g|a|a|ei
t|c|t|g|g|g|a|g|a|g|g|c|c|a|c|a|t|g|a|g|t|t|c|g|c|c|t|g|g|t|a|t|g|t|g|g|g|g|g|g|c|c|g|g|g|g|g|c|c|t|g|c|c|g|t|g|a|a|ei
a|a|t|t|t|t|g|c|t|g|g|a|g|a|a|g|c|c|a|c|a|c|t|c|a|c|g|c|a|t|a|t|a|t|t|c|c|c|t|c|t|g|g|g|a|g|c|a|c|a|g|t|a|c|g|a|a|a|ei
c|a|g|c|t|t|g|g|t|t|c|t|c|c|t|g|g|g|c|a|a|g|a|g|a|g|a|a|g|a|a|a|g|a|a|g|a|g|g|a|g|g|g|g|g|a|a|g|g|g|a|a|a|a|a|g|a|a|ei
g|g|g|a|g|c|a|g|g|a|g|g|a|g|a|a|g|a|t|g|c|g|g|g|c|a|g|g|a|g|g|a|g|a|t|g|a|t|g|t|g|g|g|a|g|t|a|g|g|a|g|g|a|g|a|a|g|a|ei
a|g|t|g|g|c|a|t|g|a|t|c|t|c|g|g|c|t|c|a|g|t|g|a|c|c|t|c|t|g|c|c|t|c|c|c|g|g|g|t|t|c|a|a|g|c|g|a|t|t|c|t|c|c|t|a|c|c|ei
c|t|c|c|c|t|a|a|g|c|c|g|g|g|g|g|c|c|t|t|g|a|g|c|t|g|c|a|g|a|g|c|c|a|g|c|c|c|t|c|c|a|c|c|c|c|a|t|c|c|c|a|t|c|c|c|a|c|ei
c|c|c|c|a|c|a|c|g|a|c|t|c|t|c|t|c|g|t|t|c|t|c|c|a|c|a|g|c|c|a|g|g|t|c|t|c|c|a|g|c|t|g|g|g|g|t|g|g|a|c|g|t|g|c|c|c|a|ei
a|a|g|c|t|g|c|a|c|g|t|g|g|a|t|c|c|t|g|a|g|a|a|t|c|a|g|g|g|t|g|g|g|t|c|c|a|g|g|a|g|a|t|g|t|t|t|c|a|c|t|t|t|t|c|t|c|c|ei
g|c|g|c|c|t|g|a|a|t|t|t|t|c|t|g|a|c|t|c|t|t|c|c|t|c|a|g|a|c|c|c|c|c|c|a|a|a|g|a|c|a|c|a|c|g|t|g|a|c|c|c|a|c|c|a|c|c|ei
c|a|g|g|g|t|a|t|t|g|a|c|t|g|a|g|g|g|c|a|g|c|c|g|c|t|c|c|a|t|g|g|g|a|a|a|t|g|t|a|t|c|t|c|c|c|t|t|c|c|c|c|a|g|g|g|a|g|ei
t|c|g|a|t|g|a|t|g|a|c|a|c|t|t|a|c|g|a|c|a|a|t|a|a|t|t|g|g|t|a|a|g|a|g|c|t|c|g|t|c|a|t|t|c|c|c|g|g|c|t|c|c|a|g|t|t|c|ei
c|a|g|t|g|a|a|c|g|a|c|g|g|a|g|g|c|t|g|t|a|t|c|c|c|g|a|g|g|t|a|a|c|a|g|t|g|c|c|t|g|a|g|g|c|g|c|g|g|g|a|g|g|a|g|g|c|g|ei
g|g|a|a|g|a|g|g|c|t|g|g|a|g|g|c|g|a|a|g|c|c|t|g|g|c|a|g|g|t|a|a|a|c|a|t|t|g|t|t|t|c|t|c|g|a|t|g|c|a|t|g|g|g|a|a|t|a|ei
c|c|c|a|c|a|a|c|a|g|t|g|t|t|t|t|t|g|c|c|t|g|g|c|g|t|a|g|t|c|t|t|g|a|c|c|c|c|a|a|a|g|a|a|a|c|t|t|c|a|g|t|g|t|g|t|g|g|ei
c|t|c|a|g|t|g|a|c|a|c|c|t|g|c|c|c|a|c|g|t|t|t|a|c|t|t|g|g|g|t|c|t|t|c|t|t|g|a|t|g|c|a|g|g|a|a|a|g|g|c|a|c|a|t|c|t|c|ei
a|a|g|a|a|t|c|g|a|t|g|g|g|g|g|a|t|g|c|t|t|c|a|g|g|a|a|c|g|t|g|g|g|a|g|t|t|c|a|g|c|t|g|c|t|t|c|t|c|t|t|g|c|c|t|a|a|g|ei
a|g|t|t|g|c|c|t|t|t|g|a|t|c|t|g|g|c|g|a|c|a|c|t|g|t|g|g|c|t|a|t|g|a|t|t|c|a|g|a|c|a|a|c|c|c|t|c|g|a|c|t|t|c|g|t|g|g|ei
g|a|t|a|a|a|a|g|g|a|t|t|t|g|g|g|c|t|g|a|a|c|a|g|t|g|g|a|g|g|g|a|g|c|a|t|t|g|g|a|a|t|g|g|c|a|c|t|c|a|g|g|g|c|a|a|a|g|ei
c|t|c|c|g|a|g|c|a|g|c|a|a|t|t|c|c|c|c|a|t|t|c|t|t|c|c|c|c|t|a|t|t|g|c|t|g|g|c|t|c|t|g|c|a|g|g|g|c|t|c|t|g|a|t|c|a|a|ei
g|g|g|a|g|g|a|g|g|a|g|g|t|t|g|c|a|g|t|g|a|g|c|g|g|a|t|g|g|t|g|c|c|a|c|t|g|c|a|c|t|c|c|a|g|c|c|t|g|g|c|a|a|c|a|g|a|g|ei
a|c|t|a|t|a|c|c|c|a|a|a|a|t|c|c|c|c|a|c|c|c|t|c|c|t|g|g|g|g|a|c|a|c|c|t|g|g|t|c|c|a|c|c|c|t|a|a|g|c|t|g|c|c|t|t|t|c|ei
t|g|t|g|g|g|c|c|a|g|t|t|c|t|g|g|g|a|g|g|a|g|g|c|g|c|g|a|t|g|t|g|t|g|c|a|c|c|t|g|c|a|c|c|g|a|c|a|t|g|g|a|g|g|a|t|g|c|ei
g|t|t|c|t|a|g|a|a|g|c|c|t|g|g|g|c|g|a|a|g|t|c|g|c|t|a|a|t|t|g|t|g|g|a|c|t|t|g|g|g|g|a|a|a|a|t|a|a|g|g|c|c|c|a|a|c|c|ei
t|g|c|t|t|g|g|g|c|t|t|c|a|g|g|g|c|t|g|c|c|t|g|c|g|c|a|g|g|t|g|c|g|t|c|c|g|g|g|g|a|g|g|t|t|t|t|c|t|c|c|a|t|a|a|a|c|t|ei
g|g|g|c|c|g|a|t|c|t|c|a|g|c|c|c|c|t|c|c|t|c|g|c|c|c|a|g|g|c|t|c|c|c|a|c|t|c|c|t|t|g|a|a|g|t|a|t|t|t|c|c|a|c|a|c|t|t|ei
g|a|g|g|a|g|c|t|t|c|c|a|a|a|t|t|a|t|c|c|a|t|t|g|a|c|a|a|g|c|c|c|g|t|c|a|g|t|g|g|c|c|c|c|a|t|g|c|a|t|a|a|a|t|g|t|a|c|ei
a|g|a|c|a|c|a|g|a|a|g|t|c|c|a|t|c|t|a|t|t|a|c|t|a|c|t|g|g|t|g|c|g|t|t|g|a|c|t|c|t|g|a|t|t|g|a|a|g|c|c|t|t|t|t|t|g|g|ei
c|c|a|a|t|c|a|c|c|a|c|c|a|a|g|c|t|c|c|t|t|g|t|c|a|c|a|g|g|c|c|t|c|t|t|t|g|a|g|c|c|c|g|g|a|g|a|c|a|c|g|a|a|a|t|a|t|g|ei
g|g|c|c|a|g|g|a|t|c|t|t|c|c|t|c|a|a|g|a|g|a|a|g|c|c|t|c|a|a|t|c|c|g|a|g|a|a|a|g|c|c|t|g|a|a|g|g|a|a|c|g|a|g|g|t|g|t|ei
g|t|g|c|c|c|a|t|c|a|c|c|a|a|c|g|c|c|a|c|c|c|t|g|c|c|g|g|g|t|g|a|g|t|g|c|c|t|g|g|g|c|t|a|g|c|c|c|t|g|t|c|c|t|g|a|g|c|ei
a|a|c|a|t|t|c|c|a|a|t|g|c|a|t|t|g|c|t|a|a|a|a|a|t|a|t|t|g|t|g|g|a|a|a|t|g|a|a|t|a|t|t|t|t|g|t|a|a|c|t|a|t|t|a|c|a|c|ei
g|g|a|g|a|t|c|t|g|c|t|t|g|a|a|t|g|t|g|c|t|g|a|g|c|a|g|g|g|t|a|a|a|g|a|g|t|c|g|t|c|g|a|t|a|t|g|c|t|t|t|t|t|g|g|t|a|g|ei
t|a|a|t|c|t|c|c|t|t|c|t|t|g|c|c|t|g|c|c|t|g|g|c|a|c|a|g|c|a|a|t|g|c|c|a|g|a|g|a|g|a|a|t|a|t|c|c|a|g|a|g|a|c|t|c|a|c|ei
g|t|g|g|c|t|g|t|t|a|a|t|t|c|t|c|c|a|g|t|c|t|t|c|t|t|c|g|c|a|g|t|g|c|c|c|a|g|t|g|a|t|g|g|c|a|t|t|a|c|t|c|t|g|c|c|g|t|ei
g|a|g|t|t|a|a|a|g|a|a|a|c|c|c|t|t|t|t|c|c|a|t|g|g|g|a|g|g|t|g|g|a|g|g|t|t|g|c|a|c|c|t|c|c|t|a|a|g|g|c|c|c|a|t|g|a|a|ei
g|t|g|g|g|c|a|a|g|t|g|c|c|g|a|a|g|c|g|c|a|g|g|a|c|a|a|g|g|t|a|c|t|g|g|c|c|t|c|c|c|a|t|c|c|t|c|c|c|c|t|c|c|a|t|t|c|t|ei
t|g|a|c|a|a|a|a|c|c|a|a|g|a|t|c|t|t|g|g|g|g|t|c|t|g|g|g|g|a|a|a|c|t|g|a|c|a|t|g|c|t|g|a|t|t|g|g|t|t|t|t|t|g|t|a|c|a|ei
t|t|t|c|g|c|a|a|c|g|g|g|t|t|t|g|c|c|g|c|c|a|g|a|a|c|a|g|g|t|a|a|g|t|g|c|c|g|t|g|t|g|t|g|g|t|t|c|c|c|g|c|g|g|g|c|c|t|ei
g|t|g|t|g|c|c|c|c|a|a|a|g|g|g|g|a|g|t|g|t|c|c|t|g|c|a|g|g|t|a|a|g|g|c|t|t|c|c|c|c|t|g|g|c|t|t|c|a|g|g|a|t|t|c|c|a|a|ei
g|a|g|c|t|c|a|t|t|t|t|t|t|a|a|a|a|a|t|c|c|a|a|t|g|t|a|c|a|t|t|a|g|a|c|t|a|a|a|c|g|t|g|a|a|a|t|t|a|t|c|t|c|t|t|a|t|t|ei
a|g|a|g|a|a|a|g|g|a|g|a|g|a|c|a|a|t|t|a|t|g|t|c|t|g|a|g|g|t|a|a|a|c|t|t|t|c|t|g|g|a|t|a|t|t|t|g|g|g|c|t|t|c|t|g|g|c|ei
a|t|g|a|g|a|a|g|a|a|c|t|g|g|g|g|g|c|t|g|t|c|t|t|t|a|t|g|g|t|a|g|g|c|a|t|g|c|t|t|a|g|c|a|g|c|c|c|c|a|a|a|c|t|c|a|t|g|ei
t|g|c|t|g|t|c|a|a|t|c|a|a|c|c|a|a|a|c|t|t|a|c|g|g|a|a|g|g|g|a|g|g|c|c|c|c|g|a|t|c|t|g|c|t|g|t|c|a|a|t|c|a|t|c|a|a|a|ei
g|a|c|c|g|c|t|t|c|c|c|a|t|a|c|c|t|g|g|c|t|c|t|t|c|a|a|g|g|t|a|a|g|g|g|c|t|g|g|g|c|c|a|c|c|t|c|a|g|a|g|t|c|c|t|c|c|a|ei
g|a|t|t|c|t|c|g|g|g|c|c|g|a|t|g|t|t|c|t|c|a|g|a|a|a|a|g|g|t|a|a|t|g|g|c|t|t|c|g|c|g|g|g|g|c|t|g|g|g|g|t|g|g|a|g|c|t|ei
a|g|t|t|a|g|t|g|g|g|t|g|c|a|g|c|g|c|a|g|c|a|g|a|g|g|c|a|c|a|t|g|t|a|t|a|c|a|t|a|t|g|t|a|a|c|t|a|a|c|t|t|g|c|a|c|a|a|ei
c|c|a|a|a|g|g|a|a|c|a|g|a|a|g|t|a|t|t|c|a|t|t|c|g|c|a|g|a|a|c|c|c|c|c|a|g|a|c|c|t|c|c|c|t|c|t|g|t|t|t|c|t|c|a|g|a|g|ei
t|g|c|t|c|t|c|c|c|a|g|g|t|c|t|a|c|c|c|t|g|a|a|t|c|a|g|a|t|c|a|c|c|a|a|t|g|t|g|g|t|a|g|a|a|g|c|c|a|a|c|c|a|a|c|c|a|g|ei
a|t|g|a|a|a|g|c|c|t|a|c|a|a|c|g|c|a|c|g|t|t|a|t|g|c|t|t|t|a|t|a|g|a|t|t|t|t|t|t|t|t|a|a|t|t|t|t|a|a|g|t|t|t|t|a|t|g|ei
a|g|a|c|a|g|g|a|c|a|a|c|a|t|t|g|c|g|g|c|t|t|a|c|t|c|c|t|c|t|g|t|t|g|c|c|a|t|c|a|t|g|g|a|c|c|t|c|t|c|g|c|a|c|c|c|c|g|ei
t|c|c|c|g|t|g|c|c|c|t|g|g|g|a|g|c|g|g|g|t|t|c|g|a|c|c|g|c|g|g|a|t|c|g|g|a|a|g|t|g|a|g|a|a|t|c|c|c|a|g|c|t|g|t|g|t|g|ei
g|a|c|a|t|c|a|c|a|g|t|a|a|c|c|a|t|g|t|c|t|t|t|t|c|t|a|g|g|a|t|c|t|g|t|t|c|c|g|g|t|c|t|a|c|t|a|t|g|a|a|g|c|c|c|g|t|c|ei
a|a|t|c|c|t|a|a|t|g|t|g|a|t|t|t|a|g|t|a|a|a|c|t|a|g|c|t|a|a|a|g|t|t|t|c|t|c|a|t|t|c|c|t|c|c|a|t|g|t|g|a|g|g|g|c|a|t|ei
a|t|c|t|c|a|c|t|g|a|t|c|c|c|t|t|c|t|g|c|c|c|c|c|t|t|a|g|g|a|t|t|c|t|g|t|c|a|a|c|t|g|a|a|t|c|t|g|c|c|a|t|c|t|g|g|a|a|ei
a|g|g|g|c|a|c|a|g|a|t|g|t|t|a|c|a|g|c|t|c|a|g|c|c|c|a|g|g|g|c|c|a|g|c|t|c|c|a|g|g|c|t|a|g|t|t|a|c|c|t|g|t|g|a|g|g|c|ei
c|t|t|g|c|c|c|c|a|c|c|g|c|a|c|c|a|c|a|c|g|g|c|c|g|c|a|g|g|t|g|a|c|t|c|t|c|c|g|a|g|g|g|t|t|g|g|g|g|a|t|g|a|g|t|g|a|g|ei
c|a|c|c|a|a|g|t|t|c|c|t|g|g|a|a|a|a|t|g|a|a|g|c|g|a|a|g|g|t|g|a|t|t|c|c|c|c|a|a|c|c|t|g|a|g|g|g|t|g|a|c|c|a|a|g|a|a|ei
a|t|t|g|g|t|g|g|c|a|g|a|a|g|a|g|g|a|a|g|a|t|t|c|g|a|a|g|a|g|t|g|c|a|g|c|t|g|c|c|t|g|a|a|c|c|g|a|g|c|c|c|t|g|c|c|g|a|ei
c|a|t|a|c|t|t|g|t|g|c|t|a|t|c|c|c|c|t|g|c|c|c|t|t|a|a|a|t|c|t|c|a|t|t|g|t|g|t|a|t|t|t|t|a|a|a|t|t|a|a|g|a|g|a|a|t|a|ei
g|a|a|a|t|g|c|a|a|g|a|a|a|c|g|g|g|t|c|a|c|c|a|c|t|g|g|t|g|g|a|g|g|g|a|g|g|a|g|a|g|a|t|t|g|a|g|c|t|g|t|t|t|g|a|c|g|g|ei
c|a|g|a|c|t|a|t|a|c|g|g|c|t|g|a|g|t|g|c|a|a|g|c|c|a|a|g|g|t|g|t|g|t|t|c|a|g|a|g|c|c|c|a|g|g|t|g|g|g|t|g|g|g|c|t|g|g|ei
g|g|a|t|t|c|c|c|c|t|g|a|c|t|c|c|a|c|c|t|c|t|t|c|c|c|a|g|a|c|g|g|c|t|g|c|c|a|c|g|c|c|g|a|c|c|c|t|g|c|c|t|g|c|g|a|c|g|ei
g|c|t|g|a|c|t|g|c|c|a|g|a|t|g|a|c|t|t|g|t|g|a|a|c|c|a|a|a|a|c|c|c|a|t|g|t|t|t|t|c|c|c|a|t|a|c|a|a|c|t|c|c|c|g|g|a|g|ei
g|g|c|a|c|c|g|a|g|c|a|g|t|t|c|g|c|g|t|c|c|a|t|c|g|g|a|c|c|t|g|t|a|c|a|t|c|a|a|g|a|a|c|g|g|c|c|a|g|g|g|c|t|t|c|a|t|c|ei
t|g|t|a|c|c|c|t|t|c|c|a|t|t|c|t|g|a|t|t|t|g|a|g|a|t|a|a|t|c|t|g|g|c|a|c|t|c|c|t|a|t|c|t|t|g|a|a|g|a|c|c|t|a|g|t|t|g|ei
t|c|t|a|a|t|t|t|g|g|a|c|c|g|a|c|t|a|g|g|c|a|a|t|a|g|a|g|g|t|g|a|g|a|t|c|c|t|a|a|g|g|g|a|t|t|a|g|g|a|c|a|a|g|g|a|g|a|ei
a|c|c|t|t|t|g|g|c|t|c|g|g|g|a|g|a|g|g|c|a|g|a|t|t|g|g|g|c|t|g|c|g|a|c|c|t|c|t|g|t|t|c|g|a|g|a|a|g|a|a|g|t|c|g|c|t|g|ei
c|c|c|t|c|g|t|g|c|g|g|t|c|c|a|c|g|a|c|c|a|a|g|c|a|g|c|g|g|t|g|a|g|c|c|a|c|g|g|g|c|a|g|g|c|c|g|g|g|g|t|c|g|t|g|g|g|g|ei
c|c|c|a|t|c|t|t|a|a|t|c|c|c|g|a|g|a|g|t|c|c|g|a|g|g|c|t|g|t|g|c|t|a|c|c|c|c|a|a|g|a|a|g|a|g|g|a|a|g|g|a|t|c|a|g|g|g|ei
c|a|g|g|g|a|g|g|c|a|c|c|c|c|c|a|c|g|c|c|t|g|g|t|g|g|c|t|g|a|t|g|t|t|t|g|t|g|t|t|t|t|t|a|g|t|a|g|g|c|a|c|g|c|c|g|t|g|ei
t|g|g|g|g|c|t|t|g|g|c|c|t|g|g|c|t|g|c|c|c|c|g|t|a|c|g|c|c|a|c|t|t|c|t|c|t|c|c|c|g|c|c|c|c|c|a|g|a|c|a|c|c|a|a|t|g|g|ei
g|t|t|g|a|g|g|g|g|g|c|t|g|t|g|a|c|c|c|a|t|g|a|c|t|g|c|c|a|t|t|g|c|a|c|t|c|c|a|g|c|c|t|a|g|g|t|g|a|c|a|g|a|g|g|g|a|g|ei
a|t|t|g|a|a|a|c|a|c|a|g|a|g|c|a|c|c|a|g|c|t|c|g|g|g|a|a|c|t|c|g|t|c|c|c|a|a|g|c|c|c|c|c|c|a|t|c|t|c|c|a|c|t|t|c|c|t|ei
t|t|t|g|c|t|t|c|a|g|t|c|c|t|t|g|a|a|t|c|a|c|c|g|g|g|g|a|c|t|t|g|a|g|g|a|c|t|c|g|g|g|a|t|c|t|t|c|a|g|g|a|c|g|c|c|t|g|ei
t|c|a|t|c|t|c|t|t|a|t|a|g|a|t|t|a|a|c|t|t|c|c|t|c|a|a|a|a|t|g|t|c|a|c|c|a|t|t|c|c|t|g|t|a|c|c|t|g|g|t|t|c|t|c|t|t|g|ei
a|c|g|g|a|g|c|g|g|g|t|g|c|g|g|t|t|c|c|t|g|c|a|a|a|g|a|c|a|t|c|t|a|t|a|a|c|c|a|a|g|a|g|g|a|g|g|a|c|t|t|g|c|g|c|t|t|c|ei
g|g|g|c|t|g|c|g|t|t|g|c|t|g|g|t|c|a|c|a|t|t|c|t|g|c|a|g|g|t|a|t|g|g|g|g|g|c|g|g|g|g|c|t|t|g|c|t|c|g|g|t|t|c|c|c|c|c|ei
a|c|g|a|c|c|t|g|c|a|c|g|c|c|a|c|c|a|a|g|c|t|g|c|c|c|c|g|g|t|g|a|g|a|g|c|a|c|c|c|c|c|c|g|c|t|c|c|g|g|c|c|g|g|g|g|a|t|ei
t|g|g|g|a|t|t|c|c|c|c|a|g|a|a|g|g|t|t|c|t|g|t|t|t|c|a|g|g|t|g|g|g|g|c|a|a|g|t|t|c|c|g|t|g|g|g|c|a|t|c|a|t|g|t|t|g|a|ei
c|t|c|t|g|t|c|c|t|t|a|t|c|a|a|c|t|t|t|c|a|t|c|c|a|c|a|g|t|a|t|t|t|t|t|c|c|t|g|t|g|a|a|c|a|g|c|c|a|t|g|c|a|a|c|c|a|a|ei
t|g|a|c|t|g|c|g|g|g|g|a|c|g|g|c|t|c|t|g|a|c|g|g|a|g|g|a|c|t|g|c|a|g|c|a|t|c|g|a|c|c|c|c|a|a|g|c|t|g|a|c|c|a|g|c|t|g|ei
a|a|a|g|a|g|t|c|c|a|g|g|a|c|c|a|g|a|t|g|g|a|t|c|c|a|g|c|c|a|a|a|t|t|c|t|a|c|c|a|g|a|g|g|t|a|c|a|a|g|g|t|g|g|a|a|c|t|ei
t|t|c|c|a|a|c|c|a|a|g|c|t|c|a|t|t|t|c|c|t|t|t|t|t|c|a|g|c|a|a|a|c|c|t|c|g|g|a|c|a|g|c|c|a|a|c|a|a|t|t|c|a|g|a|g|t|t|ei
c|a|a|a|t|t|g|t|g|g|a|c|g|t|g|a|t|t|c|c|c|t|t|c|c|a|g|g|g|t|g|a|g|g|a|c|c|t|g|g|a|g|c|c|t|a|g|a|c|a|c|c|c|c|t|g|g|g|ei
a|a|t|g|a|c|t|g|g|g|a|a|g|a|c|c|a|c|t|t|g|g|c|g|c|a|a|g|g|t|g|t|g|a|g|a|a|g|c|c|t|t|t|g|c|a|t|g|t|t|g|g|c|t|c|a|a|c|ei
g|g|a|c|g|a|a|g|t|t|g|g|t|g|g|t|g|a|g|g|c|c|c|g|g|c|a|g|g|t|t|g|g|t|a|t|c|a|a|g|g|t|t|a|c|a|a|g|g|c|a|g|g|t|t|t|a|a|ei
g|a|t|c|t|g|g|a|g|g|a|c|a|g|c|t|a|t|g|g|a|c|a|g|g|t|g|g|g|t|g|a|g|t|g|g|t|g|c|t|g|t|g|t|a|a|a|c|a|c|a|g|c|g|c|a|c|a|ei
c|c|a|g|t|c|a|c|c|a|c|a|g|g|a|c|c|c|c|t|t|g|t|c|a|c|a|g|g|t|c|t|c|t|t|t|g|a|g|c|c|t|g|g|a|g|a|c|a|t|g|a|a|a|t|a|c|g|ie
t|a|c|c|t|a|a|a|c|a|a|c|a|t|g|t|g|c|t|c|c|a|c|t|t|c|a|g|a|a|c|c|t|a|t|c|t|t|c|t|t|c|g|a|c|a|c|a|t|g|g|g|a|t|a|a|c|g|ei
t|t|c|a|g|c|t|c|a|c|t|g|c|a|a|a|c|g|c|c|g|c|c|c|t|g|g|g|t|t|c|a|a|g|c|a|g|t|t|c|t|c|c|t|a|c|c|t|c|a|g|c|c|a|c|c|c|a|ei
g|c|c|a|c|t|t|c|a|g|c|a|a|g|t|t|c|a|t|t|c|c|t|a|g|g|c|t|c|c|c|a|g|a|g|a|g|t|g|g|g|g|c|t|g|g|t|t|g|c|c|a|g|t|c|a|g|a|ei
t|c|a|a|t|c|t|a|a|g|g|c|t|t|t|t|g|t|g|a|t|c|g|c|a|c|a|g|g|t|g|a|c|a|a|t|c|t|c|c|a|a|t|a|g|a|c|t|t|g|t|g|t|c|t|t|c|a|ei
g|a|a|t|t|t|a|c|t|g|a|a|a|g|c|a|g|t|t|a|g|c|a|g|a|a|a|g|g|t|a|g|g|t|t|t|g|c|t|g|t|t|g|c|c|t|g|c|a|g|c|c|g|a|a|t|t|g|ei
t|a|t|t|c|t|g|c|c|a|a|t|c|a|c|a|t|t|t|c|t|c|t|c|a|c|t|a|t|g|c|c|t|t|g|t|g|a|t|a|t|a|g|t|t|t|g|g|c|t|c|t|g|t|c|c|c|c|ei
a|a|g|t|t|c|c|t|g|g|c|t|t|c|t|g|t|g|a|g|c|a|c|g|g|c|t|g|a|c|c|t|c|c|a|a|a|t|a|c|c|g|t|t|a|a|g|c|t|g|g|a|g|c|c|t|c|g|ei
g|g|a|g|a|t|g|a|t|c|t|c|t|c|a|a|c|t|t|t|a|a|c|g|a|a|a|g|g|t|a|t|g|t|a|t|c|t|t|g|a|a|a|g|g|g|a|a|g|a|a|a|a|a|a|a|a|g|ei
g|g|c|g|c|c|t|g|t|g|c|c|c|a|c|g|c|t|g|c|t|g|c|t|c|t|c|c|a|g|a|c|a|t|t|t|t|g|t|t|c|t|t|g|a|a|t|c|t|g|t|g|a|g|a|c|c|c|ei
t|g|g|g|c|t|g|c|a|t|c|c|t|g|c|t|g|g|a|t|c|g|g|g|c|g|t|g|g|g|a|g|a|t|a|c|t|c|c|c|t|c|g|a|g|a|a|a|g|g|a|a|g|a|a|g|a|c|ei
t|c|t|c|c|t|c|c|c|a|g|a|a|c|g|t|c|a|c|a|g|t|g|t|a|g|a|g|g|t|g|a|g|a|c|a|a|g|c|c|c|c|t|a|a|c|a|a|g|g|t|c|a|a|g|t|g|a|ei
t|g|g|c|c|a|t|c|a|g|c|a|t|c|g|c|t|c|t|c|c|t|g|t|a|c|a|g|g|t|a|c|c|c|g|g|c|a|t|g|g|g|g|c|a|g|g|a|c|t|g|g|g|g|c|t|c|c|ei
g|c|a|a|a|a|a|g|a|a|t|g|c|c|c|t|g|t|g|c|a|g|a|g|c|t|a|t|g|t|g|a|g|t|c|t|t|t|a|a|a|a|a|a|a|t|a|t|a|a|t|a|a|a|t|t|a|a|ei
g|a|c|a|t|c|g|a|g|a|t|c|g|c|c|a|c|c|t|a|c|c|g|a|a|c|t|g|c|t|g|g|a|g|g|g|c|g|a|g|g|a|g|t|a|c|a|g|a|a|t|g|t|c|t|g|g|a|ei
a|g|a|t|g|c|t|t|t|c|c|t|a|a|g|c|c|a|g|a|g|g|a|g|g|t|g|a|g|c|c|c|a|a|a|g|g|a|c|c|c|t|t|g|a|t|c|a|a|t|t|c|t|g|a|a|t|t|ei
t|c|t|t|c|c|c|a|g|t|c|c|a|c|c|g|t|c|c|c|c|a|t|g|g|g|g|c|a|t|t|g|t|t|g|c|t|g|g|c|c|t|g|g|c|t|g|t|c|c|t|a|g|c|a|g|t|t|ei
g|c|a|g|g|g|t|t|g|t|g|a|t|g|a|g|g|c|t|c|t|c|g|t|g|c|a|g|g|t|g|g|a|g|g|t|t|c|a|a|g|a|c|g|g|c|c|c|c|a|a|t|g|a|a|g|a|t|ei
c|a|c|c|t|g|c|c|a|t|g|t|g|c|a|g|c|a|t|g|a|g|g|t|t|g|c|c|c|a|a|g|c|c|c|c|t|c|a|c|c|c|t|g|a|g|a|t|g|g|g|a|g|c|c|g|t|c|ei
g|c|c|c|a|t|t|c|c|t|g|c|t|c|a|c|c|t|g|c|t|g|g|g|a|c|a|t|g|t|g|g|g|c|g|c|a|g|a|c|c|t|g|g|t|c|c|a|a|c|a|t|c|t|a|t|g|a|ei
a|t|g|t|t|a|t|a|g|t|a|a|a|t|t|t|a|t|t|t|t|a|t|t|a|g|a|t|a|t|t|a|a|a|t|g|a|t|g|t|t|t|t|a|t|t|a|g|a|t|a|a|a|t|t|t|c|a|ei
c|a|g|c|c|c|t|g|a|c|a|c|t|g|c|c|c|t|g|c|t|t|t|c|g|c|a|g|c|c|c|t|t|c|t|t|c|a|c|c|g|a|t|g|a|g|t|g|c|a|c|g|t|t|c|a|a|g|ei
g|g|g|t|g|g|g|g|a|g|g|a|g|c|a|g|a|t|c|c|a|a|g|t|t|g|c|g|g|g|g|t|c|t|a|a|a|g|c|t|g|t|g|t|g|t|g|t|t|g|a|g|g|g|g|g|a|t|ei
g|a|a|a|a|g|g|a|g|g|g|a|g|c|t|a|c|t|c|t|a|a|g|c|g|a|g|t|g|t|a|a|g|t|g|c|g|g|g|g|c|g|g|g|a|g|c|g|t|g|g|a|g|g|a|g|c|t|ei
t|g|c|g|c|g|g|c|t|a|c|t|a|c|a|a|c|c|a|g|a|g|c|a|g|c|c|g|g|t|g|a|g|t|g|a|c|c|c|c|g|g|c|c|c|g|g|g|g|c|g|c|a|g|g|t|c|a|ei
g|t|g|t|t|g|g|g|c|a|a|c|a|a|a|t|g|a|t|c|t|t|t|a|g|a|a|c|a|t|g|g|t|t|t|t|a|g|g|c|g|g|a|c|c|a|c|a|c|c|g|c|c|c|a|c|a|a|ei
g|c|c|c|c|a|g|c|t|c|a|c|c|c|a|a|c|a|c|c|a|g|c|t|t|c|t|a|a|g|a|a|c|c|c|a|g|g|a|t|t|t|c|t|t|g|t|g|a|g|g|t|c|t|c|t|g|t|ei
c|a|g|c|t|c|a|g|c|a|g|c|c|g|c|c|g|c|c|a|g|a|g|a|g|a|c|g|a|a|c|c|g|c|c|a|a|t|c|g|c|a|a|g|g|c|a|c|c|t|c|t|g|a|g|a|a|c|ei
c|t|c|c|a|c|t|t|a|a|g|g|a|c|c|a|t|g|g|c|c|t|g|g|c|t|c|t|t|t|t|c|c|a|g|g|g|a|t|g|g|a|g|t|c|t|g|c|t|g|g|c|a|t|c|c|a|t|ei
g|g|a|c|c|a|g|a|a|t|t|g|a|g|a|g|a|g|g|a|a|t|t|t|t|a|a|a|c|t|c|c|a|g|a|a|c|a|a|g|a|c|c|a|a|g|c|t|g|a|c|a|g|t|g|c|t|g|ei
a|t|t|g|g|c|t|t|a|g|t|c|c|g|a|c|c|t|g|g|t|a|c|g|t|c|t|g|g|a|g|t|t|g|c|t|g|g|a|a|g|c|c|c|a|a|g|c|a|g|c|t|a|c|t|g|g|c|ei
t|t|t|g|g|a|a|c|c|t|a|g|a|c|a|t|c|c|c|c|c|c|t|g|c|t|g|g|a|c|t|c|t|g|a|g|c|t|g|a|c|c|g|a|a|t|t|c|c|c|c|c|t|g|c|g|c|a|ei
t|g|a|t|g|c|c|t|g|c|t|t|g|t|c|c|c|t|g|c|c|c|a|a|t|t|c|c|c|a|g|c|t|g|c|c|t|g|t|g|t|c|a|g|c|t|t|g|t|c|c|c|c|c|t|g|a|g|ei
g|t|g|g|a|g|a|a|g|a|t|t|g|g|g|g|g|c|t|g|g|c|t|a|g|a|a|a|a|a|t|g|t|g|c|t|g|g|t|g|g|t|a|g|c|t|g|c|a|g|c|a|g|c|c|c|t|t|ei
c|t|t|c|a|g|c|c|t|c|c|c|a|a|g|t|a|g|c|t|g|g|t|c|a|c|a|g|g|g|c|a|c|a|c|g|t|g|t|t|t|c|a|c|g|t|t|g|a|c|a|g|g|t|t|t|g|c|ei
t|g|a|c|a|t|g|c|t|g|g|a|g|t|c|t|a|g|a|a|c|c|t|c|a|a|a|c|t|c|a|t|t|t|g|g|t|g|t|t|g|a|g|a|a|t|t|g|c|c|t|g|a|g|g|t|g|c|ei
c|t|g|t|t|c|t|c|t|t|t|g|g|c|t|g|t|g|t|g|t|g|c|t|g|t|a|g|t|t|a|t|g|t|c|a|c|g|c|a|t|c|t|g|a|t|g|a|a|g|c|g|a|a|t|t|c|a|ei
t|g|t|c|t|g|a|a|t|t|t|t|c|t|g|a|c|t|c|t|t|c|c|g|g|c|a|g|a|a|c|a|c|c|c|a|a|a|g|a|c|a|c|a|c|g|t|g|a|c|c|c|a|c|c|a|t|c|ei
c|c|t|c|a|c|c|a|c|c|a|c|c|a|c|g|t|g|t|c|t|c|c|a|c|a|g|c|c|t|c|t|g|a|g|c|t|t|c|t|c|a|t|t|c|a|c|a|g|a|g|a|c|a|c|c|c|t|ei
g|t|g|c|t|t|g|a|a|t|t|t|t|c|t|g|a|c|t|c|t|t|c|t|t|c|a|g|a|c|c|c|c|c|c|c|a|a|g|a|c|a|c|a|c|g|t|g|a|c|c|c|a|c|c|a|c|c|ei
t|g|c|t|c|c|g|c|t|a|c|t|a|c|a|a|c|c|a|g|a|g|c|a|g|c|c|g|g|t|g|a|g|t|g|a|c|c|c|c|g|g|c|c|c|g|g|g|c|g|c|a|g|g|t|c|a|c|ei
t|t|t|t|a|a|g|a|a|g|c|t|c|a|t|a|t|c|a|c|t|t|g|c|t|t|t|t|c|a|t|t|c|c|a|t|a|t|t|t|c|t|t|a|c|c|c|t|t|t|t|a|t|c|t|a|c|t|ei
g|a|t|t|t|t|c|a|c|c|t|t|g|a|c|c|c|c|t|g|t|c|a|t|t|g|t|g|a|a|c|a|c|t|g|a|a|g|c|t|t|t|c|t|t|t|g|g|a|c|a|a|g|g|c|a|c|c|ei
t|g|c|g|c|g|g|c|t|a|c|t|a|c|a|a|c|c|a|g|a|g|c|a|g|c|c|g|g|t|g|a|g|t|g|a|c|c|c|c|g|g|c|c|c|g|g|g|c|g|c|a|g|g|t|c|a|c|ei
a|a|a|g|g|t|a|a|t|g|a|g|c|c|t|g|t|g|a|g|g|a|g|g|c|c|t|g|c|c|a|c|c|t|g|t|c|c|c|a|g|a|c|c|t|t|c|c|c|c|a|c|t|c|c|c|a|c|ei
g|a|a|t|t|g|t|a|t|c|a|t|t|t|g|a|a|c|a|a|c|t|a|g|t|t|c|a|g|c|a|t|a|t|t|t|a|t|a|g|c|a|a|t|c|c|a|t|g|t|t|a|g|t|t|t|t|t|ei
c|t|a|a|a|g|a|t|c|t|c|a|a|t|t|t|c|c|t|t|t|c|t|t|g|c|a|g|a|g|t|c|c|a|g|c|c|t|c|t|g|a|t|g|a|a|g|c|a|g|g|a|g|a|g|a|a|a|ei
t|c|a|g|t|a|a|t|t|a|a|c|c|a|t|c|t|t|c|c|t|g|t|t|t|c|a|g|t|t|g|t|a|g|a|g|t|a|t|a|a|a|a|t|t|g|c|g|g|a|t|a|t|g|g|g|a|c|ei
c|c|a|a|t|c|a|c|a|g|g|a|g|a|a|g|g|a|g|g|a|g|g|g|a|g|g|a|g|g|a|g|g|g|c|t|g|c|t|t|g|a|g|g|a|a|g|t|a|t|a|a|g|a|a|t|g|a|ei
a|g|g|a|g|g|g|a|g|c|t|g|a|c|t|g|a|t|a|c|a|c|t|c|a|g|c|g|g|t|a|g|g|t|a|c|t|c|t|g|t|g|g|g|t|t|g|c|t|c|c|t|t|t|t|t|a|a|ei
c|c|t|t|c|a|g|c|t|c|a|g|c|t|c|a|g|g|a|c|t|t|a|a|g|a|a|g|g|t|a|a|g|c|c|g|a|a|t|t|g|g|g|g|g|a|a|g|a|t|a|t|t|g|t|g|a|c|ei
g|g|a|a|g|c|a|g|a|t|c|a|a|a|g|a|t|t|a|g|t|g|t|c|t|t|a|g|g|t|g|g|a|g|c|t|g|g|t|g|c|a|a|c|t|g|g|t|c|a|t|c|g|a|t|g|g|a|ei
a|c|t|a|t|a|a|t|g|a|a|t|a|c|t|t|c|a|g|g|g|a|t|t|a|a|t|g|t|a|a|g|t|a|a|t|t|g|c|t|t|c|t|t|t|t|t|c|t|c|a|c|t|c|a|t|t|t|ei
g|a|t|a|c|c|c|t|t|a|t|t|c|c|c|t|g|t|g|g|a|t|g|c|t|c|a|g|g|c|c|t|g|c|t|a|c|t|g|a|c|c|c|t|g|c|a|g|c|c|a|g|a|a|c|a|g|a|ei
t|a|g|c|t|c|a|a|t|g|c|c|a|a|c|a|c|t|t|t|t|t|t|t|c|t|t|t|t|t|c|t|t|t|g|c|a|t|t|t|a|a|c|a|t|t|g|t|c|t|t|g|g|a|g|c|t|g|ei
g|c|c|a|t|t|t|c|t|a|t|g|t|c|c|t|t|t|a|t|a|t|g|a|c|a|a|a|t|a|c|t|g|t|t|c|t|g|g|a|g|c|a|g|a|g|g|c|a|c|c|t|t|t|a|g|a|t|ei
g|a|g|c|c|c|t|g|g|c|c|c|t|g|a|c|c|g|a|g|a|c|c|g|g|c|c|t|g|t|g|a|g|t|g|c|g|g|g|g|t|t|g|g|g|a|g|g|g|a|a|a|c|g|g|c|c|t|ei
a|c|g|g|c|t|c|c|c|g|g|g|a|c|c|t|c|g|g|c|a|g|g|t|g|a|a|g|g|t|a|t|g|a|g|c|c|t|c|c|t|c|t|c|c|t|t|t|t|g|c|c|c|a|t|t|g|c|ei
a|t|c|t|g|c|a|a|a|a|t|t|t|t|c|t|c|a|a|g|g|t|a|g|c|t|g|g|a|c|t|c|t|g|g|c|a|g|g|t|c|t|g|a|c|c|c|a|g|c|c|t|c|a|c|c|g|c|ei
g|g|t|g|g|c|c|a|c|c|g|c|c|a|g|a|g|c|t|c|c|t|g|c|a|c|a|t|c|t|t|g|g|c|g|t|g|g|c|a|g|c|c|t|c|t|t|g|a|c|t|c|t|g|a|c|t|c|ei
t|a|a|t|a|c|a|a|a|c|a|g|a|a|a|t|c|a|g|a|c|c|t|t|a|g|a|g|t|t|g|a|g|a|g|t|a|a|g|t|a|g|g|a|g|a|g|t|t|a|g|g|a|c|t|t|g|t|ei
c|c|g|g|g|t|g|a|a|c|g|t|g|g|a|g|a|g|a|c|t|g|g|c|c|c|c|c|g|g|a|c|c|a|g|c|g|g|g|a|t|t|t|g|c|t|g|g|g|c|c|t|c|c|t|g|g|t|ei
a|g|g|c|c|c|t|g|g|c|c|c|t|t|a|c|c|c|a|g|a|c|c|g|g|c|g|g|g|t|g|a|g|t|g|c|g|g|g|g|t|c|g|g|g|a|t|g|g|a|a|a|c|g|g|c|c|t|ei
c|t|g|g|t|g|t|g|g|a|g|g|g|a|c|t|c|c|c|t|c|c|a|t|a|c|t|t|t|c|a|g|a|c|c|t|c|a|c|t|c|c|c|c|a|t|g|c|t|g|c|t|c|c|c|a|c|a|ei
a|g|a|c|a|t|t|t|g|c|t|g|c|a|c|t|t|t|c|c|t|t|g|t|g|t|a|g|g|t|t|g|g|t|t|t|t|g|c|g|g|a|t|t|g|c|c|a|c|t|g|a|t|g|a|t|t|c|ei
t|g|g|c|c|t|t|g|a|c|c|c|t|g|c|a|g|c|c|c|c|g|c|g|g|a|g|g|g|t|a|g|g|t|c|c|g|c|g|t|g|g|a|g|a|g|g|g|a|c|g|g|g|g|a|g|c|c|ei
c|c|c|g|g|g|a|g|c|c|t|c|g|g|g|c|c|c|g|g|c|g|c|c|c|a|c|a|c|c|c|g|g|g|g|g|c|g|t|c|t|g|g|g|a|g|g|a|g|g|c|g|g|c|c|g|c|g|ei
g|g|a|t|c|c|c|t|a|g|t|a|t|a|a|c|a|c|a|t|t|c|a|t|t|t|c|c|c|c|n|t|t|t|c|a|g|c|c|c|n|t|t|t|c|a|g|t|c|t|t|a|c|t|a|c|t|t|ei
g|t|c|c|c|t|t|t|c|a|a|a|t|t|g|t|g|a|a|g|a|a|t|c|a|g|g|t|c|t|g|t|g|g|g|a|a|a|a|g|c|a|a|g|c|g|a|g|c|a|g|c|t|g|g|c|t|g|ei
a|g|t|g|t|t|t|t|c|a|t|a|t|t|g|c|t|t|c|t|c|c|c|t|a|g|t|t|c|t|g|c|t|g|t|c|t|c|c|c|t|g|a|a|g|a|g|t|g|a|a|c|c|c|t|c|t|t|ei
c|t|c|a|a|t|t|t|t|g|t|a|g|a|a|a|a|a|t|t|t|g|t|t|t|c|t|t|t|g|t|g|a|t|a|a|t|g|a|c|t|t|t|a|g|t|g|t|t|g|t|a|t|t|t|t|t|t|ei
g|t|a|g|a|t|t|t|t|a|t|c|a|g|a|c|t|g|a|a|g|a|g|t|t|t|g|t|g|t|g|a|g|t|a|t|a|t|t|t|a|a|t|a|t|a|t|g|a|t|t|c|t|t|t|t|t|a|ei
g|t|c|g|t|c|c|t|c|a|c|g|g|t|t|a|c|t|c|t|t|t|g|g|t|g|g|g|a|t|c|t|t|t|g|c|c|t|g|a|t|c|t|t|t|g|c|a|a|a|a|t|c|a|g|g|a|g|ei
g|g|g|a|t|g|g|a|g|t|t|t|t|c|a|a|g|t|c|c|t|t|c|a|a|g|a|g|g|t|a|a|g|a|g|a|g|a|g|a|g|c|t|c|c|c|a|a|t|c|a|g|c|a|t|t|g|t|ei
g|a|c|a|a|c|t|t|c|c|c|c|a|g|a|t|a|c|c|c|c|g|t|g|c|a|a|g|t|t|c|t|t|c|c|a|a|t|a|t|g|a|c|a|c|c|t|g|g|a|a|g|c|a|g|t|c|c|ei
a|t|g|a|t|g|t|t|t|g|c|c|t|c|c|g|c|c|c|t|g|c|c|g|t|c|t|g|c|t|g|g|t|c|t|t|c|a|t|c|c|t|c|a|t|a|t|t|c|c|t|g|g|a|g|t|c|t|ei
t|c|a|g|a|c|c|t|g|g|g|c|g|g|g|a|t|g|c|c|c|a|a|a|g|a|g|c|c|a|g|g|t|g|c|c|a|g|g|g|t|t|c|c|t|g|t|c|t|g|g|c|a|c|a|g|t|c|ei
g|g|g|c|g|g|g|t|c|t|c|a|g|c|t|c|c|t|c|c|t|c|g|t|c|c|a|g|g|c|t|c|c|c|a|c|t|c|c|a|t|g|a|g|g|t|a|t|t|t|c|t|a|c|a|c|c|a|ei
c|t|c|a|c|t|g|t|g|t|c|t|c|t|c|c|t|c|c|t|t|t|a|c|t|t|a|g|g|g|t|g|a|t|t|c|t|g|g|g|g|g|t|c|c|a|c|t|t|g|t|c|t|g|t|a|a|t|ei
a|c|a|a|a|a|t|c|a|a|g|a|g|g|t|c|a|c|t|a|a|t|t|a|a|t|a|t|c|t|a|t|t|t|t|g|a|g|t|t|g|c|c|t|t|t|g|a|g|a|c|t|t|c|c|a|c|g|ei
t|g|a|c|g|c|c|c|t|c|a|a|g|g|g|c|a|c|t|g|t|g|a|t|c|c|t|g|c|c|c|a|c|c|t|g|g|g|c|c|a|g|g|c|c|c|t|g|c|c|c|c|t|t|c|t|c|t|ei
c|t|g|c|a|a|a|t|g|c|a|a|a|g|a|g|t|g|c|a|a|a|t|c|c|c|t|c|c|t|g|c|a|a|g|a|a|a|a|g|c|t|g|c|t|g|c|t|c|c|t|g|c|t|g|c|c|c|ei
g|c|t|g|g|a|a|g|a|g|g|g|c|a|a|a|g|t|g|g|a|c|g|g|g|t|g|g|a|c|a|g|g|a|g|t|g|g|a|t|g|c|g|a|t|a|a|g|a|t|g|t|g|g|t|t|t|g|ei
g|g|a|g|a|a|g|a|g|a|g|a|a|g|a|g|g|a|a|g|a|g|g|a|a|g|g|a|a|g|a|g|a|g|g|a|a|g|c|g|g|a|g|g|g|a|a|c|t|g|c|g|g|c|c|a|g|g|ei
g|a|a|a|t|a|a|c|c|g|a|t|g|c|a|t|t|c|t|t|t|c|t|g|t|t|a|g|g|c|a|t|c|a|t|c|t|g|g|g|g|a|g|a|g|g|a|t|a|c|a|c|t|g|a|t|g|g|ei
g|t|a|t|a|a|c|c|c|t|g|c|g|a|t|g|c|c|t|g|t|a|t|t|a|c|a|g|g|t|g|a|g|a|g|c|a|c|a|g|t|a|a|g|g|a|c|t|a|t|t|g|c|t|a|t|g|g|ei
a|c|c|c|c|t|t|c|a|c|g|t|c|t|t|t|g|c|t|t|g|t|c|t|g|c|a|g|g|a|t|g|t|t|c|c|t|g|t|c|c|t|t|c|c|c|c|a|c|c|a|c|c|a|a|g|a|c|ei
g|g|c|a|c|a|c|c|c|t|a|t|a|a|c|a|a|t|g|a|a|a|g|c|c|a|c|a|c|c|g|a|g|a|g|c|t|a|c|g|c|t|c|a|t|c|a|c|c|t|t|t|c|t|c|t|g|t|ei
c|t|t|t|c|t|c|c|a|a|a|c|a|t|a|a|a|a|t|a|t|t|t|t|a|t|a|g|c|t|a|c|c|t|g|c|c|t|t|t|c|t|g|g|a|a|g|a|a|c|t|t|t|g|c|c|a|t|ei
c|c|t|c|c|a|g|a|g|g|t|a|a|c|t|g|t|g|c|t|c|a|c|a|c|a|g|c|c|c|t|g|t|g|g|a|a|c|t|g|a|g|a|g|a|g|c|c|c|a|a|c|g|t|c|c|t|c|ei
c|a|g|g|c|t|g|g|a|g|t|g|c|a|g|t|g|g|c|a|c|g|a|c|c|t|g|c|t|c|a|t|t|g|c|a|a|g|c|t|c|c|g|c|c|t|c|c|t|g|g|g|t|t|c|a|c|g|ei
t|c|g|g|g|c|t|t|c|c|g|g|a|g|c|t|t|t|g|g|c|g|g|a|c|t|a|g|g|g|g|a|g|g|a|t|g|g|c|g|g|a|g|t|c|t|t|c|g|g|a|t|a|a|g|c|t|c|ei
a|t|a|g|a|g|c|a|g|g|a|g|g|g|t|c|c|g|g|a|g|t|a|t|g|g|a|c|g|g|g|g|a|g|a|c|a|c|g|g|a|a|a|g|t|g|a|a|g|g|c|c|c|a|c|t|c|a|ei
c|g|g|g|a|g|a|t|c|t|t|c|a|a|g|g|a|c|g|c|g|g|a|a|g|a|c|g|g|t|g|a|g|c|c|c|a|g|c|c|t|c|g|g|g|g|c|g|c|c|c|c|g|c|g|c|g|g|ei
a|t|g|a|g|t|c|c|a|a|g|a|a|g|c|t|c|c|t|t|g|t|c|g|c|t|t|g|g|t|a|t|g|g|g|c|t|g|g|a|g|c|c|a|g|g|c|a|g|a|a|g|g|g|g|g|c|t|ei
t|c|g|g|c|a|a|c|c|c|c|c|g|c|a|a|g|t|c|c|a|a|g|t|a|t|c|t|g|c|c|a|g|g|c|c|a|c|g|g|g|t|t|t|c|a|g|t|c|c|c|c|g|g|c|a|g|a|ei
t|g|t|c|t|t|g|g|g|g|c|a|t|g|t|g|c|a|g|a|g|g|g|t|g|g|a|c|g|c|c|a|t|c|a|g|c|c|t|t|t|g|a|c|a|g|a|a|t|t|c|t|g|g|g|c|a|g|ei
c|t|g|g|g|a|a|g|t|g|c|t|g|t|g|a|a|a|t|a|g|a|t|c|a|g|g|g|c|c|a|c|g|t|g|c|t|a|c|g|a|g|g|a|c|c|a|g|g|g|c|a|t|c|a|g|c|t|ei
g|a|a|a|a|g|a|a|a|a|a|a|a|a|g|a|a|t|c|a|a|t|g|g|a|g|g|g|g|c|t|g|c|c|t|g|c|c|t|g|a|c|c|a|c|t|g|g|t|t|g|t|g|t|g|g|a|t|ei
t|t|t|t|a|g|a|a|c|a|t|t|t|t|c|a|t|c|a|c|c|c|c|a|a|a|g|a|a|a|c|c|c|t|g|c|a|c|c|c|a|t|t|a|g|c|a|g|t|c|c|c|t|c|c|a|c|a|ei
c|c|c|a|t|c|c|c|a|c|c|c|a|c|g|t|g|t|c|g|c|t|a|c|c|t|a|g|g|t|g|a|a|g|c|t|a|g|a|g|g|a|a|c|c|a|g|a|c|c|t|c|a|t|c|a|g|c|ei
t|a|a|c|g|g|g|t|g|c|g|t|g|g|t|g|t|c|t|c|g|g|c|c|g|c|a|g|g|g|c|g|t|c|a|t|g|g|t|c|g|g|t|a|t|g|g|g|t|c|a|g|a|a|a|g|a|t|ei
a|a|g|g|a|c|c|a|g|t|g|a|a|g|a|c|g|t|c|a|g|g|g|c|a|g|g|t|c|t|c|g|g|g|g|g|t|c|c|g|g|a|a|g|g|g|t|g|a|t|c|a|t|c|g|a|c|c|ei
t|a|g|g|t|c|c|t|c|c|t|g|c|t|c|t|c|c|a|t|a|t|c|c|c|c|a|g|t|g|g|g|g|t|t|t|g|a|t|a|g|a|g|a|a|c|t|c|a|g|a|a|g|c|g|t|g|g|ei
c|t|t|c|c|a|g|t|g|c|c|t|g|g|g|c|t|t|c|a|c|c|c|t|a|a|c|a|t|c|a|g|c|g|a|g|a|c|t|t|c|a|t|t|g|c|c|c|g|t|g|a|c|c|t|a|g|g|ei
a|t|a|t|t|c|c|t|a|a|g|t|a|a|a|a|c|a|g|a|t|a|a|t|c|c|t|c|t|c|a|a|c|t|a|t|a|t|c|a|a|g|t|a|g|a|c|t|a|a|a|a|t|a|t|t|g|t|ei
c|a|c|a|g|g|a|c|a|c|c|t|c|a|c|a|g|a|g|g|t|c|a|c|c|a|c|a|c|g|g|g|g|c|a|c|a|c|t|t|c|a|c|a|c|t|c|a|g|g|t|c|a|c|c|t|c|a|ei
c|c|t|t|c|c|t|t|c|c|t|g|g|g|t|g|a|g|t|g|g|a|g|c|g|t|c|t|c|c|c|g|g|c|t|c|t|g|c|c|t|g|a|c|a|t|g|a|g|g|g|t|t|a|c|c|c|c|ei
c|t|a|g|a|g|t|t|c|c|c|t|g|a|t|t|c|c|t|a|a|a|a|t|t|t|t|a|t|c|t|t|a|a|a|t|c|c|t|g|t|t|t|g|c|c|c|t|a|a|c|c|t|t|c|t|t|a|ei
a|a|g|c|t|g|a|g|a|g|t|g|g|a|c|c|c|t|g|t|c|a|a|t|c|a|a|g|g|t|g|a|g|c|c|a|c|c|a|g|t|c|g|g|g|t|g|g|g|g|a|g|g|g|t|g|a|g|ei
g|c|g|c|t|g|g|c|a|c|c|c|a|g|c|a|c|c|a|t|g|a|a|a|c|a|a|g|g|t|g|g|g|t|g|g|t|g|g|c|c|t|g|c|g|c|g|g|g|c|t|g|t|c|g|g|c|g|ei
g|a|g|g|t|g|g|g|c|t|c|g|g|c|c|g|a|a|g|t|a|g|t|a|a|g|a|g|g|t|g|a|g|g|g|c|c|t|g|g|g|c|t|g|g|c|c|a|t|g|g|g|g|t|c|c|c|t|ei
c|t|g|g|t|g|c|g|g|t|a|c|c|a|g|t|g|c|a|c|a|g|a|g|g|t|t|t|g|t|c|c|a|g|c|g|c|c|a|c|a|t|g|c|c|c|a|c|c|a|t|c|c|g|g|t|g|c|ei
a|c|c|t|t|t|g|g|c|t|t|c|t|c|a|g|c|a|g|g|c|a|g|t|a|c|t|g|a|g|g|a|g|a|c|t|t|g|g|g|g|t|c|t|t|c|c|t|g|g|c|t|c|a|c|t|a|t|ei
a|a|t|a|a|t|g|a|c|a|g|a|a|c|c|t|a|c|t|g|g|g|a|c|t|c|t|g|a|g|t|g|g|a|g|g|c|g|a|a|c|c|a|c|t|g|a|g|c|c|a|a|g|g|a|g|c|t|ei
c|t|c|t|t|c|a|a|t|a|c|c|t|t|t|g|g|t|t|t|t|g|g|a|g|a|t|c|t|c|a|g|g|a|a|c|g|g|c|c|t|g|c|c|t|c|a|c|c|g|t|c|t|a|t|g|g|t|ei
c|t|a|g|a|g|a|c|c|g|a|g|t|g|t|c|c|t|c|a|g|t|a|a|c|a|g|g|g|t|g|a|g|g|a|g|g|g|g|c|t|g|g|g|t|g|t|g|g|c|g|g|g|g|g|c|t|c|ei
t|a|a|t|g|c|c|a|c|c|t|t|t|g|c|a|c|t|a|c|c|t|c|c|c|t|a|g|g|a|g|a|a|g|a|c|t|c|t|t|c|c|a|c|c|t|c|t|t|t|t|t|g|c|c|t|g|a|ei
c|a|a|g|g|a|a|c|a|t|c|t|g|t|g|a|c|a|t|c|t|c|c|g|g|a|c|a|g|t|g|a|g|t|a|g|c|c|c|c|t|a|t|a|a|c|c|c|t|c|t|t|t|c|t|c|t|g|ei
c|a|a|g|t|c|t|c|a|c|a|t|g|g|c|t|t|a|a|t|t|t|t|c|t|c|a|g|g|t|a|t|t|g|a|t|g|a|a|g|a|t|g|a|a|g|t|g|g|c|a|g|c|a|g|a|g|g|ei
t|g|g|a|g|a|g|g|c|t|g|a|c|a|a|c|a|t|c|c|c|t|c|g|t|c|a|c|a|c|a|g|c|t|a|g|a|t|c|t|c|a|a|g|g|t|g|c|t|c|a|g|a|c|t|t|c|a|ei
a|c|a|g|a|a|g|a|a|g|c|g|a|g|c|c|a|c|g|c|c|c|c|a|c|g|c|a|c|g|c|c|c|t|g|c|g|a|g|g|g|g|a|a|c|a|a|g|g|g|a|a|c|c|t|t|t|c|ei
c|a|g|g|g|a|c|t|c|a|g|g|c|a|g|a|a|t|t|c|a|a|t|t|c|g|a|g|g|t|a|g|a|t|t|t|c|c|t|c|g|g|a|g|t|c|t|a|t|t|t|t|t|c|c|c|a|c|ei
c|a|c|g|g|t|g|t|c|t|c|a|t|t|t|t|t|c|c|t|c|c|c|t|c|t|a|g|t|g|c|a|a|c|c|a|g|a|g|g|t|g|a|c|a|g|t|g|t|a|c|c|c|a|g|a|g|a|ei
a|c|g|g|a|g|c|g|a|g|t|c|t|g|g|a|a|c|c|t|g|a|t|a|a|t|a|c|a|t|c|t|a|t|a|a|c|c|a|a|g|a|g|g|a|g|t|a|c|g|c|g|c|g|c|t|a|c|ei
g|a|g|c|t|c|t|g|t|g|a|c|g|a|t|g|a|c|c|c|g|c|c|g|g|a|t|c|c|c|a|c|a|c|g|c|c|a|c|a|t|t|c|a|a|a|g|c|c|a|t|g|g|c|c|t|a|c|ei
c|c|c|c|c|t|t|c|t|t|t|a|g|t|g|c|c|c|a|g|c|a|g|c|a|a|c|t|c|a|t|t|g|a|a|c|t|a|t|g|g|g|g|g|c|a|t|c|g|g|c|a|t|g|g|t|c|a|ei
a|g|a|g|t|g|a|a|a|c|c|t|c|c|t|t|c|c|a|c|c|t|g|c|g|a|a|c|c|c|t|c|a|g|c|c|c|a|t|a|t|g|a|g|c|g|a|c|g|c|g|g|c|t|g|a|g|t|ei
g|g|c|c|c|c|c|a|c|c|t|g|g|t|g|g|a|a|g|c|c|c|t|t|c|c|t|g|g|t|g|t|g|c|g|g|g|g|a|g|c|g|a|g|g|t|t|t|c|t|t|c|t|a|c|g|c|a|ei
g|c|a|g|t|g|g|t|t|g|a|t|g|a|a|t|a|c|c|a|a|g|a|g|a|c|a|g|g|t|a|a|g|a|g|t|c|t|a|a|g|c|c|t|g|g|c|t|c|a|a|a|a|c|t|t|g|c|ei
t|a|a|a|t|c|t|t|c|t|a|g|c|t|c|t|a|t|t|t|t|a|t|t|a|c|a|g|a|t|t|c|a|t|t|t|a|t|g|a|g|a|t|a|g|c|a|a|g|a|a|g|g|c|a|t|c|c|ei
g|t|a|g|a|c|c|t|t|g|g|t|g|g|g|c|g|g|t|c|c|t|t|t|c|t|a|g|g|a|a|g|a|a|g|c|c|t|a|t|a|t|c|c|c|a|a|a|g|g|a|a|c|a|g|a|a|g|ie
a|c|g|g|c|g|c|a|c|c|c|c|a|g|a|c|t|a|c|t|t|c|c|a|a|a|a|t|t|t|c|t|c|c|t|g|g|g|a|a|a|c|c|t|g|c|c|t|t|t|g|t|a|t|g|t|g|g|ei
g|g|c|t|c|a|a|c|a|c|c|a|t|t|c|c|c|c|t|g|t|t|t|t|c|a|g|c|t|c|c|t|g|t|a|c|t|c|g|t|c|g|g|t|g|g|a|g|a|a|c|a|t|c|c|a|g|c|ei
g|c|c|c|g|g|a|c|c|c|c|a|g|a|g|g|c|c|g|g|t|c|c|g|a|t|t|t|g|t|t|c|c|t|g|g|a|t|g|g|a|a|g|g|a|g|a|a|t|a|a|g|a|a|c|g|g|g|ei
g|t|c|t|t|a|a|t|c|c|a|t|c|c|a|c|c|a|g|a|g|t|c|a|a|a|g|g|c|c|a|g|a|c|g|g|g|c|c|c|c|g|c|a|t|c|t|g|t|g|a|t|g|a|g|a|a|t|ei
c|c|t|t|g|a|c|t|c|c|c|c|g|g|g|c|t|g|t|g|t|g|c|t|t|c|a|g|a|c|g|g|g|c|t|g|t|g|c|t|g|a|a|c|a|c|t|g|c|a|g|c|t|t|g|a|a|t|ie
g|g|g|a|t|g|c|a|g|t|a|c|a|g|c|c|a|c|a|g|c|a|t|a|c|a|c|g|g|t|a|a|g|c|c|a|c|c|c|c|a|g|t|c|t|c|c|c|t|t|c|c|t|g|c|a|a|a|ei
c|g|c|c|t|c|a|g|g|a|a|c|c|t|c|g|t|c|t|c|c|c|c|c|t|a|a|g|g|g|c|t|g|c|c|t|t|t|c|a|a|t|g|a|c|g|t|t|t|a|t|t|g|c|g|c|c|a|ei
t|c|t|t|c|c|a|t|g|a|g|a|c|a|c|t|c|t|a|c|c|a|g|a|g|c|g|g|a|t|g|a|t|g|g|g|c|g|t|c|c|c|t|t|c|c|c|c|c|a|a|g|t|t|a|t|c|a|ei
c|a|c|c|c|g|a|g|g|a|g|c|t|g|g|a|g|g|g|g|t|c|g|c|a|a|g|c|t|g|a|c|t|g|t|a|a|a|t|t|t|c|a|c|a|g|t|c|t|c|t|c|t|g|a|a|g|a|ei
a|t|c|a|a|c|a|a|t|g|t|c|g|c|c|a|a|a|g|c|c|c|a|g|t|g|g|t|t|a|c|t|c|t|g|t|g|t|t|t|g|c|t|g|g|t|g|t|t|g|g|t|g|a|g|a|g|g|ei
g|g|t|g|t|g|g|t|g|g|c|a|c|g|c|g|t|c|t|a|t|a|a|c|c|a|g|c|t|a|c|t|c|a|g|g|a|g|g|c|t|g|a|g|g|c|a|g|g|a|g|a|a|t|c|a|c|t|ei
t|c|a|g|a|c|c|t|t|g|g|t|g|g|g|c|g|g|t|c|c|t|t|t|c|t|a|g|g|a|a|g|a|a|g|c|c|t|a|t|a|t|c|c|c|a|a|a|g|g|a|a|c|a|g|a|a|g|ei
t|g|g|c|a|c|c|a|a|c|c|c|g|g|c|c|c|t|c|c|t|t|g|c|a|c|a|g|g|g|c|a|c|c|a|g|c|c|c|c|a|g|a|a|g|g|t|g|g|c|c|c|g|g|c|g|c|g|ei
t|c|c|c|c|c|a|g|c|a|a|g|a|c|c|c|g|g|g|g|g|c|a|a|c|c|a|g|g|t|g|c|g|g|g|g|g|c|c|a|g|c|c|c|t|g|c|g|c|g|t|g|g|c|t|g|g|g|ei
a|g|a|g|g|c|a|g|a|g|c|t|g|c|c|c|c|t|g|a|g|t|g|g|c|a|t|g|c|a|g|a|g|g|a|t|c|t|c|c|t|c|c|c|t|c|a|t|c|c|a|t|c|t|c|t|c|t|ei
a|t|t|t|t|g|t|c|a|t|g|c|t|g|g|g|a|g|g|a|a|t|g|t|t|c|g|g|g|t|c|a|t|a|c|g|g|a|g|t|g|t|g|c|t|g|g|a|g|a|a|g|t|g|a|t|t|g|ei
t|c|c|a|g|c|a|t|g|g|g|c|t|c|g|c|c|t|g|t|c|a|a|g|g|c|a|g|g|t|a|a|g|g|c|t|g|g|c|t|t|c|c|c|g|t|c|g|c|c|g|c|g|g|g|g|c|c|ei
c|c|t|a|a|a|t|g|t|t|a|t|g|a|g|g|a|t|c|a|t|c|a|c|a|g|c|c|g|t|a|a|g|t|a|t|g|a|a|a|t|t|c|a|g|g|g|a|t|a|c|g|g|c|a|t|a|t|ei
g|g|a|t|g|t|g|g|a|g|a|g|c|a|g|t|g|t|c|c|c|a|a|g|t|g|c|a|c|a|g|g|c|a|g|a|g|t|g|g|c|c|a|t|g|g|c|c|a|t|g|g|c|c|a|c|a|a|ei
a|a|a|t|g|g|a|g|a|t|g|c|c|a|a|a|a|c|a|g|a|c|c|g|c|a|c|a|g|a|a|a|g|c|t|g|a|a|g|g|t|g|c|t|g|g|a|g|a|t|g|c|c|a|a|g|t|g|ei
t|g|t|c|t|a|a|t|a|g|c|g|g|a|g|t|a|a|c|a|t|g|t|c|c|a|c|t|g|c|g|g|a|g|t|g|c|c|a|g|g|c|c|a|g|c|a|t|c|t|g|a|a|t|g|t|c|a|ei
c|a|g|c|c|g|g|g|t|t|g|g|c|c|t|a|a|g|g|g|a|c|t|a|t|g|c|c|g|g|g|c|g|g|a|a|a|g|g|g|g|a|c|t|t|t|g|g|g|t|t|g|g|g|g|a|t|t|ei
t|t|g|c|t|t|t|a|t|g|g|a|g|a|a|a|g|c|t|g|a|a|c|c|c|c|t|c|c|t|g|g|t|g|c|c|c|a|c|c|c|c|t|c|c|c|c|a|g|g|c|g|a|a|g|a|a|c|ei
t|g|g|g|t|t|g|a|t|a|t|t|g|c|t|c|t|t|g|a|a|t|g|g|g|c|g|a|t|a|t|t|t|a|g|c|t|c|c|g|a|a|g|g|g|a|t|t|t|g|g|a|g|g|g|g|t|t|ei
g|g|g|a|g|t|c|c|t|a|g|c|c|t|g|a|g|a|g|g|c|t|g|g|g|t|c|c|a|t|t|t|t|g|a|g|g|t|t|a|g|a|g|a|g|g|g|g|c|a|g|t|a|g|a|g|c|a|ei
g|c|c|c|a|g|c|t|c|a|g|c|t|c|a|g|t|t|c|a|g|t|t|a|c|c|c|t|g|t|t|c|a|g|c|a|c|a|g|c|a|c|a|t|c|a|g|a|g|c|c|c|t|g|c|g|a|t|ei
a|c|g|a|g|a|a|g|a|c|a|t|a|c|c|t|g|c|c|c|g|c|t|t|g|a|t|g|a|g|a|a|a|c|t|c|a|g|g|t|a|g|c|a|c|c|t|g|c|c|c|c|t|g|g|a|g|a|ei
g|c|t|g|c|g|c|c|t|t|g|g|g|c|c|t|c|t|g|c|t|g|c|g|c|c|g|g|g|t|g|a|g|c|g|g|g|g|c|a|a|g|g|c|g|c|t|c|c|g|g|g|g|c|c|a|g|g|ei
c|a|c|t|a|c|a|a|g|c|a|g|c|a|c|t|g|c|c|c|t|c|c|a|c|c|c|g|g|t|g|a|g|t|g|c|c|t|a|c|g|g|c|a|g|g|g|c|c|t|c|c|a|g|c|a|g|g|ei
g|a|t|t|t|a|c|a|g|a|t|g|a|t|t|t|t|g|a|a|t|g|g|a|t|a|a|t|g|t|a|a|g|t|a|t|a|t|t|t|c|c|t|t|t|c|t|t|a|c|t|a|a|a|a|t|t|a|ei
a|g|c|t|c|c|g|c|c|g|a|a|g|g|c|g|c|c|g|c|c|a|a|g|a|g|a|g|g|t|g|a|g|t|g|c|g|g|g|c|c|t|t|c|t|g|c|g|g|g|g|g|g|t|g|g|t|g|ei
a|a|c|a|a|a|t|a|c|a|a|t|t|c|t|g|c|t|c|t|c|t|t|t|t|a|t|t|t|g|a|t|t|t|t|t|g|t|a|t|g|a|a|a|a|a|a|a|c|t|a|a|a|a|a|t|g|g|ei
t|g|g|a|a|t|t|t|a|a|g|t|a|t|g|a|t|t|t|c|a|a|t|c|t|c|a|a|t|g|c|t|g|t|a|c|t|c|t|a|c|c|g|c|t|a|a|a|g|g|a|g|c|a|g|t|t|g|ei
c|c|a|t|g|g|g|a|g|a|g|t|g|g|c|c|a|t|c|g|t|g|g|g|g|c|g|c|c|c|c|g|c|g|g|a|c|c|c|t|g|g|g|c|c|c|c|a|g|c|c|a|g|g|a|g|g|a|ei
c|a|a|g|t|t|g|a|c|t|a|g|a|t|g|c|c|c|t|t|t|a|t|t|t|c|a|g|a|a|a|t|a|t|t|c|t|a|c|a|t|c|a|t|t|g|g|a|g|c|t|g|t|g|g|t|a|t|ei
t|g|c|a|g|g|a|a|t|g|g|c|t|g|g|c|g|a|a|g|c|a|c|a|g|g|t|g|c|c|c|g|g|t|a|c|g|t|g|t|g|g|a|a|c|c|g|c|a|c|t|g|a|g|c|t|c|a|ei
c|a|a|t|t|t|g|c|c|c|c|a|g|a|a|t|c|t|t|a|c|c|g|c|a|c|a|t|c|t|g|g|t|a|c|a|a|a|g|g|g|c|a|a|a|t|g|a|g|g|g|a|c|c|t|c|t|a|ei
t|t|a|t|t|t|t|a|t|a|t|a|t|t|t|a|t|t|t|t|a|t|t|t|t|t|a|g|a|g|a|g|t|c|t|c|a|c|t|c|t|g|t|c|g|c|c|c|a|a|g|c|t|g|g|a|g|t|ei
a|a|g|t|t|g|c|a|c|g|t|g|g|a|t|c|c|t|c|a|g|a|a|t|c|a|c|t|g|t|g|a|g|t|c|t|a|t|g|g|g|a|c|c|t|t|c|a|a|t|g|t|t|t|c|t|c|t|ei
t|c|a|t|g|c|a|t|t|g|a|a|c|c|a|a|a|a|c|t|c|a|g|c|g|t|a|a|g|g|a|a|a|g|g|c|t|t|t|g|a|a|g|g|g|g|c|a|g|t|g|g|t|a|a|c|t|t|ei
g|g|g|c|g|c|t|g|t|c|c|t|g|t|t|t|t|c|t|c|c|t|g|g|g|c|a|g|a|c|c|g|t|t|g|g|g|g|g|g|g|t|g|a|a|t|t|a|c|t|t|c|t|t|c|g|a|c|ei
g|c|t|a|c|c|a|c|c|a|t|g|c|t|g|g|c|c|t|c|a|g|g|a|g|c|t|t|c|t|g|g|t|g|g|c|c|t|t|g|c|t|g|g|t|c|t|g|c|c|t|g|a|c|t|g|t|a|ei
c|t|c|a|t|t|g|a|a|a|c|a|g|c|t|a|t|a|t|t|t|c|t|t|t|c|a|g|a|t|t|a|g|t|g|a|t|g|a|t|g|a|a|c|c|a|g|g|t|t|a|t|g|a|c|c|t|t|ei
a|t|c|a|a|a|g|a|c|c|t|a|t|a|a|a|t|g|t|a|t|t|t|c|c|c|t|c|t|t|t|c|a|a|a|t|a|t|g|a|c|a|c|a|a|a|a|a|t|t|a|c|t|g|c|t|t|a|ei
g|a|a|a|a|g|g|a|g|g|g|a|g|c|t|a|c|t|c|t|c|a|g|c|g|c|a|a|g|t|a|a|g|t|a|t|g|a|a|g|g|a|g|g|c|t|g|a|t|c|c|c|t|g|a|a|a|t|ei
a|c|t|g|g|c|c|g|t|g|t|g|g|t|t|t|t|a|g|g|t|g|g|c|a|g|g|a|a|g|c|t|a|t|t|t|c|t|g|g|c|a|a|g|g|c|c|a|g|a|t|c|c|t|g|t|c|t|ei
a|a|g|c|a|g|a|g|c|a|g|g|a|t|t|a|a|c|c|c|a|g|g|a|t|c|t|t|g|c|t|c|t|g|c|a|g|a|a|c|t|t|g|c|t|c|t|t|a|a|t|c|a|a|g|g|t|a|ei
t|t|t|c|a|g|a|c|a|t|g|c|a|g|t|c|a|g|a|a|a|a|t|g|t|t|t|a|c|t|a|c|a|t|c|c|t|t|a|t|t|a|a|t|g|a|t|a|c|c|a|t|t|a|t|t|g|g|ei
t|g|t|t|a|c|t|a|g|a|g|a|a|g|t|t|t|c|t|c|t|g|a|c|t|g|t|a|g|a|g|c|a|c|c|g|a|g|a|a|c|c|t|a|c|a|a|a|a|t|a|c|c|a|t|g|a|a|ei
t|t|t|a|a|a|a|t|a|t|t|t|a|t|c|t|g|a|t|t|a|a|g|t|t|c|t|a|a|a|c|a|a|t|g|c|t|g|a|t|t|t|g|g|t|g|a|c|c|a|a|c|t|g|t|c|a|c|ei
t|a|t|g|a|g|g|c|c|a|c|c|c|t|g|a|g|g|t|g|c|t|g|g|c|c|t|g|g|g|c|t|t|c|t|a|c|c|c|t|g|c|g|g|a|g|a|t|c|a|t|a|c|t|g|a|c|c|ei
c|c|g|g|a|t|c|a|t|t|c|a|t|g|a|c|c|t|t|t|c|t|c|t|c|c|a|g|g|t|t|c|c|t|g|g|a|t|g|c|c|t|a|t|g|c|t|g|a|g|c|a|c|a|a|g|t|t|ei
g|g|c|t|t|t|a|c|t|g|a|a|g|a|g|g|a|g|t|t|t|a|a|a|g|c|t|g|g|t|g|a|g|t|g|g|g|t|g|t|g|a|g|c|c|a|t|a|c|t|g|g|c|c|t|t|g|a|ei
a|g|g|a|a|a|t|c|t|c|c|t|t|t|g|c|t|c|a|g|a|t|a|g|a|c|a|c|t|g|a|c|c|a|c|t|a|a|a|t|g|g|a|t|t|a|a|a|a|a|a|c|a|c|t|g|a|a|ei
a|g|a|g|c|t|a|a|a|t|a|t|c|g|a|t|g|t|t|g|t|t|g|t|t|c|a|g|g|t|g|a|g|a|t|t|t|t|g|g|t|g|g|g|a|t|a|g|c|t|a|g|a|g|g|t|c|a|ei
t|a|c|c|t|a|c|a|g|c|a|a|c|a|a|c|a|a|c|t|a|g|c|a|a|a|g|t|a|a|c|a|a|c|t|g|g|c|t|a|c|g|a|t|c|c|t|a|a|c|a|a|c|t|a|a|t|g|ei
t|t|g|g|g|g|c|a|t|t|a|c|a|c|g|t|t|t|c|a|t|a|a|a|a|a|t|g|g|t|g|c|a|a|t|a|c|t|c|c|g|a|a|a|t|t|t|t|t|t|a|a|c|g|a|a|a|a|ei
a|a|g|c|t|g|c|a|t|g|t|g|g|a|t|c|c|t|g|a|g|a|a|t|c|a|g|g|g|t|a|a|g|t|c|t|a|g|g|a|g|a|t|g|t|t|c|t|t|c|t|t|t|g|t|c|c|t|ei
c|c|c|a|c|c|c|t|c|a|c|t|c|t|t|t|g|c|t|t|g|t|c|t|g|c|a|g|g|a|t|g|t|t|c|c|t|g|t|c|c|t|t|c|c|c|c|a|c|c|a|c|c|a|a|g|a|c|ei
g|t|c|c|t|t|c|t|t|g|g|t|g|g|g|g|g|g|t|c|c|t|t|t|c|t|a|g|g|a|a|g|a|a|a|c|c|t|a|t|a|t|c|c|c|a|a|a|g|g|a|c|c|a|g|a|a|g|ie
c|a|g|c|t|g|g|c|c|a|t|t|g|a|c|a|c|c|t|a|c|c|a|g|g|t|t|t|g|t|a|a|g|t|t|c|t|t|g|g|g|g|a|a|t|g|g|g|t|g|c|g|g|g|t|c|a|g|ei
t|a|t|g|c|a|t|c|a|g|a|t|t|g|c|a|a|t|a|a|a|t|g|c|a|t|a|t|t|g|g|a|a|a|c|t|t|a|a|a|t|g|a|a|c|t|g|g|g|c|a|a|g|a|t|g|a|t|ei
a|g|g|g|t|t|c|c|c|c|t|g|a|g|c|g|c|c|g|g|a|g|c|c|c|a|g|g|t|c|t|c|g|c|c|t|t|g|t|c|c|c|g|a|a|a|g|c|c|c|c|g|c|a|a|t|c|g|ei
g|g|g|c|c|g|g|g|g|g|a|c|g|g|c|g|g|c|t|c|c|c|c|c|c|g|g|c|t|c|c|a|g|c|g|g|c|t|c|g|g|g|g|a|t|c|c|c|g|g|c|c|g|g|g|c|c|c|ei
a|a|g|a|t|c|a|c|t|g|t|a|g|t|g|g|g|t|g|t|t|g|g|c|a|g|t|t|g|g|t|a|t|g|g|c|g|t|g|t|g|c|t|a|t|c|a|g|c|a|t|t|c|t|g|g|g|a|ei
a|a|g|c|t|t|t|a|c|t|t|t|c|t|t|c|t|t|t|a|c|c|t|c|t|a|c|c|c|c|t|a|t|t|c|t|c|t|t|g|g|t|c|t|g|t|g|t|a|a|g|g|t|g|t|t|g|a|ei
t|a|a|c|t|t|t|t|c|a|c|a|t|t|t|g|t|t|c|c|a|t|g|t|c|c|a|g|t|c|a|t|c|a|g|g|t|g|g|a|a|a|a|g|c|g|g|a|a|a|t|g|c|a|a|c|a|c|ei
g|t|c|a|a|c|a|a|g|t|a|c|c|g|t|a|a|g|g|g|a|a|a|t|g|a|a|a|a|g|a|a|c|t|t|t|g|a|a|g|a|g|a|g|a|g|t|t|c|a|a|g|a|g|g|g|c|g|ei
a|a|g|c|t|t|c|g|g|g|t|g|g|a|c|c|c|g|g|t|c|a|a|t|c|a|a|g|g|t|g|a|g|c|g|g|c|g|a|g|c|c|g|g|g|a|g|c|g|a|t|c|t|g|g|g|g|t|ei
a|g|t|a|a|t|t|a|a|t|a|g|a|t|g|g|t|a|a|t|t|a|a|t|a|t|c|c|t|t|g|a|t|g|t|g|a|t|g|t|t|c|t|t|t|t|g|c|a|t|a|t|t|t|c|c|t|t|ei
c|a|g|g|t|g|t|t|g|a|c|a|a|g|a|a|c|c|c|t|g|g|a|g|a|g|g|a|g|a|g|c|a|g|g|g|a|a|a|g|g|t|c|a|g|a|a|a|g|g|g|a|a|g|a|c|c|c|ei
a|c|t|a|a|a|t|a|t|c|t|c|a|a|c|t|t|c|a|c|g|g|c|t|a|g|a|g|a|a|t|a|c|c|a|g|t|c|g|g|g|t|c|a|t|g|c|a|g|c|a|t|c|a|a|t|a|t|ei
g|a|t|c|a|a|a|a|a|a|c|c|a|a|t|a|a|a|g|a|t|g|t|t|t|c|t|a|c|a|a|c|g|g|c|t|g|g|t|g|g|a|g|t|g|g|t|a|g|a|g|t|g|g|a|a|a|g|ei
c|c|t|a|a|g|t|a|g|c|t|g|g|g|g|c|t|a|c|a|g|g|c|c|c|a|c|c|a|c|c|a|t|g|c|c|t|g|a|c|t|a|a|t|t|t|t|t|t|c|a|c|t|t|t|t|t|t|ei
g|g|c|t|g|a|c|t|t|t|a|t|g|g|c|t|a|a|g|a|a|g|t|t|c|a|c|t|g|g|a|t|g|c|a|t|t|a|a|t|a|a|c|a|a|a|t|a|t|t|t|t|a|c|c|t|t|t|ei
t|g|t|t|c|c|t|g|c|c|t|t|a|a|c|t|g|a|t|g|a|c|a|t|t|c|t|t|g|t|g|a|a|a|g|t|c|c|t|t|c|t|c|c|t|g|g|c|t|c|a|t|c|c|t|g|g|c|ei
t|g|a|a|a|t|a|t|t|a|t|a|t|a|t|a|a|t|a|t|a|g|a|t|a|a|g|a|g|g|c|c|t|g|t|c|c|a|a|a|a|g|t|c|c|t|c|c|c|a|a|a|g|t|a|t|t|a|ei
c|c|g|g|a|g|t|a|t|t|g|g|g|a|c|c|g|g|a|a|c|a|c|c|g|a|t|c|t|g|c|a|a|g|g|c|c|c|a|a|g|c|a|c|g|g|a|c|t|g|a|a|c|g|a|g|a|g|ei
g|a|c|c|t|c|t|c|a|t|t|c|a|c|c|c|c|t|t|c|c|c|t|c|a|g|a|g|c|t|g|g|t|a|c|c|a|g|a|c|a|g|c|c|c|c|a|g|t|t|c|a|t|t|a|g|c|c|ei
c|c|c|g|g|c|c|a|g|g|c|g|c|g|g|a|g|a|t|g|g|g|g|t|c|a|c|g|g|t|g|a|g|t|a|c|t|c|g|c|g|g|g|c|t|g|g|g|c|g|c|t|c|c|c|g|c|c|ei
g|a|a|a|a|g|g|a|g|g|g|a|g|c|t|g|c|t|c|t|c|a|g|c|g|c|g|t|g|t|a|a|g|t|g|a|t|g|g|c|g|g|t|g|g|g|c|g|t|g|t|g|g|a|g|g|a|g|ei
t|a|c|t|c|c|c|a|c|t|c|c|c|c|a|t|t|c|t|t|c|a|a|c|c|a|g|c|t|c|a|a|g|t|t|c|c|a|g|t|t|c|c|t|c|c|a|c|c|t|a|g|g|a|c|t|t|c|ei
g|a|g|g|g|c|c|a|g|t|t|g|g|g|g|c|c|t|g|c|c|g|a|c|g|g|c|c|a|a|g|a|a|a|g|t|a|g|a|g|g|a|c|a|t|g|a|t|g|a|a|g|a|a|g|c|t|g|ei
g|a|c|g|a|t|a|a|g|g|a|g|a|c|c|t|g|c|t|t|t|g|c|g|g|g|a|g|g|t|a|c|t|a|c|a|g|t|t|c|t|c|t|t|c|a|t|t|t|t|a|a|t|a|t|g|t|c|ei
c|t|a|c|c|a|t|a|t|c|t|t|g|a|t|c|a|t|c|c|t|t|t|c|g|t|a|g|g|a|a|t|c|g|g|a|t|a|t|a|a|c|a|t|c|a|t|c|c|g|g|g|t|a|c|c|c|a|ei
a|t|a|c|c|t|a|t|t|g|t|c|a|t|t|t|t|t|c|t|t|t|t|t|a|c|a|g|a|a|a|a|a|g|t|g|t|g|g|a|g|a|a|g|a|a|a|g|a|c|g|g|a|g|a|g|t|a|ie
c|t|a|c|a|a|g|c|a|c|t|g|a|a|g|c|t|g|t|g|c|c|g|c|g|c|t|c|t|c|a|g|t|c|c|c|a|c|a|g|c|t|c|t|c|a|g|g|c|c|c|c|t|c|t|c|t|g|ei
t|c|g|a|g|c|t|t|c|t|c|t|t|c|t|g|g|g|g|c|a|g|a|c|t|c|t|g|g|t|a|t|g|g|a|g|a|g|a|g|g|g|c|a|a|g|t|c|t|t|g|c|t|t|c|t|c|c|ei
a|a|g|g|c|g|a|c|a|c|t|a|a|g|g|a|t|t|g|g|c|c|a|g|t|g|g|a|a|t|a|t|c|t|a|c|c|a|g|t|g|c|a|a|c|g|a|c|c|a|a|c|t|t|g|a|a|g|ei
c|a|c|t|c|a|c|g|a|g|t|g|t|c|t|t|g|c|t|c|t|c|c|t|a|c|a|g|t|a|t|g|t|g|g|g|a|a|g|c|c|c|a|a|g|a|a|t|c|c|g|g|c|a|a|a|c|c|ei
a|g|t|a|a|c|g|c|c|t|c|c|c|c|c|c|a|g|g|c|t|g|g|g|a|a|a|a|g|a|a|t|g|a|g|g|a|a|g|c|t|g|c|t|g|a|t|g|a|g|g|t|c|t|t|c|a|a|ei
g|a|g|a|g|a|a|a|g|g|t|g|c|t|c|c|t|g|g|a|g|a|a|a|g|g|t|c|c|c|c|a|a|g|g|g|c|c|t|g|c|a|g|g|g|a|g|a|g|a|t|g|g|a|g|t|t|c|ei
t|g|g|g|t|a|c|c|a|c|t|g|g|c|t|g|a|g|t|a|g|g|a|a|g|g|g|a|a|g|a|c|c|a|g|g|t|g|g|c|t|c|c|a|t|g|c|c|t|t|t|c|c|c|c|a|g|g|ei
a|a|a|a|a|t|a|a|t|a|a|t|a|a|a|t|a|a|a|t|a|a|a|t|t|a|a|a|a|a|c|c|c|t|g|a|a|t|g|c|c|a|c|g|g|a|a|g|c|c|g|c|c|a|t|g|g|c|ei
t|a|g|a|g|c|a|a|g|g|g|t|t|c|a|c|t|g|t|t|c|c|t|a|a|t|c|a|a|g|a|c|c|a|t|c|c|t|t|g|g|g|a|c|c|a|t|g|c|c|t|g|c|c|t|t|t|g|ei
a|c|t|a|t|t|a|c|g|t|a|t|a|a|t|c|c|t|t|t|t|c|t|t|c|a|a|g|g|t|a|a|g|g|c|t|g|a|g|a|t|c|t|c|c|g|c|t|a|g|g|c|t|t|c|t|t|t|ei
g|a|t|t|a|a|t|c|t|c|c|t|t|g|c|t|t|g|c|c|t|g|g|c|a|c|a|g|c|g|a|t|g|c|c|a|g|a|g|a|g|a|a|c|g|t|c|c|a|g|a|g|a|c|t|c|a|c|ei
a|c|c|c|c|c|g|g|t|c|c|a|a|g|c|c|t|c|c|c|c|t|c|a|c|a|c|t|g|c|g|c|c|c|t|t|c|t|c|c|c|t|g|a|g|g|a|c|c|t|c|a|g|c|t|t|t|c|ei
c|t|g|c|t|a|c|t|t|c|t|a|g|t|t|t|c|a|g|c|t|g|g|a|g|c|g|g|a|c|t|g|a|a|g|a|t|c|t|c|c|c|a|a|a|g|g|c|t|g|t|g|g|t|g|t|t|c|ei
a|t|g|g|c|c|c|t|c|a|c|g|g|c|c|t|t|t|g|t|t|c|t|a|c|t|c|g|c|t|g|c|a|g|g|a|g|g|c|t|a|a|a|g|a|t|a|t|t|t|g|c|g|a|g|g|a|g|ei
t|g|t|g|a|g|t|g|g|c|a|t|g|a|a|g|a|a|g|g|t|g|t|t|g|c|c|c|c|a|c|c|t|a|t|g|g|c|c|t|a|t|t|t|a|c|t|g|a|c|c|c|t|c|t|a|c|a|ei
g|a|t|c|g|t|a|t|c|t|t|c|c|t|t|c|t|c|a|c|c|a|t|c|t|t|t|g|t|t|g|a|c|a|g|t|a|t|t|t|t|t|g|a|g|g|c|a|g|t|g|g|c|t|c|c|a|a|ei
t|c|c|a|g|a|c|c|t|a|c|t|c|t|g|c|c|c|t|c|a|a|c|t|c|g|a|g|g|t|g|a|g|t|g|t|c|t|g|c|t|g|g|a|g|g|c|g|g|a|g|g|c|t|g|g|a|g|ei
g|a|a|a|a|g|g|a|g|g|g|a|g|c|t|a|c|t|c|t|c|a|g|c|g|c|g|t|g|t|a|a|g|t|g|a|t|g|g|g|g|g|t|g|g|g|a|g|t|g|t|g|g|a|g|g|a|g|ei
a|t|t|c|g|c|a|a|g|t|g|g|a|c|t|g|g|a|g|a|g|a|a|a|g|t|c|t|t|a|c|t|t|a|a|a|g|t|a|a|a|t|a|a|a|t|a|c|a|a|c|t|t|t|t|c|c|c|ei
t|t|c|c|a|c|c|t|a|c|t|c|a|g|c|a|c|t|c|c|c|t|g|c|c|c|a|g|g|t|g|a|a|g|c|c|a|c|t|t|t|c|c|t|c|t|t|t|c|a|t|c|a|g|t|c|a|t|ei
c|c|c|a|a|a|g|g|t|a|a|a|c|a|c|c|t|g|g|g|t|c|t|t|c|c|a|g|c|t|t|g|t|g|a|g|a|c|a|g|c|g|a|g|g|a|c|g|c|c|t|c|g|a|g|a|t|a|ei
t|c|c|a|t|c|c|g|c|t|c|c|t|g|c|t|g|c|c|t|c|a|t|c|c|c|c|g|g|t|g|a|g|t|g|t|g|g|c|t|c|t|g|t|c|t|t|t|g|c|c|t|t|c|c|a|t|c|ei
a|a|g|c|t|g|c|a|t|g|t|g|g|a|t|c|c|t|g|a|g|a|a|t|c|a|g|g|g|t|g|a|g|t|c|c|a|g|g|a|g|t|t|t|c|a|g|c|a|g|t|t|t|c|a|g|a|g|ei
a|c|c|t|c|a|a|a|t|t|g|a|a|c|g|a|t|t|a|a|a|a|a|t|a|a|a|g|c|a|t|a|g|c|c|c|t|g|a|a|a|g|a|g|a|a|a|g|g|a|c|a|a|g|g|a|c|c|ei
t|c|a|a|g|a|a|c|g|g|t|t|c|c|c|t|c|t|t|t|g|c|c|t|c|g|a|g|g|t|g|a|a|t|c|c|a|g|g|g|c|a|g|g|t|a|c|t|g|g|g|g|a|t|g|c|g|g|ei
g|c|t|t|t|c|a|t|g|a|a|t|t|c|t|g|t|c|a|t|t|t|c|a|g|a|c|t|c|t|c|a|c|c|c|c|t|g|c|t|a|t|a|a|c|t|a|t|g|a|c|c|a|t|g|c|t|g|ei
c|a|g|g|g|c|g|t|g|g|t|g|c|c|c|c|g|g|g|g|c|g|t|a|c|c|t|g|c|a|a|g|a|g|t|t|t|c|t|t|a|a|t|g|t|c|a|c|g|a|g|c|g|t|t|c|a|c|ei
c|t|g|g|g|a|a|g|t|g|a|g|c|t|c|g|c|a|g|t|g|t|g|t|a|c|a|c|c|a|g|a|a|a|a|g|t|g|c|c|t|c|t|g|g|a|c|t|c|a|t|c|c|c|c|t|g|c|ei
c|t|t|t|g|c|t|g|a|g|a|t|g|a|a|c|a|g|g|g|g|c|t|g|a|c|g|a|g|t|g|g|a|a|g|a|c|g|g|t|t|g|t|g|g|g|c|g|g|t|g|c|c|a|t|g|t|t|ei
c|a|a|g|t|c|t|t|t|t|g|a|g|g|a|c|a|t|c|c|a|c|c|g|a|c|a|g|g|t|g|a|a|c|c|c|c|g|t|g|a|g|g|c|t|g|g|c|c|c|g|g|g|a|g|c|c|c|ei
a|a|g|g|g|c|g|t|c|t|c|t|t|c|c|t|g|g|g|g|g|c|t|t|c|c|a|g|g|t|a|a|g|a|g|a|g|a|a|t|g|a|t|g|t|t|c|a|a|g|t|t|c|a|t|g|a|g|ei
t|c|a|a|c|c|a|g|a|g|g|t|t|c|c|t|g|t|g|g|t|t|c|t|c|a|g|a|a|a|a|c|a|g|t|c|c|a|g|g|a|g|c|a|c|t|a|t|c|a|g|g|a|c|t|t|t|g|ei
g|g|a|c|a|c|t|t|c|c|c|c|g|c|c|g|c|t|g|c|c|a|g|a|c|c|g|c|t|t|c|t|c|t|g|a|a|a|g|g|c|t|c|t|c|c|t|t|g|c|a|g|c|t|g|c|c|t|ei
g|c|a|a|t|g|g|c|a|t|a|g|a|a|a|g|t|g|t|g|a|a|c|a|g|a|a|a|a|t|g|a|t|a|t|t|a|a|g|g|a|g|g|g|g|g|g|c|t|g|t|a|g|a|a|g|g|g|ei
t|a|a|g|a|a|g|c|t|g|t|c|c|a|g|c|t|g|g|g|t|g|c|g|t|g|a|t|g|a|a|a|t|a|c|c|t|g|g|g|c|a|a|t|g|c|c|a|c|c|g|c|c|a|t|c|t|t|ei
g|g|t|c|c|a|g|g|a|t|c|a|g|t|t|g|c|t|c|t|t|c|c|t|g|c|a|g|g|t|a|c|t|g|a|c|a|g|a|c|c|c|a|g|a|a|g|c|a|g|c|t|a|a|a|t|a|t|ei
c|g|g|c|a|t|c|g|a|c|t|t|g|g|g|g|a|c|c|a|c|c|t|c|c|c|t|g|g|t|a|a|g|t|g|g|g|g|t|t|g|c|g|g|a|t|g|a|g|g|g|g|g|a|c|g|g|g|ei
c|t|g|t|c|t|c|a|c|c|t|g|t|g|c|c|t|t|c|t|c|c|c|a|t|g|a|a|c|a|c|a|c|g|c|a|c|g|g|g|a|t|g|g|g|c|c|t|g|g|g|g|g|g|a|c|c|c|ei
t|t|a|t|t|t|t|c|t|c|c|a|t|t|g|t|c|t|t|a|c|c|t|t|a|c|a|g|g|t|g|t|t|a|a|t|a|t|a|g|t|g|a|a|a|a|g|g|a|a|g|c|t|t|g|c|a|g|ei
a|t|t|c|t|a|c|t|t|a|g|t|a|a|a|c|a|t|a|a|t|t|t|t|g|t|g|c|t|a|g|a|t|a|a|c|c|a|a|a|t|t|a|a|g|a|a|a|a|c|c|a|a|a|a|c|a|a|ei
t|g|c|c|a|t|t|t|t|a|c|a|a|a|t|a|a|g|a|c|t|t|a|a|t|t|g|t|c|c|t|t|t|t|g|t|t|t|t|t|c|a|g|c|c|t|a|c|c|a|t|g|a|g|a|a|t|a|ei
c|c|c|t|c|c|t|a|a|t|g|c|c|c|a|c|c|a|t|c|c|c|g|c|t|c|a|g|g|g|a|a|a|s|a|g|t|a|c|t|g|g|g|a|g|t|a|c|c|a|g|t|t|c|c|a|g|c|ei
c|a|g|c|t|t|t|c|c|t|a|a|c|c|c|t|t|t|c|c|c|t|c|c|c|c|a|g|c|a|t|c|c|g|g|a|g|g|g|g|t|t|t|c|c|a|g|g|t|a|t|a|t|a|a|g|c|a|ei
a|t|g|c|c|t|t|g|a|t|a|t|a|g|g|t|a|t|a|g|g|c|a|a|t|t|a|a|g|t|t|t|a|t|t|a|t|g|a|a|t|t|t|t|g|c|t|g|a|t|a|t|a|g|g|a|t|g|ei
t|g|t|t|t|g|a|t|t|t|t|c|t|a|g|g|t|a|a|t|c|a|a|t|c|a|a|a|g|c|a|g|c|t|g|t|g|c|t|a|t|g|g|g|a|g|g|t|a|a|a|g|a|a|a|c|c|c|ei
c|a|t|c|c|c|c|c|a|c|a|a|g|g|c|c|a|a|c|g|t|t|g|c|c|c|a|g|g|t|g|t|g|c|c|t|g|c|c|c|t|c|c|c|a|g|t|g|a|c|a|t|c|t|a|g|c|c|ei
t|t|t|g|a|a|a|g|a|t|t|c|t|g|c|c|g|a|g|g|c|c|t|a|a|g|a|g|g|t|t|a|g|a|g|a|a|g|a|c|t|a|t|g|t|a|g|g|g|g|a|g|c|t|a|g|g|t|ei
t|g|c|a|a|t|c|t|c|c|a|c|t|c|c|c|a|a|t|c|t|c|t|t|a|c|a|g|g|c|t|g|g|g|t|g|g|a|g|a|a|g|g|a|g|a|c|a|t|a|c|t|a|c|t|g|a|c|ei
g|g|c|c|g|c|c|c|t|g|t|a|c|c|c|t|c|t|t|t|c|a|c|t|t|c|c|c|t|a|a|a|g|a|c|c|c|t|a|a|a|t|c|t|g|a|g|g|a|a|t|c|a|a|c|a|g|g|ei
g|g|g|g|a|a|a|a|a|g|t|a|a|a|a|c|a|a|a|a|t|g|t|a|t|a|a|g|g|a|g|t|a|a|a|g|c|a|t|g|t|a|c|t|t|a|a|a|a|t|a|t|a|t|t|c|t|t|ei
g|a|a|g|a|t|g|a|a|a|t|t|a|a|c|c|g|c|c|g|c|a|c|g|t|g|c|t|g|a|g|a|a|t|g|a|g|t|t|t|g|t|g|g|t|c|c|t|g|a|a|g|a|a|g|g|a|t|ei
a|g|g|a|g|c|a|a|a|t|g|a|a|a|c|a|g|c|c|a|a|c|t|c|c|t|g|c|c|t|c|c|c|c|c|a|t|g|c|c|a|g|a|a|g|g|t|g|c|c|t|g|t|c|g|a|g|c|ei
t|t|g|c|a|g|c|a|a|a|g|a|t|c|t|t|g|g|a|a|a|t|g|t|g|a|a|g|a|c|c|a|c|a|a|g|g|c|t|g|a|a|a|a|g|t|g|c|t|t|t|g|c|t|g|g|a|g|ei
c|a|g|g|a|t|a|t|g|a|a|c|c|a|t|g|a|a|t|a|c|a|t|t|c|t|g|g|t|a|t|c|g|a|c|a|a|g|a|c|c|c|a|g|g|c|a|t|g|g|g|c|t|g|a|g|g|c|ei
g|t|g|t|c|t|g|a|a|a|a|c|a|a|t|a|a|t|t|c|t|t|t|a|a|t|a|g|g|t|g|g|t|t|g|a|a|a|a|g|a|a|a|a|c|t|a|a|a|c|c|a|t|a|c|a|t|t|ei
a|t|g|t|t|a|t|a|t|g|t|c|a|c|a|t|t|t|t|g|t|a|a|t|a|c|a|g|c|t|t|g|c|t|g|g|t|g|a|a|a|a|g|g|a|c|c|c|c|a|c|g|a|a|g|t|g|t|ei
g|g|g|a|c|t|c|t|g|a|c|c|a|t|c|t|g|t|t|c|c|c|a|a|t|c|a|g|c|a|a|g|t|t|c|a|t|t|c|c|t|g|a|g|g|g|c|t|c|c|c|a|g|a|g|a|g|t|ei
t|g|c|t|t|g|g|g|c|t|t|c|a|g|g|g|c|t|g|c|c|t|g|c|g|c|a|g|g|c|g|g|g|g|t|c|g|c|t|a|a|g|g|c|c|t|c|a|g|g|a|g|g|a|g|a|a|a|ei
g|a|c|t|c|c|a|a|t|g|a|a|t|t|t|t|c|t|g|t|a|a|t|g|t|g|a|c|c|c|a|a|g|a|g|g|a|a|a|c|a|c|t|c|t|a|g|g|a|c|g|g|g|g|a|a|c|g|ei
c|a|g|c|a|g|g|a|c|a|t|c|a|a|g|t|t|c|t|t|g|c|c|t|c|a|a|g|g|t|t|c|g|a|c|c|g|g|t|t|t|t|c|c|t|c|a|t|c|c|a|g|t|t|a|g|a|g|ei
g|a|g|c|t|c|c|c|a|g|a|g|c|a|g|c|a|a|g|a|g|g|g|c|g|c|t|g|a|a|g|c|a|c|c|t|g|g|a|g|a|a|g|c|a|g|g|a|g|g|c|a|c|a|g|c|t|g|ei
c|a|t|t|g|t|a|c|t|c|c|a|g|c|c|t|g|g|g|c|a|a|c|g|a|g|t|g|a|a|a|c|t|c|t|g|t|c|t|c|a|a|a|a|a|a|a|a|c|a|a|a|a|a|a|c|a|a|ei
c|g|t|c|c|t|c|a|a|g|t|g|t|g|g|c|c|g|t|c|t|t|c|c|c|c|a|g|g|g|a|g|c|c|a|t|t|g|t|g|g|c|c|g|t|g|a|c|g|g|g|t|g|a|c|g|g|g|ei
c|c|a|g|c|c|t|g|g|g|t|g|a|c|a|c|a|g|c|a|a|a|a|c|t|a|t|c|t|c|a|a|a|a|a|a|a|a|a|a|a|a|a|a|a|a|a|a|a|a|g|g|a|a|c|c|c|a|ei
a|t|t|c|t|a|g|c|t|a|a|t|g|t|a|a|t|a|a|c|t|g|t|a|g|t|t|t|a|c|a|t|t|g|t|a|a|a|t|a|g|t|a|t|t|t|g|a|g|a|g|t|t|c|t|a|a|a|ei
a|g|g|c|t|g|c|a|t|g|t|g|g|a|c|c|c|t|g|a|a|a|a|t|t|a|a|g|g|t|a|a|g|c|c|c|a|g|g|a|g|a|t|g|t|t|a|a|a|g|c|c|c|t|t|t|t|g|ei
c|g|g|c|g|c|c|g|c|g|a|g|c|t|t|c|t|c|c|t|c|t|c|t|a|c|g|a|c|c|g|a|g|g|c|a|g|a|g|c|a|g|t|c|a|t|t|a|t|g|g|c|g|a|a|c|c|t|ei
c|c|a|a|t|t|c|a|a|a|a|a|t|a|g|c|a|g|a|a|c|a|g|g|t|g|t|t|g|a|g|a|a|g|g|t|g|a|t|g|g|a|g|t|a|g|a|a|g|g|g|g|g|a|g|c|g|c|ei
c|g|c|t|c|c|a|a|c|t|c|t|a|c|c|g|c|t|g|c|t|a|c|a|t|g|a|g|g|t|t|c|c|t|g|a|g|g|t|c|a|c|a|g|t|g|t|t|t|t|c|c|a|a|g|t|c|t|ei
a|a|a|c|t|g|g|g|g|c|c|t|g|a|g|a|c|g|c|c|c|c|t|g|c|a|t|g|g|a|c|c|g|c|t|t|c|c|c|a|t|a|c|c|t|g|g|c|t|c|t|g|t|c|c|a|a|g|ei
a|t|t|t|g|g|a|g|g|g|c|t|t|c|t|t|t|g|c|c|a|c|c|t|g|g|c|g|g|t|a|t|g|a|g|c|c|g|g|g|t|g|t|g|g|g|t|g|g|g|g|t|g|t|g|c|a|g|ei
t|t|t|t|t|t|g|a|g|a|t|g|g|a|g|t|t|t|t|g|c|t|c|t|t|t|g|c|c|c|a|g|g|c|t|g|g|a|g|t|g|c|a|a|t|g|g|t|g|c|a|t|c|t|t|g|g|c|ei
c|c|t|c|g|a|g|a|a|g|g|c|a|a|a|g|c|a|g|a|c|t|c|g|a|g|a|a|c|g|a|g|c|g|g|g|g|g|g|a|g|c|t|g|g|c|c|a|a|c|g|a|g|g|t|g|a|a|ei
a|t|a|c|c|t|t|g|g|c|g|c|t|a|g|t|a|t|t|t|g|a|a|c|c|c|a|a|g|t|a|a|g|t|c|g|t|a|c|c|t|t|t|t|t|a|c|c|g|a|g|t|c|a|c|g|a|a|ei
t|t|c|t|t|t|g|a|a|t|a|a|a|t|c|c|t|t|a|c|t|a|t|t|c|c|a|g|g|a|c|a|a|c|t|g|c|a|c|c|a|g|a|c|c|a|t|g|c|t|t|c|a|g|t|g|a|g|ei
c|c|a|g|t|g|c|c|g|c|c|t|g|g|a|a|a|a|g|c|t|g|c|g|t|g|g|a|g|t|a|t|t|g|c|a|g|c|c|t|c|t|c|g|g|c|t|g|c|c|a|g|c|t|g|c|g|a|ei
c|g|g|c|c|g|c|t|g|c|c|c|g|g|c|c|c|c|g|g|c|g|a|c|g|a|g|g|g|c|g|g|a|g|c|g|c|g|g|c|g|c|c|g|g|a|g|c|c|g|a|g|g|g|c|c|g|c|ei
g|t|c|a|c|a|t|a|t|a|c|t|g|a|c|c|t|c|t|g|a|c|a|c|t|t|a|g|g|g|a|a|g|t|c|a|g|t|g|g|g|a|g|t|g|g|t|a|a|c|c|a|c|c|a|c|a|c|ei
g|a|c|t|a|a|c|g|a|c|a|c|a|t|a|c|a|t|g|a|a|a|t|t|g|c|t|g|g|t|t|a|a|c|g|g|t|g|c|c|a|g|a|a|g|a|g|t|c|a|c|t|g|g|a|c|a|a|ei
c|a|g|g|g|c|a|g|g|a|g|a|c|c|c|t|c|t|g|g|c|c|t|c|c|c|c|t|c|t|c|t|t|g|c|c|c|t|c|a|g|c|c|t|c|c|a|c|c|t|c|c|t|t|g|a|c|t|ei
t|g|g|g|g|g|t|t|g|c|t|t|t|g|c|g|g|t|g|g|c|a|g|a|g|c|c|c|c|t|t|g|c|a|t|c|c|t|g|a|g|c|t|c|c|t|t|g|g|a|g|t|a|g|g|g|a|c|ei
g|t|c|a|a|g|a|t|t|g|a|c|c|a|g|a|c|c|g|t|g|g|a|g|g|c|t|g|c|g|c|c|g|c|a|g|c|c|t|g|g|c|t|c|c|c|t|a|t|g|c|t|c|a|g|g|a|c|ei
a|g|a|t|a|g|a|g|g|a|t|g|a|c|a|t|t|g|g|a|a|g|g|g|g|c|a|g|a|a|a|t|g|a|a|t|g|a|a|c|t|t|a|t|g|g|a|g|c|a|g|a|c|c|t|c|g|g|ei
a|c|t|g|a|g|a|c|a|c|a|g|g|a|a|g|g|g|c|c|g|c|g|c|g|a|g|c|a|c|t|g|a|a|g|a|c|g|c|t|t|g|g|g|g|a|a|g|g|g|a|a|c|c|c|a|c|c|ei
c|a|g|g|a|c|c|t|c|a|c|c|a|c|g|g|a|a|a|g|c|a|a|c|g|c|t|g|g|t|a|c|g|t|g|g|g|c|c|a|t|g|a|c|t|g|c|c|a|t|c|t|t|g|g|c|t|t|ei
c|a|a|t|a|c|a|c|t|t|a|a|t|t|a|t|c|t|t|t|a|t|c|t|t|t|a|g|g|t|t|a|c|c|c|a|t|g|c|a|g|t|t|g|t|t|a|c|t|g|t|a|c|c|a|g|c|c|ei
t|t|a|a|t|g|t|c|t|c|c|c|a|a|a|c|c|t|c|a|c|c|c|a|c|c|a|g|g|a|g|a|a|a|t|t|c|c|g|g|a|g|t|g|a|c|t|c|t|a|t|c|a|c|c|a|a|c|ei
g|g|g|g|t|a|a|t|t|t|t|t|t|a|t|g|g|a|g|a|g|g|t|a|t|g|a|c|a|t|c|a|a|g|a|c|c|a|g|a|a|g|c|t|g|g|a|g|c|t|a|t|g|g|t|c|a|g|ei
a|g|a|t|c|a|g|t|a|a|a|g|a|a|c|g|t|g|g|t|c|a|g|g|a|g|a|a|c|c|c|c|t|g|a|a|g|t|a|t|t|t|t|t|t|a|a|t|c|c|t|a|c|c|t|c|a|a|ei
c|a|a|a|g|c|t|a|a|g|a|a|g|a|a|g|g|a|a|c|t|g|g|a|a|a|a|t|t|g|t|t|c|a|a|c|c|a|a|t|t|a|t|c|a|g|c|a|a|a|c|t|c|t|a|t|g|g|ei
c|t|g|g|a|c|a|g|g|t|t|g|g|a|g|g|a|g|g|t|g|a|c|a|t|g|a|a|t|c|g|g|g|c|t|a|t|g|t|g|g|a|c|g|t|g|t|t|g|a|c|c|c|t|t|c|t|g|ei
t|c|a|a|g|g|c|c|a|a|c|a|a|c|a|a|t|g|a|c|a|g|c|g|g|a|g|t|a|c|a|c|g|t|g|c|c|a|g|a|c|t|g|g|c|c|a|g|a|c|c|a|g|c|c|t|c|a|ei
t|g|g|c|c|t|c|c|t|c|t|c|t|t|c|c|t|t|g|g|a|c|c|c|c|c|a|g|g|t|g|t|g|c|a|g|c|t|g|g|c|t|g|g|c|t|g|g|c|t|g|g|c|a|g|c|g|g|ei
a|c|c|a|t|g|t|c|c|t|t|c|t|c|g|c|t|t|g|g|c|c|t|t|c|c|a|g|g|a|c|g|t|g|g|a|t|g|c|a|g|c|t|a|c|t|c|t|a|g|c|t|c|g|c|a|t|t|ei
c|t|g|a|g|c|g|t|g|g|c|t|a|c|t|c|c|t|t|c|g|t|g|c|a|c|a|g|g|t|g|c|g|c|g|g|c|g|c|c|c|c|t|g|c|a|c|c|c|g|g|g|c|g|g|a|g|g|ei
g|g|c|t|g|t|t|t|c|c|t|t|t|g|g|g|c|t|a|t|c|c|a|g|c|c|a|c|c|t|a|c|a|c|t|g|c|c|c|t|t|t|t|t|a|a|t|c|c|t|t|a|c|a|a|t|t|t|ei
c|t|t|a|t|a|a|c|a|t|c|a|c|a|t|t|t|a|a|a|a|g|c|t|t|c|a|g|g|t|a|a|c|t|a|t|a|t|t|t|t|g|a|a|t|t|t|t|t|t|a|a|a|a|a|a|g|t|ei
a|g|a|c|a|c|c|g|c|c|c|a|c|c|a|c|c|a|g|c|a|g|c|a|t|c|t|g|g|t|a|a|g|c|g|a|a|g|c|c|c|g|c|c|c|a|g|g|c|c|t|g|t|c|a|a|a|a|ei
c|a|g|a|g|c|c|a|g|c|a|a|g|a|t|g|g|g|g|g|c|t|c|g|g|a|c|a|c|c|c|g|c|a|g|g|g|a|c|a|g|g|a|g|g|a|t|t|t|t|g|t|g|g|g|g|g|c|ei
t|a|t|g|g|g|c|a|g|c|t|c|g|t|c|t|t|c|a|c|c|g|t|a|g|g|a|g|g|t|a|c|g|g|g|c|c|g|g|g|g|g|g|t|g|g|g|c|g|g|c|c|t|c|a|c|g|g|ei
t|c|t|g|g|g|c|a|t|a|g|g|a|g|t|g|t|a|t|c|c|t|g|t|c|c|a|a|c|a|g|a|c|c|c|c|a|g|g|a|c|a|g|g|g|c|c|t|t|c|a|g|t|t|c|c|t|c|ei
g|g|g|a|t|g|g|g|c|t|g|c|a|c|c|g|t|g|a|g|c|g|c|g|g|g|a|c|a|a|g|g|c|g|g|c|g|g|c|c|g|a|g|c|g|c|t|c|t|a|a|g|a|t|g|a|t|c|ei
t|c|a|g|c|t|t|t|t|t|c|t|t|t|t|c|t|c|t|c|t|c|c|c|t|c|a|g|g|a|t|c|a|t|c|t|t|c|t|c|g|a|a|c|c|c|c|g|a|g|t|g|a|c|a|a|g|c|ie
a|t|c|a|a|a|t|a|a|a|a|c|a|g|g|g|a|t|t|c|t|a|a|a|g|c|t|a|t|t|a|g|a|a|t|t|g|t|g|a|g|g|c|t|c|a|g|g|g|t|g|g|g|c|a|c|g|g|ei
a|t|c|a|t|t|t|g|g|t|a|t|c|a|t|a|a|c|a|a|a|a|t|c|c|a|a|t|t|t|t|g|g|c|a|t|t|c|a|t|t|t|t|g|a|t|c|a|t|t|t|c|a|a|g|a|a|a|ei
g|g|t|c|a|c|a|a|c|t|c|t|c|c|c|c|a|g|a|g|a|a|g|t|g|t|g|t|g|a|g|g|c|c|a|t|c|a|c|g|g|a|a|g|a|t|g|c|t|g|c|t|g|c|t|t|c|t|ei
c|g|g|a|g|a|c|g|c|t|c|t|t|c|c|a|g|c|c|c|t|c|c|t|a|t|c|g|g|t|g|a|g|c|c|c|c|g|c|t|c|g|c|c|c|t|c|g|c|c|c|c|g|g|c|c|c|c|ei
g|g|a|c|c|a|g|g|a|c|c|a|a|c|a|a|a|a|a|c|t|a|a|a|t|g|c|a|g|g|t|c|c|a|g|a|t|c|a|a|a|c|a|g|a|a|a|t|g|a|c|t|a|t|t|g|a|a|ei
g|a|c|a|g|a|g|c|c|g|a|g|a|c|t|c|c|a|t|c|t|c|a|a|a|a|t|a|c|g|a|a|a|a|c|a|a|a|a|a|t|c|a|g|c|c|g|g|g|t|g|g|t|g|g|c|g|g|ei
g|t|c|a|t|t|a|a|g|a|t|t|g|t|t|g|a|t|c|t|g|c|c|t|c|t|a|g|a|c|g|a|a|g|a|t|g|a|g|t|c|g|a|g|t|g|a|g|c|a|g|a|c|c|t|t|t|a|ei
a|c|t|c|a|c|t|g|a|g|a|c|a|g|t|c|t|t|t|g|t|t|t|t|c|t|a|g|g|g|c|a|c|a|g|t|c|g|t|a|g|t|g|c|c|a|a|c|t|c|t|g|g|a|c|t|c|t|ei
g|g|t|g|a|a|c|c|t|g|g|a|c|g|a|g|a|g|g|t|g|a|g|a|t|g|a|g|a|c|c|c|c|c|t|g|g|g|g|t|g|g|c|c|c|t|g|a|t|t|g|g|g|g|a|g|a|g|ei
t|g|a|t|g|c|g|g|g|g|a|c|t|g|g|a|g|t|t|g|c|t|c|t|t|a|c|t|t|t|a|a|c|a|a|c|a|a|c|g|t|t|c|c|g|a|t|a|g|a|t|g|a|t|t|c|a|g|ei
c|c|t|t|c|c|t|c|c|t|g|c|t|g|c|c|c|a|g|g|g|c|a|a|g|c|a|g|g|t|g|a|g|t|g|a|c|c|g|t|c|t|c|c|a|c|c|c|t|c|g|g|g|g|g|c|c|c|ei
t|t|g|g|a|g|a|t|a|a|a|c|t|t|c|c|t|g|a|a|t|g|t|a|g|c|a|g|g|t|g|g|g|t|g|c|t|g|a|g|c|a|c|t|g|a|g|c|a|c|t|t|a|a|g|a|g|a|ei
c|t|c|a|c|g|a|g|g|c|t|t|g|c|t|c|t|c|t|t|g|t|t|c|t|c|a|g|a|a|g|c|t|g|t|t|c|t|g|g|a|t|t|t|c|t|t|a|c|a|g|t|g|g|t|g|a|g|ei
g|c|t|g|c|t|g|a|c|a|c|t|c|t|c|c|t|c|c|a|t|t|g|t|t|c|a|g|a|g|t|c|a|c|c|t|g|g|t|g|g|t|t|c|t|g|c|g|c|c|t|t|c|c|c|c|t|a|ei
g|a|a|a|a|g|g|a|g|g|g|a|g|c|t|g|c|t|c|t|c|a|g|c|g|c|g|t|g|t|a|a|g|t|g|a|t|g|g|c|g|g|c|a|g|g|c|g|t|g|t|g|g|a|g|g|a|g|ei
c|a|g|a|a|t|g|a|g|c|a|a|g|t|g|a|a|g|a|a|c|t|t|g|g|g|c|t|t|c|c|c|a|t|a|t|t|g|c|c|a|a|t|a|t|c|t|t|g|a|a|c|t|c|a|g|a|a|ei
g|t|t|g|c|c|c|g|t|g|g|g|g|t|g|c|a|a|a|a|g|a|t|c|g|c|a|g|g|t|g|a|g|t|a|t|a|t|t|a|c|t|a|t|g|t|g|g|g|a|t|c|a|g|t|g|t|c|ei
c|a|c|c|t|g|c|c|a|c|c|t|c|c|t|t|t|c|t|t|t|g|c|t|t|c|a|g|g|a|a|c|a|a|g|a|t|c|c|t|g|a|t|t|t|t|t|g|g|g|c|t|c|c|t|g|g|a|ei
c|g|g|a|g|c|c|c|t|c|a|c|c|a|g|c|a|t|t|t|g|t|t|c|a|c|a|g|c|c|g|a|t|a|t|t|a|t|g|t|a|c|a|c|g|g|g|g|a|c|a|g|t|t|g|a|c|t|ei
a|t|c|t|c|g|g|c|t|c|a|c|a|g|c|a|a|c|c|t|c|c|g|c|c|c|c|a|g|g|t|t|c|a|a|g|c|c|a|t|t|c|t|c|c|t|g|c|c|t|c|a|g|g|c|t|c|c|ei
c|c|g|a|g|t|c|a|c|t|c|c|t|g|t|c|a|c|t|t|a|c|c|t|a|c|a|g|g|c|c|t|a|g|a|c|t|c|c|c|g|a|g|g|c|t|t|c|c|t|c|t|t|t|g|g|c|c|ei
t|t|t|t|c|c|c|a|t|c|a|t|c|c|t|g|t|a|c|t|t|c|t|t|c|t|a|g|a|t|g|t|c|a|g|c|c|a|g|g|a|a|g|a|t|g|t|t|c|c|c|c|t|c|g|t|a|a|ei
g|c|a|a|a|a|g|t|a|a|g|t|t|g|c|t|g|t|t|t|g|t|a|t|c|c|a|g|g|c|c|t|t|g|g|a|c|a|a|g|a|t|t|c|g|c|t|a|t|g|a|g|a|g|c|c|t|g|ei
g|g|a|g|c|t|g|g|a|g|g|a|c|a|c|a|g|c|a|c|a|t|t|g|a|a|t|c|a|a|g|a|a|g|a|a|a|a|t|a|a|a|a|g|t|a|a|a|a|a|c|a|g|g|a|a|t|t|ei
t|a|a|a|a|c|c|a|t|a|t|g|a|t|g|g|t|t|c|t|c|c|c|t|t|c|a|g|t|g|t|c|t|c|c|t|t|t|c|t|a|t|t|c|g|g|a|g|c|g|g|c|t|g|a|a|g|g|ei
c|t|t|g|t|t|c|c|a|a|t|t|t|g|a|c|a|a|a|a|c|c|c|c|g|t|t|c|t|t|g|t|a|t|t|g|t|a|t|t|g|c|c|a|g|g|g|g|g|g|a|g|c|t|a|t|c|a|ei
t|g|g|a|g|a|a|c|a|g|g|g|g|g|c|c|a|g|a|a|c|t|t|g|c|a|g|t|a|a|a|g|a|a|t|a|a|a|a|g|g|c|c|a|g|a|c|a|g|a|g|a|g|g|c|a|g|c|ei
t|a|a|t|t|t|a|a|a|a|c|t|c|a|g|a|a|g|a|a|a|g|c|t|c|a|t|c|a|a|a|g|g|g|a|a|g|t|a|g|a|a|g|t|g|g|g|c|c|c|g|g|c|t|c|a|c|t|ei
c|t|t|a|t|g|a|g|a|a|a|t|a|g|t|a|t|t|t|g|c|c|t|g|g|t|t|t|t|c|a|t|a|t|a|a|a|a|t|a|t|c|g|c|a|t|g|a|t|a|a|t|a|c|c|a|t|t|ei
c|c|a|g|c|a|g|g|c|t|g|a|g|g|g|c|c|a|g|a|g|c|g|c|a|g|c|c|c|t|g|g|g|a|g|c|t|g|g|c|a|c|t|g|g|g|t|c|g|c|t|t|t|t|g|g|g|a|ei
a|a|t|g|g|t|g|a|c|t|t|c|c|g|t|t|a|c|a|c|c|a|c|a|a|a|t|g|g|g|a|g|t|g|a|a|c|a|c|c|t|a|c|a|a|g|g|c|c|c|g|t|a|t|c|c|a|g|ei
a|t|c|a|a|t|a|a|g|c|t|c|c|t|a|g|t|c|c|a|g|a|c|c|a|t|g|g|g|t|c|a|t|t|t|c|a|c|a|g|a|g|g|a|g|g|a|c|a|a|g|g|c|t|a|c|t|a|ei
c|t|g|a|g|g|c|t|t|g|g|a|c|g|c|c|c|c|c|a|t|t|c|t|g|c|a|g|g|a|g|c|a|g|c|g|c|a|a|c|c|a|t|t|t|g|c|a|g|g|g|c|a|a|a|c|t|g|ei
t|c|t|t|a|a|c|c|c|a|a|g|t|c|c|c|g|t|t|a|c|t|c|t|c|c|a|g|g|a|c|c|a|c|t|t|t|c|t|g|t|t|t|g|a|t|a|a|g|c|c|t|g|t|g|t|c|c|ei
g|a|a|t|t|t|g|t|t|c|a|t|g|a|c|t|a|t|t|g|t|g|t|c|g|t|a|g|c|c|t|g|a|g|a|c|a|g|c|t|g|c|c|t|g|t|g|t|g|g|g|a|c|t|g|a|g|a|ie
t|a|t|a|a|t|t|g|t|t|t|g|a|t|c|a|t|t|t|c|t|t|c|t|c|c|a|g|g|g|g|c|a|a|a|a|g|a|c|a|t|g|t|g|g|a|g|a|g|c|c|t|a|c|t|c|t|g|ei
g|g|a|c|c|a|c|c|c|c|c|a|c|a|a|g|g|a|g|g|c|a|a|c|g|c|c|t|c|a|a|g|g|t|c|c|c|c|c|a|c|c|t|c|c|t|c|c|a|g|g|a|a|a|g|c|c|a|ei
g|c|t|t|a|c|t|t|a|c|a|a|a|a|g|c|a|g|c|t|t|t|t|g|t|c|a|g|a|c|t|t|a|g|t|t|t|t|t|a|t|a|a|a|a|t|g|a|g|a|a|t|t|c|t|g|a|c|ei
t|c|c|t|t|g|g|t|a|a|c|t|a|t|g|t|g|t|g|t|c|t|t|c|a|t|a|g|g|t|g|a|t|g|g|t|g|t|t|t|c|t|t|a|g|a|g|a|g|a|a|g|a|t|c|a|c|t|ei
t|t|c|t|a|t|g|a|g|a|a|a|c|g|t|g|g|c|a|t|t|g|t|c|c|a|a|g|g|t|g|g|g|c|c|c|c|g|c|g|g|g|a|c|g|g|g|g|c|a|g|c|t|c|c|g|g|g|ei
a|g|g|g|g|g|c|t|g|a|a|t|c|c|t|c|a|g|t|t|t|a|a|g|c|c|t|g|g|a|c|c|t|g|g|g|a|g|c|t|t|a|t|g|g|a|a|g|a|g|c|a|a|g|g|g|g|c|ei
c|g|c|a|g|c|g|g|g|g|t|c|g|c|a|g|g|g|c|g|c|g|g|g|g|t|t|c|c|a|g|c|g|c|g|g|g|g|a|t|g|g|c|g|c|t|g|t|c|c|g|c|g|g|a|g|g|a|ei
g|a|c|c|a|a|g|g|a|g|a|g|t|c|a|g|g|a|g|a|c|c|c|c|a|c|a|a|a|t|t|t|g|c|a|t|c|a|a|a|a|c|c|c|g|c|g|a|g|c|g|a|g|t|t|t|g|t|ei
g|g|g|a|c|a|g|g|a|c|t|c|c|t|g|g|g|t|c|t|g|a|g|g|g|g|a|g|g|g|c|c|a|a|g|g|a|a|c|c|a|g|g|t|g|g|g|g|t|c|c|a|g|c|c|c|a|c|ei
t|c|t|t|t|t|c|g|t|t|c|c|t|t|g|g|c|g|a|g|g|c|t|t|g|a|t|g|g|t|a|a|g|g|c|t|t|c|a|g|a|a|g|g|t|t|t|g|c|a|g|g|a|t|t|t|c|t|ei
c|g|c|a|c|c|t|g|g|g|c|g|c|c|c|t|g|c|t|g|g|c|a|g|t|a|c|a|t|c|c|a|g|c|a|g|g|c|c|c|g|g|a|a|a|g|g|t|a|a|g|a|a|t|g|c|t|g|ei
c|g|a|g|a|a|g|t|g|c|g|a|g|g|t|g|a|a|c|g|g|t|g|g|g|g|g|c|g|c|a|c|c|c|t|c|t|c|t|t|c|g|c|c|t|t|c|c|t|g|c|g|g|g|a|g|g|c|ei
t|t|g|c|t|c|t|g|c|a|g|g|t|g|c|g|c|c|t|c|c|t|g|g|g|t|g|g|t|g|t|c|c|a|a|g|g|g|c|c|a|g|c|c|c|a|c|g|c|t|g|g|t|g|g|t|g|a|ei
t|g|c|g|c|g|g|c|t|a|c|t|a|c|a|a|c|c|a|g|a|g|c|a|g|c|c|g|g|g|t|c|t|c|a|c|a|c|c|c|t|c|c|a|g|a|g|g|a|t|g|t|a|t|g|g|c|t|ei
a|c|c|c|c|c|g|c|g|g|c|t|t|c|t|t|c|c|t|c|t|t|c|t|g|a|g|g|g|t|g|c|g|t|g|g|t|g|g|c|c|c|c|t|g|g|g|g|a|g|t|g|g|g|g|g|t|t|ei
g|a|t|t|c|c|c|c|t|g|a|t|c|t|a|g|c|a|c|c|c|c|c|c|g|c|a|g|g|c|g|c|t|g|c|g|c|c|c|c|t|c|a|t|c|c|t|g|t|c|t|c|g|g|a|t|t|g|ei
c|g|c|t|c|c|t|g|g|t|t|c|c|c|c|c|t|c|a|t|t|t|c|t|c|c|a|g|g|g|g|c|c|a|c|t|t|t|t|g|a|c|a|a|a|c|g|a|t|c|c|c|c|t|a|c|g|t|ei
c|a|a|a|a|g|a|a|c|a|a|a|g|c|t|g|g|a|g|g|c|a|t|a|g|c|t|a|c|c|t|g|a|c|t|t|c|a|a|a|c|t|a|t|a|c|t|a|c|a|a|g|g|c|t|a|c|a|ei
g|g|a|t|t|t|a|a|a|a|t|a|t|t|a|t|g|t|t|g|a|a|t|g|c|t|t|c|t|c|a|c|t|c|t|t|t|t|t|c|c|c|c|t|t|t|t|a|c|t|t|a|g|a|a|c|a|t|ei
a|t|t|t|t|g|a|g|a|a|a|a|a|t|a|c|a|t|g|t|g|a|g|c|t|t|t|t|t|t|c|t|g|t|t|t|c|t|c|t|t|t|t|c|t|c|t|t|a|a|c|g|a|t|t|a|t|c|ei
t|g|c|t|g|a|t|g|t|c|c|c|t|c|t|g|t|c|g|g|g|t|t|t|g|c|a|g|c|g|t|c|g|g|c|g|t|g|t|t|c|a|a|g|a|a|c|g|g|c|c|g|c|g|t|g|g|a|ei
t|a|a|g|g|g|a|a|c|t|c|a|g|a|g|g|c|t|g|g|c|g|g|a|c|c|t|c|c|a|t|a|t|g|c|t|g|a|a|c|g|c|t|g|g|t|t|c|c|c|c|g|g|g|t|c|c|c|ei
a|c|c|a|g|g|g|a|a|t|g|g|c|a|g|c|a|g|c|a|t|g|c|g|a|t|c|t|t|a|g|c|a|c|t|c|t|t|t|a|g|c|a|c|a|a|t|a|t|t|t|t|g|t|a|t|t|a|ei
g|t|a|a|g|g|a|c|t|g|c|t|t|g|g|c|t|a|t|t|a|a|c|a|c|a|g|t|t|a|a|t|a|g|t|t|t|a|c|t|c|a|t|t|t|a|t|t|t|a|t|t|g|c|t|g|t|c|ei
a|g|c|a|t|t|g|g|c|a|g|g|a|g|g|g|g|c|a|a|g|g|t|g|a|c|a|g|g|t|g|a|g|g|a|a|c|t|c|t|a|g|c|g|t|a|c|t|c|t|t|c|c|t|g|g|g|a|ei
c|t|g|a|a|a|t|t|t|g|t|c|c|c|a|t|t|c|a|t|a|t|c|t|g|c|a|g|a|g|a|a|g|c|t|c|c|a|t|g|a|a|g|a|a|a|t|t|g|a|c|a|g|g|g|t|g|a|ei
t|t|c|c|a|a|g|g|a|g|g|g|a|c|c|t|c|t|c|t|g|c|c|c|c|a|c|c|a|t|t|a|c|c|a|t|c|a|c|t|g|t|g|a|c|t|t|t|c|c|c|c|a|a|g|c|c|c|ei
a|c|c|a|t|c|c|a|g|a|a|t|g|a|c|a|t|c|a|t|g|t|t|t|g|c|a|g|g|t|a|c|c|a|c|c|t|a|c|c|t|g|g|c|c|c|t|c|t|g|g|c|t|c|c|t|t|c|ei
a|g|a|a|a|c|t|a|t|a|a|a|a|t|c|t|c|t|g|t|a|g|a|a|t|t|t|c|t|c|a|t|a|a|a|t|a|a|t|c|t|t|a|t|g|a|a|c|c|a|t|t|a|t|g|g|t|g|ei
t|a|t|g|a|a|a|a|g|t|t|g|t|t|c|t|t|g|t|g|g|a|t|g|c|a|c|t|c|g|c|a|t|t|a|a|c|c|a|g|c|a|a|c|t|g|g|a|t|a|c|g|a|a|g|c|t|t|ei
a|g|c|a|a|a|g|a|g|g|t|c|c|t|g|a|t|g|g|a|g|a|g|c|g|c|c|g|g|t|g|a|g|t|g|t|g|g|t|t|g|c|g|t|g|t|g|t|g|t|a|t|g|t|a|t|g|t|ei
c|c|t|a|t|g|t|a|c|c|t|t|t|c|t|a|t|c|c|c|t|c|t|t|a|a|g|c|t|t|c|t|g|c|a|g|a|a|t|t|c|c|c|a|g|c|a|a|g|a|c|a|g|a|g|c|t|t|ei
c|c|g|t|c|c|a|t|c|g|t|g|g|g|c|c|g|c|c|c|c|c|g|c|c|c|a|g|g|t|c|a|g|g|c|t|g|c|c|c|c|t|c|c|g|c|a|g|a|g|g|g|a|g|c|c|g|g|ei
a|a|g|c|t|t|c|g|g|g|t|g|g|a|c|c|c|g|g|t|c|a|a|t|c|a|a|g|g|t|g|a|g|c|g|g|c|g|g|g|c|c|g|g|g|a|g|c|g|a|t|c|t|g|g|g|t|c|ei
t|t|t|a|a|a|a|a|g|c|g|g|c|g|a|c|t|c|c|g|t|t|c|c|c|c|g|t|g|t|g|c|t|g|t|t|t|a|g|c|a|c|c|c|a|g|c|c|t|c|c|c|c|g|t|g|a|a|ei
g|a|t|t|c|t|c|c|t|g|t|g|c|t|a|g|a|t|g|t|g|c|a|a|g|c|a|a|g|c|t|a|g|t|g|g|c|t|t|c|a|a|a|a|t|a|g|a|g|a|a|t|c|c|c|a|c|t|ei
a|t|t|c|c|c|t|a|c|g|g|a|a|a|c|t|a|g|c|a|a|t|g|g|c|t|c|c|t|g|g|c|c|a|t|c|t|g|g|a|t|c|t|c|g|t|g|g|a|a|g|g|g|a|g|c|c|t|ei
a|g|t|g|a|a|a|t|t|t|c|c|t|a|a|g|a|t|c|c|t|g|g|g|a|t|t|t|c|c|t|a|c|c|c|c|c|g|t|c|c|t|c|t|t|c|g|a|g|a|c|c|c|c|a|g|t|c|ei
a|t|c|t|c|a|c|t|c|t|c|t|c|c|c|t|g|c|t|t|t|t|a|c|t|t|a|g|g|g|t|g|a|t|t|c|t|g|g|g|g|g|c|c|c|a|c|t|t|g|t|c|t|g|t|a|a|t|ei
t|t|a|t|t|c|a|a|a|t|t|t|t|t|g|t|t|a|g|t|c|t|t|c|a|a|t|g|t|c|t|t|t|t|a|t|a|g|g|g|a|a|a|a|a|a|a|a|a|a|a|a|a|a|a|a|g|c|ei
g|a|g|a|a|g|a|g|c|t|c|a|g|a|g|t|g|t|c|t|c|t|g|c|c|c|a|g|a|c|a|t|a|c|a|a|t|g|t|a|g|a|c|a|a|a|c|a|t|g|t|g|c|c|a|g|a|c|ei
c|t|c|c|a|c|g|t|c|t|g|t|c|t|g|t|c|t|g|t|g|g|a|c|g|t|g|t|g|t|t|t|t|g|a|g|t|c|t|g|a|c|a|g|t|c|t|a|c|c|t|g|g|c|t|g|g|t|ei
c|a|g|g|t|t|t|c|t|g|c|g|g|c|c|c|c|c|c|g|g|a|c|g|g|g|c|t|c|t|g|a|c|g|g|c|g|t|t|a|c|t|g|a|t|g|g|t|g|c|t|g|c|t|c|a|c|a|ei
c|c|a|g|t|c|c|g|c|t|c|a|g|c|c|c|a|g|c|c|c|a|a|c|c|a|g|c|c|c|a|g|c|g|c|c|a|a|c|c|c|a|g|c|t|c|g|g|c|t|t|a|a|c|c|c|a|g|ei
c|c|c|c|c|c|a|t|c|c|c|c|a|g|c|t|a|c|c|t|g|a|a|g|c|c|t|g|g|a|g|c|g|t|a|t|t|g|c|a|c|a|g|a|g|t|g|a|c|t|a|c|a|t|c|c|c|c|ei
c|a|c|t|g|a|g|g|g|g|c|c|t|t|c|t|g|a|c|a|t|g|a|t|t|g|c|c|t|g|g|c|c|c|c|a|c|c|t|c|c|t|a|g|t|t|c|c|t|c|a|t|a|a|t|a|a|a|ei
g|g|g|c|c|c|t|g|a|c|c|c|t|g|a|c|c|g|a|g|a|c|c|g|g|c|g|g|g|t|g|a|g|t|g|c|g|g|g|g|t|c|a|g|g|a|g|g|g|a|a|a|c|g|g|c|c|c|ei
g|g|c|t|a|a|g|g|a|c|a|c|c|t|a|t|t|c|c|t|t|c|c|g|a|t|a|g|g|g|a|t|g|t|c|a|g|a|c|c|a|g|g|c|g|a|t|c|a|t|g|g|a|g|c|t|g|a|ei
g|g|c|a|a|t|g|a|c|g|c|t|t|t|c|t|c|t|t|c|c|t|c|c|a|c|a|g|a|g|g|a|t|g|t|c|a|c|c|c|c|c|a|t|c|c|c|c|t|c|t|g|a|c|a|g|c|a|ei
c|t|t|c|c|a|t|g|g|g|a|t|t|g|a|a|a|a|t|t|t|c|a|c|a|t|g|a|a|g|c|t|t|c|t|t|a|c|a|t|g|a|g|c|a|t|t|t|t|a|g|g|a|a|t|g|a|c|ei
g|g|a|g|a|t|g|a|a|g|a|a|g|a|g|a|g|t|c|g|a|g|g|c|t|c|c|a|t|g|t|a|g|g|t|g|c|c|a|c|g|g|t|g|g|c|c|c|c|c|a|g|c|a|g|c|a|g|ei
t|g|g|g|t|t|g|g|g|g|a|c|a|g|a|t|t|t|c|a|t|g|c|g|a|a|t|c|a|g|g|a|g|g|a|t|g|g|a|t|g|c|t|g|a|g|g|a|t|g|t|t|g|g|g|g|t|t|ei
t|t|t|t|c|c|a|t|c|t|g|c|t|a|t|g|g|t|g|c|c|a|t|t|a|c|a|g|g|c|t|c|c|t|c|g|t|t|g|t|c|t|a|c|c|c|c|t|g|g|a|c|a|c|a|g|a|g|ei
c|c|t|g|a|c|t|c|t|c|a|g|c|c|t|g|g|c|t|a|t|c|t|t|c|t|a|g|a|a|t|g|t|c|c|t|g|c|c|t|g|g|c|t|g|t|g|g|c|t|t|c|t|c|c|t|g|t|ie
a|a|g|g|t|t|a|c|c|t|t|g|a|a|c|a|a|t|g|a|c|a|g|a|t|g|t|c|t|t|t|g|c|t|g|a|c|a|g|a|g|c|c|c|a|g|c|t|g|g|t|t|a|g|t|g|g|c|ei
c|a|t|t|c|a|g|c|c|a|g|c|t|c|a|g|g|g|g|a|a|g|g|c|g|g|g|g|c|c|c|t|g|a|a|g|c|c|a|g|g|g|g|a|t|g|g|a|g|c|t|g|c|a|g|g|g|a|ei
c|c|a|a|c|a|t|a|g|t|g|a|a|a|c|c|c|c|c|a|a|c|c|c|a|c|t|a|a|a|a|a|t|a|c|a|a|a|a|a|t|t|a|g|c|t|g|g|g|g|t|g|t|g|g|t|g|g|ei
g|t|t|a|t|g|g|c|g|a|c|c|c|g|c|a|g|c|c|c|t|g|g|g|c|g|t|g|g|t|g|a|g|c|a|g|c|t|c|g|g|c|c|t|g|c|c|g|g|c|c|c|t|g|g|c|c|g|ei
a|g|a|c|a|t|c|g|c|c|c|a|c|c|a|c|c|a|g|c|a|g|c|a|t|c|t|g|g|t|a|a|g|c|g|a|a|g|c|g|c|g|c|c|c|a|g|g|c|c|t|g|t|c|a|a|a|a|ei
c|a|c|c|c|a|c|c|g|g|c|a|c|a|c|a|g|a|c|c|c|c|a|c|a|c|g|a|c|a|c|c|c|a|t|c|a|g|c|a|c|c|a|c|c|a|c|c|a|c|g|g|t|g|a|c|c|c|ei
t|g|a|g|a|g|a|t|g|a|a|g|a|t|c|c|a|g|t|t|t|c|a|t|t|c|c|t|a|c|a|t|g|t|a|g|c|t|t|g|c|c|a|g|c|t|a|t|c|c|c|g|a|c|t|c|a|t|ei
g|a|g|c|g|t|c|t|g|c|a|g|a|c|g|g|t|c|a|c|c|a|a|t|c|t|t|c|a|t|c|a|c|t|t|c|a|c|t|g|g|c|c|t|g|t|g|c|t|g|a|t|c|t|g|g|t|c|ei
g|c|c|t|g|c|g|g|g|g|a|g|c|a|c|c|t|g|g|a|g|g|c|t|t|g|c|t|t|t|g|c|t|g|g|a|g|c|g|c|t|t|c|a|g|c|g|g|c|t|a|c|c|g|g|g|a|a|ei
g|a|g|g|a|g|a|a|g|g|g|g|a|g|g|a|g|g|a|g|a|g|g|g|a|g|g|a|a|a|g|c|a|g|g|c|c|t|g|t|c|c|c|t|t|t|a|a|g|g|g|g|g|t|t|g|g|c|ei
t|t|a|t|g|c|t|t|t|c|c|t|t|t|a|t|c|c|c|t|c|t|g|a|a|c|a|g|g|a|g|a|c|a|g|a|c|c|a|a|c|t|a|g|a|a|g|a|t|g|a|g|a|a|g|t|c|t|ei
c|t|g|g|a|g|g|t|g|g|g|c|a|g|g|a|a|g|g|a|c|c|g|g|t|c|t|a|a|a|g|c|t|g|g|a|g|g|t|g|g|c|t|g|c|t|c|a|g|a|g|t|c|c|c|a|g|c|ei
c|a|c|c|t|a|g|g|t|t|t|a|c|a|a|a|t|a|t|t|t|t|t|g|a|c|t|c|a|c|g|t|t|a|a|c|t|c|a|c|a|t|t|t|a|t|a|c|a|g|c|a|g|a|a|a|t|g|ei
a|a|g|g|c|t|c|c|a|t|a|t|a|t|c|c|a|t|t|c|a|g|a|t|t|c|t|c|a|a|c|a|c|a|a|g|a|a|g|t|t|g|c|t|t|g|t|a|g|t|a|a|a|a|t|g|t|a|ei
a|g|c|t|c|g|g|c|c|c|a|g|c|t|t|g|g|c|t|c|a|g|c|c|a|c|a|c|a|g|c|c|t|g|c|t|c|a|g|c|c|c|a|g|t|t|c|a|g|c|t|c|g|g|c|t|c|a|ei
a|g|c|t|a|a|g|t|c|c|t|g|c|c|c|t|c|a|t|t|t|c|c|t|t|c|a|g|g|c|a|t|g|g|a|g|t|c|c|t|g|t|g|g|c|a|t|c|c|a|c|g|a|a|a|c|t|a|ie
a|a|g|g|g|a|g|g|a|a|c|a|g|a|a|a|t|g|a|g|a|c|c|c|a|t|c|t|t|t|c|c|c|t|a|t|a|a|a|a|a|c|a|a|c|a|t|t|t|t|t|a|c|t|g|t|c|t|ei
c|a|a|g|a|g|g|t|t|t|c|t|g|a|g|t|g|t|g|a|g|g|a|t|c|t|c|t|g|g|a|g|t|g|g|a|a|t|g|g|c|c|c|t|c|a|c|a|g|g|t|a|g|g|a|g|t|g|ei
c|c|t|g|g|t|g|a|a|g|a|c|c|a|a|g|g|a|g|g|a|g|c|g|a|c|c|t|g|g|t|g|a|t|g|a|c|a|g|c|a|c|c|c|c|c|g|c|c|c|c|c|a|c|c|a|c|c|ei
a|g|c|c|t|c|c|c|a|g|a|g|g|a|a|g|a|t|a|c|c|a|a|c|c|a|a|g|g|t|a|g|g|c|a|t|t|c|t|a|g|c|t|t|t|t|t|c|a|g|g|c|c|c|t|g|a|g|ei
g|g|g|c|g|g|g|g|c|t|g|a|c|c|g|a|g|g|g|g|g|t|g|g|c|c|a|g|g|t|t|c|t|c|a|c|a|c|c|c|t|c|c|a|g|t|g|g|a|t|g|a|t|t|g|g|c|t|ei
g|a|g|t|a|t|g|g|a|t|t|t|c|a|c|a|t|t|c|t|a|a|c|c|t|t|a|g|a|a|g|c|t|g|c|a|g|g|a|t|g|c|t|g|a|a|a|t|t|g|c|a|a|g|g|c|t|g|ei
a|a|g|a|a|t|g|c|t|t|a|c|a|a|t|a|a|a|c|t|c|t|c|t|c|a|g|g|g|t|c|t|t|c|c|t|g|g|a|t|c|a|c|a|a|c|g|c|c|c|t|c|c|c|c|g|a|c|ei
c|c|c|c|a|a|c|t|t|g|a|g|a|t|g|t|a|t|g|a|a|g|g|t|t|t|g|g|t|c|t|c|c|c|t|g|g|g|a|g|t|g|g|g|t|g|g|a|g|g|c|a|g|c|c|a|g|g|ei
c|t|c|c|t|g|a|g|a|c|c|t|t|c|a|t|c|a|c|t|g|t|g|c|c|c|a|g|g|t|c|t|c|a|a|g|a|g|c|t|g|t|t|c|t|g|c|t|c|c|c|t|c|a|g|t|c|a|ei
t|g|t|t|a|c|t|t|t|c|c|t|c|t|t|c|t|g|t|g|a|t|t|c|c|t|a|c|t|c|a|t|t|t|t|t|t|t|t|t|t|c|a|g|g|a|c|a|c|a|g|t|g|g|t|g|g|c|ei
g|g|t|g|g|a|g|g|a|g|g|c|t|t|t|c|a|t|a|t|t|c|g|g|c|a|t|g|a|c|c|c|c|t|c|a|a|g|g|c|g|g|g|c|c|a|t|t|c|g|t|g|t|g|c|a|c|c|ei
g|a|g|g|t|a|t|g|t|t|t|c|a|c|a|g|t|a|t|g|a|t|a|g|a|t|g|t|t|g|c|c|t|g|t|t|c|t|g|g|c|a|a|g|c|t|t|t|t|t|c|t|a|t|t|g|c|t|ei
c|a|c|a|t|a|c|c|t|g|c|a|t|c|a|t|t|t|t|c|a|t|c|t|t|c|t|t|t|c|a|g|c|a|a|c|t|g|a|c|c|c|t|c|t|c|a|a|c|t|g|g|a|t|g|t|a|g|ei
a|a|g|c|c|a|g|a|t|a|t|g|t|c|t|g|t|g|t|t|c|t|c|t|g|c|a|g|t|a|c|t|g|a|a|g|a|t|a|a|c|a|g|c|c|a|g|g|g|a|g|g|a|c|a|a|g|c|ei
a|g|a|a|a|t|g|a|a|a|c|a|g|g|a|c|c|c|t|a|t|c|a|t|t|g|a|a|a|t|a|c|g|g|g|a|c|c|g|a|t|a|t|g|g|t|g|g|c|a|t|c|c|g|c|a|g|t|ei
a|g|a|g|a|a|g|a|g|c|t|c|a|g|a|g|t|g|t|c|t|c|t|t|c|c|a|g|a|c|a|t|a|c|a|g|t|g|t|a|g|a|c|a|a|g|c|a|t|g|t|g|c|c|a|g|a|c|ei
a|g|t|g|a|t|t|g|a|c|t|t|t|a|a|c|t|g|c|a|c|c|a|a|g|t|t|c|t|g|t|c|t|c|t|t|c|a|g|c|a|c|t|g|g|c|c|a|a|t|a|c|c|a|a|a|g|a|ei
c|t|a|g|a|g|g|a|a|g|g|c|a|t|c|c|a|a|a|c|g|c|t|a|g|g|g|g|g|t|g|g|g|g|g|t|g|g|c|g|c|t|a|g|g|g|g|t|c|c|c|c|a|a|t|c|t|t|ei
c|a|a|t|c|c|a|t|t|c|t|t|t|t|c|t|c|g|a|t|t|t|c|t|c|c|a|g|g|a|t|a|t|g|t|g|a|g|g|a|c|g|c|a|g|a|t|g|t|c|t|g|g|t|a|a|t|g|ei
t|c|t|c|c|c|t|g|g|g|a|c|t|c|t|t|g|a|t|c|a|a|a|c|c|g|g|c|c|c|t|t|t|c|c|c|c|a|g|c|c|t|t|a|g|c|g|a|g|g|c|g|c|c|c|t|g|c|ei
g|c|c|g|a|a|a|g|c|t|g|c|c|c|g|c|g|a|g|t|c|g|g|g|g|g|a|g|c|a|g|g|c|c|c|c|c|c|a|c|c|a|c|c|a|c|g|c|a|g|a|g|a|g|a|g|t|c|ei
t|a|g|t|c|a|c|c|t|c|c|a|a|c|c|t|a|c|t|c|t|g|g|c|t|c|a|g|g|t|g|a|a|g|a|a|g|a|a|g|c|t|c|t|a|c|g|a|g|g|a|g|a|t|t|g|a|c|ei
c|c|t|a|c|a|a|g|g|t|g|t|c|c|a|c|c|t|c|t|g|g|c|c|c|g|g|g|c|c|t|t|c|a|g|c|a|g|c|c|g|c|t|c|c|t|a|c|a|c|g|a|g|t|g|g|g|c|ei
g|t|c|c|g|g|g|c|t|g|g|c|g|g|a|g|g|c|a|t|t|g|g|g|c|g|a|g|a|t|c|g|a|g|g|a|c|c|c|c|g|c|g|g|g|t|g|a|c|g|a|a|t|a|c|g|a|g|ei
a|g|g|g|a|g|g|t|g|t|c|t|g|a|t|t|g|g|t|c|c|a|g|t|a|g|t|c|c|a|t|g|t|c|c|c|t|a|c|c|c|t|g|a|a|c|a|g|g|g|g|c|a|t|g|g|g|g|ei
g|t|a|t|t|t|t|g|a|c|c|c|t|a|c|c|t|c|g|t|t|t|c|t|g|t|a|g|g|t|c|t|c|a|g|c|c|t|t|g|g|a|t|c|a|g|g|a|g|a|t|t|a|t|t|g|a|a|ei
c|t|t|c|t|a|t|a|a|t|a|t|t|a|t|g|g|g|g|t|g|g|a|g|t|g|g|t|g|g|t|a|t|g|g|a|g|c|a|a|g|g|g|g|t|a|g|g|t|g|g|g|a|a|g|a|c|g|ei
t|t|g|a|c|a|g|c|a|a|a|g|g|c|t|c|t|c|g|g|c|t|c|t|g|a|g|t|c|c|t|c|a|c|t|g|t|c|c|a|g|c|t|c|a|g|a|g|g|g|a|g|a|g|g|a|g|c|ei
c|t|c|g|c|t|c|t|g|t|g|a|g|g|c|c|a|c|g|g|t|c|t|c|c|g|c|c|a|g|g|t|t|g|a|c|t|c|g|a|g|c|c|t|c|c|t|g|c|c|a|g|a|g|c|c|a|c|ei
a|c|c|a|g|c|g|c|c|a|a|a|t|g|t|t|c|a|t|c|c|t|c|t|g|c|c|t|c|c|t|g|t|t|c|t|g|c|c|c|a|c|g|a|t|c|c|c|c|t|c|c|c|c|c|a|a|g|ei
t|t|t|t|c|t|t|t|c|a|t|t|t|t|g|t|c|t|t|t|c|a|c|t|a|c|a|g|c|t|c|c|t|g|g|g|a|a|a|c|g|t|g|a|t|g|g|t|g|a|t|t|a|t|t|c|t|g|ei
g|g|g|g|a|c|c|a|t|g|g|g|g|a|g|g|g|c|a|c|a|g|t|g|g|a|g|g|g|g|a|g|a|g|t|g|a|g|g|a|a|g|g|g|a|c|a|g|t|g|a|g|g|a|g|g|g|g|ei
g|c|c|c|a|g|a|a|g|a|t|a|a|c|t|c|a|a|a|c|c|c|a|c|a|g|g|a|a|t|g|t|t|c|g|t|g|c|a|g|g|a|a|a|a|g|g|a|g|g|c|t|g|t|g|a|c|t|ei
t|t|c|t|c|a|g|g|a|t|t|t|g|t|g|g|c|a|c|c|t|t|c|g|c|t|g|t|c|a|a|a|c|t|g|t|t|c|t|t|g|t|c|a|a|t|c|t|c|a|c|a|g|g|c|t|c|c|ei
a|t|t|c|a|c|t|g|a|a|a|a|g|a|g|g|t|a|c|a|a|a|t|t|t|t|g|t|c|a|a|g|t|a|c|a|a|g|a|c|a|g|c|t|t|t|c|t|a|c|t|c|c|t|t|c|t|a|ei
g|a|t|t|c|t|c|t|t|c|a|g|c|c|a|a|t|c|t|t|c|a|t|g|t|c|a|a|g|t|a|t|g|a|c|t|t|t|a|a|t|c|t|t|c|c|t|t|a|c|a|a|c|t|a|g|g|t|ei
g|g|c|t|g|c|c|g|g|a|g|c|c|c|c|t|c|a|t|g|c|t|g|g|t|g|g|a|g|t|a|a|g|g|a|g|g|g|a|g|a|t|g|g|a|g|g|c|a|t|c|a|t|g|t|c|t|g|ei
c|t|g|c|t|g|a|a|t|a|a|a|a|t|a|c|t|t|g|a|a|a|a|t|c|a|a|g|g|t|a|g|g|t|g|a|t|a|g|a|g|c|a|g|a|a|g|a|g|a|a|t|a|t|g|a|g|t|ei
t|g|t|g|a|a|c|a|t|g|c|g|c|t|g|t|g|t|g|c|t|g|c|t|c|t|t|t|g|g|a|a|a|c|t|n|g|c|c|t|g|g|g|t|c|c|a|g|g|c|c|t|a|g|g|g|t|g|ei
t|t|t|a|c|a|c|c|t|g|c|c|a|a|g|t|g|g|a|g|c|a|c|c|a|g|c|g|t|g|a|c|g|a|g|c|c|c|t|c|t|c|a|c|a|g|t|g|g|a|a|t|g|g|a|g|a|g|ei
g|t|t|t|c|t|a|a|t|t|g|c|t|a|t|t|g|t|c|c|t|a|t|t|a|t|a|g|a|c|t|c|c|t|g|g|t|t|g|t|c|t|a|c|c|c|a|t|g|g|a|c|c|c|a|g|a|g|ei
c|t|c|a|a|a|t|a|c|a|a|a|g|c|t|g|a|g|t|g|g|a|g|g|a|g|t|t|g|g|t|g|a|a|g|a|a|g|t|a|t|g|g|c|a|t|t|c|c|a|a|g|t|g|g|t|a|t|ei
a|g|c|c|g|g|g|c|a|g|a|g|a|c|a|c|a|a|c|a|a|a|a|a|a|g|a|a|t|t|t|t|a|g|a|c|c|a|a|t|a|t|c|c|t|t|g|a|t|g|a|a|c|a|t|t|g|a|ei
g|c|g|g|g|g|a|g|g|c|t|a|t|t|c|t|g|c|c|c|a|t|t|g|g|g|a|c|a|c|t|t|c|c|c|c|g|c|c|g|c|t|g|c|c|a|g|g|a|c|c|c|g|c|t|t|c|t|ei
t|g|a|g|g|t|t|a|a|a|g|g|t|n|g|a|a|a|a|g|g|a|a|t|t|c|t|t|c|g|t|a|t|a|a|a|a|a|c|t|a|g|a|c|a|g|a|a|t|g|a|t|t|c|t|c|a|g|ei
a|g|c|c|t|g|g|t|g|g|a|c|c|t|a|g|t|c|c|c|c|t|g|t|g|a|a|g|g|t|g|a|g|a|t|g|c|t|g|c|c|a|g|c|c|c|t|g|c|c|t|t|c|a|g|g|t|t|ei
c|c|g|c|a|g|a|a|c|t|c|c|t|c|t|g|t|g|c|c|c|t|c|c|t|c|a|c|c|a|g|a|c|c|t|t|g|t|t|c|c|t|c|c|c|a|g|t|t|g|c|t|c|c|c|a|c|a|ei
c|a|a|c|a|t|a|c|a|g|g|g|t|t|c|a|t|g|g|t|g|g|c|a|a|a|g|a|t|a|g|c|a|a|g|a|t|t|t|a|a|a|t|t|a|t|g|g|c|c|a|g|t|g|a|c|t|a|ei
a|t|g|g|g|c|t|a|t|t|a|a|g|t|g|c|a|g|a|g|g|c|a|a|a|a|g|t|c|c|c|c|a|a|c|a|g|g|t|g|a|g|g|a|a|a|c|a|a|t|g|g|c|a|t|a|g|a|ei
t|t|g|g|c|t|g|g|t|g|a|a|a|g|g|c|c|g|a|g|g|a|a|g|g|a|g|a|g|t|a|a|g|t|c|t|g|t|a|c|a|t|t|c|t|t|a|t|t|t|g|a|c|a|t|t|t|t|ei
c|c|c|c|a|c|c|c|c|t|c|a|c|t|c|t|g|c|t|t|c|t|c|c|g|c|a|g|g|a|t|g|t|t|c|c|t|g|t|c|c|t|t|c|c|c|c|a|c|c|a|c|c|a|a|g|a|c|ie
g|g|t|g|t|t|g|c|t|c|t|t|a|g|g|a|t|g|t|a|t|c|c|c|c|a|a|a|c|c|t|a|c|c|t|g|g|t|g|g|t|t|c|t|g|t|g|c|c|t|t|c|c|c|c|t|a|c|ei
t|c|t|c|a|g|c|t|a|a|t|t|t|t|t|a|a|t|t|t|a|t|t|t|t|t|a|g|a|g|a|t|a|c|g|g|t|c|c|c|a|c|t|c|t|g|t|t|t|c|c|c|a|g|g|c|t|g|ei
a|a|g|a|a|g|g|c|c|a|g|t|t|g|t|a|t|g|g|a|c|c|g|g|g|g|t|g|g|t|g|g|t|g|g|g|g|g|t|g|g|t|g|g|c|g|g|c|g|g|c|g|g|c|g|g|c|g|ei
a|g|g|g|c|a|c|t|g|t|g|g|t|a|g|g|c|a|c|c|t|a|t|g|c|c|c|a|g|c|t|a|c|t|t|g|g|g|a|g|g|c|t|g|a|g|g|c|a|a|g|a|g|a|a|t|t|g|ei
a|g|g|c|a|a|c|c|a|g|c|t|a|g|g|a|g|g|a|g|g|a|g|c|c|g|g|a|c|c|c|a|g|c|t|t|g|c|a|g|c|t|g|a|a|g|g|g|c|g|c|t|g|g|c|t|g|c|ei
c|g|c|g|g|g|g|a|g|c|c|c|c|g|c|t|t|c|a|t|c|a|c|g|g|g|g|c|t|a|c|g|t|g|g|a|c|g|a|c|a|c|g|c|t|g|t|t|c|g|t|g|a|g|g|t|t|c|ei
t|t|c|t|t|t|c|a|a|t|t|c|c|a|t|c|t|c|t|t|a|g|t|t|c|c|a|t|g|t|a|a|g|t|a|t|t|c|a|g|t|t|t|a|c|a|t|t|t|a|t|g|t|t|g|c|a|g|ei
t|g|g|g|g|a|t|c|a|t|c|t|a|t|g|c|t|g|g|t|g|a|c|c|g|a|g|a|c|c|a|g|a|t|a|c|a|c|c|c|c|g|t|c|c|t|t|c|c|g|a|g|g|c|c|a|g|g|ei
c|a|c|c|a|c|c|c|a|a|c|c|c|a|c|c|a|t|c|c|a|a|c|c|c|c|c|a|a|c|c|a|a|c|t|a|c|c|c|a|g|c|t|c|c|c|a|a|c|a|g|a|t|t|c|t|c|c|ei
c|c|c|c|a|a|a|g|t|a|a|c|t|c|a|c|c|c|t|c|c|c|t|c|c|c|a|g|g|a|t|g|a|c|c|a|c|a|a|g|c|t|g|t|c|c|t|t|g|g|a|t|g|a|g|c|t|g|ei
t|a|t|c|t|a|g|g|a|g|g|g|t|c|a|c|a|g|a|g|a|c|a|g|c|c|c|a|g|c|a|c|c|g|g|c|c|c|a|g|t|g|a|c|c|t|g|g|t|g|c|a|g|g|a|c|t|c|ei
a|g|g|a|g|g|g|a|g|c|t|a|c|t|c|t|c|a|g|g|c|t|g|a|g|t|a|a|g|t|a|t|g|a|a|g|g|a|g|g|c|t|g|a|t|c|c|c|t|g|a|g|a|t|c|c|t|t|ei
t|t|t|t|c|g|t|t|a|a|c|a|a|a|a|c|c|t|t|t|g|t|g|a|t|c|a|g|g|t|g|g|a|g|a|g|a|c|t|t|a|t|c|c|a|a|g|a|a|c|g|t|g|g|c|t|g|g|ei
g|a|g|a|c|g|c|t|g|c|a|g|c|g|c|a|c|g|g|a|c|c|c|c|c|a|a|g|a|c|a|c|a|t|a|t|g|a|c|c|c|a|c|c|a|c|c|c|c|a|t|c|t|c|t|g|a|c|ei
a|a|c|a|a|c|a|a|g|a|a|a|c|c|t|c|c|t|a|t|g|c|a|a|g|g|g|c|c|t|t|a|a|a|t|a|c|g|g|c|t|g|g|t|g|g|a|g|t|g|g|g|a|a|c|a|c|g|ei
t|g|c|c|c|t|g|a|a|g|t|g|c|a|c|t|c|a|c|c|c|t|c|t|c|c|a|g|g|g|a|g|c|c|c|c|g|a|t|t|a|c|c|a|g|c|a|g|c|a|g|g|c|g|g|c|g|g|ei
g|g|t|g|g|g|c|c|a|a|g|c|a|a|g|g|c|t|g|t|g|c|a|a|t|t|t|g|t|c|t|g|c|t|c|c|t|c|g|g|c|g|g|g|c|a|a|c|g|c|a|g|g|c|a|t|g|g|ei
t|g|t|t|t|c|a|g|t|t|t|g|a|g|a|a|t|t|c|t|t|t|t|t|c|t|a|g|g|a|a|a|c|a|g|t|g|a|c|t|g|c|t|a|c|t|t|t|g|g|g|a|a|t|g|g|g|t|ei
t|g|g|c|c|t|g|a|c|a|c|t|t|c|a|c|c|t|c|c|t|t|t|t|g|c|a|g|a|g|a|t|g|a|a|t|g|t|g|a|a|g|g|t|g|c|t|g|g|a|c|t|t|t|g|a|g|c|ei
t|c|g|a|t|g|a|c|a|c|c|c|c|t|c|t|t|g|g|a|t|c|c|c|t|a|c|a|g|g|c|c|t|g|c|c|t|g|g|a|g|a|a|c|a|g|c|t|c|a|c|a|g|c|a|c|a|g|ei
t|c|c|g|g|c|a|a|g|a|a|c|c|c|a|c|t|a|g|c|a|a|g|t|t|g|g|t|t|t|c|c|c|t|c|a|a|g|g|a|g|g|g|g|g|c|a|c|c|c|c|a|a|g|c|g|g|g|ei
t|c|c|g|c|t|g|a|c|g|c|t|g|c|t|t|t|g|g|c|t|g|t|t|c|c|a|g|a|t|g|t|g|g|t|g|g|t|g|c|t|g|a|a|c|t|c|c|a|a|g|a|g|g|a|c|c|a|ie
t|c|g|t|c|c|c|t|t|c|c|c|t|c|c|c|c|g|a|c|a|g|g|c|c|a|t|a|a|c|a|g|c|t|g|c|a|t|c|a|t|t|g|a|c|c|g|c|a|c|a|g|c|g|c|c|a|t|ei
t|t|c|c|c|c|g|c|c|g|c|c|a|c|g|a|t|g|c|c|c|a|a|a|g|a|a|g|g|t|g|a|g|c|g|g|c|g|g|c|c|g|c|g|g|c|c|c|g|c|a|c|a|c|g|c|c|c|ei
g|c|a|t|t|t|t|g|g|a|t|t|g|t|t|t|c|t|t|t|c|t|t|t|t|t|t|t|g|g|t|t|t|t|t|g|t|t|t|t|t|g|c|t|t|t|t|g|t|t|t|t|t|g|t|t|t|t|ei
a|a|t|c|c|t|t|t|c|t|t|t|c|a|g|c|t|g|g|a|g|t|g|c|t|c|a|g|g|a|g|c|c|a|g|c|c|c|c|a|c|c|c|t|t|a|g|a|a|a|a|g|a|t|g|t|t|t|ei
c|t|g|g|c|c|t|g|a|g|g|a|c|c|c|g|g|c|g|c|t|g|a|t|g|c|g|g|g|g|c|c|c|c|t|g|c|t|c|c|g|a|g|g|g|g|c|t|c|a|t|g|t|t|c|a|g|g|ei
t|t|t|g|c|c|c|c|t|g|g|c|a|a|a|t|g|c|a|c|a|c|a|c|c|a|t|g|c|t|a|g|c|c|t|c|a|c|g|a|a|a|c|t|g|g|a|a|t|a|a|g|c|c|t|t|c|g|ei
c|c|a|g|a|c|c|a|t|t|g|g|c|t|t|g|a|g|t|g|c|a|g|c|c|c|c|g|c|t|t|t|a|a|c|c|a|g|t|g|c|a|a|c|a|c|g|a|c|a|c|g|c|g|g|c|a|a|ei
c|a|t|c|g|a|c|c|a|t|c|t|c|c|a|g|c|c|a|t|c|t|g|c|a|c|c|a|a|g|c|a|t|c|t|c|a|a|g|g|a|a|g|g|a|g|g|c|c|t|c|c|t|g|a|c|c|t|ei
c|c|g|t|c|t|t|c|c|c|a|g|c|c|c|a|c|c|a|t|c|c|c|a|c|g|t|g|g|g|c|a|t|c|a|a|t|g|c|t|g|g|c|c|t|g|g|t|t|c|t|c|t|t|t|g|c|a|ei
c|c|g|g|a|a|a|a|c|c|a|g|g|a|c|c|c|a|g|a|g|g|c|a|c|c|c|g|g|a|a|a|a|g|a|t|g|g|t|g|a|c|a|a|a|g|g|g|g|a|a|a|a|a|g|g|g|a|ei
g|c|c|g|c|c|c|t|c|c|c|a|t|t|g|a|t|t|g|g|c|c|a|g|g|g|g|a|a|g|g|a|a|g|t|c|g|c|c|t|g|g|g|t|g|c|c|c|c|t|t|g|g|c|c|c|t|t|ei
t|t|c|a|g|g|a|t|g|t|g|t|t|c|t|g|g|g|c|c|a|a|g|a|a|c|a|g|g|t|g|a|g|c|a|c|c|g|g|g|a|a|g|g|a|t|t|t|g|c|c|c|c|a|g|g|a|a|ei
a|g|c|c|c|c|a|c|g|g|g|c|g|c|c|a|c|g|g|a|a|c|c|g|t|c|g|a|t|c|t|c|g|c|c|g|c|c|a|a|c|t|g|g|t|a|g|a|c|a|t|g|g|a|g|a|c|c|ei
g|c|t|a|g|t|a|t|t|t|t|t|t|t|t|t|t|t|t|t|t|t|g|a|t|t|t|t|t|a|t|a|g|a|g|a|c|a|g|g|g|t|c|t|t|g|c|c|a|t|g|t|t|g|c|c|c|a|ei
a|a|a|t|a|t|a|a|a|t|c|g|g|a|g|g|g|g|a|a|g|t|g|t|c|t|c|t|g|t|t|t|t|g|g|g|a|t|t|t|t|g|t|a|a|a|t|c|t|t|c|t|c|a|g|g|t|t|ei
g|c|t|g|t|c|a|a|a|g|t|g|c|t|c|t|t|g|t|c|a|a|t|t|a|c|a|g|g|c|t|c|c|t|g|g|t|t|g|t|c|t|a|c|c|c|a|t|g|g|a|c|c|c|a|g|a|g|ei
a|t|g|g|c|c|t|t|g|g|g|g|a|c|a|a|g|t|c|g|t|g|c|t|g|a|g|g|c|c|t|c|t|a|g|g|g|a|g|g|g|a|a|g|g|a|a|g|a|a|g|t|g|g|c|a|t|g|ei
a|c|g|t|g|c|t|g|c|a|g|a|t|c|c|g|a|a|t|t|g|g|c|c|a|c|a|c|c|c|g|t|g|g|t|g|g|t|g|c|t|g|a|g|c|g|g|c|c|t|g|g|a|c|a|c|c|a|ei
t|t|t|a|t|t|a|c|t|t|a|t|t|t|g|g|g|g|t|t|g|c|a|c|g|a|a|a|t|g|t|c|t|g|g|a|g|a|a|t|a|a|t|t|c|t|t|t|g|a|t|t|a|t|g|a|c|t|ei
a|a|a|a|a|a|g|a|a|a|a|c|a|a|t|g|a|a|c|a|a|a|t|a|a|g|g|t|g|a|a|c|c|a|t|g|a|a|a|t|g|g|c|a|t|a|t|t|t|g|c|a|a|a|c|c|a|a|ei
a|t|c|t|t|c|g|c|c|t|t|t|g|c|c|a|c|a|t|g|c|g|g|a|c|t|a|c|a|g|t|g|g|g|g|a|g|c|t|c|c|a|g|c|t|g|a|g|c|g|t|g|g|a|t|t|g|t|ei
c|t|g|c|t|c|a|c|t|g|a|a|t|c|c|a|t|t|t|t|c|t|c|t|c|c|a|g|g|a|c|t|t|c|g|g|c|a|g|t|c|t|g|t|c|c|a|a|c|c|t|t|c|a|g|g|t|c|ei
g|g|g|a|c|c|g|g|g|c|t|g|a|c|c|g|c|g|g|g|g|g|c|g|c|c|a|g|g|t|t|c|t|c|a|c|a|c|c|a|t|g|c|a|g|g|t|g|a|t|g|t|a|t|g|g|c|t|ei
g|t|t|c|t|g|c|c|c|a|g|g|a|a|t|g|a|t|g|a|t|t|g|g|c|t|a|t|t|g|t|t|a|t|a|t|t|t|t|a|a|t|a|c|t|t|g|g|g|t|a|a|a|t|a|g|g|a|ei
t|a|a|a|t|a|t|t|c|t|t|t|c|t|t|t|t|c|a|a|c|c|t|t|a|t|a|g|g|g|c|t|t|t|t|t|g|g|t|g|g|t|g|c|t|g|g|a|g|t|t|g|g|c|a|a|g|a|ei
t|g|g|g|t|t|c|c|a|a|a|t|t|a|a|t|a|g|t|t|g|t|a|g|a|t|g|a|g|t|c|t|g|c|c|a|g|t|c|a|a|t|a|a|a|t|a|c|a|t|g|g|a|t|a|t|a|a|ei
a|g|a|t|t|t|t|g|g|g|a|a|a|a|a|g|t|a|a|t|c|t|g|t|a|t|g|t|g|c|a|c|a|a|a|a|t|g|g|a|t|t|c|a|a|g|t|t|t|g|c|a|g|a|t|a|a|a|ei
c|a|c|c|t|g|g|t|g|t|c|t|g|c|t|a|c|c|a|t|g|a|g|g|g|g|t|c|a|c|c|a|c|c|t|g|c|c|t|g|c|g|c|t|t|c|c|c|a|g|g|c|c|a|g|c|t|c|ei
t|a|g|a|t|a|c|t|a|t|c|c|t|c|t|c|t|t|c|t|a|c|c|t|a|c|a|g|a|t|t|t|g|c|t|c|c|c|a|t|t|c|a|t|g|c|t|g|a|g|g|c|t|c|c|a|g|a|ei
t|a|a|a|g|g|t|t|c|t|t|a|t|c|t|c|t|c|t|a|t|c|t|c|t|t|a|g|g|a|a|g|a|t|c|c|a|g|c|t|t|c|c|a|a|g|t|g|c|c|a|c|t|g|c|a|g|t|ei
t|g|g|g|c|g|g|g|a|c|t|g|a|c|t|a|a|g|g|g|g|c|g|g|c|c|a|g|g|g|t|c|t|c|a|c|a|c|c|c|t|g|c|a|g|t|g|g|a|t|g|c|a|t|g|g|c|t|ei
g|g|g|c|g|g|g|t|c|t|c|a|g|c|c|c|c|t|c|c|t|c|g|c|c|c|a|g|g|c|t|c|c|c|a|c|t|c|c|a|t|g|a|g|g|t|a|t|t|t|c|c|a|c|a|c|c|t|ei
g|g|t|c|c|t|c|a|c|a|g|c|t|g|c|c|c|a|c|t|g|c|a|c|g|g|a|a|g|t|g|a|g|t|a|g|g|g|g|c|c|t|g|g|g|g|t|c|t|g|g|g|g|a|g|c|a|g|ei
a|t|g|c|t|t|c|a|a|a|g|g|c|t|t|c|t|a|g|g|c|c|c|t|c|c|g|g|g|a|a|g|t|g|t|t|a|a|t|g|a|g|c|t|g|t|g|g|a|c|t|g|g|t|t|c|a|c|ei
g|c|g|g|t|t|g|a|t|t|g|a|c|a|g|t|t|t|c|t|c|c|t|c|c|c|a|g|a|c|t|g|g|c|c|a|a|t|c|a|c|a|g|g|c|a|g|g|a|a|g|a|t|g|a|a|g|g|ie
g|g|g|a|g|a|a|a|a|c|g|t|t|a|g|g|g|t|g|t|g|g|a|a|t|a|c|g|g|a|a|a|g|c|c|t|t|c|c|t|a|a|a|a|a|a|t|g|a|c|a|t|t|t|a|a|c|t|ei
a|c|t|g|t|c|a|a|a|c|t|g|t|t|c|t|t|g|t|c|a|a|t|t|a|c|a|g|g|c|t|c|c|t|g|g|t|t|g|t|c|t|a|c|c|c|a|t|g|g|a|c|c|c|a|g|a|g|ei
g|a|a|a|g|c|t|c|a|t|c|c|t|g|c|g|g|c|g|g|t|a|t|c|g|g|t|g|g|t|a|a|g|c|c|c|c|t|c|c|a|c|a|t|t|c|c|c|c|c|c|a|g|c|a|a|a|g|ei
c|g|c|t|g|t|g|t|c|t|c|t|g|a|a|g|g|t|g|g|t|g|g|t|g|a|g|g|g|t|c|c|t|t|c|g|a|a|t|t|c|c|c|t|g|t|g|g|g|a|g|a|t|g|c|g|g|t|ei
a|g|g|g|c|c|g|c|g|c|c|g|g|a|c|c|t|c|g|a|c|g|t|c|c|a|a|g|g|t|g|a|g|t|c|c|c|c|a|g|c|c|c|t|g|g|t|c|c|c|g|c|g|g|c|g|c|t|ei
g|g|t|a|a|t|t|t|t|a|t|t|t|t|g|a|a|a|c|a|g|a|a|a|a|g|g|a|a|a|a|t|g|c|a|t|g|c|t|t|t|a|a|t|a|a|t|g|t|c|a|g|t|t|t|c|c|a|ei
t|t|t|c|c|a|c|t|c|c|t|c|c|t|t|g|t|c|t|t|c|t|c|c|g|c|a|g|t|g|c|c|c|t|g|g|g|a|g|c|t|g|t|c|a|t|t|g|c|c|c|t|c|c|t|g|c|t|ei
a|t|a|t|g|a|g|g|a|a|g|a|a|a|t|c|a|a|g|a|t|t|c|t|c|t|g|a|t|a|a|a|c|t|c|a|a|g|g|a|g|g|c|a|g|a|g|a|c|c|c|g|t|g|c|t|g|a|ei
a|g|g|t|a|t|t|t|a|g|t|a|t|g|c|t|g|t|a|a|a|t|a|t|t|t|a|g|g|t|a|t|t|g|g|t|a|c|t|g|t|t|c|c|t|g|t|t|g|g|c|c|g|a|g|t|g|g|ei
a|t|t|c|c|t|t|t|c|a|a|c|t|c|t|a|c|c|a|a|c|a|a|t|c|c|a|g|g|t|c|t|g|c|t|t|g|g|g|t|t|g|c|c|a|g|g|a|c|a|g|a|g|g|a|a|g|a|ei
a|a|t|c|a|t|g|c|c|g|t|g|g|t|g|t|c|t|c|g|g|a|t|g|t|a|a|g|g|t|g|g|a|a|c|g|c|c|t|g|a|a|a|c|a|g|g|t|g|c|t|g|c|t|c|c|a|c|ei
g|a|g|t|g|t|c|a|t|g|a|t|t|t|t|c|a|t|g|g|a|g|g|a|t|t|a|a|t|a|t|t|c|a|t|c|c|t|c|t|a|a|g|t|a|t|a|c|t|c|a|g|a|c|t|a|g|g|ei
c|t|g|a|c|a|g|a|a|t|g|a|a|c|c|t|g|c|a|g|a|c|c|t|c|g|c|g|g|c|t|a|c|t|a|c|a|a|c|c|a|g|a|g|c|g|a|g|g|c|c|a|g|t|g|a|g|t|ei
c|c|c|c|g|g|g|c|c|a|a|c|c|t|c|a|c|c|g|t|g|g|t|c|g|c|t|c|c|g|t|g|g|g|g|a|g|a|a|g|g|a|g|c|t|g|a|a|a|c|g|g|g|a|g|c|c|a|ei
t|a|a|c|t|c|t|t|t|c|c|a|c|c|a|a|t|t|t|c|a|a|a|a|t|g|c|g|g|c|t|t|a|a|a|a|g|a|t|g|a|a|g|g|a|g|a|g|c|t|a|a|a|c|a|a|a|c|ei
t|a|a|g|a|c|c|c|a|a|a|t|a|a|t|a|a|g|c|c|t|g|c|c|c|t|t|c|t|c|t|c|t|a|a|c|t|t|t|g|a|t|t|t|c|t|c|c|t|a|t|t|t|t|t|a|c|t|ei
g|g|c|a|t|c|g|t|t|g|a|g|a|a|t|g|a|a|t|g|g|a|a|a|a|a|c|g|t|g|c|t|c|c|a|g|a|c|c|c|a|a|a|t|c|t|a|a|c|a|t|a|g|t|t|c|t|c|ei
c|a|g|a|c|a|a|a|c|c|t|c|t|c|t|c|c|a|g|a|a|c|t|a|c|c|a|t|a|t|g|a|c|t|c|t|c|t|c|t|c|c|a|g|a|a|c|t|c|a|g|t|c|a|g|a|c|a|ei
a|a|t|t|a|a|a|a|g|t|t|a|a|a|t|a|a|c|t|t|a|t|c|t|a|c|a|g|g|t|g|a|c|c|t|g|g|t|a|c|t|g|c|t|t|c|a|t|g|t|a|t|g|t|c|c|c|c|ei
c|t|t|c|t|c|t|c|c|g|g|t|c|t|g|t|c|t|c|c|g|g|t|t|a|c|a|g|g|a|a|a|a|g|c|a|c|a|g|t|g|c|a|g|a|g|c|g|c|t|t|g|t|a|c|a|c|a|ei
c|a|g|c|t|c|a|g|t|c|c|t|t|c|c|a|c|t|c|t|c|t|a|t|a|c|a|g|g|g|g|g|a|c|t|c|t|g|g|a|g|g|c|c|c|t|c|t|t|g|t|g|t|g|t|a|a|c|ei
g|a|a|a|g|t|g|c|c|g|a|g|a|t|c|c|t|g|c|a|g|g|c|g|g|c|c|g|t|c|c|g|g|t|g|a|g|g|g|g|g|a|t|g|c|a|t|t|t|g|a|g|c|t|g|a|c|t|ei
a|t|t|c|t|c|c|t|g|g|t|g|g|c|c|c|t|g|c|a|g|g|c|c|g|g|c|t|g|a|g|c|c|a|c|t|c|c|a|g|g|c|a|a|g|a|g|c|t|g|a|t|g|a|g|g|t|t|ei
a|g|g|g|t|t|c|c|t|t|t|t|t|c|c|c|a|g|g|a|a|c|c|t|c|c|a|a|t|a|a|t|a|c|a|a|c|g|g|c|t|c|c|t|t|c|c|t|t|t|c|t|t|t|c|c|c|t|ei
t|g|a|g|c|a|a|t|c|t|g|c|t|t|c|t|t|t|c|a|g|a|g|g|g|t|g|t|g|c|g|t|t|c|t|c|t|c|a|g|c|t|t|t|c|t|t|g|a|a|t|t|t|a|t|t|t|c|ei
c|g|g|g|g|a|g|c|c|c|c|g|c|t|t|c|a|t|c|t|c|t|g|g|g|c|t|a|c|g|t|g|g|a|c|g|a|c|a|c|c|c|a|g|t|t|c|g|t|g|c|g|c|t|t|c|g|a|ei
t|a|c|a|g|c|c|a|c|c|a|t|g|a|g|a|a|g|g|a|c|a|c|c|c|t|g|c|c|t|g|g|g|t|g|c|g|a|c|t|g|c|a|c|a|g|c|a|g|t|t|c|c|a|c|a|g|g|ei
c|c|t|c|t|c|c|g|g|c|a|g|a|a|g|g|g|a|a|c|t|g|c|t|g|g|c|t|c|c|c|t|t|g|t|g|c|g|t|g|g|g|t|g|a|a|g|c|c|g|c|t|g|c|t|g|g|g|ei
g|a|a|a|a|a|g|g|a|g|g|c|a|a|t|a|t|g|a|a|a|c|g|g|a|t|t|t|g|a|g|c|g|a|t|t|c|t|g|t|c|g|t|g|g|a|c|t|a|a|a|a|g|a|a|g|t|a|ei
t|a|t|g|t|c|t|c|c|a|g|a|t|g|a|t|t|g|a|g|c|a|a|t|g|g|c|t|c|c|c|a|g|c|t|c|a|a|g|g|g|t|c|c|c|g|g|g|t|t|t|g|a|g|t|c|c|a|ei
t|t|c|g|c|c|a|a|c|a|g|c|c|t|g|g|t|g|t|a|t|g|g|g|c|t|c|g|g|a|c|a|g|c|a|a|c|g|t|c|t|a|t|c|g|c|c|a|c|c|t|g|a|a|g|g|a|c|ei
g|g|t|g|c|c|t|c|a|g|c|g|t|t|c|g|g|g|c|t|g|g|a|a|g|a|g|g|g|t|g|a|g|t|t|t|t|t|c|c|c|c|c|t|c|t|g|c|c|a|c|c|c|t|c|a|g|c|ei
c|t|c|c|a|t|c|a|c|a|c|c|a|g|t|a|a|g|g|a|g|a|a|c|a|t|a|t|a|a|g|t|g|t|g|a|t|t|g|c|a|a|g|a|a|t|g|g|t|a|g|a|g|g|a|c|c|g|ei
g|g|c|g|c|c|c|g|t|g|c|t|c|a|c|a|c|g|t|c|c|t|c|c|g|c|a|g|a|g|a|g|c|t|g|c|g|t|g|a|c|c|g|a|g|c|c|c|g|a|g|t|g|c|c|g|c|g|ei
a|c|a|t|g|c|c|g|t|g|g|a|a|g|c|c|g|g|g|g|c|c|t|a|a|g|a|g|g|t|g|a|g|c|a|g|g|g|a|c|t|g|c|c|a|c|t|g|g|t|t|t|t|g|t|c|c|t|ei
c|c|a|c|g|g|c|t|g|g|a|t|g|a|t|g|g|g|a|g|a|t|g|c|c|c|a|g|g|t|a|a|g|c|t|a|g|c|t|c|t|g|g|t|c|c|t|c|a|g|g|g|g|a|g|g|g|a|ei
a|c|c|c|a|c|t|t|t|t|c|c|t|c|t|t|c|c|a|c|t|c|t|g|g|c|a|g|c|a|t|c|g|g|t|g|a|g|t|t|t|g|c|t|g|t|g|g|a|c|a|a|g|g|g|c|a|c|ei
g|c|g|g|g|c|c|c|t|g|c|c|g|g|a|c|t|t|t|a|g|t|g|t|t|a|g|g|g|g|t|t|a|a|t|t|t|c|g|g|g|c|t|g|a|c|a|g|g|g|a|c|g|g|a|g|c|c|ei
a|a|a|g|c|a|g|g|a|a|a|c|c|t|g|t|g|g|t|a|t|g|a|g|c|a|g|a|c|c|c|c|c|g|a|g|t|g|a|a|g|a|c|t|a|c|t|a|c|t|a|c|t|a|c|t|a|c|ei
t|c|t|g|g|g|c|t|c|c|a|g|g|c|a|g|a|a|g|c|a|c|a|c|t|c|c|c|c|g|a|c|c|t|g|c|c|c|t|a|c|g|a|c|t|a|c|g|g|c|g|c|c|c|t|g|g|a|ei
g|t|t|a|t|c|a|a|c|t|t|a|a|a|a|g|a|t|g|c|c|a|c|t|t|a|a|g|g|t|a|a|g|c|a|t|t|g|a|g|c|t|a|a|t|t|g|a|t|g|t|c|c|a|c|g|t|g|ei
a|t|a|t|c|a|c|a|c|g|g|g|c|c|t|t|t|g|a|a|g|g|g|a|g|c|a|c|a|c|g|g|t|g|c|a|g|a|t|a|g|a|t|c|t|g|g|a|a|a|g|g|a|c|g|g|c|g|ei
g|t|g|g|g|t|t|g|t|t|g|a|g|g|g|g|a|a|c|a|g|g|g|a|a|t|a|g|c|t|g|t|g|c|t|a|t|g|a|g|g|t|t|t|c|t|t|t|g|a|c|t|t|c|a|a|t|g|ei
c|c|t|t|a|t|g|a|c|c|c|c|g|g|c|c|a|c|c|t|t|c|c|g|c|c|a|g|g|c|g|g|g|g|t|c|g|c|t|a|a|g|g|c|c|t|c|a|g|g|a|g|g|a|g|a|a|a|ei
g|g|c|c|g|c|t|c|g|c|t|a|g|a|g|c|a|c|g|c|g|c|g|c|c|a|g|a|c|c|t|a|g|g|g|t|a|t|t|t|g|c|g|g|a|t|c|a|g|c|g|t|c|c|t|c|g|c|ei
c|g|t|c|c|t|c|c|c|t|a|c|a|a|t|t|t|g|c|c|a|t|t|t|t|c|t|c|c|t|g|g|g|t|t|a|g|g|c|c|c|c|g|g|c|t|t|c|a|c|t|g|g|t|t|g|a|g|ei
c|c|t|g|a|a|c|a|g|g|c|t|c|t|g|c|t|t|c|c|c|a|t|c|t|c|a|g|g|t|t|c|a|a|c|a|t|c|g|g|t|g|g|c|c|c|c|a|c|a|t|c|c|t|c|c|a|t|ei
g|g|a|t|g|c|t|c|a|g|g|c|c|a|t|g|c|c|c|c|g|g|c|g|t|g|g|a|a|c|c|t|c|c|t|g|t|t|t|t|g|a|c|a|c|t|t|g|a|t|c|c|c|a|a|t|g|a|ei
g|c|g|a|c|c|t|c|t|a|c|c|t|c|a|a|t|g|a|c|t|a|c|g|c|a|c|c|g|c|g|g|c|t|t|g|c|g|g|c|t|g|c|c|c|a|c|c|a|g|c|a|a|c|a|a|c|g|ei
a|a|a|g|c|t|a|t|g|c|a|a|t|g|t|c|t|t|c|t|t|t|t|t|a|a|a|g|g|a|t|a|t|a|a|t|t|g|a|c|a|c|t|g|g|c|a|a|a|a|c|a|a|t|g|c|a|g|ei
t|t|t|t|t|t|a|t|c|a|c|a|g|t|a|a|t|t|t|t|a|a|a|t|t|g|t|a|a|a|a|a|t|t|a|a|a|a|c|c|a|g|t|g|a|c|t|c|c|t|g|t|t|t|a|a|a|a|ei
c|c|t|a|c|t|g|t|t|t|c|c|c|t|c|t|a|t|c|a|a|a|a|g|c|t|c|c|t|t|g|g|c|g|c|a|g|g|t|t|c|c|c|t|g|a|g|c|t|g|t|g|g|g|a|t|t|c|ei
a|a|g|g|a|t|t|t|g|c|t|g|g|g|a|a|g|t|g|c|t|g|t|a|a|t|a|g|g|t|g|a|g|t|a|g|g|t|g|a|g|a|g|c|a|c|g|t|g|a|a|a|c|g|a|g|c|t|ei
c|t|g|t|c|a|a|a|c|t|g|c|t|c|t|t|g|t|t|c|a|a|t|t|a|c|a|g|g|c|t|c|c|t|g|g|t|t|g|t|c|t|a|c|c|c|a|t|g|g|a|c|c|c|a|g|a|g|ie
g|t|c|t|t|c|t|g|c|t|c|c|t|c|t|t|c|g|t|c|t|g|g|c|c|t|t|a|c|t|t|c|c|a|a|g|a|c|c|c|c|a|g|a|g|a|g|g|a|a|g|g|c|a|t|g|c|t|ei
g|a|a|a|c|t|a|g|g|a|g|a|a|t|a|t|t|a|c|t|t|a|c|a|a|t|g|c|g|t|a|t|g|t|t|t|t|t|g|t|a|a|a|c|a|g|t|a|t|t|t|t|t|a|g|t|g|a|ei
a|g|a|a|g|g|g|g|a|a|g|g|a|g|a|c|g|c|t|g|c|t|t|a|c|t|g|g|g|t|a|a|g|a|g|g|g|t|c|c|a|c|a|g|g|g|c|t|a|c|t|c|t|c|c|c|a|t|ei
a|a|a|c|t|g|c|a|c|g|t|g|g|a|t|c|c|t|g|a|g|a|a|t|c|a|a|g|g|t|g|a|g|t|g|c|a|g|g|a|g|a|t|g|c|t|c|a|t|g|t|c|c|t|c|t|t|t|ei
a|g|a|g|a|c|t|g|g|g|a|t|g|g|g|a|a|c|a|c|t|g|g|g|g|c|a|g|c|t|g|a|g|g|a|c|a|c|a|c|c|c|c|a|c|a|c|c|c|c|a|g|c|c|c|a|c|c|ei
g|a|g|c|a|g|c|c|a|g|t|g|c|t|c|c|a|a|g|c|c|c|g|t|t|c|a|t|g|t|a|a|g|t|g|c|c|a|g|t|c|t|t|c|c|t|g|c|t|c|a|c|c|t|c|t|a|t|ei
g|c|g|t|g|a|c|t|g|a|g|g|g|c|c|g|c|g|t|g|g|a|c|t|c|t|g|g|g|t|g|a|g|c|c|t|c|c|t|g|g|a|a|g|c|a|t|a|t|g|g|g|c|t|c|c|t|a|ei
t|a|t|a|g|a|c|t|g|a|a|t|t|t|t|g|g|a|a|g|c|a|g|a|g|t|t|g|g|t|a|a|g|c|a|a|t|t|c|a|t|t|t|t|a|t|c|c|t|c|t|a|g|c|t|a|a|t|ei
t|c|a|t|a|g|t|c|c|t|t|t|g|g|t|a|g|c|c|t|t|c|c|g|a|a|g|c|t|g|g|t|g|g|t|a|g|a|c|t|t|t|t|a|g|t|a|g|g|t|g|c|t|c|a|a|t|a|ei
t|a|c|t|t|a|a|c|t|c|a|g|t|c|t|t|c|t|t|t|t|t|t|t|a|t|a|g|g|a|c|t|a|c|a|a|a|t|c|c|c|t|c|c|a|g|g|a|t|a|t|c|a|t|t|g|c|c|ei
t|t|g|a|g|g|a|g|a|a|g|a|t|c|a|c|a|c|a|c|a|g|t|c|c|t|g|a|c|c|a|t|c|t|g|c|t|t|c|c|c|t|g|a|g|t|a|c|a|c|a|g|g|g|g|c|c|a|ei
g|a|a|g|t|g|g|t|c|c|t|g|c|t|g|a|a|g|a|a|g|g|t|a|c|t|c|g|g|g|t|t|t|c|t|c|c|g|g|c|g|t|c|a|t|t|a|g|g|c|t|c|c|t|g|g|a|c|ei
g|c|a|g|t|a|a|a|a|g|c|a|c|a|t|c|a|g|g|t|g|a|a|a|t|c|a|c|a|t|g|t|g|g|a|t|t|t|t|t|g|t|a|a|a|t|g|c|c|t|t|a|a|t|t|g|a|a|ei
g|g|c|a|t|c|g|c|a|g|g|c|g|t|t|g|g|g|a|c|t|c|c|g|t|g|c|a|g|c|t|g|c|a|g|c|t|g|c|a|g|c|a|g|c|a|g|c|c|g|c|t|a|a|g|g|c|a|ei
c|t|a|g|a|g|g|a|a|g|g|c|a|t|c|c|a|a|a|c|g|c|t|a|g|t|g|g|g|t|g|a|g|g|g|t|g|g|c|a|c|c|a|g|g|g|a|t|c|c|c|a|a|t|c|c|t|g|ei
t|t|c|t|g|g|t|t|g|c|c|c|t|g|a|c|t|g|c|c|t|g|t|t|g|t|a|g|g|c|c|a|g|c|c|t|t|t|c|g|a|c|c|c|c|a|c|c|t|t|c|c|t|c|a|t|c|g|ei
g|g|g|a|a|g|a|a|a|t|g|a|a|a|a|c|a|a|g|a|t|g|g|c|a|t|t|a|a|g|t|g|c|a|g|a|g|a|c|a|a|a|a|a|c|t|c|c|c|c|a|a|c|a|g|g|t|g|ei
a|t|c|g|c|g|t|t|c|c|t|t|a|a|g|a|a|a|g|t|g|c|a|g|a|g|a|g|g|t|a|t|a|c|t|t|g|g|c|c|c|c|t|c|t|t|c|c|t|g|g|g|g|t|c|a|c|t|ei
a|c|c|t|c|g|g|g|c|c|t|g|c|g|g|c|a|t|g|t|g|c|a|c|g|g|c|c|t|t|c|t|t|c|c|c|t|c|c|c|g|g|c|a|c|c|g|t|g|c|a|t|c|c|g|c|t|g|ei
g|a|c|a|a|a|c|t|a|t|t|g|g|c|c|t|g|t|g|g|c|g|a|g|a|g|c|g|g|t|g|a|g|t|g|t|c|t|g|c|t|t|g|g|t|t|t|g|g|t|c|c|c|a|t|c|t|c|ei
g|g|a|g|g|g|g|g|t|c|c|t|g|c|a|g|g|g|c|g|g|g|g|g|t|g|g|g|a|a|g|g|t|g|g|g|g|a|g|a|g|g|c|t|g|c|c|g|a|g|a|g|c|c|a|c|c|c|ei
a|t|t|t|t|g|t|t|t|t|g|c|t|t|t|t|t|c|t|g|a|c|t|c|g|t|g|g|g|g|c|a|a|g|a|t|t|t|t|c|c|t|t|t|t|t|t|a|t|a|c|a|c|a|t|a|a|t|ei
g|c|c|t|c|c|t|g|c|c|a|c|c|c|c|t|t|c|c|t|c|c|c|a|a|c|t|c|c|a|c|t|c|t|g|a|t|t|c|a|c|c|t|c|t|t|c|c|t|c|t|g|g|t|t|c|c|t|ei
g|a|g|c|t|g|c|a|g|c|a|g|t|c|g|c|g|c|a|t|c|c|g|a|c|g|a|c|a|g|c|c|t|c|t|c|t|g|c|c|c|a|g|c|t|c|a|g|c|c|a|g|c|t|c|c|a|g|ei
t|c|t|a|c|a|c|a|g|a|t|g|t|c|t|t|a|g|a|g|t|t|t|a|g|a|t|g|g|t|a|a|g|a|g|g|c|c|t|c|c|a|g|t|c|t|c|c|t|a|c|c|c|c|c|a|g|g|ei
t|c|a|t|a|g|t|a|c|a|t|t|t|t|c|a|c|a|t|c|a|c|a|g|a|c|c|a|t|a|t|c|a|g|t|g|t|t|a|t|t|a|a|a|t|a|t|t|t|t|g|t|a|t|g|c|c|a|ei
c|t|c|a|g|t|g|g|a|g|c|c|a|t|g|a|a|t|a|c|t|a|g|t|c|t|g|c|a|g|t|c|t|g|a|t|g|a|a|g|a|t|a|g|c|a|a|a|t|g|a|t|a|t|t|c|g|a|ei
c|t|g|t|t|a|c|a|c|g|c|t|t|g|t|a|a|t|t|g|a|c|t|t|c|t|a|g|g|t|g|a|g|c|c|c|a|t|t|g|g|c|a|g|g|g|g|t|a|c|c|a|a|a|g|t|g|a|ei
a|t|g|c|t|g|a|c|c|a|c|t|t|c|c|c|t|c|t|t|c|t|c|g|g|c|a|g|t|g|t|g|a|c|t|t|c|a|c|c|g|a|a|g|a|c|c|a|g|a|c|c|g|c|a|g|g|t|ie
a|g|c|c|c|a|g|c|t|g|t|t|t|g|t|c|t|c|c|c|a|t|t|t|t|c|t|a|c|t|t|c|t|a|a|a|a|t|a|c|a|t|t|t|c|t|t|c|a|c|t|a|a|g|t|g|a|g|ei
t|c|g|g|a|c|t|t|c|t|g|t|g|t|g|g|a|g|g|c|t|g|c|a|a|t|g|t|g|t|g|g|a|g|c|a|g|g|a|g|g|a|g|a|c|t|t|t|t|c|t|c|c|c|a|a|t|t|ei
a|g|c|a|g|g|t|t|t|t|a|c|c|a|g|t|c|c|a|c|a|g|a|t|c|c|c|g|a|g|a|a|c|c|a|c|c|t|g|g|g|g|a|g|c|a|t|g|c|t|g|a|a|a|a|c|a|c|ei
a|c|t|c|c|c|t|t|a|c|a|a|a|t|g|a|a|t|g|g|c|a|t|g|a|g|a|g|g|a|t|t|c|t|g|a|t|g|a|g|c|c|t|t|t|a|g|a|g|a|g|a|a|g|g|c|t|g|ei
g|a|a|c|c|g|a|a|g|a|c|g|t|g|t|t|t|g|c|a|a|a|t|t|c|c|c|g|g|t|g|a|g|t|c|t|c|t|t|t|t|g|a|a|c|t|c|t|c|a|g|c|c|t|g|c|t|c|ei
g|t|g|a|t|c|a|a|g|c|t|g|t|t|t|t|t|t|c|t|c|t|c|t|c|c|a|g|a|a|t|t|t|a|a|g|g|g|a|c|g|c|t|g|t|g|a|a|g|c|a|a|t|c|a|t|g|g|ei
c|c|t|a|g|g|g|g|c|a|t|g|g|c|c|c|a|g|t|g|t|c|t|t|c|t|c|c|t|g|a|g|t|g|c|c|c|a|c|c|g|t|g|c|a|g|c|a|c|t|t|g|c|a|g|g|g|g|ei
g|g|t|t|c|a|a|g|g|t|a|a|t|g|t|t|a|c|a|g|a|t|c|c|g|a|t|t|t|a|t|t|c|t|t|g|t|a|a|a|t|t|c|a|a|a|g|g|t|a|t|g|t|c|t|t|t|t|ei
a|g|c|c|t|c|c|t|g|t|t|g|g|g|c|a|a|t|t|t|c|c|t|t|c|c|a|g|a|a|t|c|a|a|c|t|c|c|a|c|t|a|c|c|c|a|t|c|c|t|g|g|g|g|c|c|g|a|ei
a|g|c|c|c|c|g|g|c|t|g|g|g|t|a|c|g|c|a|c|c|c|g|t|g|g|c|a|c|t|g|c|t|g|c|t|g|c|t|c|t|t|c|t|g|g|c|t|c|g|g|c|t|g|g|c|t|c|ei
g|c|a|c|c|c|t|c|t|a|a|a|a|t|a|g|c|t|g|g|a|t|t|g|t|g|t|c|a|t|c|a|t|t|c|t|t|g|t|t|t|t|t|a|a|c|a|c|a|g|c|a|a|t|a|c|a|c|ei
g|c|a|g|g|a|t|c|c|t|a|c|a|c|c|t|t|a|c|a|c|a|t|a|a|a|a|g|g|g|a|g|a|t|g|a|t|g|g|g|a|c|t|a|g|a|g|g|a|g|t|a|a|c|t|g|g|a|ei
t|g|g|c|g|a|c|t|a|c|g|g|c|g|c|g|g|a|g|g|c|c|c|g|a|g|a|g|g|t|g|a|g|g|a|c|c|c|t|g|g|t|a|t|c|c|c|t|g|c|t|g|c|c|a|g|t|c|ei
g|c|g|g|a|a|a|a|c|g|g|g|g|a|a|a|c|g|a|a|g|a|c|g|g|g|a|g|g|t|c|a|g|a|a|g|t|g|t|g|t|g|t|g|t|g|t|g|t|g|t|g|t|g|t|g|t|g|ei
a|a|c|t|t|c|t|c|c|a|a|c|g|a|c|a|t|c|a|t|g|c|t|c|g|c|a|g|g|t|n|a|g|g|c|a|c|a|c|t|c|c|t|g|c|c|a|c|t|c|t|t|g|c|t|c|t|t|ei
c|t|t|a|c|a|c|a|a|a|t|t|g|g|c|a|t|g|c|t|t|g|t|t|t|c|a|g|a|t|g|c|c|t|t|g|g|t|t|c|a|a|g|g|g|a|t|g|g|a|a|a|g|t|c|a|c|c|ei
c|t|c|t|c|t|g|c|a|a|c|c|a|g|g|t|c|c|t|c|t|c|t|c|c|c|a|c|g|t|g|a|g|t|c|c|a|t|g|t|t|g|t|t|g|t|t|g|t|g|g|g|t|a|t|c|a|c|ei
g|c|t|t|g|c|a|c|c|a|t|t|c|a|g|c|t|a|a|g|a|g|g|g|a|c|a|g|a|t|c|a|t|g|a|c|a|c|t|g|a|a|g|c|g|t|g|a|t|g|a|g|a|c|g|c|t|c|ei
g|g|c|c|c|a|g|c|t|g|a|g|g|t|c|t|c|t|c|t|c|t|t|t|g|c|a|g|t|t|t|c|c|a|t|g|t|g|g|t|a|c|a|c|a|c|t|c|c|c|c|c|g|c|t|g|c|a|ei
g|t|c|a|t|c|g|a|a|g|g|g|a|a|g|g|g|t|g|g|g|g|g|c|g|c|t|g|c|g|g|t|g|g|g|g|a|g|c|t|a|t|a|a|a|a|a|t|g|a|c|a|a|t|t|a|a|a|ei
t|c|c|c|c|g|a|g|c|c|c|t|c|a|g|c|a|c|a|g|c|a|g|t|c|g|a|g|a|g|a|t|c|t|t|c|a|a|c|a|t|g|g|c|g|a|g|g|g|a|t|c|a|g|c|g|c|a|ei
c|c|a|t|c|t|t|t|c|t|t|g|g|g|t|t|t|g|g|t|c|c|t|t|c|t|g|t|a|a|t|t|t|t|g|t|g|c|t|g|t|g|a|a|a|g|g|g|t|c|g|t|g|g|t|g|g|a|ei
t|t|g|t|c|c|a|c|c|g|c|c|t|c|t|a|c|c|a|c|g|c|a|g|g|g|g|t|g|a|g|c|t|g|g|c|c|t|c|c|a|c|a|c|a|a|a|g|c|g|a|g|c|t|c|a|c|c|ei
a|g|a|a|g|g|c|t|c|t|g|c|g|c|g|a|c|g|c|c|a|a|g|t|g|a|c|a|a|g|g|c|c|c|a|g|a|t|t|c|a|c|g|a|c|c|t|g|g|t|c|c|t|g|g|t|c|g|ei
g|a|a|g|t|c|a|t|c|t|c|a|g|a|a|a|t|g|t|t|t|g|a|c|c|c|a|g|g|t|a|a|g|a|t|g|c|t|t|c|t|c|t|c|t|g|a|c|a|t|a|g|c|t|t|t|c|c|ei
t|t|g|c|c|t|c|c|a|t|c|g|t|c|a|c|g|g|g|g|g|t|g|a|g|a|g|g|g|t|g|a|g|g|a|g|g|c|t|g|c|a|t|g|g|g|t|t|g|g|g|a|t|g|g|t|t|t|ei
c|a|a|c|c|c|t|c|a|t|g|a|c|c|a|c|c|a|g|c|t|c|t|c|c|c|a|g|t|c|t|g|c|t|c|c|a|g|g|g|a|c|t|t|c|a|c|g|c|c|c|a|c|c|g|t|g|a|ei
a|t|g|t|a|c|g|g|g|g|t|a|a|a|c|t|c|t|t|a|g|c|t|t|g|g|g|a|a|g|t|g|g|t|a|g|g|g|c|c|t|g|c|a|g|g|a|g|g|t|a|g|a|g|a|g|t|c|ei
c|c|t|g|a|c|g|g|t|g|c|c|c|c|c|g|g|g|g|a|g|c|g|g|t|g|g|c|c|c|t|g|g|a|g|a|g|a|g|a|g|g|a|c|c|a|c|g|g|g|g|g|a|c|c|c|c|a|ei
t|g|g|c|c|a|g|c|c|t|c|t|a|a|c|t|c|c|a|g|c|c|c|c|t|c|a|g|c|a|t|c|t|c|c|g|g|c|t|a|c|g|a|c|a|t|c|c|c|t|g|a|g|g|g|c|a|c|ie
g|t|g|a|a|c|t|c|t|g|g|a|c|a|c|a|c|g|c|c|c|a|g|t|g|t|a|g|g|t|a|c|g|t|g|g|a|g|a|a|g|c|t|t|t|c|t|c|c|t|t|t|c|t|g|c|t|g|ei
g|g|t|g|c|a|a|t|c|g|g|c|a|g|t|c|c|a|g|g|a|c|c|g|a|g|g|c|c|c|c|a|g|a|g|g|a|c|c|t|g|t|t|g|g|a|c|c|c|a|g|t|g|g|a|c|c|t|ei
c|c|g|g|g|c|c|t|c|c|t|t|c|g|t|c|a|c|t|g|g|c|g|c|a|c|t|g|c|g|a|g|a|c|c|a|g|c|t|g|c|g|t|t|c|a|g|c|a|g|c|c|g|c|c|c|t|g|ei
a|g|c|t|g|c|t|c|t|c|a|g|g|c|t|g|c|g|t|g|t|a|a|t|a|t|g|g|c|g|g|t|g|g|g|c|g|t|g|t|g|g|a|g|g|a|g|c|t|c|a|c|c|c|a|c|c|c|ei
g|a|c|a|c|t|g|a|g|t|a|g|g|a|c|c|t|c|c|a|a|c|t|t|a|c|a|g|a|t|c|c|c|t|t|c|c|c|c|t|g|a|a|g|t|a|t|t|t|g|a|a|g|a|g|c|t|g|ei
c|c|c|g|a|a|t|g|a|t|c|t|c|c|a|g|c|a|t|t|c|t|g|g|c|t|a|g|c|t|g|c|t|g|a|t|c|g|c|c|t|a|c|a|a|g|c|c|a|g|c|c|c|c|t|g|g|c|ei
g|t|t|a|a|c|c|t|t|a|t|t|t|c|t|t|t|t|c|c|t|t|c|a|t|c|a|g|a|a|a|t|g|g|c|a|c|c|t|c|g|a|a|a|g|g|g|g|a|a|g|g|a|a|a|a|g|a|ei
c|t|g|t|c|a|a|a|c|t|g|c|t|c|t|t|a|t|t|c|a|a|t|t|a|c|a|g|g|c|t|c|c|t|g|c|t|t|g|t|c|t|a|c|c|c|a|t|g|g|a|c|c|c|a|g|a|g|ei
t|g|t|t|t|t|c|t|c|t|t|c|t|a|t|t|c|c|c|t|t|g|g|t|a|c|a|g|g|g|a|c|c|c|g|a|g|t|g|t|a|t|a|g|c|c|c|t|c|c|a|g|a|g|t|g|g|a|ei
c|t|g|g|t|g|c|a|g|g|a|a|t|g|g|c|t|g|g|c|g|a|a|c|c|c|a|g|g|t|g|a|t|g|g|g|g|g|c|t|g|g|c|g|g|g|t|g|c|a|g|g|g|g|g|c|a|c|ei
a|g|a|g|t|g|a|t|t|c|c|t|t|t|c|c|t|a|a|a|a|g|t|t|a|g|a|a|a|g|c|a|t|a|g|a|g|a|t|t|t|g|t|t|c|g|t|a|t|t|t|a|g|a|a|t|g|g|ei
g|t|g|a|t|t|a|g|t|c|c|c|a|g|a|g|c|t|c|g|g|c|t|c|a|c|c|t|c|c|a|c|c|g|g|a|c|a|c|c|t|c|a|g|a|c|a|c|g|c|t|t|c|t|g|c|a|g|ei
g|a|a|g|c|c|g|g|a|c|a|c|g|g|a|g|c|a|t|g|c|a|g|c|t|t|c|g|g|t|g|a|g|c|t|c|t|g|t|t|c|c|c|c|t|g|g|g|c|c|t|g|t|t|c|a|a|t|ei
c|t|g|a|g|g|a|c|c|a|c|a|c|a|c|c|a|c|t|t|c|c|c|c|c|c|a|g|g|c|t|g|a|g|c|t|g|g|a|g|a|t|t|c|a|g|a|a|a|g|a|c|g|c|c|c|t|g|ei
g|c|c|g|c|t|t|c|c|t|c|a|t|c|c|t|g|g|c|a|c|a|c|c|c|t|t|c|a|c|a|g|c|c|g|a|a|g|a|a|g|g|c|c|a|g|t|t|g|t|a|t|g|g|a|c|c|g|ei
a|a|c|t|g|g|a|a|g|a|g|a|a|t|t|c|a|g|a|a|t|c|a|c|a|a|a|t|t|g|t|t|t|c|a|g|c|c|t|g|g|t|c|a|g|g|t|a|g|g|g|t|g|g|t|c|a|a|ei
g|a|a|a|g|a|a|a|g|a|g|a|a|a|g|a|a|a|g|a|a|a|g|a|g|a|a|a|g|a|a|a|g|a|a|a|g|a|a|a|g|a|a|a|g|a|a|a|g|a|a|a|g|a|a|a|g|a|ei
c|c|t|g|c|c|t|g|g|g|a|a|g|c|c|g|c|c|c|t|t|c|c|g|c|c|c|a|g|c|t|c|c|a|c|t|c|c|t|g|c|t|t|c|c|a|g|a|c|c|a|t|g|g|a|c|c|g|ei
c|c|t|g|g|a|g|g|a|g|a|c|c|a|a|a|g|g|t|c|g|c|t|c|g|c|a|t|g|c|a|g|c|t|g|g|c|c|c|a|g|a|t|c|c|a|g|g|a|g|a|t|g|a|t|t|g|g|ei
t|c|t|a|c|c|a|g|g|a|g|t|g|g|c|g|g|t|g|g|g|g|a|c|g|a|c|a|c|t|a|g|g|g|c|t|g|g|a|g|c|c|c|t|c|t|g|a|a|g|a|g|g|a|g|g|c|c|ei
c|c|a|g|c|t|g|c|c|c|g|c|g|c|c|c|t|c|c|c|c|t|g|c|g|c|a|g|a|g|g|t|g|a|g|c|t|t|c|c|t|c|a|a|t|t|g|c|t|c|t|c|t|g|g|a|c|a|ei
a|g|c|t|g|g|g|g|g|g|a|c|t|t|g|g|g|g|a|g|c|g|t|t|c|t|g|g|g|t|g|a|g|a|g|g|c|c|a|g|a|a|a|c|a|g|g|a|g|g|c|t|c|a|g|a|a|g|ei
a|c|c|c|c|g|t|c|g|t|g|c|c|c|t|g|a|c|a|c|t|g|c|c|t|g|c|a|c|c|c|g|t|g|t|t|c|c|c|c|a|c|a|g|g|g|a|g|c|c|g|c|c|c|c|t|t|c|ei
t|t|c|t|t|a|t|a|a|c|t|a|g|c|a|t|a|a|g|a|a|c|a|a|a|g|g|a|c|t|t|t|c|t|c|g|a|t|t|t|t|g|a|g|g|g|g|t|a|a|t|t|a|t|t|a|g|a|ei
g|c|c|t|c|t|c|c|g|g|c|t|t|c|c|g|t|c|t|g|c|c|g|a|c|a|a|g|c|a|c|c|t|g|c|a|c|c|t|g|c|g|c|t|g|c|a|g|c|g|t|c|g|a|c|t|t|t|ei
t|c|c|c|c|a|g|g|g|c|a|g|g|g|a|a|g|g|c|c|t|a|a|t|g|t|c|c|a|t|g|g|c|c|g|t|g|t|c|c|t|c|g|g|g|a|c|c|c|a|g|g|a|c|a|g|c|a|ei
a|a|g|c|c|t|t|c|g|t|t|g|g|a|a|a|c|g|g|g|a|a|t|t|t|t|c|c|c|c|t|t|g|a|a|a|c|t|a|g|a|c|a|g|a|a|g|c|a|t|t|c|t|c|a|g|a|a|ei
a|g|t|t|t|g|c|a|c|c|t|g|t|c|c|c|c|a|c|c|c|t|c|a|t|c|a|g|c|t|g|t|c|c|t|g|c|a|g|c|a|a|a|c|a|c|t|c|c|a|c|c|c|t|c|c|a|c|ei
g|c|t|g|a|g|c|g|a|c|c|t|g|c|a|c|g|c|g|c|a|c|a|g|t|t|c|g|g|g|t|g|g|a|c|c|c|g|g|t|c|a|a|c|t|t|c|a|a|g|g|t|g|a|g|c|g|g|ei
a|g|g|a|c|c|c|t|g|c|c|c|c|t|g|a|c|c|t|a|a|g|c|c|c|c|c|c|a|a|a|g|g|c|c|a|a|a|c|t|c|t|c|c|a|c|t|c|c|c|t|c|a|g|c|t|c|g|ei
g|t|t|c|t|g|a|a|g|g|g|t|a|g|g|g|c|a|g|g|g|g|c|g|a|c|a|g|c|t|c|c|t|a|a|g|c|c|a|c|t|g|c|c|t|g|c|t|g|g|t|g|a|c|c|c|t|g|ei
c|a|t|a|t|a|t|a|g|a|c|t|a|c|a|t|g|c|t|a|g|t|t|a|t|a|c|a|t|a|g|a|g|g|a|t|g|t|g|t|g|t|g|t|a|t|a|g|a|t|a|t|a|t|g|t|t|a|ei
t|g|g|t|g|g|t|g|g|t|t|c|t|g|t|c|g|a|t|c|g|t|c|t|g|a|a|g|g|t|a|a|a|a|g|t|g|g|g|a|t|g|g|g|a|g|a|a|t|t|g|g|g|g|a|g|t|t|ei
a|c|c|t|c|c|a|g|g|g|a|c|a|g|g|a|t|a|t|g|g|a|g|a|c|a|a|g|g|t|a|a|a|t|g|g|a|a|a|c|a|t|c|c|t|g|g|t|t|t|c|c|c|t|g|c|c|t|ei
g|t|c|t|g|t|t|c|a|t|a|a|t|c|g|a|a|g|a|c|a|t|a|t|t|t|t|a|a|a|t|c|g|a|g|g|c|t|g|g|a|g|t|t|t|t|t|t|g|g|a|g|t|t|a|a|g|a|ei
g|g|a|g|a|t|c|g|a|g|a|c|c|a|t|c|c|t|g|g|c|t|a|c|c|g|g|t|t|a|a|a|t|c|c|c|g|t|c|t|c|t|a|c|t|a|a|a|a|a|t|a|t|a|a|a|a|a|ei
a|g|c|g|g|a|a|c|a|c|t|g|a|g|a|c|t|c|c|g|t|t|c|t|c|t|t|g|t|c|t|t|g|t|c|c|t|a|c|c|t|c|c|a|c|g|t|g|c|a|c|a|c|a|g|c|c|c|ei
c|a|a|g|t|t|t|g|a|c|t|a|c|t|a|c|a|t|g|c|c|t|g|t|t|c|g|c|g|t|g|a|g|t|t|g|c|c|c|c|c|a|a|c|c|c|a|c|a|g|g|t|c|c|t|a|g|g|ei
a|g|g|a|g|a|g|a|a|a|t|t|a|a|a|a|t|t|t|a|t|t|a|t|t|a|a|g|g|t|t|c|t|t|a|a|t|a|t|a|c|a|a|a|c|t|a|g|t|a|t|a|t|t|a|t|c|a|ei
c|a|c|c|a|g|c|c|g|g|g|t|a|a|a|c|a|a|t|t|t|c|a|a|g|g|c|c|a|a|t|a|a|t|a|a|c|a|t|g|c|t|a|t|a|g|a|g|a|g|a|t|t|c|a|a|a|a|ei
g|a|t|t|c|c|t|a|c|a|g|c|c|t|t|g|c|c|t|g|c|t|c|c|a|a|a|g|g|c|a|a|c|t|c|t|a|g|a|c|a|t|c|g|c|g|t|c|c|a|a|c|a|a|c|c|g|t|ei
a|c|a|g|t|g|t|c|t|c|g|t|c|t|c|t|t|t|a|t|t|t|t|c|c|c|a|g|c|t|t|c|c|a|t|g|t|a|g|g|a|a|g|c|g|g|c|t|g|t|a|c|c|g|a|t|c|c|ei
t|c|c|t|g|c|t|t|t|a|t|t|g|t|t|g|g|t|t|a|a|t|t|g|t|c|t|c|t|g|g|g|t|t|t|t|g|g|g|g|g|g|c|t|g|g|g|g|g|t|t|g|c|t|t|t|g|c|ei
g|a|g|g|t|g|a|a|g|g|a|c|g|t|c|c|t|t|c|c|c|c|a|g|g|c|c|g|g|t|g|a|g|a|a|g|c|g|c|a|g|t|c|g|g|g|g|g|c|a|c|g|g|g|g|a|t|g|ei
a|a|a|c|a|t|a|c|a|t|t|g|c|c|a|a|g|g|c|t|a|t|t|c|a|t|g|t|c|a|t|c|t|g|g|a|c|a|c|a|t|a|t|a|a|a|a|t|g|c|t|g|c|t|a|a|t|g|ei
g|c|c|a|c|a|g|c|c|c|a|g|t|t|t|t|t|c|t|c|t|g|a|c|a|t|a|g|t|c|t|t|g|c|g|c|c|c|c|a|g|g|a|g|t|c|t|t|c|a|g|t|g|t|g|t|g|a|ei
t|t|c|g|t|c|a|c|t|a|t|c|t|c|c|t|c|t|c|c|a|c|t|g|c|a|c|g|c|a|g|a|t|c|c|c|t|c|a|g|g|c|g|g|t|g|g|g|g|g|c|g|g|c|g|t|a|c|ei
a|a|c|c|t|t|t|c|c|t|c|t|g|t|c|c|t|c|t|c|t|t|t|g|a|t|a|g|g|c|c|g|a|c|c|a|g|t|g|c|a|c|g|c|g|t|c|t|c|c|a|g|g|g|c|t|t|c|ei
c|a|t|t|t|c|t|g|c|a|g|a|g|g|t|t|g|c|a|a|a|c|g|a|a|t|t|c|a|g|a|c|c|t|c|t|a|c|t|c|c|t|t|t|t|c|a|t|t|a|t|t|t|g|g|g|a|a|ei
g|g|t|g|g|g|g|t|g|t|g|c|a|c|a|c|g|g|c|a|g|c|a|g|t|t|g|a|a|t|g|a|a|g|g|c|c|a|g|g|g|a|g|g|c|a|g|c|a|c|c|t|g|a|g|t|g|c|ei
a|g|g|g|c|c|a|a|c|g|t|g|c|t|g|c|g|g|g|c|t|c|t|c|g|t|t|g|a|a|a|c|a|c|a|g|c|c|a|c|c|c|a|a|g|t|g|a|t|g|a|g|a|a|g|g|a|c|ei
c|c|a|a|c|g|c|c|a|c|c|a|g|c|c|a|t|g|g|g|a|g|t|t|c|t|c|a|g|g|a|g|t|c|g|c|g|g|g|g|c|a|g|a|c|g|t|g|a|c|a|t|c|t|g|t|c|c|ei
a|t|t|g|g|c|a|a|g|g|a|g|a|t|c|a|t|t|g|a|c|c|t|g|g|t|t|g|g|a|c|c|g|a|a|t|t|c|g|c|a|a|g|c|t|g|g|c|c|g|a|c|c|a|g|t|g|c|ei
t|g|g|c|a|g|a|c|g|g|g|g|t|g|t|c|c|t|g|c|a|c|a|c|a|c|a|g|g|t|g|a|c|c|a|g|g|c|t|t|c|a|t|g|t|c|c|c|a|g|t|c|c|c|a|g|a|t|ei
a|g|t|c|a|c|t|g|g|g|t|c|t|c|t|g|c|c|c|a|g|g|g|c|a|a|g|g|g|g|g|t|g|a|g|a|c|c|a|c|a|g|g|c|a|c|c|a|g|g|c|c|t|c|c|t|g|g|ei
a|t|c|a|a|a|a|a|c|a|t|g|a|t|t|a|c|a|g|g|g|a|c|t|t|c|a|g|g|t|t|g|g|g|a|t|t|a|a|t|a|a|t|t|c|t|a|g|g|t|t|t|c|t|t|t|a|t|ei
a|a|g|c|t|t|a|t|a|g|g|c|t|g|g|t|g|g|a|g|a|g|a|a|c|t|c|a|g|a|c|g|a|a|a|a|a|t|a|t|a|a|t|a|t|g|a|t|t|t|c|t|c|t|a|c|c|c|ei
c|t|c|t|t|a|a|a|a|c|a|t|c|t|c|c|t|a|c|a|g|t|t|t|a|a|t|t|t|c|a|c|a|t|t|t|a|c|t|a|c|t|t|t|a|a|t|t|c|a|t|c|t|g|g|g|a|t|ei
c|t|c|t|t|c|t|t|a|a|c|t|t|a|a|a|c|c|t|t|c|a|t|t|c|t|a|g|g|a|c|c|a|a|g|a|c|c|c|c|t|g|g|a|c|c|t|g|g|g|g|c|c|c|a|g|t|c|ei
c|a|t|t|t|t|t|g|t|t|g|t|c|t|c|c|t|t|t|c|a|t|c|c|a|c|a|g|c|t|c|c|t|g|g|g|a|a|a|t|g|t|g|c|t|g|g|t|g|a|c|t|g|t|t|t|t|g|ie
g|c|t|t|t|c|c|t|g|c|t|t|g|g|c|a|g|t|t|a|t|t|c|t|c|a|c|a|a|g|a|g|a|g|g|g|c|t|t|t|c|t|c|a|g|g|a|c|c|t|g|g|t|t|g|c|t|a|ei
t|g|a|a|g|g|g|g|g|a|a|g|c|c|c|c|t|t|a|t|a|a|a|c|a|t|c|a|g|c|t|c|t|c|g|t|g|a|g|a|a|c|t|c|a|c|t|c|a|c|t|a|t|c|a|c|a|a|ei
g|g|t|a|g|c|g|g|g|a|t|a|a|g|t|c|a|c|t|g|t|t|t|c|t|t|a|t|t|t|c|t|t|t|a|a|a|a|a|a|a|a|a|a|a|a|a|g|t|t|c|t|g|t|t|g|c|a|ei
a|a|t|g|a|g|a|t|t|c|t|c|a|t|a|t|t|t|t|g|g|t|c|a|g|g|a|t|a|t|a|g|g|a|t|a|c|a|g|t|t|t|t|a|c|a|g|t|g|g|g|t|g|g|g|t|c|t|ei
a|a|g|g|a|g|t|g|a|t|t|t|c|t|a|t|t|t|c|c|t|t|t|t|a|a|a|g|a|g|g|a|g|g|a|a|c|a|a|g|a|a|g|a|t|g|a|g|g|a|a|g|a|a|a|t|c|g|ie
c|g|a|c|g|c|a|g|a|c|c|c|c|a|t|c|c|c|a|c|t|g|g|g|c|t|g|g|g|c|c|a|g|a|c|a|g|c|c|t|g|t|g|a|g|g|c|a|g|t|c|a|g|c|t|g|g|t|ei
c|t|c|c|a|g|c|g|g|c|t|g|g|g|t|g|g|t|g|a|a|g|g|c|c|t|g|g|c|t|c|t|t|c|t|c|t|c|g|g|g|g|c|g|a|c|c|c|c|t|c|a|g|t|g|c|t|c|ei
g|a|c|a|a|a|t|t|t|g|t|g|c|t|a|c|c|c|t|g|g|t|c|t|c|c|t|g|g|g|a|c|a|c|c|t|g|g|g|g|a|c|a|c|t|g|a|a|c|t|g|g|t|g|c|t|g|a|ei
c|g|c|c|t|c|t|t|c|g|c|g|g|t|c|t|c|c|c|t|g|t|c|t|g|c|a|g|a|a|a|c|t|a|g|a|c|a|c|a|a|t|g|t|g|c|g|a|c|g|a|a|g|a|c|g|a|g|ei
t|t|t|a|g|t|t|t|t|t|a|t|t|t|a|a|t|a|t|t|c|t|a|a|t|t|g|a|g|t|g|a|a|a|g|t|a|a|t|t|t|t|t|a|a|t|g|t|g|t|t|t|t|c|c|c|c|a|ei
g|c|a|c|a|t|g|c|c|c|c|g|g|a|c|a|g|t|t|c|t|g|a|t|a|g|c|a|g|t|g|g|c|a|t|g|g|c|c|g|t|t|t|g|t|c|c|c|t|g|a|g|a|g|a|g|c|c|ei
a|c|c|a|t|t|t|t|c|a|g|a|g|g|a|t|a|c|c|t|c|a|t|c|c|a|a|g|g|t|t|a|a|g|c|a|a|t|g|a|g|c|c|t|g|c|a|g|c|a|c|a|c|a|g|c|a|t|ei
g|a|c|c|c|a|g|a|g|a|t|t|a|a|a|a|a|g|a|c|t|t|c|t|t|a|a|g|g|t|a|a|g|a|c|t|a|t|g|c|a|c|c|t|g|c|c|t|g|g|a|t|t|g|g|c|t|c|ei
a|g|g|c|t|g|c|a|c|g|t|g|g|a|t|c|c|t|g|a|a|a|a|t|t|a|a|g|g|t|a|a|g|t|c|c|a|g|g|a|g|a|t|g|t|t|a|a|a|g|c|c|c|t|g|t|t|g|ei
a|g|t|g|t|g|a|c|t|t|c|a|c|c|g|a|a|g|a|c|c|a|g|c|g|c|a|g|g|t|a|g|g|t|t|a|t|c|t|c|t|g|a|t|c|c|c|t|a|c|c|g|a|g|g|t|c|c|ei
c|t|c|a|g|g|c|g|t|c|c|c|c|t|g|c|t|g|t|c|c|c|g|c|g|c|a|g|t|g|a|c|c|t|g|g|g|a|g|c|c|a|a|c|a|c|c|c|t|c|g|c|t|g|a|g|g|t|ei
g|t|g|g|g|c|t|g|a|a|g|c|c|t|g|g|c|t|c|t|g|t|c|c|g|c|a|g|g|g|t|g|c|c|t|g|g|t|a|t|g|t|g|t|g|g|a|a|c|c|g|c|a|c|t|g|a|g|ei
c|g|c|t|c|a|g|c|c|c|g|c|t|c|c|t|t|t|c|a|c|c|c|c|g|c|a|g|g|a|g|a|g|c|c|t|c|g|t|g|g|c|a|g|g|c|c|a|g|t|g|g|a|g|g|g|a|c|ie
g|a|a|a|c|c|t|t|g|a|a|a|a|g|a|t|c|a|a|g|c|t|g|a|g|t|t|c|c|t|t|t|t|c|a|t|c|t|g|t|c|g|c|t|g|t|t|g|a|t|c|t|t|c|a|t|c|t|ei
a|a|t|t|a|t|c|a|a|t|g|t|t|c|t|a|g|t|t|c|t|g|t|g|c|a|t|c|t|g|c|t|t|a|g|t|a|g|a|g|c|t|t|t|t|t|g|c|a|t|g|t|a|t|c|t|t|c|ei
g|t|g|a|g|t|t|g|g|c|a|t|a|g|c|a|a|g|t|a|a|g|a|a|g|g|a|t|a|g|g|a|c|a|c|a|a|t|g|g|g|a|g|g|t|g|c|a|g|g|g|c|t|g|c|c|a|g|ei
a|a|g|c|t|g|c|a|t|g|t|g|g|a|t|c|c|t|g|a|g|a|a|t|c|a|g|g|g|t|g|a|g|t|c|c|a|g|g|a|g|a|t|g|t|t|t|c|a|g|c|c|c|t|g|t|t|g|ei
c|c|t|c|c|c|g|c|t|t|t|g|t|g|t|g|c|c|c|c|g|c|t|c|g|c|a|g|c|c|t|c|c|c|g|c|g|a|c|g|a|t|g|c|c|c|c|t|c|a|a|c|g|t|t|a|c|c|ei
c|a|a|t|a|t|g|a|a|a|t|t|a|g|t|g|c|a|c|c|t|t|g|a|a|a|g|a|a|c|a|c|a|a|t|a|a|g|a|g|c|a|a|t|t|t|t|t|a|g|g|g|a|a|c|a|a|g|ei
g|a|g|c|t|g|c|t|g|c|g|c|t|t|c|t|c|c|a|a|c|t|g|c|a|c|t|g|g|c|c|g|g|t|c|t|g|c|a|a|g|t|c|a|g|a|g|g|a|t|g|g|c|c|a|g|t|g|ei
g|c|t|g|g|a|c|a|c|c|g|t|g|c|c|c|t|t|c|c|c|g|c|g|c|c|a|g|g|t|g|c|g|c|g|c|a|g|g|c|a|c|c|g|g|g|a|c|a|c|g|g|g|g|c|a|g|g|ei
a|c|g|g|g|a|a|g|g|a|g|a|c|g|c|t|g|c|a|g|c|g|c|c|g|g|t|a|c|c|a|g|g|g|g|c|c|a|c|g|g|g|g|c|g|c|c|t|a|c|c|t|g|a|t|c|g|c|ei
c|g|t|a|g|c|c|a|g|c|t|c|t|c|g|c|t|t|t|c|c|a|c|t|t|c|a|g|g|g|a|g|c|a|g|a|t|c|a|a|a|c|g|g|g|t|g|a|a|g|g|a|c|t|c|g|g|a|ei
c|g|g|c|c|c|t|g|g|t|a|t|c|c|a|t|t|c|c|g|g|a|g|a|g|t|t|g|t|g|c|a|g|g|c|t|g|a|g|g|c|t|g|g|g|g|g|c|a|t|g|c|a|c|a|c|c|g|ei
a|c|t|t|c|a|g|t|g|g|a|g|g|a|a|a|c|a|a|c|t|g|a|g|t|g|a|g|g|t|g|g|a|a|a|t|a|a|c|a|g|a|t|c|a|t|a|g|a|a|t|g|a|g|a|a|g|c|ei
g|a|a|a|g|t|t|g|c|c|a|g|a|g|c|a|c|a|t|c|c|c|a|a|c|a|a|a|g|t|g|a|g|t|t|a|t|t|c|c|c|c|c|a|t|c|t|g|a|g|g|g|c|a|a|g|a|t|ei
t|a|c|a|t|c|g|a|g|a|c|c|t|c|g|g|c|c|a|a|g|a|c|c|g|c|a|g|g|t|g|a|g|g|c|a|g|c|t|c|t|c|c|a|c|c|c|c|a|c|a|g|c|t|a|g|c|c|ei
a|a|g|c|t|g|a|t|g|g|c|c|c|t|g|c|a|g|c|t|g|c|t|c|g|t|g|g|c|a|c|a|g|t|g|c|a|c|t|c|t|g|g|a|c|a|g|t|g|c|a|g|g|a|a|g|c|c|ei
c|a|g|g|a|a|c|a|g|g|a|a|g|t|c|t|g|c|t|t|t|g|c|g|a|g|a|g|g|t|a|c|a|t|g|c|a|g|c|t|c|a|t|t|t|c|a|t|a|c|t|c|a|a|a|a|t|a|ei
g|a|c|a|g|t|g|g|g|t|t|c|t|t|c|t|g|t|g|a|a|g|a|a|t|t|c|c|a|g|t|g|a|t|g|a|t|g|a|t|g|t|g|a|t|t|c|t|g|a|a|a|g|a|a|g|a|a|ei
t|t|g|c|c|c|c|t|c|a|c|t|g|c|t|t|g|g|c|t|t|g|c|c|g|c|a|g|a|c|t|g|t|g|g|g|c|t|g|c|g|a|c|c|t|c|t|g|t|t|c|g|a|g|a|a|g|a|ei
g|g|a|t|t|g|t|t|t|t|t|c|c|t|c|t|t|c|c|c|a|c|c|t|c|a|a|g|c|t|t|g|g|a|a|t|c|c|a|c|g|a|a|g|a|c|t|c|c|a|c|t|a|a|c|c|g|c|ei
g|t|t|g|a|a|c|a|a|t|t|t|c|c|a|c|c|a|a|c|t|t|a|t|a|t|a|g|g|c|g|g|a|c|c|t|t|g|c|c|a|a|g|t|a|t|a|t|c|t|g|t|g|a|a|a|a|t|ei
c|t|t|g|t|t|a|c|a|g|g|g|g|t|g|c|t|g|g|c|c|t|t|c|t|g|g|c|g|c|c|t|g|c|c|c|c|t|g|t|c|g|g|c|c|c|c|g|c|c|c|g|a|g|a|a|c|c|ei
c|t|c|t|c|t|c|t|c|t|c|t|c|t|c|t|c|t|c|t|c|t|t|c|c|t|c|t|c|t|c|t|c|t|c|t|g|t|c|t|c|t|c|c|g|t|c|t|c|t|c|t|g|t|g|t|c|t|ei
c|g|g|c|c|t|c|g|c|a|a|g|c|c|c|a|c|g|g|c|c|c|g|t|g|g|g|g|t|g|c|c|g|t|c|c|c|g|c|g|c|c|g|g|g|g|c|g|g|a|g|c|a|g|g|c|c|c|ei
c|t|a|g|a|g|g|a|a|g|g|c|a|t|c|c|a|a|a|c|g|c|t|a|g|t|g|g|g|t|g|a|g|g|g|t|g|g|c|a|c|c|a|g|g|g|a|t|c|c|c|c|a|a|t|c|c|t|ei
a|a|a|g|c|c|a|c|a|a|g|g|a|c|c|a|c|c|c|c|c|a|c|a|g|a|g|g|c|a|a|c|c|a|g|c|c|t|c|a|a|g|g|t|c|c|c|c|c|a|c|c|t|c|c|t|c|c|ei
t|g|g|g|c|a|t|g|g|t|g|g|c|t|g|g|a|g|a|t|g|a|g|a|a|c|c|t|a|t|g|a|g|g|t|a|g|g|g|g|g|t|c|c|c|c|a|g|a|g|t|c|t|c|c|c|t|g|ei
a|c|c|c|c|c|g|c|g|g|c|t|t|c|t|t|c|c|t|c|t|t|c|t|g|a|g|g|g|t|g|c|g|t|g|g|t|g|g|c|c|c|t|g|g|g|a|g|t|g|g|g|g|g|g|t|t|g|ei
t|t|a|a|g|g|a|g|g|a|a|g|g|a|a|t|g|a|a|a|c|c|t|t|t|c|a|a|c|a|t|g|g|a|a|a|t|g|a|t|c|t|g|t|a|t|t|g|a|c|t|a|a|t|a|c|a|c|ei
g|g|c|c|c|t|a|g|t|a|g|c|a|g|c|c|a|t|a|c|a|g|g|g|t|g|g|g|g|a|a|g|g|g|g|g|c|c|t|c|t|g|g|g|g|c|t|g|a|c|c|a|g|g|c|g|a|c|ei
a|a|g|a|g|t|g|c|a|a|a|t|g|c|a|c|c|t|c|c|t|g|c|a|a|a|g|a|g|t|g|a|g|t|g|t|g|a|g|g|c|c|a|t|c|t|c|c|a|t|g|g|t|c|t|g|g|g|ei
g|t|t|t|c|t|a|a|t|t|g|c|t|a|t|t|g|t|c|c|t|a|t|t|a|t|a|g|a|c|t|c|c|t|g|g|t|t|g|t|c|t|a|c|c|c|g|t|g|g|a|c|c|c|a|g|a|g|ei
t|t|a|c|c|t|a|a|t|t|a|g|a|a|a|a|a|a|a|a|t|c|t|g|c|a|a|a|c|a|a|t|t|a|t|a|a|t|a|a|t|g|g|g|g|a|a|g|t|c|a|t|a|t|a|c|a|a|ei
c|c|a|c|t|t|c|a|g|g|t|a|c|t|a|c|c|c|g|t|c|t|t|t|t|c|t|g|g|t|t|c|t|c|g|t|c|c|t|g|t|c|a|c|c|c|a|g|g|c|t|g|g|t|a|t|g|c|ei
t|a|a|t|t|t|t|c|a|t|c|a|a|a|t|t|a|t|t|c|c|t|t|t|g|t|a|g|c|t|c|g|a|t|g|a|a|c|t|t|c|g|g|g|a|t|g|a|a|g|g|g|a|a|g|g|c|t|ei
g|g|g|g|t|g|g|g|g|g|c|t|g|a|g|a|c|c|c|c|a|g|a|g|c|c|c|c|t|t|c|t|c|c|c|a|c|a|g|g|a|a|a|g|g|g|g|a|a|g|c|c|a|g|a|c|c|c|ei
a|a|a|c|t|a|a|a|g|a|a|t|t|a|t|t|c|t|t|t|t|a|c|t|t|c|a|g|t|t|t|t|t|c|t|t|g|a|t|c|a|t|g|a|a|a|a|c|g|c|c|a|a|c|a|a|a|a|ei
g|g|g|g|c|c|t|g|a|t|g|g|a|c|t|g|t|c|c|c|c|a|t|c|g|c|a|g|a|t|t|g|a|g|g|a|g|a|g|c|a|c|c|a|c|a|g|t|g|g|t|c|a|c|c|a|c|a|ei
c|a|g|a|t|g|g|g|c|t|c|a|c|g|g|c|c|a|t|c|c|c|t|c|g|c|a|g|g|a|g|c|a|g|c|g|a|c|t|g|g|a|c|c|c|a|g|a|g|c|c|a|t|g|t|g|g|c|ei
c|c|t|g|g|a|g|g|g|g|a|a|t|c|t|g|g|t|c|a|c|c|c|g|g|c|t|g|t|g|a|a|a|c|a|a|a|g|t|t|g|c|t|c|t|t|g|c|a|g|a|g|g|c|c|t|g|g|ei
a|a|a|c|c|c|g|c|c|t|c|c|c|a|g|g|t|t|t|a|a|g|c|a|t|c|t|c|a|t|g|c|c|t|c|a|g|c|c|t|c|c|c|a|g|t|a|g|c|t|g|g|g|a|t|t|a|g|ei
t|a|c|t|t|g|g|a|g|t|g|g|g|t|a|c|a|t|t|c|t|g|a|a|g|t|a|a|t|a|t|a|a|g|t|g|t|c|t|c|a|a|t|t|c|a|c|t|t|t|c|t|a|g|t|c|a|t|ei
c|g|c|t|t|g|g|g|a|c|t|g|c|a|g|c|g|t|g|g|a|g|a|c|g|c|g|g|c|t|g|c|g|a|g|c|a|c|g|c|g|t|g|c|a|a|t|g|c|g|a|t|c|c|c|t|g|g|ei
g|c|g|a|c|t|g|c|c|t|g|a|c|t|t|c|t|c|c|t|t|t|c|t|t|c|a|g|c|a|c|c|a|t|g|a|a|g|c|t|t|c|t|c|a|c|g|g|g|c|c|t|g|g|t|t|t|t|ei
c|t|c|g|g|a|t|g|c|a|g|a|g|a|t|c|g|g|c|a|t|g|t|a|c|t|t|g|g|t|g|t|g|t|c|c|t|g|g|a|g|c|c|c|t|g|c|g|c|t|a|c|c|a|t|t|c|a|ei
g|a|c|t|t|c|c|a|c|a|c|c|t|c|c|t|g|t|c|c|c|c|c|g|c|c|a|g|g|t|c|c|t|g|t|t|g|t|t|g|g|t|g|a|a|t|g|g|a|g|c|t|c|a|g|t|t|g|ei
a|t|t|c|c|a|a|a|a|a|t|g|c|t|t|t|c|t|t|t|c|c|c|c|g|c|a|g|g|t|g|a|g|a|a|g|a|t|g|a|c|a|g|a|g|g|a|a|g|a|a|g|t|a|g|a|g|a|ei
c|c|t|g|g|c|a|a|g|c|g|c|t|g|a|g|c|g|g|a|g|a|t|t|g|c|a|g|g|c|a|g|t|g|g|c|c|t|t|g|t|c|g|t|c|g|a|a|g|t|c|t|g|g|c|c|t|t|ei
t|c|a|g|t|g|c|c|c|t|t|c|t|a|t|c|a|t|c|a|a|t|g|g|t|g|g|t|c|t|g|a|t|t|a|a|g|g|c|c|t|g|g|c|t|c|c|c|a|c|t|g|g|c|t|a|c|c|ei
g|c|c|t|t|g|c|c|a|a|g|g|t|c|c|t|c|c|c|t|c|t|g|a|c|t|g|c|c|a|g|a|a|g|c|a|g|g|a|g|t|c|c|c|a|a|g|t|g|a|c|a|g|g|a|c|c|t|ei
g|a|a|t|t|c|t|c|a|g|t|a|g|c|t|t|c|t|t|t|g|t|g|g|g|t|g|t|a|c|t|c|a|a|c|t|c|a|c|a|g|a|g|t|t|g|a|a|c|c|t|t|c|c|t|t|t|a|ei
a|a|g|c|t|g|c|a|t|g|t|g|g|a|t|c|c|t|g|a|g|a|a|t|c|a|g|g|g|t|g|a|g|t|c|c|a|g|g|a|g|t|t|t|c|a|g|c|a|c|t|g|t|t|g|c|c|t|ei
g|g|g|g|c|a|g|g|a|c|t|c|c|a|c|c|c|g|a|t|c|a|t|c|c|c|a|g|a|t|t|c|a|g|c|a|g|c|g|a|c|t|g|c|a|g|g|a|g|g|a|g|c|t|a|g|a|c|ie
g|c|c|c|a|g|a|c|g|c|c|c|g|c|c|t|t|c|g|a|c|a|a|c|c|a|a|a|g|t|g|a|g|c|g|c|g|c|g|c|g|g|g|g|g|c|t|c|c|g|g|g|g|a|c|g|g|g|ei
c|a|t|c|a|t|c|c|g|t|g|t|c|a|a|c|c|a|g|c|c|a|t|g|g|a|a|g|g|t|g|a|g|c|a|g|a|a|c|a|c|a|a|a|t|t|a|a|a|t|a|a|a|a|t|g|a|a|ei
c|c|c|c|a|c|g|a|a|g|t|g|t|t|g|g|a|t|a|t|a|a|g|c|g|a|c|t|g|t|a|a|g|t|g|a|a|t|t|a|c|t|t|t|t|t|t|t|g|t|c|a|a|t|c|a|t|t|ei
c|t|g|g|t|g|a|t|g|c|c|c|a|c|c|t|t|c|c|c|c|t|c|c|c|c|a|g|g|c|a|a|a|t|g|g|g|a|g|a|g|a|c|c|c|t|t|t|g|a|a|g|t|c|a|a|g|g|ei
a|a|g|a|c|t|t|t|t|t|a|t|a|g|g|c|t|g|g|t|c|a|c|c|c|g|g|a|g|c|a|g|g|a|g|t|c|a|g|c|c|c|c|a|g|t|c|a|g|g|a|c|a|c|a|g|c|a|ei
c|t|g|g|a|g|c|c|t|c|a|t|a|a|g|t|t|c|c|a|g|a|a|a|g|a|c|c|a|a|c|g|g|c|a|t|c|a|c|c|c|c|t|c|g|g|c|g|c|t|g|g|c|t|g|g|t|t|ei
g|t|g|g|g|g|a|g|a|a|t|a|t|g|t|g|g|a|c|a|a|c|a|a|a|c|c|t|g|g|t|c|c|c|c|a|g|g|c|t|c|t|g|g|c|c|c|a|g|a|g|c|a|g|g|g|g|c|ei
g|t|g|c|c|c|c|t|a|c|g|c|c|t|c|t|c|c|t|t|g|c|t|c|t|c|a|g|g|g|c|c|t|c|a|c|c|a|a|c|c|a|g|c|g|g|g|c|t|c|a|g|g|a|c|g|t|t|ei
g|g|g|c|g|g|g|t|c|t|c|a|g|c|c|c|c|t|c|c|t|c|t|c|c|c|a|g|g|c|t|c|c|c|a|c|t|c|c|a|t|g|a|g|g|t|a|t|t|t|c|t|a|c|a|c|c|g|ei
a|g|c|t|c|t|c|c|g|g|c|t|a|c|g|g|c|a|a|g|c|a|t|a|g|c|c|t|g|t|a|a|g|t|g|g|a|a|g|g|a|a|g|c|c|t|c|g|g|c|c|c|c|a|t|c|c|t|ei
a|a|g|g|a|c|t|t|a|g|t|g|a|c|c|c|a|c|g|a|c|c|c|t|a|c|a|g|t|g|t|c|t|a|c|a|t|t|g|g|g|c|c|a|g|c|a|g|g|a|c|c|t|t|t|t|a|g|ei
g|c|t|g|t|a|a|t|t|a|t|a|t|t|g|a|g|g|t|g|a|t|g|a|a|a|a|g|a|a|c|t|g|a|a|g|t|t|g|a|t|g|g|a|a|a|c|a|a|t|g|a|a|g|t|t|a|a|ei
c|c|a|c|t|c|c|t|c|t|t|c|g|g|a|c|t|c|a|a|t|a|a|g|a|g|a|c|c|a|g|a|a|c|g|a|g|t|g|c|a|t|c|a|t|t|g|c|c|a|a|c|c|c|g|g|c|c|ei
c|t|g|c|t|g|t|g|a|t|a|t|g|g|a|g|g|a|a|g|a|a|g|g|t|c|a|g|g|t|g|g|g|g|a|a|g|g|g|a|g|a|a|g|g|g|t|g|g|g|g|t|c|t|g|a|g|t|ei
c|t|c|t|g|t|t|c|a|g|t|g|t|a|a|a|t|a|g|t|t|a|c|c|a|g|t|g|c|c|a|a|c|a|a|t|c|c|t|a|g|t|g|c|t|t|t|c|c|t|t|t|t|t|t|a|a|a|ei
t|a|t|t|t|c|a|t|c|a|g|g|a|a|g|a|a|t|g|g|a|g|g|c|g|a|c|c|t|a|a|a|g|g|t|a|g|a|a|a|t|a|t|g|t|c|a|a|a|t|g|t|a|c|a|g|c|a|ei
c|t|g|c|t|g|t|g|c|t|g|t|g|g|a|g|a|a|a|g|a|a|g|g|t|c|a|g|g|t|a|a|g|g|a|a|g|g|g|g|t|g|a|c|a|a|g|t|g|g|g|g|t|c|t|g|a|g|ei
g|a|g|a|a|a|a|g|c|c|c|g|t|c|t|g|t|t|t|g|c|a|g|c|t|c|t|g|a|a|c|a|t|g|a|c|a|t|c|t|t|c|g|g|t|t|t|g|c|a|g|c|c|c|t|g|c|t|ei
t|c|a|g|a|t|g|t|c|a|t|g|t|a|c|a|c|c|g|a|c|t|g|a|a|a|a|g|g|t|a|a|a|c|g|c|a|a|g|g|g|a|t|t|g|g|a|c|a|t|t|g|c|c|c|a|c|c|ei
c|a|g|a|g|c|g|g|a|c|t|g|g|g|c|t|g|t|a|a|c|a|g|t|c|c|g|g|g|t|a|a|g|a|g|g|a|a|c|t|g|g|g|g|a|t|g|g|a|a|a|t|g|g|g|a|t|g|ei
g|a|g|a|a|g|a|g|c|t|c|a|g|a|g|t|g|t|c|t|c|t|g|c|c|c|a|g|a|c|a|t|a|c|a|g|t|g|t|a|g|a|c|a|a|g|c|a|t|g|t|g|c|c|a|g|a|c|ei
g|a|a|t|a|g|c|c|c|t|c|a|c|t|g|c|t|t|g|t|c|g|t|g|c|c|a|g|g|c|a|c|c|c|c|a|g|c|t|a|c|c|a|t|g|t|c|c|c|a|g|a|t|a|g|c|c|a|ei
g|a|t|g|a|a|g|a|t|g|a|g|a|t|g|t|t|c|t|a|t|g|t|g|t|c|t|g|g|a|c|a|a|g|a|a|g|g|a|g|a|c|c|g|t|c|t|g|g|c|a|t|c|t|g|g|a|g|ei
a|g|g|g|c|c|a|c|g|t|g|c|c|a|g|g|c|c|c|g|g|g|g|t|g|c|g|g|c|t|a|c|t|c|a|g|c|a|g|c|c|c|t|c|c|t|c|a|c|c|c|g|t|c|t|g|g|g|ei
t|t|g|a|g|a|g|c|t|t|c|t|c|a|g|a|c|t|a|t|c|c|a|c|t|t|g|g|g|t|a|a|g|g|a|t|g|a|c|t|a|c|t|t|a|a|a|t|g|t|a|a|a|a|a|a|g|t|ei
t|g|t|c|a|a|g|g|a|g|g|a|a|a|a|c|a|t|t|a|g|g|g|a|a|c|a|a|a|a|a|t|g|a|t|a|t|a|a|a|g|c|c|a|t|a|t|g|a|g|g|t|t|a|t|a|t|t|ei
t|g|c|g|g|g|c|c|g|c|t|c|c|g|a|c|g|g|c|g|g|t|c|a|c|c|t|g|g|t|a|a|g|t|g|c|t|t|t|t|c|t|c|t|a|g|g|a|g|c|t|a|a|c|g|t|t|c|ei
a|c|c|g|g|g|a|c|a|g|g|a|t|t|t|g|a|c|t|g|t|g|c|a|c|a|a|g|g|t|a|a|g|c|g|a|t|a|g|c|a|g|c|a|g|g|c|c|t|c|a|a|a|a|g|c|g|t|ei
t|g|t|g|c|t|g|a|c|a|g|c|a|g|c|t|c|a|t|t|g|c|t|g|g|a|a|g|g|t|g|a|g|g|a|g|c|t|a|a|g|g|a|a|c|t|t|c|c|t|g|g|c|c|a|g|c|c|ei
a|t|t|c|a|c|g|a|t|a|t|t|t|a|a|g|a|c|a|t|a|a|t|t|t|g|t|g|t|g|t|g|t|a|t|t|t|a|t|g|a|t|g|c|t|g|t|c|a|c|t|g|t|c|t|c|t|g|ei
c|c|t|t|a|a|g|c|t|a|g|t|c|c|c|t|t|c|t|c|c|c|c|t|g|c|a|g|a|c|g|a|g|a|t|g|c|a|g|c|g|a|c|t|a|t|g|t|g|t|g|t|a|t|g|t|g|c|ei
t|c|c|a|t|c|c|g|c|t|c|c|t|g|t|t|g|t|c|t|c|a|t|c|c|c|a|a|g|t|g|a|g|t|t|t|t|c|t|a|g|a|t|t|t|c|c|a|t|c|a|t|g|c|c|g|c|c|ei
t|t|t|t|c|t|g|g|t|a|t|c|t|t|t|g|a|g|g|a|c|a|g|a|c|t|a|c|a|t|c|t|g|c|a|a|a|a|c|c|a|c|c|a|t|t|g|g|g|g|a|c|a|g|g|g|a|g|ei
g|a|c|c|t|c|c|g|c|t|g|c|a|a|a|t|a|c|a|t|c|t|c|c|c|a|t|c|t|a|c|a|c|c|a|a|c|t|a|t|g|a|g|g|c|g|g|g|c|a|a|g|g|a|t|g|a|c|ei
g|g|c|c|g|c|g|c|g|c|c|c|t|c|c|t|c|g|c|c|c|c|c|g|c|g|g|c|a|g|c|a|a|t|a|c|g|c|g|c|g|g|c|g|c|g|g|g|c|c|g|g|g|g|g|c|g|c|ei
g|t|c|a|c|c|g|a|t|c|c|t|g|a|c|c|t|c|t|g|t|c|a|c|t|c|a|g|g|a|a|a|g|t|c|a|g|t|a|g|g|a|g|t|g|g|t|g|a|c|c|a|c|c|a|c|a|c|ei
g|a|c|c|a|g|a|a|a|a|t|t|a|a|t|g|a|a|g|t|t|t|c|t|t|t|c|t|g|t|a|a|g|t|a|t|a|t|g|a|g|g|c|c|c|a|t|g|c|t|g|g|c|a|g|t|g|c|ei
c|c|c|t|g|t|g|t|a|g|c|c|t|t|g|t|g|c|a|c|a|g|c|a|c|a|t|g|g|t|a|a|g|g|g|a|g|t|g|c|t|t|g|c|a|g|g|c|t|g|g|a|a|c|a|g|g|c|ei
g|a|g|a|g|c|t|g|c|a|t|g|g|g|c|t|c|a|c|a|a|c|t|a|g|a|g|g|a|a|t|t|t|g|t|a|g|a|a|g|g|g|a|t|a|t|a|c|a|a|a|g|t|g|g|a|a|a|ei
g|a|a|c|g|t|c|t|g|g|c|t|a|a|a|t|a|c|a|a|t|c|a|c|c|a|t|g|a|g|a|a|t|t|g|a|g|g|a|a|g|a|g|c|t|g|g|g|g|g|a|t|g|a|a|g|c|t|ei
g|a|t|c|c|g|c|c|g|c|c|c|g|t|c|c|a|c|a|c|c|c|g|c|c|c|a|g|g|t|a|a|g|c|c|c|g|g|c|c|a|g|c|c|g|a|c|c|g|g|g|g|c|a|t|g|c|g|ei
a|g|g|g|c|c|c|c|t|t|a|c|g|t|t|c|c|c|c|t|c|t|t|t|c|c|a|g|a|g|c|c|g|g|c|t|t|c|c|c|a|g|c|c|c|a|c|c|a|t|c|c|c|c|a|t|c|g|ei
c|g|g|t|t|g|g|a|g|a|a|a|g|g|g|t|t|c|c|a|a|g|t|g|g|g|t|g|a|c|c|t|t|g|c|g|g|a|g|a|g|a|a|g|a|t|t|t|t|g|a|t|g|t|g|g|a|a|ei
g|a|c|a|g|a|g|c|c|t|g|g|g|t|g|g|g|c|a|t|c|t|g|c|a|c|a|g|a|c|t|g|g|t|c|c|c|c|c|a|a|g|g|t|g|g|t|g|g|a|g|c|t|g|t|g|t|a|ei
a|t|g|g|a|g|g|a|g|t|c|g|c|t|a|c|c|c|a|c|a|t|a|g|c|t|g|a|g|t|g|a|g|t|g|a|g|g|g|g|t|c|g|g|c|c|t|t|c|c|c|a|c|c|a|t|g|g|ei
t|c|a|g|c|t|t|t|g|t|t|t|g|t|t|t|t|c|t|c|t|t|t|t|a|t|a|g|a|g|t|g|c|c|c|a|c|g|a|c|c|c|t|c|c|g|g|c|t|g|t|c|c|a|c|c|t|c|ei
c|c|t|t|c|c|a|t|c|g|t|c|g|g|g|c|g|c|c|c|c|a|g|c|c|c|a|g|g|t|g|a|g|t|g|g|a|t|g|g|c|g|c|c|g|c|g|g|g|g|c|t|c|c|t|g|g|g|ei
c|t|c|c|g|g|c|g|c|a|g|t|g|t|t|g|g|g|a|c|t|g|t|t|g|g|t|a|t|c|g|g|a|a|a|g|c|a|a|g|c|c|t|a|c|g|t|t|g|c|t|c|a|c|t|a|t|t|ei
a|g|c|c|c|t|c|a|a|c|c|c|t|t|c|t|g|t|c|t|c|a|c|c|c|c|a|g|c|c|t|a|a|a|g|c|t|c|c|t|t|g|a|c|a|a|c|t|g|g|g|a|c|a|g|c|g|t|ie
a|g|g|g|a|g|t|t|g|a|c|a|g|a|g|g|t|g|t|g|a|g|c|g|a|c|t|t|t|a|a|g|a|a|g|c|t|g|c|a|c|a|t|a|a|g|a|t|g|c|t|a|g|t|a|t|g|a|ei
c|a|g|g|a|g|a|t|t|t|t|a|t|g|c|c|t|c|a|a|a|a|t|t|g|a|t|g|c|t|t|t|t|t|g|g|a|a|g|g|a|c|a|g|c|a|c|a|t|t|a|a|t|t|a|t|t|t|ei
c|g|g|a|c|c|a|g|c|t|c|a|t|g|g|c|c|t|t|c|g|g|c|g|t|c|c|a|g|c|g|a|g|c|c|g|t|g|c|g|c|g|c|t|c|t|g|c|a|g|c|c|t|g|c|a|c|a|ei
a|a|a|g|a|t|g|a|t|a|a|g|c|c|c|a|c|t|c|t|a|c|a|c|g|g|a|g|g|t|a|a|g|t|g|a|a|t|g|c|t|a|t|g|g|a|a|t|g|a|a|g|c|c|c|t|t|c|ei
t|a|c|a|c|a|a|t|c|t|t|t|c|c|t|t|c|t|g|t|g|t|c|t|c|c|a|g|a|a|c|c|t|c|c|t|c|c|t|c|c|t|t|t|g|a|g|g|t|t|c|g|a|a|c|c|t|g|ei
g|c|t|g|a|c|t|c|c|a|c|a|a|c|c|a|g|g|a|g|t|c|t|t|c|a|c|t|a|t|a|t|a|a|t|t|t|c|a|a|g|a|a|t|t|c|t|a|t|a|g|a|a|g|t|a|g|a|ei
a|t|g|g|a|c|t|c|t|g|t|t|c|g|c|t|c|a|g|g|t|c|c|t|t|g|g|c|c|a|g|a|t|c|t|t|t|a|c|a|c|c|a|g|a|c|a|a|c|t|t|t|g|t|a|t|t|t|ei
g|c|a|t|t|t|t|t|t|t|g|a|g|g|c|a|a|t|g|a|t|g|t|a|g|a|a|a|t|a|a|a|g|a|a|t|t|t|a|a|a|t|t|t|t|a|g|g|a|c|t|t|t|a|c|a|g|c|ei
g|c|a|t|c|t|a|t|c|g|c|a|t|g|a|t|c|a|a|g|c|t|a|g|c|t|a|g|g|t|a|a|g|t|a|g|c|t|t|t|g|g|t|a|c|t|t|g|g|t|g|t|g|g|c|a|a|g|ei
c|a|g|c|a|g|c|t|c|a|g|c|c|t|c|c|c|c|c|c|g|c|t|g|g|a|g|c|g|a|a|a|g|t|t|t|c|t|t|g|g|t|c|t|c|a|g|c|t|t|c|a|t|t|t|c|c|g|ei
c|a|t|c|t|c|t|g|t|t|g|t|c|t|c|t|t|t|c|t|a|c|c|t|a|c|a|g|c|t|c|c|t|g|g|g|a|a|a|c|g|a|g|c|t|g|g|t|g|a|t|t|g|t|c|t|t|g|ei
g|a|c|t|g|g|t|t|t|t|g|g|a|g|g|t|g|g|c|c|c|a|g|a|t|t|g|g|g|t|a|a|g|t|a|g|a|g|t|t|t|g|t|t|a|g|g|a|a|t|a|g|t|a|a|a|g|a|ei
a|g|g|g|c|c|c|c|t|c|a|c|c|t|t|c|c|c|c|t|c|c|t|t|c|c|a|g|a|g|c|c|a|t|c|t|t|c|c|c|a|g|c|c|c|a|c|c|a|t|c|c|c|c|a|t|c|g|ei
c|g|g|a|g|g|c|g|c|t|g|t|t|c|c|a|g|c|c|t|t|c|c|t|c|t|g|g|g|t|a|g|g|t|g|t|t|g|t|g|a|g|c|t|a|a|a|g|g|t|t|t|c|t|a|c|t|c|ei
g|g|g|t|c|a|c|t|t|c|c|c|c|a|g|c|t|t|c|a|a|c|c|c|g|c|c|t|c|a|t|c|c|a|g|c|g|t|c|a|c|c|t|c|t|g|c|c|t|c|c|c|c|c|a|a|c|c|ei
g|g|g|g|c|c|a|t|c|g|t|g|g|g|c|a|t|c|c|t|c|a|t|t|c|g|t|c|c|t|g|c|t|c|c|t|g|g|t|g|g|t|t|g|t|g|g|a|c|a|t|c|a|c|c|t|g|c|ei
a|a|a|a|g|a|g|c|t|g|a|t|g|a|a|a|c|a|a|t|g|g|c|a|a|c|c|t|c|c|a|a|g|g|t|g|a|a|a|t|t|g|a|a|g|c|t|c|a|c|a|c|a|g|a|t|g|t|ei
a|a|g|c|t|g|c|a|t|g|t|g|g|a|t|c|c|t|g|a|g|a|a|t|c|a|g|g|g|t|g|a|g|t|a|c|a|g|g|a|g|a|t|g|t|t|t|c|a|g|c|c|c|t|g|t|t|g|ei
t|c|t|g|c|t|g|c|c|t|c|c|t|t|g|c|c|c|c|t|c|a|c|c|c|c|a|g|g|c|c|a|g|g|a|t|c|a|a|g|t|c|a|c|t|g|t|a|g|c|g|a|t|g|a|c|t|c|ei
g|a|t|g|g|g|a|g|a|a|c|c|t|g|c|g|t|a|g|a|c|t|c|g|g|a|g|g|c|t|c|c|c|t|c|g|g|g|c|g|a|c|t|t|g|g|a|t|c|t|c|c|a|t|g|t|c|g|ei
a|a|t|a|t|t|a|c|c|t|g|a|g|g|t|a|a|g|g|t|a|a|g|c|a|a|g|a|g|t|g|g|g|a|g|g|c|a|g|g|g|a|g|t|c|c|a|g|t|t|c|a|g|g|g|a|c|g|ei
g|a|g|a|a|g|a|a|t|t|a|a|c|c|t|t|t|t|g|c|t|t|c|c|a|g|t|t|g|a|a|c|a|t|t|t|g|t|a|g|c|a|a|t|a|a|g|t|c|a|t|g|c|a|a|a|t|a|ei
g|t|c|a|c|a|a|t|c|t|c|t|g|a|t|t|c|c|t|t|g|c|a|a|g|g|a|t|g|t|a|g|t|g|a|a|t|g|c|t|t|t|c|c|a|g|a|g|t|g|g|a|a|g|t|t|c|c|ei
c|a|t|c|t|t|t|g|t|t|g|t|c|t|c|t|t|t|t|c|a|t|c|c|a|c|a|g|c|t|c|c|t|g|g|g|a|a|a|t|g|t|g|c|t|g|g|t|g|a|c|c|g|t|t|t|t|g|ei
g|g|c|t|g|a|g|g|c|a|g|g|a|g|a|c|t|c|a|c|t|t|g|a|c|t|g|g|g|a|g|g|c|g|g|a|g|g|t|t|g|c|a|a|t|g|a|g|c|t|g|a|g|a|t|c|g|c|ei
g|g|g|c|t|t|c|t|c|c|a|g|t|t|g|c|t|a|g|c|t|t|t|a|t|t|t|c|t|t|a|g|c|c|c|t|g|t|g|c|a|g|a|g|c|c|c|g|a|g|t|g|c|g|c|g|c|t|ei
g|c|t|c|g|c|c|a|g|t|g|a|a|a|t|g|a|t|g|g|c|t|t|t|a|c|a|g|g|t|c|a|g|t|g|g|a|g|a|c|g|c|t|g|a|g|a|c|c|a|g|t|a|a|c|a|t|g|ei
g|c|a|a|a|c|a|c|t|c|t|g|t|g|t|g|g|c|t|c|c|t|c|g|t|t|t|g|g|t|a|a|g|t|g|a|g|c|t|g|c|c|a|g|c|t|t|c|c|c|c|a|g|g|c|a|g|a|ei
a|t|t|t|t|t|g|c|t|g|g|c|c|t|g|g|a|c|c|t|t|c|c|t|c|a|c|c|t|t|c|a|c|t|g|a|a|a|c|c|a|c|c|c|t|g|t|a|c|c|g|g|a|t|a|c|t|g|ei
a|g|c|a|g|g|c|c|a|c|g|c|t|c|a|g|g|c|c|c|g|g|c|t|c|g|g|g|c|c|a|c|c|a|a|g|t|t|c|t|g|g|a|a|a|c|c|a|c|g|t|g|g|t|g|t|c|c|ei
g|c|c|c|c|g|c|g|c|c|t|a|c|t|g|a|g|t|g|c|t|c|a|t|a|a|t|g|g|a|a|g|c|a|g|c|t|t|t|g|t|a|c|g|c|c|a|g|c|g|t|t|a|t|g|g|t|g|ei
a|g|t|t|t|g|a|g|a|c|c|a|g|a|c|t|g|a|g|c|a|a|c|c|g|t|g|g|g|a|c|c|t|t|g|t|c|t|c|t|a|c|t|a|a|a|a|a|t|c|a|a|a|a|a|c|a|t|ei
a|c|c|c|t|a|c|c|c|t|g|a|t|t|g|t|a|g|g|g|t|c|t|a|t|t|t|c|t|c|a|c|c|g|a|t|a|t|t|a|g|t|c|c|t|a|c|a|c|c|a|a|t|t|g|a|a|g|ei
g|a|t|g|g|a|a|t|g|a|a|c|c|t|g|t|g|t|a|t|g|g|c|g|a|a|t|a|c|a|g|g|a|c|a|c|t|t|c|t|c|a|g|g|a|g|t|a|a|t|g|a|c|a|a|t|t|t|ei
g|g|g|a|c|g|a|c|c|t|c|c|t|g|c|a|g|t|g|t|c|a|c|c|g|c|a|g|g|t|g|a|g|a|a|g|c|c|c|c|c|a|a|t|a|c|a|t|c|g|c|c|c|a|g|g|a|a|ei
t|g|c|g|a|c|a|c|c|c|t|c|c|c|g|c|c|c|t|c|t|c|g|c|g|c|a|g|g|g|c|g|c|t|g|a|t|g|g|a|c|g|a|g|a|c|c|a|t|g|a|a|g|g|a|g|t|t|ei
t|t|g|g|t|c|c|a|c|c|a|c|t|c|a|c|t|g|t|t|t|t|g|t|c|c|a|g|g|a|g|g|a|g|a|g|g|g|a|t|c|g|c|c|c|t|c|c|c|a|g|c|t|a|a|c|a|c|ei
a|g|a|c|a|g|c|a|a|a|t|t|c|c|c|t|a|t|t|t|t|a|t|t|t|c|a|g|a|t|t|g|t|c|a|c|t|g|c|t|g|t|t|c|c|a|a|g|g|g|c|a|c|a|c|g|c|a|ei
t|a|g|a|a|g|a|g|c|t|g|g|g|a|a|t|t|g|a|a|c|t|a|a|c|c|c|a|g|a|g|g|t|a|g|a|a|t|t|c|c|a|g|t|c|a|a|t|a|c|c|a|g|a|t|t|t|c|ei
a|g|t|a|g|c|c|a|a|a|g|a|c|c|a|t|c|a|g|c|g|t|t|c|t|t|t|a|t|g|t|g|t|g|a|g|a|a|t|t|g|a|a|a|t|g|a|c|t|a|g|c|a|t|t|a|t|t|ei
g|c|c|c|t|c|a|a|a|t|g|a|c|c|t|c|a|c|c|t|t|c|t|t|c|t|a|g|g|t|g|a|t|t|c|t|c|g|g|g|c|c|g|a|t|g|t|t|c|t|c|a|g|g|a|a|a|a|ei
g|c|c|c|t|g|g|c|a|c|c|c|a|g|c|a|c|a|a|t|g|a|a|a|c|a|a|g|g|t|g|g|g|t|g|t|c|t|t|t|c|c|t|g|c|c|t|g|a|g|c|t|g|a|c|c|t|g|ei
g|g|c|a|g|a|c|a|g|g|t|g|g|g|a|g|a|t|g|g|a|g|g|a|g|g|c|t|g|g|c|t|g|g|a|g|g|a|a|g|g|a|a|a|c|a|a|c|a|a|a|g|g|a|a|g|t|g|ei
g|a|c|a|a|c|g|a|t|a|c|c|t|t|c|t|a|c|g|a|c|c|t|g|c|t|t|g|a|t|g|g|g|c|t|a|t|g|t|c|a|g|t|g|g|c|t|t|c|g|g|g|g|t|c|a|t|g|ei
t|g|t|a|a|a|t|g|c|a|a|a|c|c|a|t|c|t|a|a|t|a|g|c|g|c|g|a|g|a|c|c|c|t|a|t|a|g|c|c|c|t|g|c|t|g|c|t|t|a|a|t|g|g|g|g|g|c|ei
t|c|t|g|c|a|a|g|t|g|g|a|c|a|t|t|t|g|a|a|g|c|a|t|t|g|a|g|g|c|c|t|a|t|t|g|t|t|g|a|a|a|a|g|g|a|a|a|c|a|t|c|t|t|c|a|t|a|ei
g|a|t|t|c|a|g|a|a|g|a|g|g|a|g|c|c|a|g|a|t|c|t|a|c|a|a|g|g|t|c|g|g|g|t|g|a|a|g|c|t|g|a|g|g|g|g|t|g|c|a|t|g|g|g|g|t|c|ei
t|a|t|a|t|t|a|a|a|g|g|c|t|t|c|c|c|a|a|c|t|g|a|g|a|a|c|t|c|t|t|g|a|t|g|a|c|a|t|a|a|a|a|g|a|a|t|g|g|t|t|a|g|a|a|g|a|t|ei
t|t|c|g|c|c|a|a|g|c|g|t|t|g|g|a|t|t|g|t|t|c|a|c|a|c|t|a|a|t|a|g|g|g|a|a|c|g|t|g|a|g|c|t|g|g|g|t|t|t|a|g|a|c|c|g|t|c|ei
g|a|t|g|t|t|a|a|c|c|a|t|t|c|t|c|c|t|t|c|t|c|c|c|a|c|a|g|t|t|c|c|c|c|a|g|g|g|a|c|c|t|c|t|c|t|c|t|a|a|t|c|a|g|c|c|c|t|ei
a|a|t|g|c|c|t|g|c|g|g|a|g|t|t|g|t|g|c|a|c|g|t|g|a|g|g|g|t|c|a|g|g|c|c|a|c|g|g|c|a|g|c|c|t|a|c|c|g|g|c|a|a|t|t|t|c|c|ei
c|c|c|g|c|t|c|g|g|g|t|a|t|g|a|a|g|a|t|c|g|g|g|g|a|t|t|g|g|t|a|a|g|t|g|c|c|c|c|c|c|t|c|t|a|g|c|t|a|a|t|g|c|t|t|g|g|g|ei
a|a|c|t|c|c|a|c|a|g|t|c|c|c|c|c|g|c|t|g|c|g|g|a|c|c|a|t|g|g|a|c|a|a|a|a|c|t|g|c|t|t|c|a|c|t|c|t|a|c|t|a|a|a|a|a|g|t|ei
a|t|c|g|c|a|t|a|t|c|c|t|g|a|c|c|t|c|t|a|t|c|a|c|t|c|a|g|g|a|a|a|g|t|c|a|g|t|g|g|g|a|g|t|g|g|t|a|a|c|c|a|c|c|a|c|a|c|ei
t|a|a|a|t|g|t|g|t|t|t|c|c|t|g|c|a|t|a|c|a|g|t|a|a|g|t|t|g|c|c|a|c|t|t|c|t|t|t|t|t|c|t|t|c|a|t|a|t|c|a|t|c|g|a|t|c|t|ei
a|g|t|a|t|t|t|c|t|a|a|a|c|a|t|g|t|c|g|c|a|c|t|t|t|c|c|a|c|a|g|g|c|a|t|g|t|g|g|t|t|t|t|g|a|c|c|t|t|t|t|t|t|t|c|a|a|t|ei
g|c|t|c|g|a|c|g|a|c|c|t|g|c|a|g|c|g|g|c|t|c|a|g|c|c|a|a|g|t|g|a|g|g|g|c|c|c|g|g|c|a|c|c|c|c|a|g|a|c|t|c|c|t|c|t|t|t|ei
g|a|g|c|a|g|c|c|a|g|t|g|c|t|c|c|a|a|g|c|c|c|a|t|t|c|a|t|g|t|a|a|g|t|g|c|c|a|g|t|c|t|t|c|c|t|g|c|t|c|a|c|c|t|c|t|a|g|ei
c|t|g|c|c|a|t|a|g|t|c|a|g|a|c|t|t|c|a|g|a|c|t|t|a|a|g|a|t|t|a|t|t|c|t|a|a|a|t|c|a|c|c|a|g|a|a|a|a|t|t|a|a|t|t|t|c|a|ei
t|g|g|c|g|a|c|t|a|c|g|g|c|g|c|g|g|a|g|g|c|c|c|g|a|g|a|g|g|t|g|a|g|g|a|c|c|c|t|c|c|t|g|t|c|c|c|t|g|c|t|c|c|a|g|t|c|c|ei
a|t|c|a|a|g|a|c|c|a|t|c|g|a|g|a|c|a|c|g|g|g|a|g|g|g|a|g|g|t|a|a|g|t|g|g|t|c|t|g|t|c|t|g|g|g|c|t|c|c|t|t|a|c|c|c|t|t|ei
g|a|t|c|c|c|c|c|t|g|a|c|c|c|a|g|c|a|c|c|c|c|c|c|g|c|a|g|g|t|g|c|c|g|t|g|c|c|c|c|t|c|a|t|c|c|a|g|t|c|t|c|g|g|a|t|t|g|ei
t|t|g|a|a|c|t|c|t|c|t|g|a|g|a|t|a|a|a|c|g|g|a|a|g|c|a|g|g|g|t|c|a|a|a|c|t|a|c|a|t|a|a|a|t|g|c|c|a|g|c|t|a|t|a|t|t|g|ei
a|c|a|t|a|g|g|a|g|g|g|c|c|c|g|a|g|c|a|g|g|a|a|t|g|g|t|g|t|g|g|a|c|a|t|a|g|g|g|c|c|g|g|t|c|t|g|c|t|t|c|t|t|g|t|a|a|a|ei
c|a|c|a|g|c|c|t|t|t|g|t|g|t|c|c|a|a|g|c|a|g|g|g|g|c|a|g|c|g|a|g|g|t|a|g|t|g|a|a|g|a|g|a|c|c|c|a|g|g|c|g|c|t|a|c|c|t|ei
c|a|a|g|c|c|a|c|t|g|t|g|a|g|c|t|g|g|a|c|c|t|g|c|g|a|g|g|g|t|g|a|g|t|g|t|g|g|g|t|t|t|g|t|g|t|g|c|c|t|t|g|t|g|g|g|t|t|ei
t|c|t|c|t|c|t|g|c|c|g|c|c|c|a|c|t|g|c|t|t|c|c|g|a|g|a|g|g|t|a|g|g|g|g|c|t|c|g|g|a|a|a|c|c|c|a|g|t|t|g|g|t|t|t|t|t|c|ei
c|c|a|a|t|g|g|a|a|g|c|a|g|c|t|g|g|c|t|t|c|a|c|g|t|c|a|g|g|t|a|a|c|a|a|t|t|t|a|a|a|g|t|a|a|c|a|t|t|a|a|c|t|t|a|t|t|g|ei
t|a|c|t|c|t|t|g|c|g|t|t|t|t|c|t|g|t|c|t|g|c|c|c|c|c|a|g|c|a|c|t|c|t|g|g|c|g|c|t|t|a|c|a|g|a|a|t|g|a|a|g|a|t|c|t|a|c|ei
t|a|a|c|c|a|t|c|t|c|t|c|c|c|t|c|t|t|a|a|c|t|c|c|t|t|a|g|g|t|a|t|t|t|g|c|t|g|a|c|c|t|g|t|t|t|g|a|c|c|c|t|g|t|g|a|t|c|ei
a|a|g|c|t|g|c|a|t|g|t|g|g|a|t|c|c|t|g|a|g|a|a|t|c|a|a|g|g|t|g|a|g|t|c|c|a|g|g|a|g|a|t|g|t|t|t|c|a|g|c|c|c|t|g|t|t|g|ei
g|c|a|g|a|g|a|a|c|a|a|t|t|t|g|g|c|t|g|c|c|t|t|c|a|g|c|g|g|t|g|a|g|t|g|c|c|c|t|t|c|t|t|t|t|c|c|c|c|t|t|g|c|a|t|g|g|c|ei
g|g|c|t|c|a|c|a|g|c|g|c|g|c|c|c|g|g|c|t|a|t|t|t|g|c|a|g|c|t|c|a|c|c|a|t|g|g|a|t|g|a|t|g|a|t|a|t|c|g|c|c|g|c|g|c|t|c|ie
c|a|t|c|t|t|t|g|t|t|g|t|c|t|c|t|t|t|c|c|a|t|c|c|a|c|a|g|c|t|c|c|t|g|g|g|a|a|a|t|g|t|g|c|t|g|g|t|g|a|c|c|g|t|t|t|t|g|ei
g|a|a|c|a|c|t|g|c|a|t|a|g|a|a|a|t|g|a|a|t|a|t|g|a|t|a|g|g|t|g|a|g|a|t|a|t|t|t|t|g|t|g|t|t|t|t|t|c|t|t|g|t|c|t|t|t|t|ei
c|a|g|a|a|a|a|c|c|a|g|a|a|g|t|c|c|t|g|t|g|a|a|c|g|c|a|g|g|t|c|a|t|a|a|t|c|t|g|a|a|t|a|a|g|a|t|t|t|t|t|t|a|a|a|g|a|a|ei
g|c|t|c|t|c|c|c|t|g|c|t|t|c|a|g|g|a|g|c|g|g|t|g|g|g|g|c|c|t|g|t|g|g|c|c|t|g|g|a|g|g|a|g|g|a|g|g|c|a|c|c|a|g|c|t|t|g|ei
c|t|g|g|g|a|g|c|g|c|t|c|t|t|t|g|g|a|t|c|c|c|a|c|c|t|c|a|g|g|c|t|g|g|c|c|a|g|a|g|t|c|c|c|t|g|g|c|a|g|c|t|g|a|g|g|g|a|ei
t|t|c|t|g|g|a|g|g|c|a|g|t|a|c|c|a|g|c|a|t|g|g|t|c|a|g|c|a|t|c|t|g|c|t|t|c|c|g|g|t|g|c|g|g|g|c|c|t|c|a|g|g|a|a|c|c|t|ei
c|t|g|t|c|c|c|t|t|g|g|g|c|t|g|t|t|t|t|c|c|t|a|c|t|c|a|g|g|c|t|g|c|t|g|g|t|g|g|t|c|t|a|c|c|c|t|t|g|g|a|c|c|c|a|g|a|g|ei
g|g|a|g|g|c|a|g|g|a|a|t|g|c|a|g|c|a|t|c|c|c|t|t|t|g|t|g|g|t|a|g|g|c|t|g|g|g|g|g|c|a|g|t|g|g|g|g|c|g|a|c|c|c|a|t|g|a|ei
t|g|g|g|c|g|c|t|t|c|a|c|g|g|a|a|c|t|c|g|c|a|t|t|c|c|a|g|t|c|t|t|c|g|t|a|a|c|c|c|a|g|g|a|g|g|a|a|g|c|c|c|a|c|g|g|c|g|ei
c|c|g|g|g|t|t|c|t|a|g|c|t|g|c|c|c|t|t|c|t|c|t|c|g|t|a|g|g|a|g|a|a|c|g|c|c|a|a|g|a|a|c|g|a|a|g|a|g|a|t|t|c|t|g|a|a|t|ei
a|t|c|a|a|g|t|c|a|g|a|c|g|t|g|t|g|g|t|c|c|t|t|g|g|a|t|c|c|t|g|c|t|c|a|c|t|g|a|g|c|t|c|a|t|c|a|c|c|a|a|g|g|g|c|c|g|a|ei
c|a|c|t|t|g|a|g|c|c|c|a|g|g|a|g|t|t|g|g|a|g|g|t|c|a|g|t|a|a|t|c|t|a|c|g|a|t|t|a|t|g|c|c|a|c|t|g|c|a|t|t|t|c|a|a|c|c|ei
c|a|t|g|a|c|c|t|t|t|g|a|c|c|t|c|a|c|c|a|a|g|a|c|c|a|a|a|g|t|a|t|g|g|g|g|t|t|g|g|c|c|t|a|g|c|c|c|t|t|g|a|c|c|c|a|g|t|ei
c|a|t|c|t|t|t|a|t|t|g|t|c|t|c|c|t|t|t|c|a|t|c|c|a|c|a|g|c|t|c|c|t|g|g|g|a|a|a|t|g|t|g|c|t|g|g|t|g|a|c|c|g|t|t|t|t|g|ei
g|a|g|c|t|c|t|g|c|a|g|g|c|t|g|a|a|g|a|t|g|t|c|c|g|c|t|g|t|c|a|g|c|g|g|g|a|t|g|g|g|g|g|c|a|c|g|c|t|t|g|c|t|g|a|c|g|c|ei
g|g|a|c|g|g|g|g|c|t|g|a|c|c|a|c|g|g|g|g|g|c|g|g|c|c|a|g|g|g|t|c|t|c|a|c|a|c|c|c|t|c|c|a|g|t|g|g|a|t|g|t|g|t|g|g|c|t|ei
g|a|c|a|t|c|a|a|c|t|t|c|c|t|c|a|t|c|a|a|c|a|a|a|g|c|a|g|g|t|a|g|g|c|t|g|c|a|g|g|g|g|g|a|g|c|c|c|a|t|g|g|g|a|a|a|g|a|ei
g|c|t|t|g|g|a|t|g|a|g|c|c|t|c|t|t|c|t|c|a|a|g|a|t|g|g|g|g|t|a|t|g|g|a|c|c|a|a|c|a|c|t|c|a|a|t|c|t|c|c|t|t|t|a|t|t|t|ei
t|c|t|g|a|t|g|c|c|c|g|c|t|g|t|g|t|t|t|t|t|g|a|a|g|g|g|g|g|t|g|a|g|t|a|t|a|c|g|t|g|a|c|c|c|t|g|t|t|a|g|g|g|a|a|g|g|g|ei
t|t|t|t|t|c|t|t|c|t|a|g|a|a|t|g|t|c|t|t|g|a|t|g|g|g|a|a|g|t|a|a|g|t|t|c|a|c|a|t|t|t|a|c|t|t|t|t|a|a|t|a|t|a|a|c|a|t|ei
c|a|c|g|t|c|c|c|c|g|a|g|g|c|t|g|c|c|t|g|t|c|t|c|a|g|t|t|g|a|c|t|t|t|g|c|a|c|c|t|g|t|c|t|t|c|a|g|g|c|t|g|c|c|a|g|g|g|ei
c|a|g|c|t|t|t|c|t|c|t|a|a|t|a|a|g|a|a|a|g|c|t|t|t|c|c|t|g|c|c|a|c|c|g|t|a|t|a|g|g|t|c|a|c|c|t|t|c|t|t|a|t|t|g|g|t|a|ei
g|c|t|a|t|t|g|g|a|g|g|a|t|c|t|t|g|a|a|a|g|g|c|g|t|g|t|t|a|t|c|c|t|t|c|t|g|t|g|g|a|c|a|a|c|a|a|c|a|g|c|a|a|a|a|t|g|t|ei
a|g|g|a|g|g|a|a|c|c|c|a|t|c|g|a|t|c|t|g|t|c|t|t|g|c|a|g|a|t|g|g|g|a|a|a|c|g|a|c|t|c|t|c|g|g|a|t|t|a|t|a|g|c|a|t|c|g|ei
c|c|c|t|g|c|t|c|c|c|a|a|t|c|c|c|t|a|t|c|t|c|c|c|c|t|a|g|g|a|t|a|g|c|c|g|c|t|t|c|c|c|a|a|a|g|a|t|c|c|t|g|g|a|g|a|a|c|ei
t|g|g|a|g|a|c|t|c|a|c|t|a|c|c|a|t|c|c|a|c|t|c|c|g|c|a|g|t|g|a|c|t|c|g|c|g|g|g|g|a|t|g|t|g|t|t|c|a|c|t|a|t|g|c|c|g|g|ei
a|a|c|c|t|a|g|a|g|g|c|c|a|a|g|g|t|t|c|a|a|g|t|t|c|c|c|a|t|c|t|c|c|a|g|t|a|g|c|c|t|a|g|c|a|a|t|a|t|t|t|g|c|a|a|c|a|t|ei
g|g|g|a|c|g|g|g|c|t|g|a|c|c|a|c|g|g|g|g|g|c|g|g|c|c|a|g|g|g|t|c|t|c|a|c|a|c|c|c|t|c|c|a|g|a|g|g|a|t|g|t|a|c|g|g|c|t|ei
t|t|c|a|g|a|a|g|c|t|g|t|t|c|t|g|g|a|t|t|t|c|t|a|a|g|t|g|g|t|g|a|g|t|g|g|a|t|g|a|t|c|a|c|c|a|c|c|a|g|t|c|c|t|g|c|c|t|ei
c|c|t|a|a|a|t|g|t|c|g|g|c|g|t|c|t|t|t|g|g|t|g|c|t|c|a|g|t|g|c|a|c|a|c|g|a|g|g|g|g|g|c|t|g|g|a|c|t|t|c|g|c|c|t|g|t|g|ei
a|c|c|t|c|t|a|c|c|a|g|a|t|c|a|t|c|c|t|c|a|a|g|c|c|t|g|g|a|g|c|g|g|g|g|c|t|c|c|c|t|g|c|t|g|g|g|c|t|g|c|t|c|c|a|t|a|g|ei
a|c|t|c|t|t|a|c|a|c|a|g|c|c|g|c|c|a|a|t|a|a|g|a|a|a|a|g|g|t|a|a|g|a|g|t|c|a|c|t|t|g|t|t|a|a|a|t|a|a|a|a|c|a|a|c|a|c|ei
c|t|g|a|g|a|g|g|a|c|c|a|t|c|a|t|t|g|t|g|t|c|c|t|t|g|g|g|c|c|a|a|g|a|t|c|t|c|c|a|c|g|c|a|g|g|c|c|g|a|c|a|c|c|a|t|c|g|ei
g|g|a|a|g|a|c|a|a|a|g|t|g|a|g|a|t|c|c|t|t|t|c|c|a|a|a|a|a|a|a|a|a|a|a|a|a|a|c|t|t|t|g|g|g|t|g|g|a|a|g|g|t|g|g|g|g|t|ei
t|c|c|c|c|c|a|c|t|c|c|t|c|t|t|a|t|t|t|g|c|t|c|c|c|g|g|g|g|t|a|t|t|t|t|a|g|g|c|a|g|g|g|a|t|t|t|g|a|g|g|a|g|c|a|g|c|t|ei
g|a|g|g|a|g|c|t|a|c|g|c|c|a|c|c|t|g|t|g|g|g|a|c|g|c|t|g|t|t|a|g|a|g|c|t|g|a|c|c|c|t|g|g|a|g|a|a|g|g|g|t|g|a|c|c|a|g|ei
c|c|t|g|g|g|g|t|g|c|c|t|t|g|g|g|t|c|a|g|g|a|c|t|a|a|c|t|t|g|g|a|c|a|t|t|c|c|t|a|g|t|t|t|t|c|a|a|a|t|g|a|g|t|g|a|t|g|ei
g|c|c|g|c|c|t|a|a|c|a|c|t|t|t|g|a|g|c|a|g|a|t|t|a|g|c|c|t|t|a|c|a|c|a|g|g|a|t|t|a|t|g|a|a|g|t|c|t|g|a|a|a|g|g|a|t|t|ei
t|c|t|g|c|g|a|g|g|a|a|a|g|g|g|a|a|g|g|a|g|c|a|g|c|g|t|g|g|t|a|g|g|t|c|g|g|g|t|t|t|c|t|g|t|a|c|c|t|t|g|g|g|g|t|c|t|g|ei
c|a|g|a|c|t|g|g|g|t|g|g|a|c|a|a|c|a|a|a|a|c|c|t|a|g|c|g|g|t|a|a|g|a|g|a|g|g|g|c|c|a|a|g|c|t|c|a|g|a|g|a|c|c|a|c|a|g|ei
t|g|c|c|c|a|c|a|a|g|c|a|g|a|c|a|g|a|c|t|t|t|t|c|t|c|a|g|g|g|g|a|g|a|t|c|a|t|c|g|g|g|g|g|a|c|a|t|g|a|g|g|c|c|a|a|g|c|ei
c|c|c|a|t|c|g|a|g|a|g|g|g|t|c|a|a|a|c|t|g|c|t|c|g|c|a|g|g|t|g|a|g|g|a|c|c|g|c|g|c|g|g|t|g|c|a|a|g|a|g|g|c|g|g|g|c|g|ei
c|a|g|a|c|t|g|g|g|t|c|t|a|c|a|a|c|a|a|a|a|c|t|t|g|g|c|g|g|t|a|a|g|a|g|a|g|g|g|c|c|a|a|g|c|t|c|a|g|a|g|a|c|c|a|c|a|g|ei
c|c|c|t|c|c|a|t|c|g|t|g|g|g|g|c|g|c|c|c|c|a|g|c|c|c|a|g|g|t|a|g|g|g|g|a|g|c|t|g|g|c|t|g|g|g|t|g|g|g|g|c|a|g|c|c|c|c|ei
a|g|a|t|a|c|a|c|g|t|g|c|c|a|t|g|t|g|c|a|g|c|a|g|g|g|g|g|c|t|g|c|c|g|g|a|g|c|c|c|c|t|c|a|c|c|c|t|g|a|g|a|t|g|g|g|a|g|ei
c|c|a|t|c|g|a|g|a|a|g|c|t|c|g|c|g|g|t|g|g|a|a|c|c|t|g|t|c|c|a|g|c|c|t|g|g|a|c|g|g|c|g|a|c|c|t|g|g|c|g|g|g|c|c|g|a|t|ei
c|a|t|c|g|c|a|t|g|g|a|c|c|g|c|a|g|g|a|g|g|g|c|g|t|t|c|g|g|a|c|c|a|c|t|a|g|g|c|c|t|g|a|a|a|t|g|a|c|a|t|t|t|c|a|c|t|a|ei
t|g|g|g|a|a|a|t|g|t|t|a|c|a|t|c|a|t|t|c|a|c|a|a|t|g|t|c|a|c|a|t|t|a|a|a|a|a|t|t|g|c|t|a|t|g|t|t|g|a|a|a|t|t|t|c|a|g|ei
c|c|c|t|c|a|c|t|c|t|a|t|t|c|a|a|t|g|t|c|a|c|a|g|a|a|t|g|a|c|g|c|a|a|g|a|g|c|c|t|a|t|g|t|a|t|g|t|g|g|a|a|t|c|c|a|g|a|ei
a|g|g|g|g|g|t|c|c|c|t|g|a|g|c|c|c|t|g|t|c|c|t|c|g|c|a|g|g|a|t|t|c|c|t|a|c|c|g|g|a|a|g|c|a|g|g|t|g|g|t|c|a|t|t|g|a|t|ei
c|t|g|t|g|a|t|g|t|c|a|t|c|a|t|c|c|c|a|c|c|c|c|t|c|c|a|g|g|t|g|g|t|c|c|t|g|c|t|g|g|a|c|t|c|a|a|a|g|a|a|g|a|a|g|c|t|g|ei
t|c|t|g|g|g|g|g|g|g|t|c|a|g|a|a|c|c|c|a|g|a|g|c|t|c|c|a|g|c|t|g|g|a|g|c|c|c|t|g|a|g|t|g|g|c|t|g|a|g|c|t|c|a|g|g|c|c|ei
t|a|c|c|a|c|a|t|c|t|a|c|t|c|c|a|g|c|g|a|c|c|c|c|t|t|t|t|g|a|a|g|t|t|c|g|t|g|g|t|g|c|c|a|a|t|c|a|g|t|g|g|a|t|c|a|a|g|ei
g|g|a|g|t|g|g|g|g|g|c|g|g|t|g|c|g|t|c|c|t|c|c|g|c|g|g|c|a|g|c|g|g|t|g|g|c|c|a|c|a|g|c|t|c|t|c|c|t|c|c|c|g|c|c|g|c|c|ei
g|c|t|g|g|g|g|a|g|a|a|a|c|c|c|a|a|g|g|t|a|c|c|a|g|g|g|g|c|t|g|g|c|c|t|t|c|t|c|a|a|g|g|a|a|g|c|c|c|g|g|c|t|c|c|c|c|g|ei
c|t|a|g|a|g|g|a|a|g|g|c|a|t|c|c|a|a|a|c|g|c|t|a|g|g|g|g|g|t|g|a|g|g|g|t|g|g|c|g|c|c|a|g|g|g|g|t|c|a|c|c|a|a|t|c|t|t|ei
a|t|g|t|c|c|c|a|g|c|a|a|c|a|c|a|c|a|c|t|g|c|c|g|g|a|c|c|c|t|c|t|c|c|c|c|t|g|c|c|c|t|c|a|g|t|c|a|g|g|a|g|c|t|c|c|t|c|ei
a|g|c|g|c|t|c|c|a|a|c|t|a|t|a|c|t|c|c|g|a|t|c|c|a|a|t|g|g|t|a|c|c|t|c|c|c|t|c|t|c|t|g|c|t|g|c|a|c|t|c|c|t|g|g|a|c|a|ei
c|a|t|c|t|t|t|g|t|t|t|t|c|t|c|c|t|t|t|c|a|t|c|c|a|c|a|g|c|t|c|c|t|g|g|g|a|a|a|t|g|t|g|c|t|g|g|t|g|a|c|c|g|t|t|t|t|g|ei
a|a|c|c|c|c|c|t|a|a|t|t|a|a|t|c|t|t|c|t|t|t|a|a|g|t|t|c|t|g|a|t|t|c|t|t|a|t|g|t|g|c|c|a|t|a|a|t|g|a|a|t|t|t|t|t|t|t|ei
t|c|a|a|a|t|g|c|t|c|g|c|a|t|c|c|t|g|c|a|g|t|a|c|g|a|g|t|t|t|a|c|t|g|t|t|a|g|a|t|t|g|g|c|c|t|c|g|t|t|t|a|a|c|t|t|t|c|ei
g|c|a|c|a|c|g|g|a|t|g|c|c|a|t|g|a|t|c|a|t|c|g|c|t|g|a|g|g|t|c|a|g|t|g|g|c|c|a|g|g|g|g|t|c|a|g|t|g|c|t|t|c|c|t|a|g|c|ei
g|t|g|a|g|t|c|a|c|c|t|g|t|g|a|c|c|a|c|t|c|t|t|t|t|c|a|g|g|a|t|g|a|t|a|a|g|g|a|t|g|c|c|t|t|c|t|a|t|g|t|g|g|c|a|g|a|c|ei
g|a|c|c|c|a|a|g|c|a|g|c|t|g|g|a|g|g|c|t|c|t|g|g|g|t|g|g|g|t|g|a|g|t|t|t|a|g|c|c|c|c|a|t|c|c|c|c|t|a|g|g|t|g|t|t|c|t|ei
a|a|a|a|g|g|a|a|a|t|a|t|c|c|t|c|a|g|a|t|g|a|a|t|t|g|g|a|a|a|g|a|a|g|c|t|t|t|c|t|g|a|g|a|a|a|c|t|g|c|t|t|a|g|t|g|t|t|ei
g|t|t|a|a|t|t|t|c|t|a|t|g|c|c|t|g|g|a|a|g|a|g|a|g|g|a|g|g|t|g|a|g|t|t|c|c|t|t|t|t|t|t|t|t|t|t|t|t|t|t|t|c|c|t|t|t|c|ei
c|a|c|t|c|a|g|t|a|t|g|t|c|t|g|c|a|g|a|t|g|t|a|c|c|t|t|g|g|t|a|a|g|a|t|a|a|t|a|a|a|t|t|t|g|a|a|c|c|t|t|g|t|t|t|t|g|a|ei
a|c|a|g|c|t|c|c|a|g|a|a|g|t|t|g|a|a|a|a|t|g|c|a|t|a|g|a|g|t|a|c|c|a|g|g|a|a|a|c|a|g|g|a|g|t|t|t|c|t|t|t|t|c|c|c|t|c|ei
t|g|t|t|c|t|t|t|c|c|c|g|g|a|a|g|a|g|c|t|g|g|g|g|g|g|g|g|a|g|c|t|g|a|g|g|g|g|g|c|c|c|a|g|g|c|c|t|c|a|g|c|c|c|t|g|g|t|ei
t|t|t|t|a|g|a|c|a|t|t|a|c|a|c|c|a|a|a|a|g|c|a|a|g|c|c|g|t|a|a|a|a|g|a|a|a|a|a|a|t|a|g|a|t|a|a|a|t|t|g|g|t|g|g|a|t|t|ei
c|t|g|t|c|c|t|g|t|g|g|g|t|t|c|c|t|c|t|c|a|c|c|c|t|c|a|g|g|c|t|g|c|t|g|g|t|c|g|t|c|t|a|c|c|c|a|t|g|g|a|c|c|c|a|g|a|g|ei
a|a|t|t|g|t|c|t|g|t|g|g|t|t|t|a|a|g|a|a|c|a|c|t|t|a|a|g|c|a|g|t|t|t|t|c|c|g|c|c|c|t|g|g|g|t|g|g|g|c|c|a|g|g|t|g|t|t|ei
c|c|a|t|g|t|t|g|t|c|t|g|c|c|a|t|t|c|t|g|g|c|c|t|c|c|a|g|a|a|c|a|t|c|a|a|t|g|c|g|g|c|c|a|a|a|t|c|t|a|g|t|t|t|c|c|t|c|ei
g|g|t|t|c|t|c|t|t|g|g|g|c|t|c|t|a|g|g|t|c|c|t|g|g|a|a|t|g|t|t|g|t|g|a|g|g|g|g|t|t|t|a|t|t|t|t|t|t|t|t|t|a|a|t|a|g|t|ei
c|g|g|g|g|t|t|t|a|t|g|a|a|t|g|g|g|t|g|g|g|c|g|t|g|c|a|g|g|t|g|g|g|c|c|t|g|g|c|t|c|a|g|g|g|a|a|g|g|g|c|a|c|c|c|a|g|t|ei
g|a|c|t|a|c|g|c|c|c|g|c|c|t|c|c|c|g|c|a|g|a|c|a|g|t|t|c|c|a|t|g|t|t|t|c|t|t|t|t|a|g|g|t|a|t|a|t|c|t|t|t|g|g|a|c|t|t|ei
g|a|g|c|a|g|t|t|c|a|c|g|g|c|c|a|t|g|t|t|c|c|g|c|c|a|a|g|g|c|c|t|t|c|t|t|g|c|a|c|t|g|g|t|a|c|a|c|g|g|g|c|g|a|g|g|g|c|ei
c|t|g|a|a|g|g|a|a|c|g|g|g|t|a|g|g|g|c|c|a|g|g|c|g|c|a|g|c|t|c|c|t|g|a|g|g|c|a|c|t|g|c|c|t|g|c|t|g|g|t|g|a|c|c|c|t|g|ei
c|c|c|a|c|c|g|t|g|c|t|g|c|t|g|g|g|a|c|c|t|g|c|g|t|g|t|a|g|a|g|a|g|g|g|g|g|g|c|c|c|t|g|a|c|g|c|g|c|a|g|a|c|c|c|a|g|t|ei
c|t|g|c|c|c|c|t|g|c|c|t|t|t|g|g|c|c|c|t|c|t|a|c|a|c|a|g|g|g|a|t|g|a|t|c|c|a|g|g|c|a|c|t|g|g|g|t|g|g|c|t|t|c|t|t|c|a|ei
c|c|a|g|g|g|g|t|c|t|g|a|g|t|c|t|c|a|c|a|g|c|t|g|a|a|a|g|g|t|g|a|g|a|t|t|c|t|g|g|g|g|g|t|c|t|g|a|a|g|t|g|g|g|t|g|g|a|ei
t|g|a|c|a|a|t|a|g|c|c|c|t|g|t|g|c|t|g|c|a|g|g|a|g|g|g|t|a|a|c|t|g|c|c|a|c|t|g|a|c|a|t|c|a|g|a|g|t|a|a|c|t|c|t|t|a|a|ei
t|g|a|a|t|t|t|g|t|t|c|a|t|g|a|a|t|a|t|t|t|t|t|c|a|t|a|g|t|g|t|g|a|g|a|c|a|g|c|t|g|c|c|t|t|g|t|g|t|g|g|g|a|c|t|g|a|g|ei
g|g|g|c|a|g|t|g|c|g|g|c|a|a|c|c|a|a|a|t|c|g|g|g|c|a|a|g|g|t|a|a|g|t|t|g|c|c|g|g|g|g|c|g|c|t|g|g|g|g|c|c|a|g|g|c|g|g|ei
g|g|t|g|g|a|t|t|t|a|a|c|a|t|t|t|c|t|t|t|t|t|a|t|c|c|a|g|a|t|t|t|t|c|c|c|c|a|a|c|a|a|a|a|c|c|c|t|g|g|a|a|a|a|a|t|t|a|ei
a|g|g|a|g|g|a|c|a|c|c|t|t|g|a|c|t|t|t|g|t|g|c|g|g|g|c|t|g|c|t|t|g|c|t|c|a|g|g|g|c|a|t|g|t|t|t|t|t|t|a|c|t|t|g|a|g|a|ei
c|c|t|g|g|t|c|c|c|c|c|t|g|g|c|c|c|t|g|c|t|g|g|g|g|a|a|a|g|g|a|t|c|c|c|c|t|g|g|t|g|c|t|g|a|t|g|g|t|c|c|t|g|c|t|g|g|t|ei
a|c|g|c|c|c|c|a|g|c|c|c|t|c|t|g|a|a|g|g|t|g|c|g|t|c|c|a|g|c|t|g|t|c|c|t|g|g|g|g|g|a|g|g|t|g|g|a|c|a|c|c|t|c|g|t|t|g|ei
t|t|t|c|g|t|g|c|t|t|t|c|t|t|g|c|t|t|t|c|c|c|g|t|t|c|t|t|g|c|t|t|t|c|t|t|t|c|t|t|t|c|t|t|t|c|g|t|t|t|c|t|t|t|c|a|t|g|ei
t|t|g|g|a|g|g|c|c|a|a|g|g|a|g|g|c|c|g|a|g|a|a|a|c|a|c|g|g|t|g|a|g|a|c|c|c|c|t|t|c|c|c|c|a|g|c|a|c|a|t|t|c|c|a|c|a|g|ei
c|a|g|g|g|c|t|t|c|g|a|g|c|t|c|a|t|c|t|a|g|a|t|a|g|a|g|c|t|c|c|a|a|g|c|c|a|c|a|c|t|c|c|a|c|g|a|c|t|t|t|a|g|a|c|a|t|c|ei
g|c|a|g|c|t|t|g|g|a|g|a|g|t|a|c|a|a|a|t|t|c|c|g|a|t|g|c|g|t|a|a|g|t|a|a|t|t|t|t|t|a|t|t|g|a|c|t|g|a|t|t|t|t|t|t|t|t|ei
a|g|t|g|t|g|a|c|a|t|g|g|t|g|c|a|t|c|t|c|t|g|c|t|a|c|a|g|a|t|c|a|t|g|t|t|t|g|a|g|a|c|c|t|t|c|a|a|c|a|c|c|c|c|a|g|c|c|ei
c|t|g|c|t|t|g|a|g|c|c|c|a|g|g|a|g|t|t|t|g|a|g|c|a|g|c|c|t|g|g|g|c|a|a|c|a|a|a|g|t|g|a|g|a|c|t|c|c|a|t|c|t|c|t|a|c|a|ei
c|c|t|g|g|c|c|a|c|c|a|g|c|t|t|c|c|c|t|c|t|g|c|t|a|c|c|c|c|a|g|g|c|c|a|c|c|t|g|t|c|t|t|c|t|c|t|c|c|c|a|c|g|t|g|c|a|c|ei
c|a|a|c|c|t|g|c|t|t|g|a|c|a|a|g|t|t|t|g|a|a|c|c|c|a|g|g|c|a|t|a|c|c|t|c|c|t|g|c|a|c|c|c|c|g|a|g|g|t|g|t|t|c|c|t|c|a|ei
c|t|c|t|g|g|c|t|t|c|t|t|c|c|t|c|c|t|c|a|a|t|c|t|a|c|a|g|a|a|a|a|a|g|g|g|t|g|c|a|g|a|c|g|t|c|t|g|g|t|t|c|a|a|a|g|a|g|ei
a|a|g|g|a|a|a|c|c|t|t|a|a|a|c|t|c|t|c|t|t|a|t|a|t|t|a|g|g|a|a|t|c|c|t|g|a|t|g|g|g|g|a|t|g|c|c|a|a|g|c|c|c|t|g|g|t|g|ei
a|a|c|a|g|g|c|a|t|t|c|c|a|c|a|g|g|c|t|t|t|t|t|t|g|g|a|a|c|c|c|t|t|a|c|t|t|g|a|t|a|g|t|g|c|t|c|t|a|g|g|a|a|a|c|a|c|t|ei
a|a|a|g|a|t|g|c|a|t|a|g|a|a|a|g|a|g|t|a|t|a|a|g|t|t|t|a|a|a|a|c|a|t|a|a|g|g|c|a|t|t|c|a|t|c|t|g|c|c|a|t|t|t|t|t|c|a|ei
g|g|c|c|t|g|t|t|a|g|c|c|c|g|g|c|g|g|g|a|t|g|c|c|a|c|g|t|g|a|a|a|a|g|g|c|t|g|c|c|a|c|t|a|g|a|c|g|t|a|g|a|t|t|g|c|t|g|ei
g|a|t|g|g|c|t|c|a|g|a|a|c|c|t|g|g|t|g|g|a|c|t|g|c|g|a|t|g|t|t|t|t|c|t|g|t|c|t|a|c|a|t|g|a|g|c|a|g|t|a|a|c|c|c|a|g|a|ei
t|c|g|c|t|g|t|g|g|a|t|c|g|g|c|t|a|c|t|c|t|t|t|g|g|a|t|g|c|a|c|a|c|c|a|g|c|g|c|t|g|g|t|g|c|a|g|a|a|g|g|c|t|c|t|g|g|c|ei
t|g|c|c|t|c|c|t|t|t|c|a|c|a|c|t|c|c|t|c|t|t|g|g|c|t|c|g|t|g|a|c|a|t|t|a|c|g|a|a|c|c|c|t|a|a|c|c|c|g|g|g|c|c|c|t|g|c|ei
t|c|t|c|a|c|t|t|c|g|g|g|g|g|a|a|a|a|a|t|a|a|c|g|g|g|t|a|a|g|g|g|c|c|a|t|g|g|c|a|g|g|g|t|g|g|g|a|g|a|g|g|c|g|g|t|g|t|ei
g|c|c|c|c|c|a|c|t|g|t|g|g|a|g|a|t|a|a|g|a|a|g|g|a|t|g|g|a|a|t|g|g|g|g|g|a|a|g|a|g|g|a|g|g|a|g|c|a|g|g|a|g|g|c|c|c|t|ei
g|t|t|t|t|t|a|a|t|a|t|g|c|c|a|c|t|t|t|t|t|c|t|t|t|c|a|g|g|c|a|a|c|t|c|a|t|g|c|a|g|c|a|a|t|t|c|c|a|g|a|a|c|c|c|c|g|a|ei
g|a|a|t|t|c|a|a|t|a|a|g|t|a|t|t|c|t|g|t|a|t|t|t|t|g|t|t|t|g|a|g|a|a|t|c|c|c|a|c|c|t|c|t|t|t|g|t|c|c|a|a|g|t|a|a|g|c|ei
g|t|g|c|g|a|a|a|a|g|a|t|c|t|g|c|a|a|a|a|t|t|t|c|c|a|a|g|g|t|a|g|g|g|c|t|g|g|a|c|t|c|t|g|g|c|a|g|g|t|c|t|g|a|c|c|c|a|ei
g|a|t|c|g|t|g|c|c|a|c|t|g|c|a|c|t|c|c|a|g|c|c|g|g|c|g|a|c|a|g|a|g|t|g|a|g|a|c|t|c|t|g|t|c|t|c|a|a|a|a|a|a|a|a|a|a|a|ei
a|a|a|t|a|a|c|a|a|c|a|a|c|a|g|t|c|t|g|t|a|a|a|c|c|t|g|g|a|t|a|g|g|t|t|t|t|a|a|t|a|a|a|t|t|a|a|c|c|c|a|a|g|t|a|a|a|g|ei
t|g|g|t|g|t|c|c|t|g|a|c|c|a|c|c|c|t|c|c|c|c|t|t|t|t|g|c|a|c|c|c|g|c|c|t|c|t|c|c|c|g|t|c|a|g|g|g|c|c|c|a|a|g|t|c|c|c|ei
g|c|c|t|g|c|t|g|c|t|c|t|g|g|c|c|c|c|t|g|g|t|c|t|t|c|c|t|g|t|t|c|t|c|c|a|g|c|a|t|g|g|t|g|t|g|t|c|t|g|a|g|g|c|t|c|c|c|ei
a|g|c|c|g|t|t|c|g|g|c|t|t|c|t|g|g|g|c|t|c|t|g|c|a|c|a|g|g|g|a|t|g|c|t|g|c|c|t|g|a|c|c|c|c|a|a|g|a|a|c|g|t|g|c|a|c|a|ei
c|c|g|c|c|t|c|t|c|a|t|c|c|a|g|g|a|a|a|t|g|t|t|g|g|a|a|c|t|c|a|g|a|g|g|g|c|c|t|g|g|a|c|a|c|t|c|t|g|a|g|c|g|g|a|c|a|g|ei
a|c|a|g|a|g|g|c|t|g|a|a|c|a|g|c|a|g|c|a|g|c|t|a|t|g|a|t|g|t|g|a|g|g|g|c|c|t|t|a|a|g|a|g|g|g|t|g|c|t|g|g|t|t|g|g|t|g|ei
g|g|g|g|t|t|g|g|g|g|t|c|t|g|c|t|a|g|g|g|c|t|c|g|c|a|a|t|g|t|g|g|c|c|c|c|a|g|a|t|g|g|a|c|t|c|c|c|a|g|c|c|c|c|t|g|g|t|ei
c|c|c|g|g|g|c|a|g|c|t|c|c|c|g|c|t|a|c|g|g|a|c|c|t|c|a|g|g|t|g|a|g|c|g|c|t|g|g|g|c|c|g|g|g|c|c|c|c|g|g|c|c|t|c|c|g|c|ei
a|c|a|c|a|t|t|c|t|a|a|a|t|a|t|g|t|g|g|c|c|t|a|a|g|a|t|t|t|t|g|g|t|c|t|a|c|t|t|t|t|c|t|g|t|g|a|a|c|a|a|a|a|t|t|t|a|a|ei
a|a|a|t|t|t|t|g|g|g|a|c|c|c|g|a|a|c|t|t|t|c|c|a|c|c|a|t|g|t|a|a|g|t|t|c|a|a|g|t|t|c|t|a|t|c|t|a|g|g|g|a|a|g|a|g|g|g|ei
g|g|c|g|c|t|t|t|g|t|c|t|g|g|g|a|g|g|c|g|g|t|t|c|g|a|a|g|c|a|g|g|c|a|t|g|a|a|g|g|a|g|g|g|a|g|c|a|g|g|g|a|g|a|g|t|g|g|ei
g|t|g|c|c|t|a|g|c|c|a|t|g|g|g|a|a|t|t|c|t|c|c|t|t|g|t|t|t|t|g|c|t|a|c|a|t|t|g|a|a|c|c|c|a|g|a|t|g|c|c|a|t|t|c|t|a|a|ei
c|t|a|g|a|g|g|a|a|g|g|c|a|t|c|c|a|a|a|t|g|c|t|a|g|g|g|g|g|t|g|a|g|g|g|t|g|g|c|a|c|c|a|g|g|g|g|t|c|c|c|c|a|a|t|c|c|t|ei
g|g|g|a|t|c|c|a|c|t|c|a|a|g|g|c|t|c|c|c|t|t|g|c|a|c|a|g|g|t|c|c|t|c|a|t|g|c|c|t|c|t|c|c|t|c|c|t|c|t|t|g|c|t|g|c|t|c|ei
a|t|a|g|a|c|c|t|t|g|g|t|g|g|g|c|g|g|t|c|c|t|t|t|c|t|a|g|g|a|a|g|a|a|g|c|c|t|a|t|a|t|c|c|t|g|a|a|g|g|a|g|c|a|g|a|a|g|ei
g|t|c|t|t|t|g|c|t|t|t|t|c|t|c|t|g|t|a|t|t|a|t|t|a|a|a|c|a|t|t|g|g|g|a|a|a|t|t|c|a|g|c|c|t|c|t|c|c|a|g|g|c|g|a|t|g|g|ei
c|t|g|t|c|t|c|c|t|g|g|g|t|t|g|c|t|t|t|c|a|c|c|c|t|c|a|g|g|c|t|g|c|t|g|g|t|c|g|t|c|t|a|c|c|c|a|t|g|g|a|c|c|c|a|g|a|g|ei
t|a|a|t|a|a|t|a|g|c|t|g|t|t|t|c|t|c|t|g|t|t|g|t|a|a|a|g|g|c|a|c|t|a|c|a|a|a|t|a|c|t|g|t|g|g|c|a|g|c|a|t|a|t|a|a|t|t|ei
t|g|t|g|t|c|t|g|t|g|t|g|t|g|t|g|t|g|g|g|t|c|t|t|t|g|t|g|t|g|t|g|t|g|t|g|t|g|t|g|g|t|a|g|c|t|g|t|c|t|g|t|t|t|g|a|a|a|ei
t|t|c|a|g|c|g|g|c|c|t|c|a|g|c|c|t|g|c|c|t|g|t|t|c|c|a|g|g|t|c|t|c|t|g|t|c|c|t|t|c|c|a|c|c|a|t|g|g|c|c|c|t|g|t|g|g|a|ei
a|g|g|a|a|t|g|t|g|c|a|c|a|t|c|t|c|c|t|c|c|t|c|t|t|t|a|a|a|c|a|t|g|g|a|g|t|c|a|t|t|a|t|t|a|g|t|t|c|a|a|c|a|g|t|a|g|a|ei
a|a|c|t|c|t|c|t|t|t|c|t|c|c|a|t|t|t|c|t|t|g|c|t|t|c|a|g|a|a|g|a|a|c|a|t|g|t|g|a|t|c|a|t|c|c|a|g|g|c|c|g|a|g|t|t|c|t|ei
t|t|c|a|a|g|a|c|c|a|t|t|g|a|g|g|a|c|c|t|g|a|g|a|c|a|a|g|g|t|g|g|g|t|g|a|a|t|g|g|g|c|a|g|c|a|g|a|a|g|g|c|a|c|c|a|t|t|ei
t|g|t|g|c|t|g|a|c|c|g|c|c|t|g|c|t|g|a|c|t|g|c|t|g|c|a|g|g|t|g|a|a|a|t|t|g|c|c|c|t|g|t|g|g|t|c|c|t|t|g|g|t|g|g|t|c|c|ei
t|g|c|t|t|c|t|c|t|c|t|t|c|a|c|t|a|c|c|t|t|t|g|c|c|t|a|g|a|t|a|c|c|c|c|t|g|a|t|t|c|a|c|c|g|a|g|c|c|c|t|g|c|a|g|t|t|g|ei
t|c|a|c|g|c|a|t|c|c|t|c|t|g|c|t|t|t|c|c|t|c|t|t|c|c|a|g|a|c|a|a|g|t|a|c|t|a|c|c|g|a|g|t|c|a|a|t|c|t|t|c|g|c|a|c|a|c|ei
c|c|t|c|a|t|g|a|a|t|t|g|c|t|c|t|c|t|g|t|t|a|c|a|c|c|a|g|g|a|g|c|c|a|g|g|g|c|t|g|a|g|g|t|c|a|g|t|g|c|t|g|a|c|c|a|g|g|ei
t|t|g|c|c|c|a|a|a|a|c|a|t|c|t|g|g|c|a|a|a|g|t|g|a|t|t|g|c|t|t|c|c|a|a|a|a|g|t|t|c|a|c|a|t|t|t|a|t|c|a|g|a|a|g|g|a|c|ei
c|t|c|g|c|t|g|a|c|t|c|t|c|c|t|t|t|t|t|c|t|t|t|t|c|a|a|g|c|c|c|a|a|g|a|g|g|a|g|a|t|c|g|g|c|g|c|g|g|t|t|g|t|c|a|g|c|t|ei
a|t|t|a|g|g|g|g|c|t|t|c|c|t|t|t|t|t|t|a|t|a|c|t|a|c|a|g|g|t|t|g|c|a|g|c|g|a|g|c|c|a|a|g|g|t|g|t|t|t|c|a|a|c|g|g|g|g|ei
a|c|a|c|c|a|a|t|t|t|a|t|t|g|t|a|t|a|t|t|t|t|c|t|c|g|g|c|t|a|g|a|a|g|a|g|c|a|a|a|t|t|t|t|g|a|t|t|g|t|t|c|c|c|a|g|c|a|ei
a|t|c|t|t|t|c|g|c|t|t|c|a|c|c|c|a|g|g|c|t|g|g|t|a|g|a|g|g|t|a|a|g|a|g|g|g|a|a|g|g|c|t|t|g|a|g|a|g|g|a|c|c|t|g|g|t|t|ei
g|c|a|g|c|c|c|a|g|a|c|c|t|a|c|c|t|c|t|t|g|c|t|t|g|c|a|g|c|a|a|t|a|t|a|a|a|t|g|t|c|a|c|c|c|t|g|g|g|c|g|c|c|c|a|c|a|a|ei
a|g|a|a|a|g|c|c|a|a|a|a|t|g|t|t|t|g|t|t|t|t|t|t|a|g|a|t|t|c|t|g|a|a|a|t|g|t|g|t|t|g|t|g|a|c|a|a|c|a|a|t|g|a|c|c|t|a|ei
g|g|a|a|g|g|c|t|g|t|g|a|g|a|a|g|a|g|c|c|t|g|a|c|g|c|c|g|a|c|a|c|g|c|t|c|c|c|t|c|c|c|c|c|t|g|c|c|c|c|t|t|c|t|a|c|a|c|ei
g|t|c|a|g|c|t|t|c|a|t|g|a|a|t|g|c|t|g|t|g|c|t|t|c|g|t|a|c|g|c|a|c|a|c|a|c|t|t|g|g|g|c|a|g|c|t|g|a|a|g|c|c|c|t|g|c|c|ei
c|a|g|a|g|t|c|c|a|t|g|t|g|t|t|t|c|t|t|g|t|g|c|g|t|t|t|g|t|t|g|c|a|g|g|g|g|a|g|g|a|g|a|a|t|a|g|g|t|g|g|g|g|c|t|g|t|g|ei
g|c|c|c|c|g|g|c|g|c|c|c|a|c|c|c|g|c|a|c|c|c|c|c|c|c|a|g|g|t|c|a|g|t|g|c|g|t|g|c|c|c|g|c|g|c|g|t|g|t|c|t|g|g|g|g|g|g|ei
g|a|a|t|t|c|a|t|g|t|c|t|t|a|c|g|g|t|c|a|a|g|g|c|a|g|a|g|a|a|a|g|g|a|t|t|t|c|t|g|c|a|t|c|a|c|t|t|t|c|t|t|c|c|t|g|t|a|ei
c|t|a|t|c|c|c|a|a|g|t|c|t|a|t|g|t|c|c|a|a|g|g|a|c|t|g|t|g|g|c|c|a|t|c|t|g|c|a|a|a|g|g|g|c|t|g|a|t|g|a|c|c|a|a|a|c|a|ei
c|c|c|a|a|g|a|g|g|a|g|a|t|c|g|g|c|g|c|g|g|t|t|t|a|g|c|t|g|t|a|a|g|t|a|a|a|g|c|g|a|g|c|c|c|c|g|t|a|a|c|c|g|t|t|c|g|t|ei
c|a|a|c|c|c|t|c|a|t|g|a|c|c|a|c|c|a|g|c|t|c|t|c|c|c|a|g|t|c|t|g|c|t|c|c|a|g|g|g|a|c|t|t|c|a|c|c|c|c|a|c|c|c|a|c|c|g|ei
c|g|a|g|a|a|a|t|t|a|t|a|g|g|t|g|a|t|g|a|a|c|t|g|c|c|a|g|g|t|g|a|g|t|t|g|t|c|a|a|a|t|t|t|a|t|a|g|c|t|a|t|t|t|t|c|a|a|ei
c|a|g|a|t|g|g|c|t|g|g|a|a|g|g|a|c|c|t|c|t|t|t|g|a|a|c|t|t|t|g|t|t|t|a|a|t|t|c|c|a|t|t|a|a|t|c|t|g|t|g|t|a|t|t|c|t|t|ei
g|t|a|g|a|c|a|c|c|t|a|a|g|a|c|c|t|t|t|t|t|t|t|t|t|t|a|g|g|t|g|t|c|t|g|c|a|t|t|a|t|t|g|g|g|c|c|g|a|a|t|c|c|c|t|t|c|t|ei
t|g|a|c|t|t|a|c|a|t|t|c|a|t|t|t|c|c|c|t|t|a|t|t|c|c|a|g|a|t|c|c|g|t|t|c|t|g|g|c|t|a|c|t|t|t|g|a|t|g|a|g|a|g|g|t|a|t|ei
g|a|a|t|t|c|a|t|c|c|t|a|c|a|g|g|t|g|c|a|g|g|c|g|c|t|a|t|c|a|g|a|a|g|g|t|g|g|t|g|g|c|t|g|g|t|g|t|g|g|c|t|a|a|t|g|c|c|ei
c|c|c|t|c|c|t|t|c|t|g|t|g|t|g|g|g|g|c|a|c|t|c|c|a|c|a|g|g|g|c|t|t|c|g|a|g|c|t|c|a|t|c|t|a|g|a|t|g|a|g|g|a|g|c|t|c|c|ei
a|c|t|a|c|c|t|g|a|c|t|c|a|g|g|a|a|t|c|g|g|c|t|t|g|a|a|g|g|t|g|a|g|c|a|c|c|a|g|c|g|c|t|c|c|t|t|n|g|g|a|a|g|c|c|t|c|c|ei
t|a|c|c|a|t|t|t|t|g|a|t|t|g|g|c|g|a|t|t|t|t|c|t|t|t|a|g|g|g|c|a|g|t|a|g|c|t|c|g|c|c|t|g|a|g|c|c|a|g|a|g|a|t|t|t|c|c|ei
g|a|c|c|g|g|c|g|g|g|a|a|c|g|g|a|a|g|g|c|t|g|c|t|c|a|a|g|g|t|a|a|g|g|c|a|t|g|g|g|c|a|t|t|g|g|c|c|a|a|c|a|c|a|c|c|c|c|ei
c|c|t|a|c|a|c|a|t|c|c|a|t|g|t|c|t|c|t|t|t|t|c|c|g|c|a|g|g|c|c|c|c|a|t|g|g|g|t|c|c|a|c|c|t|g|g|a|g|a|a|a|t|g|c|c|a|t|ei
g|c|c|c|t|g|c|c|a|c|c|c|c|a|a|g|g|t|g|c|c|t|g|g|c|c|t|g|c|c|a|c|c|c|c|a|a|a|g|t|g|c|c|t|g|a|g|c|c|c|t|g|c|c|a|g|c|c|ei
t|g|c|t|t|t|a|a|a|a|t|a|t|c|c|t|g|c|a|a|a|t|g|a|c|a|g|t|t|g|a|t|c|c|a|g|t|a|g|a|a|a|g|g|t|t|t|a|t|a|t|t|t|t|g|g|t|c|ei
g|a|t|c|g|g|g|g|c|t|t|c|c|c|g|g|g|a|g|c|a|g|c|c|a|t|c|a|g|c|a|c|c|a|c|g|a|c|t|c|g|g|g|g|a|c|a|c|a|g|c|c|a|g|g|g|c|c|ei
g|g|a|a|g|a|t|g|t|t|g|g|t|g|g|t|g|a|g|g|c|c|c|g|g|c|a|g|g|t|c|a|g|t|a|t|c|a|t|g|g|c|t|a|t|g|a|g|g|c|a|g|g|c|t|t|a|a|ei
c|c|c|a|c|c|c|c|c|a|t|c|c|c|c|t|a|t|g|g|c|t|c|t|c|t|a|g|g|a|g|a|c|c|c|c|a|g|c|a|a|g|c|a|g|a|a|c|t|c|a|c|t|g|c|t|c|t|ei
c|c|g|a|a|g|g|g|a|t|c|a|g|g|g|a|g|c|c|a|a|a|g|t|a|c|t|g|g|g|a|a|g|c|t|a|a|a|g|c|a|a|c|g|a|t|c|a|c|c|t|a|a|a|t|t|a|c|ei
g|g|t|g|a|a|g|a|c|a|t|t|g|t|g|g|c|t|g|a|c|c|a|g|t|g|c|c|t|c|t|t|g|t|g|g|t|g|t|a|a|a|c|t|t|g|t|a|c|c|a|g|t|t|t|t|a|c|ei
t|a|t|g|g|g|g|g|c|a|c|a|g|g|a|t|g|a|g|g|a|g|g|a|g|a|a|t|c|c|a|a|g|a|c|t|t|g|g|a|t|g|g|a|t|t|a|t|t|a|g|t|t|t|t|c|g|a|ei
a|a|c|t|c|t|g|g|g|a|a|c|a|a|g|g|t|t|a|a|a|g|t|a|c|c|c|g|c|c|a|a|a|a|t|a|g|a|a|g|c|t|t|t|c|c|g|a|g|c|t|t|c|a|c|t|t|t|ei
t|g|g|t|t|c|a|t|g|g|t|t|t|t|g|g|t|t|t|t|g|g|t|t|c|c|a|g|a|a|g|a|t|t|t|t|g|t|g|a|t|t|c|a|g|g|c|a|a|a|g|g|c|t|g|a|c|t|ei
g|a|g|g|a|t|g|a|a|g|c|t|a|a|g|g|a|g|c|t|g|g|c|g|g|g|a|g|g|t|g|t|g|g|g|g|t|c|t|g|g|g|a|t|g|c|c|t|g|g|g|a|c|c|c|a|g|g|ei
a|g|g|g|c|c|c|c|t|c|a|t|c|t|t|c|c|c|t|t|c|c|t|t|c|c|a|g|a|g|c|c|g|t|c|t|t|c|c|c|a|g|t|c|c|a|c|c|g|t|c|c|c|c|a|t|c|g|ei
g|g|t|a|t|g|a|g|a|a|t|c|t|a|g|g|c|a|g|g|g|g|c|g|g|g|a|g|t|t|a|c|a|g|t|c|c|c|t|t|t|t|a|c|a|g|a|t|a|g|a|a|a|a|a|c|a|g|ei
a|g|a|a|c|g|g|g|a|a|g|g|a|g|a|a|g|c|t|g|c|a|g|g|g|c|g|g|g|t|a|c|c|a|g|g|g|g|c|a|g|t|g|g|g|g|a|g|c|c|t|t|c|c|c|c|a|t|ei
t|g|g|c|a|a|a|a|c|a|c|t|g|c|t|c|a|g|a|g|a|c|g|g|g|c|c|t|g|a|a|t|a|t|c|t|t|t|c|a|a|a|a|c|c|t|c|a|a|t|c|g|t|c|g|a|c|a|ei
a|g|a|a|c|g|g|g|a|a|g|g|a|g|a|g|c|c|t|g|c|a|g|g|g|c|g|g|g|t|a|c|c|a|g|g|g|g|c|a|g|t|g|g|g|g|a|g|c|c|t|t|c|c|c|c|a|t|ei
c|t|g|t|c|c|t|g|t|g|g|g|t|t|c|c|t|c|t|c|a|c|c|t|t|c|a|g|g|t|t|g|c|t|g|g|t|c|g|t|c|t|a|c|c|c|a|t|g|g|a|c|c|c|a|g|a|g|ei
c|g|a|g|t|g|a|c|a|a|g|c|c|t|g|t|a|g|c|c|c|a|t|t|g|t|a|g|g|t|a|a|g|a|g|c|t|c|t|g|a|g|g|a|t|g|t|g|t|c|t|t|g|g|a|a|c|t|ei
c|g|c|a|c|c|a|t|c|a|c|c|g|g|g|a|t|g|t|g|c|a|a|a|c|a|g|g|t|g|c|g|g|c|t|g|g|c|t|g|g|g|g|g|t|g|g|c|t|g|c|a|g|g|a|a|c|c|ei
g|t|g|g|c|c|g|a|c|c|a|g|g|t|g|g|c|g|c|t|g|c|t|c|c|a|t|g|a|g|c|t|g|g|a|g|c|g|a|g|c|t|c|t|t|c|g|t|g|c|t|g|a|a|c|g|c|g|ei
c|a|g|t|c|c|c|g|g|c|c|g|g|t|g|c|c|t|g|g|g|t|c|c|a|c|a|g|a|g|g|a|g|g|c|c|g|t|g|g|a|g|g|a|g|g|a|g|a|c|a|g|g|a|g|a|t|g|ei
c|c|t|t|c|a|c|c|c|a|t|c|c|c|c|t|g|t|c|c|c|t|g|g|c|c|a|g|g|t|c|g|a|g|g|t|g|a|t|t|g|g|g|g|g|a|g|c|a|g|a|c|a|a|g|t|a|c|ei
g|t|c|c|g|t|g|c|c|t|t|c|a|g|a|g|c|a|g|t|g|t|c|a|g|a|g|g|t|g|g|a|g|t|g|g|c|c|a|g|c|t|t|g|g|a|g|t|g|g|c|c|c|t|t|t|g|c|ei
c|t|t|c|c|a|a|g|g|c|g|c|c|c|t|c|c|c|t|t|t|c|c|g|c|a|t|a|g|a|c|c|t|g|c|a|a|c|c|c|a|c|c|t|a|a|g|c|t|g|c|a|c|g|t|c|g|g|ei
g|a|c|a|g|a|g|c|a|g|a|t|t|t|g|a|a|a|c|a|c|t|c|a|t|t|g|t|g|c|t|a|t|t|t|g|c|a|a|g|t|g|t|a|g|a|t|t|t|c|a|a|g|c|g|c|t|t|ei
c|t|g|g|g|c|t|t|g|c|a|g|c|t|g|g|g|c|t|c|c|c|a|t|a|a|g|a|g|c|a|a|g|g|g|c|t|g|a|c|a|a|a|t|g|g|g|c|c|c|g|g|g|a|t|g|c|a|ei
g|g|a|c|a|g|c|c|c|c|c|a|g|g|c|c|g|t|g|c|g|g|c|c|c|c|c|t|g|g|a|g|g|g|t|g|t|c|c|a|g|g|a|t|g|a|g|c|t|g|g|a|c|a|c|c|c|t|ei
a|t|c|c|c|t|c|c|c|c|a|a|c|c|t|g|t|g|c|c|c|t|t|t|t|t|a|c|a|g|a|g|c|a|c|t|g|a|c|a|c|g|g|c|t|c|c|c|g|g|g|a|c|c|t|c|g|g|ei
c|t|a|c|a|t|t|c|c|t|t|t|t|c|c|t|g|t|g|a|a|a|t|t|t|g|a|g|t|g|a|t|a|a|t|t|a|a|a|c|a|c|t|t|t|a|g|a|c|c|t|g|a|t|t|c|t|g|ei
a|g|g|t|t|t|t|c|t|t|c|a|g|g|c|a|g|a|g|g|g|t|c|c|t|c|a|g|g|t|a|a|c|t|g|a|t|g|g|a|a|a|c|c|c|c|t|g|g|c|c|a|t|g|g|g|g|t|ei
t|t|g|t|t|c|c|c|a|a|c|c|c|c|t|t|t|c|t|t|c|c|c|t|c|c|a|g|g|g|g|c|t|g|c|c|g|g|g|a|g|g|c|t|a|t|c|a|a|a|a|g|g|a|t|c|g|c|ei
a|g|c|a|a|a|g|c|c|c|t|g|c|t|c|g|t|g|c|t|g|a|c|c|g|g|c|c|g|t|g|t|g|g|c|t|c|c|a|g|a|g|t|c|t|g|a|c|c|g|c|c|t|c|c|c|g|c|ei
g|c|a|c|a|g|c|c|a|c|t|g|c|c|g|g|t|c|c|t|t|c|c|c|g|c|a|g|a|a|c|t|t|a|g|a|g|c|t|g|c|t|c|c|a|c|a|t|c|t|c|c|c|t|g|c|t|g|ei
c|c|t|t|c|c|c|c|a|g|g|c|c|c|a|c|c|a|t|c|a|c|c|c|g|c|c|t|c|t|g|g|c|c|g|c|c|a|c|c|c|c|c|a|t|c|t|t|c|c|a|c|c|t|g|t|g|c|ei
a|c|t|g|a|g|c|t|t|t|c|t|c|a|c|c|c|t|g|g|t|t|g|t|g|c|a|g|a|t|t|t|t|a|t|c|c|g|t|g|g|t|g|t|g|g|t|t|g|a|c|t|c|t|g|a|g|g|ei
g|g|c|c|c|c|t|c|a|c|a|g|g|a|c|a|t|t|t|t|c|t|t|c|a|c|a|g|g|t|g|g|a|a|a|a|g|g|a|g|g|g|a|g|c|t|a|c|t|c|t|a|a|g|g|c|t|g|ei
a|g|a|g|g|t|t|g|g|t|t|c|t|t|a|t|c|c|c|t|t|g|g|g|a|t|t|t|a|a|a|a|c|c|t|t|a|g|t|a|c|a|a|a|t|a|g|t|c|c|t|a|g|c|c|a|t|a|ei
t|g|g|a|c|c|a|t|c|g|c|g|g|a|t|a|g|a|c|a|a|g|a|c|g|a|g|g|g|g|c|c|t|c|t|g|c|g|c|c|c|t|g|g|g|c|c|c|a|g|c|t|c|t|g|t|c|c|ei
a|c|t|a|c|t|c|t|g|c|a|c|t|a|a|a|g|c|c|a|t|t|t|c|c|c|a|a|t|t|t|a|a|g|t|t|t|a|t|a|a|a|t|t|a|c|c|a|g|t|t|t|c|g|g|t|a|a|ei
t|a|a|g|a|a|a|g|g|a|a|g|t|a|t|a|g|g|c|t|a|g|g|a|a|g|t|g|g|c|t|c|a|c|a|c|c|t|g|t|a|a|t|c|c|t|t|g|c|a|t|t|t|t|g|g|a|a|ei
c|t|g|t|c|c|c|t|t|g|g|g|c|t|g|t|t|t|t|c|c|t|a|c|t|c|a|g|a|t|t|a|c|t|g|g|t|g|g|t|c|t|a|c|c|c|t|t|g|g|a|c|c|c|a|g|a|g|ei
a|g|t|c|c|c|g|t|a|g|t|t|c|c|t|t|c|t|c|a|c|t|c|g|t|g|c|a|t|t|t|a|t|c|a|t|t|c|t|a|a|a|c|c|c|a|g|a|c|t|t|t|c|a|c|a|t|a|ei
g|g|c|t|t|t|t|t|a|a|g|c|t|c|t|c|a|g|t|a|t|t|a|g|g|a|t|t|g|t|g|a|t|t|c|t|g|t|a|a|a|c|c|c|a|t|a|t|t|t|g|c|t|c|a|g|a|a|ei
c|c|a|g|t|t|t|g|a|a|g|g|a|g|g|c|a|c|t|g|c|t|g|t|c|c|a|g|t|c|t|t|g|c|a|g|g|t|c|t|c|c|c|g|a|g|g|g|c|a|g|a|a|g|g|t|g|a|ei
c|t|t|g|a|g|c|c|c|t|g|c|c|t|t|g|t|g|c|c|t|c|c|g|a|c|a|g|g|g|a|a|t|g|c|t|g|g|c|a|g|g|a|t|a|a|g|g|a|g|c|g|c|c|a|g|c|t|ei
g|t|g|g|a|g|g|c|t|g|c|c|c|g|g|c|g|a|g|c|c|c|a|g|g|c|t|g|g|a|g|a|t|g|g|a|g|a|t|g|c|t|c|t|c|c|a|g|c|a|c|c|a|g|c|c|c|a|ei
g|a|t|g|t|g|g|g|c|a|g|t|t|t|t|t|a|t|t|t|c|a|g|t|a|g|t|c|t|c|c|a|g|a|a|g|g|c|a|g|g|g|g|a|c|a|g|g|g|a|c|t|g|g|g|a|g|g|ei
t|a|c|t|t|t|g|a|g|t|g|g|a|g|g|a|c|c|a|c|t|g|c|g|c|t|g|c|a|a|g|a|a|a|g|a|c|a|t|a|t|t|t|a|a|a|g|c|a|a|a|t|a|a|g|g|a|g|ei
a|a|g|g|a|c|c|g|g|a|t|t|t|c|c|g|a|c|t|g|g|g|g|g|g|c|t|g|g|t|g|a|g|t|g|c|c|c|t|g|c|a|g|g|a|g|c|g|a|c|c|c|c|c|a|g|g|a|ei
g|a|g|a|t|c|g|a|c|c|t|g|g|a|c|t|c|c|a|t|g|a|g|a|t|c|t|g|g|t|g|a|g|t|g|c|c|t|t|c|a|c|a|t|c|a|c|c|t|g|c|c|c|a|g|c|t|c|ei
t|g|c|t|c|t|t|t|c|t|t|t|t|c|t|g|t|t|t|c|a|c|t|t|t|t|a|g|a|t|c|a|c|c|g|g|c|g|t|a|a|t|c|a|a|c|c|c|a|g|c|g|t|t|g|g|a|c|ei
a|t|a|t|t|t|t|a|a|g|a|t|g|g|a|c|t|g|g|g|a|a|a|a|a|t|c|a|a|c|t|c|c|t|g|a|a|g|t|t|a|g|a|a|a|t|a|a|g|a|a|t|g|g|t|t|t|g|ei
g|t|g|a|c|t|t|a|a|a|a|t|g|a|a|a|t|t|t|a|t|t|t|t|a|t|a|g|g|t|g|a|a|c|a|t|a|a|t|a|t|t|g|a|g|g|a|g|a|c|a|g|a|a|c|a|t|a|ei
t|c|g|g|c|g|g|c|g|c|g|c|a|c|g|c|g|g|a|c|a|c|c|g|g|a|c|a|g|t|g|a|g|t|g|g|c|g|c|g|g|c|c|a|g|g|c|g|c|g|a|a|g|g|g|g|c|g|ei
g|g|c|g|g|t|t|c|t|g|c|t|g|c|t|g|c|c|c|t|t|t|g|g|t|c|c|a|g|t|g|a|g|t|c|a|a|c|a|c|c|c|c|c|g|t|t|c|c|c|c|g|a|a|c|c|c|t|ei
a|c|c|t|g|g|t|c|c|t|c|c|t|g|g|c|c|c|c|c|c|t|g|t|t|c|g|g|t|g|g|g|a|a|c|t|t|t|g|c|t|g|c|t|c|a|g|t|a|t|g|a|t|g|g|a|a|a|ei
g|g|t|g|t|c|a|g|g|t|g|g|g|a|g|t|a|c|t|g|c|a|a|c|g|a|c|g|c|a|a|t|g|c|t|c|a|g|a|c|g|c|a|g|a|a|g|g|g|a|c|t|g|c|c|g|t|c|ei
a|c|a|g|g|c|c|c|g|g|t|g|g|g|t|c|c|t|g|c|a|g|g|c|a|g|c|a|g|g|g|a|a|a|c|c|t|g|g|c|c|c|t|g|a|t|g|g|t|c|t|g|a|g|g|g|g|g|ei
t|t|c|a|a|g|a|t|c|a|t|c|g|a|g|g|a|c|c|t|g|a|g|g|t|c|a|g|g|t|a|a|g|g|g|g|t|a|g|g|a|g|g|g|a|c|c|t|c|a|a|c|t|c|c|c|a|g|ei
t|t|t|a|c|a|g|a|a|t|c|a|g|g|t|t|t|a|t|t|t|g|t|t|a|t|a|a|t|t|t|g|t|a|g|a|a|t|t|a|t|c|a|a|g|c|a|t|c|a|t|a|t|t|t|t|a|g|ei
g|t|c|a|a|g|a|t|a|a|a|c|a|a|t|c|a|g|c|t|t|a|c|c|g|g|a|t|a|g|c|a|a|c|a|c|t|a|a|a|t|a|c|t|t|c|c|a|c|a|a|a|t|t|g|a|a|c|ei
g|g|g|t|c|c|c|a|c|c|a|a|t|c|t|t|g|t|t|t|g|c|t|c|g|c|a|g|a|g|c|c|t|c|a|g|c|c|t|g|c|c|t|g|g|a|a|g|a|t|g|c|c|g|a|g|a|t|ei
c|t|c|t|c|c|c|t|c|c|c|t|g|a|g|c|t|g|g|a|g|c|a|c|g|c|a|g|g|a|a|c|a|g|c|a|t|c|a|g|g|a|g|c|a|g|c|a|g|c|a|g|g|a|g|c|a|g|ei
c|a|t|a|c|t|t|g|g|c|t|c|t|a|t|t|c|t|g|c|t|t|c|c|a|c|a|g|g|c|t|g|t|g|g|a|c|a|t|a|c|t|c|a|a|g|a|c|a|g|a|g|c|g|g|c|t|g|ie
c|g|t|g|a|g|t|g|a|t|c|c|t|g|t|c|c|t|c|t|c|c|a|c|g|c|a|g|g|g|c|c|g|c|g|t|t|c|g|c|a|c|c|a|a|a|a|c|c|g|t|g|a|a|g|a|a|g|ei
g|g|c|c|t|c|t|c|a|c|a|g|g|a|c|a|t|t|t|t|c|t|t|c|a|c|a|g|a|t|t|g|a|a|a|a|g|g|a|g|g|g|a|g|c|t|a|c|t|c|t|c|a|g|g|c|t|g|ei
g|g|a|t|a|g|c|a|t|g|a|c|a|c|c|a|c|t|c|t|t|c|t|t|t|c|a|g|a|c|t|g|a|a|a|t|a|c|a|g|t|t|g|g|t|g|c|a|g|a|g|t|c|t|g|g|g|g|ei
t|t|c|t|c|c|c|g|c|c|t|c|a|g|c|c|t|c|c|c|g|a|g|a|c|t|g|g|g|a|c|t|a|c|a|g|g|c|g|c|c|c|g|c|c|a|c|c|a|t|g|c|c|c|g|g|c|t|ei
c|g|t|g|g|a|g|g|c|c|g|a|c|a|t|c|a|a|c|g|g|c|c|g|g|c|a|g|g|g|t|g|c|t|g|g|a|t|g|a|g|c|t|g|a|c|c|c|t|g|g|c|c|a|g|g|a|c|ei
c|c|a|g|c|c|t|g|g|g|t|g|a|c|a|g|a|g|c|g|a|g|a|t|c|a|t|c|t|c|a|a|a|a|a|a|a|a|a|a|a|a|c|a|a|a|a|a|a|a|a|a|a|a|a|a|a|a|ei
t|c|c|a|a|c|a|g|g|g|a|g|g|a|a|a|c|a|c|a|a|c|a|a|a|t|c|c|g|t|g|a|g|t|g|g|a|t|g|c|c|t|t|g|a|c|c|c|c|a|g|g|c|g|g|g|g|a|ei
t|g|g|c|a|g|c|g|g|g|a|t|g|g|g|g|a|g|g|a|c|c|a|a|c|c|a|g|g|a|c|a|c|g|g|a|g|c|t|t|g|t|g|g|a|g|a|c|c|a|g|g|c|c|t|g|c|a|ei
c|g|c|c|g|c|c|g|c|c|g|g|g|g|c|g|g|c|c|c|c|c|g|g|t|c|t|a|c|c|c|t|g|c|a|c|t|c|g|g|c|c|t|c|a|a|c|g|g|g|c|t|c|c|c|g|c|a|ei
g|a|a|t|t|c|t|a|g|a|g|c|t|t|g|a|c|c|a|g|t|t|t|a|g|g|g|c|a|g|c|a|g|g|g|a|c|a|a|a|a|a|c|g|t|t|t|c|c|a|a|g|a|c|a|t|g|a|ei
t|g|g|g|a|c|a|c|t|t|a|a|c|a|g|a|t|g|c|a|a|t|g|g|t|a|c|t|g|a|t|t|g|t|t|t|c|a|t|t|g|c|g|a|a|t|c|t|t|t|t|t|t|a|g|c|a|t|ei
t|c|a|t|a|a|c|c|t|c|g|t|c|t|a|t|c|c|t|c|c|t|t|c|g|c|a|g|a|a|t|g|t|c|a|g|c|a|t|c|t|c|a|t|t|a|g|a|t|g|g|t|g|c|t|t|g|g|ei
t|c|t|c|a|c|c|c|a|g|a|g|g|c|t|c|t|t|t|t|t|c|t|t|c|c|a|g|a|g|g|g|a|g|g|c|c|g|a|g|a|a|c|a|t|g|t|t|g|c|t|c|a|c|c|t|g|c|ei
t|c|c|c|t|c|t|a|a|c|c|a|t|c|t|g|t|g|c|t|t|t|c|c|c|c|a|g|g|g|a|c|t|t|g|t|a|c|a|g|c|a|a|a|a|g|c|a|c|a|g|c|a|g|c|c|a|t|ie
g|a|t|c|c|a|g|c|t|g|t|g|g|c|t|a|t|c|c|a|g|c|c|c|t|c|c|t|g|g|g|g|a|c|t|t|t|g|g|a|c|t|t|t|g|a|g|g|g|g|g|g|g|c|a|t|g|c|ei
c|c|c|c|t|c|t|a|a|c|c|a|t|c|t|g|t|g|c|t|t|t|c|c|c|c|a|g|g|g|a|c|t|t|g|t|a|c|a|g|c|a|a|a|a|g|c|a|c|a|g|c|a|g|c|c|a|t|ei
c|a|c|t|g|a|c|a|c|g|g|t|g|g|a|g|t|g|c|c|g|c|t|c|a|c|a|g|g|t|g|a|g|a|g|c|t|g|g|g|g|c|t|a|g|g|g|g|t|g|g|g|g|g|g|c|t|g|ei
t|c|c|c|t|g|g|a|a|c|a|t|a|c|c|a|a|a|c|c|c|t|a|a|a|t|g|t|t|t|c|c|a|a|g|a|a|c|a|c|c|t|g|g|a|a|t|t|t|g|g|t|t|a|c|t|c|c|ei
t|g|t|t|c|c|a|t|g|a|c|c|c|c|c|c|c|a|c|c|g|c|c|t|a|c|a|g|t|g|t|t|c|c|t|g|g|c|t|c|c|t|c|a|g|c|a|a|g|c|a|c|g|g|t|c|g|c|ei
c|c|t|g|g|c|t|c|a|t|c|c|c|a|c|c|t|t|t|c|c|t|t|c|a|c|a|g|a|g|c|t|c|g|t|c|c|g|c|a|t|g|g|t|g|c|t|g|a|a|t|g|g|c|t|g|a|g|ei
g|a|a|g|a|t|g|t|g|t|t|c|a|g|c|t|a|t|g|a|g|g|t|g|g|a|t|g|t|t|a|g|t|g|g|g|a|g|c|a|g|g|g|a|t|t|g|g|g|g|t|c|a|c|a|c|c|c|ei
t|g|g|c|t|c|t|c|t|g|c|a|a|c|c|a|g|t|t|c|t|c|t|c|t|c|a|c|g|t|g|a|g|t|c|t|g|a|g|t|t|t|c|g|t|t|g|t|g|g|g|t|a|t|c|a|c|c|ei
a|g|g|g|c|c|c|c|t|c|a|c|c|t|t|c|c|c|c|t|c|c|t|t|c|c|a|g|a|g|c|c|g|t|c|t|t|c|c|c|a|g|c|c|c|a|c|c|a|t|c|c|c|c|a|t|c|g|ei
c|c|c|c|a|t|c|c|t|g|a|a|g|g|g|c|c|t|t|a|t|g|t|t|c|c|a|g|g|t|g|a|a|c|g|c|t|a|t|g|g|c|t|c|c|a|a|g|a|a|g|a|g|c|a|t|g|g|ei
t|t|g|g|g|g|a|c|a|t|c|t|t|a|t|g|g|g|a|a|c|a|t|t|g|a|g|a|t|c|c|t|g|c|a|g|a|a|a|g|a|g|g|a|t|g|t|g|a|a|a|c|c|a|t|a|t|c|ei
t|g|a|t|a|g|t|c|a|a|t|a|c|c|a|g|g|g|a|c|c|a|g|a|g|g|t|c|g|t|g|a|c|c|a|g|t|c|c|t|g|g|a|g|g|c|c|c|c|a|g|g|c|t|g|t|a|c|ei
g|c|t|t|g|a|t|g|t|c|t|a|a|a|a|a|t|a|t|a|t|t|t|a|g|t|c|t|t|a|c|t|g|a|a|a|c|a|t|t|t|t|g|c|c|a|g|a|c|t|t|t|c|t|c|c|a|a|ei
g|g|t|a|c|t|a|a|a|g|c|a|t|t|c|a|t|g|g|a|g|g|c|c|t|c|a|g|g|t|a|t|t|g|c|a|g|t|t|c|t|g|t|a|g|g|c|a|t|t|c|a|t|a|c|t|t|a|ei
t|c|t|g|t|t|t|c|t|t|c|t|c|c|a|c|c|a|a|c|t|g|t|t|g|a|a|g|g|t|g|a|g|a|a|g|c|c|a|g|g|c|t|g|c|c|c|c|c|t|g|t|a|g|g|a|a|a|ei
c|c|t|c|a|c|t|c|c|c|a|c|t|c|t|c|c|c|a|c|c|c|c|a|c|a|c|c|t|t|g|g|c|c|c|a|t|c|c|a|t|g|g|c|g|g|c|a|t|c|t|t|g|g|g|c|c|a|ei
c|t|c|g|g|g|c|a|g|c|a|g|t|c|a|t|t|g|c|t|g|t|c|c|c|g|c|t|c|t|g|c|c|c|a|g|g|c|t|g|c|c|c|g|c|c|a|g|g|t|c|c|a|c|t|t|a|t|ei
g|c|g|c|a|c|a|c|c|c|t|c|c|c|g|c|t|c|t|t|t|c|g|c|g|c|a|g|g|a|c|g|c|t|g|a|t|g|g|a|c|g|a|g|a|c|c|a|t|g|a|a|g|g|a|g|t|t|ei
a|c|a|g|c|t|a|a|a|a|t|c|c|t|t|g|c|c|t|g|t|g|a|t|a|a|a|a|g|a|a|g|g|a|a|a|t|t|t|a|t|t|g|a|c|a|g|a|a|c|a|g|c|a|a|a|t|g|ei
a|c|g|a|g|t|a|t|g|t|t|g|g|a|g|a|a|a|t|a|a|a|a|g|c|g|a|t|a|g|t|g|g|g|g|a|t|t|t|t|a|t|t|t|t|a|a|g|t|t|t|g|t|t|g|g|t|g|ei
g|g|c|t|a|c|a|g|c|t|c|t|c|c|c|t|g|g|g|c|a|t|c|t|c|c|a|g|g|t|a|a|t|g|a|g|g|c|t|c|c|c|c|a|g|c|c|t|g|c|c|c|t|a|c|a|c|a|ei
t|g|c|t|t|g|c|c|c|c|t|g|c|t|g|c|c|t|c|t|t|c|c|t|c|c|a|g|g|t|a|t|g|g|g|a|a|a|a|g|a|c|a|c|a|a|a|g|a|g|g|a|c|a|c|g|c|t|ei
t|g|t|c|c|c|t|t|c|t|g|c|c|t|t|t|c|c|t|t|t|c|c|t|c|c|a|g|g|g|g|c|t|c|g|g|g|a|c|a|t|g|t|g|g|a|g|a|g|c|c|t|a|c|t|c|t|g|ei
c|c|a|t|c|a|t|c|a|c|c|c|t|c|t|c|t|c|t|t|t|c|c|t|a|c|a|g|t|g|c|t|g|a|g|g|c|g|g|c|a|t|t|a|a|g|a|g|g|a|a|g|t|c|c|t|g|g|ei
c|c|t|g|c|t|c|t|c|a|c|a|c|c|a|t|c|t|c|c|t|c|c|c|c|t|a|g|g|g|c|a|g|t|a|c|t|g|c|t|a|t|g|a|a|c|t|g|g|a|c|g|a|a|a|a|g|g|ei
t|g|a|c|a|t|g|t|t|t|t|c|t|a|t|t|g|t|c|t|t|g|a|c|a|t|t|a|c|t|g|c|a|t|a|t|g|a|t|a|c|a|t|c|a|a|a|g|t|t|a|a|g|t|g|a|c|a|ei
g|g|g|c|c|a|t|t|g|c|t|t|a|t|t|t|t|t|c|c|a|t|a|a|a|a|g|t|a|a|a|a|t|a|a|a|t|c|a|t|a|a|t|g|g|c|c|a|a|t|a|a|g|c|c|a|a|t|ei
a|c|c|t|g|a|g|g|t|c|g|g|g|a|g|t|t|c|g|a|g|a|c|a|c|c|t|g|a|c|c|a|a|c|a|t|g|g|t|g|a|a|a|c|c|c|c|a|t|c|t|t|t|a|c|t|a|a|ei
c|t|t|c|g|a|t|t|t|g|t|a|c|c|a|t|t|c|c|t|t|c|a|a|a|a|a|g|a|a|a|t|t|t|g|g|t|a|c|c|a|a|a|a|a|a|a|a|a|a|a|g|a|a|a|g|a|a|ei
g|c|a|g|a|t|c|c|t|c|a|t|g|a|a|t|g|c|t|a|t|g|c|a|a|g|t|g|g|t|a|g|g|t|t|t|a|t|t|g|t|t|g|g|a|a|a|a|a|a|a|t|g|t|a|g|t|t|ei
g|c|c|c|a|t|t|t|a|g|t|g|t|g|c|a|c|a|c|a|g|c|t|g|g|c|c|t|g|c|c|g|t|a|t|g|t|c|a|g|g|c|c|t|g|g|t|g|c|t|g|g|g|t|c|t|c|c|ei
a|a|a|a|c|t|a|t|g|a|c|a|a|g|t|t|c|a|t|g|g|a|a|a|a|t|g|g|g|t|a|a|a|g|a|c|t|t|t|a|t|t|t|c|t|t|t|g|t|g|g|c|t|c|a|t|t|c|ei
t|c|t|a|a|t|t|t|a|a|g|a|a|c|a|a|c|t|a|a|c|c|c|t|t|t|a|a|t|g|a|a|t|a|a|a|t|c|a|a|c|c|t|t|g|t|a|t|t|g|a|g|t|t|g|c|t|a|ei
a|a|a|t|g|c|c|a|t|a|c|c|c|a|t|g|g|g|a|g|a|g|a|g|a|g|g|a|t|g|t|g|t|a|t|a|a|g|g|c|g|g|g|t|g|a|g|c|a|a|g|t|g|a|c|t|t|a|ei
g|a|c|a|g|g|g|a|t|a|t|g|t|c|t|t|t|g|c|t|t|t|c|t|a|a|a|g|g|c|t|g|a|c|t|g|t|g|c|t|g|t|c|c|t|g|a|t|t|g|t|t|g|c|t|g|c|t|ei
c|c|c|t|g|g|c|c|c|t|t|c|c|c|t|t|g|g|c|t|g|a|t|t|t|c|a|g|a|a|a|c|c|c|a|g|a|t|c|g|a|g|a|c|t|c|a|a|a|g|c|c|c|t|g|g|t|g|ei
t|c|a|g|c|t|t|a|c|t|g|a|c|a|c|c|a|g|c|c|c|a|c|c|a|c|a|g|a|t|g|g|g|g|a|c|c|a|g|t|g|t|g|c|c|t|c|a|a|g|t|c|c|a|t|g|c|c|ei
g|g|c|a|c|c|a|a|t|g|t|a|g|a|t|a|c|c|a|a|a|a|a|a|g|a|c|t|t|c|c|a|a|t|t|t|c|c|c|t|g|t|g|g|a|t|c|t|c|t|c|c|g|a|t|t|a|t|ei
a|g|a|a|c|g|g|g|a|a|g|g|a|g|a|c|g|c|t|g|c|a|g|g|g|c|g|g|g|t|a|c|c|a|g|g|g|g|c|a|g|t|g|g|g|g|a|g|c|c|t|t|c|c|c|c|a|t|ei
a|a|g|g|g|a|g|t|g|g|c|t|t|c|c|t|c|t|c|t|g|c|c|c|g|t|g|c|c|c|a|c|t|g|a|c|a|t|g|t|a|g|g|g|g|a|g|a|g|g|g|g|a|a|g|a|t|g|ei
c|c|t|g|a|c|g|t|c|a|c|a|g|a|a|g|c|c|c|t|c|t|g|c|t|c|c|t|c|a|c|t|t|t|g|c|g|t|g|g|c|g|t|c|a|a|c|a|c|g|g|a|c|a|g|c|g|g|ei
g|t|g|c|a|g|c|a|a|g|g|a|g|a|a|g|a|g|t|t|t|g|a|c|a|c|g|g|g|t|a|a|g|g|c|a|c|t|g|a|c|c|c|a|a|g|t|g|g|g|g|a|t|c|c|t|g|g|ei
g|a|t|a|g|a|g|c|a|g|t|t|t|t|g|a|a|a|c|a|c|t|c|t|t|t|g|t|g|g|a|a|a|a|t|g|c|a|a|g|t|g|g|a|t|a|t|t|t|g|g|a|t|a|g|c|t|t|ei
c|c|a|c|c|a|g|a|c|c|t|g|g|g|c|c|a|g|a|t|a|c|t|t|t|g|a|a|g|t|a|a|g|g|g|a|t|c|a|g|c|a|a|g|g|a|t|g|t|g|g|g|a|t|c|a|g|g|ei
t|t|t|c|c|a|t|c|c|t|t|c|t|t|t|c|t|g|t|g|g|a|c|g|g|t|a|g|a|c|a|g|t|c|t|c|c|c|a|c|a|g|g|c|t|g|c|g|g|c|t|g|t|a|c|g|a|g|ei
t|g|a|g|c|g|g|g|a|a|c|g|c|c|t|a|c|a|t|t|c|t|t|c|c|c|a|g|c|t|g|a|g|c|a|g|a|a|g|a|g|t|c|a|g|a|c|g|g|a|a|t|c|g|a|a|a|c|ei
g|c|t|c|t|c|a|c|t|a|g|a|a|a|a|g|t|c|c|a|c|a|a|t|c|c|a|g|g|t|g|t|g|t|g|t|g|t|g|t|g|g|g|t|g|a|a|a|a|g|a|g|t|g|g|g|c|t|ei
t|t|c|t|a|t|g|t|c|t|t|g|g|g|t|c|t|c|t|t|c|t|g|c|g|c|t|c|t|t|t|g|c|c|t|c|t|g|t|g|g|t|c|c|t|c|a|t|c|c|t|g|c|t|g|c|t|g|ei
g|a|g|g|g|a|c|t|g|a|a|g|c|c|c|a|g|t|c|a|t|g|c|c|a|c|a|g|g|a|g|a|t|c|c|g|t|g|a|g|t|t|g|c|a|g|g|c|t|c|a|g|c|t|t|c|a|g|ei
c|c|c|a|g|g|a|c|t|c|a|c|a|c|a|t|t|t|c|t|g|c|t|c|t|c|a|g|g|g|t|t|g|g|g|g|g|t|g|c|c|c|a|c|g|g|t|g|a|c|a|g|c|c|a|c|c|a|ei
t|g|t|t|a|c|c|t|c|a|c|c|t|t|c|g|g|a|g|a|c|a|a|a|c|a|a|g|g|t|g|c|c|t|c|a|c|a|g|c|c|c|c|t|c|a|g|g|c|c|c|a|c|c|c|c|c|a|ei
a|t|g|g|t|t|a|t|g|g|a|g|g|c|a|t|c|g|c|t|t|t|g|c|g|a|a|t|g|t|g|a|g|t|t|c|c|c|t|g|c|c|t|c|t|g|t|g|t|t|t|c|a|t|c|c|a|t|ei
g|a|g|g|t|g|g|g|c|g|g|c|a|g|c|g|t|c|g|c|c|g|g|t|c|c|a|g|a|c|a|c|c|a|a|t|g|g|g|a|a|t|c|c|c|a|a|t|g|g|g|g|a|a|g|t|c|g|ei
g|c|c|a|t|g|g|a|g|g|a|t|g|a|a|c|c|a|t|c|c|a|a|g|c|a|a|t|g|t|g|a|g|c|c|c|a|c|a|c|g|c|c|t|g|a|c|c|c|g|g|g|a|a|c|a|g|c|ei
g|c|t|g|a|g|t|g|g|a|c|t|g|c|g|t|t|g|t|c|a|g|g|a|t|g|a|g|t|g|c|t|c|c|a|t|c|a|t|c|g|g|g|a|g|a|a|t|c|c|a|a|g|c|a|g|g|a|ei
t|t|g|t|a|t|t|a|a|a|g|g|a|a|c|a|g|a|c|g|g|g|c|c|g|a|t|g|g|t|a|t|g|t|a|t|a|a|a|g|g|a|c|g|a|a|t|c|a|c|t|t|c|a|t|g|t|a|ei
c|a|c|c|c|a|a|c|c|t|g|a|t|g|c|c|c|c|a|c|c|a|t|t|g|c|a|g|g|c|a|c|t|g|c|c|a|g|g|g|g|c|a|t|t|g|t|g|a|t|t|g|c|c|a|c|a|g|ei
g|t|g|a|a|c|a|c|t|t|c|t|g|g|g|t|t|t|g|c|c|c|c|g|a|c|g|c|c|c|c|c|c|t|c|c|a|c|a|g|c|c|c|a|g|g|a|g|c|a|c|c|a|c|g|t|t|c|ei
a|g|g|a|g|a|g|g|a|a|t|a|g|g|t|t|t|g|g|g|a|a|a|a|a|t|c|c|t|g|c|t|g|a|c|a|t|t|g|g|a|a|a|c|c|c|c|a|a|g|g|a|a|g|c|c|t|c|ei
g|g|g|g|a|a|a|a|c|a|t|a|a|g|a|c|c|a|t|t|t|a|t|a|t|a|g|g|t|g|a|g|t|c|g|a|g|c|a|t|c|t|g|t|a|g|g|a|a|c|a|a|a|t|g|c|a|a|ei
a|g|a|g|c|c|c|c|c|c|t|c|a|a|c|t|c|t|g|t|t|c|t|c|c|t|a|g|g|g|g|c|t|c|c|c|t|g|g|t|g|t|t|g|g|c|c|t|c|a|c|a|c|c|t|t|c|a|ei
g|c|a|t|c|a|c|t|a|a|g|g|g|a|g|g|g|c|t|c|t|g|t|c|c|t|a|g|g|t|a|t|g|g|a|a|t|c|t|t|g|c|g|g|c|a|t|c|c|a|c|g|a|g|a|c|c|a|ei
t|g|t|t|t|t|c|t|a|g|g|a|a|g|a|t|g|t|g|g|a|c|a|g|c|a|g|t|g|a|a|g|g|c|c|g|c|c|c|g|g|g|c|c|g|c|c|t|t|c|c|a|g|c|t|g|g|g|ei
a|a|t|c|a|a|t|t|a|t|c|t|t|t|a|t|t|t|t|t|g|c|t|g|t|a|t|g|a|a|a|c|c|a|c|g|a|g|c|a|g|t|g|t|t|c|t|c|t|c|c|t|t|c|a|t|t|a|ei
c|t|g|t|a|a|g|a|c|t|t|c|c|t|a|c|t|t|a|t|t|a|t|g|t|a|c|c|a|t|a|c|t|t|t|c|c|t|t|t|a|a|a|t|t|t|t|a|g|t|g|g|a|a|a|t|t|t|ei
c|c|t|g|g|g|t|g|c|t|t|a|g|c|c|c|g|t|a|a|c|c|c|a|t|c|c|a|t|c|c|t|a|g|a|c|c|c|c|t|g|t|c|c|t|c|t|g|t|g|a|g|g|c|c|t|c|c|ei
t|c|t|g|a|g|g|a|t|g|t|g|a|a|a|c|t|t|a|a|a|t|t|g|a|g|a|g|g|t|a|a|t|t|t|a|g|a|a|c|a|a|a|a|c|t|g|t|a|a|t|a|c|t|c|a|g|t|ei
c|c|c|a|g|g|a|g|g|g|g|t|g|g|a|c|c|c|a|c|a|g|c|c|g|g|g|a|g|g|c|c|g|a|a|a|g|c|g|c|g|g|g|c|g|g|g|c|a|g|g|c|a|g|a|g|g|c|ei
c|t|a|c|a|t|g|g|g|c|t|c|c|a|g|g|g|g|c|a|g|c|a|c|a|a|g|a|c|c|a|g|a|t|g|g|c|c|a|a|g|g|t|g|c|t|t|c|a|g|t|t|t|a|a|t|g|a|ei
g|c|a|g|a|g|g|c|a|g|t|g|g|g|g|g|t|g|g|g|c|a|g|a|t|t|a|c|a|g|a|a|a|a|t|c|t|g|t|g|a|t|g|a|g|a|c|a|c|c|a|c|a|a|a|a|c|c|ei
c|c|a|g|t|g|a|a|g|t|c|c|a|a|a|t|t|c|c|g|g|a|t|t|g|a|t|g|t|t|g|a|c|c|t|c|g|g|a|a|c|a|a|t|c|c|t|c|a|g|a|g|t|t|a|a|t|g|ei
t|c|g|g|a|g|c|g|g|c|g|g|g|c|c|c|c|a|g|g|c|a|a|c|t|g|c|a|c|g|a|c|g|c|c|t|g|c|c|a|g|g|g|c|g|a|t|t|c|g|g|g|a|g|g|c|c|c|ei
t|c|c|t|g|a|c|c|c|t|g|g|c|c|c|t|g|g|t|g|g|c|t|t|g|c|c|g|g|t|g|a|g|t|a|g|a|a|g|c|t|g|t|c|t|t|t|g|g|a|t|g|g|c|a|c|t|c|ei
c|a|g|t|t|c|a|t|t|c|g|t|c|t|t|t|t|t|c|c|t|t|c|g|a|a|g|t|c|t|g|g|g|t|g|t|a|a|a|g|g|g|a|t|g|g|a|g|a|g|a|g|g|t|g|a|g|g|ei
c|c|g|c|g|c|c|c|t|g|g|t|t|c|c|c|c|a|g|g|g|c|c|c|g|c|g|g|a|c|g|t|g|g|t|c|c|a|t|c|c|c|c|t|t|c|t|g|c|a|t|c|c|t|c|c|g|c|ei
g|t|a|c|t|g|t|t|t|a|t|c|t|t|t|t|t|a|t|g|a|c|t|a|t|t|a|t|t|t|c|c|c|t|t|a|g|c|a|t|a|g|t|g|c|a|t|t|c|a|a|a|g|t|c|c|a|a|ei
c|c|a|t|g|c|t|g|t|g|c|a|a|c|a|t|a|g|t|g|a|a|a|c|c|c|t|c|t|c|t|a|c|a|a|a|a|a|a|t|a|c|a|a|a|a|g|t|t|a|g|c|t|g|g|g|c|a|ei
a|g|g|a|t|t|t|t|a|g|t|t|c|t|g|a|g|c|a|g|g|g|c|g|a|c|t|g|c|g|c|c|c|c|a|g|g|a|c|c|a|g|a|a|a|g|c|c|a|g|t|a|t|c|c|a|g|a|ei
g|t|c|t|c|t|c|t|c|t|c|t|c|t|c|t|c|t|c|t|t|t|c|c|g|c|a|g|g|t|t|c|t|c|c|c|c|a|t|g|a|c|a|c|c|a|c|c|t|g|a|a|c|g|t|c|t|c|ei
a|c|a|t|c|t|t|c|a|g|t|g|t|c|t|a|g|a|a|g|a|a|g|a|t|c|a|a|a|c|c|t|c|t|g|g|a|g|g|a|a|g|t|g|c|t|a|a|a|t|t|t|a|g|c|t|c|a|ei
t|g|c|t|g|a|c|c|t|t|g|g|c|c|g|t|g|c|t|c|t|t|c|t|a|c|g|g|g|t|a|g|g|t|g|t|c|c|c|c|t|a|a|c|c|t|a|g|g|a|g|c|c|a|a|c|c|a|ei
g|t|a|g|c|c|t|c|a|c|t|c|c|c|a|g|c|c|c|t|t|g|t|t|t|c|a|g|g|a|t|g|t|g|t|t|c|t|g|g|g|c|c|a|a|g|t|a|c|a|c|a|g|g|t|g|a|g|ei
c|c|c|c|c|t|g|c|t|c|c|t|c|c|c|c|c|a|t|c|a|t|g|c|c|c|a|g|a|t|g|a|a|g|t|t|c|g|c|a|c|t|g|g|c|a|c|c|t|a|c|c|g|c|c|a|g|c|ei
g|t|t|a|c|c|t|a|t|t|g|t|g|c|a|t|c|t|t|t|t|t|a|a|a|c|t|t|g|a|t|t|a|t|g|t|a|a|c|c|a|t|a|a|a|t|c|t|g|a|c|a|g|c|a|t|g|t|ei
t|c|t|c|c|t|c|a|g|t|a|a|t|c|t|a|g|g|a|t|t|c|a|t|a|c|a|g|g|t|a|t|g|a|t|t|c|c|a|g|t|t|t|a|t|t|a|t|c|c|a|t|c|a|a|a|g|g|ei
c|a|a|c|t|g|g|g|g|a|c|c|t|c|a|c|c|c|t|c|c|c|a|c|c|c|a|g|g|a|a|c|c|a|t|g|a|a|c|g|c|t|g|c|c|t|g|t|g|a|g|c|t|g|c|t|g|g|ei
c|t|g|a|a|a|t|c|c|g|g|c|a|t|g|t|t|c|t|t|g|t|c|c|c|t|g|g|g|t|a|a|g|g|t|t|c|t|g|t|g|t|c|c|t|t|g|t|c|c|t|t|g|a|g|c|t|g|ei
a|g|c|a|g|a|a|c|g|c|t|a|a|g|t|a|t|g|t|a|a|c|g|a|c|c|t|t|c|a|t|g|a|a|g|c|a|g|t|t|g|a|t|a|g|g|t|a|g|g|c|t|t|a|a|a|c|a|ei
c|t|c|a|c|a|t|t|t|a|a|g|t|t|t|t|a|c|a|t|g|c|c|a|g|a|a|g|g|t|a|a|g|t|a|c|a|a|t|a|t|t|t|t|a|t|g|t|t|c|a|a|t|t|t|c|t|g|ei
t|a|a|c|c|a|a|g|t|a|a|c|g|a|c|t|c|t|t|a|a|t|c|t|a|c|a|g|a|t|g|g|g|a|a|a|g|g|g|c|t|c|c|t|t|c|a|a|g|t|a|t|g|c|c|t|g|g|ei
c|g|g|g|c|g|g|g|t|c|t|g|g|a|a|a|a|a|a|a|t|t|a|t|c|c|g|t|a|a|c|c|c|t|g|a|t|g|g|t|g|a|t|g|t|a|g|g|t|g|g|t|c|c|c|t|g|g|ei
c|c|c|c|a|t|c|a|c|c|a|g|c|t|c|c|c|c|c|c|t|t|c|c|c|c|a|g|a|t|c|a|c|t|g|g|c|a|a|g|t|g|g|t|t|t|t|a|t|a|t|c|g|c|a|t|c|g|ei
t|c|a|t|g|a|c|a|a|t|g|a|a|g|a|g|a|c|a|t|t|t|t|g|a|a|a|a|g|t|a|a|g|t|a|a|t|c|a|g|a|t|g|t|t|t|a|t|a|g|t|t|c|a|a|a|a|t|ei
g|a|a|c|g|a|c|a|a|t|a|g|c|t|t|t|a|c|c|c|t|c|a|g|a|t|a|g|g|c|c|t|g|g|g|t|g|c|t|g|g|c|t|g|c|c|c|a|g|a|c|c|c|c|t|c|t|g|ei
t|g|c|c|c|c|t|g|c|t|g|c|g|a|t|g|a|c|c|c|t|g|t|g|c|a|c|t|t|c|t|g|c|t|g|t|t|c|c|t|g|c|c|a|c|c|g|c|t|g|c|t|g|c|t|g|c|t|ei
t|a|c|a|a|t|g|a|t|g|g|t|c|g|c|t|t|t|c|c|t|c|t|t|t|c|a|g|g|c|c|t|g|t|g|g|t|c|a|a|a|t|c|g|g|g|a|g|a|c|a|a|g|c|c|c|a|g|ei
t|g|c|t|g|a|c|c|t|t|g|g|c|c|g|t|g|c|t|c|t|t|c|t|a|c|g|g|g|t|a|g|g|t|g|t|c|c|c|c|t|a|a|c|c|t|a|g|g|g|a|g|c|c|a|a|c|c|ei
t|t|g|g|a|g|a|t|a|a|a|c|t|t|c|c|t|g|a|a|t|g|t|a|g|c|a|g|g|t|g|g|g|t|g|c|t|g|a|g|c|a|c|t|t|a|a|g|a|g|a|g|c|a|g|g|c|a|ei
g|t|g|a|t|g|c|a|g|g|c|c|t|a|a|t|t|c|a|t|a|a|a|g|a|g|c|a|c|t|g|c|c|a|g|c|t|c|t|t|t|a|t|t|c|a|g|t|g|c|t|t|t|g|c|c|a|a|ei
g|a|a|g|g|a|c|t|g|g|g|g|a|a|g|a|c|t|g|g|a|t|g|g|a|g|g|g|t|a|g|a|a|g|a|g|g|g|t|g|g|g|t|g|t|g|g|g|a|t|g|g|g|g|a|g|g|g|ei
c|a|g|c|t|g|c|t|a|c|t|g|g|t|t|c|t|c|t|c|g|c|t|c|g|g|a|a|g|g|c|c|t|g|g|g|c|t|g|a|c|g|c|c|g|a|c|a|a|c|t|a|c|t|g|c|c|g|ei
a|c|t|t|g|t|g|a|t|t|g|a|c|t|t|t|a|a|a|c|t|t|g|t|g|c|a|g|g|c|t|g|g|t|g|c|a|g|a|c|a|t|c|t|c|c|a|t|g|a|t|t|g|g|g|c|a|g|ei
t|c|a|g|g|t|t|g|t|c|t|g|a|a|g|t|c|a|c|t|g|c|a|a|t|g|c|a|t|c|t|c|a|g|c|c|c|a|c|a|t|a|g|t|g|a|t|g|g|t|t|c|c|c|c|t|g|t|ei
g|t|a|t|c|g|g|g|g|a|a|g|t|c|c|t|g|g|c|c|a|a|g|g|g|a|g|a|t|c|t|t|c|c|t|c|t|t|c|c|t|g|g|c|c|a|t|c|c|t|g|c|t|a|c|a|g|c|ei
c|t|g|g|g|g|a|c|a|c|c|c|g|a|c|c|a|c|g|t|t|t|c|t|t|g|g|c|a|g|c|c|t|a|a|g|a|g|g|g|a|g|t|g|t|c|a|t|t|t|c|t|t|c|a|a|t|g|ei
g|c|a|c|c|c|a|t|g|a|c|c|t|g|g|c|t|c|t|c|c|c|c|t|c|c|a|g|g|a|g|g|c|t|g|t|g|a|a|g|a|g|c|g|g|c|a|t|t|c|a|c|c|g|t|a|c|t|ei
g|a|c|t|c|c|a|c|t|g|t|c|c|c|t|g|t|c|c|a|t|c|a|c|c|c|g|g|a|g|a|g|c|c|g|g|c|c|t|c|c|a|t|c|t|c|c|t|g|c|a|g|g|t|c|t|a|g|ei
t|c|c|t|g|g|g|t|t|c|a|t|g|c|c|a|t|t|c|t|c|c|t|c|t|c|a|g|c|c|t|c|c|c|g|a|g|t|a|a|g|c|t|g|g|g|a|a|t|a|c|a|g|g|c|a|c|c|ei
c|c|g|c|g|t|c|a|c|c|a|g|g|c|c|t|g|t|c|c|t|t|g|g|c|c|a|g|g|g|a|c|a|t|c|t|c|g|c|c|c|g|t|c|c|t|g|a|a|g|g|a|c|c|c|c|g|c|ei
t|g|t|g|a|a|t|g|t|g|g|a|g|t|t|a|t|a|t|g|t|g|t|c|t|a|c|a|t|g|t|a|t|g|t|g|g|g|g|g|t|g|g|t|a|t|g|c|a|t|a|t|a|t|g|g|g|t|ei
c|t|t|c|g|c|g|g|a|g|g|c|g|t|g|g|a|a|g|g|c|g|c|g|t|c|c|c|g|g|a|c|t|c|a|g|a|g|c|c|c|c|c|g|c|g|c|a|t|g|g|a|g|c|t|g|c|g|ei
c|c|g|c|c|c|g|t|c|g|c|t|a|c|t|a|c|c|g|a|t|t|g|a|g|g|t|t|t|a|g|t|g|a|g|g|c|c|c|t|c|g|g|a|t|c|g|g|c|c|c|c|g|c|c|g|g|g|ei
c|c|t|c|t|c|a|g|g|g|t|g|t|c|c|c|c|t|t|c|c|t|g|c|c|c|a|g|a|c|a|a|g|g|a|t|g|a|c|c|a|g|c|t|g|a|t|c|t|g|t|g|t|g|a|a|c|g|ei
g|g|c|c|t|c|a|c|a|c|a|g|c|c|t|t|c|c|g|g|t|g|t|c|a|c|a|g|a|t|t|c|c|a|a|c|c|c|g|a|g|a|g|g|g|t|t|g|a|g|c|g|c|c|t|a|c|c|ei
a|a|c|c|t|g|a|t|g|a|a|c|a|t|c|a|c|c|c|g|g|g|g|t|t|g|t|c|c|g|c|a|t|c|g|a|g|a|a|g|a|a|c|a|a|t|g|a|g|c|t|c|t|g|t|t|a|c|ei
g|t|t|c|t|a|g|a|c|c|t|c|t|c|c|a|c|g|a|a|t|g|t|t|c|a|g|c|a|a|c|t|t|g|t|a|c|a|a|c|t|g|g|t|c|c|g|c|c|t|c|c|t|a|c|a|g|t|ei
a|c|a|c|t|g|c|c|a|t|g|t|t|c|t|g|c|c|c|t|g|t|c|t|a|c|a|g|g|g|a|g|c|t|c|a|g|c|c|c|g|c|t|g|g|a|c|t|t|a|t|a|a|t|g|c|c|a|ei
g|c|t|c|a|g|c|c|c|c|c|a|g|g|t|c|a|c|c|c|a|g|g|a|t|g|a|c|g|t|g|a|g|t|g|t|c|c|c|c|a|t|c|c|c|g|g|c|c|c|t|t|g|a|c|c|c|t|ei
a|a|a|g|t|c|a|g|c|t|c|c|a|c|t|g|a|a|g|c|t|g|t|g|c|c|g|g|g|a|t|g|c|g|g|c|t|c|g|t|a|g|c|a|t|c|c|g|c|a|a|c|g|a|c|t|g|g|ei
g|g|a|c|a|g|c|t|c|a|c|c|t|a|g|c|g|g|c|a|a|t|g|c|g|c|a|g|g|t|a|a|g|c|g|c|c|c|c|t|a|a|a|a|t|c|c|t|t|t|g|g|g|c|a|c|a|a|ei
a|g|a|g|a|a|a|g|t|t|g|g|t|g|g|c|g|a|g|g|c|c|t|g|g|c|a|g|g|t|t|g|g|t|a|t|c|g|g|g|g|t|t|a|t|a|g|g|g|c|a|g|g|c|t|t|a|a|ei
c|t|c|c|a|t|g|c|t|c|c|c|a|c|a|t|c|t|t|c|c|a|t|t|t|c|a|g|a|t|c|a|c|c|t|t|c|t|a|c|g|a|g|g|a|c|a|g|g|g|c|c|t|t|c|c|a|g|ei
a|c|c|t|t|t|t|t|t|a|t|t|c|t|c|c|t|c|t|t|t|c|t|t|c|c|a|g|g|t|g|t|g|c|c|t|g|a|c|c|c|t|g|a|c|a|g|c|c|a|a|g|c|g|c|a|t|g|ei
g|a|g|a|a|a|a|g|a|c|a|g|c|t|c|c|g|a|t|g|c|c|g|c|g|c|a|g|c|a|g|t|t|g|c|a|g|a|a|a|a|g|a|a|t|t|g|c|a|t|a|c|c|t|c|a|g|t|ei
g|t|t|g|g|g|g|a|a|a|t|g|c|a|t|t|g|t|c|a|g|a|a|a|t|g|c|c|t|g|t|g|t|t|c|t|a|c|c|t|g|t|a|c|t|g|a|t|g|g|a|t|g|g|c|a|t|a|ei
t|c|c|a|a|c|a|t|g|g|a|g|g|a|a|a|c|g|c|a|a|c|a|a|a|t|c|c|g|t|g|a|g|t|g|g|a|t|g|c|c|g|t|c|t|c|c|c|c|t|a|g|g|c|g|g|g|g|ei
a|c|t|t|t|g|g|g|t|a|c|t|g|c|g|a|c|c|t|c|a|a|c|a|t|g|t|g|g|t|g|a|g|c|t|g|c|c|t|g|g|g|t|a|g|g|g|g|g|c|c|t|g|a|g|t|t|g|ei
g|g|a|c|a|g|c|t|c|a|c|c|t|a|g|c|t|g|c|a|a|t|g|c|a|c|a|g|g|t|a|a|g|c|g|c|c|c|c|t|a|a|a|a|t|c|c|c|t|t|t|g|g|c|a|c|a|a|ei
t|g|g|c|c|g|a|c|a|c|a|c|g|c|t|t|c|g|a|c|a|t|g|t|c|a|g|c|t|c|a|t|c|g|a|c|g|t|g|g|c|c|c|g|g|c|a|g|a|c|t|g|c|c|c|a|g|g|ei
t|g|c|a|g|c|g|c|c|a|g|a|c|a|t|t|t|t|g|c|a|c|a|a|g|g|c|a|c|c|a|a|a|c|a|g|c|c|c|a|g|g|a|c|t|g|c|c|g|a|g|a|c|t|c|t|g|g|ei
t|a|a|t|a|t|a|c|a|a|a|a|t|c|a|t|a|t|a|t|a|t|a|a|a|t|g|t|t|c|t|t|g|t|t|t|t|t|t|g|a|g|a|c|a|g|a|g|t|c|t|c|a|c|a|c|t|g|ei
c|c|g|t|g|a|g|c|c|g|a|a|a|t|c|g|c|g|c|c|a|c|t|c|c|t|c|a|c|c|g|c|a|c|c|c|g|g|c|c|a|a|t|t|t|t|t|g|t|g|t|t|t|t|t|a|g|t|ei
a|t|g|g|c|t|c|t|t|a|a|t|t|a|t|t|a|t|c|t|t|t|g|a|t|a|t|t|t|g|g|g|c|t|a|a|c|a|g|t|g|a|t|g|c|t|a|t|t|t|g|t|a|t|t|c|t|t|ei
g|a|g|g|g|g|g|a|t|g|g|g|g|g|g|g|c|a|g|a|t|c|t|g|a|c|t|c|a|t|g|a|g|g|a|g|g|g|g|c|c|c|c|c|c|t|g|c|c|c|a|g|a|g|g|g|g|t|ei
a|g|c|t|g|a|a|g|c|c|g|t|g|c|c|t|g|g|c|t|g|t|c|t|g|c|a|g|a|t|c|a|t|c|g|c|a|c|c|c|c|c|a|g|a|g|c|g|c|a|a|g|t|a|c|t|c|a|ei
g|g|g|a|c|g|c|c|a|c|a|c|t|c|g|c|c|c|t|t|c|t|c|c|a|g|g|g|g|a|c|g|c|c|a|c|a|c|t|c|g|c|c|c|t|t|c|t|c|t|c|c|a|g|g|g|g|a|ei
a|a|g|a|a|a|c|t|t|g|a|t|t|t|c|a|a|a|g|t|t|t|c|a|t|a|c|a|t|c|a|a|a|t|a|a|t|c|t|g|a|t|t|t|c|a|a|c|a|a|t|t|c|c|a|t|c|a|ei
c|a|a|c|c|c|g|c|c|c|t|g|a|t|c|c|t|t|t|t|a|a|g|a|t|t|g|g|c|g|a|t|t|t|g|g|c|t|t|t|t|t|g|a|a|a|a|g|c|a|a|t|a|a|t|a|c|a|ei
a|a|t|c|c|a|g|g|t|g|c|a|a|a|a|c|g|a|a|t|t|c|t|g|g|c|t|t|g|a|c|c|a|g|t|t|t|a|a|g|g|g|g|c|a|g|c|a|g|g|g|a|c|a|a|a|a|a|ei
g|c|a|g|g|t|a|g|g|t|c|c|a|a|g|c|t|g|c|c|c|c|g|c|a|a|a|c|a|t|c|c|t|c|t|t|c|c|t|t|g|t|c|t|g|g|a|g|c|c|t|g|g|a|g|g|a|g|ei
t|c|t|c|a|t|a|c|c|t|t|t|t|c|t|c|t|g|g|g|g|t|c|t|c|c|a|g|g|t|a|t|g|a|g|a|c|a|g|a|g|t|t|g|a|a|c|c|t|g|c|g|c|a|t|g|a|g|ei
a|g|g|a|a|g|g|g|g|t|g|a|c|a|g|t|g|c|t|t|a|t|a|a|g|a|a|g|a|c|a|a|a|g|a|g|t|t|g|g|c|t|g|a|g|c|t|g|c|g|a|g|g|t|c|t|g|g|ei
c|a|c|t|a|c|t|g|c|t|a|c|c|c|t|c|a|t|t|t|c|a|c|t|c|g|c|t|g|t|g|g|a|c|a|c|t|g|a|g|a|a|c|a|t|c|c|g|c|c|g|t|g|t|g|t|t|c|ei
c|a|g|c|t|g|c|c|a|c|c|c|g|g|c|t|g|c|g|g|c|g|a|c|c|a|a|g|c|g|c|c|t|c|g|g|g|c|c|c|c|t|g|c|g|c|g|g|c|t|t|c|c|a|g|t|g|g|ei
t|c|c|t|c|g|c|g|t|c|g|c|g|g|g|t|g|t|g|c|c|c|g|a|a|g|g|c|t|g|a|g|c|a|g|c|c|t|g|c|g|c|c|t|g|a|g|c|t|g|g|t|g|g|a|g|g|t|ei
c|t|c|g|c|g|t|c|g|c|a|t|t|t|g|g|c|c|g|c|c|t|c|c|a|c|c|g|g|t|g|a|g|t|t|c|t|c|t|c|c|a|g|g|a|g|c|c|c|t|g|g|g|t|a|c|t|t|ei
t|g|g|g|a|t|a|g|a|a|a|c|t|c|a|c|t|t|c|c|t|a|c|t|c|c|a|g|a|t|g|g|a|a|t|g|c|t|c|t|c|t|g|c|a|g|g|c|c|a|a|g|c|c|c|g|c|a|ei
t|g|t|g|g|a|c|a|a|g|t|a|c|a|a|c|g|t|g|a|g|c|g|c|c|c|a|a|c|g|g|g|a|c|c|t|g|c|c|t|g|c|t|g|g|c|c|a|g|c|a|t|g|g|g|g|c|t|ei
c|g|c|c|g|a|g|c|g|g|c|c|t|c|c|a|g|g|g|c|c|c|c|c|g|a|c|c|c|g|a|g|c|g|c|g|g|t|c|c|c|c|g|g|g|g|c|a|a|a|g|g|c|a|a|g|g|c|ei
t|c|c|a|a|c|a|g|g|g|a|g|g|a|a|a|c|a|c|a|a|c|a|a|a|t|c|c|g|t|g|a|g|t|g|g|a|t|g|c|c|t|t|c|t|c|c|c|c|a|g|g|c|g|g|g|g|a|ei
t|t|c|a|a|a|t|c|a|t|a|a|a|g|g|a|c|c|c|a|c|t|t|a|a|t|g|c|c|a|t|c|a|c|t|c|a|c|t|a|c|c|a|t|t|t|c|a|c|a|a|t|t|c|g|c|a|c|ei
a|g|g|c|t|g|c|c|t|a|t|c|a|g|a|a|g|g|t|g|g|t|g|c|g|g|t|g|t|g|g|c|t|g|c|t|g|c|t|c|t|g|g|c|t|c|a|c|a|a|g|t|a|c|c|a|t|t|ei
t|g|g|t|g|a|c|c|g|g|g|a|g|c|g|t|g|g|g|a|g|g|a|t|a|t|g|g|g|t|g|a|g|t|g|g|t|a|g|g|g|a|g|t|g|g|c|c|t|c|g|g|c|a|g|c|t|c|ei
t|a|a|a|a|a|a|c|a|t|c|a|a|a|a|a|a|c|a|a|t|t|c|c|t|t|g|c|t|t|c|c|a|t|g|a|a|t|t|a|t|g|g|t|t|a|g|t|g|c|c|t|g|g|t|t|t|t|ei
a|t|g|a|a|t|t|t|g|t|t|c|a|t|g|a|a|t|a|t|t|t|t|c|g|t|a|g|t|g|t|g|a|a|a|c|a|g|c|t|g|c|c|c|t|g|t|g|t|g|g|g|a|c|t|g|a|g|ei
c|c|a|c|a|c|c|c|c|t|t|c|c|t|c|a|a|g|t|g|c|a|g|g|c|c|a|g|c|c|t|t|g|c|c|a|t|g|g|a|c|c|c|a|c|a|g|c|g|g|c|c|c|c|t|g|g|t|ei
c|g|c|a|c|a|c|g|g|g|g|g|g|c|a|c|a|g|c|g|c|c|t|c|t|c|g|c|g|a|g|c|c|g|g|t|g|c|g|a|a|a|g|g|g|g|c|c|g|c|c|t|g|c|g|g|t|g|ei
t|a|a|a|t|a|a|t|t|t|t|a|a|g|a|a|a|g|c|t|g|g|t|c|c|a|a|g|g|t|g|c|c|a|c|a|t|t|t|g|a|t|g|a|a|a|g|c|a|a|a|a|t|a|c|a|g|t|ei
c|c|g|c|g|g|c|a|c|a|g|a|g|c|c|a|g|g|g|g|c|c|a|c|c|t|a|c|c|c|a|g|c|t|c|c|c|a|c|g|c|t|c|t|g|g|g|a|t|c|c|g|t|c|t|g|c|c|ei
g|t|a|t|g|g|g|c|c|a|g|g|a|g|a|a|a|g|g|g|g|a|a|t|a|g|a|g|g|t|g|a|g|t|g|g|c|t|c|t|g|c|c|a|g|c|c|a|t|t|t|g|c|c|t|g|g|g|ei
c|t|g|c|c|a|c|a|t|g|a|c|a|c|c|c|c|c|t|c|a|a|t|t|c|c|a|g|g|t|c|t|c|t|g|g|a|c|a|c|t|a|t|g|g|g|c|a|c|a|c|g|a|c|t|c|c|t|ie
g|c|t|g|a|t|a|a|a|g|a|c|a|t|a|c|c|t|g|a|g|a|c|g|g|t|a|a|t|t|a|c|a|a|a|a|g|a|a|a|g|g|t|t|t|a|t|t|g|g|a|c|t|c|a|c|a|g|ei
g|c|g|a|a|g|c|c|c|t|c|c|t|c|c|t|t|c|t|c|c|c|c|g|c|g|g|t|g|c|a|c|a|g|g|c|c|t|c|t|g|c|c|t|g|c|t|g|g|g|g|a|t|t|a|c|t|c|ei
c|t|t|c|a|c|t|g|c|t|a|c|a|g|a|g|c|c|a|t|a|g|t|c|a|g|c|c|a|g|g|a|g|a|a|a|a|c|t|t|c|t|a|a|t|t|c|a|a|g|t|a|g|c|c|t|a|t|ei
t|c|a|t|t|g|g|g|g|a|g|a|g|c|a|c|c|a|t|c|c|g|c|g|a|c|a|a|g|t|g|a|c|c|c|t|c|a|t|g|g|g|a|a|t|g|g|g|g|t|t|t|g|g|a|g|c|a|ei
t|c|c|c|t|g|c|c|a|g|c|c|a|c|a|c|a|c|c|t|g|c|t|t|c|c|a|g|a|t|c|t|g|c|c|c|c|t|g|g|t|c|c|a|g|c|t|a|c|c|t|c|a|c|t|g|g|t|ei
c|t|g|a|g|g|a|t|t|c|c|t|g|t|t|c|c|t|g|t|a|c|a|a|a|a|a|t|g|t|a|a|g|t|t|a|a|a|t|t|a|t|g|a|t|t|c|a|g|t|a|a|a|a|t|g|a|t|ei
t|g|c|t|g|g|c|a|t|g|g|g|t|t|g|c|t|c|t|g|g|c|t|a|c|a|a|g|g|t|a|c|a|g|g|g|g|a|t|g|t|t|g|g|t|g|g|c|c|a|t|c|t|g|g|g|t|c|ei
a|c|a|g|g|c|c|t|t|c|c|c|c|t|c|t|t|c|g|t|g|g|g|a|c|g|t|g|a|g|g|a|a|c|c|c|c|a|a|c|c|c|c|a|g|t|g|c|a|c|c|g|c|g|g|g|a|g|ei
g|c|g|g|g|c|c|g|g|a|g|c|a|c|g|g|g|c|a|c|c|c|a|c|t|g|g|g|g|g|t|a|c|t|g|c|t|c|a|c|a|c|a|g|a|g|g|a|c|g|c|t|g|c|t|c|a|g|ei
a|c|a|a|c|g|t|g|t|c|t|c|t|g|c|t|t|c|t|c|t|c|c|c|c|c|a|g|g|c|c|g|t|g|c|a|t|a|a|g|g|c|t|g|t|g|c|t|g|a|c|c|a|t|c|g|a|c|ei
a|a|c|a|g|g|c|g|c|t|a|c|g|a|g|g|t|g|c|c|c|t|t|g|g|a|c|c|c|c|g|c|g|t|g|t|c|c|a|c|a|g|c|c|g|g|g|c|a|c|c|g|t|c|c|c|c|a|ei
c|a|t|t|a|g|c|a|g|c|a|t|c|c|c|t|c|t|a|c|a|a|g|t|c|a|t|t|t|a|a|c|t|a|t|a|a|g|t|a|t|a|c|t|g|c|c|t|g|c|c|t|a|t|g|t|g|a|ei
a|a|g|t|c|c|a|c|c|t|g|c|c|c|c|a|t|c|c|t|c|t|g|t|c|c|a|g|g|t|g|a|t|c|c|t|a|g|g|t|g|g|a|g|g|c|c|g|a|a|a|g|t|a|c|a|t|g|ei
c|c|c|g|c|c|c|g|g|g|c|c|c|g|c|c|c|g|c|g|t|c|c|t|g|t|a|g|t|t|t|t|g|g|g|a|g|g|t|g|a|t|c|a|g|c|g|a|t|g|a|g|c|a|c|g|g|c|ei
c|c|t|c|t|g|a|t|t|t|t|g|c|t|t|c|c|c|a|c|c|t|t|c|g|c|a|g|g|t|g|g|a|a|g|t|c|a|a|g|a|t|g|g|a|g|g|g|g|g|a|c|t|c|t|g|t|g|ei
c|a|g|t|t|c|a|t|a|g|g|c|t|a|t|c|c|c|a|t|c|a|c|c|t|t|a|t|g|t|g|a|g|t|a|t|g|g|a|c|t|t|t|t|a|a|a|t|c|t|t|t|t|a|c|a|c|t|ei
a|t|g|g|g|g|a|c|a|c|a|g|c|c|a|a|a|c|t|a|t|g|t|a|t|a|a|t|c|a|c|g|g|t|c|g|a|g|a|c|t|a|t|c|t|g|c|a|a|t|t|t|a|g|t|g|a|a|ei
c|a|t|t|a|a|t|t|t|t|g|t|g|c|a|t|t|c|t|t|t|g|g|a|t|t|t|t|t|t|t|t|g|t|t|t|t|t|t|g|t|a|a|c|t|a|c|a|a|a|g|c|t|t|t|g|c|t|ei
g|c|g|g|g|c|t|g|a|g|t|c|c|g|a|a|a|a|g|a|g|a|g|c|g|c|a|a|a|g|g|g|a|g|a|t|a|a|g|g|g|t|g|a|g|g|c|c|a|t|t|t|t|a|t|a|a|g|ei
g|t|g|t|c|c|a|a|c|g|c|a|g|a|c|c|t|g|a|t|g|g|a|t|c|a|a|g|g|t|a|g|g|g|c|c|a|g|g|a|a|a|g|c|g|g|g|t|g|c|a|g|t|c|t|g|g|g|ei
g|c|c|t|g|c|t|g|a|a|c|t|c|a|c|a|c|t|g|t|t|t|c|c|a|c|a|g|c|g|c|a|t|g|a|g|a|g|c|c|c|a|g|c|c|c|g|g|c|a|c|c|c|c|t|g|t|g|ie
a|a|a|a|t|a|c|a|a|a|a|a|t|t|a|g|c|c|n|n|n|g|g|a|g|c|c|g|a|g|a|t|t|a|c|a|a|t|g|a|g|c|t|g|a|g|a|t|c|a|c|a|c|c|a|c|c|a|ei
c|t|c|a|g|t|c|t|c|c|c|t|t|c|t|c|c|t|c|t|c|t|a|c|a|c|a|g|g|g|g|g|a|t|t|c|c|g|g|a|g|g|c|c|c|c|c|t|g|c|t|g|t|g|t|a|a|c|ei
c|c|g|c|c|c|c|t|c|c|g|c|c|g|t|c|g|c|g|t|t|t|c|c|g|c|c|g|g|t|g|a|g|c|g|c|c|c|c|g|c|c|c|c|g|g|g|g|c|c|t|g|a|g|c|t|g|g|ei
a|a|g|g|g|a|t|a|c|t|t|t|g|a|t|a|a|t|t|a|a|g|g|c|g|a|g|g|c|c|c|a|t|t|a|g|t|t|g|a|g|a|a|a|g|t|c|a|c|a|g|a|t|a|t|a|t|t|ei
t|t|t|g|g|a|g|t|g|a|t|c|g|g|c|c|c|c|c|a|g|a|g|g|a|g|a|g|g|t|g|a|g|t|g|c|c|t|g|g|c|c|a|g|c|c|t|t|c|a|t|c|c|a|c|t|c|t|ei
t|c|c|c|t|g|a|c|t|c|t|c|c|g|g|c|t|c|t|c|c|c|t|c|t|c|a|g|g|c|t|g|g|c|c|g|t|g|a|g|t|a|c|t|c|a|c|c|t|g|c|c|g|c|c|a|c|c|ei
a|g|c|t|g|g|a|t|t|t|t|c|c|t|t|g|t|t|g|c|t|a|t|t|a|a|a|a|g|g|t|g|t|c|c|a|g|t|g|t|g|a|g|g|t|g|c|g|a|c|t|g|g|t|g|g|a|g|ei
t|c|t|c|c|t|c|a|g|t|a|a|t|c|t|a|g|g|a|t|t|c|a|t|a|c|a|g|g|t|a|c|g|a|t|t|c|c|a|g|t|t|t|a|t|t|a|t|c|c|a|t|c|a|a|a|g|g|ei
t|c|g|t|c|g|t|g|g|a|t|g|a|t|c|t|g|c|t|g|g|c|c|c|g|g|t|g|g|t|a|a|g|g|g|t|c|t|c|c|c|c|g|c|a|g|c|c|a|a|c|t|c|t|g|t|g|c|ei
c|c|t|c|c|c|c|c|t|a|c|c|c|c|a|g|g|t|g|g|c|c|a|c|a|g|c|t|c|a|a|t|g|a|c|a|c|c|c|a|c|c|c|c|t|c|c|c|t|g|g|c|c|a|t|c|c|c|ei
a|a|a|a|t|a|g|c|t|a|t|t|g|c|t|a|a|t|a|t|t|a|t|g|t|g|a|a|a|t|c|a|t|t|g|a|a|a|a|a|t|t|a|a|a|a|a|g|t|c|t|t|g|a|t|g|a|g|ei
g|c|t|g|c|t|g|c|t|g|c|t|a|a|t|c|t|t|c|a|g|g|g|a|t|g|c|t|g|c|t|g|c|c|t|t|t|a|g|t|c|g|c|t|g|a|g|g|a|a|a|a|a|t|a|a|a|g|ei
g|c|t|g|a|g|g|c|c|t|g|g|c|t|c|t|c|t|c|c|c|t|c|c|a|c|a|g|g|g|t|g|c|c|c|g|g|t|a|c|g|t|g|t|g|g|a|a|c|c|g|c|a|c|t|g|a|g|ei
a|a|g|t|a|g|a|g|c|t|c|a|g|g|g|t|g|t|c|t|c|c|g|t|g|c|a|g|a|c|a|t|a|c|a|a|t|g|t|g|g|a|c|a|g|a|c|a|g|g|t|g|c|c|a|g|a|c|ei
g|t|g|g|a|g|a|t|g|g|g|g|t|c|t|t|g|c|t|a|t|g|t|t|c|c|a|g|g|t|t|g|g|t|c|t|t|g|a|g|t|t|c|c|t|g|g|c|c|t|c|g|a|g|t|g|a|t|ei
g|a|a|g|t|c|a|a|a|c|a|t|t|t|c|a|a|a|g|t|t|t|g|a|t|g|c|a|t|c|a|a|g|t|g|g|c|a|t|g|t|g|c|t|g|t|g|a|c|c|a|t|t|t|a|t|a|a|ei
c|c|c|c|t|g|g|c|t|g|a|t|g|c|c|a|c|t|c|c|t|t|g|c|g|c|a|g|a|g|c|g|t|t|t|c|t|t|g|a|a|t|c|c|a|g|c|g|g|g|g|a|c|c|c|a|g|c|ei
a|g|c|t|g|g|c|t|g|c|t|t|a|g|a|g|a|c|t|g|c|g|a|a|g|g|a|g|g|t|g|c|g|t|c|c|t|g|c|t|g|c|c|t|g|c|c|c|c|g|g|t|c|a|c|t|c|t|ei
t|c|a|a|c|t|a|c|a|g|g|g|a|c|c|c|g|c|a|t|c|t|c|c|a|c|a|g|g|g|t|t|g|g|c|c|c|c|c|a|g|c|a|a|g|g|c|t|c|a|g|g|a|c|a|g|c|a|ei
t|a|a|a|a|g|a|c|g|g|a|a|g|a|t|a|c|a|a|t|a|a|t|c|t|t|c|c|t|t|a|c|a|g|g|g|t|t|c|t|g|a|g|a|c|t|a|c|t|a|a|g|a|g|a|a|c|t|ei
c|a|a|a|g|c|a|c|t|c|a|c|a|t|t|t|t|t|t|a|t|c|t|a|t|c|c|c|t|g|t|a|g|g|t|c|a|g|a|a|g|a|t|a|a|c|c|a|c|c|a|t|g|t|c|a|c|t|ei
g|g|a|g|a|t|g|t|g|c|t|g|g|a|t|t|g|t|c|t|g|c|a|g|t|g|g|g|g|t|g|a|g|g|a|g|t|c|t|t|g|c|t|t|c|t|t|a|a|a|a|t|a|g|a|a|g|a|ei
c|c|a|g|c|t|g|c|a|t|c|a|c|a|g|g|a|g|g|c|c|a|g|g|g|c|a|g|g|t|c|t|g|t|t|c|c|a|a|g|g|g|c|c|t|t|c|g|a|g|c|c|a|g|t|c|t|g|ei
t|t|g|a|c|a|t|a|c|a|t|c|c|a|a|c|a|t|t|a|a|a|a|c|a|c|c|c|c|c|a|a|a|t|g|c|c|c|a|a|g|a|a|a|a|a|a|a|g|a|a|a|g|a|c|t|t|a|ei
a|t|a|c|t|g|a|a|a|a|g|a|g|t|g|a|a|g|g|a|t|a|t|g|a|t|a|c|a|t|c|t|t|t|a|a|a|g|a|g|a|a|a|t|t|t|g|c|t|a|a|a|g|c|t|g|t|g|ei
g|g|c|t|g|c|c|g|a|a|g|c|c|c|c|t|c|a|c|c|c|t|g|g|t|g|g|g|g|t|a|a|g|g|a|g|g|g|g|g|a|t|g|a|g|g|g|g|t|c|a|t|a|t|c|t|c|t|ei
c|c|t|c|c|c|t|g|c|c|c|c|a|t|t|t|c|c|t|a|c|c|c|a|a|c|a|g|g|t|c|c|c|t|g|c|c|a|t|c|t|c|c|t|t|g|g|c|c|t|a|t|g|a|g|g|c|a|ei
c|a|c|a|c|a|g|c|c|t|a|c|t|t|t|c|c|a|a|g|c|g|g|g|c|a|t|g|t|c|t|g|g|t|a|a|c|g|g|c|a|a|t|g|c|g|g|c|t|g|c|a|a|c|g|g|c|g|ei
g|c|t|g|a|g|g|a|t|g|a|a|g|a|a|t|g|g|a|a|g|a|g|t|a|c|g|a|t|c|a|t|t|g|c|t|g|t|c|t|c|c|a|a|c|c|t|t|c|a|c|c|a|g|t|g|g|a|ei
c|t|g|g|a|t|g|a|g|c|t|g|a|a|g|a|a|g|g|a|g|g|t|g|a|a|t|g|g|t|g|a|g|g|g|a|a|c|t|g|c|t|g|g|g|c|c|a|t|g|g|a|g|g|a|g|g|g|ei
c|c|t|g|c|t|g|g|a|a|c|t|c|a|c|a|c|t|g|t|t|t|c|c|a|c|a|g|c|g|c|a|t|g|a|g|a|g|c|c|c|a|g|c|c|c|g|g|c|a|c|c|c|c|t|g|t|g|ei
c|t|a|g|a|g|g|a|a|g|g|c|a|t|c|c|a|a|a|c|g|c|t|a|g|g|g|g|g|t|g|a|g|g|g|t|g|g|c|g|c|c|a|g|g|g|g|t|c|c|c|c|a|a|t|c|c|t|ei
g|g|c|c|g|c|a|a|a|t|a|c|c|a|a|g|t|g|g|a|c|c|t|t|c|a|a|g|g|t|g|a|g|t|g|g|a|g|g|g|g|c|t|t|c|t|a|g|g|g|a|a|g|g|a|a|c|a|ei
a|a|a|a|g|c|a|t|t|c|t|a|a|g|g|c|t|g|t|t|t|c|t|c|c|c|a|g|g|t|t|t|c|c|g|c|c|c|c|a|c|c|a|c|c|t|g|a|c|g|g|t|g|a|t|c|t|t|ei
c|g|g|c|t|g|t|c|t|a|c|a|c|t|t|g|c|t|c|t|a|t|t|c|t|g|c|t|g|c|g|c|c|a|g|c|c|c|c|a|g|g|c|c|t|g|g|a|a|g|g|a|c|c|g|c|t|t|ei
c|t|c|t|t|t|t|t|t|t|t|t|t|t|c|t|c|c|c|c|c|a|t|a|a|c|a|g|g|t|g|a|a|t|a|t|g|a|c|c|a|t|c|t|c|c|c|a|g|a|a|c|a|g|g|c|c|t|ei
a|t|g|t|a|c|t|g|c|a|g|a|g|a|t|a|a|g|t|t|t|a|g|t|a|c|c|t|g|t|a|a|g|t|t|t|t|g|c|t|t|a|t|a|t|a|a|a|t|g|t|a|c|t|t|t|a|a|ei
a|a|a|c|t|g|a|g|c|t|g|a|t|g|a|t|a|a|t|t|a|t|t|t|c|t|a|g|g|c|c|a|c|a|g|a|a|c|t|g|a|a|a|c|a|t|c|t|t|c|a|g|t|g|t|c|t|a|ie
a|a|g|g|g|g|a|t|c|c|t|c|c|a|t|g|g|t|g|g|g|a|g|a|t|g|g|g|c|t|t|g|a|a|g|t|t|g|t|g|t|g|t|c|c|t|a|a|g|c|t|g|t|g|g|a|g|a|ei
t|t|t|g|t|c|t|c|t|t|t|g|c|c|t|t|t|g|t|c|c|t|t|c|c|t|a|g|a|a|c|c|t|c|c|t|g|t|a|c|c|a|t|g|t|g|g|t|c|g|g|c|t|g|g|a|c|c|ei
g|t|a|g|t|t|t|c|a|g|a|a|g|a|a|g|t|a|t|t|g|g|t|g|a|g|a|c|t|g|t|g|c|c|t|c|t|g|a|a|g|c|a|g|t|c|a|t|a|g|a|t|g|c|c|a|a|t|ei
c|g|c|a|a|c|t|t|g|g|g|c|c|t|g|g|g|c|a|a|g|a|a|t|g|c|t|g|g|a|g|c|a|g|t|g|g|g|t|g|a|c|c|g|a|g|g|a|g|g|c|c|g|c|c|t|g|c|ei
c|a|a|a|t|t|a|c|c|t|g|t|g|c|c|t|t|t|t|c|c|a|t|c|g|c|a|g|a|t|t|c|t|c|a|c|a|g|c|c|a|c|a|g|t|g|g|a|c|a|a|t|g|c|c|a|a|t|ei
g|a|t|c|t|a|c|t|a|t|g|t|g|a|t|g|t|c|a|g|g|g|c|t|c|g|t|g|g|t|a|a|g|t|a|a|g|c|c|a|t|g|c|a|t|g|t|t|g|a|t|g|g|t|g|c|t|g|ei
t|c|c|c|c|t|c|a|c|a|g|g|g|a|a|a|t|t|t|t|c|t|t|c|a|c|a|g|g|t|g|g|a|a|a|a|g|g|a|g|g|g|a|g|c|t|a|c|t|c|t|c|a|g|g|c|t|g|ei
t|c|c|a|a|c|a|t|g|g|a|g|g|a|a|a|c|g|c|a|a|c|a|a|a|t|c|c|g|t|g|a|g|t|g|g|a|t|g|c|c|g|t|c|t|c|c|c|t|a|g|g|c|g|g|g|g|a|ei
c|a|g|a|a|a|g|a|c|a|a|g|t|c|t|g|g|t|a|t|t|t|c|t|t|c|a|g|g|a|c|t|c|c|c|t|t|g|a|g|t|c|a|t|t|a|a|a|a|a|a|a|a|t|c|t|t|c|ei
a|t|t|c|c|a|g|g|g|g|t|g|t|g|t|t|t|c|g|t|c|g|a|a|g|c|a|c|g|t|a|a|g|a|a|a|t|c|c|a|t|t|t|t|t|c|t|a|t|t|g|t|t|c|a|a|c|t|ei
g|c|t|c|c|t|a|a|t|g|c|t|t|c|c|t|g|c|t|g|c|c|c|t|c|c|a|g|g|c|a|g|g|t|g|a|t|g|c|t|t|t|t|c|c|g|g|a|a|g|a|g|t|c|c|c|c|a|ei
g|c|c|a|g|c|t|c|a|c|t|c|c|t|c|c|t|t|t|c|t|c|c|t|c|c|a|g|c|g|c|t|g|c|t|g|c|a|g|c|t|g|a|a|a|t|c|g|g|a|t|t|c|g|t|c|c|c|ei
t|c|a|g|g|c|a|t|c|c|g|c|g|t|c|t|c|c|g|a|c|a|a|t|g|c|c|g|g|t|g|a|g|t|g|g|g|c|g|c|c|c|c|g|c|g|g|t|g|g|g|g|a|g|g|g|c|g|ei
c|c|a|t|c|a|a|a|g|g|a|t|t|c|c|a|g|c|a|g|a|t|t|t|g|c|a|g|g|t|g|a|g|a|t|t|t|t|g|a|g|t|a|c|a|a|a|t|c|t|t|g|a|a|t|g|t|t|ei
c|a|c|t|g|a|g|t|t|g|a|t|t|t|t|a|g|c|a|g|a|g|a|a|g|t|g|g|t|g|a|c|c|t|g|a|c|a|a|g|a|g|a|g|a|a|t|g|t|g|a|a|c|c|a|g|t|g|ei
c|t|t|t|t|c|a|g|t|c|a|t|t|c|c|t|c|a|t|t|c|t|g|c|t|c|a|g|g|a|a|t|g|t|c|c|c|a|a|g|c|c|t|t|t|g|a|g|t|a|g|g|g|t|a|a|g|c|ei
t|g|g|c|c|c|t|g|a|c|t|c|a|a|g|c|c|t|c|t|t|g|c|t|c|c|a|g|t|t|c|c|g|g|a|a|c|t|g|c|a|t|g|c|t|c|a|c|c|a|c|c|a|t|c|t|g|c|ei
g|a|c|c|g|c|a|t|t|c|c|t|g|g|a|a|t|t|g|t|g|c|c|a|g|c|a|g|g|t|g|a|g|a|c|c|c|a|a|g|a|g|a|g|a|c|c|t|g|g|c|t|g|a|a|c|c|c|ei
c|c|c|t|g|a|t|g|a|a|g|g|c|a|c|c|t|t|g|g|g|g|c|t|c|c|t|g|c|c|g|c|a|t|c|c|t|c|t|c|c|c|c|t|c|a|g|g|a|a|g|g|g|g|a|c|t|g|ei
g|a|a|c|a|c|c|t|a|c|c|a|a|a|a|a|a|t|a|a|g|t|t|g|t|a|a|c|a|t|t|t|a|a|a|a|g|a|t|g|g|g|c|g|t|t|t|c|c|c|c|c|a|a|t|g|a|a|ei
c|c|g|c|c|t|g|c|t|g|g|a|a|g|a|t|g|g|c|g|a|g|g|c|t|t|a|a|g|t|g|a|g|t|g|g|g|g|c|t|c|t|c|c|t|a|c|c|c|a|c|a|c|g|t|g|c|t|ei
g|g|a|a|g|a|t|g|c|t|g|g|a|g|g|a|g|a|a|a|c|c|c|g|g|a|a|g|g|t|a|g|g|c|t|c|t|g|g|t|g|a|c|c|a|g|g|a|c|a|a|g|g|a|a|g|g|g|ei
c|t|t|g|c|a|c|a|t|a|c|c|t|a|t|g|c|t|t|c|a|a|g|a|t|c|c|c|a|a|c|a|t|g|a|a|g|a|a|a|g|g|a|g|a|c|g|a|g|t|g|t|a|a|a|a|a|c|ei
a|a|g|c|a|t|t|c|t|c|a|g|a|a|a|c|t|t|a|t|t|t|g|g|t|g|t|g|t|g|t|a|c|t|c|a|a|c|t|a|a|g|a|g|a|a|t|t|g|a|a|c|c|a|c|c|g|t|ei
c|t|c|t|g|a|t|c|t|c|a|a|g|g|a|a|g|a|a|a|g|a|a|a|a|g|c|t|g|c|a|g|g|t|g|a|g|a|a|g|t|g|t|g|c|g|c|c|t|c|a|a|a|t|c|a|c|c|ei
t|c|t|g|g|g|c|t|c|c|c|a|g|a|a|c|c|c|a|c|a|a|c|t|a|a|a|g|g|t|g|a|g|g|g|n|c|t|t|c|c|t|g|c|c|a|c|a|c|t|t|g|g|g|g|t|g|g|ei
g|a|c|c|t|c|a|c|c|t|g|a|c|c|c|t|c|t|c|t|c|c|t|t|g|c|a|g|c|a|c|a|g|a|g|t|t|g|a|t|g|a|g|a|c|g|c|g|t|c|c|g|t|c|g|c|t|t|ei
t|t|a|g|t|g|g|c|a|a|c|c|t|g|g|t|g|a|c|c|c|c|c|t|c|c|t|g|t|g|a|t|t|t|t|a|g|g|c|c|a|t|g|a|g|g|c|a|g|c|c|g|g|c|a|t|c|g|ei
t|t|c|t|c|c|t|t|c|t|a|c|c|a|c|t|c|a|g|c|t|g|t|t|g|a|a|t|g|g|g|g|g|t|a|a|c|c|c|t|a|c|a|g|g|t|a|a|a|g|g|g|c|g|a|g|t|g|ei
g|g|c|t|c|a|t|c|a|g|c|a|t|g|g|c|c|t|a|c|g|g|a|a|a|t|c|g|g|t|g|c|g|c|c|a|a|g|c|c|c|c|g|g|g|c|c|t|c|g|g|g|a|g|g|g|a|a|ei
a|a|g|a|g|g|g|c|a|g|g|g|a|a|g|g|t|g|g|t|g|t|c|g|g|g|a|g|g|a|g|c|a|g|c|t|g|g|c|c|c|t|g|g|a|g|g|c|c|a|a|g|g|c|g|g|a|g|ei
t|a|t|t|t|a|c|t|g|g|a|a|a|g|t|g|t|c|a|a|t|a|a|c|g|t|t|t|g|g|t|g|a|g|a|a|g|t|c|t|g|c|g|a|g|c|t|t|c|c|g|g|g|a|a|g|t|a|ei
t|c|a|t|t|t|t|t|g|g|g|c|c|c|c|t|t|t|c|t|c|t|g|c|t|t|a|g|g|t|g|t|c|a|g|a|c|c|t|g|a|c|c|c|a|g|g|c|a|g|c|c|a|a|c|a|a|g|ei
a|g|a|g|a|c|c|c|t|t|t|g|a|a|g|t|c|a|a|g|g|a|c|c|g|a|g|g|a|a|g|a|g|g|a|c|t|t|c|c|a|c|g|t|g|g|a|c|c|a|g|g|t|g|a|c|c|a|ei
a|c|a|g|t|g|c|a|t|g|c|c|a|t|c|c|t|g|a|a|c|t|a|g|g|t|c|c|t|c|t|g|g|g|g|c|t|g|g|g|g|a|c|a|g|a|g|c|t|t|g|g|g|c|c|a|g|g|ei
g|a|a|t|t|t|g|t|t|c|a|t|g|a|c|t|a|t|t|t|t|c|t|c|g|t|a|g|c|c|t|g|a|g|a|c|a|g|c|t|g|c|c|t|t|g|t|g|t|g|c|g|a|c|t|g|a|g|ei
g|c|t|g|g|a|a|a|c|c|a|a|a|g|c|a|a|t|c|a|t|c|t|t|t|a|g|t|g|g|a|a|a|c|t|a|t|t|c|t|t|a|a|a|g|a|a|g|a|t|c|t|t|g|a|t|g|g|ei
t|c|a|c|a|c|t|c|t|t|t|c|t|c|c|a|c|g|t|g|c|c|c|t|c|c|a|g|t|t|c|c|c|t|g|a|c|a|t|c|a|t|g|g|a|g|t|t|c|t|g|c|g|a|g|g|c|c|ei
t|c|c|c|a|c|a|c|g|g|t|t|c|a|g|a|t|a|a|t|c|c|c|g|t|g|c|a|t|t|t|t|a|c|c|c|t|c|a|t|c|a|t|g|c|a|c|c|a|c|t|t|t|a|g|c|c|a|ei
t|a|c|a|c|c|t|g|c|c|a|t|g|t|g|c|a|g|c|a|t|g|a|g|t|c|t|g|c|c|c|a|a|g|c|c|c|c|t|c|a|c|c|c|t|g|a|g|a|t|g|g|g|a|g|c|c|g|ei
t|g|a|t|t|c|t|c|a|t|g|a|a|a|t|a|c|c|c|t|g|a|g|t|g|a|a|g|g|t|a|g|g|c|a|a|g|t|g|a|c|t|g|a|a|g|g|g|a|c|a|c|c|g|t|g|c|g|ei
g|t|g|a|g|g|c|a|t|c|c|a|t|g|c|c|c|t|g|c|t|c|t|t|t|c|a|g|a|t|a|c|c|a|g|g|g|c|c|a|c|g|t|g|c|t|a|c|g|a|g|g|a|c|c|a|g|g|ei
c|t|c|a|t|c|t|g|t|c|t|c|t|g|c|c|c|a|c|c|c|t|c|c|c|c|a|g|a|c|c|t|a|t|g|a|g|c|a|g|c|g|g|a|a|g|g|t|g|g|t|g|g|a|g|t|t|c|ei
t|t|c|c|t|c|c|g|a|g|g|c|c|a|g|t|a|c|c|t|t|t|c|a|t|t|a|t|t|c|t|t|t|g|a|t|c|t|t|c|a|g|g|g|a|a|c|t|g|c|a|t|a|g|a|t|t|g|ei
g|g|a|t|t|t|c|c|a|g|c|c|t|c|c|c|c|t|c|t|g|c|a|a|a|t|g|t|g|a|a|c|g|a|g|t|g|t|g|c|a|g|a|c|g|g|t|g|c|c|c|a|c|c|c|c|c|c|ei
c|t|c|c|a|c|a|t|g|a|g|c|c|a|g|a|a|a|c|a|c|a|c|g|g|a|t|g|g|t|g|a|g|a|g|g|t|g|t|g|g|g|a|t|g|c|a|c|a|g|c|a|g|t|g|g|g|c|ei
a|a|t|t|g|a|a|g|c|t|t|t|t|t|c|a|g|a|g|c|a|g|a|c|a|a|g|a|c|c|t|c|c|c|t|g|c|a|g|c|t|t|t|c|t|t|g|g|c|a|c|c|a|g|a|a|t|a|ei
g|a|a|t|g|a|t|g|a|t|g|c|a|g|t|c|c|g|g|c|c|g|g|a|g|g|g|g|g|t|a|a|g|c|t|t|g|t|g|c|t|c|t|a|c|t|c|a|t|c|t|a|a|a|c|t|t|g|ei
g|g|t|g|a|c|a|a|c|a|t|g|c|t|g|g|a|g|c|c|a|a|g|g|t|a|a|c|g|t|a|a|g|t|g|g|c|t|t|t|c|a|a|g|a|c|c|a|t|t|g|t|t|a|a|a|a|a|ei
a|t|g|t|a|a|t|t|c|g|g|a|a|c|g|a|t|t|c|t|t|c|c|t|g|c|a|g|a|t|c|a|c|c|t|t|c|t|a|t|g|a|g|g|a|c|a|g|g|g|c|c|t|t|c|c|a|g|ei
c|t|g|g|c|c|t|a|c|c|t|g|a|a|g|a|a|g|a|a|c|c|a|g|g|g|a|g|g|t|g|a|g|a|a|c|t|a|t|a|t|g|g|a|a|a|a|g|t|c|a|g|c|t|t|a|a|a|ei
g|g|a|a|a|a|c|a|a|a|g|c|a|a|t|c|t|g|g|a|c|g|g|t|a|a|g|a|c|t|g|a|g|c|a|a|c|t|c|c|c|t|g|a|a|t|t|t|t|t|a|t|a|c|a|t|c|t|ei
g|g|a|c|g|a|c|g|t|c|c|t|g|c|g|g|g|g|c|g|a|g|c|g|a|g|a|g|g|c|t|g|c|g|g|g|a|g|g|a|g|c|t|g|g|g|c|c|g|g|c|t|c|g|c|g|g|a|ei
t|t|t|c|c|t|g|t|t|g|t|c|t|c|c|t|c|t|c|c|t|t|c|c|c|t|a|g|g|t|g|a|t|c|a|t|g|g|t|a|a|c|c|g|g|g|g|a|t|c|a|c|c|c|t|a|t|c|ei
g|g|c|a|t|c|t|c|a|c|a|g|g|a|c|a|t|t|t|t|c|t|t|c|a|c|a|g|a|t|a|g|a|a|a|a|g|g|a|g|g|g|a|g|c|t|a|c|t|c|t|c|a|g|g|c|t|g|ei
c|c|c|a|a|g|c|c|t|c|a|c|a|c|a|t|t|t|c|t|g|t|t|c|t|c|a|g|g|g|a|t|g|g|g|g|g|t|g|t|c|t|a|c|g|g|t|g|a|c|a|g|c|t|g|c|c|a|ei
g|a|g|c|c|t|a|g|a|c|a|c|c|c|c|t|g|g|g|t|t|g|t|g|g|g|a|g|a|g|g|c|t|g|g|g|g|t|g|g|a|g|g|g|a|g|a|g|g|c|t|c|c|t|t|c|c|c|ei
c|c|c|c|t|a|g|a|t|g|a|a|g|t|c|t|c|c|a|t|g|a|g|t|c|a|a|g|g|g|c|c|t|g|g|t|g|t|a|t|c|c|a|g|g|t|g|a|t|c|t|a|g|t|a|a|t|t|ei
c|c|t|c|a|g|t|a|c|c|a|a|a|c|t|c|a|t|a|c|a|t|c|a|c|t|g|t|g|t|a|c|t|a|g|g|c|t|t|a|t|a|t|a|t|a|t|a|g|a|t|g|t|c|c|t|a|a|ei
t|t|c|a|c|c|c|c|a|c|a|g|g|t|g|c|a|g|g|c|t|g|c|t|t|c|a|g|a|a|g|g|t|g|g|t|g|g|c|t|g|g|t|g|t|g|g|c|t|a|a|t|g|c|c|c|t|g|ei
t|t|g|a|t|t|t|c|a|g|t|g|c|t|g|g|a|t|t|a|t|t|c|t|g|c|a|g|a|a|a|a|t|t|t|g|a|g|a|a|g|c|a|a|t|g|g|g|c|a|t|c|c|t|g|a|a|g|ei
a|t|g|g|a|g|g|c|c|c|c|a|g|c|c|c|c|t|c|t|c|t|t|c|t|g|a|c|t|c|t|c|c|g|g|c|t|c|t|c|c|c|t|c|c|c|t|c|a|g|g|c|t|g|g|c|c|g|ei
g|g|g|t|a|c|c|c|a|g|c|a|t|c|t|a|t|t|t|t|t|a|a|a|a|a|t|t|a|a|t|t|c|a|a|a|c|t|t|c|a|a|a|a|a|g|a|a|t|g|a|a|g|t|t|c|c|a|ei
a|t|g|g|a|t|t|g|t|a|a|c|t|g|c|t|g|c|c|c|a|c|t|t|t|t|g|a|a|a|c|t|g|g|t|g|t|t|a|a|a|a|t|t|a|c|a|g|t|t|g|t|c|g|c|a|g|g|ei
g|c|c|t|g|c|g|g|g|g|c|a|t|t|g|t|c|a|a|g|c|a|c|t|g|a|a|g|g|t|a|g|g|c|c|a|c|c|t|t|c|a|g|g|a|g|c|c|t|g|g|g|c|a|g|g|g|t|ei
c|a|c|c|a|g|c|a|c|g|a|g|c|g|t|a|t|g|g|g|c|t|a|c|g|c|t|g|c|a|t|g|g|a|g|c|a|g|a|g|g|t|g|a|a|c|g|g|t|g|g|g|c|t|c|c|c|a|ei
g|g|t|g|a|c|a|g|t|g|g|g|g|g|a|c|c|c|t|t|t|g|t|a|g|a|a|g|g|t|a|a|g|c|t|t|c|t|c|t|a|a|a|g|c|c|c|a|g|g|g|c|c|t|g|g|t|g|ei
a|c|a|a|g|t|a|a|t|g|t|c|g|a|t|a|a|a|g|a|g|g|a|g|a|g|c|t|g|t|a|a|g|t|a|g|t|t|t|t|t|a|a|g|t|a|a|a|a|a|g|a|a|a|a|t|a|g|ei
t|a|a|c|t|t|t|c|a|g|g|c|t|g|t|a|c|a|a|a|a|t|g|c|g|t|t|g|g|a|t|t|t|a|t|g|c|t|t|g|c|t|c|a|t|c|c|t|t|a|t|g|g|a|t|t|t|a|ei
g|c|c|a|a|g|c|t|t|g|c|c|t|t|g|a|t|c|c|a|a|g|a|a|a|a|c|a|a|a|a|a|a|t|c|g|c|t|a|c|t|t|c|c|c|t|g|c|c|t|t|t|g|a|a|a|a|a|ei
t|t|c|c|t|t|a|c|a|g|c|c|t|g|c|a|c|t|c|t|g|a|t|t|g|g|c|a|c|a|g|g|c|t|g|t|a|t|a|t|c|a|t|g|c|a|g|a|c|c|a|t|t|t|t|c|t|t|ei
c|c|t|g|c|c|g|a|c|a|a|g|a|c|c|a|a|c|g|t|c|a|a|a|c|g|c|c|t|g|g|g|g|g|a|a|g|g|t|c|g|g|c|g|c|g|c|a|c|g|c|c|g|g|c|g|a|c|ei
g|c|t|c|t|t|t|a|t|g|c|a|c|a|g|g|c|c|a|g|a|g|c|a|a|g|g|c|a|a|g|a|c|g|g|c|t|g|g|c|t|t|g|g|t|g|a|g|g|a|g|c|a|g|c|g|c|t|ei
a|g|t|g|g|c|a|c|c|a|g|c|c|g|g|a|t|c|a|g|t|t|c|t|c|c|t|g|g|t|g|a|g|t|c|t|g|t|c|c|t|g|t|c|c|t|g|c|g|c|c|c|t|g|g|g|c|c|ei
a|g|t|c|a|c|t|g|a|g|t|t|c|a|t|t|t|a|a|t|t|a|c|c|a|c|a|g|g|t|g|a|g|a|g|c|a|a|a|g|a|g|c|a|g|g|t|g|g|c|c|a|a|c|t|c|a|g|ei
t|c|t|t|c|a|t|t|a|t|g|a|t|c|t|c|c|a|t|a|t|t|g|a|a|a|a|t|g|a|a|c|t|g|a|a|c|a|g|a|g|a|t|a|a|a|a|a|t|t|c|c|c|c|a|t|c|a|ei
c|t|g|c|t|c|t|t|c|a|t|g|a|a|g|a|a|g|a|a|c|c|a|g|a|g|a|g|g|c|a|a|g|c|a|g|g|g|g|c|c|a|c|t|g|g|c|c|a|g|g|c|c|a|g|g|g|a|ei
t|g|g|t|c|t|g|g|a|c|c|c|g|g|g|t|c|c|c|g|t|g|t|c|g|c|a|g|g|c|c|g|c|t|g|c|c|c|a|g|c|a|g|c|a|g|g|a|g|t|c|a|g|c|c|a|c|c|ei
t|c|c|a|g|c|c|g|g|g|c|t|g|a|g|c|c|c|t|g|g|t|c|c|g|c|a|g|a|g|c|c|t|c|t|g|c|c|c|c|t|c|c|c|g|a|g|a|c|a|c|c|c|g|c|t|a|c|ei
t|g|a|g|a|a|g|g|a|g|a|g|a|c|a|a|a|t|c|a|a|g|a|a|a|a|a|c|g|t|g|a|g|g|a|g|t|a|t|t|t|c|a|t|t|a|c|t|g|c|a|t|g|t|g|t|t|t|ei
t|g|g|c|t|t|c|a|g|a|t|c|c|a|t|c|c|c|a|g|a|g|c|t|a|a|a|g|g|t|a|t|a|g|a|t|a|g|g|c|a|g|g|g|a|c|a|g|g|g|a|g|g|g|a|g|a|g|ei
g|g|a|c|a|g|g|a|t|g|t|a|g|c|t|c|t|c|a|g|g|t|g|g|t|c|c|a|a|t|t|t|c|g|g|g|t|c|a|t|g|t|a|t|c|c|c|t|t|t|a|t|t|g|g|t|a|c|ei
g|a|a|g|t|c|c|a|t|a|a|a|g|c|c|c|a|c|a|a|g|t|c|t|t|t|c|a|t|g|a|t|g|g|a|c|a|g|a|a|a|a|a|t|g|t|g|t|g|t|g|c|t|t|t|c|t|c|ei
t|t|c|a|t|g|g|c|a|g|g|c|t|c|t|a|a|g|a|g|g|a|g|g|c|t|c|c|t|c|c|a|g|g|g|a|g|g|a|a|a|g|g|a|c|t|t|t|g|g|c|t|t|t|c|t|a|g|ei
a|a|t|t|c|a|g|g|c|c|t|g|t|c|c|t|t|a|g|a|a|t|g|t|c|a|g|g|g|t|a|c|a|g|c|c|c|a|t|t|t|g|a|g|c|t|c|c|t|g|t|a|t|a|g|a|t|a|ei
c|t|c|g|g|g|c|t|c|a|t|t|c|t|c|t|t|c|c|t|t|t|c|c|a|c|a|g|t|t|g|c|t|g|c|t|g|a|c|a|c|g|c|c|g|a|c|c|g|c|c|t|g|c|t|g|c|t|ei
t|g|c|a|g|t|t|g|a|a|g|c|c|c|a|t|g|a|g|g|c|c|c|a|a|a|t|g|t|t|c|a|t|g|t|t|c|c|c|a|g|g|a|a|g|g|t|c|a|c|a|a|c|c|t|a|g|t|ei
g|g|a|g|a|c|a|a|a|g|t|c|a|g|t|c|t|c|a|c|t|c|c|t|g|c|c|c|a|g|g|g|t|g|g|a|g|t|g|c|a|g|t|g|g|c|g|c|g|a|t|c|t|c|g|g|c|t|ei
a|a|g|a|g|t|g|c|a|a|a|t|g|c|a|c|c|t|c|c|t|g|c|a|a|a|g|a|g|t|g|a|g|t|g|c|g|g|g|g|c|c|a|t|c|t|c|c|a|g|g|a|a|t|c|t|g|g|ei
g|c|c|c|g|c|c|t|g|a|g|t|c|c|a|t|c|c|t|t|t|t|c|g|g|c|a|g|g|t|c|g|c|a|a|t|g|g|a|a|g|a|a|g|a|g|a|t|c|g|c|c|g|c|g|c|t|g|ei
a|c|t|t|a|g|c|a|t|t|t|c|a|t|a|a|c|a|g|g|c|g|c|g|t|t|c|a|c|t|g|a|g|a|a|g|a|t|a|t|t|t|a|a|a|c|t|c|t|g|a|a|a|c|g|a|g|g|ei
c|g|t|c|g|g|c|t|t|t|c|c|c|c|t|t|c|t|g|t|t|t|t|t|c|t|a|g|g|a|c|t|t|c|t|g|c|a|c|g|g|a|c|c|t|g|g|c|c|g|t|c|t|c|c|a|g|t|ei
a|t|c|g|t|t|g|c|t|g|g|c|a|t|g|g|t|t|c|t|a|c|t|g|a|g|c|t|g|t|g|g|t|c|a|c|t|g|g|a|g|c|t|g|t|g|g|t|c|a|g|c|t|g|c|t|g|t|ei
a|c|c|a|c|t|c|g|g|t|c|c|t|a|g|c|c|t|c|c|a|g|a|a|c|c|c|a|c|a|a|t|a|c|t|c|c|t|c|t|g|a|g|c|c|t|g|a|g|g|c|c|a|g|g|c|a|g|ei
c|c|g|c|a|a|c|t|c|a|g|t|c|t|t|c|c|a|g|c|a|g|g|c|t|g|a|a|g|t|g|a|g|t|g|c|c|c|a|c|c|c|c|c|a|t|g|g|c|a|c|c|t|a|c|c|c|a|ei
t|c|c|t|g|c|t|g|g|a|a|g|c|a|c|t|c|a|g|g|a|a|g|c|c|a|a|g|g|t|g|c|g|t|a|t|c|t|g|c|t|g|c|c|t|a|g|c|a|g|g|g|c|c|c|a|g|t|ei
g|a|c|a|t|a|t|t|g|a|t|g|t|g|g|c|a|a|a|g|c|c|c|a|t|a|t|t|g|t|t|c|a|c|t|t|c|c|c|t|g|a|g|g|a|a|a|a|c|t|c|a|g|t|g|c|t|a|ei
g|g|t|c|a|g|c|a|c|g|t|c|c|c|c|c|c|t|t|c|c|c|t|c|g|c|a|g|g|g|a|g|c|g|g|a|c|a|t|g|g|a|c|t|a|c|g|a|c|t|c|g|t|a|c|c|a|g|ei
c|t|c|c|c|t|t|c|t|c|t|g|a|g|c|c|t|t|c|c|t|t|g|c|g|c|a|g|a|t|g|t|t|g|a|t|g|a|t|g|a|t|g|g|c|t|c|t|g|c|t|g|g|t|g|c|c|c|ei
a|a|c|t|a|g|a|t|t|g|g|c|c|a|t|a|t|g|t|t|t|a|t|a|t|t|t|t|t|t|a|g|a|t|t|g|g|g|t|a|a|t|g|a|a|t|a|c|a|t|g|g|a|g|t|t|t|c|ei
a|g|c|a|a|c|t|g|a|a|a|c|c|t|g|c|t|t|t|c|t|t|c|a|t|t|a|g|c|a|t|a|c|c|c|t|t|t|t|t|g|g|a|g|a|c|a|a|a|t|t|a|t|g|c|a|c|a|ei
c|c|t|g|t|c|t|c|c|t|t|g|c|c|t|g|c|c|c|c|a|c|c|t|t|c|a|g|g|a|c|t|a|c|t|c|c|g|c|a|g|c|t|c|c|c|c|g|g|g|g|c|c|g|a|t|t|t|ei
a|a|t|g|g|a|c|a|a|g|c|c|t|c|a|t|c|c|c|a|a|a|c|c|a|t|c|a|c|c|t|t|t|c|a|t|a|t|t|a|a|c|a|c|a|a|a|a|c|t|g|g|g|a|g|t|g|a|ei
t|g|g|c|a|g|c|c|g|c|g|g|g|a|c|t|g|t|c|g|c|g|t|g|c|g|c|c|c|g|a|c|g|c|g|g|a|g|t|c|a|g|c|a|g|g|g|g|c|g|a|a|a|a|g|c|g|g|ei
c|t|a|g|g|a|g|g|g|c|t|c|g|c|c|g|g|g|t|g|c|g|g|g|g|g|a|a|g|t|g|a|c|c|g|t|g|c|g|t|g|t|a|a|a|g|g|g|t|g|a|g|g|c|g|t|a|c|ei
a|c|t|t|g|g|g|c|t|t|a|t|t|c|t|c|t|c|c|t|t|t|c|c|g|c|a|g|t|t|g|c|t|g|c|t|g|a|c|a|c|g|c|c|g|a|c|c|g|c|c|t|g|c|t|g|c|t|ei
g|g|g|g|g|a|c|c|c|g|g|c|g|c|g|g|c|c|g|c|g|c|g|t|c|c|g|g|g|c|g|g|g|a|g|g|c|t|g|g|g|g|g|g|c|c|g|g|g|g|c|g|g|g|g|c|c|g|ei
t|a|c|c|g|a|t|g|c|t|a|a|a|g|g|a|t|c|c|a|t|g|t|a|a|a|t|a|a|t|g|g|c|a|t|t|a|t|t|t|g|g|a|a|a|t|c|c|c|a|g|t|g|g|t|a|t|t|ei
c|a|g|a|g|g|g|g|c|c|t|c|c|c|g|g|a|c|c|t|c|c|g|g|c|t|c|c|a|a|g|g|t|g|t|t|c|c|t|g|g|a|c|c|a|a|a|g|g|g|g|g|a|a|g|c|a|g|ei
c|a|t|c|t|g|a|g|g|t|g|g|t|t|a|a|a|a|g|c|t|c|t|c|t|c|g|t|g|t|c|a|c|c|c|c|c|t|t|t|t|a|t|g|c|a|g|t|c|a|a|a|t|g|t|a|a|t|ei
c|c|c|a|g|g|t|t|a|c|c|c|g|c|g|g|a|a|a|t|t|t|a|g|t|g|t|c|c|g|g|t|c|a|c|c|g|t|g|a|c|a|a|t|g|c|a|g|c|t|g|a|g|g|a|a|c|c|ei
g|c|c|a|g|c|a|g|g|g|t|c|c|t|g|g|a|a|c|a|g|c|t|c|g|a|g|g|g|t|g|a|g|a|a|g|g|g|t|a|a|c|c|c|t|g|g|g|c|a|t|c|c|t|c|t|t|c|ei
g|g|c|a|c|c|a|c|c|a|c|t|g|a|c|c|t|g|g|g|a|c|a|t|a|a|t|c|g|t|a|a|g|t|a|t|g|c|c|t|t|t|c|a|c|t|g|c|g|a|g|g|g|g|t|t|c|t|ei
t|a|t|t|t|t|a|t|t|t|a|a|t|t|g|t|t|c|t|a|t|t|t|a|c|a|t|t|a|g|t|t|a|t|t|g|t|t|t|g|t|t|a|a|t|c|t|c|t|t|g|c|t|g|t|a|c|c|ei
c|a|c|a|a|a|a|a|t|t|c|t|t|c|t|t|t|c|t|c|t|t|t|g|g|c|a|g|a|g|t|g|t|a|g|a|t|c|c|c|a|a|a|a|a|t|t|a|c|c|c|a|a|a|g|a|a|g|ei
g|g|c|g|c|g|c|t|g|c|g|g|a|g|c|g|g|a|g|c|c|g|c|g|t|c|g|a|c|g|g|c|g|g|t|g|c|g|c|t|g|g|c|g|g|c|g|a|g|t|g|t|a|t|g|c|a|g|ei
g|c|a|a|a|c|c|t|c|t|c|c|c|t|g|g|c|c|c|c|t|t|g|a|t|c|a|g|g|c|a|c|a|g|g|g|c|g|g|g|g|t|g|t|t|g|g|t|g|g|g|g|a|a|a|t|g|t|ei
a|g|c|g|a|t|t|g|t|t|a|c|c|c|t|t|g|g|g|c|c|t|g|c|c|t|g|g|c|c|a|g|g|g|g|t|t|t|t|t|t|c|g|g|g|g|g|c|c|a|g|a|a|g|t|c|c|a|ei
t|t|g|t|g|t|a|t|g|g|t|g|t|g|a|g|g|t|a|g|g|g|c|t|a|g|g|t|t|t|a|t|g|t|t|t|t|g|t|t|t|a|t|g|g|g|t|g|t|a|c|a|g|t|t|g|t|t|ei
t|c|t|c|c|a|t|c|g|c|c|t|t|g|t|c|t|g|t|g|g|g|g|g|a|c|t|g|g|t|g|a|g|a|t|t|g|g|g|g|g|g|a|t|a|a|a|g|g|a|a|g|g|g|g|g|g|c|ei
g|a|t|c|c|t|g|g|a|t|a|t|t|a|a|a|g|g|a|a|t|t|g|c|a|c|t|g|g|t|g|a|a|t|c|c|t|t|a|t|t|c|t|a|t|t|t|t|c|t|a|t|t|t|c|c|c|c|ei
g|a|a|t|t|t|t|t|g|c|c|a|a|g|c|a|g|g|a|a|a|a|g|a|t|c|a|g|g|t|g|a|g|c|a|g|a|a|a|c|a|c|c|t|t|t|g|c|t|t|t|t|c|a|a|t|c|a|ei
t|c|a|t|c|c|t|c|c|t|c|c|c|t|g|a|g|t|c|c|t|c|t|t|c|a|g|g|g|g|c|c|a|c|a|c|c|a|g|g|a|g|c|c|t|a|g|c|t|c|c|t|t|g|t|c|c|t|ei
g|t|a|t|c|c|c|c|a|c|t|g|c|c|t|t|g|t|a|t|g|t|g|t|a|a|a|c|c|a|a|a|g|g|g|t|t|a|c|t|t|t|t|a|c|a|c|t|t|a|a|t|c|t|a|t|a|g|ei
g|t|t|c|g|t|g|g|g|g|g|c|c|a|c|t|t|t|g|c|g|g|c|t|t|g|a|g|g|a|g|c|c|g|g|a|g|c|t|g|c|t|c|g|c|c|c|a|g|g|a|c|a|t|c|c|g|c|ei
c|t|c|c|c|t|t|c|t|t|g|c|c|c|t|c|c|g|g|t|t|t|c|c|c|c|a|g|g|c|t|c|c|c|g|g|a|c|g|t|c|c|c|t|g|c|t|c|c|t|g|g|c|t|t|t|t|g|ei
c|a|a|a|c|c|c|c|g|c|c|c|t|t|g|c|t|c|c|g|g|a|c|c|c|c|c|a|t|c|c|a|c|c|a|g|g|a|g|g|g|t|t|t|t|c|t|g|g|c|g|g|c|t|c|c|t|g|ei
t|c|t|c|g|g|g|g|g|c|g|g|c|c|g|g|c|g|c|g|g|c|g|g|a|g|c|g|g|t|c|c|c|c|g|g|c|c|g|c|g|g|c|c|c|c|g|a|c|g|t|g|t|g|t|g|t|c|ei
g|t|g|g|t|t|c|a|a|a|g|t|t|t|t|t|t|t|c|t|t|c|c|t|t|c|a|g|g|t|g|t|c|g|t|g|a|a|a|a|c|t|a|c|c|c|c|t|a|a|a|a|g|c|c|a|a|a|ei
c|t|g|t|a|c|c|a|a|c|a|a|c|g|a|g|g|a|g|c|a|c|g|g|g|c|c|t|c|t|g|g|a|a|g|t|c|a|t|g|a|g|a|g|t|a|g|a|a|a|a|a|c|c|a|g|t|c|ei
g|a|a|t|g|c|c|g|c|c|c|t|g|g|t|t|a|t|t|c|c|g|g|a|a|c|c|g|t|t|t|t|c|t|a|t|c|a|t|c|t|g|c|c|t|a|a|a|a|a|a|c|t|c|a|g|t|c|ei
c|t|c|g|a|g|t|t|t|g|a|c|t|c|g|c|t|a|c|a|g|c|c|t|c|t|t|c|t|a|c|c|c|g|g|a|c|g|a|a|g|a|t|g|a|c|t|t|c|t|a|c|t|t|c|g|g|c|ei
a|t|a|c|c|t|g|c|c|c|g|c|t|g|t|a|g|a|t|g|a|g|a|a|t|c|a|g|g|t|a|g|c|a|c|c|t|g|c|c|c|c|t|g|g|a|g|a|a|a|t|g|g|g|g|t|c|t|ei
t|g|c|t|c|c|c|c|c|a|a|c|t|t|g|g|g|g|c|c|c|t|g|a|c|c|a|g|c|a|g|g|t|g|g|a|t|c|a|g|a|g|c|t|g|g|c|g|c|a|a|a|g|a|g|c|g|g|ei
t|t|g|a|a|g|t|t|g|c|c|t|a|g|a|c|c|a|g|a|g|g|a|a|a|a|g|t|a|t|c|a|t|g|t|c|t|c|c|t|t|t|a|a|c|t|a|g|c|a|t|a|c|c|c|c|g|a|ei
g|t|g|g|t|a|a|c|t|a|t|t|g|t|a|c|t|g|a|c|a|a|g|a|c|c|t|g|c|t|g|c|t|a|t|a|a|a|t|t|g|g|a|t|a|g|a|g|g|g|a|a|g|a|g|g|a|a|ei
t|c|c|c|t|c|t|g|t|t|g|c|c|c|t|c|t|g|g|t|t|t|c|c|c|c|a|g|g|c|t|c|c|c|g|g|a|c|g|t|c|c|c|t|g|c|t|c|c|t|g|g|c|t|t|t|t|g|ie
a|c|a|g|t|g|a|c|t|a|t|t|t|c|a|a|g|c|c|a|t|t|t|c|a|c|a|g|g|t|g|a|g|a|a|a|g|a|t|c|a|g|a|g|g|c|a|g|t|a|c|c|t|t|c|c|c|t|ei
c|t|g|t|t|g|t|g|a|t|g|t|g|t|a|g|g|a|g|g|a|a|g|g|t|c|a|g|g|t|a|g|g|g|a|a|g|g|g|g|t|g|a|g|g|a|g|t|g|g|g|g|t|c|t|g|g|g|ei
a|c|c|a|a|a|c|t|g|t|t|c|a|g|a|g|c|a|c|g|a|t|t|a|g|a|c|a|t|a|a|a|a|g|t|g|a|a|a|c|a|c|a|c|a|g|c|a|a|a|g|g|c|a|g|a|a|a|ei
t|t|c|c|t|a|a|g|a|c|c|c|c|t|t|t|c|a|c|t|a|t|t|a|a|g|a|a|t|t|a|a|a|a|a|t|t|a|t|a|g|c|t|g|t|t|c|c|t|c|c|t|t|c|a|g|g|a|ei
a|g|a|c|t|g|g|a|a|g|t|t|c|a|t|a|c|c|t|a|a|g|t|c|g|t|a|a|t|a|a|t|a|c|c|t|c|a|a|t|g|t|t|t|g|a|g|g|a|g|c|a|t|g|t|t|t|t|ei
c|t|g|c|a|g|a|c|c|a|g|g|t|g|g|a|c|c|t|g|a|c|t|c|g|c|t|c|t|g|a|c|c|a|a|g|a|a|a|a|t|c|a|c|t|c|t|t|a|a|g|a|c|c|c|c|a|c|ei
c|c|a|c|t|c|a|g|c|c|a|g|g|c|c|c|t|t|c|t|t|c|t|c|c|c|a|g|g|t|c|c|c|c|c|a|c|g|g|c|c|c|t|t|c|a|g|g|a|t|g|a|a|a|g|c|t|g|ie
t|c|g|a|t|g|g|c|g|c|c|t|a|g|g|a|g|t|c|c|a|t|g|a|t|a|c|g|g|t|a|c|a|g|g|c|t|t|c|c|g|g|c|g|a|c|g|g|a|t|g|c|c|c|c|g|c|c|ei
t|t|a|c|c|t|c|t|a|a|t|c|a|a|c|a|g|t|t|c|a|a|t|a|g|c|t|t|g|a|a|t|t|t|g|t|c|c|c|t|g|t|c|t|a|t|t|a|a|t|c|a|c|t|t|c|t|c|ei
t|g|a|g|g|g|c|t|t|a|c|c|t|t|c|t|c|c|c|a|c|t|t|t|a|t|g|c|t|a|c|t|c|t|a|c|t|a|c|t|c|a|g|t|g|a|c|a|t|t|t|t|a|a|a|g|c|t|ei
c|c|t|g|a|t|c|t|g|g|g|t|c|t|c|c|c|c|t|c|c|c|a|c|t|c|a|g|g|g|a|g|c|c|a|g|g|c|t|c|g|g|c|a|t|t|t|c|t|g|g|c|a|g|c|a|a|g|ie
c|a|t|g|g|c|a|c|t|g|a|c|t|a|g|g|c|c|c|t|c|t|g|t|c|c|a|g|c|t|c|c|a|a|g|c|c|c|a|g|c|c|c|t|c|a|g|c|c|a|t|g|g|c|a|t|g|c|ei
g|t|t|t|t|t|g|a|t|c|a|c|g|c|t|t|c|t|a|t|g|g|a|t|c|a|a|g|a|a|t|t|a|c|c|a|t|a|a|g|g|c|a|a|t|g|t|t|t|c|t|g|a|a|g|a|t|t|ei
g|a|a|a|c|c|g|c|t|g|a|g|g|c|t|t|a|t|t|t|g|g|g|a|g|a|a|g|g|t|a|a|a|t|a|t|t|t|c|t|a|g|a|a|c|a|a|t|g|t|t|a|a|g|t|a|t|t|ei
c|c|c|t|g|g|a|c|c|a|g|t|c|t|g|t|g|a|c|c|c|a|t|t|a|t|g|g|g|t|a|a|t|g|a|c|c|c|c|c|t|t|c|c|t|g|c|c|c|t|g|g|c|a|t|t|c|c|ei
c|c|t|t|t|g|a|g|g|a|c|a|g|c|a|c|c|a|a|g|a|a|g|g|g|c|a|g|g|t|a|c|g|t|t|c|c|c|a|c|c|t|g|c|c|c|t|g|g|t|g|g|c|c|g|c|c|a|ei
c|a|c|a|g|c|c|a|a|t|g|c|c|c|g|t|c|c|t|t|g|c|c|c|g|c|a|g|a|a|c|c|t|a|g|a|g|c|t|g|c|t|c|c|g|c|a|t|c|t|c|c|c|t|g|c|t|g|ei
g|t|t|t|t|t|c|t|t|c|c|g|c|c|t|t|c|t|g|g|t|t|g|c|t|t|a|g|c|c|a|g|a|a|c|c|a|g|t|g|c|t|t|c|t|a|t|a|a|c|t|c|c|a|g|t|t|a|ei
g|a|a|g|g|c|t|t|g|a|g|g|c|c|t|g|g|a|g|t|t|t|g|g|c|c|a|g|c|c|t|g|g|c|c|a|a|c|a|t|a|a|c|a|a|g|a|c|c|t|c|a|t|c|t|c|t|t|ei
a|c|c|a|g|t|c|t|t|g|t|c|a|c|a|g|a|g|g|a|a|a|t|g|g|a|a|t|g|t|c|c|a|t|a|a|a|g|a|g|a|t|t|c|a|a|a|t|g|t|c|g|g|t|t|g|a|a|ei
t|a|a|a|a|a|a|g|a|c|t|c|t|c|t|g|c|t|g|t|g|g|g|g|t|c|c|c|t|t|c|a|g|a|g|a|g|a|g|a|g|a|g|a|c|c|a|g|a|a|a|t|a|a|t|c|t|t|ei
t|a|g|a|c|c|a|a|c|a|g|g|g|g|a|g|t|t|t|a|t|g|t|t|a|a|t|t|t|g|a|t|g|a|a|g|a|t|g|a|g|a|t|g|t|t|c|t|a|t|g|t|g|g|a|t|c|t|ei
a|a|a|g|c|a|g|a|t|c|a|g|c|t|g|t|a|t|a|a|a|c|a|a|a|a|t|t|a|t|t|c|g|t|g|g|t|t|t|c|t|g|t|c|a|c|t|t|g|t|g|t|g|a|t|g|g|t|ei
c|t|a|g|a|g|g|a|a|g|g|c|a|t|c|c|a|a|a|c|g|c|t|a|g|g|g|g|g|t|g|a|g|g|g|t|g|g|c|g|c|c|a|g|g|g|g|t|c|a|c|c|a|a|t|c|c|t|ei
t|a|g|t|a|a|a|a|a|c|a|c|c|a|c|t|t|a|c|t|a|a|a|a|c|t|g|a|t|t|t|g|c|t|a|a|a|g|c|a|g|a|c|c|t|c|a|t|t|c|c|a|t|t|t|a|a|g|ei
a|a|a|g|t|g|t|a|a|t|t|t|a|a|a|c|t|a|g|g|g|t|c|a|a|t|g|a|t|a|a|g|t|c|c|g|g|a|g|t|c|c|t|t|c|c|a|g|t|g|a|a|a|t|a|a|g|g|ei
c|c|a|g|a|g|c|c|c|a|a|g|t|g|c|c|c|c|c|t|g|t|c|c|g|c|a|g|c|t|c|c|a|t|g|g|c|a|g|c|c|c|g|t|c|t|g|c|t|c|c|t|c|c|t|g|g|g|ei
t|g|c|g|c|t|c|t|c|c|g|c|t|g|c|g|g|g|c|g|c|c|c|g|g|c|g|c|g|c|a|a|c|c|c|c|a|c|c|c|c|g|c|t|g|g|c|t|c|c|g|t|g|c|c|g|t|g|ei
g|c|t|g|a|t|a|a|a|g|c|t|g|c|c|t|g|c|c|t|g|t|t|c|a|a|a|g|g|t|a|t|t|a|t|g|c|a|a|a|a|g|a|a|t|a|g|a|a|a|a|a|a|a|g|a|g|t|ei
a|t|c|c|a|g|t|c|t|a|a|t|a|a|g|a|a|a|a|a|g|a|t|a|c|t|c|g|t|a|g|g|a|g|t|g|t|c|c|g|t|g|g|a|t|c|a|c|a|a|g|c|c|c|a|a|g|a|ei
g|c|t|t|t|g|t|g|a|g|a|t|a|a|a|a|c|t|c|t|c|c|t|t|c|c|t|t|a|c|c|a|t|a|c|c|a|c|t|t|t|g|a|c|a|c|g|c|t|t|c|a|a|g|g|a|t|a|ei
c|a|c|g|c|a|c|a|t|g|t|a|a|a|g|c|c|c|c|t|t|c|t|c|a|a|a|g|g|t|a|a|t|t|t|c|t|g|a|g|c|a|t|a|c|t|g|t|a|t|a|a|a|a|c|a|a|t|ei
g|g|a|c|a|g|c|t|c|a|c|c|t|a|g|c|g|g|c|a|a|t|g|c|a|c|a|g|g|t|a|a|g|c|g|c|c|c|c|t|a|a|a|a|t|c|c|c|t|t|t|g|g|g|c|a|c|a|ei
c|t|c|c|c|t|c|t|g|t|t|g|c|c|t|c|c|g|g|t|t|t|c|c|c|c|a|g|g|c|t|c|c|c|g|g|a|c|g|t|c|c|c|t|g|c|t|c|c|t|g|g|c|t|t|t|t|g|ei
a|t|a|t|c|t|t|c|g|t|t|t|a|a|a|a|a|c|t|a|g|a|c|g|a|t|c|a|t|t|c|t|c|t|g|a|a|a|c|a|a|c|g|t|a|a|t|g|a|t|t|t|g|t|g|c|g|t|ei
t|t|c|a|a|a|a|a|a|a|a|a|a|t|c|t|a|g|g|a|a|g|t|c|a|a|c|c|t|t|t|t|t|t|t|t|t|t|c|t|c|c|t|g|t|c|c|t|c|t|t|c|c|c|t|t|c|t|ei
c|a|a|a|c|c|a|c|c|t|g|c|c|c|c|a|t|c|c|a|t|t|g|c|t|c|a|g|g|t|g|a|t|c|c|t|t|g|g|c|g|g|a|g|g|c|c|g|c|a|a|g|t|a|c|a|t|g|ei
t|c|a|c|t|t|t|t|t|c|c|c|t|t|c|t|t|t|t|t|c|c|t|a|c|c|a|g|g|g|a|a|c|c|g|a|a|g|a|c|g|t|g|t|t|t|g|c|a|a|a|t|g|t|c|c|c|c|ei
t|c|c|c|t|c|c|a|t|t|g|c|c|c|t|c|c|g|g|t|t|t|c|c|c|c|a|g|g|c|t|c|c|c|g|g|a|c|g|t|c|c|c|t|g|c|t|c|c|t|g|g|c|t|t|t|t|g|ie
c|t|t|a|a|g|g|a|t|t|c|a|c|a|c|g|t|a|t|t|t|t|t|t|t|c|a|g|g|g|c|t|a|c|c|a|t|a|t|t|t|t|t|t|g|c|c|c|a|g|t|t|t|g|t|t|c|a|ei
t|c|t|a|g|a|a|g|g|g|c|t|g|a|g|a|c|c|a|t|g|c|a|t|t|t|c|a|c|a|g|c|t|g|t|a|t|c|c|c|c|t|a|g|a|a|c|a|g|t|g|c|c|t|g|a|t|a|ei
t|c|c|t|c|t|g|t|c|a|c|c|c|a|c|c|c|t|c|c|c|c|t|c|c|c|a|g|g|t|c|c|a|g|c|a|t|g|c|c|a|g|c|a|a|a|c|a|g|a|t|c|a|g|t|g|c|t|ei
a|t|c|c|c|c|a|g|a|t|c|c|t|a|a|g|a|g|g|c|c|g|a|t|g|t|a|t|c|t|g|g|g|c|a|g|a|a|a|g|a|t|c|g|a|t|a|t|a|c|c|t|a|t|a|a|c|g|ei
a|c|g|c|a|g|c|t|c|a|t|c|t|c|c|a|a|c|a|t|g|g|a|a|t|g|a|c|g|t|g|c|g|a|c|c|c|c|c|a|g|g|a|c|c|a|a|g|g|g|c|t|g|g|g|g|c|t|ei
c|a|a|t|g|g|a|c|c|c|c|a|a|c|t|g|c|t|c|c|t|g|t|c|g|c|t|g|g|t|a|a|g|g|g|a|c|g|c|c|c|g|g|g|t|t|c|t|g|t|g|c|c|t|t|g|g|a|ei
a|g|c|a|a|g|c|c|t|c|a|c|a|c|a|c|t|t|c|t|g|c|t|c|t|c|a|g|g|g|a|t|g|g|g|g|g|t|g|t|c|t|a|c|g|g|t|g|a|c|a|g|c|t|g|c|c|a|ie
t|c|t|g|a|t|g|a|c|t|a|t|g|c|a|c|t|c|c|t|t|c|c|c|t|c|a|g|g|t|g|g|a|t|a|a|c|t|c|a|t|c|c|t|t|a|a|c|a|g|g|a|g|a|g|t|c|g|ei
c|c|c|t|t|g|c|c|a|c|c|c|c|c|g|a|a|g|a|c|a|a|g|a|c|a|a|g|c|c|c|a|a|c|a|g|a|t|g|a|a|t|c|a|a|a|a|a|g|a|c|t|t|t|c|t|g|a|ei
c|c|t|g|g|c|a|t|c|g|a|g|t|c|g|g|t|a|g|a|t|g|c|a|g|a|a|t|g|c|t|g|t|t|a|a|a|c|a|t|t|c|t|a|t|a|g|t|a|c|a|c|a|g|g|a|t|g|ei
t|a|t|a|t|a|t|a|t|t|c|a|g|a|g|t|t|t|a|t|t|t|g|t|g|c|t|g|t|t|t|g|g|t|t|a|a|a|t|a|a|c|a|c|g|t|t|a|a|a|g|c|a|t|a|t|t|g|ei
g|t|g|g|g|a|c|c|t|c|a|a|c|t|c|c|t|t|c|c|c|c|a|c|a|c|a|g|a|a|a|t|g|g|t|g|c|t|a|c|c|c|a|g|c|t|c|a|a|g|c|c|t|g|g|g|c|c|ei
c|t|c|a|c|t|c|t|g|c|t|t|g|t|a|c|t|c|c|c|t|c|c|t|c|c|a|g|g|t|g|c|c|c|g|c|c|c|c|t|g|c|a|t|c|c|c|t|a|a|a|a|g|c|t|t|c|g|ei
c|t|g|c|c|t|c|c|c|g|c|t|t|t|g|t|g|t|g|c|c|c|c|c|c|c|a|g|c|a|g|c|c|t|c|c|c|g|c|g|a|c|g|a|t|g|c|c|c|c|t|c|a|a|c|g|t|t|ei
a|c|c|a|g|g|c|t|c|c|c|t|c|c|c|t|c|g|c|t|c|t|c|c|g|c|a|g|t|g|c|t|c|c|t|t|c|c|a|g|g|a|c|c|t|g|g|a|c|c|t|c|t|g|c|c|c|t|ei
c|a|g|c|a|t|c|t|c|c|c|c|c|c|t|c|t|g|g|c|c|t|t|c|g|c|a|g|g|t|g|g|t|c|g|c|a|t|c|g|a|c|c|a|t|g|g|t|c|a|t|c|a|t|g|a|a|a|ie
g|c|a|c|a|g|c|c|a|c|t|g|c|c|g|g|t|c|c|t|t|c|c|c|g|c|a|g|a|a|t|c|t|a|g|a|g|c|t|g|c|t|c|c|g|c|a|t|c|t|c|c|c|t|g|c|t|g|ie
t|c|t|a|t|t|g|g|a|a|a|c|c|t|c|a|t|c|t|t|t|c|t|c|t|c|a|g|a|g|c|c|c|c|t|t|t|a|a|c|a|a|c|c|g|c|t|g|g|t|a|t|c|a|a|a|t|g|ei
c|g|g|c|g|a|g|c|g|g|g|c|g|g|g|c|a|g|a|c|g|g|a|c|a|c|g|g|a|c|t|c|g|c|g|c|c|g|c|g|t|c|c|a|c|c|t|g|t|c|g|g|c|c|g|g|g|c|ei
g|a|c|t|a|t|t|a|t|t|c|c|c|t|a|c|t|t|t|t|g|g|g|a|a|g|t|a|a|a|t|t|g|t|c|t|g|a|t|t|c|c|t|a|c|a|a|a|c|t|g|t|g|t|g|a|a|t|ei
g|t|a|t|a|a|t|c|c|a|a|a|g|a|t|g|g|t|c|a|a|g|g|c|c|a|a|g|g|t|a|t|g|t|a|t|g|a|c|a|t|t|t|t|g|a|c|a|c|a|g|a|a|t|a|t|t|t|ei
a|c|t|g|a|a|a|g|t|a|c|a|g|a|g|a|a|a|t|g|t|t|c|g|a|a|a|t|g|a|a|a|a|c|c|a|t|g|t|g|t|t|t|c|c|t|a|t|t|a|a|a|a|g|c|c|a|t|ei
c|c|t|g|a|t|t|a|a|t|g|a|c|a|g|t|c|g|t|g|g|a|a|c|t|g|g|g|a|g|t|c|a|a|t|g|c|a|c|t|t|c|t|g|t|c|c|c|a|c|c|c|c|a|c|t|c|c|ei
a|c|t|t|a|a|a|g|g|a|c|a|a|a|c|a|g|g|c|t|t|t|c|a|g|g|c|t|g|a|c|t|g|g|g|c|c|t|c|c|a|g|g|g|t|c|g|c|a|g|g|g|a|g|a|g|c|t|ei
g|g|a|g|g|c|a|g|c|c|t|c|t|t|g|a|t|g|g|t|c|t|t|g|g|g|c|a|c|t|g|c|t|c|g|t|t|t|t|c|t|a|t|a|t|c|a|c|c|a|a|a|a|g|g|a|a|a|ei
t|a|c|c|a|g|c|a|a|c|t|c|t|g|c|a|t|c|t|a|c|t|g|a|a|a|a|g|t|a|t|t|a|t|g|a|c|t|t|t|a|a|a|a|a|c|c|c|c|a|t|t|a|t|t|g|a|a|ei
t|g|g|g|g|c|t|g|c|g|g|a|c|t|t|t|c|t|c|g|t|c|g|g|c|c|c|a|c|a|a|a|a|g|t|a|a|a|g|c|t|t|g|g|g|g|a|c|c|t|g|g|g|g|g|g|a|g|ei
g|c|t|g|a|c|c|c|c|c|t|a|c|c|c|c|g|c|c|t|t|g|t|t|g|c|a|g|a|c|g|g|t|g|a|c|c|a|g|t|g|c|t|t|g|g|t|c|t|t|g|c|c|c|t|t|g|g|ei
t|g|g|c|g|a|g|t|a|t|g|g|t|g|c|g|g|a|g|g|c|c|c|g|a|g|a|g|g|t|g|a|g|g|c|t|c|c|c|t|c|c|c|c|t|g|c|t|c|c|g|a|c|c|c|g|g|g|ei
c|c|a|a|g|g|c|t|g|a|c|c|g|g|g|g|t|g|g|g|g|t|c|c|g|c|a|g|g|t|a|a|c|t|g|t|g|c|t|g|a|g|g|g|t|c|t|g|g|g|t|a|c|g|a|a|c|t|ei
c|c|t|c|a|t|t|g|a|t|t|a|a|t|a|c|a|t|c|a|t|c|t|a|a|c|t|t|t|c|a|t|g|a|g|t|t|c|t|t|c|c|a|t|t|t|c|a|a|a|g|a|c|t|c|a|c|t|ei
a|c|c|c|t|g|c|t|g|g|t|g|a|t|g|g|g|c|a|t|c|t|t|g|c|g|a|t|g|a|g|g|a|t|g|t|g|a|a|a|c|a|g|a|t|c|t|t|g|a|a|g|a|t|g|a|t|t|ei
a|a|a|a|t|a|c|t|g|t|t|t|c|a|c|a|c|a|t|t|c|t|t|c|a|g|a|a|c|t|c|g|a|a|g|t|a|g|g|a|t|t|a|t|a|g|c|a|a|g|g|t|a|a|t|a|a|c|ei
c|t|c|c|a|a|g|g|t|c|c|g|c|t|c|c|c|c|g|g|t|c|a|c|g|g|a|t|c|c|t|g|t|t|c|a|a|t|a|a|t|g|a|a|a|t|g|g|a|c|g|a|c|t|t|c|a|g|ei
c|g|a|c|g|g|c|a|a|g|g|a|t|t|a|c|a|t|c|g|c|c|c|g|a|a|g|a|g|g|a|c|c|t|g|c|g|c|t|c|t|t|g|g|a|c|c|g|c|g|g|c|g|g|a|c|a|t|ei
t|a|g|c|a|c|a|t|g|t|g|a|c|t|g|g|a|c|t|c|c|t|c|c|c|c|a|g|g|t|c|g|t|c|a|g|t|g|a|g|g|c|c|a|c|a|c|a|g|c|a|g|c|a|g|c|a|t|ei
c|c|c|g|c|c|t|g|c|t|g|a|g|c|c|c|c|a|t|g|g|c|c|g|g|c|t|g|c|t|c|t|c|t|c|c|g|c|c|g|c|c|c|c|c|a|g|c|a|a|t|c|c|c|c|g|g|c|ei
a|t|t|g|c|t|c|t|g|a|a|g|c|a|a|c|a|g|c|g|t|a|c|a|g|a|a|a|a|a|t|a|a|a|g|a|a|g|a|g|g|c|t|g|c|a|g|a|a|t|a|t|g|c|t|a|a|a|ei
c|c|t|t|t|t|c|t|t|t|t|c|t|a|c|c|a|c|a|t|g|g|c|a|g|c|a|t|g|a|a|t|t|t|t|c|c|a|a|a|t|t|t|t|t|t|a|t|g|c|t|c|t|g|c|t|t|c|ei
g|g|t|c|t|c|t|c|c|t|t|c|t|c|t|t|g|c|t|t|c|a|c|t|g|c|a|g|a|g|g|c|t|g|g|a|a|g|a|c|g|g|c|a|g|c|c|a|c|c|t|g|a|c|t|g|g|g|ei
c|g|c|a|g|c|g|g|a|g|g|t|g|a|a|g|g|a|c|g|t|c|c|t|c|c|c|a|g|g|a|g|c|c|g|a|c|t|g|g|c|c|a|a|t|c|a|c|a|g|g|c|a|g|g|a|a|g|ei
t|c|c|t|c|t|c|a|c|c|a|c|t|t|t|t|c|t|t|g|g|t|c|c|c|c|a|g|g|g|t|g|c|t|g|c|c|g|c|c|c|c|a|g|g|t|a|c|a|g|a|c|c|g|a|g|a|t|ei
g|g|c|c|a|g|a|t|c|g|t|g|c|c|a|t|a|g|c|a|c|t|c|a|t|t|t|g|g|g|t|g|a|t|a|g|a|g|g|g|a|g|a|c|t|c|t|g|t|c|t|c|a|a|a|a|a|a|ei
t|a|c|t|t|a|a|a|a|t|a|t|a|t|t|c|t|t|a|t|t|c|t|t|a|t|a|g|g|a|t|a|a|a|t|c|t|t|c|a|g|a|c|a|a|a|a|a|a|g|t|g|c|a|a|a|c|a|ei
t|a|t|c|t|c|a|a|a|a|c|t|a|t|t|c|t|g|c|a|t|g|g|g|t|g|t|a|a|t|g|g|t|g|g|a|t|a|c|a|t|g|a|c|a|t|g|t|t|a|t|g|t|t|t|g|c|c|ei
c|c|c|t|c|a|c|c|c|c|a|a|t|t|c|c|c|c|g|c|t|g|c|t|c|t|a|g|g|a|t|a|a|g|t|g|t|g|a|g|c|c|a|c|t|g|g|a|g|a|a|g|c|a|g|c|a|c|ei
a|g|t|a|t|t|g|t|c|c|c|t|a|g|c|t|g|t|a|c|t|t|a|t|t|g|c|a|a|a|t|g|a|a|g|t|t|t|g|g|c|c|t|t|g|a|g|t|t|t|c|c|c|t|t|t|t|c|ei
a|c|c|a|c|t|c|t|g|c|t|t|c|g|g|g|c|t|c|t|g|g|g|g|c|c|a|g|g|t|g|a|g|t|a|g|g|a|g|c|g|g|a|c|a|c|t|t|c|t|g|c|t|t|g|c|c|c|ei
t|g|g|a|a|c|a|a|c|c|t|c|t|c|t|c|t|a|c|a|a|t|c|c|c|c|a|g|a|t|c|t|t|c|g|c|a|a|a|t|a|c|t|g|t|g|g|a|c|a|a|t|g|c|c|c|g|c|ei
g|a|a|a|a|g|a|a|a|c|t|t|a|t|t|t|c|t|g|t|t|g|a|a|g|g|a|a|c|a|t|t|c|c|a|a|t|a|t|c|t|a|t|c|t|t|c|a|a|a|a|t|g|g|c|c|c|a|ei
a|t|c|g|t|g|g|a|g|a|t|g|c|a|g|c|t|g|a|g|g|c|a|c|c|a|a|g|g|t|g|g|g|g|a|c|t|c|t|a|c|g|t|g|g|a|c|g|g|c|c|t|c|c|c|c|t|c|ei
g|c|t|c|a|g|g|g|c|t|t|c|t|t|g|t|c|c|t|t|t|c|c|t|c|c|a|g|g|g|c|g|t|g|a|t|g|g|t|g|g|g|c|a|t|g|g|g|t|c|a|g|a|a|g|g|a|t|ei
t|a|t|t|a|t|t|g|g|a|a|a|t|c|t|t|c|a|a|g|t|t|c|g|a|a|a|g|g|t|g|a|g|c|a|t|t|t|t|t|t|a|a|t|t|t|g|t|t|t|t|t|a|t|g|a|c|c|ei
c|c|c|a|a|g|g|c|c|a|a|c|c|g|c|g|a|g|a|a|g|a|t|a|c|c|a|g|g|t|g|a|g|t|g|g|c|c|c|g|c|t|a|c|c|t|c|t|t|c|t|g|g|t|g|g|c|c|ei
g|t|g|c|a|a|g|g|t|g|t|g|a|c|g|c|c|c|c|t|t|c|a|c|g|g|c|c|g|c|c|c|a|g|g|a|g|g|g|c|c|a|c|g|c|a|g|a|g|a|t|g|g|t|g|g|c|t|ei
c|g|c|c|c|t|a|a|c|g|c|g|g|c|c|c|c|c|t|c|g|c|c|c|g|c|a|g|c|c|t|a|a|t|g|g|c|a|c|t|c|g|a|g|t|g|c|c|c|a|t|g|g|a|a|g|t|g|ei
g|a|g|a|t|t|t|c|t|t|c|t|t|a|g|g|t|t|t|g|g|a|t|t|t|t|c|g|c|t|g|g|g|g|t|c|c|a|g|t|g|t|g|g|a|g|g|t|g|g|t|a|g|g|g|g|a|g|ei
t|t|t|t|a|c|a|t|t|t|t|t|c|a|c|t|t|t|t|c|c|t|c|c|a|c|a|g|c|g|t|g|a|g|t|g|c|a|t|c|t|c|c|a|t|c|c|a|c|g|t|t|g|g|c|c|a|g|ei
c|c|a|c|c|c|g|t|c|c|g|a|c|a|a|c|t|t|c|c|g|g|a|t|c|c|a|g|g|t|a|g|g|g|a|g|g|a|g|c|c|c|c|t|g|t|t|a|g|c|a|c|t|g|c|c|a|g|ei
c|a|t|a|t|g|t|t|g|a|a|a|a|a|t|g|a|t|c|a|a|a|t|a|g|a|t|a|t|t|t|a|g|g|a|t|g|t|g|c|a|t|c|a|g|c|t|c|a|t|g|t|a|t|t|t|a|c|ei
c|t|a|a|g|t|t|g|t|c|c|t|t|t|t|c|t|g|g|t|t|t|c|t|t|t|c|a|c|c|a|t|g|g|a|a|c|a|t|t|t|t|g|a|t|t|a|t|a|g|t|t|a|a|t|c|c|t|ei
a|t|t|c|c|t|c|t|a|g|c|g|a|g|a|a|t|c|a|c|c|c|t|c|a|g|a|c|t|t|c|c|g|t|t|t|a|c|c|a|g|a|a|a|t|c|g|c|a|a|t|t|c|c|a|g|a|a|ei
t|t|a|a|t|a|a|a|g|a|a|a|t|a|c|a|t|t|g|a|c|g|g|c|a|a|a|a|g|t|a|a|g|t|t|a|c|a|c|a|c|a|t|t|c|a|a|t|g|g|a|a|g|c|t|a|t|a|ei
c|c|t|g|a|a|c|c|a|c|c|t|t|c|a|a|c|t|t|g|t|t|c|a|a|c|a|g|g|a|t|g|c|c|a|g|g|c|c|a|a|g|g|t|g|g|a|g|c|a|a|c|c|g|g|t|g|g|ei
g|g|a|a|t|c|t|t|c|a|c|t|c|t|g|a|a|a|t|t|t|c|c|t|g|c|a|g|g|t|g|a|c|c|a|g|t|t|g|t|c|t|c|t|g|t|t|t|g|g|g|c|a|t|t|c|c|c|ei
g|t|g|g|a|g|c|a|g|c|t|g|a|c|c|c|a|g|g|a|g|t|t|t|t|g|a|g|g|t|a|a|g|g|c|t|g|g|g|c|t|c|c|t|g|a|g|g|c|c|a|c|c|t|c|g|g|g|ei
c|g|c|a|g|a|g|c|c|a|t|g|a|a|g|a|a|g|a|a|g|t|t|g|g|g|t|g|c|t|g|g|g|c|c|t|g|c|t|g|g|c|c|g|t|g|g|t|c|c|t|g|g|t|g|c|t|g|ei
a|g|g|a|g|t|t|t|g|g|t|a|a|a|g|a|t|t|g|g|t|a|a|t|a|g|g|g|c|a|t|t|t|a|a|g|a|t|t|t|g|c|c|a|t|g|g|g|t|t|g|c|a|a|a|a|g|t|ei
a|a|g|g|a|a|a|t|t|t|t|c|c|a|a|a|a|t|g|t|g|g|a|g|c|a|c|a|g|t|a|a|g|g|c|c|a|c|c|a|t|g|g|g|t|c|c|a|g|a|g|g|a|t|g|a|g|g|ei
g|t|g|c|a|c|a|t|c|a|a|a|c|t|g|c|c|c|c|t|g|c|t|a|c|a|a|a|g|t|a|a|a|g|g|a|g|t|t|g|t|g|g|g|g|t|t|a|c|a|g|a|g|g|g|g|t|g|ei
a|g|g|a|c|a|g|a|g|g|a|g|g|c|g|c|g|t|c|c|g|g|c|t|c|c|t|g|g|t|g|a|g|c|g|t|g|t|c|t|g|c|c|c|t|c|c|c|t|g|c|g|t|c|a|g|g|a|ei
c|c|c|t|c|c|c|a|c|t|c|g|t|t|g|c|t|c|t|c|c|g|g|c|g|c|a|g|c|t|t|g|a|g|c|c|t|g|a|t|c|g|a|g|t|g|c|g|g|c|c|c|a|g|t|g|c|a|ei
g|g|c|c|c|a|t|c|c|a|g|g|c|t|a|a|t|c|a|c|a|c|g|g|a|c|a|g|g|t|a|a|c|c|a|t|t|a|c|a|c|c|c|c|t|c|a|c|c|c|c|c|t|g|g|g|c|c|ei
c|t|c|a|c|t|g|g|c|t|t|t|t|t|t|t|t|c|t|c|t|t|t|t|g|c|a|g|g|t|g|t|c|t|c|c|t|g|c|a|c|c|t|g|c|g|c|t|g|g|t|t|c|c|t|g|c|a|ei
g|a|t|g|g|t|g|g|g|a|c|a|t|c|a|a|a|c|t|g|c|g|c|g|c|t|c|c|g|t|g|a|a|a|g|g|c|a|g|a|t|t|c|a|c|c|a|t|c|t|c|a|a|g|a|g|a|t|ei
g|a|t|g|t|a|c|c|c|t|g|g|g|a|t|c|g|c|t|g|a|c|c|c|t|g|c|a|g|a|a|a|g|a|g|a|t|c|a|c|c|g|c|g|c|t|g|g|c|a|c|c|c|a|g|c|a|c|ei
t|t|g|a|a|c|t|g|g|g|g|a|a|g|c|g|a|a|g|g|t|g|g|a|t|g|a|g|c|t|g|a|g|a|t|t|g|c|g|c|c|a|t|t|a|c|a|c|t|c|c|a|g|c|c|t|g|g|ei
g|t|c|a|g|g|g|t|g|t|c|c|c|c|c|a|t|g|c|c|t|g|g|a|a|g|g|a|g|c|t|g|g|t|g|c|t|g|c|c|a|g|c|c|c|t|g|g|g|c|c|c|g|g|c|a|c|a|ei
t|t|g|c|c|c|t|c|a|g|c|a|t|c|a|c|c|a|t|g|a|a|c|g|g|a|g|g|c|c|a|t|c|g|c|c|t|g|c|g|c|t|g|a|g|g|g|c|t|g|c|c|a|g|g|c|c|a|ei
c|g|c|c|g|c|a|c|c|c|c|c|a|c|t|c|g|c|c|g|g|c|t|g|c|c|a|g|g|t|a|a|t|g|g|c|a|c|t|g|a|g|c|a|g|a|a|g|g|g|a|a|g|a|a|g|c|t|ei
g|g|a|c|a|g|c|t|c|a|c|c|t|a|g|c|g|g|c|a|a|t|g|c|g|c|a|g|g|t|a|a|g|c|g|c|c|c|c|t|a|a|a|a|t|c|c|c|t|t|t|g|g|g|c|a|c|a|ei
g|a|a|g|c|g|a|a|g|c|c|g|a|a|a|a|a|g|g|c|a|g|c|g|g|a|a|g|g|t|a|a|g|c|c|t|c|g|a|a|a|c|g|c|g|c|a|t|t|g|g|g|a|t|g|c|a|g|ei
c|t|a|g|c|g|g|g|c|a|g|c|t|c|g|a|g|g|a|a|g|t|g|a|c|t|t|a|c|a|c|g|t|t|g|g|t|c|t|c|c|t|g|t|t|t|c|c|t|t|a|c|c|a|a|g|c|t|ei
g|c|t|g|g|c|t|c|t|g|t|g|a|g|g|g|t|g|c|t|g|a|c|g|c|t|t|c|a|g|c|a|a|g|t|t|a|g|a|a|c|t|a|g|c|c|a|a|a|c|c|a|g|g|a|c|c|c|ei
c|a|a|g|c|c|t|g|a|a|a|c|c|a|t|c|t|t|a|t|a|c|t|t|g|c|a|g|g|t|a|a|g|t|c|c|a|t|a|c|a|g|a|a|g|a|g|c|c|c|t|c|t|c|t|c|c|c|ei
c|g|c|c|g|c|a|a|g|t|g|g|a|t|c|c|a|g|t|g|c|t|t|a|c|g|a|t|g|t|g|a|c|t|g|c|c|a|t|c|a|t|c|t|t|c|g|t|g|g|t|g|g|c|c|a|g|c|ei
g|t|a|t|t|t|a|a|t|a|t|a|t|t|t|t|t|g|c|t|c|a|t|t|g|c|a|g|g|g|g|a|a|g|a|g|a|a|g|a|c|a|a|a|a|c|g|a|g|t|c|t|t|t|c|a|t|t|ei
a|c|a|g|g|a|a|c|c|a|t|g|a|t|g|c|t|g|g|c|a|t|c|g|t|c|a|g|c|t|t|c|t|g|a|g|g|a|a|g|c|c|t|c|a|a|g|a|a|a|c|t|t|t|c|a|a|t|ei
g|g|a|a|g|g|a|g|g|g|g|t|a|a|t|g|g|g|g|t|a|c|a|a|a|t|g|a|t|g|a|a|t|t|t|c|t|t|t|g|t|c|c|c|a|a|t|c|c|a|c|t|t|t|t|a|c|c|ei
g|g|g|c|c|c|c|c|t|g|g|g|g|a|a|a|g|g|g|g|c|c|t|c|t|g|g|a|g|a|a|g|t|c|c|t|g|g|g|a|g|c|t|c|a|g|c|c|c|g|g|g|c|c|a|c|g|g|ei
g|a|a|g|t|c|a|c|t|c|a|t|t|t|t|c|t|c|c|t|t|t|t|a|a|c|a|g|g|t|g|t|c|t|g|a|a|g|c|a|g|c|c|a|t|g|g|c|a|g|a|a|g|t|a|c|c|t|ei
g|g|c|t|a|c|c|c|g|a|g|c|c|c|g|t|c|a|c|c|c|t|g|g|t|g|g|a|g|t|a|a|g|g|a|g|g|g|g|g|a|t|g|g|g|a|g|g|t|c|a|t|g|t|c|t|c|t|ei
c|a|a|a|c|a|g|a|g|t|g|a|a|c|t|t|t|c|t|g|c|c|a|g|t|g|c|g|g|t|t|a|g|a|a|c|c|c|t|t|c|c|c|a|g|g|g|c|a|c|g|g|g|a|g|a|g|c|ei
g|c|t|g|c|a|c|t|g|g|a|t|g|g|g|a|c|c|t|t|c|c|a|a|g|a|a|g|g|t|a|a|g|g|c|g|t|c|t|g|a|t|c|c|a|g|g|t|c|t|g|g|a|g|c|t|g|g|ei
a|t|g|t|t|t|a|a|a|c|c|t|c|g|c|g|t|t|t|c|c|t|c|c|g|c|a|g|c|t|c|t|t|g|g|g|c|a|a|t|g|t|g|c|t|g|g|t|g|t|g|t|g|t|g|c|t|g|ei
t|t|c|a|c|c|t|c|t|t|c|c|t|c|t|g|g|t|t|c|c|t|t|c|t|c|t|c|t|c|t|a|c|c|t|c|c|a|c|c|c|t|g|c|a|t|t|t|t|c|c|t|c|t|t|g|t|c|ei
c|t|t|a|c|c|c|c|a|a|a|g|a|g|a|a|a|g|a|g|t|t|t|a|a|c|t|c|g|a|g|a|c|c|a|t|a|a|a|g|a|t|a|t|t|c|t|t|t|a|g|t|g|g|a|g|g|c|ei
a|a|c|c|t|g|a|g|t|a|g|a|g|a|c|a|c|t|g|c|t|g|c|g|g|a|t|g|g|t|a|a|g|t|g|a|g|a|g|a|a|t|g|t|g|g|g|c|c|t|g|t|g|c|c|t|a|g|ei
c|t|g|a|c|c|c|g|a|c|c|t|t|g|a|a|c|t|t|g|t|t|c|a|a|c|a|g|g|a|t|g|c|c|a|g|g|c|c|a|a|g|g|t|g|g|a|g|c|a|a|g|c|g|g|t|g|g|ei
a|a|a|t|c|c|a|a|c|a|c|c|t|c|a|g|c|g|a|t|g|t|g|g|a|c|c|a|c|a|t|t|c|a|a|c|c|t|c|a|t|t|c|t|g|a|t|g|c|c|t|g|a|a|a|a|g|c|ei
a|c|c|a|g|g|a|g|t|t|t|a|t|a|a|g|c|t|c|t|t|g|g|g|a|t|g|g|g|t|g|c|g|g|g|t|c|a|g|g|g|g|t|g|g|c|a|a|g|a|a|g|g|g|g|t|g|a|ei
a|a|c|a|g|a|g|a|g|a|g|a|a|c|a|g|c|g|g|c|a|a|g|c|a|a|g|a|a|g|c|c|c|g|g|g|a|c|t|c|c|t|g|a|g|a|a|c|a|a|t|a|a|g|g|a|g|t|ei
a|t|g|t|t|t|t|a|c|c|t|g|a|g|t|t|c|a|g|a|g|a|t|c|t|a|c|c|c|c|a|t|t|a|a|g|t|a|t|g|t|c|c|a|t|g|c|c|t|t|t|g|a|a|a|g|c|a|ei
t|t|c|c|t|a|t|t|c|t|t|c|c|a|c|a|t|c|c|t|c|t|c|a|c|a|c|c|t|t|t|t|g|t|t|t|c|c|t|g|a|c|t|t|t|t|t|a|a|t|a|a|t|t|g|c|c|a|ei
c|t|g|a|t|c|c|a|g|a|a|g|g|a|g|c|t|c|a|c|c|a|t|g|c|t|c|g|g|t|g|a|g|t|g|g|c|c|t|c|c|t|c|c|c|c|a|g|g|a|c|c|c|c|t|t|t|t|ei
a|g|a|a|c|g|g|g|a|a|g|g|a|g|a|c|g|c|t|g|c|a|g|g|g|c|g|g|g|t|a|c|c|a|g|g|g|g|c|c|a|c|a|g|g|g|c|g|c|c|t|c|c|c|g|g|a|t|ei
t|c|c|a|t|c|t|t|c|t|g|c|a|g|g|g|t|t|a|g|t|g|a|a|a|g|a|t|g|c|t|a|g|c|t|t|t|t|t|c|a|c|t|a|a|a|g|a|g|g|t|c|t|t|t|t|a|g|ei
t|c|a|c|c|g|t|g|g|c|c|a|c|t|g|g|c|a|g|c|c|a|g|g|t|t|c|g|c|c|g|g|c|a|c|t|g|a|c|g|a|c|t|a|c|a|t|c|t|a|c|c|t|c|a|g|c|c|ei
g|a|c|a|g|a|g|c|a|g|t|t|t|t|g|a|a|a|c|a|g|t|c|t|c|t|g|t|g|g|a|a|t|c|t|g|c|a|a|g|t|g|g|a|t|a|t|t|t|g|g|a|t|a|g|c|t|t|ei
g|g|g|c|c|c|c|t|c|t|g|a|t|c|a|c|c|t|c|c|a|c|t|c|a|t|a|g|g|t|a|t|g|a|g|a|c|a|g|a|g|c|t|g|g|c|c|a|t|g|c|g|c|c|a|g|t|c|ei
g|g|a|c|a|g|c|t|c|a|c|c|t|a|g|t|g|g|c|a|a|t|g|c|c|c|a|g|g|t|a|a|g|c|g|c|c|c|c|t|a|a|a|a|t|c|c|c|t|t|t|g|g|g|c|a|c|a|ei
t|a|t|a|t|a|t|c|c|a|c|a|t|g|t|g|c|t|c|a|g|t|a|c|g|g|t|g|g|g|a|g|t|t|g|a|t|t|t|g|t|c|t|t|c|t|c|a|c|t|g|t|t|c|t|c|t|t|ei
c|a|g|t|c|t|g|a|t|t|c|t|g|c|c|c|g|g|a|g|t|a|a|a|a|t|t|g|a|c|g|g|g|a|g|c|t|g|g|g|g|g|c|t|t|c|g|t|g|c|t|g|g|g|g|c|t|c|ei
g|c|t|c|t|g|a|t|g|a|g|t|c|t|c|t|c|a|t|c|g|c|t|g|a|a|a|g|g|t|c|a|g|a|t|t|c|t|g|g|g|g|a|g|c|t|g|a|a|g|t|g|g|t|c|g|g|g|ei
c|t|g|c|t|g|t|g|a|t|g|t|g|t|a|g|g|a|g|g|a|a|g|g|t|c|a|g|g|t|a|g|g|g|a|a|g|g|g|g|t|g|a|g|g|g|g|t|g|g|g|g|t|c|t|g|a|g|ei
c|c|a|a|g|a|a|c|c|t|c|a|t|c|c|t|c|t|t|c|c|t|g|g|g|a|t|g|g|t|g|a|g|t|g|a|g|c|a|a|g|g|c|c|t|g|t|c|c|a|g|c|c|c|c|g|t|a|ei
g|g|a|t|c|c|c|g|a|g|g|a|g|a|c|c|c|t|g|g|g|a|c|c|a|g|g|a|g|t|g|c|c|t|g|g|a|a|a|g|g|a|c|g|g|g|c|a|g|g|c|a|g|g|a|c|a|g|ei
g|t|g|t|t|a|c|c|g|a|g|g|g|c|a|t|t|t|c|t|a|a|c|g|c|t|t|c|t|t|a|c|t|a|c|g|g|c|c|t|c|c|g|c|c|g|a|c|c|g|c|g|c|g|c|t|c|g|ei
c|t|c|c|a|g|g|g|a|g|g|a|a|a|g|g|a|c|t|t|t|g|g|t|t|c|t|a|g|c|a|g|a|t|a|a|t|c|t|t|c|c|t|t|g|c|t|a|c|t|t|g|g|a|a|g|t|c|ei
g|c|a|c|a|g|c|c|a|c|t|g|c|c|g|g|t|c|c|t|t|c|c|c|g|c|a|g|a|a|c|c|t|a|g|a|g|c|t|g|c|t|c|c|g|c|a|t|c|t|c|c|c|t|g|c|t|g|ei
t|g|g|t|a|a|t|t|g|t|g|a|a|t|a|t|g|a|c|a|t|c|a|t|t|c|a|g|g|t|t|t|g|g|c|c|t|c|a|c|a|a|g|g|a|c|t|a|c|c|c|t|c|t|c|a|t|c|ei
g|t|g|g|g|g|g|t|c|c|c|c|g|c|a|t|g|c|t|g|c|t|g|c|c|c|a|g|g|t|g|a|g|t|t|t|g|a|c|t|c|c|c|t|g|c|c|c|t|g|t|c|t|g|t|c|c|a|ei
a|a|g|g|t|g|a|a|a|a|a|g|g|a|g|g|a|g|g|a|a|g|a|g|a|g|a|a|a|a|c|t|t|c|c|c|a|g|g|t|c|a|g|g|c|a|t|c|c|a|g|c|c|a|a|c|a|a|ei
a|g|c|g|c|c|t|g|g|t|g|g|t|c|c|t|a|c|a|c|c|t|g|a|g|a|a|g|g|t|a|t|g|t|g|g|g|g|c|c|c|a|g|c|c|c|c|a|a|g|c|t|t|g|g|c|a|c|ei
t|g|g|a|c|g|c|t|c|a|c|c|t|a|g|c|t|g|c|a|a|t|g|c|a|c|a|g|g|t|a|a|g|c|g|c|c|c|c|t|a|a|a|a|t|c|c|c|t|t|t|g|g|g|c|a|c|a|ei
c|a|c|c|g|c|c|t|a|c|c|t|g|c|a|g|t|g|g|a|g|c|a|c|t|g|a|a|g|g|c|c|t|c|g|g|a|c|a|c|c|g|c|c|a|t|g|t|a|t|t|a|c|t|g|t|g|c|ei
g|t|g|g|c|a|c|c|g|a|c|t|g|a|c|a|c|t|c|c|t|t|c|t|a|t|a|g|a|g|t|c|a|t|g|c|a|a|g|g|g|c|c|g|c|t|g|c|a|c|t|g|a|g|g|g|c|t|ei
t|g|c|g|a|c|c|a|g|a|c|g|t|g|a|a|t|g|a|g|a|g|c|a|a|g|c|g|g|t|g|a|g|t|g|a|g|g|c|t|g|a|a|t|g|g|c|c|c|g|t|g|c|a|g|g|g|g|ei
c|a|t|c|t|g|c|t|c|a|c|t|t|c|c|t|t|c|a|a|a|a|t|g|a|a|a|g|g|t|a|a|g|t|c|c|t|g|g|g|t|a|c|c|g|g|a|t|g|c|t|c|a|g|c|c|t|t|ei
g|c|t|c|a|g|c|t|c|c|c|a|g|g|t|c|a|c|c|c|a|g|g|a|t|g|a|g|g|t|g|a|g|t|g|t|c|c|c|c|a|t|c|c|t|g|g|c|c|c|t|t|g|a|c|c|c|t|ei
g|t|c|c|c|c|t|c|a|c|a|g|g|g|c|a|t|t|t|t|c|t|t|c|a|c|a|g|g|t|g|g|a|a|a|a|g|g|a|g|g|g|a|g|c|t|g|c|t|c|t|c|a|g|g|c|t|g|ie
a|g|c|t|g|g|g|a|c|t|a|c|a|g|g|c|a|c|a|c|g|c|c|c|t|c|g|c|c|c|g|g|c|c|c|g|a|t|c|t|t|t|c|t|a|a|a|a|t|a|c|a|g|t|t|c|t|g|ei
t|g|c|t|g|g|c|t|a|g|c|a|t|g|t|g|g|a|g|g|a|g|c|a|a|g|c|t|c|a|a|t|a|a|g|a|a|g|g|g|g|c|c|t|a|g|a|a|t|g|a|a|a|c|c|c|t|t|ei
g|c|c|a|t|g|g|t|c|a|a|g|a|t|t|c|t|c|c|a|g|c|t|t|t|a|t|t|t|g|a|a|a|a|a|g|g|g|c|c|a|a|g|g|a|t|c|c|a|c|c|a|c|a|a|c|a|c|ei
t|t|a|t|g|c|a|t|a|g|a|a|a|g|t|a|g|c|t|g|a|a|g|a|t|c|a|a|a|a|a|a|t|c|a|g|g|a|a|a|a|g|g|a|c|a|t|a|g|a|t|t|t|g|t|c|t|g|ei
a|g|a|t|g|g|a|g|g|g|c|a|t|c|c|t|t|c|a|g|g|a|g|g|g|a|t|g|a|g|a|c|c|t|c|a|t|c|a|t|a|c|t|t|g|a|c|t|g|t|c|c|a|g|c|a|t|c|ei
a|a|a|c|t|g|g|t|g|t|t|a|a|a|a|t|t|a|c|a|g|t|t|t|g|c|a|g|g|t|a|a|a|t|a|c|a|c|a|g|a|a|a|g|a|a|t|a|a|t|a|a|t|c|t|g|c|a|ei
a|c|t|c|a|g|g|c|a|a|t|g|a|t|g|t|c|a|c|g|g|a|t|t|g|c|a|g|g|t|c|a|g|t|c|t|t|t|g|g|t|t|g|g|g|t|a|g|g|a|g|t|g|t|g|c|a|t|ei
g|g|g|c|t|c|c|t|c|t|c|c|t|g|c|t|t|c|t|g|c|c|c|c|g|c|a|g|c|t|g|a|g|c|g|c|g|a|g|a|t|c|g|t|g|c|g|c|g|a|c|a|t|c|a|a|g|g|ei
t|g|c|t|g|a|g|g|c|a|a|a|g|g|a|t|g|t|c|t|t|c|c|g|g|c|a|t|g|t|a|a|g|t|a|g|a|t|a|a|g|a|a|a|t|t|a|t|t|c|t|t|t|t|a|t|a|g|ei
g|t|t|t|a|t|t|c|c|t|c|a|t|g|g|a|c|t|a|a|t|t|a|g|a|c|a|g|g|t|a|a|g|t|a|a|g|a|t|c|t|t|a|a|a|a|t|g|a|g|g|t|t|t|t|t|t|a|ei
c|t|c|t|t|t|g|t|c|c|t|t|t|g|g|g|c|c|c|t|t|g|g|g|a|g|a|a|c|a|g|t|g|c|a|t|c|c|t|t|c|a|g|a|a|c|a|g|t|g|c|a|t|c|t|t|a|a|ei
t|c|a|a|a|a|g|c|t|a|t|c|t|g|c|g|t|t|t|c|t|t|t|g|t|a|a|g|a|c|c|a|g|g|a|g|a|a|a|g|t|t|t|c|a|g|a|c|t|a|t|g|a|a|a|t|g|a|ei
t|t|t|a|c|t|a|a|t|t|t|a|a|a|g|a|c|c|t|g|t|t|t|c|a|t|a|g|g|a|g|c|t|c|a|g|t|c|t|g|a|a|t|a|t|t|c|t|t|g|g|a|g|a|a|a|g|a|ei
c|t|g|c|t|g|c|a|a|c|c|t|c|c|a|a|g|c|c|c|g|g|a|t|a|g|g|c|c|a|a|g|a|a|c|a|g|c|t|c|t|t|g|g|g|g|a|c|a|t|t|g|g|t|a|a|c|a|ei
a|a|g|a|c|t|t|a|t|a|t|t|t|g|t|c|c|t|t|t|t|g|t|t|t|c|a|g|c|c|t|a|c|c|a|t|g|a|g|a|a|t|a|a|g|a|g|a|a|a|g|a|a|a|a|t|g|a|ie
g|c|c|t|t|c|c|a|t|g|a|a|c|a|g|c|c|a|g|a|a|c|t|c|g|a|a|g|g|t|a|c|g|t|t|c|c|t|g|a|t|g|c|a|g|g|t|c|c|c|g|g|g|c|c|a|g|t|ei
t|g|c|c|c|a|c|a|c|a|a|t|a|a|t|a|a|t|g|g|g|a|g|c|t|t|a|a|c|a|c|c|c|c|a|c|t|g|t|c|a|a|c|a|t|t|a|g|a|c|a|g|a|t|c|a|a|c|ei
a|g|g|t|t|c|a|a|c|a|t|c|g|g|t|g|g|c|c|c|c|a|c|t|c|t|c|c|a|t|t|c|c|c|a|t|c|t|t|g|t|g|c|t|c|c|t|a|c|t|t|c|t|t|t|g|a|t|ei
c|t|a|g|a|g|g|a|a|g|g|c|a|t|c|c|a|a|a|c|g|c|t|a|g|g|g|g|g|t|g|a|g|g|g|t|g|g|c|g|c|c|a|g|g|g|g|t|c|g|c|c|a|a|t|c|c|t|ei
t|a|c|a|a|c|a|g|g|g|a|c|c|a|a|t|t|t|a|t|t|t|c|c|t|t|g|c|t|g|c|t|c|a|t|g|a|a|a|t|t|g|g|c|c|a|c|t|c|c|c|t|g|g|g|t|c|t|ei
c|t|g|a|g|a|t|t|c|c|a|g|c|a|t|c|c|t|g|c|a|a|c|t|c|a|g|t|t|c|t|g|a|a|a|t|a|t|t|t|t|c|a|g|t|t|g|t|a|g|c|t|a|a|g|g|g|c|ei
c|c|g|g|c|g|a|g|g|c|t|g|a|c|g|g|a|t|c|g|t|c|c|c|g|c|a|g|g|g|c|g|t|c|a|t|g|g|t|g|g|g|c|a|t|g|g|g|c|c|a|g|a|a|g|g|a|c|ei
g|c|t|c|t|c|c|a|c|c|t|g|c|t|t|c|t|t|t|c|t|g|t|c|t|t|t|t|g|c|g|a|t|t|c|t|g|c|t|t|t|a|g|t|g|c|c|a|c|c|a|g|a|a|g|a|t|a|ei
c|a|c|a|g|g|c|c|a|a|t|g|c|c|c|g|t|c|c|t|t|c|c|c|g|c|a|g|a|a|c|c|t|a|g|a|g|c|t|g|c|t|c|c|g|c|a|t|c|t|c|c|c|t|g|c|t|g|ei
a|g|t|t|c|t|g|c|a|g|c|a|c|c|c|c|t|g|c|c|t|g|c|c|g|a|g|g|g|t|a|a|g|t|g|g|c|a|g|c|c|a|c|c|c|c|g|c|c|t|t|t|c|c|c|t|g|a|ei
a|g|a|a|c|t|g|g|a|g|g|a|a|c|c|t|g|a|t|c|g|c|g|t|c|t|g|g|g|t|g|g|g|t|a|c|c|a|c|t|c|t|c|c|c|c|t|g|t|c|c|g|a|c|c|g|c|g|ei
t|g|g|g|g|g|t|g|c|c|t|g|g|g|c|t|g|c|a|g|a|a|g|g|t|c|a|g|g|t|a|a|c|t|g|a|g|c|t|c|c|t|g|g|g|a|c|g|t|t|a|g|g|g|c|t|g|g|ei
t|c|c|c|t|c|c|t|g|a|t|c|c|c|a|t|c|c|c|t|c|c|t|t|c|c|a|g|g|g|a|g|t|g|g|a|g|g|a|t|g|c|c|t|t|c|t|a|c|a|c|g|t|t|g|g|t|g|ei
c|c|t|g|c|c|c|c|c|g|g|c|c|c|c|c|t|t|c|t|c|t|t|c|g|c|a|g|a|c|a|a|a|c|t|g|g|t|c|a|a|g|t|g|t|g|a|g|g|g|c|a|t|c|a|g|c|c|ei
t|g|c|a|t|g|t|a|t|c|t|g|c|c|t|a|c|c|t|c|t|t|c|c|g|c|a|g|c|t|c|t|t|g|g|g|c|a|a|t|g|t|g|c|t|g|g|t|g|t|g|t|g|t|g|c|t|g|ei
a|c|c|t|g|a|c|c|t|g|t|g|a|a|c|a|t|a|g|c|c|t|t|t|t|t|c|t|t|a|t|g|c|c|a|t|g|a|g|g|a|c|t|a|g|a|t|a|a|t|g|a|a|t|c|c|t|c|ei
a|g|c|t|g|g|c|t|g|c|t|t|a|g|a|g|a|c|t|g|c|g|a|a|g|g|a|g|g|t|g|c|g|t|c|c|t|g|c|t|g|c|c|t|g|c|c|c|c|g|g|c|a|c|t|c|t|g|ei
t|c|t|c|c|t|c|t|g|g|a|t|c|g|c|a|g|t|c|a|t|c|c|g|g|a|t|g|g|t|a|a|g|a|c|c|c|t|c|c|t|c|c|t|c|t|g|c|a|g|g|c|c|t|g|g|g|c|ei
a|t|c|g|t|g|g|a|g|a|t|g|c|a|g|c|t|g|a|g|g|c|a|c|c|a|a|g|g|t|g|g|g|g|a|c|t|g|t|a|c|g|t|g|g|a|c|g|g|c|c|t|c|c|c|c|t|c|ei
t|g|c|a|g|c|g|a|c|c|t|c|c|t|g|t|t|t|t|c|t|c|c|t|g|c|a|g|a|a|g|g|a|a|g|c|c|a|t|c|t|c|c|c|c|t|c|c|a|g|a|t|g|c|g|g|c|c|ie
a|c|a|g|c|t|g|c|a|t|t|c|t|c|a|t|g|c|t|t|c|c|t|c|g|c|a|g|t|t|c|t|t|c|c|c|c|a|a|t|c|c|a|g|g|t|c|t|c|c|g|g|a|g|g|c|t|g|ie
c|t|c|t|g|c|c|t|g|t|g|c|a|c|g|g|c|c|a|g|c|t|g|a|c|t|a|c|t|c|a|g|g|c|c|c|c|a|a|g|g|g|g|t|t|t|c|t|g|t|t|t|c|t|a|t|t|c|ei
t|c|t|a|c|c|g|t|c|c|c|t|t|t|c|c|c|a|c|a|c|a|c|c|g|c|a|g|a|a|g|g|t|g|g|t|g|t|t|g|t|c|t|t|c|t|g|g|g|t|c|g|g|g|g|c|c|a|ei
t|a|g|g|c|t|c|c|a|g|c|a|g|g|c|t|g|g|c|t|c|a|g|c|t|c|a|t|t|c|c|a|t|g|g|t|c|c|t|c|t|g|t|t|g|g|t|t|c|c|t|a|g|t|a|g|c|a|ei
t|g|t|t|t|t|t|a|t|t|c|c|c|c|a|c|t|a|c|t|c|t|t|t|t|c|t|a|t|c|a|g|a|t|a|c|c|a|t|t|t|a|t|g|a|g|a|c|a|t|t|c|t|t|g|c|t|a|ei
a|g|g|t|c|g|g|c|g|a|g|a|a|t|c|c|t|g|a|c|t|c|t|c|c|c|c|t|c|c|t|c|c|c|c|a|a|c|t|c|c|a|t|t|t|c|c|t|t|t|g|c|t|t|c|c|t|c|ei
g|c|a|c|a|g|c|c|a|a|t|g|c|c|c|g|t|c|c|t|t|c|c|c|g|c|a|g|a|a|c|c|t|a|g|a|g|c|t|g|c|t|c|c|g|c|a|t|c|t|c|c|c|t|g|c|t|g|ei
g|t|c|t|g|c|c|a|g|a|g|c|c|c|c|t|c|a|c|c|c|t|g|g|t|g|g|g|g|t|a|a|g|g|a|g|g|g|a|g|a|t|g|g|g|g|g|t|g|t|c|a|t|g|t|c|c|c|ei
t|a|c|a|a|c|c|t|a|g|c|a|g|a|c|g|g|a|a|c|t|g|a|c|c|a|g|g|g|t|a|a|g|a|a|t|t|t|t|t|t|t|t|t|t|t|a|t|g|a|g|c|a|a|t|g|c|a|ei
t|g|t|t|a|a|t|c|c|t|a|t|t|t|t|a|t|t|g|a|a|a|a|g|a|c|t|a|a|g|a|c|t|c|a|g|a|g|a|g|a|t|a|a|a|g|c|t|g|t|t|g|c|c|c|a|a|t|ei
t|c|a|t|c|t|a|a|a|t|c|a|t|a|g|g|c|a|a|g|c|t|c|g|c|a|t|a|g|g|c|a|g|g|g|t|a|t|a|t|t|t|t|c|a|g|a|g|a|g|g|a|c|t|g|g|t|t|ei
a|t|t|g|t|t|t|a|a|t|a|g|a|a|g|c|a|g|t|t|c|t|t|a|t|t|g|c|a|a|a|g|g|t|t|c|t|t|t|g|c|a|g|t|a|g|a|a|t|t|t|t|c|t|c|a|g|c|ei
c|c|c|t|a|t|t|t|g|t|g|c|a|g|t|t|t|c|c|a|g|t|t|g|g|a|t|t|t|c|a|a|t|c|a|c|t|t|t|g|a|g|a|c|c|a|a|a|t|g|t|a|c|a|a|a|a|g|ei
c|c|a|t|a|t|a|t|g|g|a|c|g|t|t|c|c|c|a|a|a|a|t|c|g|t|c|c|a|g|c|c|c|a|t|c|g|g|c|c|c|a|c|a|a|a|c|c|c|c|a|a|a|a|g|c|g|t|ei
t|c|c|a|g|g|a|g|a|t|c|c|g|c|a|t|g|t|t|g|a|a|g|a|g|t|c|g|t|g|t|c|g|g|t|c|c|a|t|c|c|g|g|g|a|g|a|t|g|t|g|c|t|c|a|t|c|a|ei
t|c|t|a|g|a|a|t|c|c|t|g|c|t|t|t|t|a|t|c|c|c|a|c|t|c|t|t|t|g|c|t|t|t|c|t|a|t|g|t|t|g|c|t|c|a|g|t|c|g|c|c|c|t|a|t|g|t|ei
g|g|c|c|t|g|t|a|a|g|t|g|g|a|a|g|g|a|a|g|c|c|t|g|c|c|c|c|a|t|c|c|t|g|t|c|t|g|c|g|g|g|a|c|a|g|c|a|g|g|g|g|a|g|g|c|t|g|ei
c|c|t|c|a|a|t|g|a|a|a|a|a|t|c|t|a|t|t|a|c|a|a|a|t|g|a|g|g|a|t|t|a|t|t|t|t|c|g|t|t|a|a|a|c|t|t|a|t|t|a|t|t|a|a|c|a|a|ei
c|a|g|c|t|g|c|a|g|a|a|a|g|a|c|c|a|t|g|a|g|g|a|t|c|t|t|g|g|c|c|t|c|c|c|t|g|g|c|t|a|g|g|g|c|t|c|a|a|g|c|a|g|a|c|t|t|t|ei
c|c|c|t|g|g|a|c|c|c|g|t|c|t|g|t|g|a|c|c|c|a|t|t|a|t|g|g|g|t|a|a|t|g|a|c|c|c|c|c|t|t|c|c|t|g|c|c|c|t|g|g|c|a|t|c|c|t|ei
c|c|g|c|c|g|c|c|t|g|c|t|g|g|a|g|g|g|c|g|a|g|g|c|c|c|c|a|g|t|g|a|g|t|c|t|t|g|g|c|c|c|t|c|c|c|c|t|t|a|g|t|c|c|g|c|c|c|ei
t|t|c|t|a|c|t|t|c|a|g|g|c|a|g|t|g|t|c|g|t|g|g|c|t|c|a|g|g|t|g|a|g|t|g|a|g|t|c|a|a|g|g|c|a|g|t|g|g|g|g|a|g|g|t|a|g|c|ei
c|a|t|a|t|g|t|a|t|c|t|t|t|t|t|a|c|c|t|t|t|t|c|c|a|c|a|g|c|t|c|c|t|g|g|g|c|a|a|c|g|t|g|c|t|g|g|t|g|t|g|t|g|t|g|c|t|g|ei
a|a|c|t|c|c|a|c|a|c|a|g|c|a|g|c|c|a|c|a|t|g|a|a|g|g|g|t|t|g|t|t|t|a|c|t|t|c|t|t|t|t|t|t|t|t|t|t|g|t|t|t|c|t|t|a|g|a|ei
t|t|c|a|g|g|c|c|g|a|t|a|t|t|c|c|t|t|g|t|c|g|t|t|a|c|t|c|t|t|t|g|t|c|a|g|a|g|g|a|a|a|g|a|a|t|g|c|t|g|a|g|t|t|t|t|t|c|ei
a|a|g|g|t|c|c|c|g|g|a|g|a|g|c|t|g|a|g|c|a|g|t|a|g|a|t|g|g|t|g|g|g|g|c|c|c|a|g|g|t|c|t|t|g|g|g|a|g|a|c|g|g|g|c|a|g|g|ei
c|c|c|c|c|a|t|t|c|t|c|g|c|c|t|c|t|c|t|c|a|c|c|c|t|c|a|g|a|c|c|c|g|t|c|c|a|a|g|a|a|g|c|a|g|g|g|a|c|c|a|t|g|g|c|t|g|g|ei
a|a|a|c|g|c|t|a|a|t|t|t|t|a|a|c|a|c|t|t|a|t|t|t|t|t|a|g|t|t|t|c|c|c|a|g|a|a|g|a|g|g|t|c|g|c|c|a|t|t|g|t|t|g|a|a|g|a|ei
t|t|g|g|a|a|a|a|a|c|t|a|a|a|g|a|t|c|t|t|t|c|t|a|a|a|t|a|g|t|a|a|t|g|a|a|a|t|g|t|c|t|a|t|g|a|t|t|g|a|a|a|g|c|t|t|a|a|ei
c|t|g|c|t|c|a|c|c|g|a|c|g|a|a|c|g|a|c|a|t|t|t|c|a|c|a|g|g|a|g|c|c|g|a|c|c|t|g|c|c|t|a|c|a|g|a|c|c|c|g|c|c|t|g|g|a|g|ei
a|c|c|a|c|c|c|c|g|t|c|t|c|t|g|a|c|c|a|t|g|a|g|c|a|c|c|c|t|g|a|g|g|t|g|c|t|g|g|g|c|c|c|t|g|g|g|c|t|t|c|t|a|c|c|c|t|g|ei
a|g|g|t|t|t|t|a|c|g|a|t|t|a|t|g|t|a|t|g|a|t|t|c|g|c|a|g|g|t|a|g|c|g|c|t|g|g|t|a|t|a|t|g|g|t|c|a|a|a|t|g|a|a|t|g|a|a|ei
a|a|t|g|t|a|c|a|g|a|g|c|t|a|a|a|t|a|g|t|a|a|g|g|c|t|a|a|c|t|c|a|t|c|t|t|t|c|c|t|c|c|c|t|t|c|t|a|t|c|c|t|t|c|t|c|a|a|ei
a|a|c|a|g|g|t|c|t|c|a|a|a|c|t|t|a|a|t|t|a|t|g|a|a|g|a|a|t|a|t|t|c|t|g|g|a|g|a|g|c|t|t|c|c|t|t|t|t|a|c|c|c|a|g|t|c|c|ei
a|g|t|c|t|t|g|c|t|g|t|c|c|t|g|g|c|a|c|t|g|c|t|t|a|g|g|g|c|t|t|t|a|t|a|c|t|t|a|t|t|t|g|c|t|c|a|c|t|t|a|g|t|c|c|t|c|a|ei
g|c|c|c|a|t|g|t|t|c|t|a|c|c|a|c|c|t|t|g|g|c|c|c|t|c|a|g|g|t|g|a|g|t|g|g|a|g|g|g|c|g|g|g|c|a|c|c|c|c|c|a|t|t|c|c|a|t|ei
a|t|g|a|g|a|g|a|c|a|g|g|c|a|t|t|t|g|g|a|c|c|a|a|t|a|t|g|a|t|g|t|g|t|t|c|c|a|t|g|t|a|t|g|g|c|a|t|a|t|g|c|a|a|a|g|t|g|ei
g|g|c|c|t|c|a|c|a|c|a|g|c|c|c|t|c|c|g|g|t|g|t|c|a|c|a|g|a|t|t|c|c|a|a|c|c|c|g|a|g|a|g|g|g|g|t|g|a|g|c|g|c|c|t|a|c|c|ei
c|c|g|t|c|c|c|t|a|t|t|c|t|g|g|c|c|a|c|t|t|g|a|t|g|g|g|g|g|a|c|a|c|c|t|g|g|t|a|g|g|g|g|a|t|g|g|g|g|a|a|a|g|g|t|g|g|g|ei
a|c|t|g|g|c|c|t|c|g|t|g|g|t|g|t|a|t|g|a|c|t|a|c|g|c|a|g|g|t|g|g|g|t|a|t|g|c|c|a|g|a|c|c|t|c|c|t|g|a|c|c|t|g|g|a|c|c|ei
a|a|a|g|c|t|c|a|c|a|t|t|t|c|c|a|g|a|a|a|c|a|t|c|a|t|t|t|c|t|g|c|c|a|g|c|a|c|c|t|a|g|a|a|g|c|c|a|a|t|a|t|t|t|t|g|c|c|ei
a|a|a|g|a|g|g|t|c|a|t|a|t|t|a|a|t|g|g|g|a|t|g|a|a|c|c|c|a|a|g|t|g|a|g|t|t|a|t|t|a|t|a|t|g|a|c|c|g|a|g|a|a|a|g|t|c|t|ei
c|c|g|a|c|t|g|a|g|c|a|a|a|g|g|c|c|t|g|g|g|g|t|c|g|g|a|g|t|g|c|t|a|c|c|a|t|g|g|t|a|a|t|g|g|a|c|a|g|a|g|t|t|a|t|c|g|a|ei
a|t|t|c|a|t|t|a|c|t|c|a|g|t|t|g|g|t|g|c|t|g|g|a|c|a|c|t|g|a|c|c|a|a|g|g|a|g|a|a|g|t|c|c|c|c|a|a|t|g|g|c|t|a|c|a|a|t|ei
a|g|g|c|t|g|a|g|t|g|t|g|c|g|a|t|g|g|a|c|c|c|t|t|a|c|a|g|a|a|a|c|c|a|g|c|c|c|t|g|a|g|c|a|a|a|g|g|g|g|t|t|c|t|g|a|g|g|ei
t|g|c|t|t|c|t|g|c|t|a|t|a|t|t|t|g|t|g|a|t|a|t|g|a|a|t|t|a|a|g|a|g|g|a|t|a|c|a|c|a|c|g|t|t|t|g|t|t|t|c|t|t|c|g|t|g|c|ei
c|t|g|t|c|c|t|g|a|a|c|t|c|g|a|t|g|a|a|t|c|a|g|t|g|g|t|c|a|g|g|c|g|t|g|c|t|t|a|a|c|g|g|t|t|c|t|c|t|c|c|g|c|t|t|t|t|g|ei
t|c|c|t|c|a|t|t|c|c|t|g|c|g|t|c|t|g|c|t|t|c|c|c|c|c|a|g|c|a|a|a|a|g|c|g|t|g|a|t|c|t|t|g|c|t|g|g|g|t|c|g|g|c|a|c|a|g|ei
g|t|t|c|a|c|g|t|t|t|g|a|a|a|c|a|c|t|c|t|t|t|t|g|a|g|g|a|t|c|t|a|c|a|a|g|t|g|g|a|t|a|t|t|t|g|g|a|c|c|a|c|t|c|t|g|t|g|ei
g|a|a|g|a|a|g|a|g|a|c|g|g|t|t|g|a|g|t|t|t|a|a|c|a|a|t|c|c|a|t|c|a|c|t|g|a|t|g|a|t|g|a|c|c|t|g|g|a|g|g|c|c|a|t|c|g|c|ei
c|t|g|a|t|c|a|a|t|a|c|t|g|g|g|c|a|a|g|c|t|g|a|g|c|a|c|t|c|c|t|g|g|c|c|t|t|g|a|t|t|t|g|a|a|t|g|t|g|g|c|t|g|a|a|g|c|c|ei
g|c|c|a|t|c|g|a|c|a|g|t|t|t|t|c|t|c|a|g|a|a|t|c|t|t|t|g|g|t|a|a|g|t|g|g|g|g|c|t|g|g|g|g|t|g|g|g|c|g|t|t|a|t|t|t|c|a|ei
g|g|c|a|g|g|g|t|c|t|c|c|c|t|a|c|c|t|g|c|c|t|g|c|t|c|a|g|g|t|a|c|a|t|c|c|c|c|g|a|g|g|g|c|c|t|g|c|a|g|t|g|c|t|c|g|t|g|ei
g|t|g|g|g|c|c|t|c|c|t|a|t|t|c|c|c|t|g|g|a|g|t|c|g|g|a|a|g|g|t|a|a|g|a|g|g|g|c|t|g|g|g|g|t|g|g|c|c|g|g|a|g|g|a|a|g|g|ei
g|g|c|a|g|g|a|g|c|c|c|c|a|g|g|g|g|a|g|g|a|g|g|c|t|c|c|a|a|g|g|c|c|c|a|a|c|a|a|a|g|g|c|a|g|a|c|a|c|a|g|a|g|a|a|a|t|g|ei
t|c|a|a|t|t|c|t|a|t|t|c|c|a|t|t|c|g|a|t|t|t|a|t|c|g|a|t|t|c|t|a|t|t|c|a|c|t|t|c|c|a|t|t|c|c|a|t|t|c|g|a|t|t|c|c|a|g|ei
a|a|c|t|g|a|a|a|g|t|a|c|t|c|c|c|t|c|c|t|t|t|t|t|g|c|a|g|g|a|c|g|a|c|a|a|c|t|t|a|a|t|g|c|c|t|g|c|c|t|a|t|t|a|c|a|a|a|ie
t|g|a|c|c|t|g|a|t|c|t|t|t|g|c|t|c|t|c|c|c|c|c|g|c|c|a|g|t|t|g|a|g|g|a|g|g|a|g|a|a|c|c|c|g|g|a|c|t|t|c|t|g|g|a|a|c|c|ie
t|c|c|t|g|a|c|t|g|t|g|g|a|c|t|g|t|c|c|c|t|g|g|t|g|c|a|g|g|a|g|a|t|g|a|a|t|g|c|c|c|t|g|a|g|a|g|g|c|c|a|g|g|t|g|g|g|t|ei
t|c|t|g|c|t|c|a|c|g|c|t|c|c|c|c|g|c|c|g|c|g|g|c|c|c|a|g|g|t|a|t|g|g|a|g|t|c|g|g|c|g|g|g|c|a|t|t|c|a|c|g|a|g|a|c|c|a|ei
a|t|g|c|c|t|c|c|c|a|a|a|g|t|g|c|a|g|g|g|a|t|t|c|g|g|t|g|t|a|a|g|c|c|t|a|c|c|a|c|a|c|c|c|a|g|c|c|a|a|a|a|t|c|c|t|a|t|ei
c|c|t|g|a|g|c|a|c|a|g|a|c|g|g|c|t|g|t|t|c|t|c|t|c|a|a|g|g|t|t|a|c|a|a|g|c|c|t|g|a|t|g|a|a|g|g|g|a|a|a|c|g|a|g|g|g|g|ei
a|t|t|g|c|t|g|g|a|c|a|g|g|g|a|g|t|t|g|c|t|t|g|a|c|a|a|a|a|t|g|c|c|a|g|t|a|t|g|t|g|a|a|g|a|a|a|t|t|t|t|t|t|g|c|c|c|a|ei
a|t|t|g|t|t|g|a|a|t|a|t|g|a|a|g|c|a|t|t|c|c|c|a|a|c|c|t|g|a|a|c|a|c|c|a|g|c|a|g|t|g|g|a|t|c|t|a|t|a|t|g|a|a|c|a|g|a|ei
t|c|a|t|a|a|g|a|g|g|a|a|c|c|a|a|g|a|c|a|t|a|a|c|t|c|c|c|t|c|g|g|c|c|c|t|t|g|t|g|a|t|g|t|g|g|a|g|a|t|t|g|t|g|t|g|a|t|ei
g|c|g|t|c|c|g|a|c|t|g|c|g|g|g|g|c|a|g|t|g|a|a|c|c|t|g|c|c|t|g|c|a|g|a|c|c|g|t|t|t|g|g|a|a|c|a|a|g|c|c|a|a|c|a|g|t|g|ei
t|t|t|t|g|c|g|t|t|t|t|c|t|c|c|c|a|t|t|c|t|c|g|t|c|c|t|c|t|t|t|t|g|t|c|g|c|c|g|t|t|t|c|c|c|g|c|c|c|g|c|c|a|c|t|c|c|c|ei
t|t|a|c|c|a|a|c|t|a|t|t|t|t|t|g|t|c|a|t|a|t|t|t|c|a|a|a|g|a|a|g|g|a|a|a|a|a|a|t|g|t|t|t|c|t|g|c|a|t|g|t|g|a|a|a|g|g|ei
a|a|g|t|a|g|t|a|a|a|a|t|a|t|t|t|t|t|t|t|c|c|c|c|c|t|a|g|c|t|t|t|a|c|a|a|t|a|a|t|t|t|t|c|c|c|a|g|c|t|t|t|c|t|a|c|a|c|ei
a|c|t|g|g|c|g|g|a|a|t|g|a|a|t|t|t|g|a|c|t|g|g|a|a|a|g|c|a|g|g|t|g|g|a|g|a|t|t|c|t|c|a|a|c|a|g|a|t|a|c|c|c|t|c|a|c|t|ei
c|t|c|t|a|g|g|a|t|g|t|c|c|t|t|g|g|c|a|a|g|g|g|a|c|t|g|c|a|g|a|g|a|a|a|a|c|a|t|a|c|c|t|t|g|g|g|c|g|g|c|a|a|a|g|t|a|a|ei
g|c|t|c|t|a|a|t|g|t|g|t|c|t|c|t|c|a|c|g|g|c|t|g|a|a|a|t|g|t|g|a|c|a|c|c|c|c|g|g|g|g|g|g|c|c|t|g|a|t|g|t|g|t|g|t|g|g|ei
g|a|a|t|g|g|t|g|t|t|g|t|a|t|g|c|c|t|t|t|a|a|a|c|g|t|g|a|t|g|a|t|c|c|t|c|a|t|a|t|g|g|c|c|c|a|g|t|g|t|c|a|a|g|t|t|g|t|ei
g|c|t|g|g|a|g|g|a|t|g|t|g|g|c|t|g|c|a|g|a|g|c|t|c|t|g|c|t|c|t|t|g|g|g|c|a|c|t|g|t|g|g|c|c|t|g|c|a|g|c|a|t|c|t|c|t|g|ei
a|t|g|t|c|a|a|t|g|t|g|a|a|a|g|g|t|a|t|g|g|t|a|g|t|g|g|g|g|a|g|g|a|g|a|t|g|c|a|g|c|a|a|g|g|t|g|g|g|g|a|a|t|t|a|a|g|g|ei
g|c|a|a|g|a|a|g|a|g|c|c|t|g|g|a|g|a|c|t|g|a|a|a|a|a|g|g|c|c|t|t|g|a|c|c|a|g|t|g|a|g|a|t|t|g|c|a|c|t|g|c|t|g|c|a|g|t|ei
t|c|c|t|t|t|a|c|a|g|a|c|a|g|c|t|a|g|t|g|t|g|g|g|c|c|a|c|t|c|a|g|t|t|t|t|a|g|c|a|t|c|t|c|t|g|c|t|c|t|a|t|t|t|g|g|c|c|ei
t|c|t|t|t|g|g|a|g|g|a|a|c|a|g|c|t|c|c|c|t|a|g|g|c|t|t|c|c|t|c|c|g|t|c|t|g|c|a|a|t|g|t|c|c|c|t|t|g|c|a|c|a|g|c|c|c|a|ei
c|c|t|g|t|g|g|g|t|g|a|a|g|a|g|a|g|a|g|g|g|a|a|c|c|a|g|c|a|g|c|a|t|c|t|c|t|c|c|a|c|t|g|a|a|a|g|a|a|g|t|g|g|g|a|c|t|t|ei
c|a|g|a|a|g|c|g|g|c|a|a|a|a|g|c|a|g|g|t|a|c|c|g|t|c|a|c|g|c|c|c|g|a|g|a|c|t|t|t|c|a|c|a|t|c|a|a|c|c|t|c|t|t|t|c|a|a|ei
g|a|t|c|t|a|c|t|g|t|c|t|a|a|t|a|t|c|t|t|a|a|g|g|t|t|a|g|t|a|t|t|t|t|t|c|t|c|a|g|t|g|a|c|t|t|t|g|t|g|g|g|t|t|c|t|t|t|ei
a|a|t|a|t|c|t|t|t|c|g|t|t|g|g|c|t|t|c|c|a|g|g|t|c|a|g|a|a|a|a|a|t|a|a|t|t|t|g|t|a|a|c|a|a|a|g|t|t|t|a|a|a|g|g|t|c|a|ei
t|a|g|a|g|c|t|a|a|g|t|g|c|c|a|a|a|t|g|c|t|t|c|t|c|c|a|g|g|g|g|a|g|a|t|c|a|t|c|g|g|a|g|g|c|c|g|g|g|a|g|a|g|c|a|g|g|c|ei
t|t|t|t|t|t|c|c|t|g|a|g|c|t|t|g|g|c|c|a|g|a|a|g|g|g|c|c|a|t|g|a|g|g|c|c|t|c|a|g|t|g|g|a|c|t|t|t|c|c|a|c|c|c|c|c|t|c|ei
g|a|g|a|a|a|c|t|c|a|a|c|a|a|t|g|c|a|a|a|a|t|a|g|c|a|t|c|t|c|t|a|t|g|g|c|c|c|g|a|a|a|a|a|t|t|g|g|a|g|c|a|a|g|a|g|t|g|ei
c|c|a|g|a|a|a|t|c|t|g|a|a|c|t|c|a|c|c|c|a|g|c|a|t|c|a|a|g|t|a|a|g|a|g|g|g|a|c|t|a|c|a|g|t|g|t|g|t|g|g|t|g|g|t|g|a|c|ei
a|c|c|c|c|c|a|t|c|c|t|c|a|c|t|c|t|g|c|t|c|t|c|c|g|c|a|g|c|t|c|c|a|t|a|a|a|t|g|t|c|a|c|c|t|t|g|g|g|g|g|c|c|c|a|c|a|a|ei
t|c|t|g|a|g|a|a|a|g|t|t|c|t|t|c|a|t|g|a|t|g|a|t|c|a|t|t|t|a|a|c|t|c|g|c|a|g|a|g|a|t|g|a|a|c|c|t|g|c|c|t|t|t|g|a|g|a|ei
t|a|c|a|t|c|t|a|c|a|a|c|c|g|g|g|a|g|g|a|g|c|t|g|g|c|g|c|t|t|c|g|a|c|a|g|c|g|a|c|g|t|g|g|g|g|g|a|g|t|t|c|c|g|g|g|c|g|ei
a|g|g|g|c|c|a|t|g|t|c|c|g|a|c|c|t|g|g|a|g|c|t|a|a|c|a|g|g|t|a|c|t|t|c|c|c|a|c|t|g|t|g|g|g|c|c|a|t|c|t|c|a|g|g|g|c|a|ei
c|t|g|c|a|t|c|t|t|t|c|t|g|a|c|t|t|t|t|g|t|t|t|a|a|c|a|g|t|t|g|a|a|t|a|t|c|c|a|t|g|t|g|g|a|a|a|a|a|t|a|c|c|t|a|t|t|c|ei
c|g|a|a|t|g|g|t|a|t|c|t|g|g|g|c|a|g|a|a|a|g|a|c|a|t|a|t|a|c|c|t|a|t|a|a|c|g|a|c|a|c|t|g|t|g|a|t|a|t|t|t|g|c|t|t|g|c|ei
g|c|t|c|t|g|a|t|g|a|g|t|c|t|c|t|c|a|t|c|g|c|t|g|a|a|a|g|g|t|c|a|g|a|t|t|c|t|g|g|g|a|g|c|t|g|a|a|g|t|g|g|t|c|g|g|g|g|ei
t|g|c|g|c|g|g|c|t|a|c|t|a|c|a|a|c|c|a|g|a|g|c|a|g|c|c|a|g|t|g|a|g|t|a|a|c|t|c|c|g|g|c|c|c|a|g|g|g|a|g|c|a|g|a|t|c|a|ei
g|g|t|t|a|a|c|a|t|t|c|c|t|c|a|a|g|g|c|a|g|c|t|g|c|a|a|g|g|t|g|a|g|g|t|c|c|a|c|a|g|g|a|t|a|g|g|g|g|g|c|a|g|g|a|g|g|c|ei
a|g|g|c|t|g|c|g|g|c|a|g|g|a|a|a|a|c|a|t|g|c|a|t|c|g|a|g|g|t|a|a|g|c|g|g|g|c|c|a|g|g|g|a|g|t|g|g|g|g|a|g|g|a|a|c|c|a|ei
a|g|g|c|t|g|a|c|c|t|g|a|t|c|t|c|t|a|c|t|c|t|c|c|c|t|g|g|c|c|a|g|c|t|g|a|g|g|a|g|g|a|g|a|a|c|c|c|g|g|c|c|t|t|c|t|g|g|ei
g|t|c|t|g|a|t|c|c|c|c|c|t|g|a|c|c|c|a|g|c|a|c|c|c|t|c|c|g|c|a|g|g|t|g|c|c|g|t|g|c|c|c|c|t|c|a|t|c|c|a|g|t|c|t|c|g|g|ei
c|c|a|t|c|t|a|c|a|g|g|c|t|c|c|a|c|c|t|t|g|g|g|t|c|a|a|g|g|t|g|a|g|a|g|g|c|t|g|a|t|c|t|c|g|c|t|c|t|g|g|c|c|c|t|c|a|c|ei
a|a|a|c|t|a|c|c|c|c|t|a|a|a|a|g|c|c|a|a|a|a|t|g|a|a|a|g|g|a|a|a|a|g|a|c|t|c|a|t|a|t|c|a|a|c|a|t|t|g|t|c|g|t|c|a|t|t|ei
t|a|a|t|c|g|t|t|g|a|t|t|c|c|c|t|t|c|c|c|t|c|c|t|a|c|a|g|a|a|a|g|c|a|t|c|c|c|t|g|g|a|g|a|a|c|a|g|c|c|t|g|g|a|g|g|a|g|ei
g|g|g|a|a|g|g|g|t|c|t|c|t|g|g|g|t|c|t|t|t|g|t|g|t|g|g|t|g|t|g|c|c|a|c|g|t|g|g|g|a|t|g|g|g|a|a|g|g|c|c|g|g|g|g|c|t|c|ei
c|a|t|t|g|c|c|t|g|t|a|t|t|c|a|g|t|g|g|a|g|c|c|g|a|g|c|a|a|t|g|a|g|g|a|a|g|a|g|g|g|a|g|t|c|c|a|a|c|a|t|g|t|c|a|a|t|a|ei
c|a|c|t|g|g|t|t|a|t|c|a|c|c|c|t|t|t|a|c|t|g|c|a|c|a|c|a|g|t|a|a|g|t|c|c|c|g|a|g|g|a|a|t|c|g|c|g|g|c|g|g|g|a|a|g|g|a|ei
t|t|g|c|t|c|a|g|c|c|t|c|g|c|t|g|c|t|t|g|c|c|t|c|g|c|a|g|a|c|g|c|c|g|c|c|a|g|g|c|c|g|a|g|c|c|a|g|t|t|c|c|g|g|g|t|g|t|ei
t|c|g|g|c|c|c|c|a|c|t|g|a|c|c|c|t|c|t|t|c|t|c|g|a|c|a|g|c|t|c|c|t|g|a|g|c|c|a|c|t|g|c|c|t|g|c|t|g|g|t|g|a|c|t|c|t|g|ei
c|c|a|g|t|a|g|t|c|t|t|t|c|a|g|g|g|a|a|c|t|g|a|g|c|a|t|c|g|g|t|c|a|c|c|c|a|g|c|c|c|c|t|a|a|a|t|c|a|g|t|c|a|g|g|g|g|a|ei
c|c|t|c|c|c|c|a|c|c|t|c|c|c|a|c|t|c|t|a|g|g|t|c|a|g|t|c|a|a|a|t|g|g|a|a|a|t|a|t|g|t|g|g|c|t|t|t|t|c|t|c|a|c|t|c|c|a|ei
a|a|t|g|g|a|t|a|g|a|c|c|a|g|c|a|c|t|c|a|g|a|c|a|t|a|t|t|t|t|c|a|g|t|a|t|c|t|g|t|t|t|t|t|c|t|t|a|a|c|t|c|a|g|g|g|c|c|ei
t|c|c|t|c|a|t|g|c|a|t|c|c|a|c|c|c|c|c|t|t|c|c|c|c|c|a|g|g|a|a|t|a|g|c|c|a|g|g|t|c|t|g|g|c|t|g|g|g|t|c|g|g|c|a|c|a|a|ei
c|t|t|g|a|a|t|g|t|a|t|c|t|t|t|g|t|a|t|a|c|t|t|t|a|a|g|t|g|t|t|t|t|t|g|t|a|g|c|a|a|t|t|g|a|t|t|c|c|c|a|g|a|a|g|t|g|g|ei
g|g|a|g|c|a|g|g|g|c|a|g|a|g|t|g|a|g|c|a|g|g|a|g|a|a|t|g|a|t|g|c|t|g|g|g|g|a|a|t|t|t|g|t|g|t|g|c|t|c|c|t|t|g|g|g|t|g|ei
a|g|g|c|c|t|g|g|g|g|c|g|g|g|a|a|g|a|a|g|g|a|g|a|c|t|g|a|a|g|g|c|t|g|c|g|c|a|g|g|a|g|g|a|g|t|a|t|g|t|c|a|a|g|c|g|a|g|ei
a|c|c|g|a|c|t|g|c|c|t|g|c|t|c|g|t|g|g|a|a|a|t|g|g|a|a|g|g|t|a|g|g|c|t|c|g|g|c|c|t|c|c|c|a|t|g|a|t|g|t|g|g|g|c|t|c|t|ei
c|a|t|t|c|t|c|a|c|a|t|c|t|g|t|t|c|t|c|t|a|a|c|t|a|a|c|t|g|a|a|g|t|t|t|t|c|t|a|a|t|t|c|t|c|t|c|c|a|g|c|t|t|g|a|a|a|g|ei
c|g|c|t|g|a|t|a|c|c|t|a|t|g|c|c|a|g|c|a|c|c|a|a|g|g|c|a|c|t|a|t|g|a|t|a|t|t|a|a|t|g|c|a|c|a|c|g|c|c|t|g|t|g|t|t|a|c|ei
a|c|t|c|t|g|t|a|t|t|t|t|g|g|c|c|t|g|a|a|a|c|c|a|a|g|t|g|g|t|g|c|t|g|c|a|t|g|g|a|t|a|t|g|a|a|g|c|a|g|t|g|a|a|g|g|a|a|ei
c|t|c|t|a|a|t|c|a|g|c|c|c|t|c|t|g|g|c|c|c|a|g|c|g|t|c|a|g|t|a|a|g|t|g|t|c|t|c|c|a|a|a|c|c|t|c|t|t|t|c|c|t|a|a|t|t|c|ei
t|t|g|t|g|a|a|a|a|g|t|t|g|t|t|a|a|a|a|a|c|a|a|c|a|a|a|t|g|t|g|a|a|c|t|t|a|a|c|c|c|t|c|a|c|t|c|t|a|a|g|c|t|t|t|c|c|c|ei
c|a|a|a|c|g|c|c|a|a|a|c|c|t|g|c|t|a|t|c|t|c|c|t|g|c|a|g|g|g|c|g|a|t|t|c|g|g|g|a|g|g|c|c|c|c|c|t|g|g|t|g|t|g|t|c|t|g|ei
t|c|c|t|c|a|c|t|g|c|c|t|g|t|c|c|c|c|t|t|c|c|c|c|t|c|a|g|a|t|c|a|t|t|g|c|t|c|c|t|c|c|t|g|a|g|c|g|c|a|a|g|t|a|c|t|c|c|ie
a|t|t|g|a|a|a|a|a|t|t|t|g|a|g|a|a|g|g|a|g|g|c|g|t|g|a|g|g|t|a|t|g|t|t|t|a|a|t|a|c|c|a|g|a|a|a|g|g|g|a|a|a|g|a|t|c|a|ei
g|c|g|c|c|c|g|c|c|c|c|t|c|c|g|c|g|c|c|g|c|c|t|c|c|g|c|c|c|g|c|c|c|g|c|c|g|c|g|c|t|c|c|c|g|c|c|c|g|c|c|g|c|t|c|t|c|c|ei
a|a|c|t|c|a|a|a|c|a|g|a|a|g|g|t|g|t|c|t|g|t|t|a|g|a|g|a|g|a|g|t|g|a|t|g|c|c|c|a|t|c|t|g|c|c|t|a|c|c|a|t|c|c|a|a|g|g|ei
g|g|g|c|t|c|t|c|c|t|g|a|c|a|c|a|c|t|c|t|c|c|c|c|g|c|a|g|a|g|g|t|c|c|a|g|g|g|g|a|c|c|c|a|a|c|a|g|c|c|c|c|a|g|c|a|a|g|ie
a|t|t|t|t|t|g|t|a|t|t|t|a|g|t|g|g|c|a|g|g|t|t|c|c|a|t|g|t|t|a|g|t|a|g|g|g|t|g|g|t|c|t|t|c|t|t|g|a|c|c|t|g|a|c|c|t|t|ei
t|c|t|g|t|g|c|c|a|g|c|t|t|c|t|t|a|t|c|c|t|a|t|g|g|g|a|g|a|a|a|g|c|t|c|a|a|a|g|a|t|g|a|a|a|t|g|a|a|t|c|t|c|c|t|t|c|t|ei
t|g|g|g|c|c|g|c|a|c|t|g|a|c|c|c|t|c|t|t|c|t|c|g|a|c|a|g|c|t|c|c|t|a|a|g|c|c|a|c|t|g|c|c|t|g|c|t|g|g|t|g|a|c|c|c|t|g|ei
g|g|a|a|g|a|t|g|c|t|g|g|a|g|g|a|g|a|a|a|c|t|c|g|g|a|a|g|g|t|a|g|g|c|t|c|t|g|g|t|g|a|c|c|a|g|g|a|c|a|a|g|g|g|a|g|g|g|ei
a|g|t|a|c|t|t|c|c|t|c|t|c|t|c|c|g|t|c|t|c|t|t|a|a|t|a|g|a|g|a|c|c|t|a|a|a|c|c|a|g|a|t|g|a|g|a|a|g|t|a|t|t|a|t|t|c|a|ei
t|a|a|a|t|t|c|t|t|c|t|g|t|t|t|g|t|t|a|a|c|a|c|t|t|c|a|g|a|c|t|t|a|t|g|t|g|t|a|t|g|a|a|g|g|a|g|t|a|g|a|a|g|c|c|a|a|a|ei
g|a|a|a|t|g|a|c|t|g|a|t|g|g|a|g|g|t|g|t|g|g|a|t|t|t|c|g|t|t|t|g|a|a|g|t|c|a|t|c|g|g|t|c|g|g|c|t|t|g|a|c|a|c|c|a|t|g|ei
g|t|c|c|t|g|g|c|t|c|c|a|g|c|c|a|c|a|t|t|c|t|a|g|c|a|t|c|t|g|c|c|a|g|c|a|g|g|a|c|a|g|t|t|g|c|c|a|c|c|a|g|g|a|g|c|a|a|ei
g|a|c|c|t|g|c|a|g|c|a|c|c|g|g|c|t|g|g|a|c|g|a|g|c|g|a|g|c|a|g|a|t|c|g|c|c|c|t|c|a|a|g|g|g|c|g|g|c|a|a|g|a|a|g|c|a|g|ei
c|c|t|a|c|t|t|c|g|g|a|g|t|c|t|a|t|g|a|t|a|c|t|c|a|a|g|g|g|t|g|a|g|a|g|a|g|g|g|g|c|a|t|c|g|g|g|g|a|g|a|a|g|g|a|g|g|g|ei
c|t|g|a|c|t|a|a|g|c|c|g|c|c|c|c|t|t|g|t|c|c|c|t|t|c|a|g|a|t|t|a|t|g|t|t|t|g|a|g|a|c|c|t|t|c|a|a|c|a|c|c|c|c|g|g|c|c|ei
c|c|c|c|t|t|a|c|c|t|g|a|c|a|c|a|c|t|c|t|c|c|c|c|g|c|a|g|a|g|g|t|c|c|a|g|g|g|g|a|c|c|c|a|a|c|a|g|c|c|c|c|a|g|c|a|a|g|ei
a|t|c|c|t|t|c|c|t|c|c|a|c|c|t|c|t|g|g|t|t|t|c|t|g|c|a|g|g|a|a|a|t|c|c|a|t|g|c|c|c|g|a|t|t|c|a|g|a|a|g|a|g|g|a|g|c|c|ei
a|a|g|c|a|c|c|c|c|t|a|c|t|a|c|a|a|c|t|c|c|a|t|a|c|a|a|g|g|t|g|g|g|c|t|g|c|c|t|t|t|g|c|t|g|g|g|a|a|g|g|c|c|t|c|t|g|g|ei
g|g|g|c|c|c|t|g|g|c|c|c|t|g|a|c|c|c|a|g|a|c|c|g|g|c|g|c|g|t|g|a|g|t|g|c|a|g|g|g|t|c|t|g|c|a|g|g|g|a|a|a|t|g|g|t|c|g|ei
c|a|t|c|t|c|t|g|t|c|c|t|c|c|a|t|g|a|g|a|t|g|a|c|a|g|c|a|g|a|c|c|t|t|c|a|a|t|c|t|c|t|t|c|a|g|c|a|c|a|a|a|g|g|a|c|t|c|ei
a|g|g|g|t|g|g|t|t|t|t|t|c|t|t|t|t|a|a|c|c|a|g|t|a|g|a|c|g|g|g|c|a|a|a|a|g|c|t|t|g|a|t|t|g|c|c|c|t|t|t|a|a|c|c|g|c|c|ei
t|c|a|g|c|c|a|c|t|t|c|g|t|g|c|c|g|g|t|c|t|t|c|t|c|c|a|g|g|t|c|c|g|c|g|c|g|c|c|g|g|g|t|t|g|c|n|n|c|a|c|c|t|c|t|c|c|g|ei
t|c|a|c|g|c|a|g|c|c|g|c|t|a|g|c|g|c|c|c|a|g|g|g|c|t|c|t|c|g|c|c|t|t|c|t|c|c|t|t|c|a|g|g|t|g|g|c|g|c|a|a|a|a|c|t|t|t|ei
a|c|c|a|a|g|g|a|g|a|t|c|t|a|c|t|c|c|c|a|c|t|t|a|c|t|g|c|g|c|c|a|c|c|g|a|c|a|c|c|a|g|t|a|a|c|a|t|c|c|a|g|t|t|t|g|t|c|ei
g|a|t|c|c|c|c|t|g|a|a|c|c|c|c|t|g|c|c|t|c|t|g|c|c|c|a|g|a|g|t|g|c|c|c|c|t|c|c|g|g|c|c|t|c|g|c|c|a|t|g|a|g|g|c|t|c|t|ei
c|c|a|a|c|a|g|c|a|c|c|a|a|t|a|t|c|t|t|c|t|t|c|c|c|c|a|g|t|g|a|g|c|a|t|c|g|c|t|a|c|a|g|c|c|t|t|t|g|c|a|a|t|g|c|t|c|t|ei
a|a|a|t|t|t|g|g|t|t|t|a|g|a|g|g|g|t|c|a|a|a|a|t|a|g|t|t|g|t|g|t|a|t|t|g|a|t|g|a|a|t|a|g|c|a|c|g|g|t|c|c|t|g|c|t|a|c|ei
g|a|t|c|a|c|a|c|t|a|t|c|t|c|c|a|c|t|t|g|c|c|c|g|c|c|t|g|t|g|g|a|a|g|a|t|t|a|g|c|g|g|c|c|a|t|g|t|a|t|t|c|c|a|a|t|g|t|ei
t|g|c|c|t|c|t|c|c|a|g|g|a|t|g|t|c|t|a|c|a|a|a|t|g|g|t|g|g|t|a|a|g|t|t|g|g|c|t|g|t|a|a|a|c|a|a|a|g|t|t|g|a|a|t|t|t|g|ei
c|a|c|c|c|c|c|g|g|t|a|t|t|a|a|a|a|c|g|a|a|c|g|g|c|g|g|a|a|a|g|a|a|g|c|c|c|t|c|a|g|t|c|g|c|c|g|g|c|c|g|g|g|a|g|g|c|g|ei
c|c|t|t|g|c|t|c|a|g|a|g|c|g|g|a|g|a|a|a|g|c|a|t|g|t|t|t|g|t|a|c|a|a|g|a|t|c|c|g|c|a|g|a|c|g|t|g|t|a|a|a|t|g|t|t|c|c|ei
a|a|a|t|g|t|g|a|a|t|t|t|c|t|g|g|a|t|t|t|t|t|t|t|a|t|a|g|c|a|t|g|t|t|t|g|t|g|t|c|a|t|t|a|g|t|g|a|a|a|c|t|g|g|a|a|a|a|ei
a|a|c|t|g|t|c|a|g|g|g|g|a|a|g|a|c|c|t|a|c|c|t|t|c|a|a|g|g|t|g|c|c|a|g|g|g|g|c|t|g|t|g|g|g|c|c|a|g|g|g|t|a|g|a|a|a|g|ei
g|g|c|t|a|c|a|g|c|t|c|t|c|c|c|t|g|g|g|c|a|t|c|t|c|c|a|g|g|t|a|a|t|g|a|g|g|c|t|c|c|c|c|g|a|g|c|t|g|c|c|c|c|t|a|c|a|c|ei
g|g|c|c|t|c|g|g|c|g|c|c|t|c|g|c|g|g|c|c|g|c|g|g|g|g|c|c|g|t|g|c|g|c|t|c|t|g|c|c|t|a|t|g|g|g|g|g|c|c|c|g|g|t|g|g|g|c|ei
g|t|g|g|c|t|t|t|a|t|t|c|t|c|t|t|t|g|c|t|c|c|a|a|g|g|t|c|c|a|g|a|c|c|t|c|c|c|c|a|g|a|a|t|t|t|a|c|c|c|t|t|c|a|t|t|c|a|ei
g|c|c|a|a|c|t|a|c|a|g|g|a|a|c|g|t|g|a|t|c|c|a|a|c|t|a|c|a|a|c|a|t|g|c|t|t|c|c|t|g|a|t|g|c|c|a|t|g|a|g|c|t|t|t|g|a|a|ei
t|a|t|c|t|t|g|g|c|t|t|a|t|a|g|a|t|g|g|c|c|g|t|t|c|t|t|c|c|c|g|t|g|t|c|t|c|t|a|c|a|c|a|c|c|g|t|c|t|t|c|c|t|t|c|t|g|t|ei
g|t|a|t|t|t|c|a|c|a|t|a|t|t|a|c|a|a|t|t|t|g|t|a|a|t|t|g|t|t|g|g|t|g|t|g|c|a|c|t|t|t|g|t|g|g|g|t|t|c|t|t|c|c|t|g|c|a|ei
c|a|t|g|t|c|c|c|t|a|c|a|a|a|g|g|a|c|a|t|g|a|a|t|a|t|c|c|t|t|t|t|t|t|a|t|g|g|c|t|g|c|a|c|a|g|t|a|t|t|c|c|a|t|g|g|t|g|ei
a|a|g|c|a|a|c|t|t|t|t|a|a|g|t|g|a|g|g|c|t|g|c|a|a|g|c|c|g|c|c|g|g|g|a|t|g|t|a|g|a|t|t|t|t|a|g|t|t|c|g|t|g|g|c|c|a|a|ei
c|c|a|c|c|c|t|c|c|a|g|c|c|c|c|c|a|a|c|t|c|c|t|c|g|c|a|g|a|c|a|a|g|c|t|g|g|t|g|t|c|t|a|a|g|a|a|c|t|a|c|c|c|g|g|a|c|t|ei
t|c|g|g|c|c|c|c|a|c|t|g|a|c|c|c|t|c|t|t|c|t|c|g|a|c|a|g|c|t|c|c|t|a|a|g|c|c|a|c|t|g|c|c|t|g|c|t|g|g|t|g|a|c|c|c|t|g|ei
g|g|a|a|g|a|t|g|t|t|g|g|a|g|g|a|g|a|a|a|c|c|c|g|g|a|a|g|g|t|a|g|g|c|t|c|t|g|g|t|g|a|c|c|a|g|g|a|c|a|a|g|g|g|a|g|g|g|ei
t|t|t|c|c|a|t|t|t|a|a|t|c|c|a|t|t|c|g|a|t|c|t|a|c|a|a|g|g|t|g|a|g|t|c|a|g|t|a|a|a|c|a|a|c|t|a|t|a|t|t|g|t|t|t|t|c|t|ei
t|g|a|t|g|g|g|g|g|c|a|g|g|g|g|a|t|g|g|a|a|c|a|c|c|a|c|a|t|g|g|g|c|a|t|a|a|a|g|g|a|a|t|c|t|c|a|g|a|g|c|c|a|g|a|g|c|a|ei
a|g|c|g|g|g|a|g|a|a|t|g|g|g|a|c|c|g|t|c|t|c|c|g|t|a|c|g|g|t|g|a|g|g|g|c|c|a|g|c|c|c|t|c|a|g|g|c|a|g|g|a|g|g|g|t|t|c|ei
a|t|g|t|g|g|a|g|c|c|a|g|a|a|c|c|a|c|g|g|c|t|t|a|t|g|t|t|a|g|a|c|a|c|t|a|g|g|a|t|g|a|t|g|c|c|c|a|c|t|t|t|g|t|g|c|c|a|ei
t|c|t|c|a|a|t|c|c|t|t|t|c|c|c|t|g|t|a|a|c|t|c|t|c|c|a|g|a|g|t|t|c|c|t|g|g|a|t|g|a|t|g|a|c|a|t|t|a|c|t|g|a|t|g|a|c|a|ei
g|a|c|c|a|a|g|c|c|g|c|a|g|c|t|c|t|g|g|c|c|g|c|g|c|c|c|c|a|c|c|c|c|t|c|c|c|g|g|g|c|c|t|c|g|c|a|a|a|c|g|g|c|c|g|g|t|g|ei
a|c|t|t|t|c|a|c|a|g|t|g|t|a|c|g|a|a|t|a|c|c|a|a|a|c|c|a|g|a|t|a|a|a|c|a|g|t|g|t|a|c|c|a|t|g|t|t|t|t|a|t|a|g|c|a|c|t|ei
t|c|c|a|t|g|t|t|t|g|t|a|a|a|a|c|t|a|c|a|c|a|t|c|t|a|a|t|g|t|g|t|g|c|c|a|t|a|g|a|g|t|t|t|a|a|c|a|c|a|a|g|t|c|c|t|g|t|ei
t|g|c|a|t|c|c|a|a|t|t|t|a|a|c|t|t|a|a|c|t|c|t|a|c|t|a|t|t|t|t|c|t|g|c|a|g|c|t|g|c|t|c|c|c|a|g|a|t|t|a|c|t|c|c|t|t|c|ei
a|g|g|g|g|c|t|g|c|c|g|c|a|g|c|c|g|c|c|g|c|g|a|c|t|c|c|g|g|a|c|a|g|a|c|g|c|c|a|g|a|g|c|g|a|g|g|a|g|g|c|g|c|t|a|c|g|c|ei
t|c|a|a|g|g|t|c|c|t|g|g|g|g|a|a|c|c|c|c|a|a|g|g|g|a|t|g|g|t|g|a|g|g|g|g|c|c|t|a|a|a|g|a|a|c|a|a|c|t|c|c|t|c|a|t|t|g|ei
a|t|t|t|a|t|g|g|t|a|a|a|a|c|a|t|t|a|t|t|c|a|c|a|c|t|t|c|t|g|t|a|t|t|t|c|t|t|t|c|t|a|a|g|g|g|t|g|c|t|c|g|t|g|g|t|t|t|ei
t|a|t|t|a|c|t|g|t|g|c|c|a|c|c|t|g|g|a|a|g|g|a|t|t|t|a|t|a|a|g|a|a|a|c|t|c|t|t|t|g|g|c|a|g|t|g|g|a|a|c|a|a|c|a|c|t|t|ei
g|g|a|c|a|g|c|c|c|c|a|g|a|t|c|t|a|a|g|c|g|g|t|c|g|t|a|a|t|c|t|g|a|g|t|a|c|t|t|g|c|a|t|g|c|t|g|g|g|c|a|c|a|t|a|c|a|c|ei
g|t|t|g|a|a|g|t|a|c|t|a|a|a|g|a|a|c|a|a|c|a|a|t|t|c|c|a|g|t|a|a|g|t|t|t|g|t|t|t|t|c|a|t|a|t|g|t|g|a|t|a|t|g|t|t|c|c|ei
a|a|c|c|a|t|g|a|c|c|a|g|a|a|g|c|t|a|t|g|g|g|t|a|c|c|c|a|t|c|t|g|a|g|t|t|c|c|t|a|c|c|t|g|a|a|c|g|g|t|t|t|c|t|c|a|c|c|ei
a|t|a|t|t|a|c|t|t|g|g|t|a|a|t|a|c|t|a|a|a|g|c|a|g|a|t|g|a|a|t|t|a|t|g|t|g|c|a|t|g|g|a|g|t|c|a|t|t|a|a|t|c|t|t|c|t|g|ei
a|c|c|t|c|t|a|a|a|a|c|t|a|a|c|c|t|g|c|c|t|c|t|a|t|t|c|t|g|a|a|t|c|c|a|g|a|c|a|g|a|a|t|c|a|a|t|c|c|t|c|a|g|c|t|g|t|g|ei
t|t|g|t|a|a|t|c|t|g|a|g|a|a|g|a|g|g|a|g|a|a|g|a|a|g|g|g|a|c|c|t|t|t|c|c|t|g|a|c|a|t|g|a|g|g|g|g|a|g|t|c|c|a|a|t|c|t|ei
t|c|t|c|c|g|t|g|a|t|g|a|a|t|c|g|g|g|c|c|a|a|g|a|g|c|a|g|g|t|g|a|g|c|t|g|g|g|g|c|c|c|g|c|t|g|c|t|g|g|g|t|c|a|c|g|g|c|ei
c|c|c|t|g|g|a|c|c|c|g|t|c|t|g|t|g|a|c|c|c|a|t|t|a|t|g|g|g|t|a|a|t|g|a|c|c|c|c|c|t|t|c|c|t|g|c|c|c|t|g|g|c|a|t|c|c|c|ei
t|t|t|g|t|g|g|a|c|g|a|a|t|a|c|g|a|c|c|c|c|a|c|a|a|g|a|g|g|t|g|a|g|c|c|t|a|g|c|g|c|c|g|c|c|g|t|c|c|a|g|g|t|g|c|c|a|g|ei
c|t|c|c|c|c|a|c|c|c|a|c|c|t|g|t|c|c|a|c|c|c|g|c|g|c|a|g|a|t|c|g|c|t|t|c|c|t|g|g|a|g|c|c|a|g|g|c|a|a|g|a|a|c|t|c|c|a|ie
c|c|g|g|a|g|t|g|g|g|g|a|g|a|t|c|a|g|a|t|g|g|g|c|c|t|g|t|g|t|a|t|c|a|t|g|c|a|a|a|g|g|a|c|t|t|t|g|c|a|t|t|c|t|g|t|t|c|ei
g|g|a|a|g|a|t|g|c|t|g|g|a|g|g|a|g|a|a|a|c|c|c|g|g|a|a|g|g|t|a|g|g|c|t|c|t|g|g|t|g|a|c|c|a|g|g|a|c|a|a|g|g|g|a|g|g|g|ei
a|g|g|g|g|g|a|a|g|c|g|t|g|g|g|t|g|g|g|g|a|a|t|c|a|c|c|t|t|a|a|g|c|t|g|g|t|g|c|c|a|g|c|a|t|a|c|a|c|c|a|t|a|c|t|t|t|a|ei
a|t|t|a|t|a|a|c|t|c|t|g|t|a|t|a|a|t|a|g|a|g|a|a|g|t|c|c|a|t|t|t|t|t|t|a|a|a|a|a|t|g|t|t|t|t|c|c|c|c|a|a|a|c|c|a|t|a|ei
t|g|a|a|g|g|a|g|g|a|c|g|g|t|t|a|a|c|t|t|g|t|a|a|t|c|c|a|c|c|a|t|t|c|a|c|a|t|t|t|g|a|t|g|t|a|c|a|t|g|t|g|t|a|g|g|g|a|ei
a|g|a|a|t|g|t|c|g|t|g|t|g|c|t|g|c|a|g|a|a|g|c|g|g|a|g|c|a|g|a|c|g|c|t|g|t|t|g|g|c|a|t|g|a|g|t|a|c|a|g|t|a|c|c|a|g|a|ei
t|g|t|g|g|t|a|t|c|t|c|t|t|t|c|t|c|a|t|c|t|t|t|c|t|c|a|g|t|g|a|t|c|t|g|t|a|c|c|a|t|g|t|t|t|c|a|c|a|c|c|a|g|t|g|g|t|t|ei
c|c|c|a|g|g|g|a|g|c|a|c|t|a|a|g|c|g|a|g|c|a|c|g|c|c|a|a|c|a|a|c|a|c|c|a|g|c|t|c|c|t|c|t|c|c|c|c|a|g|c|c|a|a|a|g|a|a|ei
a|c|c|g|t|t|c|a|c|t|g|g|c|t|t|t|t|t|c|t|c|t|t|t|g|c|a|g|g|t|g|t|c|t|c|c|t|g|c|a|c|c|t|g|c|g|c|c|a|g|c|t|c|c|t|g|c|a|ei
c|a|g|c|c|a|c|t|c|t|g|c|c|c|c|a|a|g|a|t|g|g|g|c|t|g|g|g|g|t|g|a|g|t|a|t|c|c|c|t|a|a|a|g|a|g|c|a|g|g|g|g|t|c|g|c|a|g|ei
a|g|g|c|a|g|c|c|t|t|c|g|a|c|g|t|c|a|a|t|a|a|c|a|g|a|t|g|t|g|t|c|g|g|t|g|a|t|g|a|t|g|a|g|c|g|a|g|a|t|g|g|a|c|g|t|g|a|ei
c|c|c|a|c|c|a|t|g|a|g|g|a|c|a|t|a|c|a|a|c|t|g|g|a|a|t|a|c|t|g|a|a|a|c|t|t|g|c|t|g|c|c|t|a|t|t|g|g|g|t|a|t|g|c|t|g|a|ei
t|a|t|a|c|c|a|a|g|a|g|g|c|t|c|g|g|c|a|c|a|g|a|a|g|g|a|g|g|t|a|g|c|t|c|c|a|c|c|t|g|c|c|t|t|c|c|c|t|g|c|a|g|g|c|c|g|g|ei
g|g|c|t|g|g|a|c|c|g|a|c|c|a|c|a|g|c|g|c|g|t|g|a|t|a|a|g|t|c|g|g|c|c|c|c|c|t|g|c|c|c|c|g|t|c|c|t|g|c|c|c|t|g|c|c|g|g|ei
t|g|g|g|a|g|g|g|a|c|c|a|a|a|g|g|c|g|g|c|c|a|g|a|a|t|a|a|c|t|g|a|c|t|t|c|a|c|c|a|t|g|c|a|a|t|t|t|g|t|g|t|c|t|t|c|c|t|ei
a|g|c|g|a|a|a|g|t|g|a|a|a|c|t|c|c|t|t|a|c|t|g|g|c|t|g|t|a|a|a|t|a|g|t|g|t|c|a|t|a|g|c|t|c|a|a|g|c|t|c|c|a|c|c|t|g|t|ei
c|t|g|a|c|t|g|c|c|t|c|c|t|c|g|t|c|c|t|t|t|c|c|c|c|c|a|g|c|c|a|c|c|t|g|c|g|g|c|c|t|g|a|g|a|c|a|g|t|a|c|a|g|c|c|a|g|c|ei
g|g|c|t|a|c|a|g|c|t|c|t|c|c|c|t|g|g|g|c|a|t|c|t|c|c|a|g|g|t|a|a|t|g|a|g|g|c|t|c|c|c|c|c|a|g|c|t|g|c|c|c|c|t|a|c|a|g|ei
g|t|g|g|g|a|c|c|a|c|a|g|c|c|a|g|g|a|c|g|g|c|c|t|c|a|a|g|a|t|a|g|g|g|g|c|t|g|a|g|g|g|a|g|g|c|c|a|a|g|g|g|g|a|a|c|a|t|ei
a|g|c|c|a|g|g|g|c|a|c|t|c|a|c|c|a|g|g|c|t|g|c|a|a|a|c|a|g|t|g|c|t|g|g|g|g|t|a|a|g|a|g|g|g|g|a|g|c|g|g|g|g|g|a|t|c|c|ei
a|t|g|a|g|g|g|a|g|g|t|a|g|g|g|a|c|g|g|t|a|c|t|t|c|c|a|g|g|t|a|t|a|t|t|c|g|a|a|a|g|t|c|c|a|t|a|a|t|g|g|t|t|c|a|g|a|a|ei
t|g|a|a|c|a|g|c|t|t|t|c|t|g|t|a|g|c|a|g|a|g|a|c|c|c|a|a|t|g|c|t|t|g|c|t|t|t|g|a|g|c|c|a|g|c|c|a|a|c|c|a|g|a|t|g|g|t|ei
t|g|t|g|a|g|c|c|a|c|a|c|c|c|t|a|c|a|g|t|t|g|g|c|a|t|c|t|a|c|t|c|c|c|a|g|g|a|g|c|a|g|g|g|a|g|g|g|c|a|g|g|a|g|c|c|a|g|ei
c|g|t|c|t|g|g|t|g|g|g|g|g|g|c|a|g|c|a|g|c|a|t|t|t|g|a|a|g|g|c|a|c|c|g|t|g|g|a|g|g|t|g|c|g|c|c|a|g|g|g|g|g|c|t|c|a|g|ei
t|c|t|c|a|c|t|g|c|c|c|c|g|a|c|c|t|c|t|g|t|c|t|c|a|c|a|g|a|a|c|a|c|c|t|t|a|g|g|c|t|g|g|t|g|g|g|g|c|t|g|c|g|g|c|a|a|g|ei
g|g|t|g|c|t|c|a|c|a|g|c|t|g|c|c|c|a|t|t|g|c|c|a|a|g|a|a|g|t|a|a|g|t|a|g|g|a|c|c|c|t|g|g|g|a|t|c|t|g|g|g|g|a|g|g|g|a|ei
g|g|t|g|a|t|a|g|g|a|c|t|a|g|a|g|g|a|g|t|a|a|c|g|a|t|a|t|t|t|c|a|c|c|t|t|c|a|a|c|t|t|a|t|a|c|c|t|g|a|a|g|c|t|g|c|c|c|ei
t|t|c|c|t|c|t|t|t|t|a|c|c|a|a|g|g|a|c|c|c|g|c|a|c|a|t|g|g|t|a|g|g|t|g|t|t|t|t|g|g|c|t|c|g|a|g|g|c|c|g|c|c|a|t|c|c|t|ei
c|c|t|c|t|c|t|g|t|a|a|c|t|a|c|c|t|g|t|t|g|t|c|c|c|c|a|g|c|t|g|t|c|t|a|t|c|c|a|c|g|a|g|c|g|a|g|a|a|g|a|c|a|g|c|c|c|c|ei
c|a|a|c|a|t|t|c|c|c|a|t|g|a|g|t|c|a|a|g|t|c|a|c|c|c|a|g|g|t|g|a|g|g|c|c|t|c|t|g|c|a|g|g|a|a|g|c|c|c|c|t|g|t|g|c|c|c|ei
a|c|a|t|g|t|t|g|c|c|c|t|c|t|g|g|a|t|a|a|a|t|t|t|a|a|g|g|a|g|g|c|a|g|a|a|a|g|g|t|g|a|a|a|g|c|t|g|g|a|g|a|t|a|c|t|g|t|ei
g|a|t|t|c|t|t|a|c|a|g|a|a|a|a|c|a|a|g|t|g|g|t|a|a|g|a|t|g|g|t|g|a|a|a|c|c|t|g|t|t|t|g|t|t|g|g|a|c|a|t|a|c|t|g|g|a|t|ei
c|c|a|c|t|g|g|c|t|g|c|c|t|t|c|t|t|t|c|c|c|a|c|g|t|g|a|g|t|a|c|c|c|c|c|a|c|g|t|c|g|g|g|g|t|c|c|a|t|g|t|g|c|c|c|g|c|c|ei
g|g|g|a|a|c|c|t|g|a|c|g|g|a|g|a|c|c|c|t|g|g|g|t|c|c|a|g|g|t|g|g|c|c|a|t|c|a|a|a|c|a|c|g|t|g|g|a|g|a|a|g|g|a|c|c|g|g|ei
c|c|c|c|c|a|t|t|c|t|c|g|c|c|t|c|t|c|t|c|c|c|c|c|t|c|a|g|a|c|c|c|g|t|c|c|a|a|g|a|a|g|c|a|g|g|g|a|c|c|a|t|g|g|c|t|g|g|ei
a|t|g|t|c|c|a|t|a|t|c|t|c|t|c|g|t|c|t|c|t|t|c|c|a|c|a|g|c|t|c|c|t|g|g|g|c|a|a|c|g|t|g|c|t|g|g|t|g|g|t|t|g|t|g|c|t|g|ei
c|t|g|t|c|t|c|t|c|t|c|c|c|c|t|c|c|c|t|c|c|c|t|c|t|g|g|c|g|c|c|t|t|c|t|c|g|g|c|t|c|g|c|c|g|c|c|g|c|c|g|c|c|g|c|c|t|c|ei
a|a|t|a|g|a|t|g|g|g|g|c|t|g|t|g|c|c|t|a|g|t|g|g|g|c|t|c|a|g|g|c|c|a|g|t|a|t|g|g|a|c|t|t|t|a|t|g|t|g|g|t|c|a|c|t|g|c|ei
t|c|c|c|t|t|t|c|c|c|t|g|t|a|t|t|t|t|c|c|t|t|t|c|a|a|a|g|a|a|t|t|t|g|c|t|g|g|a|c|c|a|t|t|t|g|g|a|a|g|a|a|a|a|g|a|t|g|ei
c|c|t|a|t|g|g|g|a|t|g|c|c|a|c|c|t|t|c|a|g|c|c|c|g|c|a|g|g|t|a|g|g|t|t|c|c|t|g|t|c|t|g|g|g|c|t|t|c|t|g|g|g|c|a|g|t|t|ei
c|t|g|t|g|t|t|c|a|c|c|a|c|a|t|c|a|a|g|c|g|c|c|g|a|c|a|t|c|g|t|g|c|t|c|a|a|g|t|g|g|g|a|g|c|t|g|g|g|g|g|a|g|g|g|c|g|c|ei
c|c|a|a|g|g|c|t|a|a|c|t|t|c|t|g|t|t|t|t|t|g|t|a|t|t|a|g|t|t|g|g|a|g|a|a|g|g|a|a|c|g|a|g|a|g|a|a|g|g|a|a|a|t|t|a|g|t|ei
g|g|c|t|g|c|t|g|t|t|c|a|a|g|g|g|c|a|a|g|g|c|c|t|g|c|a|g|g|t|a|c|c|c|a|g|g|g|a|g|a|g|g|a|g|a|c|g|c|c|c|g|g|g|g|a|g|c|ei
c|g|t|c|a|a|t|c|a|a|g|t|c|t|a|c|a|c|t|g|t|t|c|a|t|a|a|g|g|t|a|a|g|c|t|g|g|g|t|a|c|a|g|a|a|a|a|a|g|a|a|a|a|t|t|a|a|g|ei
g|g|g|t|g|t|a|g|c|g|c|t|g|c|a|a|a|c|g|a|t|g|a|g|a|a|g|a|g|t|a|a|g|a|a|a|c|t|g|t|t|a|c|t|t|g|c|t|a|g|c|a|t|g|g|a|a|a|ei
t|c|t|t|t|a|c|t|a|a|a|a|c|t|a|c|a|a|a|a|t|t|a|c|g|g|g|t|g|t|g|g|t|g|g|c|a|c|a|t|g|c|c|t|g|t|a|a|t|c|c|c|a|g|a|t|a|t|ei
t|t|t|g|a|a|g|c|t|g|a|t|g|g|c|c|c|t|a|a|a|c|a|a|g|a|a|g|g|t|a|a|g|a|c|t|a|t|g|g|g|t|t|t|a|a|c|t|c|c|c|a|a|c|c|c|a|a|ei
c|c|t|g|g|g|c|g|g|g|a|c|g|c|g|c|c|a|g|g|c|c|g|c|c|c|c|g|g|c|g|a|g|a|g|g|a|t|g|g|g|g|c|c|a|g|a|c|t|t|g|c|g|g|t|c|t|g|ei
a|c|a|g|t|t|t|t|c|t|g|c|t|t|t|a|a|t|t|t|c|a|t|a|a|a|g|a|t|t|a|t|g|a|t|c|t|c|a|g|a|a|a|t|t|g|t|a|t|c|t|t|a|g|t|t|g|g|ei
t|g|a|t|g|a|a|a|g|a|g|g|t|c|c|c|a|t|c|a|a|a|a|c|a|a|c|a|g|t|a|a|g|t|t|g|c|t|c|t|t|a|t|t|g|c|a|t|c|t|a|t|g|c|a|c|a|a|ei
g|g|g|g|g|a|a|g|a|g|a|t|a|a|a|a|g|c|a|a|a|c|a|g|c|t|g|g|g|a|g|g|c|a|g|t|t|c|t|g|t|t|g|c|c|a|c|t|c|t|c|t|c|t|c|c|t|g|ei
c|t|t|a|a|g|a|a|t|c|c|a|c|t|a|t|g|a|t|g|g|g|a|a|a|t|t|t|c|a|t|t|c|t|c|a|a|a|a|a|a|a|a|a|a|a|a|a|a|a|a|t|t|t|c|t|c|t|ei
a|c|c|a|a|a|g|c|t|t|t|t|c|a|t|g|g|a|t|t|a|g|g|a|a|a|a|t|c|a|t|t|t|t|g|t|c|t|c|t|a|t|g|t|c|a|a|a|c|a|t|c|t|t|g|g|a|g|ei
c|a|t|g|a|g|c|t|t|t|c|a|c|g|a|g|a|t|a|a|g|a|a|a|a|g|a|c|a|c|a|g|t|g|c|c|c|t|g|g|t|t|c|c|c|a|a|g|a|a|c|c|a|t|t|c|a|a|ei
g|a|t|t|c|a|g|c|t|t|c|g|a|g|g|g|a|a|c|c|a|g|c|g|t|a|g|a|c|t|a|t|a|a|g|a|t|c|c|t|g|g|g|g|c|t|c|c|a|g|t|t|c|a|a|g|c|t|ei
g|c|g|c|c|g|c|c|t|t|c|g|g|c|g|t|t|t|g|c|t|g|c|a|g|a|c|g|g|t|g|c|g|c|g|g|c|g|g|g|g|g|c|g|g|g|c|c|t|g|g|g|g|g|g|g|g|g|ei
t|t|a|a|c|t|t|t|t|g|g|a|a|a|a|t|t|t|t|g|t|t|c|t|a|t|a|g|g|a|a|c|a|g|g|a|g|t|a|c|a|g|c|t|g|t|g|t|a|g|t|a|a|a|g|a|t|g|ei
g|g|t|c|t|c|c|c|c|a|c|c|t|c|a|c|g|c|g|c|t|g|t|t|g|c|a|g|a|t|c|a|t|c|g|c|c|c|c|g|c|c|g|g|a|g|c|g|c|a|a|a|t|a|c|t|c|g|ei
a|g|c|c|t|g|g|g|c|t|g|a|c|c|c|c|a|c|g|t|c|t|g|c|a|c|a|g|g|c|c|c|g|c|g|t|g|c|t|g|c|c|c|c|g|g|a|a|g|t|c|t|a|t|g|c|g|t|ei
t|g|c|t|g|t|g|t|t|g|c|t|g|t|c|t|t|t|t|t|c|c|c|c|c|t|c|t|c|a|c|g|a|a|a|g|g|t|t|t|c|c|c|a|g|g|g|c|a|g|c|c|a|g|g|g|g|c|ei
c|a|a|a|t|a|g|a|a|t|t|c|a|g|c|t|g|t|t|c|a|g|a|g|a|t|t|t|t|t|c|t|t|a|a|t|t|g|g|c|t|c|a|a|c|c|a|c|t|a|g|t|c|g|t|t|g|t|ei
t|c|c|t|c|t|g|g|t|g|c|c|a|a|c|t|g|c|a|g|c|a|c|c|a|g|g|g|g|t|g|g|t|c|a|c|c|t|c|a|g|c|c|g|a|g|g|a|c|a|c|c|t|c|g|g|g|g|ei
g|t|c|t|g|c|c|t|c|a|g|t|c|c|a|c|c|c|t|g|t|a|c|c|g|g|c|c|c|g|g|t|c|c|t|t|t|g|g|a|g|t|a|g|a|a|t|g|g|a|t|t|g|c|a|a|g|t|ei
t|g|g|a|g|g|a|a|a|t|t|c|t|c|g|a|g|g|t|g|a|c|c|g|a|c|a|g|g|g|c|g|g|g|c|t|g|g|g|c|g|a|g|g|a|c|g|c|t|c|c|c|g|g|g|g|c|c|ei
a|c|a|c|a|c|a|c|a|c|c|c|t|g|t|c|c|a|c|a|a|a|g|g|c|t|a|g|g|a|a|a|c|t|a|c|g|t|g|c|c|c|t|t|c|a|g|c|c|a|t|g|c|a|c|c|c|g|ei
g|g|g|g|a|c|a|t|g|g|c|c|c|t|c|t|c|a|g|a|a|c|a|g|a|a|g|c|t|t|c|a|g|c|t|t|t|g|g|c|a|a|g|g|c|t|c|t|c|c|c|t|c|c|t|t|c|a|ei
g|t|a|g|a|a|a|g|t|a|t|c|c|t|g|a|a|c|t|g|g|g|t|a|a|t|t|t|a|a|g|g|c|t|c|a|g|a|c|t|c|a|g|c|t|g|a|a|t|a|a|g|a|a|g|t|g|t|ei
c|t|t|c|c|t|a|c|t|g|a|a|a|c|t|g|a|a|c|c|c|t|c|a|c|c|a|g|g|g|a|g|c|c|c|c|g|a|g|t|a|t|c|g|g|c|a|g|c|a|g|t|c|a|g|c|a|g|ei
a|a|c|a|t|t|c|c|t|t|a|t|t|t|t|t|t|g|c|c|t|c|t|g|t|a|c|c|g|a|c|t|c|a|t|t|g|g|t|t|c|c|t|c|g|t|c|t|g|c|c|a|c|a|t|g|c|a|ei
c|c|c|t|c|t|c|c|t|g|c|a|g|g|g|c|c|a|g|t|c|a|g|g|g|t|t|a|g|c|a|g|c|a|g|c|t|a|c|t|t|a|a|c|c|t|g|g|t|a|t|c|a|g|c|a|g|a|ei
c|a|g|g|c|a|g|t|g|c|a|g|g|a|g|t|a|t|g|g|t|t|g|g|t|g|c|t|a|c|c|a|a|c|t|g|c|c|a|t|t|c|t|g|c|t|g|g|t|c|t|t|g|g|c|a|g|t|ei
c|t|c|t|a|c|t|a|a|a|a|a|t|a|t|a|a|a|a|a|t|t|a|c|g|g|g|c|g|t|g|g|t|a|g|t|g|c|a|t|g|g|c|t|g|t|c|a|t|c|c|c|a|g|t|t|a|c|ei
c|c|c|c|a|g|t|c|a|g|t|c|t|c|c|t|t|g|c|t|c|c|c|c|g|c|a|g|c|t|g|a|c|a|a|g|c|c|a|g|a|g|a|c|g|a|c|c|a|a|g|g|a|g|c|a|a|c|ei
a|c|t|c|g|c|t|g|t|a|t|a|c|a|a|t|a|c|c|a|a|a|g|g|t|t|t|t|t|t|g|g|g|t|c|c|c|a|c|c|t|c|c|t|g|c|c|t|t|t|t|g|c|t|t|t|t|c|ei
g|g|c|c|t|c|t|c|c|t|t|c|t|c|t|t|c|c|t|t|c|a|c|t|g|c|a|g|a|g|g|c|t|g|g|a|a|g|a|t|g|g|c|a|g|c|c|c|c|c|g|g|a|c|t|g|g|g|ie
c|g|g|a|g|a|c|c|c|a|a|c|g|c|c|a|t|c|c|a|t|a|a|t|a|g|t|t|c|t|t|c|c|t|g|a|g|g|g|c|g|a|g|c|g|g|c|c|a|g|g|t|g|c|g|c|c|t|ei
c|a|c|t|c|t|c|a|g|c|t|t|c|t|c|c|t|c|c|c|t|g|c|c|c|t|a|g|c|t|c|c|t|c|t|a|a|g|g|a|t|g|t|g|c|c|t|c|t|t|a|c|c|a|t|c|a|a|ei
a|c|t|t|c|a|t|c|t|c|t|g|a|g|a|t|c|a|g|c|a|g|t|c|a|g|g|a|t|c|c|c|a|c|c|a|c|a|g|a|a|g|a|g|g|a|a|g|a|g|g|a|t|t|t|c|a|g|ei
g|t|c|a|c|c|g|t|g|t|c|c|t|g|c|t|c|t|a|g|a|t|g|g|g|t|g|g|t|t|a|t|t|c|a|c|a|a|c|g|g|t|t|a|t|t|c|a|g|c|c|g|t|c|a|g|t|t|ei
c|a|t|c|a|g|t|a|g|a|t|t|c|a|c|t|t|a|t|c|a|c|a|g|t|a|a|g|c|g|g|g|a|t|g|t|c|a|c|t|c|a|g|g|c|c|a|c|g|g|g|t|a|a|a|t|t|a|ei
a|g|g|c|a|g|t|c|c|t|g|g|t|c|a|g|t|t|t|g|c|a|a|c|a|g|t|c|t|t|t|c|c|t|g|g|c|c|t|g|a|a|t|t|a|c|t|g|c|a|c|c|t|c|a|g|g|c|ei
g|c|c|c|a|t|a|t|t|c|t|t|a|t|g|a|a|a|a|t|g|t|g|a|t|t|t|t|g|g|c|a|a|c|t|t|c|t|g|g|t|g|c|g|a|g|t|t|t|t|g|g|a|c|t|t|c|c|ei
c|a|g|g|c|a|g|g|g|g|t|g|g|g|a|g|a|g|c|c|a|g|c|c|c|t|c|t|a|c|c|c|g|g|c|c|c|a|g|a|g|a|c|c|c|c|t|t|c|c|t|t|t|c|c|t|c|t|ei
a|g|c|c|a|c|c|t|t|t|g|c|c|t|t|t|g|c|t|g|g|a|c|t|a|a|c|a|a|c|c|t|c|a|a|t|g|g|g|g|a|a|g|a|c|c|a|a|g|a|c|a|t|t|c|t|g|a|ei
c|c|a|c|c|a|t|c|g|t|g|g|g|c|g|t|c|c|g|c|a|a|g|c|g|g|g|c|a|g|a|t|c|t|g|g|c|c|c|a|a|c|g|a|t|g|a|c|g|a|g|g|g|c|g|c|c|t|ei
a|a|g|c|c|a|a|t|t|t|t|g|t|c|c|a|c|g|t|g|t|t|g|g|t|c|a|t|g|t|g|a|g|t|g|a|a|a|t|c|c|c|a|t|c|t|g|a|t|t|a|t|c|a|c|t|t|c|ei
c|a|t|g|c|t|c|a|c|t|g|t|t|c|t|c|c|c|c|a|t|c|c|t|t|c|c|t|t|c|c|c|a|t|g|t|t|c|a|t|t|a|a|t|t|c|a|t|a|t|t|g|c|c|c|c|g|c|ei
t|t|g|a|t|a|a|c|a|t|g|a|c|a|t|t|t|t|c|c|t|t|t|c|a|c|a|g|a|a|t|g|a|a|a|c|a|g|t|a|g|a|a|g|t|c|a|t|c|t|c|a|g|a|a|a|t|g|ei
c|a|c|g|t|t|g|g|g|a|g|g|t|c|g|a|g|g|c|a|g|g|c|g|t|c|a|c|t|t|g|a|g|c|c|c|a|g|c|a|g|t|g|t|a|a|g|g|t|t|c|t|t|g|t|a|t|c|ei
a|t|t|a|c|a|g|g|c|g|t|g|a|g|c|c|a|c|t|g|c|g|c|t|g|c|c|t|c|c|a|t|c|c|t|c|a|t|c|c|t|g|a|a|g|a|t|g|c|a|a|g|a|a|c|t|t|c|ei
g|a|a|c|c|a|t|c|t|g|a|a|a|g|c|t|a|c|a|c|c|c|a|t|a|a|a|g|g|t|t|g|g|t|a|a|c|g|t|t|t|a|a|a|a|t|c|c|t|g|t|t|t|c|t|t|t|g|ei
t|g|g|g|c|c|c|t|g|a|g|a|c|c|t|g|t|t|c|t|c|c|c|a|c|c|a|g|g|t|g|c|a|g|g|a|g|c|g|g|g|a|c|a|g|g|g|c|a|c|t|c|a|g|c|t|c|a|ei
a|t|t|t|t|g|a|a|c|c|c|c|t|g|c|c|c|a|t|c|t|t|c|t|g|c|a|g|g|c|c|c|a|g|c|c|c|c|a|g|c|c|c|a|g|g|g|g|a|c|c|c|c|a|g|a|c|g|ei
c|a|g|g|t|c|c|c|t|g|a|a|a|c|t|c|t|t|t|c|t|c|c|t|c|c|a|g|c|t|a|t|a|t|c|t|g|g|g|t|g|t|g|g|t|g|c|t|g|g|c|a|g|c|t|g|t|g|ei
g|g|t|t|a|t|g|a|g|g|c|t|t|a|t|g|a|t|g|a|g|a|g|g|g|g|a|t|g|a|t|g|c|c|t|c|c|g|a|t|a|c|c|a|a|c|c|c|t|g|a|t|t|t|c|t|a|c|ei
g|g|g|c|a|c|a|g|t|g|c|c|a|c|t|c|a|g|t|g|c|c|t|t|a|a|a|a|g|t|a|t|g|t|g|c|t|g|a|g|g|c|t|g|g|a|a|g|g|t|g|g|t|g|c|a|t|g|ei
t|g|t|g|g|a|g|c|a|g|t|c|t|t|c|g|t|t|t|c|g|c|c|a|c|c|a|g|g|t|t|g|g|t|g|t|g|c|a|g|g|a|t|c|c|c|t|g|t|g|t|c|c|c|g|c|c|c|ei
t|t|a|a|g|t|g|c|t|a|g|t|t|g|t|g|a|t|t|t|t|a|t|c|t|a|a|a|g|g|c|c|a|g|a|a|g|c|t|g|t|c|t|g|a|g|g|c|a|a|t|c|a|t|g|a|t|t|ei
t|t|g|a|a|a|t|c|t|g|g|a|a|c|t|g|c|c|t|c|t|g|t|g|g|t|g|c|c|t|g|c|t|g|a|a|t|a|a|c|t|t|c|t|a|t|c|c|c|a|g|a|g|a|g|g|c|c|ei
t|g|c|t|a|a|c|t|t|c|a|a|g|a|t|a|g|a|g|c|c|t|c|t|g|a|c|t|t|t|t|c|c|g|t|g|g|c|c|g|c|g|g|c|a|a|c|c|a|c|c|c|c|a|a|g|a|t|ei
g|c|g|t|c|c|c|g|c|t|c|a|c|c|c|c|g|c|c|c|g|t|c|c|c|g|a|g|t|g|c|c|t|c|c|c|c|t|g|c|g|g|c|c|c|c|g|g|g|g|g|c|a|a|a|g|g|c|ei
c|t|g|c|t|g|c|t|g|g|t|t|c|t|g|c|t|g|c|c|t|g|g|g|c|c|a|g|g|t|g|a|g|g|c|a|g|c|a|g|g|a|g|a|a|t|g|g|g|g|g|c|t|g|c|t|g|g|ei
g|t|g|g|c|c|a|c|a|g|c|t|c|t|c|c|t|c|c|c|g|c|c|c|g|c|a|g|g|t|c|t|t|c|c|t|c|a|c|c|g|c|t|t|t|g|c|g|c|g|c|c|c|c|g|a|a|g|ei
g|c|t|c|t|c|a|a|c|t|c|c|t|c|c|a|a|t|t|g|c|g|g|t|c|c|a|g|g|c|c|a|t|c|c|g|c|g|g|a|a|c|t|c|g|a|g|g|a|g|t|c|g|c|c|a|c|c|ei
g|g|c|c|t|g|a|c|t|t|c|t|a|g|c|c|a|c|g|g|g|t|c|c|g|c|a|g|t|t|g|g|c|c|c|a|g|c|g|c|t|t|c|g|g|g|c|c|g|g|t|g|t|t|c|a|c|g|ei
t|g|a|a|g|c|c|t|t|c|t|c|a|c|c|a|a|g|g|g|t|a|c|c|c|a|c|c|g|g|a|a|t|t|t|c|c|a|g|g|a|a|g|a|a|a|t|a|g|a|g|t|t|t|c|t|t|a|ei
g|c|c|g|t|g|g|t|t|t|t|t|t|t|g|c|t|t|c|a|c|c|a|c|t|g|a|g|g|t|g|c|g|t|c|c|t|g|g|g|g|a|c|a|a|g|c|a|a|a|a|g|g|c|t|c|c|t|ei
c|c|a|a|c|a|t|g|c|c|t|g|c|c|t|c|a|t|t|g|a|g|g|c|a|g|g|g|g|t|a|a|g|g|a|c|t|g|g|g|g|g|g|t|g|a|g|g|g|t|t|g|g|g|a|g|g|a|ei
t|t|a|t|a|t|a|a|a|t|t|a|g|g|c|a|t|a|a|t|g|a|c|a|t|a|a|g|t|a|a|g|a|a|c|t|t|c|a|a|g|c|c|c|t|a|t|t|c|a|t|c|c|c|a|t|g|g|ei
g|g|c|t|t|t|g|a|g|a|a|g|g|g|t|g|g|a|c|a|g|a|g|c|c|c|t|a|g|c|c|c|c|a|c|c|a|g|g|g|a|t|g|c|t|t|a|g|c|c|a|a|g|c|a|g|t|c|ei
g|a|g|c|t|g|a|g|c|a|g|c|c|t|g|a|g|a|t|c|t|g|a|g|c|a|c|g|g|c|c|g|t|g|t|a|t|t|a|c|t|g|t|g|c|g|a|c|c|g|c|a|a|c|t|g|g|a|ei
a|g|a|c|c|c|g|c|c|g|g|g|a|g|g|c|g|g|a|g|g|a|c|t|c|a|g|g|g|t|g|a|g|c|c|c|c|a|c|c|g|c|c|c|c|t|c|c|g|t|g|c|c|c|c|c|g|c|ei
c|t|g|a|t|a|t|t|g|c|t|g|a|c|a|t|t|g|a|a|a|c|a|t|a|a|a|g|g|t|a|a|a|g|a|a|t|t|t|c|c|t|a|t|t|t|c|t|g|g|g|a|a|a|g|t|t|t|ei
c|c|t|g|t|g|a|g|g|a|a|g|g|c|t|t|c|a|t|g|t|t|g|a|g|g|a|c|c|a|g|c|c|c|a|g|g|t|t|g|a|a|t|g|c|a|c|c|a|c|t|c|a|a|g|g|g|c|ei
a|g|c|t|t|c|a|t|t|c|c|t|g|c|c|t|c|t|t|g|t|c|t|g|t|c|a|g|c|a|c|a|t|a|t|t|g|g|t|c|a|t|a|a|a|a|c|a|t|a|t|t|c|t|g|g|t|t|ei
g|a|c|c|a|g|g|t|c|t|t|t|t|t|t|t|t|t|g|t|t|c|t|c|c|c|a|g|c|c|a|g|c|a|a|c|a|g|t|g|c|c|c|a|g|g|g|c|t|c|t|g|a|t|g|a|g|t|ie
t|t|c|c|c|t|c|t|g|g|g|c|g|c|c|g|g|g|c|t|g|c|a|a|g|c|c|a|a|c|t|a|g|g|a|c|g|c|t|g|g|c|c|c|c|g|c|g|c|t|c|c|g|g|g|c|t|a|ei
t|t|a|t|g|a|g|c|c|a|a|t|c|a|g|a|g|g|t|g|t|t|g|a|a|a|a|c|a|c|c|t|c|c|c|t|a|c|t|a|g|g|t|c|a|a|g|g|t|a|g|a|a|a|g|g|g|g|ei
t|g|c|c|t|a|g|t|a|c|a|g|c|c|t|g|t|t|a|c|t|a|t|c|g|c|t|a|a|t|c|a|g|g|g|a|g|a|t|a|a|t|c|c|t|t|g|t|a|a|a|c|c|a|g|t|a|a|ei
g|c|g|c|g|c|c|g|a|g|c|g|c|c|c|c|g|c|t|c|c|g|c|t|a|c|c|t|g|c|c|a|c|c|a|g|g|g|a|g|t|g|g|g|c|g|g|g|c|a|t|t|g|t|t|c|g|c|ei
c|c|a|g|c|c|t|c|t|c|t|c|a|t|g|c|t|t|t|t|g|g|c|a|a|c|a|g|g|t|a|a|g|g|g|c|c|a|c|c|c|c|a|g|g|c|t|a|t|g|g|g|a|g|a|g|t|t|ei
c|t|a|a|t|a|a|t|t|g|c|c|a|g|a|g|t|a|c|a|g|t|g|t|t|t|g|t|t|g|a|t|c|a|t|g|t|a|t|t|c|a|g|t|c|a|a|g|t|t|a|a|a|a|c|a|a|t|ei
c|c|a|g|t|a|g|t|g|t|c|g|g|g|a|g|c|a|a|g|t|t|c|g|a|a|a|a|c|t|c|a|a|a|c|c|t|t|t|c|a|g|g|g|t|t|g|t|g|g|a|a|t|c|t|t|g|c|ei
c|c|t|c|t|a|t|c|c|g|t|a|t|t|a|g|g|t|c|t|t|t|g|g|g|c|t|g|g|a|t|g|c|a|c|c|a|t|t|g|g|c|t|c|c|t|g|t|t|t|g|a|a|a|t|g|a|g|ei
t|g|a|a|g|a|a|g|a|c|a|g|g|g|a|g|a|c|a|t|t|c|a|g|a|c|a|a|g|t|a|a|g|g|a|t|c|c|a|g|t|t|t|a|a|a|g|g|t|a|g|a|t|g|c|a|a|a|ei
g|c|a|a|c|t|c|a|t|g|a|a|c|t|t|g|g|c|c|a|t|t|c|t|g|g|g|t|a|t|g|g|g|a|c|a|t|t|c|c|t|c|t|g|a|t|c|c|t|a|a|t|g|c|a|g|t|g|ei
c|a|c|t|g|t|g|t|g|t|c|a|a|a|a|t|c|t|a|g|a|a|c|t|a|t|c|t|c|c|t|a|c|c|t|g|c|t|c|t|g|a|a|a|c|c|a|a|c|a|g|c|a|a|g|t|t|g|ei
c|g|t|c|t|g|c|c|c|c|t|g|c|a|g|c|t|g|g|a|t|g|a|g|t|g|t|t|c|g|g|c|c|t|g|a|g|c|a|a|g|a|a|g|g|a|g|a|a|g|a|g|g|a|a|g|g|a|ei
t|g|a|c|c|a|g|g|t|c|c|t|g|t|t|t|t|t|a|t|t|c|t|c|c|c|a|g|g|c|g|g|c|a|a|c|a|g|t|g|c|c|c|a|g|g|g|c|t|c|t|g|a|t|g|t|g|t|ei
a|c|t|g|a|g|t|c|c|c|c|g|t|g|c|t|t|c|c|c|c|c|t|t|c|t|a|g|g|c|a|a|g|g|a|g|a|a|g|g|a|g|c|c|c|c|t|g|g|a|g|t|c|g|c|a|g|t|ei
t|t|g|g|a|t|t|t|g|a|a|g|g|a|a|a|g|a|a|c|t|g|t|a|t|t|a|g|g|t|a|a|g|t|a|a|c|t|a|t|t|t|t|t|t|g|a|a|t|a|c|t|c|a|t|g|g|t|ei
c|a|t|t|a|a|a|a|c|a|t|t|t|a|t|a|t|c|t|a|t|a|a|t|t|g|a|a|a|a|c|t|a|a|t|c|a|g|t|a|t|t|t|t|t|t|a|a|a|g|t|a|t|a|a|a|a|c|ei
c|c|t|a|a|c|c|a|c|a|a|g|a|c|c|c|c|c|t|t|c|t|t|c|t|c|a|g|t|g|g|t|g|t|t|c|t|c|c|a|t|g|t|c|c|t|t|t|g|t|a|c|a|a|g|g|a|g|ei
t|a|g|a|c|c|c|t|t|t|c|t|c|c|t|c|c|a|g|g|a|g|a|g|a|t|c|t|c|t|c|t|c|c|g|a|c|c|t|g|c|c|a|c|a|g|a|t|c|c|c|c|t|a|t|t|c|a|ei
c|t|t|a|a|c|t|g|a|t|g|a|c|a|t|t|c|c|a|c|c|a|c|a|a|g|a|a|g|t|g|a|a|a|a|t|g|g|c|c|g|g|t|c|c|t|t|g|c|c|t|t|a|a|g|t|g|a|ei
g|a|t|a|t|a|t|t|t|g|a|g|a|c|a|t|t|t|t|c|a|a|g|c|t|a|a|t|g|a|a|a|c|a|t|t|c|t|g|c|c|t|g|t|g|a|t|a|c|a|a|a|t|c|t|c|c|a|ei
c|a|c|g|a|c|c|a|t|c|g|a|a|a|a|c|g|c|a|t|g|g|g|c|c|a|a|g|g|t|a|a|a|a|g|g|g|t|t|g|g|g|a|g|g|c|c|a|t|g|g|t|g|g|g|t|a|t|ei
t|g|t|t|t|g|t|a|g|a|c|t|t|g|g|a|a|c|c|c|a|c|a|t|a|t|t|g|g|t|g|a|g|t|t|g|a|c|c|t|c|a|g|t|a|a|c|c|c|a|a|g|t|g|a|g|a|t|ei
a|a|a|a|a|t|g|a|t|t|g|t|a|t|t|t|c|c|t|t|t|c|c|c|c|c|a|g|a|c|t|c|t|g|a|g|g|a|t|t|c|c|t|g|t|t|c|c|t|g|t|a|c|a|t|a|a|a|ie
a|g|c|t|g|g|c|a|t|a|t|c|g|g|c|c|g|c|c|c|a|a|g|g|c|c|c|t|g|t|c|c|a|g|t|g|t|c|t|g|c|t|t|g|c|c|a|t|c|c|t|g|c|c|a|g|a|a|ei
t|c|t|c|c|g|t|g|g|t|g|a|a|t|c|g|g|g|c|c|a|a|g|a|g|c|a|g|g|t|g|g|a|g|c|t|g|g|g|g|c|c|c|g|g|c|t|g|t|g|g|g|g|t|c|a|g|g|ei
t|a|t|t|c|t|t|g|a|c|a|t|g|a|g|a|a|a|a|t|c|a|g|a|t|t|g|g|a|c|c|a|g|g|c|g|c|g|g|t|g|g|c|t|c|t|t|g|c|c|t|g|t|a|a|t|c|c|ei
g|g|c|g|a|c|c|c|t|c|c|t|c|t|g|g|t|a|t|c|c|t|g|g|c|t|c|a|c|t|g|a|g|a|t|g|c|t|t|t|t|c|c|t|a|t|c|t|g|c|a|c|a|g|a|t|c|a|ei
a|c|t|g|t|c|t|g|t|c|t|t|t|c|t|g|t|c|t|g|t|c|c|a|c|c|a|g|g|c|t|g|c|a|g|g|a|g|g|a|g|a|t|t|c|a|g|t|t|g|a|a|g|g|a|a|g|a|ei
c|a|t|t|g|a|g|g|a|c|c|g|t|g|t|t|c|a|a|g|a|g|g|a|c|t|c|a|c|t|g|c|c|t|t|g|t|g|g|a|g|g|a|g|t|t|g|a|g|a|a|a|a|a|c|c|a|a|ei
a|g|t|g|a|c|c|c|c|c|t|t|c|c|t|t|a|t|t|c|c|t|c|c|a|c|a|g|g|g|a|g|t|g|g|t|t|t|t|c|a|g|a|g|a|c|a|t|t|t|c|a|g|a|a|a|g|t|ei
c|c|g|g|a|a|g|c|t|g|c|t|g|g|a|g|g|g|a|g|a|g|g|g|g|c|c|g|g|t|g|a|g|g|g|g|c|c|a|g|g|c|a|g|g|a|g|c|c|g|a|g|t|g|g|g|a|g|ei
a|t|g|a|g|g|c|t|g|a|c|a|c|c|a|c|c|g|a|a|g|a|t|a|t|c|t|g|g|t|g|a|t|t|g|g|g|t|g|c|t|c|c|a|g|a|g|g|g|g|g|t|g|g|a|t|a|g|ei
g|a|g|g|a|g|c|t|a|g|a|c|a|a|g|t|a|c|t|g|g|t|c|c|g|c|a|g|g|t|g|c|g|t|g|a|g|g|g|g|a|g|g|g|g|a|t|g|g|c|t|g|c|c|a|a|g|g|ei
c|t|g|g|c|c|t|t|t|g|c|t|t|g|g|g|c|t|t|c|t|a|g|c|c|c|t|t|t|c|a|c|t|g|c|a|c|t|c|a|c|t|g|t|c|t|t|c|t|c|c|c|c|c|t|c|c|t|ei
a|c|a|t|a|t|g|g|c|t|a|g|c|c|a|g|c|t|t|t|c|c|a|c|c|c|a|t|t|t|a|t|t|a|a|a|t|a|g|g|g|a|a|t|c|c|t|t|t|c|c|c|c|a|t|t|g|c|ei
c|t|t|t|a|a|a|a|a|a|t|t|a|a|c|a|t|t|t|t|t|c|t|t|a|t|a|g|g|g|a|t|c|t|g|a|a|a|c|a|a|c|a|t|t|c|a|t|g|t|g|t|g|a|a|t|a|t|ie
t|c|t|g|g|g|a|g|a|g|g|c|c|a|c|a|t|g|a|g|t|t|c|g|c|c|t|g|g|t|a|t|g|t|g|g|g|g|g|c|c|g|g|g|g|g|c|c|t|g|c|c|g|t|c|a|a|a|ei
t|g|a|g|c|g|c|t|c|a|g|g|a|a|t|c|a|t|g|g|g|c|t|t|a|a|a|g|g|t|a|g|g|t|g|c|t|g|a|g|g|g|a|a|t|g|a|a|a|t|c|t|g|g|g|a|c|g|ei
g|c|c|a|g|g|g|g|a|c|c|t|a|g|g|g|c|a|a|g|c|a|g|g|t|t|t|c|t|c|c|t|c|c|t|t|c|c|t|c|c|c|a|g|g|a|a|g|g|g|c|c|a|g|g|a|a|a|ei
g|c|g|g|g|c|t|g|g|t|c|g|g|g|c|c|t|c|t|t|g|t|c|c|g|c|a|g|t|g|t|g|t|a|a|c|g|c|a|g|g|c|c|t|g|g|g|c|c|t|g|c|t|g|g|g|g|c|ei
g|c|t|a|a|t|a|a|a|a|a|c|a|a|g|c|a|c|t|a|t|t|g|t|a|a|c|t|t|t|t|a|g|g|t|g|t|g|t|g|t|a|c|t|t|t|g|g|a|g|c|c|a|c|c|a|t|t|ei
c|a|g|a|g|c|t|g|c|g|a|g|g|a|g|a|g|g|a|a|t|c|t|c|g|g|a|g|a|a|c|g|g|g|t|a|t|g|a|g|t|g|t|g|a|g|t|g|g|c|g|c|t|a|t|a|a|c|ei
g|c|t|a|c|c|c|c|c|t|g|c|g|a|g|g|g|a|g|c|t|c|c|t|t|t|c|g|g|t|a|g|g|c|c|t|g|g|g|g|a|t|g|a|g|t|g|g|c|a|g|g|t|g|c|t|g|c|ei
g|g|a|g|c|t|c|c|a|g|a|a|a|c|a|g|c|a|g|t|c|t|t|g|c|g|c|t|g|a|g|c|t|c|a|g|c|g|c|g|g|t|g|g|g|t|g|a|g|a|a|c|g|g|c|g|g|g|ei
c|c|t|g|g|a|c|t|t|t|c|t|t|g|c|c|t|c|t|t|c|c|c|c|c|c|a|g|c|t|g|g|a|g|a|g|a|a|a|g|g|c|c|a|a|g|c|g|g|a|c|c|a|g|a|g|c|t|ei
c|t|c|t|a|c|g|t|g|g|g|c|a|c|c|a|t|g|t|t|g|g|a|g|g|g|g|c|g|a|c|c|t|g|t|c|c|c|g|a|t|t|t|g|c|a|c|t|g|c|t|c|a|t|g|a|c|c|ei
a|c|t|g|g|g|g|c|c|t|a|t|c|a|g|a|g|g|g|t|g|g|a|g|t|g|a|g|a|g|a|a|g|g|a|g|a|g|g|a|t|c|a|g|g|a|a|a|a|a|t|c|a|c|t|a|a|t|ei
c|a|g|t|a|t|c|c|t|t|t|t|g|c|t|g|t|g|a|c|g|a|g|t|c|g|g|g|a|a|g|a|a|t|c|t|g|t|a|t|t|t|c|a|c|a|g|a|c|t|g|g|a|a|g|a|t|g|ei
c|a|g|c|t|g|g|c|a|t|a|t|g|a|c|a|c|c|t|a|t|c|a|g|g|t|t|t|g|t|a|a|g|c|t|c|t|t|g|g|g|t|a|a|t|g|g|g|t|g|c|g|c|t|t|c|a|g|ei
a|a|t|t|g|a|c|t|g|g|g|g|a|c|g|c|a|g|t|c|t|t|g|a|t|a|t|g|c|a|c|t|t|t|c|t|t|t|g|c|c|a|a|a|g|g|c|a|a|a|c|g|c|a|g|a|a|c|ei
a|t|t|g|a|t|c|a|g|t|c|c|a|t|t|g|a|c|t|t|c|g|a|a|c|g|a|c|t|c|t|g|c|c|a|t|t|g|a|c|c|t|c|c|a|g|a|t|c|a|a|c|a|c|a|c|a|g|ei
c|t|t|a|c|t|t|t|t|t|t|t|t|c|t|c|a|t|t|c|t|c|c|a|c|c|a|g|g|c|t|g|a|c|a|t|t|a|t|t|a|t|c|g|g|a|c|a|c|t|t|a|t|g|t|a|t|c|ei
g|t|g|a|g|g|t|t|t|g|t|t|t|c|t|a|c|c|a|g|t|t|a|t|c|g|g|a|g|t|a|a|c|c|a|g|a|t|a|a|a|g|a|g|a|t|g|c|c|c|t|c|t|g|t|t|t|c|ei
c|c|t|t|g|c|t|c|c|t|g|c|c|g|c|t|g|g|c|c|t|t|g|t|c|t|c|c|g|t|g|a|g|t|t|t|g|a|g|a|c|g|c|c|c|g|g|g|a|a|g|g|c|a|g|g|g|g|ei
g|g|c|t|c|t|g|a|t|g|t|g|t|c|t|c|t|c|a|c|g|g|c|t|a|a|a|g|g|t|g|a|g|a|c|c|t|t|g|g|g|g|g|g|c|c|t|g|a|t|g|t|g|t|g|g|g|g|ei
c|t|c|a|t|c|a|t|t|g|t|g|g|a|g|g|g|a|t|g|t|c|a|a|g|c|a|g|g|t|g|a|g|c|a|c|a|g|c|c|a|c|g|g|g|a|g|g|c|a|g|a|t|g|a|c|a|g|ei
a|a|a|a|a|a|a|a|a|a|t|a|g|c|t|g|g|g|c|a|t|g|g|g|c|a|g|g|c|g|c|c|t|g|t|a|g|t|t|t|c|a|g|c|t|g|c|t|t|g|g|t|g|t|c|t|g|a|ei
g|c|t|c|a|t|c|t|c|c|a|t|c|g|a|g|a|a|g|a|a|g|g|c|g|c|g|g|c|g|g|c|g|g|c|c|c|g|c|a|g|c|c|g|g|c|c|g|a|g|c|c|g|c|g|c|t|g|ei
c|g|c|t|c|c|g|c|t|a|c|t|a|c|a|a|c|c|a|g|a|g|c|a|g|g|c|g|g|t|g|a|g|t|g|a|c|c|c|c|g|g|c|c|c|g|g|g|a|c|g|c|a|g|g|t|c|a|ei
t|g|a|c|t|t|t|g|c|a|c|c|t|g|c|t|c|t|g|t|g|a|t|a|g|a|c|t|a|t|c|c|c|a|c|a|g|t|c|t|c|c|t|g|g|t|t|g|t|c|t|a|c|c|c|a|t|g|ei
g|t|t|t|c|a|g|t|g|t|g|c|c|t|t|c|c|c|t|t|g|a|a|c|t|g|a|c|a|c|a|a|a|g|t|a|t|g|a|a|t|t|a|c|t|t|t|a|c|t|t|g|g|c|g|g|a|g|ei
g|a|g|c|t|g|g|t|g|a|g|g|a|c|a|g|c|c|t|g|c|c|a|a|t|c|t|g|g|t|a|a|g|a|a|a|g|g|g|a|c|t|c|a|g|g|g|t|g|c|g|g|g|g|a|c|a|g|ei
a|g|t|g|c|t|t|a|a|c|t|c|t|t|c|c|t|c|c|c|t|t|c|c|a|c|a|g|c|t|t|c|c|t|a|a|c|c|a|a|g|c|g|a|a|g|c|c|g|g|c|a|g|g|t|c|t|g|ei
g|t|c|a|c|g|c|a|t|g|a|a|g|g|g|a|g|c|a|c|c|g|t|g|g|a|a|g|a|c|a|g|t|g|g|c|c|c|c|t|a|c|a|g|a|a|t|g|t|t|c|a|t|a|g|g|t|t|ei
a|t|g|a|c|c|t|t|t|g|g|g|c|t|t|t|g|t|g|g|a|c|a|c|a|c|t|g|a|g|g|t|a|a|g|g|g|t|c|t|c|t|c|c|c|c|c|t|c|a|a|a|a|g|t|g|g|t|ei
t|c|a|c|a|t|t|a|g|a|t|g|c|a|a|a|t|g|c|t|g|a|c|t|g|g|g|a|a|t|g|g|a|a|c|c|a|c|c|t|c|a|g|c|a|a|a|c|g|a|a|g|c|a|g|g|t|a|ei
a|t|t|c|a|g|g|a|t|t|a|t|g|a|a|g|t|t|t|t|t|c|g|t|c|g|a|a|g|a|t|t|c|a|c|t|g|g|a|c|g|a|a|a|g|a|a|a|g|a|t|a|a|a|a|g|g|g|ei
t|c|t|g|a|a|t|g|c|a|t|t|t|g|t|a|t|g|t|c|t|c|c|g|a|g|a|a|g|a|c|t|g|t|a|g|c|c|a|t|c|a|t|t|c|a|g|a|a|g|a|t|c|t|c|t|g|t|ei
a|a|a|a|t|t|t|g|g|a|g|a|a|a|g|a|g|c|t|t|t|c|a|a|c|a|t|g|g|t|a|a|a|t|a|c|t|t|t|t|a|a|a|c|a|t|a|g|t|t|g|g|c|a|t|c|t|t|ei
a|c|c|c|a|c|a|c|a|c|a|c|c|a|a|t|t|g|c|a|g|g|c|c|g|g|a|a|c|a|t|g|a|c|c|a|g|a|a|g|t|a|g|g|c|a|a|a|c|a|c|t|a|g|t|a|a|g|ei
c|t|c|c|c|c|t|a|a|a|c|c|a|g|g|c|c|c|t|t|g|g|a|a|c|a|g|g|c|c|c|c|a|g|g|g|g|a|g|c|a|g|t|g|c|a|a|c|t|c|a|c|c|t|t|c|a|c|ei
c|c|c|a|a|a|t|g|t|c|t|c|a|g|a|a|t|g|t|a|t|g|t|c|a|g|a|a|a|c|c|t|g|t|g|g|c|t|g|c|t|t|c|a|a|c|c|a|t|t|g|a|c|a|g|t|t|t|ei
g|a|g|t|t|g|g|c|a|g|c|a|a|c|a|t|c|t|c|t|t|g|g|t|a|a|g|a|g|t|t|c|c|a|g|c|a|c|a|g|c|g|a|t|a|g|t|a|c|t|t|t|c|t|a|g|c|c|ei
t|g|g|g|c|g|c|a|c|c|c|t|t|c|a|c|t|g|t|g|g|g|g|g|a|a|a|g|g|t|g|a|g|c|t|g|g|a|a|g|c|t|g|a|g|g|t|c|t|g|g|c|g|g|g|g|c|t|ei
c|t|c|g|g|g|g|a|c|g|c|c|c|c|c|a|c|c|a|g|c|t|c|a|t|t|c|c|g|a|g|t|g|c|a|g|a|a|a|a|g|a|a|a|c|c|g|g|a|c|c|c|c|c|c|a|g|t|ei
t|t|c|t|a|t|g|a|g|g|c|a|t|t|c|t|c|t|a|a|a|a|a|c|c|a|a|g|g|t|a|a|a|a|a|g|g|c|a|a|a|t|a|a|t|g|c|t|t|a|t|t|c|c|c|t|t|t|ei
c|a|c|g|c|t|c|t|t|t|a|c|t|c|c|a|t|g|t|g|t|g|g|a|a|t|t|c|a|t|t|g|c|g|g|a|a|t|a|a|c|a|t|c|g|g|a|g|g|a|g|a|a|g|t|t|t|c|ei
g|g|c|a|a|g|g|a|c|t|t|c|t|c|t|g|g|g|c|g|g|c|c|c|a|a|t|g|g|t|a|a|g|t|g|g|t|g|c|c|c|a|t|c|t|c|c|t|c|c|c|t|g|c|c|c|c|c|ei
t|t|t|t|t|c|a|a|t|g|a|t|g|a|a|t|c|t|t|t|t|g|t|t|g|t|a|g|g|t|t|a|c|c|a|t|a|g|a|g|a|t|g|a|a|t|g|a|a|c|c|a|g|t|t|c|a|a|ei
c|a|c|c|g|g|g|g|c|t|t|g|c|t|g|t|t|g|g|a|t|a|c|t|t|c|g|c|c|a|t|t|a|c|c|t|g|c|c|a|c|t|c|t|c|t|a|g|c|a|t|c|c|t|g|g|a|c|ei
t|g|t|g|t|g|c|c|a|a|c|c|c|a|g|a|g|a|a|g|a|a|a|g|g|t|t|c|g|g|g|a|g|t|a|c|a|t|c|a|a|c|t|c|t|t|t|g|g|a|g|a|t|g|a|g|c|t|ei
t|a|g|a|a|t|c|t|g|c|a|a|a|t|g|g|a|t|a|t|t|t|g|a|c|t|a|t|t|t|c|a|g|g|c|c|c|a|t|g|g|t|g|a|a|a|a|a|g|a|a|a|g|t|a|t|c|t|ei
g|t|g|a|c|c|t|c|t|c|a|t|g|c|t|c|c|t|c|t|t|c|t|c|c|c|a|g|g|c|t|g|c|t|g|c|t|c|c|t|g|c|t|g|c|c|c|c|g|t|g|g|g|c|t|g|t|a|ei
a|t|c|t|g|c|a|t|c|a|a|g|c|t|g|a|a|g|t|t|c|t|g|g|c|c|t|c|a|c|g|a|g|c|t|g|a|t|t|t|c|a|c|c|t|t|t|g|c|a|c|a|g|a|t|c|t|t|ei
t|c|c|c|c|g|c|a|c|a|g|c|g|a|a|a|t|c|t|c|c|c|a|t|g|c|a|c|c|g|a|g|g|g|g|g|c|g|a|g|g|g|t|t|a|a|g|t|g|g|g|g|g|g|g|a|g|g|ei
t|g|a|a|g|a|a|a|a|c|c|a|a|g|a|t|c|a|t|c|t|t|t|t|g|t|g|g|g|t|g|a|g|t|t|g|c|g|g|g|c|a|g|g|c|g|g|g|t|g|g|t|g|c|a|g|c|a|ei
g|c|t|c|a|a|c|c|a|c|a|g|g|g|a|c|c|c|c|t|c|t|c|c|g|c|a|g|g|g|c|t|g|g|c|c|c|c|t|g|g|c|a|a|g|g|c|c|c|g|g|g|a|c|a|g|g|a|ei
a|g|g|a|c|g|c|t|c|a|g|t|g|c|t|g|c|t|t|t|t|g|c|t|t|c|a|g|a|a|a|c|c|t|c|c|t|g|c|a|a|a|a|g|t|g|g|a|a|g|c|g|a|a|g|c|c|g|ei
c|a|t|c|g|t|c|t|a|c|c|t|g|g|g|t|c|g|c|t|c|a|a|g|t|t|a|a|c|t|c|c|a|a|c|a|c|g|c|a|a|g|g|g|g|a|g|a|t|g|a|a|g|t|t|t|g|a|ei
g|a|g|g|g|a|a|a|g|c|a|g|c|g|t|g|c|c|t|g|t|g|t|c|c|c|a|g|g|a|g|c|g|t|c|g|g|t|a|c|g|c|a|g|g|c|c|t|g|a|a|g|c|c|c|g|g|g|ei
a|a|t|a|t|c|a|a|c|g|t|a|a|t|a|g|t|t|c|t|g|g|a|c|a|a|a|g|g|t|a|a|g|g|c|a|t|t|a|c|t|t|t|a|t|t|t|g|c|t|c|t|c|c|t|g|g|a|ei
t|c|t|t|g|t|a|t|t|t|t|g|t|t|t|t|g|t|t|t|t|a|a|t|a|c|a|g|g|t|t|t|c|t|c|a|t|t|a|a|c|c|t|t|g|t|g|a|a|g|c|a|a|a|a|g|c|c|ei
c|t|g|g|a|c|t|g|c|a|g|c|g|g|t|c|t|g|t|a|c|t|t|t|t|a|c|a|c|g|a|c|a|c|c|c|a|c|c|a|c|c|t|a|c|a|t|c|g|a|t|g|a|c|a|t|c|a|ei
a|g|t|g|c|t|t|a|a|c|t|c|t|t|c|c|t|c|c|c|t|t|c|c|a|c|a|g|c|t|t|c|c|t|a|a|c|c|a|a|g|a|g|a|g|g|c|c|g|g|c|a|g|g|t|c|t|g|ei
c|c|a|t|c|c|a|g|a|g|t|g|t|c|t|t|c|t|t|c|t|t|c|c|g|g|a|g|g|t|a|g|g|a|g|c|c|g|c|t|g|c|c|a|c|c|c|c|t|g|a|a|g|c|t|g|g|t|ei
t|g|a|a|g|g|c|t|c|c|g|c|c|t|t|g|g|g|a|a|a|a|c|g|t|a|a|a|g|t|a|a|g|g|a|c|c|c|a|g|c|c|t|g|g|g|g|t|t|g|a|g|g|g|c|a|g|g|ei
c|c|a|a|g|a|a|c|c|t|c|a|t|c|a|t|g|t|t|c|c|t|g|g|g|a|c|g|g|t|g|a|g|t|g|a|g|c|c|a|g|c|c|t|t|c|c|a|g|c|c|c|c|g|c|a|g|c|ei
g|t|t|c|t|a|a|t|c|a|t|t|t|c|a|c|c|a|t|t|t|t|t|t|a|t|t|c|g|t|t|t|t|a|a|a|a|c|a|t|c|t|a|t|c|t|g|g|a|g|g|c|a|g|g|a|c|a|ei
g|a|c|a|a|c|a|g|c|c|t|c|a|a|g|a|t|c|a|t|c|a|g|a|t|g|c|c|t|c|c|t|g|c|a|c|c|a|c|c|a|a|c|t|g|c|t|t|a|g|c|a|c|c|c|c|t|g|ei
c|a|t|c|a|g|a|g|a|a|g|a|t|g|a|c|t|a|a|t|t|g|a|t|a|t|t|g|t|c|c|a|t|c|a|t|c|t|g|g|a|t|t|a|g|t|g|t|t|t|t|a|a|g|g|c|a|g|ei
t|g|g|c|a|t|t|t|a|c|t|t|t|c|t|c|t|c|a|t|g|a|t|a|a|a|a|g|g|c|t|c|c|a|c|a|a|g|t|c|a|t|c|a|t|c|t|c|g|t|g|t|c|t|a|g|g|a|ei
g|g|c|a|c|a|c|a|c|a|t|g|g|a|t|a|t|g|t|g|c|a|c|c|t|g|g|a|c|a|c|a|t|a|c|a|t|g|t|g|c|a|g|g|a|c|a|t|g|c|a|c|a|c|a|c|a|c|ei
c|t|t|t|t|g|t|g|g|a|c|t|t|g|t|c|t|g|a|c|c|a|c|t|c|t|a|t|t|t|g|c|c|c|a|g|a|g|t|t|t|g|c|t|c|a|a|t|t|c|c|a|a|g|a|c|a|g|ei
t|g|t|g|c|a|c|a|g|a|c|a|g|g|a|a|g|g|t|g|t|g|t|a|c|c|g|c|a|g|a|c|t|t|c|t|t|t|g|c|a|a|t|g|g|g|g|a|c|a|a|t|g|a|c|t|g|t|ei
t|c|t|c|a|c|t|a|g|g|c|c|c|t|t|c|t|t|c|c|t|t|c|c|a|a|a|g|c|t|t|g|c|t|c|c|a|g|g|c|t|g|g|a|t|a|c|a|a|g|g|g|g|c|g|g|g|t|ei
c|a|a|g|g|t|g|a|g|c|t|c|c|c|c|t|c|c|c|t|c|c|a|a|c|c|a|g|a|c|t|c|a|g|t|g|t|t|c|t|c|c|a|g|c|a|g|c|g|a|g|c|g|t|g|c|c|c|ei
a|c|c|a|a|g|g|c|t|g|t|c|a|c|c|a|c|a|t|t|c|a|c|a|c|a|c|t|g|t|g|c|g|t|c|c|c|a|a|g|a|a|c|g|c|a|g|c|c|c|t|g|g|g|t|c|c|c|ei
g|c|c|c|c|g|c|a|a|t|g|a|c|c|t|g|c|g|c|c|c|c|g|c|c|c|a|g|g|c|c|t|g|c|t|g|g|a|g|c|t|c|t|c|g|c|c|c|g|t|g|g|a|g|c|g|g|g|ei
g|g|a|a|g|a|g|g|c|t|g|g|a|g|g|a|g|a|a|g|c|t|c|g|g|a|a|g|g|t|a|t|g|c|t|c|t|g|g|g|g|g|c|c|a|g|g|a|c|a|a|g|g|g|a|g|g|g|ei
t|a|c|t|a|t|t|a|a|c|a|c|a|a|t|t|c|t|t|t|t|a|t|t|t|c|a|g|t|t|c|g|a|t|g|a|a|t|t|t|a|a|a|c|c|t|c|t|t|g|t|g|g|a|a|g|a|g|ei
g|c|c|t|a|t|t|a|c|t|g|c|a|c|t|g|g|g|g|a|c|g|t|a|t|g|c|c|t|g|g|a|c|c|a|a|g|t|g|t|a|t|g|g|t|c|a|a|g|a|c|a|c|a|g|a|c|a|ei
t|g|t|t|t|c|t|g|a|a|a|g|a|g|g|g|a|t|t|a|g|c|c|g|t|g|t|c|t|t|a|c|a|t|a|g|t|c|t|g|a|c|t|t|t|g|c|a|c|c|t|g|c|t|c|t|g|t|ei
t|g|c|t|g|g|c|c|a|g|t|t|c|t|t|c|c|c|g|g|a|g|g|a|c|g|c|a|g|g|t|g|g|c|c|t|a|t|c|a|g|a|t|g|t|g|g|g|a|a|c|t|t|a|g|t|g|c|ei
t|g|g|a|c|g|g|t|a|a|c|a|g|g|a|a|t|g|t|a|t|g|a|a|t|t|g|g|g|t|g|c|c|a|a|a|a|c|t|t|g|t|g|g|c|c|g|c|c|c|t|g|t|a|c|a|a|g|ei
g|t|a|t|a|c|g|t|g|g|c|a|a|t|g|c|g|t|t|g|c|t|g|g|t|a|t|t|t|t|a|a|t|c|a|t|t|c|t|a|g|g|c|a|t|c|g|t|t|t|t|c|c|t|c|c|t|t|ei
c|a|c|c|t|t|c|c|t|c|a|t|c|g|g|c|t|g|c|g|c|g|c|c|g|c|a|a|c|g|t|c|a|t|a|g|c|c|g|a|c|a|t|c|c|t|c|t|t|c|c|g|c|a|a|g|c|a|ei
t|a|t|a|t|a|t|a|t|a|g|t|t|t|t|t|t|t|t|t|t|t|t|a|c|t|a|g|a|a|t|g|a|c|c|a|g|t|c|a|a|c|a|g|g|g|g|a|c|a|t|a|a|a|a|g|t|a|ei
g|c|c|c|c|c|a|a|c|c|a|c|g|c|t|c|t|g|t|t|g|c|t|t|g|c|a|g|c|g|a|a|g|c|c|c|a|c|c|a|c|g|a|c|g|c|c|a|g|c|g|c|c|g|c|g|a|c|ei
g|a|t|c|a|t|c|g|a|g|a|g|c|t|a|t|g|a|g|g|g|c|a|c|g|t|t|a|t|a|c|t|t|t|c|a|t|c|g|a|c|c|c|c|a|c|g|c|a|g|c|t|g|c|c|t|t|a|ei
g|c|t|g|g|g|c|c|c|t|g|g|g|c|t|t|c|t|a|c|c|c|t|c|g|a|g|a|t|c|a|c|a|c|t|g|a|c|c|t|g|g|c|a|g|c|g|g|g|a|t|g|g|c|g|a|g|g|ei
c|c|a|a|a|g|g|c|g|g|g|a|a|g|a|t|g|g|t|g|g|g|c|g|c|c|a|g|a|c|a|c|c|g|t|t|g|g|g|a|t|g|a|a|c|t|a|c|g|g|c|a|g|c|t|a|c|a|ei
a|t|t|a|t|t|a|t|t|a|t|t|a|t|t|a|t|t|a|t|t|a|t|a|g|t|a|g|g|g|g|a|c|c|t|g|g|a|g|c|c|t|t|g|a|g|g|g|a|a|a|t|a|a|a|c|t|t|ei
c|t|c|t|t|g|c|c|t|g|g|a|c|a|t|g|t|c|c|a|g|g|c|t|c|c|a|g|g|t|g|g|g|t|c|c|t|g|t|g|a|g|a|a|g|g|a|a|t|g|g|a|g|a|g|g|c|t|ei
g|c|t|c|t|c|a|c|a|g|c|c|t|t|c|t|c|t|c|c|c|c|a|c|g|c|a|g|a|a|g|g|a|g|a|a|t|a|a|g|a|a|t|g|a|a|a|a|g|g|t|c|a|t|a|g|a|a|ei
a|a|g|c|t|t|c|t|g|a|g|a|t|t|c|c|c|c|c|a|t|g|t|c|g|a|c|t|g|g|g|a|c|a|a|a|c|t|c|t|a|c|c|c|c|c|c|a|a|a|a|g|a|a|a|a|g|a|ei
a|a|g|g|c|t|c|a|g|g|a|g|g|a|g|g|g|a|g|a|t|c|a|c|t|c|a|a|c|c|t|g|c|c|c|c|g|c|c|c|c|c|t|c|c|c|c|a|g|c|c|t|g|a|t|a|a|a|ei
c|t|a|t|g|a|a|a|c|a|g|g|g|a|a|g|c|t|g|a|a|c|t|t|a|a|t|c|c|a|g|g|c|c|t|g|g|t|t|g|a|t|a|g|a|a|a|c|t|c|a|g|a|g|c|t|c|t|ei
a|g|a|a|a|t|a|a|t|c|a|g|a|a|a|a|g|c|a|a|c|a|t|a|a|g|t|c|c|t|t|g|g|t|t|a|t|c|t|t|g|g|a|t|g|a|a|c|t|a|g|g|a|a|g|a|g|g|ei
g|a|t|g|g|a|c|c|t|t|g|g|a|a|a|a|a|g|g|c|a|c|c|t|g|a|t|g|g|g|c|c|t|t|g|g|t|t|c|t|g|t|t|c|t|a|a|a|g|c|t|t|c|t|c|t|t|c|ei
t|c|t|c|c|g|t|g|a|t|g|a|a|c|c|g|g|g|c|c|a|a|g|a|g|c|a|g|g|t|g|a|g|c|t|g|g|g|g|c|c|c|g|c|t|g|t|g|g|g|g|t|c|a|g|g|a|c|ei
a|c|a|a|a|a|a|t|g|g|c|a|a|c|a|t|g|g|c|a|g|g|c|t|t|c|a|g|a|c|c|a|a|a|g|g|a|t|c|g|c|c|a|t|c|g|a|c|c|t|g|t|t|c|a|a|g|c|ei
g|t|a|t|t|t|a|a|t|t|t|t|a|g|t|t|t|t|a|g|a|g|a|a|g|g|t|g|t|c|t|g|g|c|t|g|t|g|t|t|g|c|c|a|a|g|a|c|t|g|g|t|c|t|c|t|a|a|ei
a|g|a|a|g|c|c|g|g|a|a|g|t|g|g|t|g|a|a|g|a|c|g|a|c|t|g|c|g|g|g|a|c|a|t|g|a|t|c|a|t|c|c|t|a|c|c|c|g|a|g|a|t|g|g|t|g|g|ei
a|c|t|t|c|t|g|c|t|c|a|g|g|t|g|g|a|a|t|t|g|a|a|a|g|a|a|g|c|g|g|g|a|g|g|c|t|g|a|g|t|t|t|c|a|g|a|a|a|c|t|g|c|g|c|a|g|g|ei
t|g|g|a|c|g|a|c|a|c|g|c|a|g|t|t|c|g|t|g|c|g|g|t|g|a|c|a|g|c|g|a|c|g|c|c|g|c|g|a|g|t|c|c|a|a|g|a|g|g|g|g|a|g|c|c|g|c|ei
g|a|c|c|c|c|a|g|g|g|t|c|c|c|c|c|a|c|a|c|c|t|c|t|g|c|a|g|g|t|a|g|g|a|g|c|t|g|c|t|g|a|c|t|g|c|c|c|t|g|c|t|t|g|c|c|t|c|ei
c|a|g|g|c|c|c|c|t|c|a|c|c|a|c|c|t|c|t|g|c|c|t|c|t|c|a|g|t|g|a|a|g|t|t|c|c|c|t|t|g|t|g|g|g|a|g|g|c|c|c|t|g|g|a|a|g|c|ei
g|t|c|a|a|a|a|t|t|a|a|g|c|a|t|a|a|c|t|g|g|c|g|a|a|c|c|c|a|g|a|g|g|t|c|t|t|a|a|c|a|g|t|a|g|g|g|t|t|c|g|t|a|g|a|a|g|g|ei
a|g|c|t|c|c|a|g|g|c|t|a|t|t|t|t|t|g|t|g|c|t|t|g|t|a|c|t|g|g|t|t|t|t|c|t|c|c|a|t|t|g|c|a|t|t|g|t|t|a|g|g|c|a|t|g|g|t|ei
g|a|g|t|a|a|a|c|t|t|t|t|g|c|t|g|g|g|c|t|c|c|a|g|g|a|c|c|g|c|c|c|a|t|a|g|t|t|t|a|t|t|a|t|a|a|a|g|g|t|g|a|c|t|g|c|a|c|ei
c|c|c|t|c|c|t|a|c|c|g|g|a|a|c|t|g|a|a|c|c|c|t|c|a|c|a|g|g|g|a|g|c|c|c|c|g|a|g|t|a|t|c|g|g|c|a|g|c|a|g|t|c|a|g|c|a|g|ei
t|t|t|t|g|t|a|g|g|a|c|t|a|a|c|a|t|c|c|g|c|c|a|a|a|a|t|t|a|a|a|a|a|t|t|a|t|g|g|t|t|t|a|g|g|a|g|t|c|a|t|g|c|a|g|a|t|a|ei
a|t|t|t|t|a|a|a|g|c|a|t|g|t|g|t|c|t|c|c|t|g|t|t|c|t|a|g|t|a|t|g|t|c|c|a|a|a|a|t|a|c|t|a|a|a|a|t|g|c|g|c|c|g|g|c|a|a|ei
c|c|a|t|c|c|t|g|t|g|c|t|g|c|a|t|g|c|g|c|c|a|c|a|c|c|c|a|g|t|g|a|g|t|a|g|g|a|t|c|a|c|c|g|c|c|c|t|g|c|c|c|a|g|g|g|c|c|ei
a|t|c|c|t|t|t|g|c|a|t|t|g|a|c|c|t|g|g|g|c|a|c|g|t|a|t|g|g|t|g|a|g|c|g|c|a|g|g|a|g|g|t|g|g|a|g|g|a|g|g|g|g|a|c|a|g|g|ei
g|a|t|t|t|a|g|a|t|g|t|t|g|a|a|c|a|a|c|t|t|g|g|a|t|c|c|a|g|t|g|a|g|t|a|t|c|a|g|t|t|t|c|t|c|a|t|t|g|t|a|g|a|g|a|g|t|g|ei
a|a|t|t|t|g|c|t|c|c|t|a|a|t|t|c|a|g|t|g|t|c|c|t|t|t|t|c|t|g|a|g|c|c|t|c|c|a|g|a|c|c|a|t|c|g|c|t|a|t|g|a|g|c|t|t|c|c|ei
t|c|c|c|g|a|g|c|g|c|c|c|a|g|g|g|c|g|c|t|c|a|g|g|g|g|a|c|a|t|g|g|t|t|g|g|g|g|a|g|g|c|c|t|t|t|g|g|g|a|c|a|g|g|t|g|c|g|ei
a|c|t|c|t|c|c|t|c|t|c|c|c|t|c|t|c|t|c|c|c|t|c|c|c|c|a|g|c|a|a|a|c|c|c|t|c|a|a|g|c|t|g|a|g|g|g|g|c|a|g|c|t|c|c|a|g|t|ei
c|t|g|g|t|g|t|g|a|a|t|g|g|c|a|t|t|c|t|c|t|t|t|t|g|c|a|g|a|c|a|g|a|g|g|a|g|c|t|g|a|a|c|c|g|c|g|a|g|g|t|g|g|c|c|a|c|c|ei
c|a|t|t|t|c|t|t|t|c|c|c|t|t|a|t|t|t|t|a|c|c|c|t|g|t|t|t|t|c|t|c|a|t|a|c|a|g|g|t|t|a|t|a|a|g|c|a|c|a|t|g|t|c|c|t|t|g|ei
a|g|g|a|a|a|g|c|t|t|g|a|c|c|c|t|g|g|t|g|g|g|t|t|g|g|t|g|a|c|t|t|c|t|a|t|c|a|c|g|a|t|g|t|c|c|t|a|g|t|t|t|c|t|c|c|g|c|ei
g|g|c|t|t|g|a|t|c|a|g|g|a|a|c|t|a|c|t|g|c|a|g|a|t|c|c|a|g|a|t|c|c|t|g|t|g|g|c|a|g|c|c|c|c|t|t|a|t|t|g|t|t|a|t|a|c|g|ei
g|a|c|c|g|c|t|t|c|c|c|a|t|a|t|g|t|g|g|c|t|c|t|t|c|a|a|g|g|t|a|a|g|t|g|c|t|g|g|g|c|t|a|c|c|t|t|a|g|a|g|t|c|c|t|c|c|a|ei
t|c|c|t|t|g|a|c|c|t|g|g|g|t|t|c|c|c|c|c|t|c|t|c|g|c|a|g|a|a|c|g|a|t|t|c|c|c|t|g|a|t|g|a|g|g|c|a|g|a|t|g|c|g|g|g|a|a|ei
g|c|c|c|t|g|g|c|g|c|c|c|a|g|c|a|c|c|a|t|g|a|a|a|c|a|a|g|g|t|g|a|g|t|c|g|a|g|g|g|g|t|t|g|g|t|g|g|c|c|c|t|c|t|g|c|c|t|ei
c|t|c|g|a|c|g|g|t|g|a|t|g|g|g|g|g|g|c|a|a|c|t|g|c|g|g|g|g|g|a|g|c|t|g|t|g|c|g|t|c|t|t|c|c|c|c|t|t|c|a|c|t|t|t|c|c|t|ei
t|a|g|c|a|c|c|a|g|c|a|g|t|g|g|c|a|g|c|t|t|c|g|a|c|c|a|g|c|c|c|a|g|t|g|g|a|a|c|c|a|c|a|a|c|t|g|c|c|c|t|c|a|a|a|a|g|a|ei
t|a|g|a|t|g|g|t|c|c|t|g|a|g|g|a|a|a|a|g|t|t|t|t|g|c|t|t|g|t|c|t|a|t|t|t|c|t|c|t|c|t|c|t|a|a|c|a|t|a|g|t|t|g|t|c|a|g|ei
t|a|g|a|t|a|c|a|t|c|a|a|c|a|t|g|c|t|g|a|c|c|a|g|c|t|a|g|g|t|g|t|g|t|g|c|c|a|c|a|g|t|t|g|g|g|g|a|g|a|g|a|g|a|t|c|c|c|ei
t|g|g|a|t|t|a|c|a|g|g|c|a|t|g|a|g|c|c|a|c|c|g|g|c|c|g|g|c|c|t|t|a|t|c|a|c|a|t|t|t|a|t|t|a|t|t|t|a|t|t|g|t|t|t|t|t|c|ei
t|c|c|a|g|c|t|t|t|t|c|t|c|a|g|t|c|a|c|t|c|a|g|a|c|c|a|c|a|c|a|g|g|c|c|a|g|g|a|c|c|a|g|a|a|a|t|c|c|c|t|t|t|t|c|a|c|c|ei
t|t|c|c|g|a|a|g|a|c|c|t|t|c|a|g|a|a|a|a|g|a|a|c|g|c|a|c|a|t|a|a|t|g|a|g|a|c|a|c|c|a|t|a|a|a|g|a|a|g|t|t|g|g|t|c|t|g|ei
c|t|c|a|a|t|g|g|a|g|a|c|c|c|c|t|g|g|c|a|c|a|a|a|c|c|c|t|g|c|c|c|t|g|g|a|c|c|c|a|g|a|g|a|a|g|c|t|c|a|a|t|g|t|c|t|t|c|ei
g|a|g|a|g|a|g|a|g|a|c|c|a|g|a|a|a|t|a|a|t|c|t|g|t|t|a|t|g|c|t|t|t|c|c|c|t|c|a|g|c|c|a|g|t|g|t|t|t|a|c|c|a|t|t|g|c|a|ei
c|c|g|t|c|t|t|g|c|t|g|c|t|g|a|t|g|a|c|t|t|t|a|a|t|c|a|a|g|t|a|a|g|t|t|t|g|g|g|g|g|c|t|a|g|a|g|a|g|c|t|g|g|g|g|g|t|c|ei
g|g|a|g|c|c|t|g|a|c|g|c|t|g|c|c|c|g|c|t|c|t|c|c|g|c|a|g|c|t|g|g|c|c|t|t|c|t|g|g|t|c|c|a|a|g|c|a|c|g|t|c|g|g|t|g|a|g|ei
g|g|a|c|c|t|g|c|t|c|t|g|c|g|t|g|g|c|t|c|g|c|c|t|g|c|a|g|t|g|g|g|g|c|a|g|g|t|g|g|a|g|c|t|g|g|g|t|g|g|g|g|g|c|t|c|t|a|ei
a|c|a|c|a|a|c|t|a|c|c|a|g|t|t|g|g|a|g|c|t|c|c|c|c|g|a|c|c|t|t|g|c|a|g|c|g|g|c|g|a|g|g|t|g|a|g|c|g|g|c|g|t|c|g|c|c|c|ei
a|c|c|c|t|t|g|c|c|t|c|c|c|a|c|c|c|t|c|c|g|c|g|g|c|c|a|g|g|t|g|c|c|a|g|a|g|g|a|c|g|a|g|c|t|g|g|t|g|t|c|c|a|c|g|c|t|g|ei
t|a|a|a|t|c|c|t|c|t|c|g|c|t|g|c|g|t|g|g|t|g|a|a|a|a|c|t|g|a|t|g|c|c|t|n|g|a|g|t|c|t|g|t|g|a|c|c|t|g|c|c|t|n|g|g|a|c|ei
c|t|g|g|a|a|g|c|a|c|t|g|g|a|t|g|g|a|a|t|c|t|t|t|t|g|t|c|t|g|t|c|c|t|c|t|c|t|g|g|g|g|a|a|t|c|a|c|c|c|c|a|a|g|g|t|a|t|ei
g|c|g|g|g|a|g|g|c|c|t|c|t|c|t|a|g|g|a|a|a|t|c|g|g|g|a|c|t|c|a|c|a|c|g|t|t|t|a|c|t|a|a|t|g|t|t|g|c|t|g|c|a|g|c|c|c|c|ei
g|a|t|c|a|a|a|a|c|t|t|t|g|c|t|t|c|t|a|t|a|a|a|g|a|a|a|g|a|c|g|g|t|a|a|c|t|g|g|a|a|t|t|t|c|g|c|g|a|a|c|t|t|t|a|g|a|g|ei
t|t|t|t|g|t|c|c|a|t|g|t|c|a|c|t|g|a|t|c|t|t|t|t|g|c|a|a|g|t|g|a|g|t|a|c|c|t|g|g|g|t|g|g|a|g|a|g|g|c|a|t|c|c|a|g|c|t|ei
t|g|a|c|c|t|g|a|t|c|t|c|t|a|c|t|c|t|c|c|c|c|c|g|c|c|a|g|c|t|g|a|g|g|a|g|g|a|g|a|a|c|c|c|g|g|c|c|t|t|c|t|g|g|a|a|c|c|ei
a|t|t|c|t|g|t|c|a|c|g|t|c|t|g|t|c|a|t|g|t|g|t|c|c|c|a|g|t|a|c|c|t|c|c|a|g|a|g|g|t|a|a|c|t|g|t|g|c|t|c|a|c|g|a|a|c|a|ei
c|c|c|c|a|a|g|t|g|t|g|g|t|t|a|t|g|c|c|t|c|c|t|g|t|t|g|c|t|c|c|g|t|a|c|t|c|t|a|a|c|a|t|c|t|a|g|c|t|g|g|c|t|t|c|c|c|t|ei
a|t|g|a|a|g|a|t|c|a|g|g|c|c|c|t|t|c|t|t|c|c|c|c|g|c|a|a|t|a|g|t|c|c|c|c|a|a|t|a|c|g|t|a|g|a|t|t|t|t|t|g|c|t|c|t|t|c|ei
t|g|c|g|g|a|a|a|g|g|a|t|a|a|g|a|c|c|a|a|g|t|c|g|t|t|c|t|t|c|c|a|c|c|a|t|c|t|t|c|t|t|c|c|a|c|t|g|t|g|a|c|c|c|t|c|t|g|ei
c|t|g|g|c|c|t|t|c|c|t|g|g|a|c|a|g|c|a|g|g|g|g|c|c|c|t|g|g|g|a|t|t|c|c|t|g|g|g|t|t|t|c|c|a|g|g|t|a|a|g|t|g|a|t|t|t|t|ei
g|g|c|t|g|g|c|c|t|g|c|g|g|c|g|c|c|t|g|g|g|c|g|t|t|g|a|g|g|t|g|a|g|g|g|a|c|t|c|c|c|c|g|g|c|c|g|c|g|g|a|g|g|a|a|g|g|g|ei
a|a|g|c|a|t|c|a|c|c|c|c|c|c|t|c|t|g|g|c|c|t|t|c|g|c|a|g|g|c|g|g|c|c|g|c|a|t|c|g|a|c|c|a|t|g|g|t|c|a|t|c|a|t|g|a|g|g|ei
c|c|a|c|c|c|t|c|c|a|g|c|c|c|c|c|a|c|c|t|c|c|t|c|g|c|a|g|a|c|a|a|g|c|t|g|g|t|g|t|c|t|a|a|g|a|a|c|t|a|c|c|c|g|g|a|c|c|ei
t|c|c|t|c|c|c|g|c|t|c|a|c|c|c|c|g|c|c|c|g|t|c|c|g|c|a|g|t|g|c|c|t|c|c|c|c|t|g|c|g|g|c|c|c|c|g|g|g|g|g|c|a|a|a|g|g|c|ei
a|a|a|t|a|t|t|t|t|c|a|t|c|c|c|t|a|t|t|t|a|t|t|c|a|c|a|g|t|g|c|t|a|c|a|a|t|g|a|a|a|a|a|g|a|a|g|g|g|t|g|a|g|a|a|g|a|g|ei
c|c|t|c|c|a|t|g|a|c|t|c|a|a|g|g|c|a|c|a|g|a|c|c|c|c|a|g|g|t|a|a|g|a|a|c|a|g|a|g|c|a|a|t|t|g|t|t|t|t|t|t|t|c|c|a|g|t|ei
c|t|a|a|c|a|a|g|t|t|t|t|t|c|t|g|t|a|t|g|t|a|a|t|c|t|a|g|g|t|g|a|a|a|g|a|c|c|c|c|t|g|a|c|a|a|a|a|g|a|c|a|a|t|c|a|t|c|ei
t|c|t|c|t|t|c|c|c|t|t|c|c|c|c|t|c|t|c|t|c|t|t|c|t|t|c|t|t|t|t|c|t|c|t|c|c|t|c|t|t|c|t|c|t|t|c|t|t|t|c|c|t|c|t|c|t|t|ei
g|g|g|c|a|g|a|t|c|t|t|c|a|a|t|c|a|g|t|c|c|t|a|a|c|a|a|g|t|t|t|g|a|c|a|c|a|a|a|a|t|c|g|c|a|c|a|a|c|g|a|t|g|a|c|g|c|a|ei
a|a|a|a|c|t|t|a|t|a|c|t|t|t|a|t|t|t|t|c|c|c|t|t|g|c|a|g|g|a|a|a|a|a|a|t|c|a|t|g|t|c|c|t|a|c|a|t|a|t|g|t|t|c|t|c|a|a|ei
a|t|g|g|a|t|t|c|c|t|t|c|a|a|g|a|a|c|a|t|g|g|t|c|t|c|a|g|g|t|a|a|g|a|t|g|g|c|a|g|g|g|c|t|g|g|g|c|t|c|t|g|g|g|c|t|a|g|ei
t|g|a|c|a|a|a|t|g|a|t|t|a|g|c|t|g|t|g|t|t|c|t|t|a|c|a|g|g|t|c|a|g|a|g|t|g|g|t|g|c|t|g|g|g|a|a|c|a|a|c|t|g|g|g|c|c|a|ei
t|a|t|c|t|g|a|t|t|a|t|g|t|t|t|a|t|t|c|t|t|a|a|t|t|c|a|g|g|g|a|c|a|a|a|a|a|c|t|g|a|t|t|t|c|a|a|a|a|a|c|t|c|g|t|g|c|t|ei
t|a|c|a|g|a|t|c|a|g|g|g|g|a|a|a|a|t|c|t|g|a|a|c|c|t|c|c|t|g|c|c|a|t|g|c|a|g|c|c|t|c|t|a|a|c|c|c|a|c|c|t|g|c|a|c|a|g|ei
a|t|g|c|c|c|c|c|a|t|g|g|a|g|g|a|c|t|g|t|g|t|g|t|t|c|c|a|t|c|c|t|g|g|g|a|a|g|g|g|g|g|c|t|c|a|t|t|c|a|c|a|g|a|g|a|g|a|ei
c|c|c|a|g|t|a|t|g|t|c|g|t|g|a|a|g|t|g|t|a|a|c|a|g|g|c|c|c|t|a|c|a|c|t|c|c|c|c|g|a|c|a|t|c|t|c|t|t|t|c|c|a|c|c|t|g|g|ei
c|c|a|g|c|t|c|c|a|c|t|c|c|g|c|t|g|t|c|g|c|c|c|c|c|g|c|a|t|c|a|c|c|c|g|g|c|t|g|c|a|g|g|a|g|a|a|g|g|a|g|g|a|c|c|t|g|c|ei
a|c|t|c|a|g|c|t|c|a|t|c|t|c|c|a|a|c|a|t|g|g|a|a|t|g|a|c|g|t|g|c|g|a|c|c|c|c|c|g|g|g|c|c|a|a|g|g|g|c|t|g|g|g|g|c|t|g|ei
a|a|t|g|t|a|t|a|t|g|t|a|a|t|a|a|t|t|c|t|t|c|a|t|t|c|a|g|g|a|a|g|a|a|g|a|a|t|t|a|c|a|g|a|a|a|t|a|c|a|t|c|c|a|g|g|a|g|ei
g|t|g|g|c|c|g|t|g|a|a|g|a|t|g|c|t|g|a|a|a|g|a|a|c|g|c|c|t|c|c|c|c|g|a|g|t|g|a|g|c|t|t|c|g|a|g|a|c|c|t|g|c|t|g|t|c|a|ei
a|t|a|t|g|c|a|a|a|a|t|g|t|a|t|a|t|t|t|t|c|t|t|a|t|c|c|t|g|a|c|c|a|t|t|g|a|t|a|c|t|t|a|a|t|g|t|c|c|a|t|g|t|g|a|c|t|c|ei
g|g|t|g|a|g|c|t|g|g|g|a|g|t|t|c|a|g|g|t|g|g|g|t|c|t|c|a|c|a|g|c|c|t|c|c|t|t|c|a|g|a|g|g|c|c|c|c|a|c|c|a|a|t|t|t|c|t|ei
t|c|a|g|c|t|c|c|t|c|c|a|g|t|g|g|c|c|t|g|g|g|c|g|a|a|a|g|g|t|a|a|g|c|a|c|c|c|c|c|t|g|c|c|a|c|c|c|c|g|g|c|c|g|c|c|t|t|ei
t|c|a|a|c|t|a|a|t|t|t|c|a|a|g|a|c|a|a|t|t|t|t|g|g|t|g|g|g|a|a|c|c|c|a|a|a|c|c|c|g|t|c|a|a|t|c|a|a|g|t|c|t|a|c|a|c|t|ei
a|g|g|t|g|t|g|c|a|t|c|a|c|c|t|t|t|g|a|c|c|a|g|c|g|a|c|c|t|g|a|c|c|a|t|c|a|a|g|c|t|g|c|c|a|g|a|c|g|g|a|c|a|t|g|a|a|t|ei
g|c|c|a|g|g|a|a|g|a|t|g|t|t|c|c|c|c|t|c|g|t|a|t|t|c|a|g|g|t|a|a|a|t|c|c|c|a|a|t|a|a|a|t|t|c|t|c|a|g|t|a|a|a|c|t|c|t|ei
a|g|g|c|c|c|a|t|c|c|c|t|a|c|t|c|c|t|c|t|c|c|t|a|a|c|a|g|a|g|g|g|g|a|c|c|t|c|a|c|c|c|c|a|g|a|c|g|a|g|g|t|g|g|t|g|g|c|ei
t|c|t|c|t|t|g|t|c|a|g|c|t|g|t|c|t|t|t|c|a|g|a|g|c|c|t|g|g|t|a|a|g|t|g|g|g|a|c|t|g|t|c|t|g|g|g|t|t|g|g|c|c|c|c|g|c|a|ei
c|t|c|t|g|g|a|c|a|g|g|t|g|g|t|a|a|a|g|a|c|a|c|t|t|g|g|g|g|t|g|a|g|t|c|a|t|c|c|c|t|a|c|t|c|c|c|a|a|c|a|t|c|t|g|g|a|g|ei
a|t|g|c|c|a|g|g|t|t|a|a|a|g|a|g|a|a|a|a|t|g|a|a|g|a|g|a|g|g|a|g|g|c|c|a|g|g|g|a|g|g|g|t|t|g|a|a|t|t|t|a|g|t|g|t|g|c|ei
c|t|a|g|a|g|g|c|c|t|g|a|g|g|a|t|g|a|g|c|t|g|g|a|g|a|g|t|g|a|g|a|g|g|g|g|a|c|a|a|a|a|c|c|c|a|c|c|t|t|g|t|t|g|g|a|g|c|ei
a|t|g|a|g|c|a|g|c|a|a|g|g|g|c|a|a|g|c|t|c|t|a|g|c|t|c|g|g|t|g|a|g|t|a|c|c|g|c|a|g|g|g|g|t|c|t|g|g|c|t|a|g|g|c|a|c|c|ei
g|g|g|t|g|g|g|g|t|g|c|t|g|a|g|c|g|g|c|c|t|c|c|g|g|t|c|t|g|a|g|g|a|c|t|c|a|t|t|t|a|a|g|a|g|a|a|g|g|a|a|a|a|a|g|g|g|t|ei
t|g|c|t|g|t|t|a|c|t|g|t|c|t|a|t|t|t|t|g|c|t|t|t|t|t|a|g|a|t|g|t|a|a|c|a|t|g|t|a|a|c|a|t|t|a|a|g|a|a|t|g|g|c|a|g|a|t|ei
t|g|t|g|c|c|t|g|c|t|c|a|c|c|t|t|c|a|c|c|a|g|c|c|g|c|c|a|c|g|g|c|t|g|g|a|c|c|g|g|a|g|a|c|g|c|t|c|t|g|c|g|g|g|g|c|t|g|ei
g|g|t|a|a|c|a|a|g|g|g|g|a|g|g|g|g|c|c|a|g|g|a|a|a|g|t|t|t|t|t|c|c|t|g|a|t|t|t|a|a|a|c|c|c|a|g|g|c|a|g|c|c|t|g|g|a|t|ei
t|c|t|t|a|a|t|a|a|c|a|a|t|g|c|a|t|t|a|t|a|c|t|t|t|t|a|g|a|a|t|t|a|c|a|a|g|a|a|t|c|c|c|a|a|a|c|t|c|a|c|c|a|g|g|a|t|g|ie
g|a|c|a|g|a|a|a|c|a|a|a|g|a|g|a|c|a|t|t|t|c|t|t|c|a|a|a|a|c|c|c|c|c|c|a|a|a|t|g|c|c|t|t|g|c|a|g|t|c|a|c|t|t|g|g|t|c|ei
c|c|a|a|g|a|a|c|c|t|c|a|t|c|a|t|c|t|t|c|c|t|g|g|g|a|t|g|g|t|g|a|g|t|g|a|g|c|c|a|g|g|c|c|t|t|c|c|a|g|c|c|c|t|g|c|a|g|ei
g|g|c|t|g|c|c|g|g|a|g|c|c|c|c|t|c|a|c|c|c|t|g|g|t|g|g|g|g|t|a|a|g|g|a|g|g|g|g|g|a|t|g|a|g|g|g|g|t|g|a|t|g|t|g|t|c|t|ei
a|a|t|c|a|a|t|g|a|g|a|a|g|g|g|g|c|t|g|c|c|t|g|c|g|a|c|c|a|c|t|g|g|t|t|g|t|g|t|g|g|a|t|c|c|t|t|c|g|g|g|a|a|g|g|a|a|a|ei
c|t|t|t|t|a|c|a|a|a|t|c|a|g|g|g|a|a|t|c|a|a|g|a|c|a|t|a|g|a|a|g|c|c|a|c|g|t|g|c|a|c|t|t|g|t|c|c|a|a|g|t|c|a|a|c|a|t|ei
a|t|t|t|g|c|a|t|t|t|t|a|a|a|a|a|t|t|t|t|c|c|t|a|t|t|a|g|c|a|c|c|a|a|c|t|g|t|g|c|a|c|t|g|a|a|g|a|a|a|t|c|t|t|t|c|a|g|ei
t|g|a|a|t|a|g|a|a|t|c|t|t|a|a|c|t|c|c|t|a|g|a|c|a|c|t|c|t|g|t|g|g|g|g|t|g|g|g|g|a|g|g|a|g|c|a|g|a|t|c|c|a|a|g|t|t|t|ei
a|c|t|t|t|t|g|a|t|c|c|a|c|a|g|t|c|t|g|c|c|t|g|g|c|a|c|a|c|a|a|t|t|g|a|a|a|t|g|c|a|t|c|a|c|a|a|c|a|t|t|g|a|c|a|c|t|g|ei
a|t|a|g|a|t|g|t|g|g|a|a|g|t|t|a|a|t|a|g|c|t|t|t|a|t|t|t|t|a|a|c|c|t|t|g|t|t|a|g|t|a|a|g|a|a|t|g|t|t|t|t|t|a|a|a|a|a|ei
a|a|t|t|t|a|c|t|a|a|g|t|t|g|a|a|g|c|t|t|t|c|g|t|t|t|a|g|a|a|t|t|a|a|a|t|a|t|g|g|g|t|g|a|t|g|t|t|g|a|g|a|a|a|g|g|c|a|ei
c|t|t|a|c|t|c|t|t|t|t|t|t|t|c|c|c|c|c|c|t|t|c|t|a|a|c|c|a|c|c|a|g|t|g|g|t|t|c|a|t|t|t|t|t|a|a|g|g|t|t|t|t|t|t|c|a|t|ei
a|t|c|t|c|a|c|c|g|a|t|c|c|g|c|c|t|t|t|t|c|g|t|c|t|t|c|t|t|t|t|t|a|t|t|c|t|c|t|t|t|a|g|a|c|g|g|a|g|t|t|t|c|a|c|t|c|t|ei
c|t|a|g|g|c|t|c|c|a|g|a|t|a|g|c|c|a|t|a|g|a|a|a|c|c|a|a|a|c|a|c|t|t|t|c|t|g|c|g|t|g|t|g|t|g|a|g|a|a|t|a|a|t|c|a|g|a|ei
t|c|g|a|g|a|c|t|g|g|c|c|a|g|a|t|g|c|t|c|g|t|g|a|t|t|t|g|g|t|a|t|g|a|a|g|c|t|g|c|t|c|a|t|t|a|c|c|t|c|t|t|t|t|g|t|c|t|ei
g|g|a|a|c|c|c|t|g|a|a|g|a|t|a|t|c|c|t|c|t|t|c|c|g|t|c|c|t|g|t|c|a|c|t|c|t|a|t|g|g|g|a|c|t|t|a|c|g|g|c|t|c|t|t|t|g|t|ei
g|g|a|g|t|t|g|g|c|t|g|g|a|g|t|c|a|t|c|c|t|c|t|c|a|c|a|a|t|g|t|g|a|a|a|t|t|g|t|c|a|a|g|t|g|t|a|a|g|c|c|t|c|c|t|c|c|a|ei
a|c|t|g|g|g|c|c|t|g|g|g|c|a|a|a|c|a|t|a|a|t|t|c|g|c|c|g|g|t|a|g|g|t|a|g|c|a|c|a|g|g|g|g|t|g|g|g|g|g|g|t|t|c|a|g|g|t|ei
c|g|c|c|t|t|g|a|g|g|a|g|c|t|a|g|a|c|t|t|g|g|c|a|c|t|a|c|a|a|t|a|g|c|a|t|c|a|a|t|g|g|t|g|c|c|a|t|c|a|c|c|c|a|g|t|t|c|ei
g|t|t|c|a|g|c|c|t|t|t|g|a|c|c|t|t|g|g|a|a|g|t|c|a|g|a|g|t|g|c|c|c|c|t|a|a|g|c|t|t|c|t|g|c|c|c|c|c|t|c|a|g|a|a|c|a|g|ei
a|g|a|t|g|c|t|g|a|g|c|g|a|c|a|g|c|t|a|t|t|g|t|c|t|t|g|g|a|a|a|c|c|c|a|a|g|a|g|g|t|a|c|c|t|t|t|c|t|t|a|t|c|c|g|c|g|a|ei
c|a|g|a|c|a|t|g|a|t|t|t|c|g|g|a|t|t|c|c|c|c|g|g|a|g|g|a|g|t|t|t|g|a|t|g|g|c|c|a|c|c|a|g|t|t|c|c|a|g|a|a|g|a|c|t|c|a|ei
g|t|g|g|c|c|g|g|g|a|g|c|g|g|g|t|c|t|a|c|t|t|c|t|a|a|g|g|g|t|a|c|t|c|a|g|g|g|g|g|t|g|g|t|g|g|g|a|g|a|c|t|g|a|g|c|a|g|ei
t|g|g|g|c|a|a|a|g|g|t|g|g|a|a|a|t|g|a|a|g|a|a|g|a|c|a|a|a|g|a|c|a|g|g|a|a|a|c|g|c|t|g|g|a|a|g|t|c|g|t|t|t|g|g|c|t|t|ei
c|t|t|c|a|t|t|t|a|a|c|t|c|a|a|c|t|a|t|a|g|a|a|t|t|t|a|g|g|c|t|g|g|t|g|c|g|c|a|a|g|t|g|a|c|t|g|c|a|g|t|t|t|t|t|a|c|c|ei
a|t|g|g|c|c|t|a|c|a|t|g|g|g|t|g|t|g|g|g|t|g|c|g|a|a|t|t|t|c|c|g|c|t|n|c|g|g|c|a|g|a|c|a|g|t|t|g|g|g|a|a|c|g|a|t|a|c|ei
t|g|c|g|g|c|g|c|t|a|c|t|a|c|a|a|t|c|a|g|a|g|c|a|g|c|c|g|g|t|g|a|g|t|g|a|c|c|c|c|g|g|c|c|a|g|g|a|g|c|a|g|g|t|c|a|c|g|ei
c|c|c|a|a|g|c|g|g|g|a|t|g|t|g|g|a|g|g|g|c|a|t|g|c|c|c|c|c|c|t|g|a|g|a|t|c|a|a|g|t|a|c|g|g|g|g|a|g|t|c|a|c|t|g|t|g|c|ei
g|t|g|t|c|t|c|a|t|c|a|a|t|a|c|c|a|t|t|g|t|t|a|t|c|t|a|g|g|a|a|a|a|c|g|a|g|t|g|t|g|t|g|c|t|g|g|a|g|a|a|g|g|c|c|t|g|g|ei

## JRip

Decision list:

rules | predicted class
---|---
(POS29 = A) and (POS28 = C) and (POS30 = G) and (POS20 = T) and (POS24 = T) and (POS54 = G)|IE (53.0/0.0)
(POS29 = A) and (POS28 = C) and (POS24 = C) and (POS23 = T) and (POS30 = G) and (POS9 = C)|IE (49.0/0.0)
(POS29 = A) and (POS28 = C) and (POS30 = G) and (POS19 = T) and (POS26 = T) and (POS24 = T)|IE (39.0/0.0)
(POS29 = A) and (POS28 = C) and (POS24 = C) and (POS30 = G) and (POS19 = T) and (POS26 = C)|IE (42.0/0.0)
(POS29 = A) and (POS30 = G) and (POS21 = T) and (POS17 = T) and (POS28 = C) and (POS25 = T)|IE (42.0/0.0)
(POS29 = A) and (POS30 = G) and (POS21 = T) and (POS28 = T) and (POS26 = T)|IE (47.0/0.0)
(POS29 = A) and (POS28 = C) and (POS30 = G) and (POS20 = T) and (POS16 = T) and (POS18 = T)|IE (32.0/0.0)
(POS29 = A) and (POS28 = C) and (POS30 = G) and (POS31 = A) and (POS25 = C)|IE (44.0/0.0)
(POS29 = A) and (POS28 = C) and (POS30 = G) and (POS17 = C) and (POS60 = G) and (POS48 = G)|IE (26.0/0.0)
(POS29 = A) and (POS30 = G) and (POS22 = T) and (POS20 = T) and (POS21 = C)|IE (25.0/0.0)
(POS29 = A) and (POS30 = G) and (POS28 = C) and (POS34 = C) and (POS35 = T) and (POS25 = C)|IE (19.0/0.0)
(POS29 = A) and (POS30 = G) and (POS28 = T) and (POS24 = C) and (POS23 = T)|IE (25.0/0.0)
(POS29 = A) and (POS28 = C) and (POS30 = G) and (POS32 = G) and (POS24 = C)|IE (16.0/0.0)
(POS29 = A) and (POS28 = C) and (POS30 = G) and (POS33 = T) and (POS5 = C)|IE (18.0/0.0)
(POS29 = A) and (POS30 = G) and (POS28 = C) and (POS33 = C) and (POS18 = C) and (POS49 = C)|IE (16.0/0.0)
(POS29 = A) and (POS30 = G) and (POS18 = T) and (POS24 = T) and (POS28 = C) and (POS40 = G)|IE (13.0/0.0)
(POS29 = A) and (POS30 = G) and (POS28 = T) and (POS25 = C)|IE (17.0/0.0)
(POS29 = A) and (POS30 = G) and (POS28 = C) and (POS21 = T) and (POS35 = C) and (POS22 = C)|IE (10.0/0.0)
(POS29 = A) and (POS30 = G) and (POS28 = C) and (POS19 = C) and (POS6 = T) and (POS1 = T)|IE (12.0/0.0)
(POS29 = A) and (POS30 = G) and (POS22 = T) and (POS44 = T) and (POS26 = T)|IE (15.0/0.0)
(POS29 = A) and (POS30 = G) and (POS25 = T) and (POS28 = T) and (POS27 = C)|IE (10.0/0.0)
(POS29 = A) and (POS28 = C) and (POS30 = G) and (POS35 = A) and (POS1 = C) and (POS2 = C)|IE (9.0/0.0)
(POS29 = A) and (POS30 = G) and (POS28 = C) and (POS25 = T) and (POS26 = T) and (POS22 = C)|IE (10.0/0.0)
(POS29 = A) and (POS30 = G) and (POS18 = T) and (POS21 = T) and (POS17 = T) and (POS27 = A)|IE (11.0/0.0)
(POS29 = A) and (POS28 = C) and (POS30 = G) and (POS32 = A) and (POS16 = T) and (POS20 = C)|IE (7.0/0.0)
(POS29 = A) and (POS28 = C) and (POS30 = G) and (POS32 = C) and (POS31 = G) and (POS44 = C)|IE (6.0/0.0)
(POS29 = A) and (POS30 = G) and (POS26 = C) and (POS24 = T) and (POS6 = C)|IE (8.0/0.0)
(POS29 = A) and (POS30 = G) and (POS33 = T) and (POS25 = T) and (POS19 = C)|IE (6.0/0.0)
(POS29 = A) and (POS30 = G) and (POS28 = C) and (POS35 = A) and (POS21 = C) and (POS5 = T)|IE (5.0/0.0)
(POS29 = A) and (POS30 = G) and (POS22 = T) and (POS4 = T) and (POS41 = A) and (POS49 = A)|IE (6.0/0.0)
(POS29 = A) and (POS30 = G) and (POS19 = T) and (POS34 = G) and (POS43 = A)|IE (5.0/0.0)
(POS29 = A) and (POS30 = G) and (POS26 = C) and (POS24 = T) and (POS11 = A) and (POS1 = T)|IE (5.0/0.0)
(POS29 = A) and (POS28 = C) and (POS34 = C) and (POS12 = C) and (POS45 = A)|IE (4.0/0.0)
(POS29 = A) and (POS30 = G) and (POS21 = T) and (POS11 = T) and (POS48 = G)|IE (5.0/0.0)
(POS29 = A) and (POS26 = C) and (POS32 = G) and (POS13 = C) and (POS17 = T)|IE (5.0/0.0)
(POS29 = A) and (POS30 = G) and (POS31 = T) and (POS48 = G) and (POS39 = G)|IE (3.0/0.0)
(POS29 = A) and (POS28 = C) and (POS48 = T) and (POS51 = A) and (POS47 = G)|IE (5.0/0.0)
(POS29 = A) and (POS18 = T) and (POS45 = G) and (POS11 = C) and (POS33 = C)|IE (4.0/0.0)
(POS29 = A) and (POS19 = C) and (POS46 = C) and (POS23 = C) and (POS27 = C) and (POS8 = G)|IE (3.0/0.0)
(POS29 = A) and (POS28 = C) and (POS46 = C) and (POS57 = C) and (POS3 = C) and (POS51 = A)|IE (3.0/0.0)
(POS29 = A) and (POS5 = G) and (POS57 = A) and (POS38 = T) and (POS8 = T)|IE (3.0/0.0)
(POS45 = G) and (POS14 = C) and (POS29 = A) and (POS10 = A)|IE (9.0/6.0)
(POS40 = G) and (POS9 = T) and (POS8 = G) and (POS46 = T) and (POS13 = G)|IE (3.0/0.0)
(POS32 = T) and (POS31 = G) and (POS35 = G) and (POS34 = A)|EI (448.0/0.0)
(POS32 = T) and (POS31 = G) and (POS30 = G) and (POS35 = G) and (POS29 = A)|EI (95.0/0.0)
(POS31 = G) and (POS32 = T) and (POS30 = G) and (POS33 = A) and (POS34 = A)|EI (36.0/0.0)
(POS31 = G) and (POS32 = T) and (POS30 = G) and (POS35 = G) and (POS33 = A)|EI (27.0/0.0)
(POS31 = G) and (POS32 = T) and (POS30 = G) and (POS4 = G) and (POS29 = A)|EI (19.0/0.0)
(POS31 = G) and (POS32 = T) and (POS30 = G) and (POS35 = G) and (POS1 = A)|EI (9.0/0.0)
(POS31 = G) and (POS32 = T) and (POS30 = G) and (POS28 = C) and (POS35 = C)|EI (10.0/0.0)
(POS31 = G) and (POS32 = T) and (POS30 = G) and (POS7 = C) and (POS11 = C)|EI (8.0/0.0)
(POS31 = G) and (POS32 = T) and (POS29 = A) and (POS18 = C) and (POS10 = A)|EI (7.0/0.0)
(POS31 = G) and (POS32 = T) and (POS30 = G) and (POS10 = G) and (POS55 = A)|EI (5.0/0.0)
(POS31 = G) and (POS32 = T) and (POS44 = C) and (POS4 = C) and (POS30 = G)|EI (5.0/0.0)
(POS31 = G) and (POS32 = T) and (POS33 = A) and (POS42 = G) and (POS29 = A)|EI (5.0/0.0)
(POS31 = G) and (POS32 = T) and (POS40 = T) and (POS29 = A) and (POS28 = C)|EI (3.0/0.0)
(POS31 = G) and (POS41 = G) and (POS16 = T) and (POS9 = G) and (POS1 = G)|EI (3.0/0.0)
(POS31 = G) and (POS9 = C) and (POS42 = A) and (POS8 = G) and (POS3 = C)|EI (3.0/0.0)
|N (1491.0/5.0)


## PART

Decision list:

rules | predicted class
---|---
POS30 = C AND POS31 = T|N (120.0)
POS30 = C AND POS31 = C|N (103.0)
POS30 = T AND POS35 = T|N (100.0)
POS30 = A AND POS32 = C|N (93.0)
POS30 = C AND POS31 = A AND POS49 = G|N (34.0)
POS30 = T AND POS35 = A|N (94.0)
POS32 = A AND POS29 = G|N (69.0)
POS30 = A AND POS35 = C|N (66.0)
POS32 = G AND POS29 = T|N (56.0)
POS32 = A AND POS29 = C|N (57.0)
POS31 = T AND POS29 = T|N (38.0)
POS32 = A AND POS29 = T AND POS31 = A|N (22.0)
POS32 = A AND POS29 = T AND POS49 = A|N (11.0)
POS32 = A AND POS30 = A AND POS29 = A|N (27.0)
POS32 = A AND POS29 = T AND POS33 = G|N (8.0)
POS32 = A AND POS29 = T AND POS31 = G|N (7.0)
POS32 = A AND POS29 = A AND POS28 = G AND POS31 = G|N (7.0)
POS32 = A AND POS29 = A AND POS28 = C AND POS18 = C|IE (54.0)
POS31 = T AND POS29 = G|N (27.0)
POS31 = C AND POS29 = C|N (35.0)
POS32 = A AND POS29 = A AND POS28 = T AND POS23 = T|IE (32.0)
POS31 = T AND POS30 = T|N (18.0)
POS31 = T AND POS30 = A AND POS43 = A|N (10.0)
POS31 = T AND POS30 = A AND POS32 = T|N (7.0)
POS31 = T AND POS29 = A AND POS28 = C AND POS19 = C|IE (19.0)
POS32 = A AND POS29 = A AND POS28 = G|N (9.0/1.0)
POS32 = A AND POS29 = A AND POS28 = A AND POS19 = T|N (6.0)
POS32 = A AND POS29 = A AND POS18 = T AND POS28 = C AND POS25 = C|IE (18.0)
POS32 = A AND POS29 = A AND POS24 = T AND POS23 = C|IE (14.0)
POS32 = G AND POS29 = G AND POS10 = G|N (17.0)
POS31 = T AND POS29 = C|N (10.0/1.0)
POS31 = T AND POS28 = T AND POS11 = T|IE (8.0)
POS31 = T AND POS28 = C AND POS42 = C|IE (9.0)
POS31 = T AND POS28 = C AND POS42 = G|IE (7.0)
POS31 = A AND POS29 = C|N (36.0)
POS32 = G AND POS29 = C|N (22.0)
POS31 = A AND POS29 = G|N (36.0)
POS31 = A AND POS29 = T|N (23.0)
POS31 = A AND POS30 = A|N (10.0)
POS31 = A AND POS30 = C AND POS54 = C|N (8.0)
POS31 = A AND POS30 = G AND POS28 = C AND POS25 = C|IE (58.0)
POS32 = G AND POS29 = A AND POS30 = G AND POS28 = C AND POS21 = C AND POS24 = T|IE (22.0)
POS32 = G AND POS29 = A AND POS30 = G AND POS28 = C AND POS21 = T AND POS31 = G|IE (22.0)
POS32 = A AND POS29 = A AND POS18 = T AND POS19 = C|IE (14.0)
POS32 = G AND POS29 = A AND POS30 = G AND POS28 = C AND POS24 = C|IE (31.0)
POS32 = G AND POS29 = G|N (14.0/1.0)
POS31 = A AND POS30 = C|N (11.0/1.0)
POS32 = G AND POS30 = G AND POS28 = T AND POS36 = T|IE (13.0)
POS32 = G AND POS30 = A|N (12.0)
POS31 = A AND POS30 = G AND POS28 = T AND POS43 = A|IE (8.0/1.0)
POS31 = A AND POS30 = G AND POS28 = C AND POS18 = T|IE (27.0)
POS32 = G AND POS28 = G|N (13.0/1.0)
POS32 = G AND POS34 = T|IE (7.0/1.0)
POS32 = G AND POS34 = A AND POS40 = G|IE (6.0/1.0)
POS32 = G AND POS34 = A|IE (7.0/1.0)
POS32 = G AND POS28 = A|N (11.0)
POS32 = G AND POS42 = C|IE (8.0/2.0)
POS32 = C AND POS29 = C|N (19.0)
POS31 = A AND POS25 = T AND POS23 = T|IE (20.0)
POS31 = A AND POS19 = T|IE (12.0/4.0)
POS31 = A AND POS24 = C|N (7.0)
POS31 = A AND POS44 = C|N (6.0/2.0)
POS31 = A|N (9.0/2.0)
POS31 = T AND POS28 = C|IE (8.0/2.0)
POS31 = C AND POS29 = G AND POS28 = G|N (14.0)
POS31 = C AND POS29 = T AND POS30 = G|N (20.0)
POS31 = C AND POS30 = T|N (15.0)
POS32 = G|N (8.0/3.0)
POS32 = C AND POS29 = G AND POS41 = G|N (7.0)
POS32 = C AND POS29 = G AND POS41 = C|N (6.0)
POS32 = C AND POS29 = A AND POS28 = C AND POS25 = T AND POS24 = C|IE (18.0)
POS31 = T|N (11.0/4.0)
POS31 = C AND POS30 = A AND POS54 = A|N (7.0)
POS31 = C AND POS30 = G AND POS29 = A AND POS43 = G AND POS40 = A|IE (16.0)
POS31 = C AND POS30 = G AND POS29 = A AND POS16 = T AND POS24 = C|IE (9.0)
POS32 = T AND POS31 = G AND POS35 = G AND POS34 = A AND POS33 = A|EI (188.0)
POS32 = C AND POS29 = G|N (8.0/1.0)
POS32 = C AND POS28 = C AND POS25 = C AND POS16 = C|IE (25.0)
POS31 = C AND POS30 = G AND POS16 = T AND POS24 = T|IE (9.0)
POS31 = C AND POS30 = G AND POS16 = C AND POS12 = G|N (11.0/5.0)
POS31 = C AND POS30 = G AND POS16 = C|IE (15.0)
POS31 = C AND POS30 = G AND POS53 = C|N (14.0/2.0)
POS32 = T AND POS31 = G AND POS35 = G AND POS30 = G AND POS28 = A|EI (117.0)
POS32 = C AND POS28 = C AND POS44 = C|IE (13.0)
POS32 = A AND POS24 = C|IE (10.0/1.0)
POS32 = T AND POS31 = G AND POS30 = A AND POS35 = G AND POS34 = A|EI (23.0)
POS32 = T AND POS31 = C|IE (12.0/6.0)
POS32 = T AND POS30 = A AND POS29 = A|EI (9.0/4.0)
POS32 = T AND POS30 = C AND POS36 = T|EI (13.0)
POS30 = A|N (12.0/2.0)
POS32 = A AND POS25 = T|IE (7.0)
POS32 = T AND POS30 = C|N (13.0/3.0)
POS32 = A|N (12.0/2.0)
POS32 = T AND POS30 = T AND POS35 = G AND POS1 = A|EI (7.0/1.0)
POS32 = T AND POS30 = T AND POS35 = G|EI (9.0/3.0)
POS30 = G AND POS32 = T AND POS35 = G AND POS25 = G|EI (68.0)
POS30 = G AND POS32 = T AND POS29 = C AND POS33 = G|EI (28.0)
POS30 = G AND POS32 = T AND POS29 = G AND POS35 = G|EI (24.0)
POS30 = T|N (10.0/1.0)
POS32 = T AND POS29 = T AND POS36 = T|EI (15.0)
POS32 = C AND POS53 = A AND POS18 = C|IE (8.0)
POS32 = T AND POS29 = C|EI (9.0/2.0)
POS29 = T AND POS20 = C|EI (6.0/1.0)
POS29 = T|N (9.0/1.0)
POS29 = G AND POS3 = C|N (7.0/3.0)
POS32 = T AND POS29 = A AND POS28 = G AND POS35 = G|EI (24.0)
POS32 = T AND POS29 = G|EI (11.0/4.0)
POS32 = T AND POS28 = T AND POS38 = T|IE (10.0)
POS32 = T AND POS28 = G|EI (13.0/2.0)
POS32 = T AND POS28 = T AND POS53 = C|IE (7.0)
POS32 = T AND POS28 = T|IE (8.0/3.0)
POS32 = T AND POS28 = A AND POS27 = C AND POS3 = C|EI (7.0)
POS32 = T AND POS28 = C AND POS35 = G AND POS24 = G|EI (23.0)
POS32 = T AND POS28 = C AND POS21 = T AND POS35 = C|IE (15.0)
POS32 = T AND POS28 = C AND POS34 = A AND POS21 = A AND POS1 = G|EI (7.0)
POS32 = T AND POS28 = C AND POS34 = A AND POS21 = G AND POS37 = C|EI (9.0)
POS32 = T AND POS28 = C AND POS35 = G AND POS36 = T|EI (15.0)
POS28 = C AND POS32 = T AND POS33 = T|IE (10.0/1.0)
POS32 = T AND POS28 = C AND POS23 = A|EI (12.0)
POS28 = T|IE (10.0/3.0)
POS28 = C AND POS32 = T AND POS33 = C AND POS57 = G|IE (9.0)
POS28 = C AND POS32 = T AND POS17 = G AND POS7 = A|EI (8.0)
POS28 = C AND POS33 = G AND POS24 = T|IE (9.0/1.0)
POS28 = C AND POS33 = G AND POS24 = A|EI (9.0/1.0)
POS28 = C AND POS33 = G AND POS16 = C|IE (8.0)
POS28 = C AND POS32 = C AND POS15 = T|IE (6.0)
POS32 = T AND POS28 = C AND POS33 = G AND POS19 = T|IE (8.0)
POS32 = T AND POS33 = A AND POS55 = T|EI (9.0/1.0)
POS32 = T AND POS28 = C AND POS12 = C|IE (8.0/2.0)
POS32 = T AND POS28 = C AND POS12 = T|IE (8.0)
POS33 = A AND POS14 = A|EI (8.0)
POS32 = C|N (14.0/6.0)
POS56 = A|EI (13.0/7.0)
POS33 = G|EI (8.0/2.0)
|EI (9.0/2.0)


## J48 Decision Tree

* POS30 = G
	* POS32 = T
		* POS31 = G
			* POS35 = G: EI (500.0/22.0)
			* POS35 != G
				* POS29 = A
					* POS33 = A: EI (58.0/9.0)
					* POS33 != A
						* POS28 = A: EI (13.0/6.0)
						* POS28 != A
							* POS23 = A: EI (10.0/3.0)
							* POS23 != A
								* POS26 = A
									* POS23 = T: IE (8.0/1.0)
									* POS23 != T: EI (7.0/2.0)
								* POS26 != A: IE (63.0/4.0)
				* POS29 != A
					* POS3 = A: EI (8.0)
					* POS3 != A: N (22.0/7.0)
		* POS31 != G
			* POS29 = A
				* POS26 = G
					* POS9 = T: IE (7.0)
					* POS9 != T: N (7.0/1.0)
				* POS26 != G: IE (126.0/6.0)
			* POS29 != A: N (44.0)
	* POS32 != T
		* POS29 = A
			* POS28 = G: N (29.0/3.0)
			* POS28 != G
				* POS28 = A
					* POS48 = G: IE (14.0/5.0)
					* POS48 != G: N (26.0/1.0)
				* POS28 != A
					* POS25 = G
						* POS57 = T: N (7.0)
						* POS57 != T
							* POS38 = A: IE (8.0)
							* POS38 != A
								* POS55 = C: N (7.0/2.0)
								* POS55 != C: IE (16.0/3.0)
					* POS25 != G: IE (450.0/26.0)
		* POS29 != A: N (219.0/2.0)
* POS30 != G
	* POS35 = G
		* POS31 = G
			* POS32 = T
				* POS34 = A: EI (109.0)
				* POS34 != A
					* POS29 = A: EI (10.0/3.0)
					* POS29 != A: N (9.0/1.0)
			* POS32 != T: N (55.0)
		* POS31 != G: N (191.0/1.0)
	* POS35 != G: N (846.0/5.0)


## SimpleCart Decision Tree

		* POS30=(C)|(T)|(A)
					* POS35=(A)|(T)|(C)|(N)|(R): N(841.0/5.0)
					* POS35!=(A)|(T)|(C)|(N)|(R)
					* POS31=(T)|(C)|(A)|(N): N(190.0/1.0)
					* POS31!=(T)|(C)|(A)|(N)
					* POS32=(G)|(C)|(A): N(55.0/0.0)
					* POS32!=(G)|(C)|(A): EI(117.0/11.0)
		* POS30!=(C)|(T)|(A)
			* POS32=(G)|(C)|(A)
				* POS29=(T)|(G)|(C): N(217.0/2.0)
				* POS29!=(T)|(G)|(C)
				* POS28=(G)|(A): N(56.0/13.0)
				* POS28!=(G)|(A): IE(447.0/41.0)
			* POS32!=(G)|(C)|(A)
				* POS31=(T)|(C)|(A)
					* POS29=(T)|(G)|(C): N(44.0/0.0)
					* POS29!=(T)|(G)|(C): IE(128.0/12.0)
				* POS31!=(T)|(C)|(A)
					* POS35=(A)|(T)|(C)
							* POS33=(T)|(C)|(G)|(N)
						* POS28=(G)|(A): N(14.0/11.0)
						* POS28!=(G)|(A): IE(70.0/21.0)
							* POS33!=(T)|(C)|(G)|(N): EI(61.0/12.0)
					* POS35!=(A)|(T)|(C): EI(478.0/22.0)


