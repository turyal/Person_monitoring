import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def spl (a): return a.split(' ')[1]

df = pd.read_csv('gait.csv')
df['Counter'] = df['Counter'] - 1820
df['Time'] = df['Timestamp'].apply(spl)
df['Time'] = df['Time'] +':'+ df['Counter'].astype(str)



def plot_tug_graph(gender,age, last_tug ):
    # following code is for plotting TUG time
    age_x_axis = np.array([24, 33, 45, 55, 65, 75])
    female_tug = np.array([8.57, 8.56, 8.86, 8.87, 9.44, 11.5])
    male_tug = np.array([8.57, 8.56, 8.86, 9.90, 9.25, 10.8])


    high_risk = 16.0
    moderate_risk = 13.0

    # Define the colors for each category
    colors = ['r', 'y', 'g']

    # Create the plot
    fig1, ax = plt.subplots(figsize=(8, 4))

    if gender == 'female' or gender == "Female" or gender == 'F' or gender == 'f':
        # Define the categories based on the risk thresholds
        label_line = "Avg TUG values for " + gender

        ax.plot(age, last_tug, marker='o', color='b', label='Your Result', markersize=7)
        ax.plot(age_x_axis, female_tug, label=label_line)
        ax.annotate("Your TUG " + str(round(last_tug, 2)) + 'sec', (age, last_tug + 1.5))


    elif gender == 'male' or gender == "Male" or gender == 'M' or gender == 'm':
        label_line = "Avg TUG values for " + gender

        ax.plot(age, last_tug, marker='o', color='b', label='Your Result', markersize=7)
        ax.plot(age_x_axis, male_tug, label=label_line)
        ax.annotate("Your TUG " + str(round(last_tug, 2)) + 'sec', (age, last_tug + 1.5))

    ax.axhspan(ymin=high_risk, ymax=25, color=colors[0], alpha=0.2, label='High risk')
    ax.axhspan(ymin=moderate_risk, ymax=high_risk, color=colors[1], alpha=0.2, label='Moderate risk')
    ax.axhspan(ymin=3, ymax=moderate_risk, color=colors[2], alpha=0.2, label='Low risk')

    # Add a legend and title
    ax.legend()
    ax.set_title('TUG values')
    ax.set_xlabel('Age (years)')
    ax.set_ylabel('TUG Time (sec)')
    return fig1, ax

fig, ax = plot_tug_graph('male', 25, 8.9)
st.title('Functional Mobility')

cola, colb = st.columns([0.5,0.5])
cola.line_chart(data=df, x='Time', y='Step Count', x_label='Time (s)', y_label='Cadence', height=200)
colb.pyplot(fig=fig)

cola2, colb2 = st.columns([0.5,0.5])
cola2.line_chart(data=df, x='Time', y='Distance Travelled', x_label='Time (s)', y_label='Gait Speed')
colb2.line_chart(data=df, x='Time', y=['Left Flexion Angle','Right Flexion Angle'], x_label='Time (s)', y_label='Angles (Degrees)')

st.line_chart(data=df, x='Time', y=['Step Length','Step Width', 'Stride Length'], x_label='Time (s)', y_label='Distance (cm)')