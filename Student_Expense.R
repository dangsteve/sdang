# ====== 1. Is Income a Predictor of Total Spending? ======
library(tidyr)
library(ggplot2)
library(dplyr)

# Import Data and Create Total Variables
setwd("/Users/mainuser/R Linear Regression")
data <- read.csv("./School Project/spending.csv")

spending <- data %>%
  mutate(
    total_income = monthly_income + financial_aid,
    total_spending = (tuition / 4) + housing + food + transportation +
      books_supplies + entertainment + personal_care +
      technology + health_wellness + miscellaneous
  )

# Analyze Income vs. Spending
model_income <- lm(total_spending ~ total_income, data = spending)
summary(model_income)

ggplot(spending, aes(x = total_income, y = total_spending)) +
  geom_point(color = "blue") +
  geom_smooth(method = "lm", color = "red", se = TRUE) +
  ggtitle("Income vs Spending with Regression Line") +
  xlab("Total Income") +
  ylab("Total Spending")

plot(model_income, which = 1)  # Residuals vs. Fitted
plot(model_income, which = 2)  # Q-Q Plot

# ====== 2. Does Major Indicate Spending Habits? ======
# Reshape Data for Spending Categories
spending_long <- spending %>%
  pivot_longer(cols = c(housing, food, transportation, books_supplies, 
                        entertainment, personal_care, technology, 
                        health_wellness, miscellaneous), 
               names_to = "category",       
               values_to = "amount")        

# Visualize Spending by Major and Category
ggplot(spending_long, aes(x = major, y = amount, fill = major)) +
  geom_boxplot() +
  facet_wrap(~ category, scales = "free_y") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1)) +
  ggtitle("Spending Trends by Major and Category") +
  xlab("Major") +
  ylab("Spending Amount")

# ANOVA to Check Differences by Major
anova_results <- spending_long %>%
  group_by(category) %>%
  summarize(p_value = summary(aov(amount ~ major, data = cur_data()))[[1]][["Pr(>F)"]][1])

print("ANOVA Results (p-values for each category):")
print(anova_results)

# Post-Hoc Test for Housing Spending
tukey_housing <- TukeyHSD(aov(amount ~ major, data = subset(spending_long, category == "housing")))
print("Tukey's HSD for Housing Spending:")
print(tukey_housing)

# Spending Summary by Major and Category
spending_summary <- spending_long %>%
  group_by(major, category) %>%
  summarize(mean_spending = mean(amount, na.rm = TRUE),
            sd_spending = sd(amount, na.rm = TRUE)) %>%
  arrange(category, desc(mean_spending))

print("Spending Summary by Major and Category:")
print(spending_summary)

# ====== 3. Does Year in School Influence Total Spending? ======
# ANOVA: Total Spending by Year in School
anova_year <- aov(total_spending ~ year_in_school, data = spending)
summary(anova_year)

# Post-Hoc Test: Tukey's HSD for Year in School
tukey_year <- TukeyHSD(anova_year)
print("Tukey's HSD for Year in School and Total Spending:")
print(tukey_year)

# Visualize Total Spending by Year in School
ggplot(spending, aes(x = year_in_school, y = total_spending, fill = year_in_school)) +
  geom_boxplot() +
  ggtitle("Total Spending by Year in School") +
  xlab("Year in School") +
  ylab("Total Spending") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

# Analyze Spending Categories by Year
spending_long_by_year <- spending %>%
  pivot_longer(cols = c(housing, food, transportation, books_supplies, 
                        entertainment, personal_care, technology, 
                        health_wellness, miscellaneous), 
               names_to = "category",       
               values_to = "amount")

anova_results_by_year <- spending_long_by_year %>%
  group_by(category) %>%
  summarize(p_value = summary(aov(amount ~ year_in_school, data = cur_data()))[[1]][["Pr(>F)"]][1])

print("ANOVA Results for Spending Categories by Year:")
print(anova_results_by_year)

# Visualize Spending Categories by Year in School
ggplot(spending_long_by_year, aes(x = year_in_school, y = amount, fill = year_in_school)) +
  geom_boxplot() +
  facet_wrap(~ category, scales = "free_y") +
  ggtitle("Spending by Category Across Years in School") +
  xlab("Year in School") +
  ylab("Spending Amount") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))
