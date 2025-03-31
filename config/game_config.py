import json
import os

def load_game_info():
    """
    Load game information from configuration file
    Returns: Dictionary containing all game information
    """
    # Get configuration file path
    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(current_dir, 'games_info.json')
    
    try:
        # Read JSON file
        with open(json_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: Configuration file not found at {json_path}")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in configuration file {json_path}")
        return None

def get_game_info(game_id):
    """
    Get information for a specific game
    Parameters:
        game_id: Game ID (e.g., "game1", "game2")
    Returns: Game information dictionary, or None if not found
    """
    games_data = load_game_info()
    if games_data and 'games' in games_data:
        return games_data['games'].get(game_id)
    return None

def print_game_info(game_id):
    """
    Print information for a specific game
    Parameters:
        game_id: Game ID (e.g., "game1", "game2")
    """
    game_info = get_game_info(game_id)
    if game_info:
        print(f"\nGame Name: {game_info['name']}")
        print(f"Description: {game_info['description']}")
        print("\nHow to Play:")
        for i, step in enumerate(game_info['how_to_play'], 1):
            print(f"{i}. {step}")
    else:
        print(f"Game information not found for {game_id}")

# Test code
if __name__ == "__main__":
    # Print all game information
    games_data = load_game_info()
    if games_data:
        print("Available Games:")
        for game_id in games_data['games']:
            print(f"- {game_id}: {games_data['games'][game_id]['name']}")
        
        # Print detailed information for game1 as an example
        print("\n=== Game 1 Details ===")
        print_game_info("game1") 