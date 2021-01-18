import pickle

# 1. Leader Numbers
leader = {}
leader['Jacore Baptise'] = '(845) 200-6250'
leader['Andrew'] = '(925) 727-4611'
leader['Richard'] = '(123) 456-7890'

# 2. create/open pod_nbrs.pkl file
pod_file = open('pod_nbrs.pkl', 'wb')

# 3. Write POD Leader number to a file
pickle.dump(leader,pod_file)

# 4. Member Numbers
member = {}
member['Moussa Ndiaye'] = '(123) 456-7890'
member['Morris Jones'] = '(925) 286-5922'
member['Prince Fields'] = '(510) 472-0804'
member['Akari Johnson'] = '(510) 500-2206'

# 5. Write Member numbers to pod_file
pickle.dump(member,pod_file)

# 6. Close pod_file
pod_file.close()

# 7. Open pod.file
pod_file = open('pod_nbrs.pkl', 'rb')

# 8. Leader numbers
print('Leaders: ')
for key,value in leader.item():
    print(key, value)

print('\n')

# 9. Print POD members
print('Members')

print('\n')

# 10. Close pod_file

