library("gapminder", lib.loc="/Library/Frameworks/R.framework/Versions/3.4/Resources/library")

# Exporting the Gapminder dataset to csv format, to use in Python
# Export whole dataset
write.csv(gapminder, file = "gapminder.csv", row.names = FALSE)

# Splitting the dataset into the Training set and Test set
# install.packages('caTools')
library(caTools)
set.seed(004)
split = sample.split(gapminder$lifeExp, SplitRatio = 0.02)
gapminder_mini = subset(gapminder, split == TRUE)

write.csv(gapminder_mini, file = "gapminder_mini.csv", row.names = FALSE)

## Making a file with only 2007 data

gapminder2007 = gapminder[gapminder$year == 2007,]
write.csv(gapminder_mini, file = "gapminder_2007.csv", row.names = FALSE)
