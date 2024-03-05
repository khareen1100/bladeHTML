import random
import pandas as pd

# Define lists of possible values for categorical columns
possible_values = {
    'Address': ["P2 Camote,Barangay Maon", "P3 Kammungay,Barangay Maon", "P1 Cassava,Barangay Maon", "P5 Ube,Barangay Maon"],
    'Marital status of household head': ["Married", "Single", "Widower"],
    'Household head kind of business (if business is the source of income)': ["None", "Sari-sari Store/Peso Net", "Drygoods Retail/ Natasha", "Vaind Seller"],
    'Educational Attainment of the household head': ["High School Graduate", "College Graduate", "Elementary Graduate"],
    'Household head occupation': ["Part time Technician", "Businness Onwer", "Tatoo Artist", "Senior Citizen", "Orgon Worker", "Company Driver", "None", "Barangay Councilor", "Tricycle Driver", "Engineer", "Coordinator", "Sideline", "Glass Installer"],
    'Household head spouse is employed (y/n)': ["Yes", "No"],
    'Household type': ["Normal", "Extended"],
    'Spend for Laundry Services (y/n)': ["Yes", "No"],
    'Pay Tuition fees in cash': ["20,000-25,000", "10,000 - 22,000", "50,000 - UP", "26,000 - 30,000"],
    'Receive cash receipts, assistance from abroad (y/n)': ["Yes", "No"],
    'Household owned motorcycles (y/n)': ["Yes", "No"],
    'Household owned car (y/n)': ["Yes", "No"],
    'Spend for maid/boy services (y/n)': ["Yes", "No"],
    'Household Means in Cooking': ["FIREWOOD", "LPG"],
    'Number of own APPLIANCES': ["1-2", "5", "3", "6"],
    'Number of phones/gadgets owned': ["1-2", "5 - up", "3-4"],
    'Household House Structure type': ["Metal Roof & Half Concrete", "Metal Roof & Amakan", "Nipa & Wood", "Metal Roof & Hardiflex", "Metal Roof & Full Concrete"],
    'Have a sala sets (y/n)': ["Yes", "No"],
    'Household have toilet facility (y/n)': ["Yes", "No"],
    'Household have main source of water (y/n)': ["Yes", "No"],
    'Prediction': ["very poor", "poor", "average", "above average", "rich"]
}

def income_to_prediction(income):
    if income == "10,000 and below":
        return "very poor"
    elif "10,000 - 22,000" in income:
        return "poor"
    elif "23,000 - 43,000" in income:
        return "average"
    elif "44,000 - 75,000" in income:
        return "above average"
    elif "76,000-131,000" in income or "50,000 - UP" in income:
        return "rich"
    else:
        return None

def generate_sample():
    # Generate random values for each column based on their types and possible values
    income_range = random.choice(["10,000 and below", "10,000 - 22,000", "23,000 - 43,000", "44,000 - 75,000", "76,000-131,000", "50,000 - UP"])
    sample = {
        'Age': random.randint(20, 70),
        'Address': random.choice(possible_values['Address']),
        'Marital status of household head': random.choice(possible_values['Marital status of household head']),
        'Household head kind of business (if business is the source of income)': random.choice(possible_values['Household head kind of business (if business is the source of income)']),
        'Educational Attainment of the household head': random.choice(possible_values['Educational Attainment of the household head']),
        'Household head occupation': random.choice(possible_values['Household head occupation']),
        'Household head spouse is employed (y/n)': random.choice(possible_values['Household head spouse is employed (y/n)']),
        'Household type': random.choice(possible_values['Household type']),
        'Spend for Laundry Services (y/n)': random.choice(possible_values['Spend for Laundry Services (y/n)']),
        'Pay Tuition fees in cash': income_range,
        'Receive cash receipts, assistance from abroad (y/n)': random.choice(possible_values['Receive cash receipts, assistance from abroad (y/n)']),
        'Household owned motorcycles (y/n)': random.choice(possible_values['Household owned motorcycles (y/n)']),
        'Household owned car (y/n)': random.choice(possible_values['Household owned car (y/n)']),
        'Spend for maid/boy services (y/n)': random.choice(possible_values['Spend for maid/boy services (y/n)']),
        'Household Means in Cooking': random.choice(possible_values['Household Means in Cooking']),
        'Number of own APPLIANCES': random.choice(possible_values['Number of own APPLIANCES']),
        'Number of phones/gadgets owned': random.choice(possible_values['Number of phones/gadgets owned']),
        'Household House Structure type': random.choice(possible_values['Household House Structure type']),
        'Have a sala sets (y/n)': random.choice(possible_values['Have a sala sets (y/n)']),
        'Household have toilet facility (y/n)': random.choice(possible_values['Household have toilet facility (y/n)']),
        'Household have main source of water (y/n)': random.choice(possible_values['Household have main source of water (y/n)'])
    }
    sample['Prediction'] = income_to_prediction(sample['Pay Tuition fees in cash'])
    return sample

# Generate a desired number of samples
num_samples = 15000
data = [generate_sample() for _ in range(num_samples)]

# Convert the generated data into a DataFrame
df = pd.DataFrame(data)

# Save the generated data to a CSV file
df.to_csv('generated_data.csv', index=False)
