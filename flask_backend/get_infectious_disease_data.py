import pandas as pd
from datetime import datetime


def get_year_graph_for_district(district,date_str):
    # Load the Excel file into a pandas DataFrame
    df = pd.read_excel('Contagious_disease_data_Ascending_order.xlsx')

    # Check if district available here
    
    district_data = df[df['city_name'] == district]
    district_data = district_data[district_data['start_date'].dt.year == 2023]

    # Validate the input date
    try:
        input_date = datetime.strptime(date_str, '%Y/%m/%d').date()
    except ValueError:
        return None, "Invalid date format. Please use the format 'YYYY/MM/DD'."

    # Find the record where the input date is within the start_date and end_date range
    matching_record = district_data[(district_data['start_date'].dt.month == input_date.month) &
                                   (district_data['start_date'].dt.day <= input_date.day) &
                                   (district_data['end_date'].dt.day >= input_date.day)].iloc[0]
    matching_total = matching_record['total_diseases_weekly_city']

    # Convert the data to a format suitable for plotting (e.g., a list of dictionaries)
    plot_data = [
        {
            'date': row['start_date'].strftime('%Y-%m-%d'),
            'total_diseases': row['total_diseases_weekly_city']
        }
        for _, row in district_data.iterrows()
    ]
        # Calculate the mean and standard deviation of the total_diseases_weekly_city values for the year
    year_total_values = district_data['total_diseases_weekly_city'].tolist()
    year_mean = sum(year_total_values) / len(year_total_values)
    year_std_dev = (sum((x - year_mean) ** 2 for x in year_total_values) / len(year_total_values)) ** 0.5

    # Determine the classification based on the matching record's value
    if matching_total < year_mean - year_std_dev:
        classification_text = "The current level of reported diseases in your area for the date "+ str(date_str) +"is lower than the yearly average. However, it's still important to maintain good hygiene practices, such as regular handwashing, to prevent the spread of illnesses."
    elif matching_total < year_mean + year_std_dev:
        classification_text = "The current level of reported diseases in your area for the date "+ str(date_str) +" is within the normal range. It's important to be cautious and follow recommended hygiene and safety protocols to help limit the spread of illnesses, even if the situation is not out of the ordinary."
    else:
        classification_text = "The current level of reported diseases in your area for the date "+ str(date_str) +" is higher than usual. While this may be concerning, it's essential that all residents take appropriate precautions, such as avoiding large gatherings and wearing masks, to help mitigate the spread of illnesses in the community"

    print(classification_text)
    return(plot_data, classification_text)