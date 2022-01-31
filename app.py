import streamlit as st
# from streamlit_folium import folium_static
import folium
# import geopandas as gpd
import json
import pydeck as pdk
# import geemap.eefolium as geemap

uploaded_file = st.sidebar.file_uploader(label="Upload GeoJSON file", type=['geojson'], accept_multiple_files=False)
if uploaded_file is not None:
    data = json.load(uploaded_file)
    lon  = data['features'][0]['geometry']['coordinates'][0][0][0]
    lat  = data['features'][0]['geometry']['coordinates'][0][0][1]
    st.pydeck_chart(pdk.Deck(
        map_provider="mapbox",
        map_style=pdk.map_styles.SATELLITE,
        api_keys  = { "mapbox": "pk.eyJ1IjoiZ3JvbDIwMjAiLCJhIjoiY2tvajI0MW5pMDMxMDJ3bzdpN3dzbHBidyJ9.jxYSuCXT1u1eFKMMWwSFVg"},
        initial_view_state=pdk.ViewState(
            latitude  = lat,
            longitude = lon,
            zoom=12,
            pitch=0,
        ),
        layers=[
            pdk.Layer(
                'GeoJsonLayer',
                data=data,
                get_fill_color=[0, 0, 0]
            ),
        ],
    ))
    st.write()

    
#     st.write(gpd.read_file(uploaded_file))
    # # center on Liberty Bell
    # m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
    # folium.GeoJson(uploaded_file, name="geojson").add_to(m)
    # # add marker for Liberty Bell
    # tooltip = "Liberty Bell"
    # folium.Marker(
    #     [39.949610, -75.150282], popup="Liberty Bell", tooltip=tooltip
    # ).add_to(m)

    # # call to render Folium map in Streamlit
    # folium_static(m)

