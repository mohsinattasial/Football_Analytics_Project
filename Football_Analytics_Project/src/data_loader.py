import pandas as pd

class DataLoader:
    def load_cups_data(self, file_path):
        try:
            df = pd.read_csv(file_path)
            if 'Attendance' in df.columns:
                df['Attendance'] = df['Attendance'].astype(str).str.replace('.', '', regex=False)
                df['Attendance'] = pd.to_numeric(df['Attendance'], errors='coerce')
            print("✅ WorldCups data loaded successfully!")
            return df
        except FileNotFoundError:
            print(f"❌ Error: '{file_path}' nahi mili.")
            return None

    def load_matches_data(self, file_path):
        try:
            df = pd.read_csv(file_path)
            df = df.dropna(subset=['Home Team Goals', 'Away Team Goals'])
            print("✅ Matches data loaded successfully!")
            return df
        except FileNotFoundError:
            print(f"❌ Error: '{file_path}' nahi mili.")
            return None

    def load_players_data(self, file_path):
        """WorldCupPlayers.csv ko load karta hai."""
        try:
            # DtypeWarning se bachne ke liye low_memory=False use kiya hai
            df = pd.read_csv(file_path, low_memory=False)
            print("✅ Players data loaded successfully!")
            return df
        except FileNotFoundError:
            print(f"❌ Error: '{file_path}' nahi mili. Check karein ke file unzip ho kar raw folder mein hai.")
            return None