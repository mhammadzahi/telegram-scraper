from telethon.sync import TelegramClient
import asyncio
import re
import random

from dotenv import load_dotenv
import os


load_dotenv()


api_id = int(os.getenv('API_ID'))
api_hash = os.getenv('API_HASH')
phone_number = os.getenv('PHONE_NUMBER')


client = TelegramClient('_0639_session', api_id, api_hash)

async def main():
    entity = await client.get_entity('UAE_ABU_DHABI_jobs')

    err = False
    counter = 0
    maximum = 3000
    email_list = []
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    async for message in client.iter_messages(entity):
        try:
            err = False
            counter = counter + 1
            if counter <= maximum:
                print(message.date, counter)
                if message.text:
                    email = re.search(email_pattern, message.text)
                    if email:
                        eml = email.group()
                        email_list.append(eml)
                        print(eml)

                else:
                    continue

                await asyncio.sleep(random.choice([2, 1]))

            else:
                print('done!')
                break

        except Exception as e:
            err = True
            print(f'Error e: {e}')
            continue

        except TypeError as te:
            err = True
            print(f'Error te: {te}')
            continue
        
        except ValueError as ve:
            err = True
            print(f'Error ve: {ve}')
            continue

        finally:
            if err:
                print("finally")
                continue


    with open('data_UAE_ABU_DHABI_jobs__.txt', 'w') as f:
        for email_ in email_list:
            f.write(email_ + '\n')


    await client.disconnect()


with client:
    client.loop.run_until_complete(main())