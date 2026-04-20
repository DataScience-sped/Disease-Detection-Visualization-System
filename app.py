from flask import Flask, render_template
import folium
import pandas as pd

app = Flask(__name__)

locations_data = {
    'Name': ['Hospital A', 'Nursing Home B', 'Hospital C', 'Nursing Home D', 'Hospital B', 'Hospital D', 'Nursing Home E', 'Nursing Home X', 'Nursing Home M', 'Hospital Z'],
    'Latitude': [40.7128, 21.8975, 65.4356, 33.6521, 75.6857, 29.8796, 4.56231, 68.8792, 71.589, 54.6897],
    'Longitude': [-74.0060, -63.0981, -49.5163, -21.5647, -75.4562, -42.6789, -25.5631, -53.1458, -61.3287, -1.69871],
    'Type': ['Hospital', 'Nursing Home', 'Hospital', 'Nursing Home', 'Hospital', 'Hospital', 'Nursing Home', 'Nursing Home', 'Nursing Home', 'Hospital']
}

disease_data = {
    'Disease': ['Flu', 'Cold', 'Diabetes', 'Heart Disease', 'Cancer', 'Dengue', 'Corona', 'Normal Injury', 'Psychological Imbalance', 'Trauma'],
    'Latitude': [40.7128, 21.8975, 65.4356, 33.6521, 75.6857, 29.8796, 4.56231, 68.8792, 71.589, 54.6897],
    'Longitude': [-74.0060, -63.0981, -49.5163, -21.5647, -75.4562, -42.6789, -25.5631, -53.1458, -61.3287, -1.69871],
    'Affected': [100, 50, 30, 45, 18, 63, 93, 33, 17, 77]
}

locations_df = pd.DataFrame(locations_data)
diseases_df = pd.DataFrame(disease_data)

def get_color(disease):
    colors = {
        'Flu': 'blue',
        'Cold': 'green',
        'Diabetes': 'orange',
        'Heart Disease': 'red',
        'Cancer': 'violet',
        'Dengue': 'purple',
        'Corona': 'yellow',
        'Normal Injury': 'brown',
        'Psychological Imbalance': 'indigo',
        'Trauma': 'gray'
    }
    return colors.get(disease, 'white')


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/map')
def map_view():
    disease_map = folium.Map(location=[4.0, -76.0], zoom_start=2)

    # Hospital markers
    for _, row in locations_df.iterrows():
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=row['Name'],
            icon=folium.Icon(color='purple' if row['Type'] == 'Hospital' else 'lightblue')
        ).add_to(disease_map)

    # Disease markers
    for _, row in diseases_df.iterrows():
        folium.CircleMarker(
            location=[row['Latitude'], row['Longitude']],
            radius=row['Affected'] / 10,
            color=get_color(row['Disease']),
            fill=True,
            fill_opacity=0.6,
            popup=f"{row['Disease']} - Affected: {row['Affected']}"
        ).add_to(disease_map)

    # Save map
    disease_map.save('templates/disease_analysis_map.html')

    return render_template('disease_analysis_map.html')

if __name__ == '__main__':
    app.run(debug=True)
