# tuition increase

tuition = 45000

increase_rate = 0.03

print("Years\t\tTuition")
print("---------------------------")

for year in range(5):
    
    tuition_increase = tuition * increase_rate
    tuition += tuition_increase
    
    print(year + 1, '\t\t', format(tuition, '.2f'))