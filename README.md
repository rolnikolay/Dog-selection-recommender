# Dog selection recommender


The program prompts the user for some specific data about the lifestyle habits and factors that are important to consider when looking for the best dog breed match.
The program asks the following data:
* Level of physical activity:  “Please, choose the level of your physical activity – high, medium, low: “ 
* Property size: “How would you describe your living property? (big, medium, small)”
* Place of living: “Please, specify, where do you live – city/countryside” 
* Walking with a dog time: "How many hours are you going to spend on the walking?
* Dog-size preference of the potential owner:" Which size of dog would you prefer? (big, medium, small)

For the user\`s convenience initially the program asks the user – would he/she like to answer all the needed questions within the program or would like to import the beforehand prepared file with all the information (answers).
![name-of-you-image](https://github.com/rolnikolay/Dog-selection-recommender/blob/main/Picture%201.png)

An example of question windows if the user chooses to answer within  the program :
![name-of-you-image](https://github.com/rolnikolay/Dog-selection-recommender/blob/main/Picture%202.png)
![name-of-you-image](https://github.com/rolnikolay/Dog-selection-recommender/blob/main/Picture%203.png)
![name-of-you-image](https://github.com/rolnikolay/Dog-selection-recommender/blob/main/Picture%204.png)

An example of user path if it was decided to upload a file:
![name-of-you-image](https://github.com/rolnikolay/Dog-selection-recommender/blob/main/Picture%205.png)
![name-of-you-image](https://github.com/rolnikolay/Dog-selection-recommender/blob/main/Picture%206.png)

The program will read the file data, find the answers and bring the result.

The program will make the recommendation based on points collected by the user. Each answer will weight the certain amount of points. Then, the program will look through the condition:” if points in range” and the right choice will be made.

For the final decision program will use nested data structure, having  the answer to the last question. The program will make the initial decision from the nested data structure, that reflects the type of dog(companion/guard/sporting)
breeds_base = [[small breeds],[medium breeds],[large breeds]], [[small breeds],[medium breeds],[large breeds]], [[small breeds],[medium breeds],[large breeds]

The program outputs the most matching breed according to the inserted data (options are offered based on different breeds’ specific characteristics match with the user\`s desires)
Possible outputs (look at print lines):
![name-of-you-image](https://github.com/rolnikolay/Dog-selection-recommender/blob/main/Picture%207.png)

All the outputs consists of some specific offers + hyperlink that can be then inserted to the SE and used + the recommendation to consider adoption from the shelter.
