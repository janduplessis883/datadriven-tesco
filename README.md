# Tesco Stores Challange

### General instructions:
• This task is intended to be a general DS assessment. If you have applied for an Operational Research role, please contact your recruiter.
• Please, explain any step or though that you think may be important to evaluate your task.
• The expected programming language is python
• For the sake of the review, we strongly prefer to receive back a jupyter notebook containing all the code, comments and thoughts. This notebook should work from end to end, so we can restart and run all or go through it, cell by cell, if we needed to do so.
TESCO STORES Dataset
At Tesco, the location of a retail store plays a huge role in its commercial success. Our Stores Team use various data sources to better understand the potential of candidate locations for new stores in the UK. They need data science help in designing a model that can predict the future sales [normalised_sales] of a store based on location characteristics. Your task is to examine the provided dataset and answer the questions below.

### Dataset files

# Q1
: id of Tesco property location
: normalised sales value of Tesco store
: crime rate in the area
: mean household size in the area
: mean household affluency in the area
: index of public transport availability in the area
: proportion of newly built property in the area : average property value in the area
: percentage of commercial properties in the area : average school proximity in the area
: proximity of different transport modes : new Tesco store opened recently
: proportion of non-retail commercial properties in the area : density of competitor retailers
: proportion of blocks of flats in the area : county code of the area
 tesco-dataset/train.csv
 tesco-dataset/test.csv
location_id
normalised_sales
crime_rate
household_size
household_affluency
public_transport_dist
proportion_newbuilds
property_value
commercial_property
school_proximity
transport_proximity
new_store
proportion_nonretail
competitor_density
proportion_flats
county
Before diving into the modelling, you are given the dataset and the Stores Team expect you to come back with an analysis of the data and any concerns you may have about it. They would also like to know which other information you think would be useful to collect for future developments.
# Q2
Build a model that can predict store sales based on the provided area features. Please show how you developed the model and report how well your model is
performing. Constraint: Please use Random Forest as the model family to solve this problem.
# Q3
The dataset contains a test set of potential store locations. Use your developed model to predict the sales value in these areas and explain what recommendations you would give to the Stores Team to use it. Use any tools that may help you to share your findings with product owners and other non-technical decision makers in the team. Complete this task by explaining how you would improve the current results.

