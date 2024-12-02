# Libraries
library(ggplot2)
library(dplyr)
library(GGally)
library(purrr)
library(car)

# Importing Data
setwd("/Users/mainuser/R Linear Regression")
data <- read.csv("./School Project/spending.csv")

# Reviewing Data
str(data)
summary(data)

# Create New Variables
spending <- data %>%
  mutate(
    total_income = monthly_income + financial_aid,
    total_spending = (tuition / 4) + housing + food + transportation +
      books_supplies + entertainment + personal_care +
      technology + health_wellness + miscellaneous
  )

# Create a Scatter Plot to Visualize the Relationship Between Income and Spending
ggplot(spending, aes(x = total_income, y = total_spending)) +
  geom_point(color = "green") +  
  ggtitle("Income vs Spending") +  
  xlab("Monthly Income") +  
  ylab("Monthly Spending")  

# Create a Pairplot on Income and Spending Variables
ggpairs(spending[c("total_income",
                   "total_spending",
                   "housing",
                   "food",
                   "entertainment")],
        aes(color = spending$gender),
        title = "Pairplot of Income and Spending Variables")

# 1. Is Income a Predictor of Total Spending?
model_income <- lm(total_spending ~ total_income, data = spending)
summary(model_income)

ggplot(spending, aes(x = total_income, y = total_spending)) +
  geom_point(color = "blue") +
  geom_smooth(method = "lm", color = "red", se = TRUE) +
  ggtitle("Income vs Spending with Regression Line") +
  xlab("Total Income") +
  ylab("Total Spending")

plot(model_income, which = 1)
plot(model_income, which = 2)





