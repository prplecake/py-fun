import rps

Op = rps.Opponent()

options = ['rock', 'paper', 'scissors']


def test_random():
    i = 0
    while i <= 10:
        Op.randoms()
        assert Op.get_what() in options
        i += 1


def test_game_eval():
    assert rps.eval_game("rock", "rock") == "tie"
    assert rps.eval_game("rock", "paper") == "lose"
    assert rps.eval_game("rock", "scissors") == "win"

    assert rps.eval_game("paper", "rock") == "win"
    assert rps.eval_game("paper", "paper") == "tie"
    assert rps.eval_game("paper", "scissors") == "lose"

    assert rps.eval_game("scissors", "rock") == "lose"
    assert rps.eval_game("scissors", "paper") == "win"
    assert rps.eval_game("scissors", "scissors") == "tie"
