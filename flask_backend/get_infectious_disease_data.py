import pandas as pd
from datetime import datetime


def get_year_graph_for_district(district):
    # Load the Excel file into a pandas DataFrame
    df = pd.read_excel('J:\IIT Folder\Year_4\FYP\Code\Tests\Contagious_disease_data_Ascending_order.xlsx')

    # Check if district available here
    
    district_data = df[df['city_name'] == district]
    district_data = district_data[district_data['start_date'].dt.year == 2023]

    # Convert the data to a format suitable for plotting (e.g., a list of dictionaries)
    plot_data = [
        {
            'date': row['start_date'].strftime('%Y-%m-%d'),
            'total_diseases': row['total_diseases_weekly_city']
        }
        for _, row in district_data.iterrows()
    ]
    return(plot_data)