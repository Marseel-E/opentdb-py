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
	'Get',
	'QuestionData',
	'QuestionResponse',
	'CategoryData',
	'CategoriesList',
	'_CategoryQuestionCount',
	'CategoryQuestionCount',
	'_GlobalQuestionCount',
	'GlobalQuestionCount',
	'NoResults',
	'InvalidParameter',
	'ResponseEncoding',
	'QuestionDifficulty',
	'QuestionType',
	'QuestionCategory'
]

from typing import TypedDict


class QuestionData(TypedDict):
	category: str
	type: str
	difficulty: str
	question: str
	correct_answer: str
	incorrect_answers: list[str]

class QuestionResponse(TypedDict):
	response_code: int
	results: list[QuestionData]

class CategoryData(TypedDict):
	id: int
	name: str

class CategoriesList(TypedDict):
	trivia_categories: list[CategoryData]

class _CategoryQuestionsCount(TypedDict):
	total_questions_count: int
	total_easy_questions_count: int
	total_medium_questions_count: int
	total_hard_questions_count: int

class CategoryQuestionsCount(TypedDict):
	category_id: int
	category_questions_count: list[_CategoryQuestionsCount]

class _GlobalQuestionsCount(TypedDict):
	total_num_of_questions: int
	total_num_of_pending_questions: int
	total_num_of_verified_questions: int
	total_num_of_rejected_questions: int

class GlobalQuestionsCount(TypedDict):
	overall: _GlobalQuestionsCount
	categories: dict[str, _GlobalQuestionsCount]


class NoResults(Exception):
	def __init__(self) -> str:
		super().__init__("[Code 1] Could not return results. The API doesn't have enough questions for your query. (Ex. Asking for 50 Questions in a Category that only has 20.)")	

class InvalidParameter(Exception):
	def __init__(self) -> str:
		super().__init__("[Code 2] Contains an invalid parameter. Arguements passed in aren't valid. (Ex. Amount = Five)")


class ResponseEncoding(TypedDict):
	default: None = None
	url: str = "url3986"
	base64: str = "base64"

class QuestionDifficulty(TypedDict):
	undefined: None = None
	easy: str = "easy"
	medium: str = "medium"
	hard: str = "hard"

class QuestionType(TypedDict):
	both: None = None
	multiple_choice: str = "multiple"
	true_false: str = "boolean"

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


import aiohttp


class Get:
	@classmethod
	async def _request(self, endpoint: str, params: dict | None = {}) -> CategoriesList | CategoryQuestionsCount | GlobalQuestionsCount | QuestionResponse:
		async with aiohttp.ClientSession() as session:
			async with session.get(f"https://opentdb.com/{endpoint}", params=params) as response:
				return await response.json()

	@classmethod
	async def questions(self, 
		amount: int = 10, 
		category: QuestionCategory = QuestionCategory.undefined, 
		difficulty: QuestionDifficulty = QuestionDifficulty.undefined, 
		_type: QuestionType = QuestionType.both, 
		encoding: ResponseEncoding = ResponseEncoding.default
	) -> QuestionData:
		kwargs = {'amount': amount}

		for key, value in {
			'category': category,
			'difficulty': difficulty,
			'type': _type,
			'encode': encoding
		}.items():
			if value is not None:
				kwargs[key] = value

		data = await self._request("api.php", kwargs)

		if data['response_code'] == 1:
			raise NoResults()
		if data['response_code'] == 2:
			raise InvalidParameter()

		return data['results']

	@classmethod
	async def categories(self) -> CategoriesList:
		return await self._request("api_category.php")

	@classmethod
	async def category_questions_count(self, category: QuestionCategory) -> CategoryQuestionsCount:
		return await self._request("api_count.php", params={'category': category})

	@classmethod
	async def global_questions_count(self) -> GlobalQuestionsCount:
		return await self._request("api_count_global.php")
