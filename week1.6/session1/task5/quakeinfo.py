# Week 1.6, Session 1: Task 5

# Write a program here that uses the QuakeFeed and QuakeDataset
# classes to download earthquake data from a USGS data feed,
# analyze it and display the results

# See README.md for full details of what is required and what
# program output should look like
# Week 1.6, Session 1: Task 5

from feed import QuakeFeed
from dataset import QuakeDataset

level = input("Enter significance level: ")
period = input("Enter time period: ")

feed = QuakeFeed(level, period)

dataset = QuakeDataset(feed)

dataset.read_feed()

print(dataset)

print(f"Mean depth = {dataset.mean_depth():.2f} km")

print(f"Mean magnitude = {dataset.mean_magnitude():.1f}")

strongest = dataset.strongest_quake()

print(f"Strongest quake occurred at "
    f"{strongest.when.strftime('%H:%M:%S')} "
    f"on {strongest.when.strftime('%Y-%m-%d')}")

print(f"at {strongest.longitude:.1f}° longitude, "
    f"{strongest.latitude:.1f}° latitude")

print(f"The depth was {strongest.depth:.1f} km")

print(f"The magnitude was {strongest.magnitude:.1f}")