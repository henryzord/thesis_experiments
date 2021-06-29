# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Children >= 0.5 and Wife_age >= 41.5 | 1 | 0.107754 |
| Children >= 0.5 and Wife_age < 41.5 and Wife_education < 3.5 and Children >= 2.5 and Wife_age < 37.5 | 3 | 0.105172 |
| Children <= 0.5 | 1 | 0.099698 |
| Children >= 0.5 and Wife_age < 41.5 and Wife_education < 3.5 and Children < 2.5 | 1 | 0.089518 |
| Children >= 0.5 and Wife_age < 41.5 and Wife_education >= 3.5 and Children >= 2.5 | 2 | 0.045564 |
| Children >= 0.5 and Wife_age < 41.5 and Wife_education >= 3.5 and Children < 2.5 | 3 | 0.041928 |
| Wife_age > 41.5 and Wife_education > 3.5 and Children > 2.5 and Children <= 7.5 and Wife_working = all | 2 | 0.016849 |
| Wife_age <= 32.5 and Wife_education > 3.5 and Children > 2.5 and Children <= 7.5 and Wife_working = all | 3 | 0.017940 |
| Children >= 0.5 and Wife_age < 41.5 and Wife_education < 3.5 and Children >= 2.5 and Wife_age >= 37.5 | 1 | 0.022978 |
| Wife_age > 32.5 and Wife_age <= 41.5 and Wife_education > 3.5 and Children > 0.5 and Children <= 2.5 and Wife_working = all | 1 | 0.011789 |
| Wife_age > 32.5 and Wife_age <= 41.5 and Wife_education > 2.5 and Wife_education <= 3.5 and Children > 2.5 and Children <= 7.5 and Wife_working = all | 2 | 0.007525 |
| Children > 0.5 and Wife_age <= 41.5 and Wife_education > 3.5 and Children <= 2.5 and Husband_education > 3.5 and Husband_occupation <= 1.5 and Wife_age > 25.5 and Children <= 1.5 | 1 | 0.014492 |
| Children > 0.5 and Wife_age <= 41.5 and Wife_education <= 3.5 and Husband_occupation > 1.5 and Wife_age <= 37.5 and Children <= 2.5 and Husband_occupation <= 3.5 and Wife_age <= 30.5 and Media_exposure <= 0.5 and Husband_occupation > 2.5 and Standard-of-living <= 3.5 and Wife_working > 0.5 and Standard-of-living > 1.5 and Children <= 1.5 and Standard-of-living > 2.5 | 3 | 0.006144 |
| Children > 0.5 and Wife_age <= 41.5 and Wife_education > 3.5 and Children > 2.5 and Wife_age <= 28.5 and Husband_occupation <= 2.5 | 1 | 0.005614 |
| Children > 0.5 and Wife_age <= 41.5 and Wife_education <= 3.5 and Husband_occupation > 1.5 and Wife_age <= 37.5 and Children <= 2.5 and Husband_occupation <= 3.5 and Wife_age <= 30.5 and Media_exposure <= 0.5 and Husband_occupation <= 2.5 and Children > 1.5 and Wife_age <= 26.5 and Wife_education <= 2.5 | 3 | 0.006897 |
| Children > 0.5 and Wife_age <= 41.5 and Wife_education <= 3.5 and Husband_occupation > 1.5 and Wife_age <= 37.5 and Children > 2.5 and Wife_religion > 0.5 and Children <= 5.5 and Standard-of-living <= 2.5 and Husband_education > 1.5 and Wife_working <= 0.5 and Wife_education <= 2.5 | 1 | 0.004731 |
| Children > 0.5 and Wife_age <= 41.5 and Wife_education > 3.5 and Children > 2.5 and Wife_age > 28.5 and Wife_age > 36.5 and Husband_occupation > 2.5 | 3 | 0.004051 |
| Children > 0.5 and Wife_age <= 41.5 and Wife_education <= 3.5 and Husband_occupation > 1.5 and Wife_age <= 37.5 and Children > 2.5 and Wife_religion <= 0.5 and Husband_occupation <= 2.5 | 1 | 0.004731 |
| Children > 0.5 and Wife_age <= 41.5 and Wife_education > 3.5 and Children <= 2.5 and Husband_education > 3.5 and Husband_occupation <= 1.5 and Wife_age <= 25.5 and Children <= 1.5 and Wife_age <= 23.5 | 2 | 0.004762 |
| Children > 0.5 and Wife_age <= 41.5 and Wife_education <= 3.5 and Husband_occupation > 1.5 and Wife_age <= 37.5 and Children <= 2.5 and Husband_occupation <= 3.5 and Wife_age <= 30.5 and Media_exposure <= 0.5 and Husband_occupation > 2.5 and Standard-of-living <= 3.5 and Wife_working > 0.5 and Standard-of-living > 1.5 and Children <= 1.5 and Standard-of-living <= 2.5 and Wife_age > 20.5 | 3 | 0.004614 |
| Children > 0.5 and Wife_age > 41.5 and Children > 1.5 and Wife_education <= 3.5 and Wife_working <= 0.5 and Standard-of-living > 2.5 and Husband_occupation > 2.5 | 3 | 0.004119 |
| Children > 0.5 and Wife_age <= 41.5 and Wife_education > 3.5 and Children <= 2.5 and Husband_education > 3.5 and Husband_occupation <= 1.5 and Wife_age > 25.5 and Children > 1.5 and Wife_working <= 0.5 and Wife_religion > 0.5 and Wife_age <= 32.5 | 2 | 0.003891 |
| Children > 0.5 and Wife_age <= 41.5 and Wife_education > 3.5 and Children > 2.5 and Wife_age > 28.5 and Wife_age > 36.5 and Husband_occupation <= 2.5 and Wife_religion > 0.5 and Husband_occupation > 1.5 | 3 | 0.003211 |
| Children > 0.5 and Wife_age <= 41.5 and Wife_education <= 3.5 and Husband_occupation <= 1.5 and Children > 1.5 and Media_exposure <= 0.5 and Wife_working > 0.5 and Husband_education > 3.5 and Standard-of-living > 3.5 and Children <= 3.5 and Wife_age <= 30.5 | 2 | 0.003505 |
| Children > 0.5 and Wife_age <= 41.5 and Wife_education <= 3.5 and Husband_occupation > 1.5 and Wife_age <= 37.5 and Children <= 2.5 and Husband_occupation <= 3.5 and Wife_age <= 30.5 and Media_exposure <= 0.5 and Husband_occupation <= 2.5 and Children > 1.5 and Wife_age <= 26.5 and Wife_education > 2.5 and Husband_education <= 3.5 | 3 | 0.003609 |
| Children > 0.5 and Wife_age > 41.5 and Children > 1.5 and Wife_education > 3.5 and Wife_working > 0.5 and Standard-of-living > 3.5 and Husband_occupation > 1.5 and Wife_age <= 44.5 | 3 | 0.003211 |
| Children > 0.5 and Wife_age <= 41.5 and Wife_education <= 3.5 and Husband_occupation > 1.5 and Wife_age <= 37.5 and Children > 2.5 and Wife_religion > 0.5 and Children > 5.5 and Media_exposure <= 0.5 and Husband_occupation <= 2.5 and Wife_education > 2.5 | 1 | 0.005249 |
| Children > 0.5 and Wife_age <= 41.5 and Wife_education <= 3.5 and Husband_occupation > 1.5 and Wife_age > 37.5 and Media_exposure <= 0.5 and Children > 2.5 and Husband_education > 3.5 | 3 | 0.002634 |
| Children > 0.5 and Wife_age <= 41.5 and Wife_education <= 3.5 and Husband_occupation > 1.5 and Wife_age <= 37.5 and Children > 2.5 and Wife_religion > 0.5 and Children <= 5.5 and Standard-of-living <= 2.5 and Husband_education > 1.5 and Wife_working > 0.5 and Wife_age <= 33.5 and Children <= 4.5 and Children > 3.5 and Media_exposure > 0.5 | 1 | 0.006545 |
| Children > 0.5 and Wife_age <= 41.5 and Wife_education <= 3.5 and Husband_occupation <= 1.5 and Children > 1.5 and Media_exposure <= 0.5 and Wife_working > 0.5 and Husband_education > 3.5 and Standard-of-living <= 3.5 and Children <= 2.5 | 3 | 0.004119 |
| Children > 0.5 and Wife_age <= 41.5 and Wife_education <= 3.5 and Husband_occupation > 1.5 and Wife_age <= 37.5 and Children > 2.5 and Wife_religion > 0.5 and Children > 5.5 and Media_exposure <= 0.5 and Husband_occupation > 2.5 and Husband_education <= 2.5 | 2 | 0.004049 |
| Children > 0.5 and Wife_age <= 41.5 and Wife_education <= 3.5 and Husband_occupation <= 1.5 and Children > 1.5 and Media_exposure <= 0.5 and Wife_working > 0.5 and Husband_education <= 3.5 | 2 | 0.003190 |
| Children > 0.5 and Wife_age <= 41.5 and Wife_education > 3.5 and Children <= 2.5 and Husband_education > 3.5 and Husband_occupation > 1.5 and Husband_occupation > 2.5 and Wife_working <= 0.5 and Wife_age > 26.5 | 2 | 0.002228 |
| Children > 0.5 and Wife_age > 41.5 and Children > 1.5 and Wife_education > 3.5 and Wife_working > 0.5 and Standard-of-living <= 3.5 and Children <= 5.5 | 3 | 0.002642 |
| Children > 0.5 and Wife_age > 41.5 and Children > 1.5 and Wife_education <= 3.5 and Wife_working > 0.5 and Media_exposure <= 0.5 and Wife_religion > 0.5 and Wife_education > 1.5 and Children > 3.5 and Standard-of-living > 2.5 and Wife_education <= 2.5 and Wife_age <= 44.5 | 2 | 0.003113 |
| Children > 0.5 and Wife_age <= 41.5 and Wife_education > 3.5 and Children > 2.5 and Wife_age > 28.5 and Wife_age <= 36.5 and Standard-of-living <= 3.5 and Wife_working <= 0.5 | 1 | 0.002635 |
| Children > 0.5 and Wife_age <= 41.5 and Wife_education <= 3.5 and Husband_occupation > 1.5 and Wife_age <= 37.5 and Children > 2.5 and Wife_religion > 0.5 and Children <= 5.5 and Standard-of-living <= 2.5 and Husband_education > 1.5 and Wife_working > 0.5 and Wife_age <= 33.5 and Children <= 4.5 and Children <= 3.5 and Media_exposure <= 0.5 and Wife_education <= 2.5 | 1 | 0.003008 |
| Children > 0.5 and Wife_age <= 41.5 and Wife_education <= 3.5 and Husband_occupation > 1.5 and Wife_age <= 37.5 and Children > 2.5 and Wife_religion > 0.5 and Children <= 5.5 and Standard-of-living > 2.5 and Wife_education <= 2.5 and Husband_education > 2.5 and Wife_age <= 23.5 | 1 | 0.004199 |
| Children > 0.5 and Wife_age <= 41.5 and Wife_education <= 3.5 and Husband_occupation <= 1.5 and Children > 1.5 and Media_exposure <= 0.5 and Wife_working > 0.5 and Husband_education > 3.5 and Standard-of-living > 3.5 and Children > 3.5 | 1 | 0.003294 |
| Children > 0.5 and Wife_age <= 41.5 and Wife_education > 3.5 and Children > 2.5 and Wife_age > 28.5 and Wife_age <= 36.5 and Standard-of-living <= 3.5 and Wife_working > 0.5 and Children > 3.5 and Wife_age > 32.5 | 3 | 0.003609 |
| Children > 0.5 and Wife_age <= 41.5 and Wife_education <= 3.5 and Husband_occupation > 1.5 and Wife_age <= 37.5 and Children <= 2.5 and Husband_occupation <= 3.5 and Wife_age <= 30.5 and Media_exposure <= 0.5 and Husband_occupation > 2.5 and Standard-of-living > 3.5 and Wife_working <= 0.5 | 2 | 0.001951 |
| Children > 0.5 and Wife_age <= 41.5 and Wife_education <= 3.5 and Husband_occupation > 1.5 and Wife_age <= 37.5 and Children <= 2.5 and Husband_occupation <= 3.5 and Wife_age <= 30.5 and Media_exposure <= 0.5 and Husband_occupation > 2.5 and Standard-of-living <= 3.5 and Wife_working > 0.5 and Standard-of-living > 1.5 and Children > 1.5 and Standard-of-living > 2.5 and Wife_education > 2.5 and Wife_age > 23.5 | 3 | 0.002642 |
| Children > 0.5 and Wife_age <= 41.5 and Wife_education > 3.5 and Children <= 2.5 and Husband_education > 3.5 and Husband_occupation > 1.5 and Husband_occupation <= 2.5 and Wife_age > 22.5 and Standard-of-living > 3.5 and Wife_working > 0.5 and Wife_age <= 27 | 2 | 0.002597 |
| Children > 0.5 and Wife_age <= 41.5 and Wife_education <= 3.5 and Husband_occupation > 1.5 and Wife_age <= 37.5 and Children <= 2.5 and Husband_occupation <= 3.5 and Wife_age <= 30.5 and Media_exposure <= 0.5 and Husband_occupation > 2.5 and Standard-of-living <= 3.5 and Wife_working > 0.5 and Standard-of-living > 1.5 and Children > 1.5 and Standard-of-living <= 2.5 and Wife_age > 25.5 | 3 | 0.003691 |
| Children > 0.5 and Wife_age <= 41.5 and Wife_education <= 3.5 and Husband_occupation > 1.5 and Wife_age <= 37.5 and Children > 2.5 and Wife_religion > 0.5 and Children > 5.5 and Media_exposure > 0.5 | 1 | 0.003008 |
| Children > 0.5 and Wife_age <= 41.5 and Wife_education > 3.5 and Children <= 2.5 and Husband_education > 3.5 and Husband_occupation <= 1.5 and Wife_age > 25.5 and Children > 1.5 and Wife_working <= 0.5 and Wife_religion <= 0.5 | 2 | 0.001463 |
| Children > 0.5 and Wife_age <= 41.5 and Wife_education <= 3.5 and Husband_occupation > 1.5 and Wife_age > 37.5 and Media_exposure <= 0.5 and Children > 2.5 and Husband_education <= 3.5 and Standard-of-living > 2.5 and Children <= 5.5 | 3 | 0.002081 |
| Children > 0.5 and Wife_age > 41.5 and Children > 1.5 and Wife_education <= 3.5 and Wife_working > 0.5 and Media_exposure <= 0.5 and Wife_religion <= 0.5 and Husband_education <= 3.5 | 2 | 0.001754 |
| Children > 0.5 and Wife_age > 41.5 and Children > 1.5 and Wife_education > 3.5 and Wife_working > 0.5 and Standard-of-living > 3.5 and Husband_occupation <= 1.5 and Wife_religion > 0.5 and Children <= 6.5 and Children <= 3.5 | 3 | 0.001490 |
| Children > 0.5 and Wife_age <= 41.5 and Wife_education > 3.5 and Children > 2.5 and Wife_age > 28.5 and Wife_age <= 36.5 and Standard-of-living > 3.5 and Children <= 4.5 and Husband_occupation > 2.5 | 3 | 0.004157 |
| Children > 0.5 and Wife_age <= 41.5 and Wife_education > 3.5 and Children <= 2.5 and Husband_education > 3.5 and Husband_occupation > 1.5 and Husband_occupation > 2.5 and Wife_working <= 0.5 and Wife_age <= 26.5 | 1 | 0.002368 |
| Children > 0.5 and Wife_age <= 41.5 and Wife_education <= 3.5 and Husband_occupation > 1.5 and Wife_age <= 37.5 and Children > 2.5 and Wife_religion > 0.5 and Children <= 5.5 and Standard-of-living <= 2.5 and Husband_education <= 1.5 | 1 | 0.002635 |
| Children > 0.5 and Wife_age <= 41.5 and Wife_education > 3.5 and Children <= 2.5 and Husband_education > 3.5 and Husband_occupation > 1.5 and Husband_occupation <= 2.5 and Wife_age > 22.5 and Standard-of-living <= 3.5 | 1 | 0.003655 |
| Children > 0.5 and Wife_age <= 41.5 and Wife_education <= 3.5 and Husband_occupation > 1.5 and Wife_age <= 37.5 and Children <= 2.5 and Husband_occupation <= 3.5 and Wife_age <= 30.5 and Media_exposure <= 0.5 and Husband_occupation <= 2.5 and Children <= 1.5 and Wife_education > 2.5 and Wife_age <= 20.5 | 3 | 0.002081 |
| Children > 0.5 and Wife_age > 41.5 and Children > 1.5 and Wife_education > 3.5 and Wife_working > 0.5 and Standard-of-living > 3.5 and Husband_occupation <= 1.5 and Wife_religion > 0.5 and Children > 6.5 | 3 | 0.002081 |
| Children > 0.5 and Wife_age <= 41.5 and Wife_education <= 3.5 and Husband_occupation > 1.5 and Wife_age <= 37.5 and Children > 2.5 and Wife_religion > 0.5 and Children <= 5.5 and Standard-of-living > 2.5 and Wife_education > 2.5 and Husband_education <= 3.5 and Wife_working <= 0.5 | 1 | 0.001976 |
| Children > 0.5 and Wife_age <= 41.5 and Wife_education <= 3.5 and Husband_occupation <= 1.5 and Children > 1.5 and Media_exposure <= 0.5 and Wife_working > 0.5 and Husband_education > 3.5 and Standard-of-living <= 3.5 and Children > 2.5 | 2 | 0.002514 |
| Children > 0.5 and Wife_age <= 41.5 and Wife_education > 3.5 and Children <= 2.5 and Husband_education > 3.5 and Husband_occupation <= 1.5 and Wife_age > 25.5 and Children > 1.5 and Wife_working > 0.5 | 1 | 0.007599 |
| Children > 0.5 and Wife_age <= 41.5 and Wife_education <= 3.5 and Husband_occupation > 1.5 and Wife_age <= 37.5 and Children <= 2.5 and Husband_occupation <= 3.5 and Wife_age <= 30.5 and Media_exposure <= 0.5 and Husband_occupation > 2.5 and Standard-of-living > 3.5 and Wife_working > 0.5 and Children > 1.5 and Husband_education <= 3.5 | 3 | 0.001736 |
| Children > 0.5 and Wife_age <= 41.5 and Wife_education <= 3.5 and Husband_occupation <= 1.5 and Children > 1.5 and Media_exposure > 0.5 | 2 | 0.001463 |
| Children > 0.5 and Wife_age <= 41.5 and Wife_education <= 3.5 and Husband_occupation <= 1.5 and Children > 1.5 and Media_exposure <= 0.5 and Wife_working <= 0.5 | 3 | 0.003609 |
| Wife_age > 32.5 and Wife_age <= 41.5 and Wife_education > 3.5 and Children > 7.5 and Wife_working = all | 3 | 0.001157 |
| Wife_age > 32.5 and Wife_age <= 41.5 and Wife_education <= 2.5 and Children > 7.5 and Wife_working = all | 1 | 0.008191 |
| Wife_age > 32.5 and Wife_age <= 41.5 and Wife_education > 2.5 and Wife_education <= 3.5 and Children > 7.5 and Wife_working = all | 1 | 0.002345 |
| Children > 0.5 and Wife_age > 41.5 and Children > 1.5 and Wife_education > 3.5 and Wife_working <= 0.5 | 2 | 0.009089 |
| Children > 0.5 and Wife_age <= 41.5 and Wife_education > 3.5 and Children > 2.5 and Wife_age > 28.5 and Wife_age <= 36.5 and Standard-of-living > 3.5 and Children <= 4.5 and Husband_occupation <= 2.5 and Wife_working <= 0.5 and Wife_age <= 34 | 3 | 0.007356 |
| Children > 0.5 and Wife_age > 41.5 and Children > 1.5 and Wife_education > 3.5 and Wife_working > 0.5 and Standard-of-living > 3.5 and Husband_occupation <= 1.5 and Wife_religion <= 0.5 | 2 | 0.003891 |
| Wife_age > 32.5 and Wife_age <= 41.5 and Wife_education <= 2.5 and Children > 2.5 and Children <= 7.5 and Wife_working = all | 3 | 0.019413 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Children <= 0.5 | 1 | 0.099698 |
| Wife_age > 41.5 and Children > 1.5 and Wife_education <= 3.5 and Wife_working > 0.5 and Wife_education <= 1.5 | 1 | 0.043356 |
| Wife_education <= 3.5 and Wife_age > 37.5 and Children > 1.5 and Husband_education > 1.5 and Children <= 9.5 and Wife_education > 1.5 and Media_exposure <= 0.5 and Wife_working > 0.5 and Wife_age <= 46.5 and Children > 3.5 and Wife_age > 40.5 | 2 | 0.007214 |
| Wife_education <= 3.5 and Wife_age > 37.5 and Children > 1.5 and Husband_education > 1.5 and Children <= 9.5 and Standard-of-living > 1.5 and Wife_education > 1.5 and Media_exposure <= 0.5 and Wife_working > 0.5 | 1 | 0.037618 |
| Wife_education <= 3.5 and Wife_age > 37.5 and Children > 1.5 and Standard-of-living <= 3.5 | 1 | 0.033181 |
| Wife_education <= 3.5 and Wife_age > 37.5 and Children <= 1.5 | 1 | 0.022280 |
| Wife_education <= 3.5 and Children <= 2.5 and Husband_occupation <= 3.5 and Wife_age > 30.5 | 1 | 0.024563 |
| Wife_education <= 3.5 and Husband_occupation > 1.5 and Children > 2.5 and Husband_education > 1.5 and Wife_age <= 32.5 and Wife_age <= 23.5 and Wife_age > 21.5 | 3 | 0.005970 |
| Wife_education <= 3.5 and Husband_occupation > 1.5 and Children > 2.5 and Husband_education > 1.5 and Wife_age <= 32.5 and Wife_age > 22.5 and Media_exposure <= 0.5 and Standard-of-living <= 2.5 | 3 | 0.037371 |
| Wife_education <= 3.5 and Standard-of-living <= 1.5 and Husband_education <= 3.5 and Children <= 3.5 and Wife_education <= 2.5 and Wife_age <= 25.5 and Wife_age <= 24.5 | 1 | 0.006934 |
| Wife_education <= 3.5 and Children <= 1.5 and Husband_occupation <= 3.5 and Wife_age > 24.5 and Husband_occupation <= 2.5 | 1 | 0.016058 |
| Wife_education <= 3.5 and Husband_occupation > 1.5 and Wife_age <= 24.5 and Media_exposure <= 0.5 and Husband_education > 2.5 and Standard-of-living <= 3.5 and Wife_age > 20.5 and Husband_occupation > 2.5 | 3 | 0.021250 |
| Wife_education <= 3.5 and Husband_occupation > 1.5 and Husband_education > 1.5 and Children > 2.5 and Standard-of-living > 2.5 and Husband_occupation > 2.5 and Wife_religion > 0.5 and Wife_age > 25.5 and Children <= 7.5 and Wife_working > 0.5 and Standard-of-living <= 3.5 | 3 | 0.040630 |
| Wife_education <= 2.5 and Wife_age > 20.5 and Husband_education > 1.5 and Husband_occupation <= 2.5 and Husband_occupation > 1.5 and Children <= 6.5 and Husband_education <= 2.5 | 3 | 0.023984 |
| Wife_education <= 2.5 and Wife_age > 20.5 and Wife_age > 35.5 and Husband_occupation <= 2.5 | 1 | 0.007586 |
| Children <= 2.5 and Wife_age > 41.5 | 1 | 0.018163 |
| Wife_age > 34.5 and Children <= 2.5 and Wife_religion > 0.5 | 1 | 0.006541 |
| Wife_age > 34.5 and Children <= 2.5 | 3 | 0.013832 |
| Wife_age > 34.5 and Wife_age > 47.5 and Children <= 6.5 | 1 | 0.005211 |
| Wife_age > 34.5 and Standard-of-living > 2.5 and Children <= 8.5 and Media_exposure <= 0.5 and Wife_education > 3.5 and Wife_age <= 41.5 and Standard-of-living > 3.5 and Husband_occupation <= 2.5 | 2 | 0.053535 |
| Wife_education <= 2.5 and Wife_age > 23.5 and Wife_working > 0.5 and Children <= 6.5 and Children <= 5.5 and Husband_occupation > 1.5 and Wife_age <= 33.5 and Standard-of-living <= 3.5 | 1 | 0.026058 |
| Husband_occupation > 1.5 and Wife_age <= 28.5 and Wife_age > 27.5 and Husband_education > 3.5 and Children > 1.5 | 3 | 0.010610 |
| Husband_occupation > 1.5 and Children <= 2.5 and Husband_occupation <= 3.5 and Wife_education <= 3.5 and Media_exposure <= 0.5 and Husband_occupation <= 2.5 and Wife_age <= 24.5 | 1 | 0.013225 |
| Wife_education <= 2.5 and Children > 1.5 and Wife_age > 24.5 and Husband_education > 2.5 and Husband_occupation > 1.5 and Wife_working > 0.5 | 3 | 0.057912 |
| Wife_education <= 2.5 and Husband_education > 2.5 and Wife_age > 20.5 and Standard-of-living > 3.5 | 1 | 0.024405 |
| Wife_age <= 28.5 and Wife_age <= 20.5 and Wife_education <= 3.5 | 1 | 0.013342 |
| Media_exposure > 0.5 and Husband_education <= 2.5 | 1 | 0.003656 |
| Children > 2.5 and Husband_occupation > 2.5 and Wife_age <= 29.5 | 3 | 0.019430 |
| Wife_age > 30.5 and Husband_education > 2.5 and Children > 2.5 and Children <= 7.5 and Wife_age <= 32.5 | 3 | 0.026497 |
| Husband_occupation <= 1.5 and Husband_education <= 3.5 and Children <= 5.5 | 2 | 0.012603 |
| Wife_age > 31.5 and Husband_education <= 2.5 and Children > 5.5 | 2 | 0.014423 |
| Husband_occupation > 1.5 and Wife_age <= 29.5 and Wife_age > 20.5 and Wife_age > 22.5 and Wife_education > 2.5 and Children > 1.5 and Standard-of-living <= 3.5 | 3 | 0.020213 |
| Wife_age > 37.5 and Wife_age > 39.5 and Wife_education > 3.5 and Children <= 7.5 and Children > 5.5 | 2 | 0.023840 |
| Wife_age <= 22.5 and Husband_occupation > 2.5 | 3 | 0.027214 |
| Wife_age <= 22.5 and Husband_occupation <= 1.5 | 2 | 0.007913 |
| Standard-of-living <= 2.5 and Wife_age > 24.5 and Children <= 3.5 | 1 | 0.028177 |
| Children > 1.5 and Children > 7.5 | 3 | 0.027814 |
| Wife_age <= 22.5 | 3 | 0.036548 |
| Children > 1.5 and Children > 6.5 | 1 | 0.013788 |
| Children > 1.5 and Husband_education <= 2.5 and Wife_age <= 31.0 | 2 | 0.015481 |
| Children > 1.5 and Standard-of-living > 2.5 and Wife_education <= 3.5 and Wife_age > 34.5 | 3 | 0.033409 |
| Children > 1.5 and Standard-of-living > 2.5 and Children <= 5.5 and Husband_occupation <= 1.5 and Wife_age > 43.5 | 2 | 0.035320 |
| Children > 1.5 and Wife_age > 42.5 | 1 | 0.011121 |
| Children > 1.5 and Husband_occupation > 1.5 and Wife_age <= 31.0 and Children > 2.5 and Wife_working > 0.5 | 3 | 0.007018 |
| Children > 1.5 and Wife_religion <= 0.5 and Children <= 3.5 and Husband_occupation > 1.5 | 3 | 0.020684 |
| Wife_age > 34.5 and Children > 3.5 and Standard-of-living > 2.5 | 2 | 0.041995 |
| Wife_age > 34.5 and Children <= 3.5 | 2 | 0.030371 |
| Children <= 1.5 and Wife_age <= 27.5 and Wife_age <= 26.5 and Wife_age > 24.5 | 1 | 0.017105 |
| Children > 4.5 | 1 | 0.017633 |
| Standard-of-living > 2.5 and Wife_religion <= 0.5 and Wife_age > 27.5 | 1 | 0.032175 |
| Wife_religion <= 0.5 | 2 | 0.066068 |
| Husband_education <= 3.5 and Standard-of-living <= 3.5 | 3 | 0.039794 |
| Wife_age > 23.5 and Wife_age > 26.5 and Husband_occupation <= 2.5 and Husband_occupation <= 1.5 and Children > 1.5 | 2 | 0.050702 |
| Husband_occupation > 2.5 | 2 | 0.118470 |
| Wife_age > 27.5 | 1 | 0.099518 |
| Wife_age > 24.5 | 3 | 0.524607 |
| Husband_occupation <= 1.5 | 3 | 0.025912 |
|  | 1 | 0.529412 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

