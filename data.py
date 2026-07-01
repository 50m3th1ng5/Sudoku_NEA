def set_difficulty(selected_difficulty):
    difficulty = {
        'easy': 45,
        'medium': 35,
        'hard': 29,
        'expert': 24,
        'extreme': 20,
    }
    return difficulty[selected_difficulty]