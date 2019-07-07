# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'
data=np.genfromtxt(path,delimiter=",",skip_header=1)
print(data)
print(type(data))
#New record
new_record=np.array([[50,  9,  4,  1,  0,  0, 40,  0]])

print(new_record)
census=np.concatenate((data,new_record),axis=0)
print(census)

#Code starts here



# --------------
#Code starts here
age=census[:,0]
print(age)
max_age=np.max(age)
min_age=np.min(age)
age_mean=np.mean(age)
age_std=np.std(age)
print(max_age)
print(min_age)
print(age_mean)
print(age_std)


# --------------

race=census[:,2]
print("length of complete data setup cencus is :  "+ str(len(race)))

race_0=census[census[:,2]==0]
race_1=census[census[:,2]==1]
race_2=census[census[:,2]==2]
race_3=census[census[:,2]==3]
race_4=census[census[:,2]==4]
#race_0=int(race_temp_0)
print("value of race_0 column is:")
print(race_0)
len_0=len(race_0)
print(len_0)

print("value of race_1 column is:")
print(race_1)
len_1=len(race_1)
print(len_1)

print("value of race_2 column is:")
print(race_2)
len_2=len(race_2)
print(len_2)

print("value of race_3 column is:")
print(race_3)
len_3=len(race_3)
print(len_3)

print("value of race_4 column is:")
print(race_4)
len_4=len(race_4)
print(len_4)

minimun_count=np.min([len_0,len_1,len_2,len_3,len_4])

if minimun_count==len_0:
    minority_race=0;
elif minimun_count==len_1:
    minority_race=1;
elif minimun_count==len_2:
    minority_race=2;
elif minimun_count==len_3:
    minority_race=3;
elif minimun_count==len_4:
    minority_race=4;

print(minority_race)



# --------------
#Code starts here
senior_citizens=census[census[:,0]>60]
#print(senior_citizens)
working_hours_sum=np.sum(senior_citizens[:,6])
print(working_hours_sum)
senior_citizens_len=len(senior_citizens[:,0])
avg_working_hours=working_hours_sum/senior_citizens_len
print(avg_working_hours)




# --------------
#Code starts here
high=census[census[:,1]>10];
low=census[census[:,1]<=10];
avg_pay_high=np.mean(high[:,7])
avg_pay_low=np.mean(low[:,7])
print(avg_pay_high);
print(avg_pay_low);


