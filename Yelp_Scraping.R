# Load necessary libraries for data manipulation, scraping, and HTTP requests
library(tidyverse)
library(rvest)
library(data.table)
library(dplyr)
library(httr)

# Set URL of the Yelp page to scrape
url <- "https://www.yelp.com/biz/haidilao-hotpot-cupertino-cupertino-3?osq=Haidilao+Us&sort_by=date_asc"

# Read the initial page's HTML content to extract information
page <- read_html(url)

# Initialize an empty list to store data collected across pages
df_final <- list()

# Attempt to extract the total number of pages available
pageNums <- page %>% 
  html_elements(xpath = "//div[@aria-label='Pagination navigation']//span[contains(text(), 'Page')]") %>% 
  html_text() %>% 
  str_extract('\\d+$') %>%   # Extract the last number in the "Page 1 of X" format
  as.numeric()

# Check if pageNums was successfully extracted and has a length of 1
if (is.na(pageNums) || length(pageNums) != 1) {
  pageNums <- 1  # Default to 1 if pageNums is not available or invalid
}

# Create a sequence of page offsets to iterate through all available pages
pageSequence <- seq(from = 0, to = (pageNums - 1) * 10, by = 10)

# Loop through each page based on the calculated page offsets
for (i in pageSequence) {
  
  # Construct the URL for each page by adding the page offset to the URL
  page_url <- sprintf("https://www.yelp.com/biz/haidilao-hotpot-cupertino-cupertino-3?start=%d&sort_by=date_asc", i)
  
  # Read the HTML content of each specific page
  page <- read_html(page_url)
  
  # Extract usernames from each review
  usernames <- page %>% 
    html_elements(xpath = "//div[contains(@class, 'user-passport')]//a[contains(@href, '/user_details')]") %>% 
    html_text()
  
  # Extract user locations (excluding any missing or empty data)
  locations <- page %>% 
    html_elements(xpath = "//div[contains(@class, 'user-passport')]//span[@class=' y-css-h9c2fl']") %>% 
    html_text() %>% 
    .[.!="Location"]
  
  # Extract review comments from each page
  comments <- page %>% 
    html_elements(xpath = "//p[@class='comment__09f24__D0cxf y-css-h9c2fl']") %>% 
    html_text()
  
  # Extract ratings from each review, converting to numeric format
  ratings <- page %>% 
    html_elements(xpath = "//div[@class='y-css-dnttlc']") %>% 
    html_attr("aria-label") %>% 
    str_extract("\\d+(\\.\\d+)?") %>%
    as.numeric()
  
  # Extract review dates from each review
  the_dates <- page %>% 
    html_elements(xpath = "//span[contains(@class, 'y-css-1qvtk2j') and contains(text(), ',')]") %>% 
    html_text()
  
  # Extract 'Helpful' reaction counts from each review
  helpful_reactions <- page %>% 
    html_elements(xpath = "//div[@aria-label[contains(., 'Helpful')]]") %>% 
    html_attr("aria-label") %>%
    str_extract("\\d+")
  
  # Extract 'Thanks' reaction counts from each review
  thanks_reactions <- page %>% 
    html_elements(xpath = "//div[@aria-label[contains(., 'Thanks')]]") %>% 
    html_attr("aria-label") %>%
    str_extract("\\d+")
  
  # Extract 'Love this' reaction counts from each review
  love_reactions <- page %>% 
    html_elements(xpath = "//div[@aria-label[contains(., 'Love this')]]") %>% 
    html_attr("aria-label") %>%
    str_extract("\\d+")
  
  # Extract 'Oh no' reaction counts from each review
  oh_no_reactions <- page %>% 
    html_elements(xpath = "//div[@aria-label[contains(., 'Oh no')]]") %>% 
    html_attr("aria-label") %>%
    str_extract("\\d+")
  
  # Compile extracted data into a list for each page
  df_new <- list(username = usernames,
                 dates = the_dates,
                 location = locations, 
                 rating = ratings, 
                 comment = comments, 
                 helpful = helpful_reactions, 
                 thanks = thanks_reactions, 
                 love = love_reactions, 
                 oh_no = oh_no_reactions)
  
  # Convert the list to a data frame for easier manipulation
  df_new_table <- as.data.frame(df_new)
  
  # Append the current page's data to the final data frame list
  df_final <- rbindlist(list(df_final, df_new_table), fill = TRUE)
}

# Print or save the final compiled data frame containing all review data
print(df_final)
