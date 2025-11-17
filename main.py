#Working with sets
from pyscript import display #type: ignore


studentsclub1 = {'Miguel', 'Aj', 'Carl', 'Martina'}
studentsclub2 = {'Sang-heon', 'Skyler', 'Carl', 'Jalainie'}

display(studentsclub1 | studentsclub2, target='output') # Union
display(studentsclub1 & studentsclub2, target='output2') # Intersection
display(studentsclub1 - studentsclub2, target='output3') # Difference
display(studentsclub2 - studentsclub1, target='output4') # Difference
display(studentsclub1 ^ studentsclub2, target='output5') # Symmetric