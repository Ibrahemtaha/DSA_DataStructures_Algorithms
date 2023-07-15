# num = int(input("How many numbers you want to add? "))
# list1 = [int(input()) for x in range(num)]
list1 = [45, 56, 33, 27, 17, 77, 36, 17, 45]
print("Unordered list is: ", list1)

for i in range(len(list1)-1):
    m_ind = i

    for j in range(i+1, len(list1)):
        if list1[j] < list1[m_ind]:
            m_ind = j

    if list1[i] != list1[m_ind]:
        list1[i], list1[m_ind] = list1[m_ind], list1[i]

print(list1)

# -----------------------------------------------------------

# list1 = [45, 56, 33, 27, 17, 77, 36, 17, 45]

# for i in range(len(list1)-1):
#     m_val = min(list1[i:])
#     m_ind = list1.index(m_val, i)  # start from i
#     if list1[i] != list1[m_ind]:
#         list1[i], list1[m_ind] = list1[m_ind], list1[i]

# print(list1)
