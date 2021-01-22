#!/usr/bin/env python
# coding: utf-8

# In[4]:


iceCreamRating = 3
sleepingRating = 8


# In[5]:


firstName = input('Please type your first name: ')
lastName = input('Please type your last name: ')
myName = firstName + ' ' + lastName


# In[6]:


happinessRating = (iceCreamRating + sleepingRating) / 2


# In[7]:


t1 = type(iceCreamRating)
t2 = type(sleepingRating)
t3 = type(happinessRating)
print("Ice Cream Rating Type: ", t1)
print("Sleeping Rating Type: ", t2)
print("Happiness Rating Type: ", t3)


# The data types make sense as integers were inputted for the first two ratings
# and the result (happinessRating) is likely to have a decimal.  Everything is
# as it was expected to be.

# In[8]:


print('My name is', firstName, 'and I give eating ice cream a score of', iceCreamRating, 'out of 10!')
print('I am', myName, 'and my sleeping enjoyment is', sleepingRating, 'out of 10!')
print('Based on the factors above, my happiness rating is', round(happinessRating, 1), 'out of 10, or', happinessRating*10, '%!')


# In[ ]:




