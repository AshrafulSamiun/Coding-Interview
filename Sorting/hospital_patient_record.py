

n=int(input().strip())
patient_list=[]
for _ in range(n):
    patient_id, name, age, severity = input().split()
    patient_list.append((int(patient_id), name, int(age), int(severity)))

patient_list.sort(key=lambda x: (-x[3], x[2]))

print("====================Output=======================")
for patient in patient_list:
    print(patient[0], patient[1], patient[2], patient[3])