wife_age|wife_education|children|wife_working|contraceptive_method
---|---|---|---|---
(32.5-41.5]|(3.5-inf)|(7.5-inf)|all|3
(41.5-inf)|(3.5-inf)|(7.5-inf)|all|3
(41.5-inf)|(2.5-3.5]|(7.5-inf)|all|1
(32.5-41.5]|(2.5-3.5]|(7.5-inf)|all|1
(32.5-41.5]|(-inf-2.5]|(7.5-inf)|all|1
(-inf-32.5]|(-inf-2.5]|(7.5-inf)|all|3
(41.5-inf)|(-inf-2.5]|(7.5-inf)|all|1
(-inf-32.5]|(3.5-inf)|(2.5-7.5]|all|3
(41.5-inf)|(3.5-inf)|(2.5-7.5]|all|2
(32.5-41.5]|(3.5-inf)|(2.5-7.5]|all|2
(41.5-inf)|(2.5-3.5]|(2.5-7.5]|all|1
(-inf-32.5]|(2.5-3.5]|(2.5-7.5]|all|3
(32.5-41.5]|(2.5-3.5]|(2.5-7.5]|all|2
(41.5-inf)|(3.5-inf)|(0.5-2.5]|all|1
(41.5-inf)|(-inf-2.5]|(2.5-7.5]|all|1
(32.5-41.5]|(-inf-2.5]|(2.5-7.5]|all|3
(-inf-32.5]|(3.5-inf)|(0.5-2.5]|all|3
(32.5-41.5]|(3.5-inf)|(0.5-2.5]|all|1
(-inf-32.5]|(-inf-2.5]|(2.5-7.5]|all|3
(41.5-inf)|(2.5-3.5]|(0.5-2.5]|all|1
(32.5-41.5]|(2.5-3.5]|(0.5-2.5]|all|1
(-inf-32.5]|(2.5-3.5]|(0.5-2.5]|all|1
(41.5-inf)|(3.5-inf)|(-inf-0.5]|all|1
(32.5-41.5]|(-inf-2.5]|(0.5-2.5]|all|1
(41.5-inf)|(-inf-2.5]|(0.5-2.5]|all|1
(32.5-41.5]|(3.5-inf)|(-inf-0.5]|all|1
(-inf-32.5]|(3.5-inf)|(-inf-0.5]|all|1
(-inf-32.5]|(-inf-2.5]|(0.5-2.5]|all|1
(41.5-inf)|(2.5-3.5]|(-inf-0.5]|all|1
(32.5-41.5]|(2.5-3.5]|(-inf-0.5]|all|1
(-inf-32.5]|(2.5-3.5]|(-inf-0.5]|all|1
(41.5-inf)|(-inf-2.5]|(-inf-0.5]|all|1
(32.5-41.5]|(-inf-2.5]|(-inf-0.5]|all|1
(-inf-32.5]|(-inf-2.5]|(-inf-0.5]|all|1

