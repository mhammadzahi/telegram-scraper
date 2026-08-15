from telethon.sync import TelegramClient
from dotenv import load_dotenv
import asyncio
import os
import random
import re


load_dotenv()

api_id = int(os.getenv('API_ID'))
api_hash = os.getenv('API_HASH')
entity_name = str(os.getenv('ENTITY_NAME'))

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
client = TelegramClient('abc_0639_session', api_id, api_hash, loop=loop)


async def main():
    entity = await client.get_entity(entity_name)

    counter = 0
    maximum = 20000
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    try:
        async for message in client.iter_messages(entity):
            counter += 1
            if counter > maximum:
                print('done!')
                break

            print(message.date, counter)
            if not message.text:
                continue

            email = re.search(email_pattern, message.text)
            if email:
                eml = email.group()
                print(eml)
                with open(f'{entity_name}_mails.txt', 'a', encoding='utf-8') as f:
                    f.write(eml + '\n')

            await asyncio.sleep(random.choice([2, 1]))
    except Exception as e:
        print(f'Error: {e}')
    finally:
        await client.disconnect()


if __name__ == '__main__':
    with client:
        client.loop.run_until_complete(main())