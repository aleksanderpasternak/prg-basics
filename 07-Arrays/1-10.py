test_results = [
   False, True, False, True, True,
   True, True, False, True, True,
   False, True, True, True, False
]
question_number = len(test_results)
correct_answers = 0
for answer in test_results:
   if answer==True:
      correct_answers += 1

print('TEST STATISTICS')
print('===============')
print('Number of questions: ', question_number)
print('Number of correct answers: ', correct_answers)
print('Number of incorrect answers: ', question_number-correct_answers)
print('Percentage of correct answers: ', (correct_answers/question_number)*100,'%')