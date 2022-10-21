# this program ELT program will read and generate "needs testing" csv from benchmark data

import pandas as pd

##############################read excel files with sheets


dict_df = pfd.read_excel('C:\Users\jcassibba\Desktop\Intervention Benchmark data\data\Math\benchmark 2 results',sheet_name=['grade 9','grade 10','grade 11','grade 12'])


#############################load dataframes



grade_9_df = dict_df.get('grade 9') 
grade_10_df = dict_df.get('grade 10')
grade_11_df = dict_df.get('grade 11')
grade_12_df = dict_df.get('grade 12')



##########################print dfs (check)



#print(grade_9_df)
#print(grade_10_df)
#print(grade_11_df)
#print(grade_12_df)

print(dict_df)


####################combine all dfs in to 1



#results_df = pd.merge(grade_9_df, grade_10_df, grade_11_df, grade_12_df, on = "Student")

#print(results) #check



######################remove columns 2 - 7 from df


#del results_df["SIS Primary Key",	"Points Earned",	"Points Available",	"% Correct",	"Performance Level*"]
del dict_df["SIS Primary Key",	"Points Earned",	"Points Available",	"% Correct",	"Performance Level*"]

#print(results_df) #check
print(dict_df) #check



#############################make array of all column 1 entries with "not tested" in column 2


x=[]
i = 1
for i in 'Recommendation': 
    if i == "Not Tested":
        S == i in 'Student'
        x.append(S)
    i += 1

print(x) #check

###############################change array to df



needs_Testing_df = pd.DataFrame(x)



###############################print df


print(needs_Testing_df) #check


#####################write needs_Testing_df to csv

needs_testing = open("needs_testing.csv","w")
needs_testing.write(needs_Testing_df)
needs_testing.close

