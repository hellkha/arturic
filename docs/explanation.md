# Project Methodology and Anomalies

## Methodology

The Arturic data-processing pipeline is a stateless program, able to be run in isolation.

The project states: 

> ### "Calculate the **sum of all valid entry values** across all departments". 

So the final value is the sum of all entries of all departments, all people, once the invalid entries are filtered out, following the 6 rules in the [Manual](https://d1ihdmbljgo2cz.cloudfront.net/manual.html).

### Results
> ***__The sum is: <u>1350141.67</u>__ (exactly: 1350141.670000003 - more on this in the anomalies section below)***

### Rationale

#### Order of actions:
1. **Starting point and pipeline control**: The entry point of the application is main.py file. It is the main function that is called when the application is run. Pipeline logic is handled by `pipeline` package.

2. **Files discovery**: `file_finder` package finds all files in the data directory.

3. **Files reading**: `file_reader` package reads all files in the data directory, and transform them in a list of objects from Entry class.    

4. **Data validation**: `entry_validator` package validates all Entry objects in the list for every validation rule. It only tests the Entry object and returns a boolean validating it or not.

5. **Data aggregation**: pipeline in `pipeline` package holds the Entry objects that passed the validation and the sum of their values.

6. **Output generation**: `utils` package holds the `logger`, which generates the output in the logs directory. Pipeline also prints statistics and sum on console.

## Anomalies Encountered

The final sum was evaluated to `1165175.4300000023`. This is most likely due to a base-2 binary limitation dealing with base-10 fractions. Float aggregations might cause numerical drift and imprecisions.

## Other Notes

**Image**: As it was not clear how the image was supposed to be used, a search was conducted, and it was found that not only the picture, but also names of departments, people, bins (tempers), and categories (refinement progress) are related to the TV show "Severance". The department I was assigned to is the Macro Data Refinement, which address is: 101 Crawfords Corner Rd, Holmdel, NJ 07733, EUA.

**Unit Tests**: A few unit tests were created, however it was not the intention to create an exhaustive test suite at the moment.