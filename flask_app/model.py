import json
import os

class Champion:
    def __init__(self, champ_json, detailed=False):
        self.id = champ_json['id']
        self.name = champ_json['name']
        self.title = champ_json['title']
        self.blurb = champ_json['blurb']
        self.image_url = f"https://ddragon.leagueoflegends.com/cdn/14.10.1/img/champion/{champ_json['image']['full']}"

        if detailed:
            # Optional extension if using full data file
            self.tags = champ_json.get('tags', [])
            self.stats = champ_json.get('info', {})  # e.g., difficulty, attack, defense

    def __repr__(self):
        return self.name


class ChampionClient:
    def __init__(self, data_file_path=None):
        # Get default path if none provided
        if data_file_path is None:
            base_dir = os.path.dirname(os.path.dirname(__file__))  # Goes from flask_app/ to FInal_Project/
            data_file_path = os.path.join(base_dir, 'data', 'champions.json')

        with open(data_file_path) as f:
            raw_data = json.load(f)
            self.champion_data = raw_data['data']

    def get_all_champions(self):
        return [Champion(champ) for champ in self.champion_data.values()]

    def search(self, query):
        """Returns a list of Champion objects matching the query."""
        query = query.lower()
        return [
            Champion(champ)
            for champ in self.champion_data.values()
            if query in champ['name'].lower()
        ]
    

    def retrieve_champion_by_id(self, champ_id):
        """Returns a detailed Champion object by internal ID (e.g., 'Ahri')."""
        champ_json = self.champion_data.get(champ_id)
        if not champ_json:
            raise ValueError(f"Champion with id {champ_id} not found.")
        return Champion(champ_json, detailed=True)



# -- Example usage for testing --
if __name__ == '__main__':
    client = ChampionClient()
    results = client.search("aatrox")
    for champ in results:
        print(f"{champ.name} - {champ.title}")
    print(f"Total matches: {len(results)}")

    detailed_champ = client.retrieve_champion_by_id("Aatrox")
    print(f"Blurb length: {len(detailed_champ.blurb)}")
    print("FULL BLURB:")
    print(detailed_champ.blurb)
