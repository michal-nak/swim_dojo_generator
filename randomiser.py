import sys
import requests
from bs4 import BeautifulSoup
import random
import webbrowser

# Tag categories for interactive selection
distance_tags = [
    '0-1000', '1000-2000', '2000-3000', '3000-4000', '4000-5000', '5000+',
    'Mid Distance', 'Distance', 'Short course', 'Open Water', 'Timed Swim'
]

difficulty_tags = [
    'Beginner', 'Intermediate', 'Advanced', 'Easy', 'Hard', 'Insane',
    'Steady State', 'Recovery'
]

style_tags = [
    'Freestyle', 'Backstroke', 'Breaststroke', 'Butterfly', 'IM', 'Stroke',
    'Pull', 'Sprint', 'Technique', 'Triathlon', 'Curreri Workouts'
]


def prompt_for_tag(category, tags):
    """Prompt user to select a tag from a category."""
    print(f"\nSelect a {category} tag (or press Enter to skip):")
    for i, tag in enumerate(tags, 1):
        print(f"  {i}. {tag}")
    choice = input(f"Enter the number for {category} (or press Enter to skip): ").strip()
    if choice.isdigit() and 1 <= int(choice) <= len(tags):
        return tags[int(choice) - 1].lower()
    return None


def open_random_workout(selected_tags=None):
    """
    Open a random workout from swimdojo.com in the default browser.
    
    Args:
        selected_tags: List of tags to filter by. If None or empty, returns any workout.
                      If multiple tags are provided, returns workouts matching ALL tags (intersection).
    
    Returns:
        str: The full URL of the opened workout.
    
    Raises:
        Exception: If no workouts are found or if there's a connection error.
    """
    base_url = 'https://www.swimdojo.com'
    selected_tags = selected_tags or []
    
    # Fetch the archive page
    url = f'{base_url}/archive'
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to load page: {response.status_code}")
    
    soup = BeautifulSoup(response.content, 'html.parser')
    workout_links = []
    
    if selected_tags:
        # Filter workouts by tag intersection
        tag_to_workouts = {}
        found_tags = set()
        
        for group in soup.find_all('li', class_='archive-group'):
            group_link = group.find('a', class_='archive-group-name-link')
            if group_link:
                group_name = group_link.text.strip().lower()
                if group_name in [t.lower() for t in selected_tags]:
                    found_tags.add(group_name)
                    item_list = group.find('ul', class_='archive-item-list')
                    links = set()
                    if item_list:
                        for item in item_list.find_all('a', class_='archive-item-link'):
                            href = item.get('href')
                            if href and href.startswith('/workouts/'):
                                links.add(href)
                    tag_to_workouts[group_name] = links
        
        # Check for missing tags
        missing = set([t.lower() for t in selected_tags]) - found_tags
        if missing:
            raise Exception(f"No archive group(s) found for tag(s): {', '.join(missing)}.")
        
        # Get intersection of all tag workout sets
        sets = list(tag_to_workouts.values())
        if sets:
            workout_links = list(set.intersection(*sets))
    else:
        # Get all workouts if no tags specified
        for group in soup.find_all('li', class_='archive-group'):
            item_list = group.find('ul', class_='archive-item-list')
            if item_list:
                for item in item_list.find_all('a', class_='archive-item-link'):
                    href = item.get('href')
                    if href and href.startswith('/workouts/'):
                        workout_links.append(href)
    
    # Verify we found workouts
    if not workout_links:
        if selected_tags:
            raise Exception(f"No workout links found for tag(s): {', '.join(selected_tags)}.")
        else:
            raise Exception("No workout links found.")
    
    # Select and open a random workout
    random_workout_link = random.choice(workout_links)
    full_workout_link = base_url + random_workout_link
    webbrowser.open(full_workout_link)
    return full_workout_link


def list_available_tags():
    """Fetch and display all available tags from swimdojo.com archive."""
    base_url = 'https://www.swimdojo.com'
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
        print(f"  - {tag}")
    return tags


if __name__ == "__main__":
    """Command-line interface for the workout generator."""
    
    # Handle --tags flag (list available tags)
    if len(sys.argv) > 1 and sys.argv[1].strip().lower() == '--tags':
        list_available_tags()
        sys.exit(0)
    
    # Handle --help flag
    if len(sys.argv) > 1 and sys.argv[1].strip().lower() == '--help':
        print("""
Swim Dojo Workout Generator
============================

Usage: python randomiser.py [TAGS ...] [OPTIONS]

Options:
    --any        Select a completely random workout (ignore all tags)
    --tags       List all available workout tags from swimdojo.com
    --help       Show this help message

Examples:
    python randomiser.py                    # Interactive mode with prompts
    python randomiser.py --any              # Fully random workout
    python randomiser.py Beginner Sprint    # Workout matching both tags
    python randomiser.py "2000-3000" Hard   # Distance + difficulty filter

Notes:
    - Tags are case-insensitive
    - Multiple tags filter by intersection (workouts must have ALL tags)
    - If no arguments provided, you'll be prompted to select categories
""")
        sys.exit(0)
    
    # Handle --any flag (fully random workout)
    if len(sys.argv) > 1 and sys.argv[1].strip().lower() == '--any':
        try:
            result = open_random_workout()
            print(f"\n✓ Opened workout: {result}")
        except Exception as e:
            print(f"\n✗ Error: {e}")
            sys.exit(1)
        sys.exit(0)
    
    # Parse command-line arguments for tags
    selected_tags = [arg.strip() for arg in sys.argv[1:] if not arg.startswith('--')]
    
    # If no tags provided via arguments, prompt interactively
    if not selected_tags:
        print("\nSwim Dojo Workout Generator - Interactive Mode")
        print("=" * 50)
        print("Select categories to filter your workout (or skip any)")
        
        distance = prompt_for_tag('Distance', distance_tags)
        if distance:
            selected_tags.append(distance)
        
        difficulty = prompt_for_tag('Difficulty', difficulty_tags)
        if difficulty:
            selected_tags.append(difficulty)
        
        style = prompt_for_tag('Style', style_tags)
        if style:
            selected_tags.append(style)
    
    # Open the workout
    try:
        result = open_random_workout(selected_tags if selected_tags else None)
        if selected_tags:
            print(f"\n✓ Opened workout with tags: [{', '.join(selected_tags)}]")
        else:
            print(f"\n✓ Opened random workout")
        print(f"   URL: {result}")
    except Exception as e:
        print(f"\n✗ Error: {e}")
        sys.exit(1)
