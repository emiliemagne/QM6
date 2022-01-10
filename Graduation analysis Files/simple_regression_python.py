# This program performs a linear regression from data stored in a csv file,
# plots a scatter plot with line of best fit and saves it as a png image.

# The data file must be two columns of numbers, the x values and y values - no column labels, etc.
# It must be saved as a csv file (e.g. use "Save As" in Excel and choose csv format).
# It must be saved in the same folder as this program.
# See the file population_regression_data.csv for reference.

# In the next line, replace sample_boxplot_data.csv with the filename of your data:
data_filename = 'NoOutliersAgeVSSurvivalAllSexesAllGenes.csv'

# In the next line, replace boxplot with the filename you wish to save as:
output_filename = 'regression_figure.png'

# Use the next line to set figure height and width (experiment to check the scale):
figure_width, figure_height = 8,8

# You can ignore these two lines:
import matplotlib.pyplot as plt
import statsmodels.api as sms
import numpy as np

data = np.genfromtxt(data_filename,delimiter = ',')

# If there are errors importing the data, you can also copy the data in as a list.
# e.g. data = [1.95878982, 2.59203983, 1.22704688, ...]

# These lines extract the y-values and the x-values from the data:
x_values = data[:,0]
y_values = data[:,1]
x_values = [66252, 48412, 40088, 52226, 48703, 58377, 46820, 54940, 52002, 56365, 66787, 56023, 49544, 81219, 58121, 56763, 50407, 50482, 60524, 53601, 58675, 54646, 52685, 60231, 54524, 59510, 61633, 60075, 49462, 116100, 86553, 55522, 56027, 61359, 64944, 79944, 52620, 55967, 54028, 104486, 68666, 68991, 82783, 93024, 107740, 84291, 65499, 57714, 52327, 54545, 53663, 101031, 57426, 62999, 60240, 64304, 61024, 57258, 59449, 96610, 58052, 56563]
y_values = [2.0, 2.0, 5.0, 3.0, -1.0, 4.0, 1.0, 8.0, 7.0, 3.0, 1.0, 3.0, 5.0, 4.0, 5.0, -3.0, 3.0, 3.0, 0.0, 5.0, -4.0, 3.0, 3.0, 2.0, 1.0, 4.0, 3.0, 3.0, 10.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 3.0, 10.0, 1.0, 3.0, 0.0, 2.0, 0.0, 1.0, 1.0, 3.0, 11.0, 0.0, 5.0, 3.0, 2.0, 1.0, 3.0, -2.0, 2.0, 6.0, -3.0, 1.0, 1.0, 2.0, -3.0]
x_values = np.array([a for a in x_values if not np.isnan(a)])
y_values = np.array([a for a in y_values if not np.isnan(a)])

# These lines perform the regression procedure:
X_values = sms.add_constant(x_values)
regression_model_a = sms.OLS(y_values, X_values)
regression_model_b = regression_model_a.fit()
# and print a summary of the results:
print(regression_model_b.summary())
print() # blank line

# Now we store all the relevant values:
gradient  = regression_model_b.params[1]
intercept = regression_model_b.params[0]
Rsquared  = regression_model_b.rsquared
MSE       = regression_model_b.mse_resid
pvalue    = regression_model_b.f_pvalue

# And print them:
print("gradient  =", regression_model_b.params[1])
print("intercept =", regression_model_b.params[0])
print("Rsquared  =", regression_model_b.rsquared)
print("MSE       =", regression_model_b.mse_resid)
print("pvalue    =", regression_model_b.f_pvalue)

# This line creates the endpoints of the best-fit line:
x_lobf = [min(x_values),max(x_values)]
y_lobf = [x_lobf[0]*gradient + intercept,x_lobf[1]*gradient + intercept]

# This line creates the figure. 
plt.figure(figsize=(figure_width,figure_height))

# Uncomment these lines (remove the #) to set the axis limits (otherwise they will be set automatically):
#x_min,x_max = 0,5000000
#y_min,y_max = 0,5000000
#plt.xlim([x_min,x_max])
#plt.ylim([y_min,y_max])

# The next lines create and save the plot:
plt.plot(x_values,y_values,'b.',x_lobf,y_lobf,'r--')
plt.title('Relationship Between Median Household Income and Difference in Graduation Rate')
plt.xlabel('Median Household Income (in 2019 dollars), 2015-2019')
plt.ylabel('Difference in Graduation Rates in Percentage Points')
plt.savefig(output_filename)