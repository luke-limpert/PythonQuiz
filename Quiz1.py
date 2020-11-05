#Q1
# import re
# string = 'bat, lat, mat, bet, let, met, bit, lit, mit, bot, lot, mot'
# result = re.findall('b[ao]t', string)
# print(result)
# import numpy as np
# a = np.zeros((20,20))
# b = np.ones((20,20))

# #Q2
# def l2_dist(a, b):
#     result = ((a - b) * (a - b)).sum()
#     result = result ** 0.5
#     return result
# print(l2_dist(np.reshape(a, (20 * 20)), np.reshape(b, (20 * 20, 1))))

# #Q3
# a1 = np.random.rand(4)
# a2 = np.random.rand(4, 1)
# a3 = np.array([[1, 2, 3, 4]])
# a4 = np.arange(1, 4, 1)
# a5 = np.linspace(1, 4, 4)

# print(a1)
# print(a2)
# print(a3)
# print(a4)
# print(a5)

# print(a1.shape == a2.shape)
# print(a3.shape == a4.shape)

# print(a5.shape == a1.shape)

#Q4
import numpy as np

# old = np.array([[1, 1, 1], [1, 1, 1]])
# new = old
# new[0, :2] = 0
# print(old)

# #Q5
# Q5 = np.arange(0, 36, 1)
# print(Q5)

# Q5 = np.reshape(Q5, (6, 6))
# print(Q5)

# # print(Q5[[2, 4], [2, 4]])
# #output [14 28]

# # print(Q5[2:3,2:3])
# #output [[14]]

# #based on that the 1st 2:3 is row, and the second is column
# #so starting from row 0 i chose row 2 and column 2 which is 14
# # to select the entire range i would need to select 
# #row 2 and 3 and column 2 and 3

# print(Q5[2:4, 2:4])
#Q6
import re
# s = 'ACBCAC'

# print(re.findall('AC', s))

#Q7 
# s = 'ACAABAACAAAB'
# result = re.findall('A{1,2}', s)
# L = len(result)
# print(L)

#Q8 
# pn = '''Office of Research Administration: (734) 647-6333 | 4325 North Quad
# Office of Budget and Financial Administration: (734) 647-8044 | 309 Maynard, Suite 205
# Health Informatics Program: (734) 763-2285 | 333 Maynard, Suite 500
# Office of the Dean: (734) 647-3576 | 4322 North Quad
# UMSI Engagement Center: (734) 763-1251 | 777 North University
# Faculty Adminstrative Support Staff: (734) 764-9376 | 4322 North Quad'''

# phone = re.findall('[(]\d{3}[)]\s\d{3}[-]\d{4}', pn)
# print(phone)

# #Q9
# s = 'I refer to https://google.com and I never refer http://www.baidu.com if I have to search anything'
# domain_names = re.findall('(?<=[https]:\/\/)([A-Za-z0-9.]*)', s)
# #if you use http in the [https] portion of the regex it will only extract 
# #the baidu domain name, but this allows you to look up partial matches and full matches
# print(domain_names)
import re

text=r'''Everyone has the following fundamental freedoms:
(a) freedom of conscience and religion;
(b) freedom of thought, belief, opinion and expression, including freedom of the press and other media of communication;
(c) freedom of peaceful assembly; and
(d) freedom of association.
'''

pattern = '\(.\)'
print(len(re.findall(pattern, text)))