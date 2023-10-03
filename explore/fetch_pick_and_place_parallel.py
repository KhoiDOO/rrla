import gymnasium as gym
import numpy as np

# env = gym.make("FetchPickAndPlace-v2", render_mode="human")
# observation, info = env.reset(seed=42)

# action = policy(observation)  # User-defined policy function

# for idx in range(1000):
#     action = env.action_space.sample()
#     observation, reward, terminated, truncated, info = env.step(action)
    
#     if idx == 0:
#         print(observation.keys)
#         for key in observation:
#             print(key, observation[key])
#         print(reward)
#         print(info)
    
#     if terminated or truncated:
#         print(terminated)
#         print(truncated)
#         observation, info = env.reset()
# env.close()

def make_env(env_id, idx, capture_video, run_name, gamma):
    def thunk():
        if capture_video:
            env = gym.make(env_id, render_mode="rgb_array")
        else:
            env = gym.make(env_id, render_mode="human")
        env = gym.wrappers.FlattenObservation(env)  # deal with dm_control's Dict observation space
        env = gym.wrappers.RecordEpisodeStatistics(env)
        if capture_video:
            if idx == 0:
                env = gym.wrappers.RecordVideo(env, f"videos/{run_name}")
        env = gym.wrappers.ClipAction(env)
        env = gym.wrappers.NormalizeObservation(env)
        env = gym.wrappers.TransformObservation(env, lambda obs: np.clip(obs, -10, 10))
        env = gym.wrappers.NormalizeReward(env, gamma=gamma)
        env = gym.wrappers.TransformReward(env, lambda reward: np.clip(reward, -10, 10))
        return env

    return thunk

envs = gym.vector.SyncVectorEnv(
    [make_env("FetchPickAndPlace-v2", i, False, "Test", 0.99) for i in range(2)]
)


next_obs, _ = envs.reset()
for idx in range(1000):
    action = envs.action_space.sample()
    observation, reward, terminated, truncated, info = envs.step(action)
    
    if idx == 0:
        print(observation.shape)
        print(action.shape)
        print(reward.shape)
        print(terminated.shape)
        print(truncated.shape)
        print([info[key].shape for key in info])