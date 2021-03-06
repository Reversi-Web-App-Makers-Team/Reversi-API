import os

from reversiAPI.players.player_dqn2 import PlayerDqn2
from reversiAPI.players.player_human import PlayerHuman
from reversiAPI.utils.reversi_processor import ReversiProcessor
from reversiAPI.utils.settings import DQN


def _human_vs_dqn(white, black, file_path):
    player_human_name = input("playerの名前は?:")
    player_white_instance = PlayerHuman(player_human_name, white)
    player_black_instance = PlayerDqn2(black, file_path)
    game = ReversiProcessor(
        player_white_instance=player_white_instance,
        player_black_instance=player_black_instance,
        options=None,
        play_game_num=1,
        display_board=True,
        display_result=True
    )
    game.progress()


def _main(file_path):
    _human_vs_dqn(1, -1, file_path)


if __name__ == '__main__':
    executing_file_path = os.path.dirname(os.path.abspath(__file__))
    pt_path = DQN['dqn2']
    path = os.path.join(executing_file_path, pt_path)
    _main(path)
