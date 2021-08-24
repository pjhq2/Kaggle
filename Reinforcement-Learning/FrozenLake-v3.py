import gym
from gym.envs.registration import register
# import sys, tty, termios
import msvcrt


# 키보드를 입력 받고 액션을 취하는 코드
# class _Getch:
#     def __call__(self):
#         fd = sys.stdin.fileno()
#         old_settings = msvcrt.tcgetattr(fd)
#         try:
#             tty.setraw(sys.stdin.fileno())
#             ch = sys.stdin.read(3)
#         finally:
#             msvcrt.tcsetattr(fd, msvcrt.TCSADRAIN, old_settings)
#         return chr
class getkey():
    def __call__(self):
        msvcrt.getch()
    # return msvcrt.getch()

inkey = getkey()  # 화살표 키를 통해서 게임 가능
# MACROS
LEFT = 0
DOWN = 1
RIGHT = 2
UP = 3

# Key mapping
arrow_keys = {
    # b'\xe0': UP,

    # '\x1b[A': UP,
    # '\x1b[B': DOWN,
    # '\x1b[C': RIGHT,
    # '\x1b[D': LEFT,

    b'w': UP,
    b's': DOWN,
    b'd': RIGHT,
    b'a': LEFT
}

# Register FrozemLake with is_slippery False
register(
    id='FrozenLake-v3',
    entry_point='gym.envs.toy_text:FrozenLakeEnv',
    kwargs={'map_name': '4x4', 'is_slippery': False}
)

env = gym.make('FrozenLake-v3')
env.render()  # Show the initial board

while True:
    # Choose an action from keyboard
    key = inkey
    print(f'key: {key}, {type(key)}')
    # if key not in arrow_keys.keys():
    #     print("Game aborted!")
    #     break

    action = arrow_keys[key]
    # action = 1
    state, reward, done, info = env.step(action)
    env.render()
    print("State: ", state, "Action: ", action, "Reward: ", reward, "Info: ", info)

    if done:
        print("Finished with reward", reward)
        break
