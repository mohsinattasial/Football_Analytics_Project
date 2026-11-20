import matplotlib.pyplot as plt
import seaborn as sns

class FootballVisualizer:
    def __init__(self):
        sns.set_theme(style="whitegrid", palette="muted")

    def plot_goals_trend(self, df):
        if df is None: return
        plt.figure(figsize=(12, 5))
        sns.lineplot(x='Year', y='GoalsScored', data=df, marker='o', color='#b22222', linewidth=2.5)
        plt.title('📈 Trend of Total Goals Scored in FIFA World Cups', fontsize=14, fontweight='bold')
        plt.xlabel('Tournament Year', fontsize=12)
        plt.ylabel('Total Goals Scored', fontsize=12)
        plt.xticks(df['Year'], rotation=45)
        plt.tight_layout()
        plt.show()

    def plot_most_wins(self, df):
        if df is None: return
        plt.figure(figsize=(10, 5))
        winner_counts = df['Winner'].value_counts()
        sns.barplot(x=winner_counts.index, y=winner_counts.values, palette='viridis')
        plt.title('🏆 Most FIFA World Cup Victories by Country', fontsize=14, fontweight='bold')
        plt.xlabel('Country', fontsize=12)
        plt.ylabel('Number of Titles', fontsize=12)
        plt.yticks(range(0, max(winner_counts.values) + 2))
        plt.tight_layout()
        plt.show()

    def plot_home_advantage(self, df_matches):
        if df_matches is None: return
        home_wins = (df_matches['Home Team Goals'] > df_matches['Away Team Goals']).sum()
        away_wins = (df_matches['Home Team Goals'] < df_matches['Away Team Goals']).sum()
        draws = (df_matches['Home Team Goals'] == df_matches['Away Team Goals']).sum()
        
        labels = ['Home Team Wins', 'Away Team Wins', 'Draws']
        sizes = [home_wins, away_wins, draws]
        colors = ['#4CAF50', '#F44336', '#2196F3']
        explode = (0.1, 0, 0) 

        plt.figure(figsize=(8, 6))
        plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', 
                shadow=True, startangle=140, textprops={'fontsize': 12, 'fontweight': 'bold'})
        plt.title('🏟️ Home Team Advantage: Match Outcomes', fontsize=16, fontweight='bold')
        plt.tight_layout()
        plt.show()

    def plot_top_scorers(self, df_players):
        """Event column ko parse kar ke top 10 goal scorers nikalta hai."""
        if df_players is None: return
        
        # Missing events ko empty string se fill karna
        df_players['Event'] = df_players['Event'].fillna('')
        
        # String mein 'G' (Goal) kitni dafa aya hai, wo count karna
        # Event strings use tokens such as G12 or G45; counting every letter 'G' is inaccurate.
        # Count goal tokens only (exclude penalty shootout markers and other text).
        df_players['Goals'] = df_players['Event'].str.count(r'(?<![A-Za-z])G\d+(?!\d)')
        
        # Player ke hisaab se total goals sum karna aur top 10 nikalna
        top_scorers = df_players.groupby('Player Name')['Goals'].sum().sort_values(ascending=False).head(10)
        
        plt.figure(figsize=(12, 6))
        sns.barplot(x=top_scorers.values, y=top_scorers.index, palette='rocket')
        plt.title('⚽ Top 10 Goal Scorers in World Cup History', fontsize=16, fontweight='bold')
        plt.xlabel('Total Goals', fontsize=12)
        plt.ylabel('Player Name', fontsize=12)
        plt.tight_layout()
        plt.show()