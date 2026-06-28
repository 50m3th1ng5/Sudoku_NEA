
#Hard coded difficulties
def set_difficulty(selected_difficulty):
    difficulty = {
        'easy': 40,
        'medium': 25,
        'hard': 10,
        'evil': 5,
    }
    return difficulty[selected_difficulty]