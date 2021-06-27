from pprint import pprint

from Views.TournamentView import TournamentView
from Models.Tournament import Tournament
from Core.Controller import Controller


class TournamentController(Controller):

    def __init__(self):
        super().__init__()
        self.logger.info("TournamentController constructor")

    @staticmethod
    def create_tournament():
        tournament_data = TournamentView.create_tournament_form()
        tournament = Tournament(tournament_data)
        pprint(tournament.__dict__)
        tournament.save()
        return tournament
