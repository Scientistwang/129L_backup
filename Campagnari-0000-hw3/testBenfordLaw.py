#!/usr/bin/env python3
#
# Read data from the census on populations on
# all city/towns in the United States and test
# Benford law.
#
# The data is in a csv file
# CensusTownAndCityPopulation.csv
#
# The first row of the csv file is a header row.
# The other rows are: State,City.Population
#
# Read the csv with a python csv reader
#
# Claudio 12-12-2018
# Added encoding='utf-8' to file open   12-24-2018
# Upgraded to ccHistStuff                1-29-2019
# --------------------------------------------
import csv as csv
import numpy as np
import matplotlib.pyplot as plt
import ccHistStuff as cc

method = 1
#-----------------------------------------------------
# This is a list of populations.
# Careful: the information will be in strings not numbers
#-----------------------------------------------------
population = []

#------------------------------------------------------
# Fill the population list using the csv python package
#------------------------------------------------------
if method == 1:
    with open("CensusTownAndCityPopulation.csv", encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, dialect='excel', delimiter=',')
        header = True
        for row in csvreader:
            if header:
                header = False
            else:
                population.append(row[2])

#--------------------------------------------------
# Alternative
# Careful: some numbers have a comma in it
# so splitting the string has to be done carefully
#------------------------------------------------
if method == 2:
    with open("CensusTownAndCityPopulation.csv", encoding='utf-8') as csvfile:
         contents = csvfile.readlines()
         
    header = True
    for line in contents:
        if header:
            header=False
        else:
            # remove end of line character from line
            thisLine = line.strip('\r\n')

            # split the line using the first two commas
            # the third entry in the list is (almost) what we want
            blah = thisLine.split(",",2)[2]

            # remove the quotes if they are there
            blah = blah.strip('"')
            population.append(blah)

            # some debug statements
            # print(line)
            # print(blah)

    # unfortunately there is at least one non conforming entry
    # in the csv file, with one extra comma
    # Florida,".Islamorada, Village of Islands village","6,435"
    # So let's go over the entries and try to fix 
    for i in range( len(population) ):
        blah = population[i]
        replace = False
        while blah.count(",") > 1 and (not blah[0].isnumeric()):
            blah = blah.split(",",1)[1]
            blah = blah.strip('"')
            replace = True
        if replace:
            print("Debug special case")
            print("Replacing: ", population[i])
            print("With:      ", blah)
            print(" ")
            population[i] = blah

                
        
#-------------------------------------------------------------------
# extract the first digit, as a number, from the population string
#------------------------------------------------------------------
digit = np.array([])
for entry in population:
    digit = np.append( digit, int(entry[0]) )   

#------------------------------------------------
# Plot the digit now
#------------------------------------------------
fig, ax, = plt.subplots()
contents, binEdges, _ = ax.hist(digit, np.linspace(0.5, 9.5, 10),
                                histtype='step', log=False, color='black')
# Make it prettier, add the stat box
cc.statBox(ax, digit, binEdges)
# cc.plotErr(ax, contents, binEdges, color='blue')
ax.set_xlim(binEdges[0], binEdges[-1])
# ax.set_ylim(0. , 1.4*np.max(contents))
ax.tick_params("both", direction='in', length=10, right=True)
ax.set_xticks(binEdges, minor=True)
# ax.tick_params("both", direction='in', length=7, right=True, which='minor')


fig.show()
input("Press any key to continue")



            