## PART

Decision list:

rules | predicted class
---|---
Children <= 0.5|1 (88.0/2.0)
Wife_age > 41.5 AND Children > 1.5 AND Wife_education <= 3.5 AND Wife_working > 0.5 AND Wife_education <= 1.5|1 (42.0/4.0)
Wife_education <= 3.5 AND Wife_age > 37.5 AND Children > 1.5 AND Husband_education > 1.5 AND Children <= 9.5 AND Wife_education > 1.5 AND Media_exposure <= 0.5 AND Wife_working > 0.5 AND Wife_age <= 46.5 AND Children > 3.5 AND Wife_age > 40.5|2 (26.0/13.0)
Wife_education <= 3.5 AND Wife_age > 37.5 AND Children > 1.5 AND Husband_education > 1.5 AND Children <= 9.5 AND Standard-of-living > 1.5 AND Wife_education > 1.5 AND Media_exposure <= 0.5 AND Wife_working > 0.5|1 (51.0/17.0)
Wife_education <= 3.5 AND Wife_age > 37.5 AND Children > 1.5 AND Standard-of-living <= 3.5|1 (46.0/7.0)
Wife_education <= 3.5 AND Wife_age > 37.5 AND Children <= 1.5|1 (17.0)
Wife_education <= 3.5 AND Children <= 2.5 AND Husband_occupation <= 3.5 AND Wife_age > 30.5|1 (36.0/9.0)
Wife_education <= 3.5 AND Husband_occupation > 1.5 AND Children > 2.5 AND Husband_education > 1.5 AND Wife_age <= 32.5 AND Wife_age <= 23.5 AND Wife_age > 21.5|3 (10.0/4.0)
Wife_education <= 3.5 AND Husband_occupation > 1.5 AND Children > 2.5 AND Husband_education > 1.5 AND Wife_age <= 32.5 AND Wife_age > 22.5 AND Media_exposure <= 0.5 AND Standard-of-living <= 2.5|3 (47.0/14.0)
Wife_education <= 3.5 AND Standard-of-living <= 1.5 AND Husband_education <= 3.5 AND Children <= 3.5 AND Wife_education <= 2.5 AND Wife_age <= 25.5 AND Wife_age <= 24.5|1 (12.0/5.0)
Wife_education <= 3.5 AND Children <= 1.5 AND Husband_occupation <= 3.5 AND Wife_age > 24.5 AND Husband_occupation <= 2.5|1 (17.0/3.0)
Wife_education <= 3.5 AND Husband_occupation > 1.5 AND Wife_age <= 24.5 AND Media_exposure <= 0.5 AND Husband_education > 2.5 AND Standard-of-living <= 3.5 AND Wife_age > 20.5 AND Husband_occupation > 2.5|3 (35.0/15.0)
Wife_education <= 3.5 AND Husband_occupation > 1.5 AND Husband_education > 1.5 AND Children > 2.5 AND Standard-of-living > 2.5 AND Husband_occupation > 2.5 AND Wife_religion > 0.5 AND Wife_age > 25.5 AND Children <= 7.5 AND Wife_working > 0.5 AND Standard-of-living <= 3.5|3 (30.0/4.0)
Wife_education <= 2.5 AND Wife_age > 20.5 AND Husband_education > 1.5 AND Husband_occupation <= 2.5 AND Husband_occupation > 1.5 AND Children <= 6.5 AND Husband_education <= 2.5|3 (16.0/1.0)
Wife_education <= 2.5 AND Wife_age > 20.5 AND Wife_age > 35.5 AND Husband_occupation <= 2.5|1 (17.0/6.0)
Children <= 2.5 AND Wife_age > 41.5|1 (16.0/1.0)
Wife_age > 34.5 AND Children <= 2.5 AND Wife_religion > 0.5|1 (20.0/10.0)
Wife_age > 34.5 AND Children <= 2.5|3 (10.0/4.0)
Wife_age > 34.5 AND Wife_age > 47.5 AND Children <= 6.5|1 (9.0/3.0)
Wife_age > 34.5 AND Standard-of-living > 2.5 AND Children <= 8.5 AND Media_exposure <= 0.5 AND Wife_education > 3.5 AND Wife_age <= 41.5 AND Standard-of-living > 3.5 AND Husband_occupation <= 2.5|2 (74.0/26.0)
Wife_education <= 2.5 AND Wife_age > 23.5 AND Wife_working > 0.5 AND Children <= 6.5 AND Children <= 5.5 AND Husband_occupation > 1.5 AND Wife_age <= 33.5 AND Standard-of-living <= 3.5|1 (30.0/13.0)
Husband_occupation > 1.5 AND Wife_age <= 28.5 AND Wife_age > 27.5 AND Husband_education > 3.5 AND Children > 1.5|3 (12.0/4.0)
Husband_occupation > 1.5 AND Children <= 2.5 AND Husband_occupation <= 3.5 AND Wife_education <= 3.5 AND Media_exposure <= 0.5 AND Husband_occupation <= 2.5 AND Wife_age <= 24.5|1 (25.0/11.0)
Wife_education <= 2.5 AND Children > 1.5 AND Wife_age > 24.5 AND Husband_education > 2.5 AND Husband_occupation > 1.5 AND Wife_working > 0.5|3 (40.0/13.0)
Wife_education <= 2.5 AND Husband_education > 2.5 AND Wife_age > 20.5 AND Standard-of-living > 3.5|1 (23.0/8.0)
Wife_age <= 28.5 AND Wife_age <= 20.5 AND Wife_education <= 3.5|1 (24.0/9.0)
Media_exposure > 0.5 AND Husband_education <= 2.5|1 (8.0/3.0)
Children > 2.5 AND Husband_occupation > 2.5 AND Wife_age <= 29.5|3 (23.0/7.0)
Wife_age > 30.5 AND Husband_education > 2.5 AND Children > 2.5 AND Children <= 7.5 AND Wife_age <= 32.5|3 (36.0/16.0)
Husband_occupation <= 1.5 AND Husband_education <= 3.5 AND Children <= 5.5|2 (8.0/2.0)
Wife_age > 31.5 AND Husband_education <= 2.5 AND Children > 5.5|2 (8.0/3.0)
Husband_occupation > 1.5 AND Wife_age <= 29.5 AND Wife_age > 20.5 AND Wife_age > 22.5 AND Wife_education > 2.5 AND Children > 1.5 AND Standard-of-living <= 3.5|3 (30.0/11.0)
Wife_age > 37.5 AND Wife_age > 39.5 AND Wife_education > 3.5 AND Children <= 7.5 AND Children > 5.5|2 (16.0/4.0)
Wife_age <= 22.5 AND Husband_occupation > 2.5|3 (18.0/7.0)
Wife_age <= 22.5 AND Husband_occupation <= 1.5|2 (15.0/8.0)
Standard-of-living <= 2.5 AND Wife_age > 24.5 AND Children <= 3.5|1 (20.0/8.0)
Children > 1.5 AND Children > 7.5|3 (15.0/6.0)
Wife_age <= 22.5|3 (12.0/4.0)
Children > 1.5 AND Children > 6.5|1 (10.0/6.0)
Children > 1.5 AND Husband_education <= 2.5 AND Wife_age <= 31.0|2 (6.0/2.0)
Children > 1.5 AND Standard-of-living > 2.5 AND Wife_education <= 3.5 AND Wife_age > 34.5|3 (22.0/8.0)
Children > 1.5 AND Standard-of-living > 2.5 AND Children <= 5.5 AND Husband_occupation <= 1.5 AND Wife_age > 43.5|2 (19.0/7.0)
Children > 1.5 AND Wife_age > 42.5|1 (17.0/10.0)
Children > 1.5 AND Husband_occupation > 1.5 AND Wife_age <= 31.0 AND Children > 2.5 AND Wife_working > 0.5|3 (9.0/3.0)
Children > 1.5 AND Wife_religion <= 0.5 AND Children <= 3.5 AND Husband_occupation > 1.5|3 (19.0/6.0)
Wife_age > 34.5 AND Children > 3.5 AND Standard-of-living > 2.5|2 (18.0/7.0)
Wife_age > 34.5 AND Children <= 3.5|2 (10.0/3.0)
Children <= 1.5 AND Wife_age <= 27.5 AND Wife_age <= 26.5 AND Wife_age > 24.5|1 (21.0/10.0)
Children > 4.5|1 (25.0/15.0)
Standard-of-living > 2.5 AND Wife_religion <= 0.5 AND Wife_age > 27.5|1 (19.0/10.0)
Wife_religion <= 0.5|2 (9.0/3.0)
Husband_education <= 3.5 AND Standard-of-living <= 3.5|3 (8.0/2.0)
Wife_age > 23.5 AND Wife_age > 26.5 AND Husband_occupation <= 2.5 AND Husband_occupation <= 1.5 AND Children > 1.5|2 (48.0/26.0)
Husband_occupation > 2.5|2 (26.0/13.0)
Wife_age > 27.5|1 (18.0/9.0)
Wife_age > 24.5|3 (17.0/7.0)
Husband_occupation <= 1.5|3 (13.0/7.0)
|1 (8.0/4.0)


