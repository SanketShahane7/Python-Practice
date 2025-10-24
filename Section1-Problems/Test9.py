import numpy as np

arr = np.array([20, 35, 68, 82, 83, 70, 90])

def ratio(marks_arr):
    distinction = marks_arr[marks_arr >= 80]   # Use masking to get the values
    print("Distinction Marks:", distinction)
    
    print("\n")
    
    first_div = marks_arr[(marks_arr >= 60) & (marks_arr < 80)]      # Use masking to get the values
    print("First Division Marks:", first_div)
    
    distinction_count = len(distinction)
    first_div_count = len(first_div)
    
    ratio = distinction_count / first_div_count if first_div_count != 0 else 0  # Avoid division by zeros
    
    print("\n")
    print("Distinction to First Division Ratio:", ratio)
    
    return round(ratio,2)

print(ratio(arr))