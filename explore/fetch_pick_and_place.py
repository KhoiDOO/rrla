import gymnasium as gym

env = gym.make("FetchPickAndPlace-v2", render_mode="human")
observation, info = env.reset(seed=42)

# action = policy(observation)  # User-defined policy function

for idx in range(1000):
    action = env.action_space.sample()
    observation, reward, terminated, truncated, info = env.step(action)
    
    if idx == 0:
        print(observation.keys)
        for key in observation:
            print(key, observation[key])
        print(reward)
        print(info)
    
    if terminated or truncated:
        print(terminated)
        print(truncated)
        observation, info = env.reset()
env.close()