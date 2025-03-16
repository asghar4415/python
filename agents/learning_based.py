# this is a program for a Learning-Based Agent

# A game-playing agent plays Tic-Tac-Toe. Initially, it doesn’t know which moves are good. Over time, by playing games and learning from wins/losses, it improves.

# This is a Learning-Based Agent because it:

# Learns from experience.
# Adjusts its behavior using feedback (win/loss).
# Uses Q-Learning (a simple reinforcement learning algorithm).


import random


class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9
        self.current_winner = None

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all(s == letter for s in row):
            return True
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all(s == letter for s in column):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all(s == letter for s in diagonal1):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all(s == letter for s in diagonal2):
                return True
        return False

    def reset(self):
        self.board = [' '] * 9
        self.current_winner = None

    def board_state(self):
        return ''.join(self.board)


class QLearningAgent:
    def __init__(self, alpha=0.5, gamma=0.9, epsilon=0.2):
        self.q_table = {}  # {(state, action): value}
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon

    def get_q(self, state, action):
        return self.q_table.get((state, action), 0.0)

    def choose_action(self, state, available_actions):
        if random.random() < self.epsilon:
            return random.choice(available_actions)
        qs = [self.get_q(state, a) for a in available_actions]
        max_q = max(qs)
        max_actions = [a for a, q in zip(available_actions, qs) if q == max_q]
        return random.choice(max_actions)

    def learn(self, state, action, reward, next_state, next_available):
        old_q = self.get_q(state, action)
        future_qs = [self.get_q(next_state, a)
                     for a in next_available] if next_available else [0]
        max_future_q = max(future_qs)
        new_q = old_q + self.alpha * \
            (reward + self.gamma * max_future_q - old_q)
        self.q_table[(state, action)] = new_q


# Training the agent
game = TicTacToe()
agent = QLearningAgent()

for episode in range(10000):
    game.reset()
    state = game.board_state()
    while True:
        action = agent.choose_action(state, game.available_moves())
        game.make_move(action, 'X')
        next_state = game.board_state()
        if game.current_winner == 'X':
            agent.learn(state, action, 1, next_state, [])
            break
        elif not game.available_moves():
            agent.learn(state, action, 0.5, next_state, [])
            break
        else:
            opponent_move = random.choice(game.available_moves())
            game.make_move(opponent_move, 'O')
            next_state2 = game.board_state()
            if game.current_winner == 'O':
                agent.learn(state, action, -1, next_state2, [])
                break
            else:
                agent.learn(state, action, 0, next_state2,
                            game.available_moves())
                state = next_state2

print("Training complete! The agent has learned to play better.")
