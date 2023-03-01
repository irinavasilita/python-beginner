authors = 'Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni'

'''
Given a long string with the names separated by commas, 
create a list called author_names containing each individual 
author name as it’s own string.
'''

author_names = authors.split(',')

'''
Create another list called author_last_names that only contains 
the last names of the poets in the provided string.
'''
author_last_names = []
for author in author_names: 
  author_last_names.append(author.split()[-1])