## J48 Decision Tree

* Children <= 0.5: 1 (88.0/2.0)
* Children > 0.5
	* Wife_age <= 41.5
		* Wife_education <= 3.5
			* Husband_occupation <= 1.5
				* Children <= 1.5: 1 (7.0/3.0)
				* Children > 1.5
					* Media_exposure <= 0.5
						* Wife_working <= 0.5: 3 (8.0/3.0)
						* Wife_working > 0.5
							* Husband_education <= 3.5: 2 (11.0/5.0)
							* Husband_education > 3.5
								* Standard-of-living <= 3.5
									* Children <= 2.5: 3 (7.0/2.0)
									* Children > 2.5: 2 (14.0/8.0)
								* Standard-of-living > 3.5
									* Children <= 3.5
										* Wife_age <= 30.5: 2 (10.0/4.0)
										* Wife_age > 30.5: 1 (5.0/2.0)
									* Children > 3.5: 1 (10.0/5.0)
					* Media_exposure > 0.5: 2 (6.0/3.0)
			* Husband_occupation > 1.5
				* Wife_age <= 37.5
					* Children <= 2.5
						* Husband_occupation <= 3.5
							* Wife_age <= 30.5
								* Media_exposure <= 0.5
									* Husband_occupation <= 2.5
										* Children <= 1.5
											* Wife_education <= 2.5: 1 (12.0/2.0)
											* Wife_education > 2.5
												* Wife_age <= 20.5: 3 (5.0/2.0)
												* Wife_age > 20.5: 1 (12.0/4.0)
										* Children > 1.5
											* Wife_age <= 26.5
												* Wife_education <= 2.5: 3 (6.0)
												* Wife_education > 2.5
													* Husband_education <= 3.5: 3 (8.0/3.0)
													* Husband_education > 3.5: 1 (7.0/3.0)
											* Wife_age > 26.5: 1 (7.0/4.0)
									* Husband_occupation > 2.5
										* Standard-of-living <= 3.5
											* Wife_working <= 0.5: 1 (8.0/4.0)
											* Wife_working > 0.5
												* Standard-of-living <= 1.5: 1 (20.0/8.0)
												* Standard-of-living > 1.5
													* Children <= 1.5
														* Standard-of-living <= 2.5
															* Wife_age <= 20.5: 1 (6.0/3.0)
															* Wife_age > 20.5: 3 (9.0/3.0)
														* Standard-of-living > 2.5: 3 (12.0/4.0)
													* Children > 1.5
														* Standard-of-living <= 2.5
															* Wife_age <= 25.5: 1 (6.0/2.0)
															* Wife_age > 25.5: 3 (5.0/1.0)
														* Standard-of-living > 2.5
															* Wife_education <= 2.5: 1 (7.0/3.0)
															* Wife_education > 2.5
																* Wife_age <= 23.5: 1 (5.0/2.0)
																* Wife_age > 23.5: 3 (7.0/3.0)
										* Standard-of-living > 3.5
											* Wife_working <= 0.5: 2 (8.0/4.0)
											* Wife_working > 0.5
												* Children <= 1.5: 1 (8.0/2.0)
												* Children > 1.5
													* Husband_education <= 3.5: 3 (6.0/3.0)
													* Husband_education > 3.5: 1 (5.0/1.0)
								* Media_exposure > 0.5: 1 (9.0/4.0)
							* Wife_age > 30.5: 1 (26.0/6.0)
						* Husband_occupation > 3.5: 1 (8.0/3.0)
					* Children > 2.5
						* Wife_religion <= 0.5
							* Husband_occupation <= 2.5: 1 (10.0/4.0)
							* Husband_occupation > 2.5: 3 (10.0/4.0)
						* Wife_religion > 0.5
							* Children <= 5.5
								* Standard-of-living <= 2.5
									* Husband_education <= 1.5: 1 (8.0/4.0)
									* Husband_education > 1.5
										* Wife_working <= 0.5
											* Wife_education <= 2.5: 1 (10.0/4.0)
											* Wife_education > 2.5: 3 (7.0/2.0)
										* Wife_working > 0.5
											* Wife_age <= 33.5
												* Children <= 4.5
													* Children <= 3.5
														* Media_exposure <= 0.5
															* Wife_education <= 2.5: 1 (7.0/3.0)
															* Wife_education > 2.5: 3 (11.0/3.0)
														* Media_exposure > 0.5: 3 (5.0)
													* Children > 3.5
														* Media_exposure <= 0.5: 3 (14.0/4.0)
														* Media_exposure > 0.5: 1 (5.0)
												* Children > 4.5: 3 (5.0/2.0)
											* Wife_age > 33.5: 3 (6.0/3.0)
								* Standard-of-living > 2.5
									* Wife_education <= 2.5
										* Husband_education <= 2.5: 3 (17.0/5.0)
										* Husband_education > 2.5
											* Wife_age <= 23.5: 1 (5.0/1.0)
											* Wife_age > 23.5: 3 (42.0/10.0)
									* Wife_education > 2.5
										* Husband_education <= 3.5
											* Wife_working <= 0.5: 1 (6.0/3.0)
											* Wife_working > 0.5: 3 (15.0/4.0)
										* Husband_education > 3.5: 3 (22.0/4.0)
							* Children > 5.5
								* Media_exposure <= 0.5
									* Husband_occupation <= 2.5
										* Wife_education <= 2.5: 3 (13.0/5.0)
										* Wife_education > 2.5: 1 (9.0/3.0)
									* Husband_occupation > 2.5
										* Husband_education <= 2.5: 2 (6.0/1.0)
										* Husband_education > 2.5: 3 (26.0/10.0)
								* Media_exposure > 0.5: 1 (7.0/3.0)
				* Wife_age > 37.5
					* Media_exposure <= 0.5
						* Children <= 2.5: 1 (9.0/1.0)
						* Children > 2.5
							* Husband_education <= 3.5
								* Standard-of-living <= 2.5: 1 (7.0/1.0)
								* Standard-of-living > 2.5
									* Children <= 5.5: 3 (5.0/2.0)
									* Children > 5.5: 1 (6.0/2.0)
							* Husband_education > 3.5: 3 (11.0/6.0)
					* Media_exposure > 0.5: 1 (11.0)
		* Wife_education > 3.5
			* Children <= 2.5
				* Husband_education <= 3.5: 3 (9.0/1.0)
				* Husband_education > 3.5
					* Husband_occupation <= 1.5
						* Wife_age <= 25.5
							* Children <= 1.5
								* Wife_age <= 23.5: 2 (10.0/3.0)
								* Wife_age > 23.5: 3 (14.0/7.0)
							* Children > 1.5: 3 (9.0/4.0)
						* Wife_age > 25.5
							* Children <= 1.5: 1 (26.0/9.0)
							* Children > 1.5
								* Wife_working <= 0.5
									* Wife_religion <= 0.5: 2 (6.0/3.0)
									* Wife_religion > 0.5
										* Wife_age <= 32.5: 2 (9.0/3.0)
										* Wife_age > 32.5: 1 (7.0/4.0)
								* Wife_working > 0.5: 1 (25.0/13.0)
					* Husband_occupation > 1.5
						* Husband_occupation <= 2.5
							* Wife_age <= 22.5: 3 (11.0/4.0)
							* Wife_age > 22.5
								* Standard-of-living <= 3.5: 1 (9.0/4.0)
								* Standard-of-living > 3.5
									* Wife_working <= 0.5: 3 (10.0/4.0)
									* Wife_working > 0.5
										* Wife_age <= 27: 2 (6.0/2.0)
										* Wife_age > 27: 3 (6.0/3.0)
						* Husband_occupation > 2.5
							* Wife_working <= 0.5
								* Wife_age <= 26.5: 1 (5.0/2.0)
								* Wife_age > 26.5: 2 (7.0/3.0)
							* Wife_working > 0.5: 3 (34.0/15.0)
			* Children > 2.5
				* Wife_age <= 28.5
					* Husband_occupation <= 2.5: 1 (15.0/7.0)
					* Husband_occupation > 2.5: 3 (12.0/2.0)
				* Wife_age > 28.5
					* Wife_age <= 36.5
						* Standard-of-living <= 3.5
							* Wife_working <= 0.5: 1 (8.0/4.0)
							* Wife_working > 0.5
								* Children <= 3.5: 2 (7.0)
								* Children > 3.5
									* Wife_age <= 32.5: 2 (5.0/2.0)
									* Wife_age > 32.5: 3 (8.0/3.0)
						* Standard-of-living > 3.5
							* Children <= 4.5
								* Husband_occupation <= 2.5
									* Wife_working <= 0.5
										* Wife_age <= 34: 3 (10.0/2.0)
										* Wife_age > 34: 2 (5.0/2.0)
									* Wife_working > 0.5: 2 (37.0/20.0)
								* Husband_occupation > 2.5: 3 (10.0/4.0)
							* Children > 4.5: 2 (11.0/4.0)
					* Wife_age > 36.5
						* Husband_occupation <= 2.5
							* Wife_religion <= 0.5: 2 (15.0/1.0)
							* Wife_religion > 0.5
								* Husband_occupation <= 1.5: 2 (28.0/7.0)
								* Husband_occupation > 1.5: 3 (9.0/4.0)
						* Husband_occupation > 2.5: 3 (14.0/7.0)
	* Wife_age > 41.5
		* Children <= 1.5: 1 (23.0)
		* Children > 1.5
			* Wife_education <= 3.5
				* Wife_working <= 0.5
					* Standard-of-living <= 2.5: 1 (9.0/1.0)
					* Standard-of-living > 2.5
						* Husband_occupation <= 2.5: 1 (10.0/3.0)
						* Husband_occupation > 2.5: 3 (7.0/2.0)
				* Wife_working > 0.5
					* Media_exposure <= 0.5
						* Wife_religion <= 0.5
							* Husband_education <= 3.5: 2 (5.0/2.0)
							* Husband_education > 3.5: 1 (6.0/1.0)
						* Wife_religion > 0.5
							* Wife_education <= 1.5: 1 (23.0/3.0)
							* Wife_education > 1.5
								* Children <= 3.5: 1 (9.0/1.0)
								* Children > 3.5
									* Standard-of-living <= 2.5: 1 (7.0/1.0)
									* Standard-of-living > 2.5
										* Wife_education <= 2.5
											* Wife_age <= 44.5: 2 (5.0/1.0)
											* Wife_age > 44.5: 1 (5.0/2.0)
										* Wife_education > 2.5: 1 (20.0/7.0)
					* Media_exposure > 0.5: 1 (24.0/2.0)
			* Wife_education > 3.5
				* Wife_working <= 0.5: 2 (18.0/5.0)
				* Wife_working > 0.5
					* Standard-of-living <= 3.5
						* Children <= 5.5: 3 (7.0/3.0)
						* Children > 5.5: 1 (7.0/3.0)
					* Standard-of-living > 3.5
						* Husband_occupation <= 1.5
							* Wife_religion <= 0.5: 2 (9.0/3.0)
							* Wife_religion > 0.5
								* Children <= 6.5
									* Children <= 3.5: 3 (7.0/4.0)
									* Children > 3.5: 2 (14.0/5.0)
								* Children > 6.5: 3 (5.0/2.0)
						* Husband_occupation > 1.5
							* Wife_age <= 44.5: 3 (9.0/4.0)
							* Wife_age > 44.5: 1 (5.0/2.0)


## SimpleCart Decision Tree

* Children < 0.5: 1(86.0/2.0)
* Children >= 0.5
	* Wife_age < 41.5
		* Wife_education < 3.5
			* Children < 2.5: 1(131.0/117.0)
			* Children >= 2.5
				* Wife_age < 37.5: 3(170.0/136.0)
				* Wife_age >= 37.5: 1(30.0/21.0)
		* Wife_education >= 3.5
			* Children < 2.5: 3(84.0/119.0)
			* Children >= 2.5: 2(95.0/99.0)
	* Wife_age >= 41.5: 1(143.0/91.0)


