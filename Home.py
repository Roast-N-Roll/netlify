import streamlit as st
import pandas as pd
from API import list_sites, list_builds

# Page config
st.set_page_config(
    page_title="Roast n' ROll | Streamlit App",
    page_icon='assets/favicon.png',
    layout='wide')

# Main screen
st.title("Home Page")


sites = list_sites()

if sites:
    for site in sites:
        st.write(f"Site: {site['url']}")
        builds = list_builds(site['site_id'])

        df = pd.DataFrame(builds)

        # Convert the 'timestamp' column to datetime format
        df['created_at'] = pd.to_datetime(df['created_at'])

        # Convert datetime to date
        df['date'] = df['created_at'].dt.date

        data = df.groupby('date')['deploy_state'].count()
        st.line_chart(data)
else:
    st.write("No sites found.")