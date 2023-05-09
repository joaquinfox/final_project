from halo import Halo
import time
question_counter = {
    "interval": 100,
    "frames": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
}

spinner = Halo(text="", text_color="green", spinner=question_counter)
# spinner = Halo(text='8 + 5 = ?', spinner='dots')
spinner.start()

start_time = time.time()
duration = 10 # seconds

# try:
#     while time.time() - start_time < duration:
#         print("hanga banga")
#         # Your code here
#         # time.sleep(2)
#         # answer = input("Answer: ")
#         # Check for user input
#         # if answer.isdigit() and answer == '13':
#         #     spinner.succeed(text=answer)
#         #     break
#     else:
#         spinner.warn(text='Timeout!')
# except KeyboardInterrupt:
#     spinner.stop(text='Interrupted by keyboard')
