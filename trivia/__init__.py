from __future__ import annotations

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

__all__ = ['Client']

__title__ = 'opentdb-py'
__author__ = 'Marseel Eeso'
__license__ = 'MIT'
__copyright__ = 'Copyright 2022-present Marseel Eeso'
__version__ = '2.0.0'
# __path__ = __import__('pkgutil').extend_path(__path__, __name__)

import aiohttp

from typing import Optional, Union

from utils import *


API_BASE = "https://opentdb.com/"


class Client:
	def __init__(self, session_token: str) -> None:
		self.session_token = session_token
		self.session: Optional[aiohttp.ClientSession] = None

	async def __aenter__(self) -> "Client":
		self.session = aiohttp.ClientSession()
		return self

	async def __aexit__(self) -> None:
		await self.session.close()

	async def close_session(self) -> None:
		assert session is not None
		await self.session.close()

	@staticmethod
	async def check_response(response_code: int) -> None:
		if response_code == 1:
			raise NoResults()
		if response_code == 2:
			raise InvalidParameter()
		if response_code == 3:
			raise TokenNotFound()
		if response_code == 4:
			raise TokenEmpty()

	@classmethod
	async def get_session_token(cls) -> TokenResponse:
		async with aiohttp.ClientSession() as session:
			async with session.get(API_BASE + "api_token.php", params={'command': 'request'}) as response:
				data = await response.json()

				await cls.check_response(data['response_code'])

				return data['token']

	async def reset_session_token(self) -> None:
		self.token = await self._request(endpoint="api_token.php", command="reset")

	async def _request(self, endpoint: str, **params) -> Union[CategoriesList, CategoryQuestionsCount, GlobalQuestionsCount, QuestionResponse]:
		params['token'] = self.token

		if self.session is None:
			self.session = aiohttp.ClientSession()
		
		async with self.session.get(API_BASE + endpoint, params=params) as response:
			return await response.json()

	async def get_questions(self, 
		amount: int = 10, 
		category: Optional[Category] = Category.undefined, 
		difficulty: Optional[Difficulty] = Difficulty.undefined, 
		question_type: Optional[QuestionType] = QuestionType.both, 
		encoding: Optional[ResponseEncoding] = ResponseEncoding.default
	) -> QuestionData:
		kwargs = {'amount': amount}

		for key, value in {
			'category': category,
			'difficulty': difficulty,
			'type': question_type,
			'encode': encoding
		}.items():
			if value.value is not None:
				kwargs[key] = value.value

		data = await self._request("api.php", **kwargs)

		await self.check_response(data['response_code'])

		return data['results']

	async def get_categories(self) -> CategoriesList:
		return await self._request("api_category.php")

	async def get_category_questions_count(self, category: Category) -> CategoryQuestionsCount:
		return await self._request("api_count.php", category=category.value)

	async def get_global_questions_count(self) -> GlobalQuestionsCount:
		return await self._request("api_count_global.php")
