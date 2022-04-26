# opentdb-py
Python wrapper for the open-trivia-database API
# Installation  
```cmd
py -m pip install -U opentdb-py

# latest (unstable)
py -m pip install -U git+https://github.com/Marseel-E/opentdb-py
```
# Quickstart  
```py
import asyncio

from trivia import Get
from rich import print_json


async def main() -> None:
  print_json(await Get.questions(amount=1))
  
if __name__ == '__main__:
  asyncio.run(main())
```
```json
{
  "category":"Entertainment: Video Games",
  "type":"boolean",
  "difficulty":"medium",
  "question":"In the Resident Evil series, Leon S. Kennedy is a member of STARS.",
  "correct_answer":"False",
  "incorrect_answers":["True"]
}
```
# Documentation  
## `class` Get  
Sends a POST call to the API and gets the desired data.  
**Methods**  
`async` [questions](async-Get.questions)  
`async` [categories](async-Get.categories)  
`async` [category_questions_count](async-Get.category_questions_count)  
`async` [global_questions_count](async-Get.global_questions_count)  
<hr />
## `async` Get.questions  
```py
await Get.questions(
  amount=10,
  category=QuestionCategory.undefined,
  difficulty=QuestionDifficulty.undefined,
  _type=QuestionType.both,
  encoding=ResponseEncoding.default
)
```
This function is a [coroutine](https://docs.python.org/3/library/asyncio-task.html#coroutine).  

Fetches the requests amount of questions from the API with the appropriate parameters.  

**Parameters**  
- amount ( [int](https://docs.python.org/3/library/functions.html#int) ) - The amount of questions to return.  
- category ( [QuestionCategory]() ) - The category of questions.  
- difficulty ( [QuestionDifficulty]() ) - The difficulty of the question (undefined=any, easy, medium, hard).  
- _type ( [QuestionType]() ) - The type of question (both, multiple choice, true/false).  
- encoding ( [ResponseEncoding]() ) - The encoding of the API response.  

**Returns**  
A list of questions.  

**Return Type**  
[QuestionData]()  
<hr />
## `async` Get.categories  
```py
await Get.categories()
```
This function is a [coroutine](https://docs.python.org/3/library/asyncio-task.html#coroutine).  

Fetches a list of all categories the API has.  

**Returns**  
A list of categories.  

**Return Type**  
[CategoriesList]()  
<hr />
## `async` Get.category_questions_count  
```py
await Get.category_questions_count(category=QuestionCategory.general_knowledge)
```
This function is a [coroutine](https://docs.python.org/3/library/asyncio-task.html#coroutine).  

Fetches statistics about a specific category.

**Parameters**  
- category ( [QuestionCategory]() ) - The category to fetch data from.  

**Returns**  
Statistics about the category.  

**Return Type**  
[CategoryQuestionsCount]()  
<hr />
## `async` Get.global_questions_count  
```py
await Get.global_questions_count()
```
This function is a [coroutine](https://docs.python.org/3/library/asyncio-task.html#coroutine).  

Fetches statistics about all the categories.  

**Returns**  
Global statistics  

**Return Type**  
[GlobalQuestionsCount]()  
<hr />
## `exception` NoResults  
```cmd
<NoResults>: [Code 1] Could not return results. The API doesn't have enough questions for your query. (Ex. Asking for 50 Questions in a Category that only has 20.)
```
This exception is raised when a `response_code` 1 is returned.  

The API doesn't have enough questions for the given query.  
<hr />
## `exception` InvalidParameter  
```cmd
<InvalidParameter>: [Code 2] Contains an invalid parameter. Arguements passed in aren't valid. (Ex. Amount = Five)
```
This exception is raised when a `response_code` 2 is returned.  

One or more of the query parameters are invalid.  
<hr />
## `type` QuestionData  
```py
class QuestionData(TypedDict):
	category: str
	type: str
	difficulty: str
	question: str
	correct_answer: str
	incorrect_answers: list[str]
```
## `type` QuestionResponse  
```py
class QuestionResponse(TypedDict):
	response_code: int
	results: list[QuestionData]
```
## `type` CategoryData  
```py
class CategoryData(TypedDict):
	id: int
	name: str
```
## `type` CategoriesList  
```py
class CategoriesList(TypedDict):
	trivia_categories: list[CategoryData]
```
## `type` CategoryQuestionsCount  
```py
class CategoryQuestionsCount(TypedDict):
	category_id: int
	category_questions_count: list[_CategoryQuestionsCount]
```
## `type` GlobalQuestionsCount  
```py
class GlobalQuestionsCount(TypedDict):
	overall: _GlobalQuestionsCount
	categories: dict[str, _GlobalQuestionsCount]
```
<hr />
## ResponseEncoding  
```py
class ResponseEncoding(TypedDict):
	default: None = None
	url: str = "url3986"
	base64: str = "base64"
```
## QuestionDifficulty  
```py
class QuestionDifficulty(TypedDict):
	undefined: None = None
	easy: str = "easy"
	medium: str = "medium"
	hard: str = "hard"
```
## QuestionType  
```py
class QuestionType(TypedDict):
	both: None = None
	multiple_choice: str = "multiple"
	true_false: str = "boolean"
```
## QuestionCategory  
```py
class QuestionCategory(TypedDict):
	undefined: None = None
	general_knowledge: int = 9
	entertainment_books: int = 10
	entertainment_film: int = 11
	entertainment_music: int = 12
	entertainment_music_and_theatres: int = 13
	entertainment_television: int = 14
	entertainment_video_games: int = 15
	entertainment_board_games: int = 16
	science_and_nature: int = 17
	science_computers: int = 18
	science_mathematics: int = 19
	mythology: int = 20
	sports: int = 21
	geography: int = 22
	history: int = 23
	politics: int = 24
	art: int = 25
	celebrities: int = 26
	animals: int = 27
	vehicles: int = 28
	entertainment_comics: int = 29
	science_gadgets: int = 30
	entertainment_japanese_anime_and_manga: int = 31
	entertainment_cartoons_and_animations: int = 32
```
