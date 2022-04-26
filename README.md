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

from Trivia import Client, EmptyToken

async def main() -> None:
	session_token = await Client.get_session_token()
	trivia_client = Client(session_token)
	
	try:
		data = await trivia_client.get_questions(amount=1)
	except EmptyToken:
		await trivia_client.reset_session_token()
	else:
		data = await trivia_client.get_questions(amount=1)
		
	print(data)
    
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
## `class` Client   
Sends a POST call to the API and gets the desired data.  

**Parameters**  
- session_token ( [str](https://docs.python.org/3/library/functions.html#str) ) - The session token.

**Methods**  
`async` [get_session_token](https://github.com/Marseel-E/opentdb-py/blob/main/README.md#async-clientget_session_token)  
`async` [reset_session_token](https://github.com/Marseel-E/opentdb-py/blob/main/README.md#async-clientreset_session_token)  
`async` [get_questions](https://github.com/Marseel-E/opentdb-py/blob/main/README.md#async-clientget_questions)  
`async` [get_categories](https://github.com/Marseel-E/opentdb-py/blob/main/README.md#async-clientget_categories)  
`async` [get_category_questions_count](https://github.com/Marseel-E/opentdb-py/blob/main/README.md#async-clientget_category_questions_count)  
`async` [get_global_questions_count](https://github.com/Marseel-E/opentdb-py/blob/main/README.md#async-clientget_global_questions_count)   
  
## `async` Client.get_session_token  
```py
await Client.get_session_token()
```
This function is a [coroutine](https://docs.python.org/3/library/asyncio-task.html#coroutine).  

Fetches a session token from the API.  

**Returns**  
Session Token.  

**Return Type**  
[str](https://docs.python.org/3/library/functions.html#str)  

## `async` Client.reset_session_token  
```py
await Client(...).reset_session_token()
```
This function is a [coroutine](https://docs.python.org/3/library/asyncio-task.html#coroutine).  

Resets the session token.  
  
## `async` Client.get_questions  
```py  
await Client(...).questions(   
  amount=10,  
  category=Category.undefined,  
  difficulty=Difficulty.undefined,  
  question_type=QuestionType.both,  
  encoding=ResponseEncoding.default  
)  
```  
This function is a [coroutine](https://docs.python.org/3/library/asyncio-task.html#coroutine).  

Fetches the requests amount of questions from the API with the appropriate parameters.  

**Parameters**  
- amount ( [int](https://docs.python.org/3/library/functions.html#int) ) - The amount of questions to return.  
- category ( [Category](https://github.com/Marseel-E/opentdb-py/blob/main/README.md#enum-category) ) - The category of questions.  
- difficulty ( [Difficulty](https://github.com/Marseel-E/opentdb-py/blob/main/README.md#enum-difficulty) ) - The difficulty of the question (undefined=any, easy, medium, hard).  
- question_type ( [QuestionType](https://github.com/Marseel-E/opentdb-py/blob/main/README.md#enum-questiontype) ) - The type of question (both, multiple choice, true/false).  
- encoding ( [ResponseEncoding](https://github.com/Marseel-E/opentdb-py/blob/main/README.md#enum-responseencoding) ) - The encoding of the API response.  

**Returns**  
A list of questions.  

**Return Type**  
[QuestionData](https://github.com/Marseel-E/opentdb-py/blob/main/README.md#type-questiondata)  
  
## `async` Client.get_categories  
```py
await Client(...).categories()
```
This function is a [coroutine](https://docs.python.org/3/library/asyncio-task.html#coroutine).  

Fetches a list of all categories the API has.  

**Returns**  
A list of categories.  

**Return Type**  
[CategoriesList](https://github.com/Marseel-E/opentdb-py/blob/main/README.md#type-categorieslist)  
   
## `async` Client.get_category_questions_count  
```py
await Client(...).category_questions_count(category=Category.general_knowledge)
```
This function is a [coroutine](https://docs.python.org/3/library/asyncio-task.html#coroutine).  

Fetches statistics about a specific category.

**Parameters**  
- category ( [Category](https://github.com/Marseel-E/opentdb-py/blob/main/README.md#enum-category) ) - The category to fetch data from.  

**Returns**  
Statistics about the category.  

**Return Type**  
[CategoryQuestionsCount](https://github.com/Marseel-E/opentdb-py/blob/main/README.md#type-categoryquestionscount)  
  
## `async` Client.get_global_questions_count  
```py
await Client(...).global_questions_count()
```
This function is a [coroutine](https://docs.python.org/3/library/asyncio-task.html#coroutine).  

Fetches statistics about all the categories.  

**Returns**  
Global statistics  

**Return Type**  
[GlobalQuestionsCount](https://github.com/Marseel-E/opentdb-py/blob/main/README.md#type-globalquestionscount)  
  
## `exception` NoResults  
```cmd
<NoResults>: [Code 1] Could not return results. The API doesn't have enough questions for your query. (Ex. Asking for 50 Questions in a Category that only has 20.)
```
This exception is raised when a `response_code` 1 is returned.  

The API doesn't have enough questions for the given query.  
  
## `exception` InvalidParameter  
```cmd
<InvalidParameter>: [Code 2] Contains an invalid parameter. Arguements passed in aren't valid. (Ex. Amount = Five)
```
This exception is raised when a `response_code` 2 is returned.  

One or more of the query parameters are invalid.  

## `exception` TokenNotFound  
```cmd
<TokenNotFound>: [Code 3] Session Token does not exist.
```
This exception is raised when a `response_code` 3 is returned.  

The session token was not specified.

## `exception` TokenEmpty
```cmd
<TokenEmpty>: [Code 4] Session Token has returned all possible questions for the specified query. Resseting the Token is necassery.
```
This exception is raised when a `response_code` 4 is returned.

The session token is about to expire. **(session tokens last 6 hours only)**
  
## `type` QuestionData  
```py
class QuestionData(TypedDict):
	category: str
	type: str
	difficulty: str
	question: str
	correct_answer: str
	incorrect_answers: List[str]
```
## `type` QuestionResponse  
```py
class QuestionResponse(TypedDict):
	response_code: int
	results: List[QuestionData]
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
	trivia_categories: List[CategoryData]
```
## `type` CategoryQuestionsCount  
```py
class CategoryQuestionsCount(TypedDict):
	category_id: int
	category_questions_count: List[_CategoryQuestionsCount]
```
## `type` GlobalQuestionsCount  
```py
class GlobalQuestionsCount(TypedDict):
	overall: _GlobalQuestionsCount
	categories: Dict[str, _GlobalQuestionsCount]
```
   
## `enum` ResponseEncoding  
```py
class ResponseEncoding(Enum):
	default: None = None
	url: str = "url3986"
	base64: str = "base64"
```
## `enum` Difficulty  
```py
class QuestionDifficulty(Enum):
	undefined: None = None
	easy: str = "easy"
	medium: str = "medium"
	hard: str = "hard"
```
## `enum` QuestionType  
```py
class QuestionType(Enum):
	both: None = None
	multiple_choice: str = "multiple"
	true_false: str = "boolean"
```
## `enum` Category  
```py
class QuestionCategory(Enum):
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
#### :scroll: [License](https://github.com/Marseel-E/opentdb-py/blob/main/LICENSE)
