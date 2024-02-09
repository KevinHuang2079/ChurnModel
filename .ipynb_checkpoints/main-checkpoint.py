import pandas as pd
import numpy as np

def main():
    #read in data from csv 
    table = pd.read_csv("TelcoCustomerChurn.csv")
    table.drop("customerID")
    

if __name__ == "__main__":
    main()