from rl_coach.agents.rainbow_dqn_agent import RainbowDQNAgentParameters
from rl_coach.base_parameters import VisualizationParameters, PresetValidationParameters, TaskParameters, Frameworks
from rl_coach.core_types import TrainingSteps, EnvironmentEpisodes, EnvironmentSteps, RunPhase
from rl_coach.environments.gym_environment import GymVectorEnvironment
from rl_coach.graph_managers.basic_rl_graph_manager import BasicRLGraphManager
from rl_coach.graph_managers.graph_manager import ScheduleParameters
from rl_coach.schedules import LinearSchedule
from rl_coach.exploration_policies.e_greedy import EGreedyParameters
from rl_coach.filters.filter import NoInputFilter, NoOutputFilter, InputFilter
from rl_coach.filters.observation.observation_stacking_filter import ObservationStackingFilter
from rl_coach.filters.observation.observation_to_uint8_filter import ObservationToUInt8Filter
from rl_coach.memories.memory import MemoryGranularity
from markov import environments

####################
# Graph Scheduling #
####################
schedule_params = ScheduleParameters()
schedule_params.improve_steps = TrainingSteps(100000)       #Changing to 100K
schedule_params.steps_between_evaluation_periods = EnvironmentEpisodes(40)
schedule_params.evaluation_steps = EnvironmentEpisodes(5)
schedule_params.heatup_steps = EnvironmentSteps(0)

#########
# Agent #
#########
agent_params = RainbowDQNAgentParameters()

agent_params.network_wrappers['main'].learning_rate = 0.0003
agent_params.network_wrappers['main'].input_embedders_parameters['observation'].activation_function = 'relu'
agent_params.network_wrappers['main'].middleware_parameters.activation_function = 'relu'
agent_params.network_wrappers['main'].batch_size = 64
agent_params.network_wrappers['main'].optimizer_epsilon = 1e-5
agent_params.network_wrappers['main'].adam_optimizer_beta2 = 0.999

agent_params.algorithm.discount = 0.999
#agent_params.algorithm.optimization_epochs = 10
agent_params.algorithm.num_steps_between_copying_online_weights_to_target = EnvironmentEpisodes(20)
agent_params.algorithm.num_consecutive_playing_steps = EnvironmentEpisodes(20)
agent_params.exploration = EGreedyParameters()
agent_params.memory.max_size = (MemoryGranularity.Transitions, 10**5)


###############
# Environment #
###############
Training_Ground_Filter = InputFilter(is_a_reference_filter=True)


env_params = GymVectorEnvironment()
env_params.level = 'Mars-v1'


vis_params = VisualizationParameters()
vis_params.dump_csv = True
vis_params.dump_signals_to_csv_every_x_episodes = 1
vis_params.tensorboard = True

########
# Test #
########
preset_validation_params = PresetValidationParameters()
preset_validation_params.test = True
preset_validation_params.min_reward_threshold = 2000
preset_validation_params.max_episodes_to_achieve_reward = 1000



graph_manager = BasicRLGraphManager(agent_params=agent_params, env_params=env_params, schedule_params=schedule_params,
                                    vis_params=vis_params, preset_validation_params=preset_validation_params)

