# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 17:55:55 2023

@author: admin
"""

import streamlit as st
import osmnx as ox
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import MultiPolygon

ox.settings.log_console = True
ox.settings.use_cache = True



# @st.cache
# def map_osmn(place_name):
    # return place_name


# def visualize_osmn(place_name):
    # try:
        # city = ox.geocode_to_gdf(place_name)

        # fig, ax = plt.subplots()

        # city.plot(color="white", edgecolor="k", linewidth=.5, ax=ax)

        # # %%

        # # Get all building geometries within some place

        # gdf1 = ox.features_from_place(place_name, tags={'building': True})

        # gdf1.plot(color="gray", edgecolor="k",
                  # linewidth=.5, ax=ax, label="Buildings")

        # def create_acronym(text):
            # words = text.split()
            # acronym = ''.join(word[0].upper() for word in words)
            # return acronym

        # if place_name == 'Università Politecnica delle Marche - Polo "Alfredo Trifogli" Monte Dago':
            # avoid = ["Cabina elettrica",
                     # "Gruppo elettrogeno",
                     # "Laboratori pesanti",
                     # "Archivio cartaceo - Settore A"
                     # "Archivio cartaceo - Settore B",
                     # "Laboratori pesanti - Motori a combustione interna",
                     # "Facoltà di Ingegneria - Laboratorio Prove Materiali e Strutture"]

            # names = []

            # for i in gdf1.name:
                # if type(i) != str:
                    # names.append(" ")
                    # pass
                # elif i in avoid:
                    # names.append(" ")
                # elif len(i) > 10 and i not in avoid:
                    # if "-" in i:
                        # # print(i.split("-")[1])
                        # names.append(i.split("-")[1])
                    # else:
                        # # print(i)
                        # names.append(("\n").join(i.split()))
                # else:
                    # names.append(i)

            # for i, j in enumerate(gdf1.geometry.centroid):
                # ax.annotate(text=names[i], xy=j.coords[0],
                            # ha='center', fontsize=10)

        # # %%

        # # Get the road network
        # G = ox.graph_from_place(place_name, network_type='all')

        # ec = ['green' if data['highway'] == 'motorway' else 'gray' for u,
              # v, key, data in G.edges(keys=True, data=True)]
        # lw = [2 if data['highway'] == 'motorway' else 1 for u,
              # v, key, data in G.edges(keys=True, data=True)]

        # # Plot the road network
        # ox.plot_graph(G, bgcolor='white', edge_color=ec,
                      # edge_linewidth=lw, ax=ax)

        # plt.axis('off')
        # ax.set_title(("\n").join(place_name.split("-")))

        # # Save the SVG file
        # svg_filename = f"{place_name}_geopandas.svg"
        # fig.savefig(svg_filename, format='svg')

        # return fig, svg_filename

        # st.pyplot(fig)

    # except Exception as e:
        # st.error(f"An error occurred: {str(e)}")
        # return None, None


# if __name__ == '__main__':
    # st.title("OSM Network Visualization")

    # place_name = st.text_input("Enter a place name:")

    # if place_name:
        # if st.button("Visualize"):
            # result, svg_filename = map_osmn(place_name)

            # if result:
                # st.pyplot(result)
                # st.success(f"SVG file saved: {svg_filename}")

                # # Display a download button
                # st.download_button(
                    # label="Download SVG file",
                    # data=open(svg_filename, "rb").read(),
                    # file_name=svg_filename,
                    # key="download_button",
                # )

@st.cache_data
def map_osmn(place_name):
    try:
        city = ox.geocode_to_gdf(place_name)

        fig, ax = plt.subplots()

        city.plot(color="white", edgecolor="k", linewidth=.5, ax=ax)

        # %%

        # Get all building geometries within some place

        gdf1 = ox.features_from_place(place_name, tags={'building': True})

        gdf1.plot(color="gray", edgecolor="k",
                  linewidth=.5, ax=ax, label="Buildings")

        def create_acronym(text):
            words = text.split()
            acronym = ''.join(word[0].upper() for word in words)
            return acronym

        if place_name == 'Università Politecnica delle Marche - Polo "Alfredo Trifogli" Monte Dago':
            avoid = ["Cabina elettrica",
                     "Gruppo elettrogeno",
                     "Laboratori pesanti",
                     "Archivio cartaceo - Settore A"
                     "Archivio cartaceo - Settore B",
                     "Laboratori pesanti - Motori a combustione interna",
                     "Facoltà di Ingegneria - Laboratorio Prove Materiali e Strutture"]

            names = []

            for i in gdf1.name:
                if type(i) != str:
                    names.append(" ")
                    pass
                elif i in avoid:
                    names.append(" ")
                elif len(i) > 10 and i not in avoid:
                    if "-" in i:
                        # print(i.split("-")[1])
                        names.append(i.split("-")[1])
                    else:
                        # print(i)
                        names.append(("\n").join(i.split()))
                else:
                    names.append(i)

            for i, j in enumerate(gdf1.geometry.centroid):
                ax.annotate(text=names[i], xy=j.coords[0],
                            ha='center', fontsize=10)

        # %%

        # Get the road network
        G = ox.graph_from_place(place_name, network_type='all')

        ec = ['green' if data['highway'] == 'motorway' else 'gray' for u,
              v, key, data in G.edges(keys=True, data=True)]
        lw = [2 if data['highway'] == 'motorway' else 1 for u,
              v, key, data in G.edges(keys=True, data=True)]

        # Plot the road network
        ox.plot_graph(G, bgcolor='white', edge_color=ec,
                      edge_linewidth=lw, ax=ax)

        plt.axis('off')
        ax.set_title(("\n").join(place_name.split("-")))

        # Save the SVG file
        svg_filename = f"{place_name}_geopandas.svg"
        fig.savefig(svg_filename, format='svg')

        return svg_filename

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        return None

if __name__ == '__main__':
    st.title("OSM Network Visualization")

    place_name = st.text_input("Enter a place name:")
    
    if place_name:
        if st.button("Visualize"):
            svg_filename = map_osmn(place_name)
            
            if svg_filename:
                st.image(svg_filename, use_column_width=True)
                st.success(f"SVG file saved: {svg_filename}")

                # Display a download button
                st.download_button(
                    label="Download SVG file",
                    data=open(svg_filename, "rb").read(),
                    file_name=svg_filename,
                    key="download_button",
                )