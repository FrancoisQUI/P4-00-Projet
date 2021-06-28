from pprint import pprint

from Views.TournamentView import TournamentView
from Models.Tournament import Tournament
from Core.Controller import Controller


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
        pprint(tournament.__dict__)
        tournament.save_new()
        return tournament

    @staticmethod
    def select_tournament():
        tournaments = Tournament.get_list(Tournament())
        tournament_name = TournamentView.select_tournament(tournaments)
        tournament = Tournament.find_one_by_name(Tournament(), tournament_name)
        pprint(tournament)
