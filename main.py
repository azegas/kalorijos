import ollama
import time

start_time = time.time()

response = ollama.chat(
    model='llava:13b',
    messages=[
        {'role': 'user',
         'content': 'Describe this meal in one sentence. Also, how many calories approximately in it?:',
         'images': ['./images/kotletai.jpg']
        }
    ]
)

print(response['message']['content'])

end_time = time.time()
elapsed_time = end_time - start_time
hours = int(elapsed_time // 3600)
minutes = int((elapsed_time % 3600) // 60)
seconds = int(elapsed_time % 60)
print(f"Time taken: {hours:02d}:{minutes:02d}:{seconds:02d}")