def get_ans(player_name: str) -> str:
    """Asks for user's choice of weapon.

    Args:
        player_name: Chosen name of player.

    Returns:
        User's weapon of choice.
    """

    user_option = input(f'{player_name} choose your weapon: ')

    return user_option


def validate(p1_ans: str, p2_ans: str) -> str:
    """Checks the winner of the round.

    Args:
        p1_ans: Player 1's answer.
        p2_ans: Player 2's answer.

    Returns:
        A match result in string format.
    """

    winner = {
        'rock': {
            'rock': 'tie',
            'paper': 'lose',
            'scissors': 'win'
        },
        'paper': {
            'rock': 'win',
            'paper': 'tie',
            'scissors': 'lose'
        },
        'scissors': {
            'rock': 'lose',
            'paper': 'win',
            'scissors': 'tie'
        }
    }

    result = winner[p1_ans][p2_ans]

    return result


def main():
    """Start the show."""

    print("""
    --------------------------------------------
                Starting game...
    --------------------------------------------
          """)

    # Get names
    p1_name = input('Player 1 name: ')
    p2_name = input('Player 2 name: ')

    round_num = 1  # Round tracker
    scores = [0, 0]

    running = True
    while running:

        print(f'\n******** ROUND {round_num} ********\n')

        # Get answer
        p1_ans = get_ans(p1_name)
        p2_ans = get_ans(p2_name)

        # validate answers
        match_result = validate(p1_name, p2_name, p1_ans, p2_ans)

        if match_result == 'win':
            print(f'MATCH RESULT: {p1_name} wins!\n')
            scores[0] += 1

        elif match_result == 'lose':
            print(f'MATCH RESULT: {p2_name} wins!\n')
            scores[1] += 1

        else:
            print('MATCH RESULT: Tie\n')

        # Ask if players want to play again
        end_game = input('Continue? (y/n): ')

        if end_game == 'n':

            if scores[0] > scores[1]:
                print(f'\n{p1_name} WON THE GAME!!')
            elif scores[0] < scores[1]:
                print(f'\n{p2_name} WON THE GAME!!')
            else:
                print('The game was a tie!')

            print(f'{p1_name}\'s score: {scores[0]}')
            print(f'{p2_name}\'s score: {scores[1]}')
            print(f'Total number of rounds: {round_num}')
            print('Thanks for playing!\n')

            running = False

        round_num += 1  # Keeps track of rounds


if __name__ == '__main__':
    main()
