import sys
import requests
from bs4 import BeautifulSoup
import random
import webbrowser

distance_tags = [
    '0-1000', '1000-2000', '2000-3000', '3000-4000', '4000-5000', '5000+', 'Mid Distance', 'Distance', 'Short course', 'Open Water', 'Timed Swim'
]
difficulty_tags = [
    'Beginner', 'Intermediate', 'Advanced', 'Easy', 'Hard', 'Insane', 'Steady State', 'Recovery'
]
style_tags = [
    'Freestyle', 'Backstroke', 'Breaststroke', 'Butterfly', 'IM', 'Stroke', 'Pull', 'Sprint', 'Technique', 'Triathlon', 'Curreri Workouts'
]
other_tags = ['No Bases']

def prompt_for_tag(category, tags):
    print(f"Select a {category} tag (or press Enter to skip):")
    for i, tag in enumerate(tags, 1):
        print(f"  {i}. {tag}")
    choice = input(f"Enter the number for {category} (or press Enter to skip): ").strip()
    if choice.isdigit() and 1 <= int(choice) <= len(tags):
        return tags[int(choice)-1].lower()
    return None

def open_random_workout(selected_tags=None):
    base_url = 'https://www.swimdojo.com'
    if selected_tags is None:
        selected_tags = []
    url = f'{base_url}/archive'
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to load page: {response.status_code}")
    soup = BeautifulSoup(response.content, 'html.parser')
    workout_links = []
    if selected_tags:
        tag_to_workouts = {}
        found_tags = set()
        for group in soup.find_all('li', class_='archive-group'):
            group_link = group.find('a', class_='archive-group-name-link')
            if group_link:
                group_name = group_link.text.strip().lower()
                if group_name in selected_tags:
                    found_tags.add(group_name)
                    item_list = group.find('ul', class_='archive-item-list')
                    links = set()
                    if item_list:
                        for item in item_list.find_all('a', class_='archive-item-link'):
                            href = item.get('href')
                            if href and href.startswith('/workouts/'):
                                links.add(href)
                    tag_to_workouts[group_name] = links
        missing = set(selected_tags) - found_tags
        if missing:
            raise Exception(f"No archive group(s) found for tag(s): {', '.join(missing)}.")
        sets = list(tag_to_workouts.values())
        if sets:
            workout_links = list(set.intersection(*sets))
    else:
        for group in soup.find_all('li', class_='archive-group'):
            item_list = group.find('ul', class_='archive-item-list')
            if item_list:
                for item in item_list.find_all('a', class_='archive-item-link'):
                    href = item.get('href')
                    if href and href.startswith('/workouts/'):
                        workout_links.append(href)
    if not workout_links:
        if selected_tags:
            raise Exception(f"No workout links found for tag(s): {', '.join(selected_tags)}.")
        else:
            raise Exception("No workout links found.")
    random_workout_link = random.choice(workout_links)
    full_workout_link = base_url + random_workout_link
    webbrowser.open(full_workout_link)
    return full_workout_link

if __name__ == "__main__":
    base_url = 'https://www.swimdojo.com'
    if len(sys.argv) > 1 and sys.argv[1].strip().lower() == '--tags':
        url = f'{base_url}/archive'
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f"Failed to load page: {response.status_code}")
        soup = BeautifulSoup(response.content, 'html.parser')
        tags = []
        for group in soup.find_all('li', class_='archive-group'):
            group_link = group.find('a', class_='archive-group-name-link')
            if group_link:
                tags.append(group_link.text.strip())
        print("Available workout tags:")
        for tag in tags:
            print(f"- {tag}")
        sys.exit(0)

    if len(sys.argv) > 1 and sys.argv[1].strip().lower() == '--help':
        print("""
Usage: python3 swim_randomiser.py [TAGS ...] [--any] [--list-tags] [--help]

Options:
    TAGS         One or more tags (e.g. Beginner Sprint) to filter workouts. Tags are case-insensitive.
    --any        Ignore tags and select a fully random workout.
    --list-tags  List all available workout tags.
    --help       Show this help message and exit.

If no tags or --any are provided, you will be prompted to select tags by category (Distance, Difficulty, Style).
""")
        sys.exit(0)

    if len(sys.argv) > 1 and sys.argv[1].strip().lower() == '--list-tags':
        url = f'{base_url}/archive'
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f"Failed to load page: {response.status_code}")
        soup = BeautifulSoup(response.content, 'html.parser')
        tags = []
        for group in soup.find_all('li', class_='archive-group'):
            group_link = group.find('a', class_='archive-group-name-link')
            if group_link:
                tags.append(group_link.text.strip())
        print("Available workout tags:")
        for tag in tags:
            print(f"- {tag}")
        sys.exit(0)

    # Accept tags from argv, or prompt if none given
    selected_tags = [arg.strip().lower() for arg in sys.argv[1:] if not arg.startswith('--')]

    # If --any is present, ignore all tags and do a full random workout
    if '--any' in [arg.lower() for arg in sys.argv[1:]]:
        selected_tags = []

    # If no tags provided, prompt interactively
    if not selected_tags:
        distance = prompt_for_tag('Distance', distance_tags)
        if distance:
            selected_tags.append(distance)
        difficulty = prompt_for_tag('Difficulty', difficulty_tags)
        if difficulty:
            selected_tags.append(difficulty)
        style = prompt_for_tag('Style', style_tags)
        if style:
            selected_tags.append(style)

    open_random_workout(selected_tags)
    if selected_tags:
        print(f"Opened workout with tags [{', '.join(selected_tags)}]")
    else:
        print(f"Opened workout.")
