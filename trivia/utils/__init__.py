"""
MIT License

Copyright (c) 2022 Marseel-E

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

__all__ = [
	'TokenResponse',
	'QuestionData',
	'QuestionResponse',
	'CategoryData',
	'CategoriesList',
	'CategoryQuestionsCount',
	'GlobalQuestionsCount',
	'NoResults',
	'InvalidParameter',
	'TokenNotFound',
	'TokenEmpty',
	'ResponseEncoding',
	'Difficulty',
	'QuestionType',
	'Category'
]


from typing import TypedDict, List, Dict

class TokenResponse(TypedDict):
	response_code: int
	response_message: str
	token: str

class QuestionData(TypedDict):
	category: str
	type: str
	difficulty: str
	question: str
	correct_answer: str
	incorrect_answers: List[str]

class QuestionResponse(TypedDict):
	response_code: int
	results: List[QuestionData]

class CategoryData(TypedDict):
	id: int
	name: str

class CategoriesList(TypedDict):
	trivia_categories: List[CategoryData]

class _CategoryQuestionsCount(TypedDict):
	total_questions_count: int
	total_easy_questions_count: int
	total_medium_questions_count: int
	total_hard_questions_count: int

class CategoryQuestionsCount(TypedDict):
	category_id: int
	category_questions_count: List[_CategoryQuestionsCount]

class _GlobalQuestionsCount(TypedDict):
	total_num_of_questions: int
	total_num_of_pending_questions: int
	total_num_of_verified_questions: int
	total_num_of_rejected_questions: int

class GlobalQuestionsCount(TypedDict):
	overall: _GlobalQuestionsCount
	categories: Dict[str, _GlobalQuestionsCount]


class NoResults(Exception):
	def __init__(self) -> str:
		super().__init__("[Code 1] Could not return results. The API doesn't have enough questions for your query. (Ex. Asking for 50 Questions in a Category that only has 20.)")	

class InvalidParameter(Exception):
	def __init__(self) -> str:
		super().__init__("[Code 2] Contains an invalid parameter. Arguements passed in aren't valid. (Ex. Amount = Five)")

class TokenNotFound(Exception):
	def __init__(self) -> str:
		super().__init__("[Code 3] Session Token does not exist.")

class TokenEmpty(Exception):
	def __init__(self) -> str:
		super().__init__("[Code 4] Session Token has returned all possible questions for the specified query. Resseting the Token is necassery.")


from enum import Enum

class ResponseEncoding(Enum):
	default: None = None
	url: str = "url3986"
	base64: str = "base64"

class Difficulty(Enum):
	undefined: None = None
	easy: str = "easy"
	medium: str = "medium"
	hard: str = "hard"

class QuestionType(Enum):
	both: None = None
	multiple_choice: str = "multiple"
	true_false: str = "boolean"

class Category(Enum):
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