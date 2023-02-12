#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2023/2/11 09:04
# @Author  : gy
# @File    : chat_api.py
# @Software: PyCharm

import openai
openai.api_key = "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"


def main_chat(prompt):
    if not prompt:
        return
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=prompt,
      temperature=0.9,
      max_tokens=150,
      top_p=1,
      frequency_penalty=0.0,
      presence_penalty=0.6,
      stop=[" Human:", " AI:"]
    )
    return response

"""

{
    "id": "cmpl-6iYfgNI4vjNiKkamgbyrb3imvwD9e",
    "object": "text_completion",
    "created": 1676077728,
    "model": "text-davinci-003",
    "choices": [
        {
            "text": "，实现算术运算\n\n#!/usr/bin/env python\n# -*- coding: utf-8 -*-\n\n# 加法\ndef addition(a, b):  \n    return a + b\n\n# 减法\ndef subtraction(a, b):  \n    return a - b\n\n# 乘法\ndef multiplication(a, b):  \n    return a * b\n\n# 除法\ndef division(a, b):  \n    return a / b\n\na = int(input(\"输入",
            "index": 0,
            "logprobs": null,
            "finish_reason": "length"
        }
    ],
    "usage": {
        "prompt_tokens": 11,
        "completion_tokens": 148,
        "total_tokens": 159
    }
}

"""
if __name__ == '__main__':
    a = main_chat('hahhaah')
    print(a.get("choices")[0].get("text"))