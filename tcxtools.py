"""
Tools to process TCX files,
specifically for parsing and
converting to other formats.
"""

import numpy as np
import pandas as pd
from lxml import objectify
import dateutil.parser
import logging

TPXNS = "{http://www.garmin.com/xmlschemas/ActivityExtension/v2}TPX"
LXNS = "{http://www.garmin.com/xmlschemas/ActivityExtension/v2}LX"

POWER_CONSTANT = 4184


class TCXPandas(object):
    """
    Class for Parsing .TCX files to Pandas DataFrames.

    Parameters
    ----------
    tcx_file : string, path object,
               the path to the tcx file

    """

    def __init__(self, tcx_file, **kwds):
        self.__filehandle__ = tcx_file
        self.tcx = None
        self.activity = None
        self.laps_dataframe = None
        self.traverse_dataframe = None

        logging.basicConfig(filename="TCXconversion.log", level=logging.DEBUG)

    def parse(self):
        """
        Parse specified TCX file into a DataFrame
        Return a Dataframe and sets Dataframe and sets
        the self.dataframe object in the TCXParser.
        """

        self.tcx = objectify.parse(open(self.__filehandle__))
        self.activity = self.tcx.getroot().Activities.Activity

        self.traverse_dataframe = pd.DataFrame(self._traverse_laps_())
        self.laps_dataframe = pd.DataFrame(self._info_laps_())

        return self.traverse_dataframe, self.laps_dataframe

    def get_activity_timestamp(self):
        """
        Returns the TCX file timestamp if parsed
        """
        if self.activity is None:
            return None
        else:
            return self.activity.Id

    def get_sport(self):
        """
        Returns the specified sport of the TCX file
        """
        if self.activity is None:
            return None
        else:
            return self.activity.attrib['Sport']

    def get_workout_startime(self):
        """
        Returns the starting timestamp of the specified TCX file
        """
        if self.activity is None:
            return None
        else:
            return self.activity.Lap.items()[0][1]

    def _info_laps_(self):

        # New iterator method to align with lxml standard
        return_array = []
        for lap in self.activity.Lap:
            return_dict = {}

            try:
                return_dict['time (s)'] = np.int(lap.TotalTimeSeconds)
            except AttributeError:
                pass  # TODO log this

            try:
                return_dict['distance (m)'] = np.float(lap.DistanceMeters)
            except AttributeError:
                pass  # TODO log this

            try:
                return_dict['max speed (m/s)'] = np.float(lap.MaximumSpeed)
                return_dict['max speed (km/h)'] = round((np.float(lap.MaximumSpeed) * 3.6), 3)
            except AttributeError:
                pass  # TODO log this

            try:
                return_dict['avg speed (m/s)'] = np.float(lap.Extensions[LXNS].MaximumSpeed)
                return_dict['avg speed (km/h)'] = round((np.float(lap.Extensions[LXNS].MaximumSpeed) * 3.6), 3)
            except AttributeError:
                pass  # TODO log this

            try:
                return_dict['calories'] = np.int(lap.Calories)
            except AttributeError:
                pass  # TODO log this

            try:
                return_dict['avg hr'] = np.int(lap.AverageHeartRateBpm.Value)
            except AttributeError:
                pass  # TODO log this

            try:
                return_dict['max hr'] = np.int(lap.MaximumHeartRateBpm.Value)
            except AttributeError:
                pass  # TODO log this

            try:
                return_dict['power (w)'] = round((np.float(lap.Calories) * POWER_CONSTANT / np.float(lap.TotalTimeSeconds)), 3)
            except AttributeError:
                pass  # TODO log this

            return_array.append(return_dict)

        return return_array

    def _traverse_laps_(self):

        # New iterator method to align with lxml standard
        return_array = []
        for laps in self.activity.Lap:
            for tracks in laps.Track:
                for trackingpoints in tracks.Trackpoint:
                    return_dict = {}

                    return_dict['time'] = dateutil.parser.parse(str(trackingpoints.Time))

                    try:
                        return_dict['latitude'] = np.float(trackingpoints.Position.LatitudeDegrees)
                    except AttributeError:
                        pass  # TODO log this

                    try:
                        return_dict['longitude'] = np.float(trackingpoints.Position.LongitudeDegrees)
                    except AttributeError:
                        pass  # TODO log this

                    try:
                        return_dict['altitude'] = np.float(trackingpoints.AltitudeMeters)
                    except AttributeError:
                        pass  # TODO log this

                    try:
                        return_dict['distance'] = np.float(trackingpoints.DistanceMeters)
                    except AttributeError:
                        pass  # TODO log this

                    try:
                        return_dict['hr'] = np.int(trackingpoints.HeartRateBpm.Value)
                    except AttributeError:
                        pass  # TODO log this

                    try:
                        return_dict['speed (m/s)'] = np.float(trackingpoints.Extensions[TPXNS].Speed)
                        return_dict['speed (km/h)'] = np.float(trackingpoints.Extensions[TPXNS].Speed) * 3.6
                    except AttributeError:
                        pass  # TODO log this

                    if self.get_sport == 'Running':
                        try:
                            return_dict['cadence'] = np.float(trackingpoints.Extensions[TPXNS].RunCadence)
                        except AttributeError:
                            pass  # TODO log this
                    else:  # self.activity.attrib['Sport'] == 'Biking':
                        try:
                            return_dict['cadence'] = np.float(trackingpoints.Cadence)
                        except AttributeError:
                            pass  # TODO log this

                        try:
                            return_dict['power'] = np.float(trackingpoints.Extensions[TPXNS].Watts)
                        except AttributeError:
                            pass  # TODO log this

                    return_array.append(return_dict)

        return return_array
