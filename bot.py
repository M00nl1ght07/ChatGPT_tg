from aiogram import Bot, Dispatcher, executor, types
import logging
import openai

logging.basicConfig(level=logging.INFO)

chat_api = "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"
bot = Bot(token='6256047443:AAEBbAzxQ5m9U_7_kaOectZBQ0sQLFgeyWo')
dp = Dispatcher(bot)

@dp.message_handler()
async def chat_cmd(message: types.Message):
    openai.api_key = chat_api
    model_engine = "text-davinci-003"
    completation = openai.Completion.create(
        engine = model_engine,
        prompt=message.text,
        max_tokens = 1024,
        n = 1,
        stop = None,
        temperature = 0.5
    )
    response = completation.choices[0].text
    await message.reply(f"{response}")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)