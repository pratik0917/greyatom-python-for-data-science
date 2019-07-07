# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 



# code starts here

bank=pd.read_csv(path);
categorical_var=bank.select_dtypes(include = 'object');
print(bank.columns)
print(categorical_var.columns)
numerical_var=bank.select_dtypes(include = 'number')

print(numerical_var)






# code ends here


# --------------
# code starts here
banks=bank.drop('Loan_ID',axis=1)
#print(banks.isnull().sum())
bank_mode=banks.mode()
#print(bank_mode)
#bank_mode_dict=bank_mode.to_dict()
#print(bank_mode_dict)
#banks=banks.fillna(value=bank_mode_dict)
#print(banks.isnull().sum())
Gen=bank_mode['Gender'][0]
Mar=bank_mode['Married'][0]
Dep=bank_mode['Dependents'][0]
Edu=bank_mode['Education'][0]

#print(Gen)
#banks['Gender']=banks['Gender'].fillna(bank_mode['Gender'][0])
#banks['Married']=banks['Married'].fillna(bank_mode['Married'][0])
#banks['Dependents']=banks['Dependents'].fillna(bank_mode['Dependents'][0])
#banks['Education']=banks['Education'].fillna(bank_mode['Education'][0])
#banks['Self_Employed']=banks['Self_Employed'].fillna(bank_mode['Self_Employed'][0])
#banks['ApplicantIncome']=banks['ApplicantIncome'].fillna(bank_mode['ApplicantIncome'][0])


for i in banks.columns:
    if banks[i].isnull:
        banks[i]=banks[i].fillna(bank_mode[i][0]);
    else:
        pass;





print(banks.isnull().sum())

#code ends here


# --------------
# Code starts here




#avg_loan_amount=banks.pivot_table(index=['Gender','Married','Self_Employed'],column='LoanAmount',value=banks['LoanAmount'].mean())


avg_loan_amount=pd.pivot_table(banks,aggfunc=np.mean,index=['Gender','Married','Self_Employed'],values=['LoanAmount'])
print(avg_loan_amount)


# code ends here



# --------------
# code starts here





SelfE_df= banks[(banks['Self_Employed'] == 'Yes') & (banks['Loan_Status'] == 'Y')]
loan_approved_se=SelfE_df['Self_Employed'].count()
print(loan_approved_se)

SelfNE_df= banks[(banks['Self_Employed'] == 'No') & (banks['Loan_Status'] == 'Y')]
loan_approved_nse=SelfNE_df['Self_Employed'].count()
print(loan_approved_nse)

percentage_se=(loan_approved_se/614)*100;
percentage_nse=(loan_approved_nse/614)*100;

print(percentage_nse);
print(percentage_se)


#

# code ends here


# --------------
# code starts here

loan_term=(banks['Loan_Amount_Term']).apply(lambda x:(x/12));
print(loan_term)
big_loan_term=loan_term[loan_term>=25].count()
print(big_loan_term)



# code ends here


# --------------
# code starts here
loan_groupby=banks.groupby('Loan_Status')
loan_groupby=loan_groupby['ApplicantIncome', 'Credit_History']
mean_values=loan_groupby.mean()
print(mean_values)
print(loan_groupby)




# code ends here


