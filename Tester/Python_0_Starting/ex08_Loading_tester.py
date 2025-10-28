from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

range_length = 333
sleep_time = 0.005

for elem in ft_tqdm(range(range_length)):
    sleep(sleep_time)
print()
for elem in tqdm(range(range_length)):
    sleep(sleep_time)
print()
