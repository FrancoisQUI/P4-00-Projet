from pprint import pprint

from colorama import Fore

from Views.tournament_view import TournamentView
from Models.tournament import Tournament
from Core.controller import Controller
from player_controller import PlayerController
from turn_controller import TurnController
from player_view import PlayerView
from turn_view import TurnView
from match_view import MatchView


class TournamentController(Controller):

    def __init__(self):
        super().__init__()
        self.view = TournamentView()
        self.view.clear()
        self.logger.info("TournamentController constructor")

    @staticmethod
    def create_tournament():
        tournament_data = TournamentView.create_tournament_form()
        tournament = Tournament()
        tournament.deserialize_tournament_data(tournament_data)
        tournament.save_new()
        return tournament

    @classmethod
    def select_tournament(cls):
        tournament_name = TournamentView.select_tournament()
        if tournament_name is not None:
            tournament_data = Tournament.find_one_by_name(
                tournament_name)
            tournament = Tournament()
            tournament.deserialize_tournament_data(tournament_data)
            return tournament
        else:
            return None

    @classmethod
    def manage_tournament_action(cls, tournament: Tournament):
        if tournament.ongoing_turn is not None:
            print("Ongoing Turn")
            TurnView.show_turn(tournament.ongoing_turn)

        action = TournamentView.manage_tournament_action(tournament)

        if action == 'Add new player':
            PlayerController.create_player(tournament)
        elif action == 'Add existing player':
            PlayerController.add_existing_player(tournament)
        elif action == 'Compute first turn':
            tournament.compute_round()
            TurnView.show_turn(tournament.ongoing_turn)
        elif action == 'Enter turn scores':
            TurnView.show_turn(tournament.ongoing_turn)
            TurnView.wait_user_action()
            TurnController.set_scores(tournament.ongoing_turn)
            tournament.close_ongoing_turn()
        elif action == 'Compute next turn':
            tournament.compute_round()
        elif action == 'Save Tournament':
            pprint(tournament)
            tournament.update()
        else:
            pass
        return tournament

    @staticmethod
    def view_tournaments_list():
        tournament_list = Tournament.get_list()
        TournamentView.view_list(tournament_list)

    @staticmethod
    def view_tournament_players_by(current_tournament: Tournament,
                                   sort_by: str):
        players_data = []
        for player in current_tournament.players:
            players_data.append(player.__dict__)
        PlayerView.view_list(players_data, sort_by)

    @staticmethod
    def view_tournament_turns(current_tournament: Tournament):
        turn_to_show = TournamentView.choose_active_tournament_turn(current_tournament)
        turn = current_tournament.get_tournament_turn_by_name(turn_to_show)
        TurnView.show_turn(turn)

    @classmethod
    def view_tournament_matches(cls, current_tournament: Tournament):
        all_matches = current_tournament.get_all_match()
        MatchView.show_matches(all_matches)

