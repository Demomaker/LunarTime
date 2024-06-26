import time
import sys
from datetime import datetime

# Constants for the moon
EARTH_DAYS_IN_MOON_MONTH = 29.5
EARTH_YEAR_IN_DAYS = 365
SECONDS_MULTIPLICATION = 24 * 3600
MOON_DAY_SECONDS = EARTH_DAYS_IN_MOON_MONTH * SECONDS_MULTIPLICATION  # Lunar month in seconds
MOON_YEAR = EARTH_YEAR_IN_DAYS / EARTH_DAYS_IN_MOON_MONTH
MOON_YEAR_SECONDS = MOON_YEAR * SECONDS_MULTIPLICATION  # Moon year in seconds

# Timestamp of the discovery of the moon
MOON_DISCOVERY_YEAR = -361  # first observations in 1609 which is 1970 (epoch start) - 361.
MOON_DISCOVERY_TIMESTAMP = MOON_DISCOVERY_YEAR * SECONDS_MULTIPLICATION * EARTH_YEAR_IN_DAYS
FULL_MOON_OFFSET_SECONDS = -(3 * SECONDS_MULTIPLICATION + 11 * 3600 + 6 * 60)

def get_current_year_seconds(current_time_seconds):

    # Get the current year
    current_year = time.localtime(current_time_seconds).tm_year

    # Calculate the timestamp for the start of the current year
    start_of_year_timestamp = time.mktime((current_year, 1, 1, 0, 0, 0, 0, 0, -1))

    # Calculate the number of seconds since the start of the current year
    seconds_since_start_of_year = current_time_seconds - start_of_year_timestamp

    return seconds_since_start_of_year

def get_current_day_seconds(current_time_seconds):

    # Calculate the timestamp for the start of the current day (midnight)
    start_of_day_timestamp = time.mktime(time.localtime(current_time_seconds)[:3] + (0, 0, 0) + (0, 0, -1))

    # Calculate the number of seconds since the start of the current day
    seconds_since_start_of_day = current_time_seconds - start_of_day_timestamp

    return seconds_since_start_of_day

def get_lunar_time(current_time_seconds = time.time()):
    # Get the current time in seconds since the epoch
    current_year_seconds = get_current_year_seconds(current_time_seconds)

    current_day_seconds = get_current_day_seconds(current_time_seconds)

    # Calculate days since the discovery of the moon
    days_since_discovery = (current_time_seconds - MOON_DISCOVERY_TIMESTAMP + FULL_MOON_OFFSET_SECONDS) / (SECONDS_MULTIPLICATION)

    # Calculate current lunar year
    current_lunar_year = int(days_since_discovery / EARTH_YEAR_IN_DAYS)

    # Calculate current lunar day
    current_lunar_day = int((current_year_seconds - FULL_MOON_OFFSET_SECONDS) / MOON_DAY_SECONDS) + 1  # Lunar day ranges from 1 to 28

    this_lunar_day_seconds = int((current_year_seconds - FULL_MOON_OFFSET_SECONDS) - (MOON_DAY_SECONDS * (current_lunar_day - 1)))

    # Calculate cumulative lunar time in Earth days, hours, minutes, and seconds
    lunar_time_days = int(this_lunar_day_seconds / SECONDS_MULTIPLICATION)  # Days within the current lunar cycle
    lunar_time_hours = (lunar_time_days * 24) + int((current_day_seconds) / 3600)
    lunar_time_minutes = int((current_day_seconds % 3600) / 60)
    lunar_time_seconds = int(current_day_seconds % 3600 % 60 % 60)

    return current_lunar_year, current_lunar_day, lunar_time_hours, lunar_time_minutes, lunar_time_seconds

def get_lunar_time_in_months_format(current_time_seconds = time.time()):
    # Get the current time in seconds since the epoch
    current_year_seconds = get_current_year_seconds(current_time_seconds)

    current_day_seconds = get_current_day_seconds(current_time_seconds)

    # Calculate days since the discovery of the moon
    days_since_discovery = (current_time_seconds - MOON_DISCOVERY_TIMESTAMP + FULL_MOON_OFFSET_SECONDS) / (SECONDS_MULTIPLICATION)

    # Calculate current lunar year
    current_lunar_year = int(days_since_discovery / EARTH_YEAR_IN_DAYS)

    # Calculate current lunar day
    current_lunar_month = int((current_year_seconds - FULL_MOON_OFFSET_SECONDS) / MOON_DAY_SECONDS) + 1  # Lunar day ranges from 1 to 28

    this_lunar_day_seconds = int((current_year_seconds - FULL_MOON_OFFSET_SECONDS) - (MOON_DAY_SECONDS * (current_lunar_month - 1)))

    # Calculate cumulative lunar time in Earth days, hours, minutes, and seconds
    lunar_time_days = int(this_lunar_day_seconds / SECONDS_MULTIPLICATION)  # Days within the current lunar cycle
    lunar_time_hours = int((current_day_seconds) / 3600)
    lunar_time_minutes = int((current_day_seconds % 3600) / 60)
    lunar_time_seconds = int(current_day_seconds % 3600 % 60 % 60)

    return current_lunar_year, current_lunar_month, lunar_time_days, lunar_time_hours, lunar_time_minutes, lunar_time_seconds

def show_lunar_time(current_time_seconds = time.time()):
    lunar_year, lunar_day, lunar_hours, lunar_minutes, lunar_seconds = get_lunar_time(current_time_seconds)
    print("===================")
    print("Lunar time : ")
    print("{:d}-{:02d} {:02d}:{:02d}:{:02d}".format(lunar_year, lunar_day, lunar_hours, lunar_minutes, lunar_seconds))
    print(" ")

def show_lunar_time_in_months_format(current_time_seconds = time.time()):
    lunar_year, lunar_month, lunar_time_days, lunar_time_hours, lunar_time_minutes, lunar_time_seconds = get_lunar_time_in_months_format(current_time_seconds)
    print("===================")
    print("Lunar time in months and days format :")
    print("{:d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(lunar_year, lunar_month, lunar_time_days, lunar_time_hours, lunar_time_minutes, lunar_time_seconds))
    print(" ")

def show_earth_time(current_time_seconds = time.time()):
    print("==================")
    print("In Earth Time : ")
    print(datetime.fromtimestamp(current_time_seconds).strftime("%Y-%m-%d %H:%M:%S"))

def show_time(current_time_seconds = time.time()):
    show_lunar_time(current_time_seconds)
    show_lunar_time_in_months_format(current_time_seconds)
    show_earth_time(current_time_seconds)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        show_time()
    else:
        show_time(float(sys.argv[1]))
