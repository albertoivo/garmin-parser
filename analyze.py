from fitparse import FitFile
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the fitfile
fitfile = FitFile('./stair/5272936472.fit')

# This is a ugly hack
# to avoid timing issues
while True:
    try:
        fitfile.messages
        break
    except KeyError:
        continue

# Get all data messages that are of type record
workout = []
for record in fitfile.get_messages('record'):
    r = {}
    # Go through all the data entries in this record
    for record_data in record:
        r[record_data.name] = record_data.value

    workout.append(r)

df = pd.DataFrame(workout)

# Describe the workout
print(df.tail(10))
