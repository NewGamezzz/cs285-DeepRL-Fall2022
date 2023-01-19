import gym

env = gym.make("MsPacman-v4", render_mode="human")

observation = env.reset(seed=42)
for _ in range(1000):
    # env.render()
    action = env.action_space.sample() # User-defined policy function
    observation, reward, terminated, info = env.step(action)

    if terminated:
        observation = env.reset()
env.close()