import sys

#importing pandas as pd 
import pandas as pd 

# Taking the argument from command line: input and output files
input_file: str = sys.argv[1]
output_file: str = sys.argv[2]
  
# Read and store content 
# of an excel file  
read_file = pd.read_excel(input_file) 
  
# Write the dataframe object 
# into csv file 
read_file.to_csv(output_file,  
                  header=True) 
