import boto3

REGION = "us-east-1"
TABLE_NAME = "Games"

def get_table():
    dynamodb = boto3.resource("dynamodb", region_name=REGION)
    return dynamodb.Table(TABLE_NAME)

def print_game(game):
    title    = game.get("Title", "Unknown Title")
    genre    = game.get("Genre", "Unknown Genre")
    platform = game.get("Platform", "Unknown Platform")
    rating   = game.get("Rating", "No rating")

    print(f"  Title   : {title}")
    print(f"  Genre   : {genre}")
    print(f"  Platform: {platform}")
    print(f"  Rating  : {rating}/10")
    print()

def print_all_games():
    table = get_table()
    response = table.scan()
    items = response.get("Items", [])

    if not items:
        print("No games found.")
        return

    print(f"Found {len(items)} game(s):\n")
    for game in items:
        print_game(game)

def main():
    print("===== My Games Library =====\n")
    print_all_games()

if __name__ == "__main__":
    main()