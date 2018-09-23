#This program finds percentage of male and females
#09/23/2018
#CTI-110-P2HW2
#Preston Urbanek

males = int( input('Please enter the number of males in the class: '))
females = int( input('Please enter the number of females in the class: '))
totalStudents= males + females

malePercentage = ( males / totalStudents ) * 100
femalePercentage = ( females / totalStudents ) * 100

print( 'There are ' + str(totalStudents) + ' students in the class. ' + \
       format( malePercentage, '.2f' ) + '% of them are males and ' + \
       format( femalePercentage, '.2f' ) + '% of them are females')
