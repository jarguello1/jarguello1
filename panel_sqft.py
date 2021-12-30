"""
Created on Thu Aug  5 09:19:02 2021

@author: josea
"""

import numpy as np

#User inputs are stored in the following lists  
panel_x = []
panel_y = []
number_of_panels = []

#if main function for importing and for stopping the script
def main():
    
    #while loop to continue taking values as needed
    while True:

        #inputs for panel dimensions and continuing the program
        try:
            p_x = int(input("Panel X Dimension: "))
            p_y = int(input("Panel Y Dimension: "))
            panel_quantity = int(input(f"How many panels are {p_x}x{p_y}: "))
        except ValueError:
            print("Please input a number")
            continue
        else:
            panel_x.append(p_x)
            panel_y.append(p_y)
            number_of_panels.append(panel_quantity)
        
        #Print panel dimensions to keep track and spot errors
        print(f"\nPanel is {p_x}*{p_y}")
        for i in range(min(len(panel_x), len(panel_y), len(number_of_panels))):
            print(f"{panel_x[i]}x{panel_y[i]} {number_of_panels[i]}")
        
        #Possible entries for input
        print("\n1 to calculate values")
        print("del to delete entry")
        continput = input("Any other key to continue\n")
        
          
        #conditions to end the script and output results    
        if continput == "1":
            
            print(f"Panel x-dimensions {panel_x}")
            print(f"Panel x-dimensions {panel_y}")
            
            #numpy arrays for calculating total panel sqft 
            a = np.array(panel_x)
            b = np.array(panel_y)
            c = np.array(number_of_panels)
        
            #Print final output, f-string function to limit decimals        
            print(f"Total panel: {sum(a*b*c)}mm^2")
            print(f"Total panel: {(sum(a*b*c))/92903:0.2f}sqft")
            
            return False

        #command to delete last input
        if continput == "del":
            
            del_input = int(input("Delete which entry column? "))

            print(f"{panel_quantity} Panels {panel_x[del_input-1]}*{panel_y[del_input-1]}x{number_of_panels[del_input-1]} deleted")
            del panel_x[del_input-1]
            del panel_y[del_input-1]
            del number_of_panels[del_input-1]
            

             
if __name__ == '__main__':
    main()
