import easygui

#Asking questions
def ask_questions():
  choices_for_level_of_activity = ['high', 'medium', 'low']    
  level_of_activity = easygui.choicebox("What is your level of activity (high, medium, low)? ",title = "Dog selection recommender", choices = choices_for_level_of_activity)

  
  choices_for_type_of_living_property = ['big', 'medium', 'small']
  type_of_living_property = easygui.choicebox("How would you describe your living property? (big, medium, small) ",title = "Dog selection recommender",choices = choices_for_type_of_living_property)


  choices_for_place_of_living = ['city','countryside']
  place_of_living = easygui.choicebox("Do you live in city or in countryside? ",title = "Dog selection recommender", choices =choices_for_place_of_living)


  choices_for_hours_spent_on_walking = [0,1,2,3,4,5,6,7,8]
  hours_spent_on_walking = int(easygui.choicebox("How many hours are you going to spend on that walking (it should not be more than 8 hours)? ",title = "Dog selection recommender", choices = choices_for_hours_spent_on_walking))

  
  choices_for_size_of_dog = ['big', 'medium', 'small']
  size_of_dog = easygui.choicebox("Which size of dog would you prefer? (big, medium, small) (last question) ",title = "Dog selection recommender", choices = choices_for_size_of_dog)

      
  return level_of_activity,type_of_living_property,place_of_living,hours_spent_on_walking,size_of_dog

#import file with answers
def import_file():
  file=None
  while file==None:
    file_name = easygui.enterbox("Please, specify the file name: ",title = "Dog selection recommender")
    try:
      file = open(file_name)
      file=file.read()
    except:
      easygui.msgbox("seems like smth is wrong - check the file")
    
  easygui.msgbox("Your answers were: "+str(file.split()),title = "Dog selection recommender")
  move_next=easygui.ynbox("The input is correct? Do you want to change your answers? ", title = "Dog selection recommender")
  while move_next ==1:
    file_name = easygui.enterbox("Please, specify the file name: ", title = "Dog selection recommender")
    file = open(file_name)
    file=file.read()
    easygui.msgbox("Your answers were: "+str(file.split()), title = "Dog selection recommender")
    move_next=easygui.ynbox("The input is correct? Do you want to change your answers? ", title = "Dog selection recommender")
  return file.split()


#Map answers to points
def count_points(level_of_activity,type_of_living_property,place_of_living,hours_spent_on_walking,size_of_dog):  
  point_level_of_activity=0
  point_type_of_living_property=0
  point_place_of_living=0
  point_hours_spent_on_walking=0
  point_size_of_dog=0
  for key in dict_for_level_of_activity:
      if level_of_activity in key:
          point_level_of_activity = int(dict_for_level_of_activity[key])
  for key in dict_for_type_of_living_property:
      if type_of_living_property in key:
          point_type_of_living_property = int(dict_for_type_of_living_property[key])
  for key in dict_for_place_of_living:
      if place_of_living in key:
          point_place_of_living = int(dict_for_place_of_living[key])
  for key in dict_for_hours_spent_on_walking:
      if hours_spent_on_walking in key:
          point_hours_spent_on_walking = int(dict_for_hours_spent_on_walking[key])
  for key in dict_for_size_of_dog:
      if size_of_dog in key:
          point_size_of_dog = int(dict_for_size_of_dog[key])
  return point_level_of_activity+point_type_of_living_property+point_place_of_living+point_hours_spent_on_walking+point_size_of_dog

#function to get dog breed based on final number of points and size of dog
def points_to_dog_breed(total_points,size_of_dog):
  total_points = int(total_points)
  for key in dict_total_points_to_general_dogs_mapping:
      if total_points in key:
        easygui.msgbox('Thanks for the test! The good  breed matches might be '+str(dict_total_points_to_general_dogs_mapping[key][size_of_dog])+'. You can find more https://www.purina.com/dogs/dog-breeds/collections/small-dog-breeds-dogs/ or consider the adoption from the shelter!', title = "Dog selection recommender")


#The main function
def main_function():
  easygui.msgbox("To decide which dog is a best fit for you - you would have to answer 5 questions.",title = "Dog selection recommender")
  easygui.msgbox("Or are you ready to import the answers? if you answer 'yes' - you can import a file by name. If you answer 'no' - you will be asked 5 questions",ok_button = "Let's start", title = "Dog selection recommender")
  if  easygui.ynbox("Do you want to import answers?", title = "Dog selection recommender"):
    level_of_activity,type_of_living_property,place_of_living,hours_spent_on_walking,size_of_dog = import_file()
  else:
    level_of_activity,type_of_living_property,place_of_living,hours_spent_on_walking,size_of_dog = ask_questions()
  hours_spent_on_walking = int(hours_spent_on_walking)
  total_points=count_points(level_of_activity,type_of_living_property,place_of_living,hours_spent_on_walking,size_of_dog)
  easygui.msgbox('Congrats, you have successfully completed the test and you have got '+str(total_points)+' points. You have also selected a '+size_of_dog+' dog.',title = "Dog selection recommender")
  points_to_dog_breed(total_points,size_of_dog)



#Dictionary list
dict_for_level_of_activity = {
    "high":"5",
    "medium":"3",
    "low":"1"
}

dict_for_type_of_living_property = {
    "big":"5",
    "medium":"3",
    "small":"1"
}

dict_for_place_of_living = {
    "city":"3",
    "countryside":"5"
}

dict_for_hours_spent_on_walking = {
    (0,1):"2",
    (2,3):"3",
    (4,5,6,7,8,9):"5"
}

dict_for_size_of_dog = {
    "big":"5",
    "medium":"3",
    "small":"1"
}

dict_total_points_to_general_dogs_mapping = {
    (8,9,10,11,12,13,14,15): {'small': 'Terriers, Pinchers, Corgis', 'medium': 'Poodle, Shepherd, German Pointer', 'big': 'Husky'},
    (16,17,18,19,20,21): {'small': 'Papillon, Pinchers', 'medium': 'Retrievers, Collie, German Shepherds', 'big': 'Great Pyrenees dog'},
    (22,23,24,25,26): {'small': 'Spaniels, Pinchers', 'medium': 'Labradors, Belgian Sheepdog, German Shepherd', 'big': 'Airedele Terrier, Malamute, Afgan, Bernese Mountain dog'}
}

main_function()




