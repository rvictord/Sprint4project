{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import plotly.express as px \n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Load data\n",
    "data = pd.read_csv('C:/Users/victo/Downloads/vehicles_us.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2023-04-14 15:42:14.999 \n",
      "  \u001B[33m\u001B[1mWarning:\u001B[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\victo\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python310\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Header\n",
    "st.header(\"Exploratory Data Analysis\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Checkbox to toggle between histograms and scatter plots\n",
    "show_histograms = st.checkbox(\"Show histograms\", True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Histogram of mileage\n",
    "if show_histograms:\n",
    "    st.subheader(\"Mileage Distribution\")\n",
    "    fig = px.histogram(data, x=\"odometer\")\n",
    "    st.plotly_chart(fig)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Show scatter plot of days listed vs condition\n",
    "show_days_vs_condition = st.checkbox(\"Show days listed vs condition scatter plot\")\n",
    "if show_days_vs_condition:\n",
    "    st.subheader(\"Days Listed vs Condition\")\n",
    "    fig = px.scatter(data, x=\"days_listed\", y=\"condition\")\n",
    "    st.plotly_chart(fig)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Scatter plot of mileage vs. price\n",
    "st.subheader(\"Mileage vs. Price\")\n",
    "fig = px.scatter(data, x=\"odometer\", y=\"price\")\n",
    "st.plotly_chart(fig)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.11"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
