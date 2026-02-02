import clr
from System import *
from System.IO import *
from System.Collections.Generic import *
from System.Text import *
clr.AddReference('ArcticFox')
from ArcticFox import *
from ArcticFox.Public import *
from ArcticFox.Tokens import *
from ArcticFox.Tokens.Python import *
from ArcticFox.Automations import *
clr.ImportExtensions(Functions)




class SortedGroupMean(PythonAutomation):

    def ApplyAutomation(self):

        #> DontInterpolate



        lastDf = self.MostRecent('dataframe')

        groupColumn = self.Option(optionName = 'groupColumn', position = 0) | Item.Required
        valueColumn = self.Option(optionName = 'valueColumn', position = 1) | Item.Required

        groupColumnChecked = self.CheckStringLiteral(groupColumn)
        valueColumnChecked = self.CheckStringLiteral(valueColumn)

        resultVar = self.CodeScope.NewVariable("avgByGroup")

        self.CodeAfterKit += f"""
{self.PythonInterpolate(resultVar)} = {self.PythonInterpolate(lastDf)}.groupby({self.PythonInterpolate(groupColumnChecked)})[{self.PythonInterpolate(valueColumnChecked)}].mean().sort_values(ascending=False)
print('HOWDY THERE!')"""

    def Help(self):
        message = ""
        if self.HelpItems.Contains('?'):
            if self.Items.Get('guideStep') == 'Step1' or not self.Items.Contains('guideStep'):
                message += """
Specify the group column and the value column you want to calculate the average on.
                - Add required group and value column <> --groupColumn ? --valueColumn ? --guideStep <x>
                \n"""
        self.RegisterHelpText('groupColumn', '\nThe column to group by when calculating the average.\n- Example: --groupColumn breed')
        self.RegisterHelpText('valueColumn', '\nThe column whose mean will be calculated for each group.\n- Example: --valueColumn top_speed_mph')
        message += self.CreateHelpTextForOptions(['groupColumn','valueColumn'])
        return message
    def GetAutomationDescription(self):
        return 'Calculates the mean of a specified value column grouped by another column and sorts the result in descending order.'
    def GetKeywords(self):
        return ['mean', 'average', 'group', 'sort', 'descending']


