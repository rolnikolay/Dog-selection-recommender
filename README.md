# Dog selection recommender


The program prompts the user for some specific data about the lifestyle habits and factors that are important to consider when looking for the best dog breed match.
The program asks the following data:
Level of physical activity:  “Please, choose the level of your physical activity – high, medium, low: “ 
Property size: “How would you describe your living property? (big, medium, small)”
Place of living: “Please, specify, where do you live – city/countryside” 
Walking with a dog time: "How many hours are you going to spend on the walking?
Dog-size preference of the potential owner:" Which size of dog would you prefer? (big, medium, small)

For the user\`s convenience initially the program asks the user – would he/she like to answer all the needed questions within the program or would like to import the beforehand prepared file with all the information (answers).

![name-of-you-image](https://github.com/rolnikolay/Dog-selection-recommender/blob/main/Picture%201.png)


2. IF/while is used twice:
▪ Initially, the program gives choice to the user: he can redirect the program to the file with al the needed data or fill in the questionnaire – answer the questions one by one|
▪ (The program will either open and read the file OR collect the data from the user by prompting the questions)
The program will make the recommendation based on points collected by the user. Each answer will weight the certain amount of points. Then, the program will look through the condition:” if points in range” and the right choice will be made.

For instance, one of the windows looks like: 
Please, choose your level of activity? (Question) 
High Medium Low (Options)

3. easyGUI is used for prompting the quest ions when user decides to enter the data

4. Nested data structure:
▪ The program will make the initial decision from the nested data structure, that reflects the type of dog(companion/guard/sporting)
breeds_base = [[small breeds],[medium breeds],[large breeds]], [[small breeds],[medium breeds],[large breeds]], [[small breeds],[medium breeds],[large breeds]]
