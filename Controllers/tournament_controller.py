from pprint import pprint

from Views.tournament_view import TournamentView
from Models.tournament import Tournament
from Core.controller import Controller


class TournamentController(Controller):

    def __init__(self):
        super().__init__()
        self.view = TournamentView()
        self.view.clear()
        self.logger.info("TournamentController constructor")

    @staticmethod
    def create_tournament():
        tournament_data = TournamentView.create_tournament_form()
        tournament = Tournament(tournament_data)
        tournament.save_new()
        return tournament

    @staticmethod
    def select_tournament():
        tournaments = Tournament.get_list()
        tournament_name = TournamentView.select_tournament(tournaments)
        tournament = Tournament.find_one_by_name(
            tournament_name['selected_tournament'])
        return tournament

    @classmethod
    def manage_tournament_action(cls, current_tournament):
        action = TournamentView.manage_tournament_action(current_tournament)
        if action == 'Add player':
            pprint(current_tournament)
            pass
        elif action == 'Compute First round':
            pass

        return current_tournament
