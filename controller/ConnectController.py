from model.ConnectModel import ConnectModel
from view.ConnectView import ConnectView


class ConnectController:

    @staticmethod
    def main(args):
        model = ConnectModel(6, 7)
        view = ConnectView()
        while True:
            view.show_board(model.board)
            view.show_turn(model.current_player)
            try:
                if model.make_move(view.show_menu()):
                    if model.check_win() or model.check_draw():
                        view.show_board(model.board)
                        break
                    model.next_player()
            except Exception as e:
                view.show_error(str(e))
        if model.check_win():
            view.show_end_game(model.current_player)
        else:
            view.show_end_game(0)
