install.packages("tidyverse")
install.packages("infer")
library(tidyverse)
library(infer)
times = read_csv(file.choose())
s=sd(times$Times)
x_bar = mean(times$Times)
#point+STD_ERR*crit_val
crit_val = qt(.995, 199)
std_err = s/sqrt(200)
lower = x_bar - std_err * crit_val;
upper = x_bar + std_err * crit_val;
lower
upper
