from Icii import *

#> DontInterpolate 

"""
Guides
**********************************************
Step: Step 1
Text: Specify the group column and the value column you want to calculate the average on.
    Select: Add required group and value column
        Options: --groupColumn ? --valueColumn ?
        Next:

Options
**********************************************
Option: groupColumn
    Description: The column to group by when calculating the average.
    Example: --groupColumn breed

Option: valueColumn
    Description: The column whose mean will be calculated for each group.
    Example: --valueColumn top_speed_mph

Description
**********************************************
Calculates the mean of a specified value column grouped by another column and sorts the result in descending order.

Keywords
**********************************************
mean average group sort descending
"""

lastDf = MostRecent('dataframe')

groupColumn = Option(position = 0) | Item.Required
valueColumn = Option(position = 1) | Item.Required

groupColumnChecked = CheckStringLiteral(groupColumn)
valueColumnChecked = CheckStringLiteral(valueColumn)

resultVar = CodeScope.NewVariable("avgByGroup")

with CodeAfterKit:
    ((resultVar)) = ((lastDf)).groupby(((groupColumnChecked)))[((valueColumnChecked))].mean().sort_values(ascending=False)
