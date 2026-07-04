import os
from src.data_loader import DataLoader
from src.visualizer import FootballVisualizer

def main():
    print("🚀 Starting Advanced Football Analytics...\n")
    
    # Paths setup karna
    base_dir = os.path.dirname(os.path.abspath(__file__))
    cups_csv_path = os.path.join(base_dir, 'data', 'raw', 'WorldCups.csv')
    matches_csv_path = os.path.join(base_dir, 'data', 'raw', 'WorldCupMatches.csv')
    players_csv_path = os.path.join(base_dir, 'data', 'raw', 'WorldCupPlayers.csv')
    
    # Data load karna
    loader = DataLoader()
    df_cups = loader.load_cups_data(cups_csv_path)
    df_matches = loader.load_matches_data(matches_csv_path)
    df_players = loader.load_players_data(players_csv_path)
    
    visualizer = FootballVisualizer()
    
    # Graphs generate karna (Eik close karne par agla khulega)
    if df_cups is not None:
        print("\n📊 1/4: Showing Goals Trend Graph...")
        visualizer.plot_goals_trend(df_cups)
        
        print("📊 2/4: Showing Most Wins Graph...")
        visualizer.plot_most_wins(df_cups)
        
    if df_matches is not None:
        print("📊 3/4: Showing Home Team Advantage Graph...")
        visualizer.plot_home_advantage(df_matches)
        
    if df_players is not None:
        print("📊 4/4: Showing Top 10 Goal Scorers Graph...")
        visualizer.plot_top_scorers(df_players)
        
    print("\n✅ All analyses completed! Masterpiece is ready.")

if __name__ == "__main__":
    main()